from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def kfc(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((450, 450))
        #头像坐标
        return frame.copy().paste(img, (775, 390), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kfc",
    kfc,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["kfc","KFC","肯德基"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2024, 7, 26),
)
