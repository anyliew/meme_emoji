from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def yuzu_soft_national_day_plan(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の国庆计划"
    try:
        frame.draw_text(
            (412, 28, 1175, 238),
            text,
            fill=(0, 0, 0),
            max_fontsize=120,
            min_fontsize=15,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((210, 210))
        return frame.copy().paste(img, (152, 28), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yuzu_soft_national_day_plan",
    yuzu_soft_national_day_plan,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["国庆计划","国庆节计划"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 9, 28),
    date_modified=datetime(2025, 9, 28),
)
