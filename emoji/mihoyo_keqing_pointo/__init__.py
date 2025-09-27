from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_keqing_pointo(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"此人「{name}」\n\n拥有我的六个命座\n\n已经是满命了"
    try:
        frame.draw_text(
            (1, 538, 577, 711),
            text,
            fill=(0, 0, 0),
            max_fontsize=60,
            min_fontsize=15,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((230, 290))
        return frame.copy().paste(img, (26, 171), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "mihoyo_keqing_pointo",
    mihoyo_keqing_pointo,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["刻晴指"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 9, 27),
    date_modified=datetime(2025, 9, 27),
)
