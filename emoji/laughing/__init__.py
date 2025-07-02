from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def laughing(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},你真是好搞笑呀🤣😂~"
    try:
        frame.draw_text(
            (1, 1, 1495, 407),
            text,
            fill=(255, 255, 255),
            max_fontsize=100,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((400, 400))
        return frame.copy().paste(img, (1097, 550), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "laughing",
    laughing,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["笑指"],
    date_created=datetime(2025, 7, 2),
    date_modified=datetime(2025, 7, 2),
)
