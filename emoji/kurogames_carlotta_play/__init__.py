from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_carlotta_play(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"无语,拿着{name}\n一边玩去吧"
    try:
        frame.draw_text(
            (0, 1350, 1672, 1726),
            text,
            fill=(0, 0, 0),
            max_fontsize=1500,
            min_fontsize=15,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((290, 340)).rotate(-60, expand=True)
        return frame.copy().paste(img, (1090, 920), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_carlotta_play",
    kurogames_carlotta_play,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["一边玩去吧","一边玩去"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 10, 11),
    date_modified=datetime(2025, 10, 11),
)
