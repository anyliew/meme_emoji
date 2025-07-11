from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def ai_ace(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"不用了\n我{name}是AI高手\n正在用AI写代码中ing"
    try:
        frame.draw_text(
            (35, 19, 594, 406),
            text,
            fill=(58, 58, 58),
            max_fontsize=100,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((340, 340))
        return frame.copy().paste(img, (600, 77), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "ai_ace",
    ai_ace,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["AI高手","ai高手"],
    date_created=datetime(2025, 7, 11),
    date_modified=datetime(2025, 7, 11),
)
