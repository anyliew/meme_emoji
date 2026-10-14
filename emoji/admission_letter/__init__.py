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

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]


def admission_letter(images: list[BuildImage], texts: list[str], args: Model):
    name = args.name or texts[0]
    now = datetime.now()
    date_str = f"{MONTHS[now.month - 1]} {now.day} {now.year}"
    text = f"{date_str}\n\nDear {name}"
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (60, 225, 490, 320),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=24,
            min_fontsize=10,
            valign="top",
            halign="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "admission_letter",
    admission_letter,
    min_images=0,
    max_images=0,
    min_texts=1,
    max_texts=1,
    default_texts=["KaedeharaLu"],
    keywords=["录取通知书"],
    args_type=args_type,
    date_created=datetime(2025, 8, 25),
    date_modified=datetime(2026, 10, 14),
)
