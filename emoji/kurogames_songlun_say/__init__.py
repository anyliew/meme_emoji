# 文件: __init__.py
from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage
from pydantic import Field

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
)

img_dir = Path(__file__).parent / "images"

help_text = "图片编号，0=随机选择，1=第一张(1.png)，2=第二张(2.png)"


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


def kurogames_songlun_say(images, texts: list[str], args: Model):
    text = texts[0]

    img_files = ["1.png", "2.png"]
    total_num = len(img_files)

    if args.number == 0:
        img_index = random.randint(0, total_num - 1)
    elif 1 <= args.number <= total_num:
        img_index = args.number - 1
    else:
        raise ValueError(f"图片编号错误，请选择 1~{total_num} 或 0（随机）")

    frame = BuildImage.open(img_dir / img_files[img_index])

    text_areas = [
        (283, 318, 760, 615),
        (280, 185, 942, 545),
    ]

    try:
        frame.draw_text(
            text_areas[img_index],
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)

    return frame.save_jpg()


add_meme(
    "kurogames_songlun_say",
    kurogames_songlun_say,
    min_texts=1,
    max_texts=1,
    default_texts=["我看到弹幕上的好好好……"],
    keywords=["松伦说"],
    tags=MemeTags.wuthering_waves,
    args_type=args_type,
    date_created=datetime(2025, 6, 10),
    date_modified=datetime(2025, 6, 10),
)