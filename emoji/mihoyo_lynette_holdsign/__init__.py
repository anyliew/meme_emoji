from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_lynette_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (564, 1488, 1330, 1909),
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
    "mihoyo_lynette_holdsign",
    mihoyo_lynette_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["林尼大笨蛋"],
    keywords=["琳妮特举牌"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 5, 26),
    date_modified=datetime(2025, 5, 26),
)