from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def mihoyo_kuki_shinobu_who(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"\n久岐忍:此人是谁?\n\n旅行者:此人是{name},擅长跳、唱、rap、打篮球\n\n旅行者:是稻妻国两年半不可多得的尤物~\n"
    try:
        frame.draw_text(
            (1, 1023, 2048, 1324),
            text,
            #fill=(255, 255, 255),
            fill=(0, 0, 0),
            max_fontsize=120,
            min_fontsize=15,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((210, 300)).rotate(-11, expand=True)
        return frame.copy().paste(img, (932, 310), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "mihoyo_kuki_shinobu_who",
    mihoyo_kuki_shinobu_who,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["此人是谁","是谁","是谁？","是谁？"],
    date_created=datetime(2025, 9, 30),
    date_modified=datetime(2025, 9, 30),
)
