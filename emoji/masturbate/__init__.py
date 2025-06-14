from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def masturbate(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (207, 178, 156, 17),
        (194, 172, 159, 27),

    ]
    for i in range(2):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "masturbate",
    masturbate,
    min_images=1,
    max_images=1,
    keywords=["导","打飞机"],
    date_created=datetime(2025, 5, 27),
    date_modified=datetime(2025, 6, 14),
)