from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def shipborne_laser_weapons(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 第一个头像尺寸和坐标
        img1 = imgs[0].convert("RGBA").resize((167, 167))
        result = frame.copy().paste(img1, (118, 212), alpha=True, below=True)
        
        # 第二个头像尺寸和坐标（较小，放在不同位置）
        img2 = imgs[0].convert("RGBA").resize((73, 73))
        result = result.paste(img2, (572, 918), alpha=True, below=True)

        return result

    return make_jpg_or_gif(images, make)


add_meme(
    "shipborne_laser_weapons",
    shipborne_laser_weapons,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["舰载激光武器"],
    date_created=datetime(2025, 9, 21),
    date_modified=datetime(2025, 9, 21),
)