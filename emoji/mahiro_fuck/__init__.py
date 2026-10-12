from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
img_dir = Path(__file__).parent / "images"
def mahiro_fuck(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((180, 180))
        return frame.copy().paste(img, (430, 40), alpha=True)
    return make_png_or_gif(images, make)
add_meme(
    "mahiro_fuck",
    mahiro_fuck,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["真寻中指","中指","🖕🏻"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2026, 10, 12),
)
