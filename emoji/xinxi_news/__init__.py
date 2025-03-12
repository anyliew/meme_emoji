from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def xinxi_news(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "她"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}"
    #{name}喜报人名字❤️👩‍❤️‍💋‍👨
    try:
        frame.draw_text(
            (235, 615, 478, 659),
            text,
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((300, 300))
        #头像坐标
        return frame.copy().paste(img, (210, 270), alpha=True, below=True )

    return make_jpg_or_gif(images, make)


add_meme(
    "xinxi_news",
    xinxi_news,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["新喜报"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2024, 7, 26),
)
