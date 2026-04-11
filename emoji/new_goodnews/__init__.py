from datetime import datetime
from pathlib import Path

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
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"

help_text = "昵称（第一段文字）"


class Model(MemeArgsModel):
    name: str = Field("", description=help_text)


args_type = MemeArgsType(
    args_model=Model,
    parser_options=[
        ParserOption(
            names=["-n", "--name"],
            args=[ParserArg(name="name", value="str")],
            help_text=help_text,
        ),
    ],
)


def new_goodnews(images: list[BuildImage], texts: list[str], args: Model):
    frame = BuildImage.open(img_dir / "0.png")

    # 第一段文字（昵称）：只能通过 -n 参数传入，若未提供则使用默认值
    name = args.name if args.name else "天命之人"
    try:
        frame.draw_text(
            (363, 910, 719, 985),
            name,
            fill=(28,28,28),
            max_fontsize=100,
            min_fontsize=10,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    # 第二段文字（正文）：从 texts[0] 获取（min_texts=1 保证存在）
    text2 = texts[0]
    try:
        frame.draw_text(
            (297, 1055, 775, 1379),
            text2,
            fill=(249, 250, 161),
            allow_wrap=True,
            max_fontsize=60,
            min_fontsize=10,
            lines_align="center",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(text2)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((445, 445))
        return frame.copy().paste(img, (319, 408), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "new_goodnews",
    new_goodnews,
    min_images=1,
    max_images=1,
    min_texts=1,          # 需要一个文本作为第二段文字
    max_texts=1,          # 最多一个
    keywords=["新喜报"],
    default_texts=["喜报传佳讯\n福星高照\n满门庭"],   # 第二段文字的默认值
    args_type=args_type,
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2026, 4, 11),
)