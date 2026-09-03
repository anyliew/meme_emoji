from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (109, 103), (108, 103), (107, 102), (131, 118), (135, 119),
    (135, 117), (130, 115), (127, 112), (127, 112), (126, 112),
    (126, 112), (125, 112), (125, 112), (124, 111), (123, 111),
    (116, 106), (114, 105), (113, 105), (114, 106), (113, 103),
    (113, 103), (113, 104), (113, 106), (114, 105), (114, 105),
    (115, 106), (115, 106), (115, 106), (114, 106), (114, 106),
    (114, 106)
]

positions = [(x - 2, y - 2) for x, y in positions]

sizes = [(60, 60)] * 31

def nailoong_hit(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 31
    for i in range(1, total_frames + 1):
        frame = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        idx = i - 1
        pos = positions[idx]
        size = sizes[idx]
        user_head = user_img.resize(size)
        new_frame.paste(user_head, pos, alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.07)

add_meme(
    "nailoong_hit",
    nailoong_hit,
    min_images=1,
    max_images=1,
    keywords=["奶龙打"],
    date_created=datetime(2026, 7, 13),
    date_modified=datetime(2026, 7, 13),
)