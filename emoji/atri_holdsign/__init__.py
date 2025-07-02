from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def atri_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (247, 935, 639, 1333),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "atri_holdsign",
    atri_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["请不要忘记我哦……\n请一直,一直记住我哦\n明天,请把我带到伊甸\n我想看见大家的笑容\n我想看到大家开心的表情\n我想学习喜悦"],
    keywords=["亚托莉举牌"],
    tags=MemeTags.atri,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)
