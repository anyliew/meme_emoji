from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def widow(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"祭祀者:安心去吧,{name}桑[さん]\n你最❤️愛の妻子[未亡人]我会好好照顾的\n{name}你去了冥界也要保佑我们"
    try:
        frame.draw_text(
            (3, 877, 925, 1030),
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
        img = imgs[0].convert("RGBA").resize((210, 215))
        img = img.rotate(21, expand=True)
        return frame.copy().paste(img, (162, 200), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "widow",
    widow,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["未亡人"],
    date_created=datetime(2025, 8, 13),
    date_modified=datetime(2025, 8, 13),
)
