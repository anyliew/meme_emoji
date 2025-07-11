from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_cartethyia_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (190, 565, 780, 945),
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
    "kurogames_cartethyia_holdsign",
    kurogames_cartethyia_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["一份青枝月桂沙拉谢谢"],
    keywords=["卡提举牌", "卡提希娅举牌", "卡提西亚举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)
