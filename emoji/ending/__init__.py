from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def ending(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        images[1].convert("RGBA").circle().resize((284, 284)), (463, 700), alpha=True, below=True
    ).paste(
        images[0].convert("RGBA").circle().resize((530, 530)), (1516, 880), alpha=True, below=True
    )
    return frame.save_jpg()


add_meme(
    "ending",
    ending,
    min_images=2,
    max_images=2,
    keywords=["下场"],
    date_created=datetime(2026, 5, 17),
    date_modified=datetime(2026, 5, 17),
)
