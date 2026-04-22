from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"


def steal_two(images: list[BuildImage], texts: list[str], args):
    frame = BuildImage.open(img_dir / "0.png")
    img0 = images[0].convert("RGBA").circle().resize((131, 131))
    img1 = images[1].convert("RGBA").circle().resize((140, 140))
    img2 = images[2].convert("RGBA").circle().resize((125, 125))
    frame.paste(img0, (253, 78), alpha=True, below=True)
    frame.paste(img1, (11, 304), alpha=True, below=True)
    frame.paste(img2, (532, 387), alpha=True, below=True)
    return frame.save_jpg()


add_meme(
    "steal_two",
    steal_two,
    min_images=3,
    max_images=3,
    keywords=["双偷"],
    date_created=datetime(2026, 4, 11),
    date_modified=datetime(2026, 4, 17),
)