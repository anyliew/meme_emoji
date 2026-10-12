from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"

def prosperitywish(images, texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs):
        img = imgs[0].convert("RGBA").circle().resize((800, 800))
        return frame.copy().paste(img, (1035, 700), alpha=True)
    return make_png_or_gif(images, make)

add_meme(
    "prosperitywish",
    prosperitywish,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["恭喜发财"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2026, 10, 12),
)
