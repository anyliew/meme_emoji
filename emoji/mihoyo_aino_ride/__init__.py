from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_aino_ride(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 复制背景图
        result = frame.copy()
        
        # 位置1
        img1 = imgs[0].convert("RGBA").resize((224, 199))
        result.paste(img1, (593, 721), alpha=True, below=True)
        
        # 位置2
        img2 = imgs[0].convert("RGBA").resize((132, 144))
        result.paste(img2, (262, 832), alpha=True, below=True)
        
        # 位置3
        img3 = imgs[0].convert("RGBA").resize((115, 115))
        result.paste(img3, (390, 754), alpha=True, below=True)
        
        # 位置4
        img4 = imgs[0].convert("RGBA").resize((111, 125))
        result.paste(img4, (133, 692), alpha=True, below=True)
        
        return result

    return make_jpg_or_gif(images, make)


add_meme(
    "mihoyo_aino_ride",
    mihoyo_aino_ride,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["爱诺骑"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 12, 2),
    date_modified=datetime(2025, 12, 2),
)