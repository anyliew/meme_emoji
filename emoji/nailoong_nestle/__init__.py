from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [(160, 9)]
sizes = [(120, 120)]

def nailoong_nestle(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 1
    for i in range(total_frames):
        frame = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(frame, (0, 0), alpha=True)
        pos = positions[i]
        size = sizes[i]
        user_head = user_img.resize(size).circle()
        new_frame.paste(user_head, pos, alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.13)

add_meme(
    "nailoong_nestle",
    nailoong_nestle,
    min_images=1,
    max_images=1,
    keywords=["奶龙依偎"],
    date_created=datetime(2026, 10, 10),
    date_modified=datetime(2026, 10, 10),
)