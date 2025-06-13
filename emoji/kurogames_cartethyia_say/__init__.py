from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_cartethyia_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (1, 1, 874, 393),
            text,
            fill=(72, 44, 41),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_cartethyia_say",
    kurogames_cartethyia_say,
    min_texts=1,
    max_texts=1,
    default_texts=["我不再是那个无力迷茫、只能等待你拯救的少女了，现在的我已能和你并肩而战，为你提供助益了。"],
    keywords=["卡提希娅说","卡提希娅说"],
    date_created=datetime(2025, 6, 13),
    date_modified=datetime(2025, 6, 13),
)