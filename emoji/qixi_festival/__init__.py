from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def qixi_festival(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"农历七月初七 新历8月29日 20:00 \n{name}和派蒙在原神官方直播间过七夕"

    try:
        frame.draw_text(
            (58, 1085, 1330, 1234),
            text,
            fill=(0, 0, 0),
            max_fontsize=100,
            min_fontsize=20,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((370, 370))
        return frame.copy().paste(img, (618, 284), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "qixi_festival",
    qixi_festival,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["七夕和谁过","七夕和谁过?","七夕和谁过？"],
    date_created=datetime(2025, 8, 28),
    date_modified=datetime(2025, 8, 28),
)
