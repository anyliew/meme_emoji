from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def adoption(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"请收养{name}"
    try:
        frame.draw_text(
            (96, 585, 521, 782),
            text,
            fill=(57,49,46),
            max_fontsize=100,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((310, 310))
        return frame.copy().paste(img, (293, 90), alpha=True,below=True)

    return make_png_or_gif(images, make)


add_meme(
    "adoption",
    adoption,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["收养"],
    date_created=datetime(2025, 3, 24),
    date_modified=datetime(2025, 3, 24),
)
