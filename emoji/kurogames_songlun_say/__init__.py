from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_songlun_say (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (283, 318, 760, 615),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_songlun_say",
    kurogames_songlun_say,
    min_texts=1,
    max_texts=1,
    default_texts=["鸣潮玩家的声音太尖锐了"],
    keywords=["难道说","松伦说"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 10),
    date_modified=datetime(2025, 6, 10),
)