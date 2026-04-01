from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage
from pydantic import Field

from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
    add_meme,
)
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


help_text = "图片模板编号，1~3  可选：1: 财神丛雨，2: 原版丛雨，3: 虎头丛雨，0 为随机"


class Model(MemeArgsModel):
    number: int = Field(0, description=help_text)


args_type = MemeArgsType(
    args_model=Model,
    parser_options=[
        ParserOption(
            names=["-n", "--number"],
            args=[ParserArg(name="number", value="int")],
            help_text=help_text,
        ),
    ],
)


def yuzu_soft_murasame_hug(images: list[BuildImage], texts: list[str], args: Model):
    # 模板配置
    template_config = {
        1: {"file": "1.png", "pos": (20, 146), "size": (118, 118)},
        2: {"file": "2.png", "pos": (23, 185), "size": (156, 156)},
        3: {"file": "3.png", "pos": (24, 188), "size": (156, 156)},
    }

    # 参数处理
    if args.number == 0:
        number = random.randint(1, 3)
    elif args.number in template_config:
        number = args.number
    else:
        raise ValueError(f"图片编号错误，请选择 0~3")

    config = template_config[number]
    frame = BuildImage.open(img_dir / config["file"])

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize(config["size"])
        return frame.copy().paste(img, config["pos"], alpha=True, below=True)

    return make_png_or_gif(images, make)


add_meme(
    "yuzu_soft_murasame_hug",
    yuzu_soft_murasame_hug,
    min_images=1,
    max_images=1,
    args_type=args_type,
    keywords=["丛雨抱"],
    date_created=datetime(2026, 2, 19),
    date_modified=datetime(2026, 4, 1),
)