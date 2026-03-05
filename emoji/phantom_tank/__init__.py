from datetime import datetime
from pathlib import Path

import numpy as np
from PIL import Image
from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif


def phantom_tank(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    if len(images) < 2:
        raise ValueError("需要至少两张图片作为上层和下层")

    def hollow(image: np.ndarray, mode: int) -> np.ndarray:
        img = image.copy()
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img[i, j, 1] = 255 - img[i, j, 0]
                if (i + j) % 2 == mode:
                    img[i, j, 0] = 0
                    img[i, j, 1] = 0
                else:
                    img[i, j, 0] = mode * 255
        return img

    def make(imgs: list[BuildImage]) -> BuildImage:
        top_pil = imgs[0].convert("RGBA").image
        bottom_pil = imgs[1].convert("RGBA").image

        if top_pil.size != bottom_pil.size:
            bottom_pil = bottom_pil.resize(top_pil.size, Image.LANCZOS)

        top_la = np.array(top_pil.convert("LA"))
        bottom_la = np.array(bottom_pil.convert("LA"))

        top_hollowed = hollow(top_la, mode=1)
        bottom_hollowed = hollow(bottom_la, mode=0)

        out_array = (top_hollowed + bottom_hollowed).astype("uint8")

        out_pil = Image.fromarray(out_array, mode="LA").convert("RGBA")
        return BuildImage(out_pil)

    return make_png_or_gif(images, make)


add_meme(
    "phantom_tank",
    phantom_tank,
    min_images=2,
    max_images=2,
    min_texts=0,
    max_texts=0,
    keywords=["幻影坦克"],
    date_created=datetime(2026, 3, 5),
    date_modified=datetime(2026, 3, 5),
)