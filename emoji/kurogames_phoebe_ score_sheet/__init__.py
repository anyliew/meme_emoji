from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def kurogames_phoebe_score_sheet(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},你这个月评分为0,纯纯的饭桶！"
    try:
        frame.draw_text(
            (50, 50, 740, 280),
            text,
            fill="black",
            max_fontsize=100,
            min_fontsize=35,
            allow_wrap=True,
            lines_align="center",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((140, 140))
        return frame.copy().paste(img, (155, 855), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_phoebe_score_sheet",
    kurogames_phoebe_score_sheet,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["菲比评分表","评分表"],
    date_created=datetime(2025, 5, 24),
    date_modified=datetime(2025, 5, 24),
)
