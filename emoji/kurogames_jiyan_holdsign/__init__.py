from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_jiyan_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (166, 441, 500, 738),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_jiyan_holdsign",
    kurogames_jiyan_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["气势确有提升，想来你对练兵之道也颇有研究？"],
    keywords=["忌炎举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 12, 5),
    date_modified=datetime(2025, 12, 5),
)