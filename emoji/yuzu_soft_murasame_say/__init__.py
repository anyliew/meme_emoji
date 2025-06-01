from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags


img_dir = Path(__file__).parent / "images"


def yuzu_soft_murasame_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (922, 0, 1275, 659),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "yuzu_soft_murasame_say",
    yuzu_soft_murasame_say,
    min_texts=1,
    max_texts=1,
    default_texts=["非酋，不要再涩涩了"],
    keywords=["丛雨说"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2024, 12, 21),
    date_modified=datetime(2024, 12, 21),
)