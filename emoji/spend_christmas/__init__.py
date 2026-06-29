from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
img_dir = Path(__file__).parent / "images"
def spend_christmas(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta
    text = f"{name}❤️,我们一起过圣诞"
    try:
        frame.draw_text(
            (173, 193, 728, 374),
            text,
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((255, 255))
        return frame.copy().paste(img, (120, 535), alpha=True, below=True)
    return make_jpg_or_gif(images, make)
add_meme(
    "spend_christmas",
    spend_christmas,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["一起圣诞"],
    date_created=datetime(2024, 12, 21),
    date_modified=datetime(2024, 12, 21),
)
