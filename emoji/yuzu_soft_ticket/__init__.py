from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def yuzu_soft_ticket(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "柚子厨"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}"
    try:
        frame.draw_text(
            (485, 544, 625, 583),
            text,
            max_fontsize=100,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((300,300))
        return frame.copy().paste(img, (72,330), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yuzu_soft_ticket",
    yuzu_soft_ticket,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["准考证"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 6, 7),
    date_modified=datetime(2025, 6, 7),
)
