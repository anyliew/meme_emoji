from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def yuzu_soft_ayachi_nene(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},这是你的照片吗？"
    try:
        frame.draw_text(
            (0, 0, 716, 128),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=20,
            lines_align="left",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((165, 165))
        img = img.rotate(-45, expand=True)
        return frame.copy().paste(img, (500, 410), alpha=True,below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yuzu_soft_ayachi_nene",
    yuzu_soft_ayachi_nene,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["宁宁困惑","绫地宁宁困惑"],
    tags=MemeTags.ayachi,
    date_created=datetime(2025, 3, 24),
    date_modified=datetime(2025, 3, 24),
)
