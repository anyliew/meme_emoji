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
help_text = "图片编号，0=随机选择，1=第一张(1.png)，2=第二张(2.png)，...，13=第十三张(13.png)"
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
def kurogames_phoebe_say(images, texts: list[str], args: Model):
    text = texts[0]
    img_files = [
        "1.png",   
        "2.png",   
        "3.png",   
        "4.png",   
        "5.png",   
        "6.png",   
        "7.png",   
        "8.png",   
        "9.png",   
        "10.png",  
        "11.png",  
        "12.png",  
        "13.png",  
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
        (15, 29, 954, 387),   
        (0, 0, 515, 210),     
        (0, 0, 667, 206),     
        (0, 0, 512, 114),     
        (0, 0, 727, 249),     
        (0, 0, 800, 171),     
        (0, 0, 800, 250),     
        (0, 0, 1024, 222),    
        (0, 0, 800, 162),     
        (0, 0, 594, 254),     
        (0, 0, 1024, 217),    
        (0, 0, 361, 147),     
        (0, 0, 626, 149),     
    ]
    try:
        frame.draw_text(
            text_areas[img_index],
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=200,
            min_fontsize=10,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()
add_meme(
    "kurogames_phoebe_say",
    kurogames_phoebe_say,
    min_texts=1,
    max_texts=1,
    default_texts=["菲比啾比"],
    keywords=["菲比说"],
    tags=MemeTags.wuthering_waves,
    args_type=args_type,
    date_created=datetime(2025, 5, 10),
    date_modified=datetime(2026, 2, 16),  
)
