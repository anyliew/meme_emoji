from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_the_shorekeeper_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (155, 455, 462, 698),
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
    "kurogames_the_shorekeeper_holdsign",
    kurogames_the_shorekeeper_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["松伦狗策划太坏了"],
    keywords=["守岸人举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 5),
    date_modified=datetime(2025, 6, 5),
)