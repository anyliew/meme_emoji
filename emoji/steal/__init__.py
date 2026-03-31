from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def steal(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA")
    frame = BuildImage.open(img_dir / "0.png")
    frames: list[IMG] = []
    for i in range(0, 360, 10):
        frames.append(
            frame.copy()
            .paste(img.rotate(-i).circle().resize((182, 182)), (24, 42), below=True)
            .image
        )
    return save_gif(frames, 0.05)


add_meme(
    "steal",
    steal,
    min_images=1,
    max_images=1,
    keywords=["偷"],
    date_created=datetime(2026, 3, 31),
    date_modified=datetime(2026, 3, 31),
)
