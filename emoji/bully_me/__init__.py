from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags


def bully_me(images, texts: list[str], args):
    text = texts[0]
    
    img = images[0].convert("RGBA")
    
    img = img.resize_width(650)
    img_w, img_h = img.size
    
    display_text = f"当你想对{text}恶语相向时，请注意，屏幕后面的我可是这样的："
    text_height = 50 * (len(display_text) // 15 + 1) + 10
    frame = BuildImage.new("RGBA", (img_w, text_height + img_h), "white")
    
    
    try:
        frame.draw_text(
            (20, 10, img_w - 20, text_height - 10),
            display_text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=40,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(display_text)
    
    frame.paste(img, (0, text_height), alpha=True)
    
    return frame.save_jpg()


add_meme(
    "bully_me",
    bully_me,
    min_images=1,
    max_images=1,
    min_texts=1,
    max_texts=1,
    default_texts=["我"],
    keywords=["恶语相向"],
    date_created=datetime(2025, 10, 11),
    date_modified=datetime(2025, 10, 11),
)