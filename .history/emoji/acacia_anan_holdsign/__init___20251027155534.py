from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def acacia_anan_holdsign(images, texts: list[str], args):
    text = texts[0]
    
    # 随机选择一张图片
    img_index = random.randint(0, 2)
    frame = BuildImage.open(img_dir / f"{img_index}.jpg")
    
    # 为每张图片设置不同的文字区域坐标
    text_areas = [
        (313, 548, 623, 902),   # 图片0的坐标
        (272, 477, 723, 812),    # 图片1的坐标
        (339, 611, 717, 891)     # 图片2的坐标
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
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "acacia_anan_holdsign",
    acacia_anan_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["佩洛肚皮空空，灵感快来快来"],
    keywords=["举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 10),
    date_modified=datetime(2025, 8, 10),
)