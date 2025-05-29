from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_liuwei_holdsign (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (204, 596, 763, 918),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "mihoyo_liuwei_holdsign",
    mihoyo_liuwei_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["你的声音太尖锐了"],
    keywords=["刘伟举牌","大伟举牌","大伟哥举牌"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)