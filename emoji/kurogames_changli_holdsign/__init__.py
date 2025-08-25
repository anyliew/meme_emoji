import random
from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from pydantic import Field
from meme_generator.tags import MemeTags

from meme_generator import (
    MemeArgsModel,
    MemeArgsType,
    ParserArg,
    ParserOption,
    add_meme,
)
from meme_generator.exception import MemeFeedback, TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


help_text = "图片编号，范围为 1~5"


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


def kurogames_changli_holdsign(images, texts: list[str], args: Model):
    text = texts[0]
    total_num = 5
    if args.number == 0:
        num = random.randint(1, total_num)
    elif 1 <= args.number <= total_num:
        num = args.number
    else:
        raise MemeFeedback(f"图片编号错误，请选择 1~{total_num}")

    params = [
        # 图1：262,850 到 262,950
        ((500, 200), (262, 820), ((0, 0), (500, 0), (500, 200), (0, 200)), 0),
        
        # 图2：360,780 到 360,880，逆时针旋转20度
        ((500, 200), (242, 760), ((0, 0), (500, 0), (500, 200), (0, 200)),-8),
        
        # 图3：262,840 到 262,940
        ((500, 200), (252, 760), ((0, 0), (500, 0), (500, 200), (0, 200)), 0),
        
        # 图4：262,870 到 262,970
        ((500, 200), (252, 760), ((0, 0), (500, 0), (500, 200), (0, 200)), 0),
        
        # 图5：262,830 到 262,930，逆时针旋转20度
        ((500, 200), (252, 800), ((0, 0), (500, 0), (500, 200), (0, 200)),-8),
    ]
    
    size, loc, points, angle = params[num - 1]                   
    frame = BuildImage.open(img_dir / f"changli_{num:02d}.png")
    text_img = BuildImage.new("RGBA", size)
    padding = 10
    try:
        text_img.draw_text(
            (padding, padding, size[0] - padding, size[1] - padding),
            text,
            max_fontsize=120,
            min_fontsize=60,
            allow_wrap=True,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
            fill="#3b0b07",
        )
    except ValueError:
        raise TextOverLength(text)
    
    # 旋转处理
    if angle != 0:
        # 先旋转再透视变换，避免变形
        text_img = text_img.rotate(-angle, expand=True)
    
    frame.paste(text_img.perspective(points), loc, alpha=True)
    return frame.save_png()


add_meme(
    "kurogames_changli_holdsign",
    kurogames_changli_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["弈棋布势之道，如同万物运转"],
    args_type=args_type,
    keywords=["长离举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 25),
    date_modified=datetime(2025, 8, 25),
)