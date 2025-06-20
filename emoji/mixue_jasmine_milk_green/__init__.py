from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def mixue_jasmine_milk_green(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        images[1].convert("RGBA").resize((100, 85)), (218, 458), alpha=True,below=True
    ).paste(
        images[0].convert("RGBA").resize((100, 85)), (452, 395), alpha=True,below=True
    )
    return frame.save_jpg()


add_meme(
    "mixue_jasmine_milk_green",
    mixue_jasmine_milk_green,
    min_images=2,
    max_images=2,
    keywords=["茉莉奶绿"],
    date_created=datetime(2025, 6, 20),
    date_modified=datetime(2025, 6, 20),
)
