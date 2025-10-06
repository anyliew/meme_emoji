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
from meme_generator.exception import TextOverLength, MemeFeedback

img_dir = Path(__file__).parent / "images"


help_text = "图片编号，范围为 1~3"


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


def kurogames_verina_holdsign(images, texts: list[str], args: Model):
    text = texts[0]
    
    total_num = 3
    if args.number == 0:
        image = random.choice(["0.png", "1.png", "2.png"])
    elif 1 <= args.number <= total_num:
        image = f"{args.number - 1}.png"
    else:
        raise MemeFeedback(f"图片编号错误，请选择 1~{total_num}")
    
    frame = BuildImage.open(img_dir / image)
    try:
        if image == "0.png":
            frame.draw_text(
                (475, 525, 790, 775),
                text,
                fill=(0, 0, 0),
                allow_wrap=True,
                max_fontsize=120,
                min_fontsize=10,
                lines_align="center",
                font_families=["FZShaoEr-M11S"],
            )
        elif image == "1.png":
            frame.draw_text(
                (345, 730, 645, 960),
                text,
                fill=(0, 0, 0),
                allow_wrap=True,
                max_fontsize=120,
                min_fontsize=10,
                lines_align="center",
                font_families=["FZShaoEr-M11S"],
            )
        else:
            frame.draw_text(
                (50, 650, 710, 760),
                text,
                fill=(0, 0, 0),
                allow_wrap=True,
                max_fontsize=120,
                min_fontsize=10,
                lines_align="center",
                stroke_fill=(255, 255, 255),
                font_families=["FZShaoEr-M11S"],
            )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_png()


add_meme(
    "kurogames_verina_holdsign",
    kurogames_verina_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["希望你开心哦"],
    args_type=args_type,
    keywords=["小维举牌", "维里奈举牌"],
    date_created=datetime(2025, 10, 5),
    date_modified=datetime(2025, 10, 5),
)