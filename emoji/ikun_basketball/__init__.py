from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def ikun_basketball(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((250, 250))
        img = img.rotate(10, expand=True)
        #头像坐标
        return frame.copy().paste(img, (322, 129), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "ikun_basketball",
    ikun_basketball,
    min_images=1,
    max_images=1,
    keywords=["篮球","🏀"],
    date_created=datetime(2025, 5, 29),
    date_modified=datetime(2025, 5, 29),
)
