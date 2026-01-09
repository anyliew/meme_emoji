from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def atri_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (25, 166, 114, 284),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "atri_say",
    atri_say,
    min_texts=1,
    max_texts=1,
    default_texts=["好久不见，你长大了呢。"],
    keywords=["亚托莉说"],
    tags=MemeTags.atri,
    date_created=datetime(2026, 1, 9),
    date_modified=datetime(2026, 1, 9),
)
