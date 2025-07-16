from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def pregnancy_test (images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((640, 640))
        #头像坐标
        return frame.copy().paste(img, (1, 1), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "pregnancy_test",
    pregnancy_test ,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["验孕棒"],
    date_created=datetime(2025, 7, 16),
    date_modified=datetime(2025, 7, 16),
)
