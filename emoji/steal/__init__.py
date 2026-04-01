from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def steal(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((182, 182))
        #头像坐标
        return frame.copy().paste(img, (24, 42), alpha=True, below=True)

    return make_png_or_gif(images, make)


add_meme(
    "steal",
    steal,
    min_images=1,
    max_images=1,
    keywords=["偷"],
    date_created=datetime(2026, 3, 31),
    date_modified=datetime(2026, 4, 1),
)
