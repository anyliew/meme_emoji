from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def together_two(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.jpg")
    frame.paste(
        images[1].convert("RGBA").circle().resize((200, 200)), (280, 90), alpha=True
    ).paste(
        images[0].convert("RGBA").circle().resize((200, 200)), (680, 20), alpha=True
    )
    return frame.save_jpg()


add_meme(
    "together_two",
    together_two,
    min_images=2,
    max_images=2,
    keywords=["在一起"],
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 5, 25),
)
