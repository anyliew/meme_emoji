from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_neuvillette_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (104, 53, 307, 460),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=20,
            lines_align="center",
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "mihoyo_neuvillette_say",
    mihoyo_neuvillette_say,
    min_texts=1,
    max_texts=1,
    default_texts=["潮水啊，我已归来"],
    keywords=["那维莱特说","水龙王说"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2026, 1, 12),
    date_modified=datetime(2026, 1, 12),
)