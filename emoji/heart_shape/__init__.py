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

img_dir = Path(__file__).parent / "images"

help_text = "昵称"


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


def heart_shape(images: list[BuildImage], texts: list[str], args: Model):
    frame = BuildImage.open(img_dir / "0.png")
    name = args.name or (
        args.user_infos[0].name if args.user_infos else texts[0]
    )
    try:
        frame.draw_text(
            (180, 93, 1868, 295),
            name,
            fill=(255, 255, 255),
            allow_wrap=True,
            max_fontsize=300,
            min_fontsize=15,
            lines_align="center",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(name)
    return frame.save_png()


add_meme(
    "heart_shape",
    heart_shape,
    min_images=0,
    max_images=0,
    min_texts=1,
    max_texts=1,
    default_texts=["Anyliew"],
    keywords=["爱心形状"],
    args_type=args_type,
    date_created=datetime(2026, 10, 12),
    date_modified=datetime(2026, 10, 14),
)
