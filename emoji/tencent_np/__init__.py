from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def tencent_np(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")


    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((363, 363))
        return frame.copy().paste(img, (1101, 211), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "tencent_np",
    tencent_np,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["农P","农批"],
    date_created=datetime(2026, 1, 9),
    date_modified=datetime(2026, 1, 9),
)
