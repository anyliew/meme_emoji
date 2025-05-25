from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def yuzu_soft_murasame_clothes(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    ta = "蔡徐坤"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "蔡徐坤" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name},你好变态,穿我的衣物"
    try:
        frame.draw_text(
            (0, 0, 130, 339),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=100,
            min_fontsize=25,
            lines_align="center",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((140, 140))
        return frame.copy().paste(img, (700, 80), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "yuzu_soft_murasame_clothes",
    yuzu_soft_murasame_clothes,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["丛雨衣服","丛雨衣物"],
    tags=MemeTags.yuzu_soft,
    date_created=datetime(2025, 3, 24),
    date_modified=datetime(2025, 3, 24),
)
