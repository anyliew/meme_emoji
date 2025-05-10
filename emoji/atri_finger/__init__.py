from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def atri_finger(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    ta = "anyliew"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "anyliew" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},你和夏先生一样笨得可爱"

    try:
        frame.draw_text(
            (0, 588, 1171, 720),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=15,
            lines_align="left",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((300, 300))
        return frame.copy().paste(img, (600, 140), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "atri_finger",
    atri_finger,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["亚托莉指"],
    date_created=datetime(2025, 3, 24),
    date_modified=datetime(2025, 3, 24),
)
