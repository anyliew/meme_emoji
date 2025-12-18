from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def acacia_anan_holdsign(images, texts: list[str], args):
    text = texts[0]
    
    # 随机选择一张图片
    img_index = random.randint(0, 1)
    frame = BuildImage.open(img_dir / f"{img_index}.png")
    
    # 为每张图片设置不同的文字区域坐标
    text_areas = [
        (147, 810, 736, 1105),   # 图片0的坐标
        (179, 344, 464, 413),   # 图片1的坐标
    ]
    
    try:
        frame.draw_text(
            text_areas[img_index],
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "acacia_anan_holdsign",
    acacia_anan_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["快说吾辈可爱"],
    keywords=["安安举牌", "夏目安安举牌"],
    date_created=datetime(2025, 10, 27),
    date_modified=datetime(2025, 12, 18),
)