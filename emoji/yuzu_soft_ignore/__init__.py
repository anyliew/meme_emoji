from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

from meme_generator import (
    CommandShortcut,
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
    add_meme,
)

img_dir = Path(__file__).parent / "images"


def yuzu_soft_ignore(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((340, 204))
        #头像坐标
        return frame.copy().paste(img, (95, 42), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yuzu_soft_ignore",
    yuzu_soft_ignore,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["视若无睹"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 12, 1),
    date_modified=datetime(2025, 12, 1),
)