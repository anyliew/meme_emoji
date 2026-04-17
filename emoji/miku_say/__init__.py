from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def miku_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (845, 230, 2645, 1133),
            text,
            fill=(18, 25, 63),
            allow_wrap=True,
            max_fontsize=1000,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "miku_say",
    miku_say,
    min_texts=1,
    max_texts=1,
    default_texts=["みく！"],
    keywords=["初音说", "初音未来说"],
    date_created=datetime(2026, 4, 16),
    date_modified=datetime(2026, 4, 16),
)
