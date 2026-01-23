from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_phoebe_trumpet(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (0, 0, 1024, 290),
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
    return frame.save_jpg()


add_meme(
    "kurogames_phoebe_trumpet",
    kurogames_phoebe_trumpet,
    min_texts=1,
    max_texts=1,
    default_texts=["岁主在上\n菲比湫比"],
    keywords=["菲比喇叭"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 1, 23),
    date_modified=datetime(2026, 1, 23),
)