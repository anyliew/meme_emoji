from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def azur_lane_cheshire_thumbs_up(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},你真是一个大聪明\n柴郡为你点个赞👍🏻"
    try:
        frame.draw_text(
            (207, 1, 739, 150),
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
        img = imgs[0].convert("RGBA").circle().resize((230, 230))
        return frame.copy().paste(img, (30, 120), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "azur_lane_cheshire_thumbs_up",
    azur_lane_cheshire_thumbs_up,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["柴郡点赞","柴郡猫点赞"],
    date_created=datetime(2025, 7, 2),
    date_modified=datetime(2025, 7, 2),
)
