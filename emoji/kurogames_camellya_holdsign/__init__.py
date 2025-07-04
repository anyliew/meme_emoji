from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_camellya_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (179, 611, 538, 878),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=10,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_camellya_holdsign",
    kurogames_camellya_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["尽情挣扎，别让我无聊！"],
    keywords=["大傻椿举牌","傻椿举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 4),
    date_modified=datetime(2025, 7, 4),
)