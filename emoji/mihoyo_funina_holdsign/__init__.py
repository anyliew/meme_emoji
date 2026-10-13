from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def mihoyo_funina_holdsign (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (616, 731, 925, 950),
            text,
            fill=(116, 111, 112),
            allow_wrap=True,
            max_fontsize=200,
            min_fontsize=10,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()
add_meme(
    "mihoyo_funina_holdsign",
    mihoyo_funina_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["真是一派荒芜的景象，让我赐予你们水的恩泽吧！"],
    keywords=["芙宁娜举牌","芙芙举牌","芙芙酱举牌"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 6, 1),
    date_modified=datetime(2026, 10, 13),
)
