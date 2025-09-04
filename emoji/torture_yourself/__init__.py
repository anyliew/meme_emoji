from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def torture_yourself(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    #
    frame.paste(
        #被动人
        images[1].convert("RGBA").resize((175, 175)), (722, 752), alpha=True, below=True
    ).paste(
        #主人
        images[0].convert("RGBA").resize((380, 410)), (63, 278), alpha=True, below=True
    )
    return frame.save_jpg()


add_meme(
    "torture_yourself",
    torture_yourself,
    min_images=2,
    max_images=2,
    keywords=["折磨自己"],
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 9, 4),
)
