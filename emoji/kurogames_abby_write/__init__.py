from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_abby_write(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (473, 1164, 1671, 1851),
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
    "kurogames_abby_write",
    kurogames_abby_write,
    min_texts=1,
    max_texts=1,
    default_texts=["用新鲜的肉烹饪出的沙丁布卡~\n我是比较老派的七丘口味\n这道菜可以添加适量的辣椒\n但不要学拉古那人加奇怪的酸味酱啊！"],
    keywords=["阿布写信"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 4),
    date_modified=datetime(2025, 7, 4),
)