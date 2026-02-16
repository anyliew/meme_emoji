from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def double_happiness(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        images[1].convert("RGBA").circle().resize((522, 522)), (1206, 138), alpha=True
    ).paste(
        images[0].convert("RGBA").circle().resize((536, 536)), (532, 332), alpha=True
    )
    return frame.save_jpg()


add_meme(
    "double_happiness",
    double_happiness,
    min_images=2,
    max_images=2,
    keywords=["双喜"],
    date_created=datetime(2026, 2, 16),
    date_modified=datetime(2026, 2, 16),
)
