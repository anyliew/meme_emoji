from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def naruto_bagua_seal(images: list[BuildImage], texts, args):
    img = images[0]
    mask = BuildImage.open(img_dir / "0.png").resize(
        (img.width, img.height), keep_ratio=True, inside=True
    )

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA")
        img.paste(mask, alpha=True)
        return img

    return make_png_or_gif(images, make)


add_meme(
    "naruto_bagua_seal",
    naruto_bagua_seal,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["八卦封印"],
    date_created=datetime(2025, 12, 2),
    date_modified=datetime(2025, 12, 2),
)
