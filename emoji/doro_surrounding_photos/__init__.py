from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def doro_surrounding_photos(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"桃乐丝:我这边里有Doro动漫周边公仔\n桃乐丝:还有{name}的写真~\n桃乐丝:你要吗？"
    try:
        frame.draw_text(
            (1, 1, 1080, 250),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=60,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA")
        
        # 创建frame副本
        result_frame = frame.copy()
        
        # 第一次粘贴：
        img1 = img.resize((123, 109))#.rotate(37.5, expand=True)
        #img1 = img.rotate(10, expand=True)
        result_frame.paste(img1, (860, 1095), alpha=True, below=True)
        
        # 第二次粘贴：
        img2 = img.resize((68, 68))
        result_frame.paste(img2, (864, 1227), alpha=True, below=True)
        
        # 第三次粘贴：
        img3 = img.resize((100, 100)).rotate(-15, expand=True)
        result_frame.paste(img3, (815, 1296), alpha=True, below=True)
        
        return result_frame

    return make_jpg_or_gif(images, make)


add_meme(
    "doro_surrounding_photos",
    doro_surrounding_photos,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["周边写真"],
    date_created=datetime(2025, 9, 13),
    date_modified=datetime(2025, 9, 13),
)