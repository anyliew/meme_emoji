from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage
from pydantic import Field

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
)

img_dir = Path(__file__).parent / "images"

help_text = "图片编号，0=随机选择，1=第一张(0.png)，2=第二张(1.png)，3=第三张(2.jpg)，4=第四张(3.jpg)"


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


def acacia_anan_holdsign(images, texts: list[str], args: Model):
    text = texts[0]
    
    # 定义图片文件列表（包含扩展名）
    img_files = [
        "0.png",  # 索引0
        "1.png",  # 索引1  
        "2.jpg",  # 索引2
        "3.jpg",  # 索引3
    ]
    
    total_num = len(img_files)  # 总共4张图片
    
    # 根据参数选择图片编号
    if args.number == 0:
        img_index = random.randint(0, total_num - 1)  # 随机选择 0-3
    elif 1 <= args.number <= total_num:
        img_index = args.number - 1  # 转换为0-based索引
    else:
        raise ValueError(f"图片编号错误，请选择 1~{total_num} 或 0（随机）")
    
    # 打开对应图片
    frame = BuildImage.open(img_dir / img_files[img_index])
    
    # 为每张图片设置不同的文字区域坐标
    text_areas = [
        (147, 810, 736, 1105),   # 图片0.png的坐标
        (179, 344, 464, 413),    # 图片1.png的坐标
        (150, 470, 400, 600),    # 图片2.jpg的坐标
        (310, 740, 790, 990),    # 图片3.jpg的坐标
    ]
    
    # 设置不同的字体参数
    font_params = [
        {  # 图片0.png
            "fill": (0, 0, 0),
            "allow_wrap": True,
            "max_fontsize": 120,
            "min_fontsize": 30,
            "lines_align": "center",
            "font_families": ["FZShaoEr-M11S"],
        },
        {  # 图片1.png
            "fill": (0, 0, 0),
            "allow_wrap": True,
            "max_fontsize": 120,
            "min_fontsize": 30,
            "lines_align": "center",
            "font_families": ["FZShaoEr-M11S"],
        },
        {  # 图片2.jpg
            "fill": (0, 0, 0),
            "allow_wrap": True,
            "max_fontsize": 120,
            "min_fontsize": 5,
            "lines_align": "left",
            "font_families": ["FZShaoEr-M11S"],
        },
        {  # 图片3.jpg
            "fill": (0, 0, 0),
            "allow_wrap": True,
            "max_fontsize": 120,
            "min_fontsize": 5,
            "lines_align": "left",
            "font_families": ["FZShaoEr-M11S"],
        }
    ]
    
    try:
        frame.draw_text(
            text_areas[img_index],
            text,
            **font_params[img_index]
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "acacia_anan_holdsign",
    acacia_anan_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["快说吾辈可爱"],
    keywords=["安安举牌", "夏目安安举牌"],
    args_type=args_type,  # 添加args_type参数
    date_created=datetime(2025, 10, 27),
    date_modified=datetime(2026, 1, 12),
)