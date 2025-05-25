from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def deer_help(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.jpg")
    frame.paste(
        #人类角色
        images[1].convert("RGBA").circle().resize((180, 180)), (605, 200), alpha=True
    ).paste(
        #鹿头角色
        images[0].convert("RGBA").circle().resize((180, 180)), (300, 190), alpha=True
    )
    return frame.save_jpg()


add_meme(
    "deer_help",
    deer_help,
    min_images=2,
    max_images=2,
    keywords=["帮鹿","帮🦌"],
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 5, 25),
)
