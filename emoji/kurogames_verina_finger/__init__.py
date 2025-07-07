from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_verina_finger(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"维里奈:坏消息,{name}抽卡又歪了\n维里奈:好消息,歪的是我的共鸣链😆😁\n维里奈:哈哈哈😆😁"
    try:
        frame.draw_text(
            (1, 1, 1203, 257),
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
        img = imgs[0].convert("RGBA").resize((420, 420))
        return frame.copy().paste(img, (248, 555), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_verina_finger",
    kurogames_verina_finger,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["维里奈指","小维指"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 7),
    date_modified=datetime(2025, 7, 7),
)
