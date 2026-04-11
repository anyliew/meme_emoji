from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def steal_two(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 处理三个头像
        img0 = imgs[0].convert("RGBA").circle().resize((131, 131))
        img1 = imgs[1].convert("RGBA").circle().resize((140, 140))
        img2 = imgs[2].convert("RGBA").circle().resize((125, 125))

        frame_copy = frame.copy()
        frame_copy.paste(img0, (253, 78), alpha=True, below=True)
        frame_copy.paste(img1, (11, 304), alpha=True, below=True)
        frame_copy.paste(img2, (532, 387), alpha=True, below=True)
        return frame_copy

    return make_png_or_gif(images, make)


add_meme(
    "steal_two",
    steal_two,
    min_images=3,
    max_images=3,
    keywords=["双偷"],
    date_created=datetime(2026, 4, 11),
    date_modified=datetime(2026, 4, 11),
)