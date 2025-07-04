from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_lupa_photo(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((630, 410))
        img = img.rotate(-5, expand=True)
        #头像坐标
        return frame.copy().paste(img, (435, 680), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_lupa_photo",
    kurogames_lupa_photo,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["露帕照片"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 4),
    date_modified=datetime(2025, 7, 4),
)
