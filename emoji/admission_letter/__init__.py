from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def admission_letter(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    # frame.draw_rectangle((102, 195, 500, 217), outline=(255, 0, 0), width=2)
    try:
        frame.draw_text(
            (102, 195, 500, 217),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=16,
            min_fontsize=10,
            valign="top",
            halign="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "admission_letter",
    admission_letter,
    min_texts=1,
    max_texts=1,
    default_texts=["Anyliew"],
    keywords=["录取通知书"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 25),
    date_modified=datetime(2025, 8, 25),
)
