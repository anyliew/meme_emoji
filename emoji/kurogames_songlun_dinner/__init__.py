from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_songlun_dinner(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}:松伦哥\n松伦:{name}\n{name}:今天很开心和你共进晚餐\n松伦:我也很开心和{name}一起享用麦当劳双人套餐"
    try:
        frame.draw_text(
            (1, 1056, 992, 1296),
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
        img = imgs[0].convert("RGBA").resize((245, 245)).circle().rotate(-40, expand=True)
        return frame.copy().paste(img, (175, 108), alpha=True, below=True)
    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_songlun_dinner",
    kurogames_songlun_dinner,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["松伦晚餐","松伦哥晚餐"],
    tags=MemeTags.genshin,
    date_created=datetime(2025, 9, 2),
    date_modified=datetime(2025, 9, 2),
)
