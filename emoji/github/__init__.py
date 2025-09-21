from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def github(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 第一个头像尺寸和坐标
        img1 = imgs[0].convert("RGBA").resize((125, 125))
        result = frame.copy().paste(img1, (347, 201), alpha=True, below=True)
        
        # 第二个头像尺寸和坐标（较小，放在不同位置）
        img2 = imgs[0].convert("RGBA").resize((125, 125)).rotate(-10, expand=True)
        result = result.paste(img2, (310, 553), alpha=True, below=True)
        
        # 第三个头像尺寸和坐标（更小，放在另一个位置）
        img3 = imgs[0].convert("RGBA").resize((108, 108)).rotate(15, expand=True)
        result = result.paste(img3, (297, 1003), alpha=True, below=True)
        
        return result

    return make_jpg_or_gif(images, make)


add_meme(
    "github",
    github,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["Github", "github"],
    date_created=datetime(2025, 9, 21),
    date_modified=datetime(2025, 9, 21),
)