from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from meme_generator import CommandShortcut, MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

IMG_DIR = Path(__file__).parent / "images"
BG_IMAGE = IMG_DIR / "0.png"
PASTE_BOX = (364, 363, 719, 658)
RESIZE_SIZE = (355, 295)

def yuzu_soft_ciallo(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    background = BuildImage.open(BG_IMAGE)
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize(RESIZE_SIZE)
        return background.copy().paste(img, PASTE_BOX[:2], alpha=True, below=True)
    return make_jpg_or_gif(images, make)

add_meme(
    "yuzu_soft_ciallo",
    yuzu_soft_ciallo,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["ciallo", "ciallo~", "ciallo～", "柚子社", "yuzusoft"],
    shortcuts=[
        CommandShortcut(
            key=r"(?i:ciallo)",
            args=[],
            humanized="ciallo",
        ),
        CommandShortcut(
            key=r"(?i:ciallo～\(∠・ω< \)⌒[★☆])",
            args=[],
            humanized="ciallo～(∠・ω< )⌒★",
        ),
    ],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 9, 5),
    date_modified=datetime(2026, 8, 2),
)