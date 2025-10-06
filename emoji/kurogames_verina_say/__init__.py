from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

import random
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_verina_say(images, texts: list[str], args):
    text = texts[0]
    image = random.choice(["0.png"])
    frame = BuildImage.open(img_dir / image)
    try:
        if image == "0.png":
            frame.draw_text(
                (520, 30, 735, 375),
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
    return frame.save_png()


add_meme(
    "kurogames_verina_say",
    kurogames_verina_say,
    min_texts=1,
    max_texts=1,
    default_texts=["希望你开心哦"],
    keywords=["小维说", "维里奈说"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 10, 5),
    date_modified=datetime(2025, 10, 5),
)