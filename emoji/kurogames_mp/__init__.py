from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_mp(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
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
    try:
        frame.draw_text(
            (50, 20, 700, 130),
            text,
            max_fontsize=70,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((130, 130))
        img_rotated = img.rotate(25, expand=True)  # 向左旋转18度
        return frame.copy().paste(img_rotated, (300, 2), alpha=True)
    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_mp",
    kurogames_mp,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["鸣批","鸣P","鸣p","鸣潮玩家","鸣潮男"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 3, 7),
    date_modified=datetime(2025, 3, 7),
)
