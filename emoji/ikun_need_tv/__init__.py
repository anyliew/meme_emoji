from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def ikun_need_tv(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"坤坤好喜欢{name}\n想要一个{name}❤️~"
    try:
        frame.draw_text(
            (2, 2, 572, 250),
            text,
            fill=(255, 255, 255),
            #allow_wrap=True,
            max_fontsize=50,
            min_fontsize=5,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((518, 488))
        return frame.copy().paste(img, (614, 118), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "ikun_need_tv",
    ikun_need_tv,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["坤坤想要"],
    date_created=datetime(2025, 9, 4),
    date_modified=datetime(2025, 9, 4),
)
