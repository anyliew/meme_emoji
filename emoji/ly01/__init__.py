from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def ly01(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        images[1].convert("RGBA").circle().resize((235, 235)), (933, 251), alpha=True, below=True
    ).paste(
        images[0].convert("RGBA").circle().resize((235, 235)), (272, 243), alpha=True, below=True
    )
    return frame.save_jpg()


add_meme(
    "ly01",
    ly01,
    min_images=2,
    max_images=2,
    keywords=["ly01","ly-1","LY-1","舰载激光武器"],
    date_created=datetime(2025, 9, 4),
    date_modified=datetime(2025, 9, 4),
)
