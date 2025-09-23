from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mi_leijun_holdsign (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (448, 943, 1598, 1572),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=220,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "mi_leijun_holdsign",
    mi_leijun_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["Are you OK ?"],
    keywords=["雷军举牌"],
    date_created=datetime(2025, 9, 23),
    date_modified=datetime(2025, 9, 23),
)