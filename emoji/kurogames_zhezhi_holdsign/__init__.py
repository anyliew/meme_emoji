from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_zhezhi_holdsign (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    loc = (306, 417)
    padding = 5
    points = ((0, 100), (741, 22), (828, 566), (29, 688))
    size = (550, 400)
    text_img = BuildImage.new("RGBA", size)
    try:
        text_img.draw_text(
            (padding, padding, size[0]-padding*2, size[1]-padding*2),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=30,
            lines_align="center",
            font_families=["FZSJ-QINGCRJ"],
        )
    except ValueError:
        raise TextOverLength(text)
    frame.paste(text_img.perspective(points), loc, alpha=True)
    return frame.save_jpg()


add_meme(
    "kurogames_zhezhi_holdsign",
    kurogames_zhezhi_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["祝你鸣潮玩的开心"],
    keywords=["折枝举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)
