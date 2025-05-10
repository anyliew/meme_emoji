from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_phoebe_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (15, 29, 954, 387),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=60,
            min_fontsize=35,
            lines_align="center",
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_phoebe_say",
    kurogames_phoebe_say,
    min_texts=1,
    max_texts=1,
    default_texts=["anyliew,我的主人"],
    keywords=["菲比说"],
    tags=MemeTags.bronya,
    date_created=datetime(2022, 10, 27),
    date_modified=datetime(2023, 3, 30),
)
