from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def doro_work_for_you(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},桃乐丝正在努力为你打工赚钱"
    try:
        frame.draw_text(
            (1, 520, 1077, 575),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=60,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA")
        
        # 创建frame副本
        result_frame = frame.copy()
        
        # 第一次粘贴：大小135x135，位置(25, 100)
        img1 = img.resize((170, 170)).rotate(37.5, expand=True)
        #img1 = img.rotate(10, expand=True)
        result_frame.paste(img1, (12, 7), alpha=True, below=True)
        
        # 第二次粘贴：大小80x80，位置(351, 130)
        img2 = img.resize((90, 90)).rotate(-25, expand=True)
        result_frame.paste(img2, (313, 130), alpha=True, below=True)
        
        # 第三次粘贴：大小30x30，位置(63, 465)
        img3 = img.resize((35, 35)).rotate(35, expand=True)
        result_frame.paste(img3, (60, 450), alpha=True, below=True)
        
        return result_frame

    return make_jpg_or_gif(images, make)


add_meme(
    "doro_work_for_you",
    doro_work_for_you,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["为你打工"],
    date_created=datetime(2025, 9, 2),
    date_modified=datetime(2025, 9, 2),
)