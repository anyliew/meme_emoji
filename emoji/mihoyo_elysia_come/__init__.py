from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_elysia_come(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        #男右
        images[1].convert("RGBA").circle().resize((190, 190)), (410, 380), alpha=True,below=True
    ).paste(
        #爱莉希雅左
        images[0].convert("RGBA").circle().resize((130, 130)), (92, 310), alpha=True,below=True
    )
    return frame.save_jpg()


add_meme(
    "mihoyo_elysia_come",
    mihoyo_elysia_come,
    min_images=2,
    max_images=2,
    keywords=["爱莉希雅降临"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 5, 25),
)
