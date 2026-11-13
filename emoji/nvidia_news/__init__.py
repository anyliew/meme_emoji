from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def nvidia_news(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"刚刚得知：{name}据报道被提名作为英伟达CEO黄仁勋的潜在继任者。"
    try:
        frame.draw_text(
            (145,130,936,230),
            text,
            fill="black",
            allow_wrap=True,
            max_fontsize=25,
            min_fontsize=20,
            lines_align="left",
            #font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").resize((386, 540), keep_ratio=True)
        return frame.copy().paste(img, (155, 244), alpha=True,below=True)

    return make_png_or_gif(images, make)


add_meme(
    "nvidia_news",
    nvidia_news,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["n卡新闻", "nvidia新闻", "N卡新闻", "Nvidia新闻"],
    date_created=datetime(2026, 11, 13),
    date_modified=datetime(2026, 11, 13),
)
