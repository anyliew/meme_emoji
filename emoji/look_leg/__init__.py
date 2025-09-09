from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def look_leg(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((406, 406))
        #头像坐标
        return frame.copy().paste(img, (563, 210), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "look_leg",
    look_leg,
    min_images=1,
    max_images=1,
    keywords=["看看腿"],
    date_created=datetime(2025, 9, 9),
    date_modified=datetime(2025, 9, 9),
)
