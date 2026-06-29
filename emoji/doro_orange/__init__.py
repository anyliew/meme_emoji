from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
img_dir = Path(__file__).parent / "images"
def doro_orange(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")
    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta
    text = f"桃乐丝:和{name}一起品尝欧润吉真是一种享受\n \n{name}:欧润吉真好吃"
    try:
        frame.draw_text(
            (1, 585, 949, 792),
            text,
            fill=(0, 0, 0),
            max_fontsize=100,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZXS14"],
        )
    except ValueError:
        raise TextOverLength(name)
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((270, 270))
        return frame.copy().paste(img, (588, 65), alpha=True, below=True)
    return make_jpg_or_gif(images, make)
add_meme(
    "doro_orange",
    doro_orange,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["欧润吉","润吉","润橘","橘子","橘","🍊"],
    date_created=datetime(2025, 7, 7),
    date_modified=datetime(2025, 7, 7),
)
