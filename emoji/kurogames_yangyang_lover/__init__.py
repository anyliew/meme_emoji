from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_yangyang_lover(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "漂泊旅人"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "漂泊旅人" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"这是我念念不忘的漂泊者{name},是秧秧的老公~"
    try:
        frame.draw_text(
            (0, 1443, 1440, 1761),
            text,
            max_fontsize=100,
            min_fontsize=20,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((600, 600))
        return frame.copy().paste(img, (426, 845), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_yangyang_lover",
    kurogames_yangyang_lover,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["秧秧老公"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 10),
    date_modified=datetime(2025, 6, 10),
)
