from datetime import datetime
from pathlib import Path
import re
import random

import numpy as np
from PIL import Image, ImageFilter, ImageChops, ImageDraw
import cv2
from pil_utils import BuildImage, Text2Image
from pydantic import Field
from meme_generator import (
    MemeArgsModel,
    add_meme,
    MemeArgsType,
    ParserArg,
    ParserOption,
)
from meme_generator.exception import MemeFeedback
from meme_generator.utils import make_png_or_gif

# 致谢 itorr/one-last-image 项目 (https://github.com/itorr/one-last-image)
# 致谢 su226/IdhagnBot 项目 提供了部分代码参考

help_text = (
    "线迹模式: 0=随机选择, 1=精细, 2=一般, 3=稍粗, 4=超粗, 5=极粗, 6=浮雕, 7=彩色线稿"
)


class Model(MemeArgsModel):
    number: int = Field(0, description=help_text)
    color: int = Field(1, description="Kiss 彩色渐变: 0=关(铅笔灰度), 1=开")
    shade: int = Field(1, description="调子阴影: 0=关, 1=开")
    denoise: int = Field(1, description="降噪: 0=关, 1=开")
    cover: int = Field(0, description="方形裁剪(专辑封面比例): 0=关, 1=开")
    dark_cut: int = Field(118, description="线迹轻重 80~126")
    shade_limit: int = Field(120, description="调子阈值 20~200")
    light: int = Field(0, description="亮度 -100~100")
    texture: float = Field(0.4, description="铅笔纹理强度 0~1")
    lyric: int = Field(0, description="叠印歌词+专辑封面: 0=关, 1=开")


args_type = MemeArgsType(
    args_model=Model,
    parser_options=[
        ParserOption(
            names=["-n", "--number"],
            args=[ParserArg(name="number", value="int")],
            help_text=help_text,
        ),
        ParserOption(
            names=["--color"],
            args=[ParserArg(name="color", value="int")],
            help_text="Kiss 彩色渐变 0/1",
        ),
        ParserOption(
            names=["--shade"],
            args=[ParserArg(name="shade", value="int")],
            help_text="调子阴影 0/1",
        ),
        ParserOption(
            names=["--denoise"],
            args=[ParserArg(name="denoise", value="int")],
            help_text="降噪 0/1",
        ),
        ParserOption(
            names=["--cover"],
            args=[ParserArg(name="cover", value="int")],
            help_text="方形裁剪 0/1",
        ),
        ParserOption(
            names=["--dark-cut"],
            args=[ParserArg(name="dark_cut", value="int")],
            help_text="线迹轻重 80~126",
        ),
        ParserOption(
            names=["--shade-limit"],
            args=[ParserArg(name="shade_limit", value="int")],
            help_text="调子阈值 20~200",
        ),
        ParserOption(
            names=["--light"],
            args=[ParserArg(name="light", value="int")],
            help_text="亮度 -100~100",
        ),
        ParserOption(
            names=["--texture"],
            args=[ParserArg(name="texture", value="float")],
            help_text="铅笔纹理强度 0~1",
        ),
        ParserOption(
            names=["--lyric"],
            args=[ParserArg(name="lyric", value="int")],
            help_text="叠印歌词+封面 0/1",
        ),
    ],
)


# 卷积核定义
def kernel_average(size: int) -> np.ndarray:
    return np.full((size, size), 1 / size**2)


KERNELS: dict[str, np.ndarray] = {
    "精细": kernel_average(5),
    "一般": kernel_average(7),
    "稍粗": kernel_average(9),
    "超粗": kernel_average(11),
    "极粗": kernel_average(13),
    "浮雕": np.array(
        [
            [1, 1, 1],
            [1, 1, -1],
            [-1, -1, -1],
        ]
    ),
    "线稿(彩色)": kernel_average(5),
}

MODE_MAPPING = {
    1: "精细",
    2: "一般",
    3: "稍粗",
    4: "超粗",
    5: "极粗",
    6: "浮雕",
    7: "线稿(彩色)",
}

