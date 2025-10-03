from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"

def new_goodnews(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
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
            fill=(255, 223, 0),
            max_fontsize=100,
            min_fontsize=10,
            lines_align="center",
            font_families=["FZXS14"], 
        )
    except ValueError:
        raise TextOverLength(name)

    # 添加第二段文字
    if len(texts) > 1:
        try:
            frame.draw_text(
                (199, 708, 512, 923),  # 调整坐标区域以适应你的模板
                texts[1],
                fill=(255, 215, 0),
                allow_wrap=True,
                max_fontsize=60,
                min_fontsize=10,
                lines_align="center",
                font_families=["FZXS14"], 
            )
        except ValueError:
            raise TextOverLength(texts[1])

    def make(imgs: list[BuildImage]) -> BuildImage:
        #头像尺寸
        img = imgs[0].convert("RGBA").circle().resize((300, 300))
        #头像坐标
        return frame.copy().paste(img, (210, 270), alpha=True, below=True )

    return make_jpg_or_gif(images, make)


add_meme(
    "new_goodnews",
    new_goodnews,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=2,
    keywords=["新喜报"],
    default_texts=["天命之人","喜报传佳讯\n福星高照\n满门庭"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2025, 10, 3),
)
