from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"

AVATAR_SLOTS: list[tuple[int, int, int, int]] = [
    (77, 710, 220, 220),      # 1
    (77, 968, 220, 220),      # 2
    (322, 429, 246, 246),     # 3
    (599, 429, 246, 246),     # 4
    (350, 710, 485, 485),     # 5
    (350, 1255, 215, 215),    # 6
    (620, 1255, 495, 495),    # 7
    (891, 710, 220, 220),     # 8
    (891, 968, 220, 220),     # 9
    (891, 1793, 220, 220),    # 10
    (1163, 429, 500, 500),    # 11
    (1163, 968, 500, 500),    # 12
    (1163, 1508, 247, 247),   # 13
    (1709, 688, 244, 244),    # 14
    (1709, 974, 244, 244),    # 15
]


def heart_shape(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    def make(imgs: list[BuildImage]) -> BuildImage:
        result = frame.copy()
        for i, (x, y, w, h) in enumerate(AVATAR_SLOTS):
            img = imgs[i % len(imgs)].convert("RGBA").square().resize((w, h))
            result.paste(img, (x, y), alpha=True)
        if texts:
            result.draw_text(
                (180, 93, 1868, 295),
                texts[0],
                fill=(255, 255, 255),
                allow_wrap=True,
                max_fontsize=300,
                min_fontsize=15,
                lines_align="center",
                font_families=["FZKaTong-M19S"],
            )
        return result

    return make_png_or_gif(images, make)


add_meme(
    "heart_shape",
    heart_shape,
    min_images=1,
    max_images=15,
    min_texts=0,
    max_texts=1,
    keywords=["爱心形状"],
    date_created=datetime(2026, 10, 12),
    date_modified=datetime(2026, 10, 12),
)