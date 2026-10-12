from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def mihoyo_funina_round_head(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((500, 500))
        return frame.copy().paste(img, (68, 68), alpha=True, below=True )
    return make_png_or_gif(images, make)
add_meme(
    "mihoyo_funina_round_head",
    mihoyo_funina_round_head,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["芙芙圆形头像","芙宁娜圆形头像"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 3, 29),
    date_modified=datetime(2026, 10, 12),
)
