from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def mygo_chihaya_anon_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (80, 74, 315, 219),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=10,
            lines_align="left",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()
add_meme(
    "mygo_chihaya_anon_say",
    mygo_chihaya_anon_say,
    min_texts=1,
    max_texts=1,
    default_texts=["诶？！！！等……等等等，是一辈子喔？"],
    keywords=["千早爱音说"],
    date_created=datetime(2026, 8, 13),
    date_modified=datetime(2026, 8, 13),
)
