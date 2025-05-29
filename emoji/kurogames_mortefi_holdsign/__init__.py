from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_mortefi_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (56, 286, 202, 473),
            text,
            fill=(255, 255, 255),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_png()


add_meme(
    "kurogames_mortefi_holdsign",
    kurogames_mortefi_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["今汐令尹万岁！"],
    keywords=["莫特斐举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 26),
    date_modified=datetime(2025, 5, 26),
)