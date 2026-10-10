from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def kurogames_hsin_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (168, 140, 620, 445),
            text,
            fill=(8, 46, 20),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=50,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()
add_meme(
    "kurogames_hsin_say",
    kurogames_hsin_say,
    min_texts=1,
    max_texts=1,
    default_texts=["同赏人间欢喜，共守……灯火长明"],
    keywords=["心月狐说","心说"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 10, 10),
    date_modified=datetime(2026, 10, 10),
)
