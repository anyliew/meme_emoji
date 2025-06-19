from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags


img_dir = Path(__file__).parent / "images"


def yuzu_soft_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (1150, 896, 3024, 1240),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=300,
            min_fontsize=30,
            lines_align="left",
            font_families=["PangMenZhengDao-Cu"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "yuzu_soft_holdsign",
    yuzu_soft_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["不要再涩涩了"],
    keywords=["柚子厨举牌"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2024, 12, 21),
    date_modified=datetime(2024, 12, 21),
)