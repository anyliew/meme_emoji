from datetime import datetime
from typing import List
from PIL import Image, ImageEnhance
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
def miragetank_separate(
    images: List[BuildImage],
    texts: List[str],
    args: MemeArgsModel,
) -> BuildImage:
    """
    分离幻影坦克图片为表图和里图
    :param images: [0] 幻影坦克图片（需为 RGBA PNG）
    :param texts: 可选第一个文本为亮度增强因子（默认 2.0，建议范围 1~6）
    """
    bright_factor = 2.0
    if texts and texts[0].strip():
        try:
            bright_factor = float(texts[0].strip())
            bright_factor = min(max(bright_factor, 0.1), 6.0)  
        except ValueError:
            pass
    tank_img = images[0].convert("RGBA")
    def make(imgs: List[BuildImage]) -> BuildImage:
        current_tank = imgs[0].convert("RGBA")
        white_bg = BuildImage.new("RGBA", current_tank.size, (255, 255, 255, 255))
        black_bg = BuildImage.new("RGBA", current_tank.size, (0, 0, 0, 255))
        white_bg.paste(current_tank, (0, 0), alpha=True)
        black_bg.paste(current_tank, (0, 0), alpha=True)
        black_pil = ImageEnhance.Brightness(black_bg.image).enhance(bright_factor)
        white_rgb = white_bg.convert("RGB")
        black_rgb = BuildImage(black_pil).convert("RGB")
        total_width = white_rgb.width + black_rgb.width
        max_height = max(white_rgb.height, black_rgb.height)
        result = BuildImage.new("RGB", (total_width, max_height), (255, 255, 255))
        result.paste(white_rgb, (0, 0))
        result.paste(black_rgb, (white_rgb.width, 0))
        return result
    return make_png_or_gif(images, make)
add_meme(
    "miragetank_separate",
    miragetank_separate,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["幻影分离", "坦克分离"],
    date_created=datetime(2026, 3, 5),
    date_modified=datetime(2026, 3, 5),
)
