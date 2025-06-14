from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def naruro_uzumaki_naruto_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (281, 591, 858, 1001),
            text,
            fill=(72, 44, 41),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "naruro_uzumaki_naruto_holdsign",
    naruro_uzumaki_naruto_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["我才不要在这种时候放弃,即使当不成中忍,我也会通过其他的途径成为火影的,这就是我的忍道 "],
    keywords=["鸣人举牌","漩涡鸣人举牌"],
    date_created=datetime(2025, 6, 14),
    date_modified=datetime(2025, 6, 14),
)