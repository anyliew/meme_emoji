from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_phoebe_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (15, 29, 954, 387),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=50,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_phoebe_say",
    kurogames_phoebe_say,
    min_texts=1,
    max_texts=1,
    default_texts=["嘟嘟嘟说什么呢"],
    keywords=["菲比说"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 10),
    date_modified=datetime(2025, 5, 10),
)
