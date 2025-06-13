from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_phrolova_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (1, 1, 990, 192),
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
    "kurogames_phrolova_say",
    kurogames_phrolova_say,
    min_texts=1,
    max_texts=1,
    default_texts=["怪鸟在鸣啸，时间到了。"],
    keywords=["弗洛洛说"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 13),
    date_modified=datetime(2025, 6, 13),
)
