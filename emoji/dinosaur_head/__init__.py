from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def dinosaur_head(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "她"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f""
    #{name}恐龙头
    try:
        frame.draw_text(
            (27, 73, 374, 136),
            text,
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((620, 620))
        return frame.copy().paste(img, (215, 245), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "dinosaur_head",
    dinosaur_head,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["恐龙头"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2024, 7, 26),
)
