from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def yes(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name} YES!👍🏻👍🏻"
    try:
        frame.draw_text(
            (295, 817, 980, 936),
            text,
            fill=(0, 0, 0),
            max_fontsize=120,
            min_fontsize=15,
            lines_align="center",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((165, 165))
        return frame.copy().paste(img, (396, 452), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yes",
    yes,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["yes","Yes","YES"],
    date_created=datetime(2025, 8, 19),
    date_modified=datetime(2025, 8, 19),
)
