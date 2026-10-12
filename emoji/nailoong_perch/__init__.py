from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (98, 52), (93, 58), (64, 57), (61, 55), (53, 46),
    (45, 38), (46, 39), (50, 40), (62, 40), (74, 36),
    (95, 31), (99, 22), (107, 21), (113, 23), (109, 24),
    (98, 29), (86, 31), (61, 32), (56, 32), (52, 34),
    (50, 33), (52, 32), (57, 32), (76, 33), (88, 27),
    (108, 20), (127, 24), (136, 26), (155, 38), (148, 40),
    (132, 46), (114, 54), (101, 55), (75, 58), (68, 60),
    (62, 59), (62, 55), (62, 55)
]

sizes = [(63, 63)] * 24 + [(65, 65)] + [(63, 63)] * 13

def nailoong_perch(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 38
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
    "nailoong_perch",
    nailoong_perch,
    min_images=1,
    max_images=1,
    keywords=["趴墩"],
    date_created=datetime(2026, 10, 12),
    date_modified=datetime(2026, 10, 12),
)