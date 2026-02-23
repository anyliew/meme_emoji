from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def moria_ruruka_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (210, 714, 656, 985),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=10,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "moria_ruruka_holdsign",
    moria_ruruka_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["变身"],
    keywords=["露露卡举牌","森亚露露卡举牌"],
    date_created=datetime(2026, 2, 23),
    date_modified=datetime(2026, 2, 23),
)