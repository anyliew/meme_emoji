from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / "images"
def kurogames_xuanling_say(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (168, 140, 620, 445),
            text,
            fill=(9, 47, 20),
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
    "kurogames_xuanling_say",
    kurogames_xuanling_say,
    min_texts=1,
    max_texts=1,
    default_texts=["清风骀荡，侠思飞扬，此身、此剑、皆为守护而生"],
    keywords=["玄翎说"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 10, 10),
    date_modified=datetime(2026, 10, 10),
)
