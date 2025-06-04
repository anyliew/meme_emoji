from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags


img_dir = Path(__file__).parent / "images"


def kurogames_gugu_blowfish_small_classes(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (65, 173, 1301, 897),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_gugu_blowfish_small_classes",
    kurogames_gugu_blowfish_small_classes,
    min_texts=1,
    max_texts=1,
    default_texts=["松伦哥,不要再涩涩了"],
    keywords=["咕咕河豚小课堂","小课堂"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 1),
    date_modified=datetime(2025, 6, 1),
)