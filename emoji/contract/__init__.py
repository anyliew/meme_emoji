from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def contract(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}⭐️💢契约"
    try:
        # 创建一个临时图像来绘制旋转的文本
        text_img = BuildImage.new("RGBA", (200, 100))  # 调整大小以适应文本
        text_img.draw_text(
            (0, 0, text_img.width, text_img.height),
            text,
            fill="black",
            max_fontsize=100,
            min_fontsize=10,
            valign="bottom",
            font_families=["FZKaTong-M19S"],
        )
        # 旋转文本图像7度
        text_img = text_img.rotate(7, expand=True)
        # 将旋转后的文本粘贴到frame上
        frame.paste(text_img, (430, 120), alpha=True)
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((110, 110))
        img = img.rotate(5, expand=True)
        return frame.copy().paste(img, (561, 340), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "contract",
    contract,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["⭐️💢契约","橙喵契约","卖身契"],
    date_created=datetime(2025, 3, 24),
    date_modified=datetime(2025, 3, 24),
)