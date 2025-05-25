from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_rover_head(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((1200, 1200))
        img = img.rotate(10, expand=True)
        #头像坐标
        return frame.copy().paste(img, (248, 250), alpha=True,below=True)

    return make_png_or_gif(images, make)


add_meme(
    "kurogames_rover_head",
    kurogames_rover_head,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["漂泊者头像框"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 5, 25),
)
