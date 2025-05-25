from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags


img_dir = Path(__file__).parent / "images"


def yuzu_soft_murasame_blackboard(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (351, 128, 1119, 326),
            text,
            fill=(255, 255, 255),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "yuzu_soft_murasame_blackboard",
    yuzu_soft_murasame_blackboard,
    min_texts=1,
    max_texts=1,
    default_texts=["不要再涩涩了"],
    keywords=["丛雨黑板"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2024, 12, 21),
    date_modified=datetime(2024, 12, 21),
)