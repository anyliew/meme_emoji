from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def springframe (images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((159, 159))
        #头像坐标
        return frame.copy().paste(img, (23, 28), alpha=True,below=True)

    return make_png_or_gif(images, make)


add_meme(
    "springframe",
    springframe ,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["春日燕归来"],
    date_created=datetime(2026, 4, 17),
    date_modified=datetime(2026, 4, 17),
)
