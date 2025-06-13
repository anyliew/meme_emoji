from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_phoebe_holdsign(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (143, 512, 721, 855),
            text,
            fill=(72, 44, 41),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kurogames_phoebe_holdsign",
    kurogames_phoebe_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["我是隐海修会的教士，菲比。岁主在上，愿你的旅途永远有爱与光明垂耀。"],
    keywords=["菲比举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 13),
    date_modified=datetime(2025, 6, 13),
)