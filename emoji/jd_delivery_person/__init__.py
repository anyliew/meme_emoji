from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from PIL import ImageEnhance
from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
img_dir = Path(__file__).parent / "images"
def jd_delivery_person(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta
    text = f"{name}"
    try:
        text_img = BuildImage.new("RGBA", (930 - 353, 2104 - 1710))  
        text_img.draw_text(
            (0, 0, text_img.width, text_img.height),
            text,
            fill=(58, 60, 73),
            allow_wrap=True,
            max_fontsize=60,
            min_fontsize=45,
            lines_align="left",
        )
        text_img = text_img.rotate(-17, expand=True)  
        frame.paste(text_img, (353, 1710), alpha=True)  
    except ValueError:
        raise TextOverLength(name)
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((630, 630))
        enhancer = ImageEnhance.Brightness(img.image)
        img_darkened = enhancer.enhance(0.8)  
        img = BuildImage(img_darkened)
        img = img.rotate(-20, expand=True)
        return frame.copy().paste(img, (420, 1000), alpha=True,below=True)
    return make_jpg_or_gif(images, make)
add_meme(
    "jd_delivery_person",
    jd_delivery_person,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["京东外卖骑手","京东外卖工牌"],
    date_created=datetime(2025, 3, 24),
    date_modified=datetime(2025, 9, 25),
)
