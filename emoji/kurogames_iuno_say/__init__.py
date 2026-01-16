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

help_text = "图片编号，0=随机选择，1=第一张(1.jpg)，2=第二张(2.jpg)"

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


def kurogames_iuno_say(images, texts: list[str], args: Model):
    text = texts[0]
    
    # 定义图片文件列表
    img_files = [
        "1.jpg",  # 索引0
        "2.jpg",  # 索引1
    ]
    
    total_num = len(img_files)  # 总共2张图片
    
    # 根据参数选择图片编号
    if args.number == 0:
        img_index = random.randint(0, total_num - 1)  # 随机选择 0-1
    elif 1 <= args.number <= total_num:
        img_index = args.number - 1  # 转换为0-based索引
    else:
        raise ValueError(f"图片编号错误，请选择 1~{total_num} 或 0（随机）")
    
    # 打开对应图片
    frame = BuildImage.open(img_dir / img_files[img_index])
    
    # 为每张图片设置不同的文字区域坐标
    text_areas = [
        (1, 1, 199, 42),     # 图片1.jpg的坐标
        (0, 0, 1024, 249),   # 图片2.jpg的坐标
    ]
    
    # 设置字体参数
    font_params = {
        "fill": (0, 0, 0),
        "allow_wrap": True,
        "max_fontsize": 180,
        "min_fontsize": 30,
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
    "kurogames_iuno_say",
    kurogames_iuno_say,
    min_texts=1,
    max_texts=1,
    default_texts=["月亮游离世间"],
    keywords=["尤诺说"],
    args_type=args_type,  # 添加args_type参数
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 11),
    date_modified=datetime(2025, 8, 11),
)