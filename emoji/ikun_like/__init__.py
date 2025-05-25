from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"

default_text = "坤坤喜欢这个"


def ikun_like(images: list[BuildImage], texts: list[str], args):
    text = texts[0] if texts else default_text
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (5, frame.height - 60, frame.width - 5, frame.height - 10),
            text,
            max_fontsize=40,
            fill="white",
            stroke_fill="black",
            stroke_ratio=0.06,
        )
    except ValueError:
        raise TextOverLength(text)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((305, 235), keep_ratio=True)
        return frame.copy().paste(img, (106, 72), below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "ikun_like",
    ikun_like,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    default_texts=[default_text],
    keywords=["坤坤喜欢"],
    tags=["ikun","坤坤","真爱粉","喜欢"],
    date_created=datetime(2025, 5, 25),
    date_modified=datetime(2025, 5, 25),
)
