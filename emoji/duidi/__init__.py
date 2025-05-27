from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def duidi(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((110, 110)).circle()
    frames: list[IMG] = []
    locs = [
        (92, 75, 22, 6),
        (93, 76, 20, 6),
        (92, 76, 23, 10),
        (92, 76, 22, 5),
        (94, 77, 23, 2),

    ]
    for i in range(5):
        frame = BuildImage.open(img_dir / f"{i}.png")
        w, h, x, y = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)


add_meme(
    "duidi",
    duidi,
    min_images=1,
    max_images=1,
    keywords=["怼地","怼"],
    date_created=datetime(2025, 5, 27),
    date_modified=datetime(2025, 5, 27),
)