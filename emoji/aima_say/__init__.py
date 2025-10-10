from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def aima_say(images, texts: list[str], args):
    text = texts[0]
    img = random.choice(["0.jpg", "1.jpg"])
    frame = BuildImage.open(img_dir / img)
    
    try:
        if img == "0.jpg":
            frame.draw_text(
                (40, 35, 140, 210),  # 第一张图片的文字区域坐标
                text,
                fill=(0, 0, 0),
                allow_wrap=True,
                max_fontsize=120,
                min_fontsize=5,
                lines_align="left",
                font_families=["FZShaoEr-M11S"],
            )
        elif img == "1.jpg":
            frame.draw_text(
                (360, 10, 490, 200),  # 第二张图片的文字区域坐标
                text,
                fill=(0, 0, 0),
                allow_wrap=True,
                max_fontsize=120,
                min_fontsize=5,
                lines_align="left",
                font_families=["FZShaoEr-M11S"],
            )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "aima_say",
    aima_say,
    min_texts=1,
    max_texts=1,
    default_texts=["何意味？"],
    keywords=["艾玛说", "樱羽艾玛说"],
    date_created=datetime(2025, 10, 5),
    date_modified=datetime(2025, 10, 5),
)