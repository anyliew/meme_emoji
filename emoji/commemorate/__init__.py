from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def commemorate(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((815, 747), keep_ratio=True)
        img = img.convert("L").convert("RGBA")  # 添加黑白滤镜
        return frame.copy().paste(img, (129, 218), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "commemorate",
    commemorate,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["奠","寄"],
    date_created=datetime(2026, 1, 12),
    date_modified=datetime(2026, 1, 12),
)
