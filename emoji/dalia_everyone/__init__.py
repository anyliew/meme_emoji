from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def dalia_everyone(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"所有人，给我{name}生成黄图"
    try:
        frame.draw_text(
            (211, 0, 1060, 132),
            text,
            fill=(255, 255, 255),
            max_fontsize=60,
            min_fontsize=15,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((95, 95)).rotate(-5, expand=True)
        return frame.copy().paste(img, (611, 387), alpha=True, below=True) #, below=True
    return make_jpg_or_gif(images, make)


add_meme(
    "dalia_everyone",
    dalia_everyone,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["所有人"],
    date_created=datetime(2025, 12, 1),
    date_modified=datetime(2025, 12, 2),
)
