from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"

AVATAR_SLOTS: list[tuple[int, int, int, int]] = [
    (323, 73, 242, 241),      # 1
    (599, 73, 242, 241),      # 2
    (1163, 73, 501, 500),     # 3
    (1710, 332, 242, 241),    # 4
    (77, 355, 218, 218),      # 5
    (350, 355, 482, 482),     # 6
    (891, 355, 218, 218),     # 7
    (77, 613, 218, 218),      # 8
    (1163, 613, 501, 499),    # 9
    (891, 619, 218, 217),     # 10
    (1710, 619, 247, 247),    # 11
    (352, 899, 213, 213),     # 12
    (620, 899, 489, 491),     # 13
    (1163, 1153, 242, 241),   # 14
    (891, 1433, 218, 220),    # 15
]


def heart_shape(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        result = frame.copy()
        for i, (x, y, w, h) in enumerate(AVATAR_SLOTS):
            img = imgs[i % len(imgs)].convert("RGBA").square().resize((w, h))
            result.paste(img, (x, y), alpha=True)
        return result

    return make_png_or_gif(images, make)


add_meme(
    "heart_shape",
    heart_shape,
    min_images=1,
    max_images=15,
    min_texts=0,
    max_texts=0,
    keywords=["爱心形状"],
    date_created=datetime(2026, 10, 12),
    date_modified=datetime(2026, 10, 16),
)
