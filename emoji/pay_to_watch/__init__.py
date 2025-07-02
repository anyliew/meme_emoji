from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def pay_to_watch(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"男主:旁边怎么有人傻乎乎站在那里？\n女主:{name}付钱让他站在那付费观看的"
    try:
        frame.draw_text(
            (36, 5, 1051, 141),
            text,
            fill=(0, 0, 0),
            max_fontsize=100,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((185, 185))
        return frame.copy().paste(img, (150, 240), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "pay_to_watch",
    pay_to_watch,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["付费观看"],
    date_created=datetime(2025, 7, 2),
    date_modified=datetime(2025, 7, 2),
)
