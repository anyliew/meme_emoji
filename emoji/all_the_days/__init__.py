from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def all_the_days(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        images[1].convert("RGBA").circle().resize((95, 95)), (255, 255), alpha=True
    ).paste(
        images[0].convert("RGBA").circle().resize((95, 95)), (425, 210), alpha=True
    )
    return frame.save_jpg()


add_meme(
    "all_the_days",
    all_the_days,
    min_images=2,
    max_images=2,
    keywords=["一生一世"],
    date_created=datetime(2025, 3, 14),
    date_modified=datetime(2025, 3, 14),
)
