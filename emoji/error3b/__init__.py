from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif
img_dir = Path(__file__).parent / "images"
def error3b(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((1024, 1024))
        bg = frame.copy()
        bg.paste(img, (0, 0), alpha=True, below=True)
        return bg.circle_corner(200)
    return make_png_or_gif(images, make)
add_meme(
    "error3b",
    error3b,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["30亿error", "三十亿报错"],
    date_created=datetime(2026, 4, 17),
    date_modified=datetime(2026, 4, 17),
)
