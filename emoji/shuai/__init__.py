from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def shuai(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (83, 69, 43, 135),
        (53, 45, 49, 103),
        (53, 44, 138, 100),
        (61, 62, 149, 125),


    ]
    for i in range(4):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "shuai",
    shuai,
    min_images=1,
    max_images=1,
    keywords=["甩"],
    date_created=datetime(2025, 5, 27),
    date_modified=datetime(2025, 5, 27),
)