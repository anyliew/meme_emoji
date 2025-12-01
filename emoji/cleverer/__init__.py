from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def cleverer(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    
    def make(imgs: list[BuildImage]) -> BuildImage:
        input_img = imgs[0].convert("RGBA")

        SCREEN_X = -60
        SCREEN_Y = 99
        TARGET_WIDTH = 680
        TARGET_HEIGHT = 680
        
        target_ar = TARGET_WIDTH / TARGET_HEIGHT
        img_ar = input_img.width / input_img.height

            
        if img_ar > target_ar:
            new_height = TARGET_HEIGHT
            new_width = int(new_height * img_ar)
            resized = input_img.resize((new_width, new_height))
            left = (new_width - TARGET_WIDTH) // 2
            right = left + TARGET_WIDTH
            final_img = resized.crop((left, 0, right, new_height))
        else:
            new_width = TARGET_WIDTH
            new_height = int(new_width / img_ar)
            resized = input_img.resize((new_width, new_height))
            top = (new_height - TARGET_HEIGHT) // 2
            bottom = top + TARGET_HEIGHT
            final_img = resized.crop((0, top, new_width, bottom))

        result = frame.copy()
        result.paste(final_img, (SCREEN_X, SCREEN_Y), alpha=True, below=True)
        return result

    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta
    else:
        name = "这家伙"
        
    frame.draw_text(
        (40, 845, 1056, 992),
        f"你还能有{name}聪明？",
        max_fontsize=100,
        min_fontsize=20,
        lines_align="center",
        font_families=["FZShaoEr-M11S"],
    )
    
    return make_png_or_gif(images, make)


add_meme(
    "cleverer",
    cleverer,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["比聪明"],
    date_created=datetime(2025, 11, 21),
    date_modified=datetime(2025, 11, 21),
)
