from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_hutao_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (196, 736, 739, 943),
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
    "mihoyo_hutao_holdsign",
    mihoyo_hutao_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["嗯哼，太阳出来我晒太阳，月亮出来我晒月亮嘞"],
    keywords=["胡桃举牌"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 7, 1),
    date_modified=datetime(2025, 7, 1),
)