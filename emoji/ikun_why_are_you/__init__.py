from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def ikun_why_are_you(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((120, 120))
        img = img.rotate(-10, expand=True)
        #头像坐标
        return frame.copy().paste(img, (275, 75), alpha=True)
        

    return make_jpg_or_gif(images, make)


add_meme(
    "ikun_why_are_you",
    ikun_why_are_you,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["你干嘛","你干吗"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2024, 7, 26),
)
