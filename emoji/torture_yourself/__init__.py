from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def torture_yourself(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")
    #
    frame.paste(
        #被打人747, 822
        images[1].convert("RGBA").circle().resize((200, 200)), (725, 780), alpha=True
    ).paste(
        #主人70, 283
        images[0].convert("RGBA").resize((400, 400)), (70, 283), alpha=True, below=True
    )
    return frame.save_jpg()


add_meme(
    "torture_yourself",
    torture_yourself,
    min_images=2,
    max_images=2,
    keywords=["折磨自己"],
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 5, 25),
)
