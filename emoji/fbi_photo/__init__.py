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


def fbi_photo(images: list[BuildImage], texts: list[str], args: Model):
    frame = BuildImage.open(img_dir / "0.png")
    name = args.name or (
        args.user_infos[0].name if args.user_infos else texts[0]
    )
    box = (240, 579, 645, 648)
    frame.draw_rectangle(box, fill=(203, 185, 187))
    try:
        frame.draw_text(
            box,
            name,
            fill=(0, 0, 0),
            max_fontsize=45,
            min_fontsize=20,
            valign="bottom",
            halign="left",
        )
    except ValueError:
        raise TextOverLength(name)
    return frame.save_jpg()


add_meme(
    "fbi_photo",
    fbi_photo,
    min_images=0,
    max_images=0,
    min_texts=1,
    max_texts=1,
    default_texts=["KaedeharaLu"],
    keywords=["fbi", "FBI"],
    args_type=args_type,
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2026, 10, 14),
)
