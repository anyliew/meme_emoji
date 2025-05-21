from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def kfc_head(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((450, 450))
        img = img.rotate(10, expand=True)
        #头像坐标
        return frame.copy().paste(img, (140, 140), alpha=True)

    return make_png_or_gif(images, make)


add_meme(
    "kfc_head",
    kfc_head,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["kfc头像","KFC头像","肯德基头像"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2024, 7, 26),
)
