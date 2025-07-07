from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def doro_dear(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"桃乐丝:{name},你永远是桃乐丝的最爱之人❤️"
    try:
        frame.draw_text(
            (1, 675, 1200, 812),
            text,
            fill=(0, 0, 0),
            max_fontsize=60,
            min_fontsize=15,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((100, 100))
        return frame.copy().paste(img, (576, 529), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "doro_dear",
    doro_dear,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["最爱","doro最爱","Doro最爱","DORO最爱","桃乐丝最爱"],
    date_created=datetime(2025, 7, 7),
    date_modified=datetime(2025, 7, 7),
)
