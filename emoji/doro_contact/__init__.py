from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def doro_contact(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"桃乐丝:{name}同学,这是你的头像照片吗？\n桃乐丝:你长得好帅呀\n桃乐丝:{name},你愿意和我交往在一起吗？\n{name}:我愿意,我愿意\n{name}:桃乐丝,我{name}愿意和你在一起一生一世"
    try:
        frame.draw_text(
            (1, 1, 677, 207),
            text,
            fill=(0, 0, 0),
            max_fontsize=60,
            min_fontsize=15,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((108, 108))
        return frame.copy().paste(img, (145, 278), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "doro_contact",
    doro_contact,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["交往","doro交往","Doro交往","DORO交往","桃乐丝交往"],
    date_created=datetime(2025, 7, 7),
    date_modified=datetime(2025, 7, 7),
)
