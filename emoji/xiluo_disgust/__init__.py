from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def xiluo_disgust(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    
    SCREEN_X = 0
    SCREEN_Y = 75
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 800

    def make(imgs: list[BuildImage]) -> BuildImage:
        input_img = imgs[0].convert("RGBA")

        screen_aspect_ratio = SCREEN_WIDTH / SCREEN_HEIGHT
        img_aspect_ratio = input_img.width / input_img.height

        if img_aspect_ratio > screen_aspect_ratio:
            new_height = SCREEN_HEIGHT
            new_width = int(new_height * img_aspect_ratio)
            resized_img = input_img.resize((new_width, new_height))
            
            left_crop = (new_width - SCREEN_WIDTH) / 2
            right_crop = new_width - left_crop
            
            final_img = resized_img.crop((left_crop, 0, right_crop, new_height))
            
        else:
            new_width = SCREEN_WIDTH
            new_height = int(new_width / img_aspect_ratio)
            resized_img = input_img.resize((new_width, new_height))
            
            top_crop = (new_height - SCREEN_HEIGHT) / 2
            bottom_crop = new_height - top_crop
            
            final_img = resized_img.crop((0, top_crop, new_width, bottom_crop))

        final_img = final_img.rotate(8, expand=True)

        return frame.copy().paste(final_img, (SCREEN_X, SCREEN_Y), alpha=True, below=True)

    return make_png_or_gif(images, make)


add_meme(
    "xiluo_disgust",
    xiluo_disgust,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["希罗嫌弃", "二阶堂希罗嫌弃"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 10, 5),
    date_modified=datetime(2025, 10, 5),
)
