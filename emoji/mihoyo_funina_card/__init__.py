from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_funina_card (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (361, 274, 1392, 940),
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
    "mihoyo_funina_card",
    mihoyo_funina_card,
    min_texts=1,
    max_texts=1,
    default_texts=["曾经我是戴上假面的演员，只想要掩饰真相…"],
    keywords=["芙芙卡片","芙宁娜卡片","芙芙酱卡片"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 26),
)