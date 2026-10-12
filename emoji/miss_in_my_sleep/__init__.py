from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
img_dir = Path(__file__).parent / "images"
def miss_in_my_sleep(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((250, 250))
        return frame.copy().paste(img, (125, 45), alpha=True)
    return make_png_or_gif(images, make)
add_meme(
    "miss_in_my_sleep",
    miss_in_my_sleep,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["睡梦中想念"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2026, 10, 12),
)
