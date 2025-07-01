from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_navia_caspar_persuade(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"我可以对{name} \n 使用『说服』吗?"
    try:
        frame.draw_text(
            (1, 492, 544, 616),
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
        img = imgs[0].convert("RGBA").resize((350, 350))
        return frame.copy().paste(img, (141, 85), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "mihoyo_navia_caspar_persuade",
    mihoyo_navia_caspar_persuade,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["说服"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 7, 1),
    date_modified=datetime(2025, 7, 1),
)
