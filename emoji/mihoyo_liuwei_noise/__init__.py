from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_liuwei_noise(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"正常人{name}"
    try:
        frame.draw_text(
            (333, 320, 547, 347),
            text,
            fill=(0, 0, 0),
            max_fontsize=30,
            min_fontsize=15,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((145, 145)).circle()
        return frame.copy().paste(img, (31, 252), alpha=True ) 
    return make_jpg_or_gif(images, make)


add_meme(
    "mihoyo_liuwei_noise",
    mihoyo_liuwei_noise,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["声音","尖锐的声音"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 12, 30),
    date_modified=datetime(2025, 12, 30),
)
