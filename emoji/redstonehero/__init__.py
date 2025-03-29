from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags


img_dir = Path(__file__).parent / "images"


def redstonehero(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (143, 334, 360, 378),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=20,
            min_fontsize=10,
            lines_align="left",
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "redstonehero",
    redstonehero,
    min_texts=1,
    max_texts=1,
    default_texts=["蔡徐坤"],
    keywords=["赤石英雄"],
    date_created=datetime(2025, 3, 28),

    date_modified=datetime(2025, 3, 28),
)