from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength


img_dir = Path(__file__).parent / "images"


def naruto_uchiha_itachi_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (778, 572, 1020, 979),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=300,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "naruto_uchiha_itachi_say",
    naruto_uchiha_itachi_say,
    min_texts=1,
    max_texts=1,
    default_texts=["鸣潮牛逼"],
    keywords=["鼬说","宇智波鼬说"],
    date_created=datetime(2026, 1, 9),
    date_modified=datetime(2026, 1, 9),
)