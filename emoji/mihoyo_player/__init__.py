from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"

def mihoyo_player(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    pil = images[0].image.copy()
    if getattr(pil, "is_animated", False):
        pil.seek(0)
    img = BuildImage(pil.convert("RGBA"))
    img = img.circle().resize((312, 312))
    result = frame.copy().paste(img, (1073, 628), alpha=True, below=True)
    return result.save_jpg()

add_meme(
    "mihoyo_player",
    mihoyo_player,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["二游玩家"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2026, 9, 9),
    date_modified=datetime(2026, 9, 9),
)