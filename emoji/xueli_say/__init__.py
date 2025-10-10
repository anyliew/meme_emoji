from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def xueli_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    
    try:
        frame.draw_text(
            (240, 30, 300, 240),  # 第一张图片的文字区域坐标
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=10,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "xueli_say",
    xueli_say,
    min_texts=1,
    max_texts=1,
    default_texts=["你是高手？"],
    keywords=["雪莉说", "雪梨说", "橘雪莉说"],
    date_created=datetime(2025, 10, 5),
    date_modified=datetime(2025, 10, 5),
)