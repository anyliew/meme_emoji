from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def something(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"这{name}是什么东西?\n竟然让人如此着迷"
    try:
        frame.draw_text(
            (117, 0, 845, 190),
            text,
            fill=(0, 0, 0),
            max_fontsize=90,
            min_fontsize=20,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((308, 308))
        return frame.copy().paste(img, (118, 471), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "something",
    something,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["什么东西"],
    date_created=datetime(2026, 1, 12),
    date_modified=datetime(2026, 1, 12),
)
