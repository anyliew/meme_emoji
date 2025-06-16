from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_lingyang_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (146, 465, 627, 890),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_lingyang_holdsign",
    kurogames_lingyang_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["我叫凌阳，比起我摘下狮头后的这幅模样，可能大家更习惯的，还是那位梅花桩上的“狮首”吧？希望相处之后，你能记住这个原原本本的我呀。"],
    keywords=["凌阳举牌", "雪豹举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 6, 16),
)