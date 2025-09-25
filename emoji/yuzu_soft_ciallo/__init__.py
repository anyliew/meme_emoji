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


def yuzu_soft_ciallo(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((355, 295))
        #头像坐标
        return frame.copy().paste(img, (364, 363), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yuzu_soft_ciallo",
    yuzu_soft_ciallo,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["ciallo","ciallo~"],
    shortcuts=[
        CommandShortcut(
            key=r"(?i)ciallo",
            args=[],
            humanized="ciallo",
        ),
        CommandShortcut(
            key=r"(?i)ciallo～\(∠・ω< \)⌒[★☆]",
            args=[],
            humanized="ciallo～(∠・ω< )⌒★",
        )
    ],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 9, 5),
    date_modified=datetime(2025, 9, 25),
)