from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def swimsuit_group_photo(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(
        # 客 右边1830, 436
        images[1].convert("RGBA").circle().resize((480, 480)), (1695, 151), alpha=True
    ).paste(
        #主 左边
        images[0].convert("RGBA").circle().resize((480, 480)), (695, 161), alpha=True
    )
    return frame.save_jpg()


add_meme(
    "swimsuit_group_photo",
    swimsuit_group_photo,
    min_images=2,
    max_images=2,
    keywords=["泳衣合影","比基尼合影"],
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 9, 5),
)
