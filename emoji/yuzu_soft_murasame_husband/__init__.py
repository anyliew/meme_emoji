from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def yuzu_soft_murasame_husband(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((200, 200))
        return frame.copy().paste(img, (160, 40), alpha=True)
    return make_png_or_gif(images, make)
add_meme(
    "yuzu_soft_murasame_husband",
    yuzu_soft_murasame_husband,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["丛雨老公"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2026, 10, 12),
)
