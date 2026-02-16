from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def doro_group_photo(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((407, 407))
        return frame.copy().paste(img, (112, 430), alpha=True,below=True)

    return make_png_or_gif(images, make)


add_meme(
    "doro_group_photo",
    doro_group_photo,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["doro合影","Doro合影","桃乐丝合影"],
    date_created=datetime(2026, 2, 16),
    date_modified=datetime(2026, 2, 16),
)
