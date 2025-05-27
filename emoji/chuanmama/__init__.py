from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def chuanmama(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (192, 192, 91, 23),
        (192, 192, 91, 23),

    ]
    for i in range(2):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "chuanmama",
    chuanmama,
    min_images=1,
    max_images=1,
    keywords=["川妈妈"],
    date_created=datetime(2025, 5, 27),
    date_modified=datetime(2025, 5, 27),
)