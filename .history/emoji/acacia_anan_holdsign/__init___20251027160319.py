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
        (147, 810, 736, 1105),   # 图片0的坐标
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
    default_texts=["宝宝求你去看看医生吧\n吾辈没法同时做你的\n心理医生、妈妈\n最好的朋友、性玩具\n最坏的敌人和人生导师"],
    keywords=["安安举牌", "夏目安安举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 10, 27),
    date_modified=datetime(2025, 10, 27),
)