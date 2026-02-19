from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def yuzu_soft_murasame_hug(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA")
    frame = BuildImage.open(img_dir / "0.png")
    frames: list[IMG] = []
    for i in range(0, 360, 10):
        frames.append(
            frame.copy()
            .paste(img.rotate(-i).resize((352, 352)), (117, 429), below=True)
            .image
        )
    return save_gif(frames, 0.05)


add_meme(
    "yuzu_soft_murasame_hug",
    yuzu_soft_murasame_hug,
    min_images=1,
    max_images=1,
    keywords=["丛雨抱"],
    date_created=datetime(2026, 2, 19),
    date_modified=datetime(2026, 2, 19),
)