SHADE_LIGHT = 108
LIGHT_CUT = 128

_IMAGE_DIR = Path(__file__).parent / "images"
_PENCIL_PATH = _IMAGE_DIR / "pencil-texture.jpg"
_COVER_PATH = _IMAGE_DIR / "One_Last_Kiss.JPG"
_LRC_PATH = _IMAGE_DIR / "one-last-kiss.lrc"


def make_gradient(width: int, height: int, color: bool = True) -> Image.Image:
    """创建 Kiss 风格色彩渐变（纯 numpy 实现，无需 cairo）"""
    if color:
        stops = [
            (0.0, (251, 186, 48)),
            (0.4, (252, 114, 53)),
            (0.6, (252, 53, 78)),
            (0.7, (207, 54, 223)),
            (0.8, (55, 181, 217)),
            (1.0, (62, 182, 218)),
        ]
    else:
        stops = [(0.0, (245, 245, 245)), (1.0, (208, 208, 208))]

    xs = np.arange(width, dtype=np.float64)
    ys = np.arange(height, dtype=np.float64)
    xg, yg = np.meshgrid(xs, ys)
    t = (xg * width + yg * height) / (width * width + height * height)

    pos = np.array([s[0] for s in stops], dtype=np.float64)
    pts = np.array([s[1] for s in stops], dtype=np.float64)

    out = np.empty((height, width, 3), dtype=np.float64)
    for c in range(3):
        out[:, :, c] = np.interp(t.ravel(), pos, pts[:, c]).reshape(height, width)
    return Image.fromarray(out.astype(np.uint8), "RGB")


def make_mask(
    im: Image.Image,
    pencil: Image.Image,
    kernel: np.ndarray,
    dark_cut: int = 118,
    shade_limit: int = 120,
    denoise: bool = True,
    enable_shade: bool = True,
) -> Image.Image:
    """创建图像掩膜"""
    if enable_shade:
        shade = im.point(lambda v: 0 if v > shade_limit else 255, "L")
        shade = shade.filter(ImageFilter.BoxBlur(3))
        shade = ImageChops.multiply(shade, ImageChops.invert(pencil))
        shade = ImageChops.multiply(
            shade, Image.new("L", shade.size, SHADE_LIGHT)
        )
    else:
        shade = Image.new("L", im.size, 0)

    if denoise:
        im = im.filter(ImageFilter.Kernel((3, 3), [1] * 9, 9))

    im_array = np.array(im)
    im1 = Image.fromarray(cv2.filter2D(im_array, -1, kernel))

    im = ImageChops.subtract(im, im1, 1, 128)

    scale = (255 - LIGHT_CUT - dark_cut) / 255
    im = ImageChops.subtract(im, Image.new("L", im.size, dark_cut), scale)

    return ImageChops.lighter(ImageChops.invert(im), shade)


_LYRIC_RE = re.compile(r"^\[(\d+):(\d+(?:\.\d+))\](.+?)(?:「(.+)」)?$")


