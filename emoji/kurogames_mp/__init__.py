from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def kurogames_mp(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((130, 130))
        img_rotated = img.rotate(25, expand=True)  
        return frame.copy().paste(img_rotated, (300, 2), alpha=True)
    return make_png_or_gif(images, make)
add_meme(
    "kurogames_mp",
    kurogames_mp,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["鸣批","鸣P","鸣p","鸣潮玩家","鸣潮男"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 3, 7),
    date_modified=datetime(2026, 10, 12),
)
