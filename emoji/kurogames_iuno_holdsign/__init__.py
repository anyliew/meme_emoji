from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_iuno_holdsign(images, texts: list[str], args):
    text = texts[0]
    # 随机选择两张图片中的一张
    image_choice = random.choice(["0.png", "1.png"])
    frame = BuildImage.open(img_dir / image_choice)
    
    try:
        if image_choice == "0.png":
            # 第一张图片的文字坐标
            frame.draw_text(
                (249, 577, 768, 952),  # 第一张图片的文字区域坐标
                text,
                fill=(0, 0, 0),
                allow_wrap=True,
                max_fontsize=120,
                min_fontsize=30,
                lines_align="center",
                font_families=["FZSJ-QINGCRJ"],
            )
        else:
            # 第二张图片的文字坐标
            frame.draw_text(
                (273, 521, 729, 980),  # 第二张图片的文字区域坐标（请根据实际图片调整）
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
    "kurogames_iuno_holdsign",
    kurogames_iuno_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["月相轮转之间，我以我为锚点"],
    keywords=["尤诺举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 3),
    date_modified=datetime(2025, 8, 3),
)