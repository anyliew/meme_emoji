from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def kurogames_phoebe_love(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((439, 312), keep_ratio=True)
        return frame.copy().paste(img, (156, 688), alpha=True,below=True)
    return make_png_or_gif(images, make)
add_meme(
    "kurogames_phoebe_love",
    kurogames_phoebe_love,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["菲比爱心"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 10, 14),
    date_modified=datetime(2026, 10, 14),
)
