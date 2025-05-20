from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_carlotta_hold_sigh(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (196, 552, 785, 920),
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
    "kurogames_carlotta_hold_sigh",
    kurogames_carlotta_hold_sigh,
    min_texts=1,
    max_texts=1,
    default_texts=["十连三金"],
    keywords=["珂莱塔举牌"],
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)