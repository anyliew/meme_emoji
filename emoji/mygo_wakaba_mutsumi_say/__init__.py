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


def mygo_wakaba_mutsumi_say(images, texts: list[str], args: Model):
    text = texts[0]
    
    img_files = [
        "1.png",
        "2.png",
    ]
    
    total_num = len(img_files)
    
    if args.number == 0:
        img_index = random.randint(0, total_num - 1)
    elif 1 <= args.number <= total_num:
        img_index = args.number - 1
    else:
        raise ValueError(f"图片编号错误，请选择 1~{total_num} 或 0（随机）")
    
    frame = BuildImage.open(img_dir / img_files[img_index])
    
    text_areas = [
        (31, 89, 166, 175),
        (40, 48, 192, 139),
    ]
    
    font_params = {
        "fill": (0, 0, 0),
        "allow_wrap": True,
        "max_fontsize": 180,
        "min_fontsize": 10,
        "lines_align": "center",
        "font_families": ["FZShaoEr-M11S"],
    }
    
    try:
        frame.draw_text(
            text_areas[img_index],
            text,
            **font_params
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "mygo_wakaba_mutsumi_say",
    mygo_wakaba_mutsumi_say,
    min_texts=1,
    max_texts=1,
    default_texts=["我从没觉得玩乐队开心过……"],
    keywords=["若叶睦说","睦子米说"],
    args_type=args_type,
    date_created=datetime(2026, 4, 11),
    date_modified=datetime(2026, 4, 13),
)