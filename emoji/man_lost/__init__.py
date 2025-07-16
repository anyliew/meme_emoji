from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def man_lost(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"你们看到了{name}了吗"
    try:
        frame.draw_text(
            (85, 28, 238, 73),
            text,
            fill=(0, 0, 0),
            max_fontsize=100,
            min_fontsize=5,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((113, 113))
        return frame.copy().paste(img, (98, 78), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "man_lost",
    man_lost,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["寻人启事"],
    date_created=datetime(2025, 7, 16),
    date_modified=datetime(2025, 7, 16),
)
