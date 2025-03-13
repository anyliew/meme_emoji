from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def begged_me(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "她"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f""
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
        img = imgs[0].convert("RGBA").circle().resize((1720, 1720))
        # 头像旋转15度（顺时针方向）
        img = img.rotate(-15, expand=True)
        #头像坐标320, 855
        return frame.copy().paste(img, (125, 655), alpha=True, below=True )

    return make_jpg_or_gif(images, make)


add_meme(
    "begged_me",
    begged_me,
    min_images=1,
    max_images=1,
    max_texts=1,
    keywords=["求我"],
    date_created=datetime(2025, 3, 10),
    date_modified=datetime(2025, 3, 10),
)
