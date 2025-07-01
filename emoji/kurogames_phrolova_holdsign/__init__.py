from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_phrolova_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (286, 490, 506, 739),
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
    "kurogames_phrolova_holdsign",
    kurogames_phrolova_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["让我们一起，完成这场万众期待的演奏。"],
    keywords=["弗洛洛举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 1),
    date_modified=datetime(2025, 7, 1),
)