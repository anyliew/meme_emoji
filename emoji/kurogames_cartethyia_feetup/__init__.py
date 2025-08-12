from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_cartethyia_feetup(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").resize((120, 120))
        # 向左旋转15°（逆时针旋转）
        img = img.rotate(15, expand=True)
        
        #头像坐标
        return frame.copy().paste(img, (395, 130), alpha=True, below=True ) #411, 147

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_cartethyia_feetup",
    kurogames_cartethyia_feetup,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["卡提希娅抬脚","卡提抬脚"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 12),
    date_modified=datetime(2025, 8, 12),
)
