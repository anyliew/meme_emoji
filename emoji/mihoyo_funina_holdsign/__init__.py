from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_funina_holdsign (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (451, 258, 736, 477),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_png()


add_meme(
    "mihoyo_funina_holdsign",
    mihoyo_funina_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["大伟丘，你的声音太尖锐了"],
    keywords=["芙宁娜举牌","芙芙举牌","芙芙酱举牌"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 6, 1),
    date_modified=datetime(2025, 6, 1),
)