def _load_lyrics(path: Path) -> list[tuple[float, str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return []
    lyrics: list[tuple[float, str, str]] = []
    for line in text.strip().splitlines():
        m = _LYRIC_RE.match(line.strip())
        if not m:
            continue
        mm, ss, t, cn = m.group(1), m.group(2), m.group(3), m.group(4)
        lyrics.append((int(mm) * 60 + float(ss), t.strip(), cn.strip() if cn else ""))
    return lyrics


LYRICS = _load_lyrics(_LRC_PATH)


def _overlay_lyric(result: BuildImage, w: int, h: int) -> BuildImage:
    lines = [l for l in LYRICS if l[1]]
    if not lines:
        return result
    _, jp, cn = random.choice(lines)

    margin = max(10, int(h * 0.02))
    jp_size = max(16, int(h * 0.045))
    cn_size = max(12, int(h * 0.03))
    jp_img = Text2Image.from_text(
        jp,
        jp_size,
        fill=(255, 255, 255),
        stroke_fill=(15, 15, 15),
        stroke_width=max(1, int(jp_size * 0.06)),
    ).to_image()
    cn_img = (
        Text2Image.from_text(
            cn,
            cn_size,
            fill=(235, 235, 235),
            stroke_fill=(15, 15, 15),
            stroke_width=max(1, int(cn_size * 0.06)),
        ).to_image()
        if cn
        else None
    )

    canvas = result.image.convert("RGBA")
    y = h - margin - jp_img.height - (cn_img.height if cn_img else 0)
    x = margin
    canvas.alpha_composite(jp_img, (x, y))
    if cn_img:
        canvas.alpha_composite(cn_img, (x, y + jp_img.height))

    if _COVER_PATH.exists():
        sz = max(40, int(h * 0.14))
        cover = Image.open(_COVER_PATH).convert("RGBA").resize((sz, sz))
        cx = w - sz - margin
        cy = h - sz - margin
        border = max(2, int(sz * 0.04))
        draw = ImageDraw.Draw(canvas)
        draw.rectangle(
            [cx - border, cy - border, cx + sz + border, cy + sz + border],
            fill=(255, 255, 255, 255),
        )
        canvas.alpha_composite(cover, (cx, cy))

    return BuildImage(canvas.convert("RGB"))


def louvre(images: list[BuildImage], texts: list[str], args: Model):
    if args.number == 0:
        mode_number = random.randint(1, 7)
    elif 1 <= args.number <= 7:
        mode_number = args.number
    else:
        raise MemeFeedback("模式编号错误，请选择 1~7 或 0（随机）")

    mode_name = MODE_MAPPING[mode_number]
    kernel = KERNELS[mode_name]

    if _PENCIL_PATH.exists():
        pencil = BuildImage.open(_PENCIL_PATH).convert("L")
    else:
        pencil = BuildImage.new("L", (100, 100), 255)

    dark_cut = min(126, max(80, args.dark_cut))
    shade_limit = min(200, max(20, args.shade_limit))
    light = min(100, max(-100, args.light))
    texture = min(1.0, max(0.0, args.texture))
    color_on = args.color > 0
    shade_on = args.shade > 0
    denoise_on = args.denoise > 0
    cover_on = args.cover > 0
    lyric_on = args.lyric > 0

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0]
        if cover_on:
            w0, h0 = img.width, img.height
            side = min(w0, h0)
            left, top = (w0 - side) // 2, (h0 - side) // 2
            img = BuildImage(img.image.crop((left, top, left + side, top + side)))

        w, h = img.width, img.height
        l, a = img.convert("LA").image.split()

        if light:
            la = np.asarray(l, np.float64) * (1.0 + light / 100.0)
            l = Image.fromarray(np.clip(la, 0, 255).astype(np.uint8), "L")

        frame = BuildImage.new("L", (w, h), 255)
        frame.image.paste(l, mask=a)

        resized_pencil = pencil.resize((w, h))
        mask = make_mask(
            frame.image,
            resized_pencil.image,
            kernel,
            dark_cut=dark_cut,
            shade_limit=shade_limit,
            denoise=denoise_on,
            enable_shade=shade_on,
        )

        result = BuildImage.new("RGB", (w, h), (255,255,255))
        gradient = make_gradient(w, h, color_on)
        result.image.paste(gradient, (0, 0), mask=mask)

        if texture > 0:
            tex = np.asarray(resized_pencil.image, np.float64)
            tmask = tex > 100
            base = np.asarray(result.image.convert("RGB"), np.float64)
            dark = np.clip(base - 20, 0, 255)
            blended = base * (1 - texture) + dark * texture
            blended = np.where(tmask[..., None], blended, base)
            result = BuildImage(Image.fromarray(blended.astype(np.uint8), "RGB"))

        if lyric_on:
            result = _overlay_lyric(result, w, h)

        return result

    return make_png_or_gif(images, make)


add_meme(
    "louvre",
    louvre,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["卢浮宫"],
    args_type=args_type,
    date_created=datetime(2025, 5, 29),
    date_modified=datetime(2026, 10, 12),
)
