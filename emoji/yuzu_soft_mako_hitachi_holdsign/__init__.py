from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def yuzu_soft_mako_hitachi_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (50, 309, 474, 598),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=25,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "yuzu_soft_mako_hitachi_holdsign",
    yuzu_soft_mako_hitachi_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["Ciallo～"],
    keywords=["常陸茉子举牌","茉子举牌","常陆茉子举牌"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)