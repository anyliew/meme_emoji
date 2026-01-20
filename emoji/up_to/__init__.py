from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def up_to(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((960, 960))
        #头像坐标
        return frame.copy().paste(img, (0, 0), alpha=True, below=True)
        

    return make_jpg_or_gif(images, make)


add_meme(
    "up_to",
    up_to,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["干嘛"],
    date_created=datetime(2026, 1, 20),
    date_modified=datetime(2026, 1, 20),
)
