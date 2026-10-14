from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (121, 13), (121, 13), (122, 12), (120, 12), (120, 12),
    (120, 12), (120, 12), (120, 12), (121, 12), (124, 13),
    (129, 25), (128, 26), (123, 30), (97, 24), (92, 21),
    (81, 18), (75, 17), (72, 15), (67, 13), (65, 13),
    (62, 13), (60, 13), (60, 13), (59, 13), (58, 14),
    (58, 14), (58, 14), (58, 14), (58, 14), (58, 14),
    (58, 12), (51, 15), (48, 23), (49, 28), (57, 31),
    (75, 27), (94, 23), (102, 21), (113, 17), (115, 17),
    (120, 15), (120, 15), (120, 15)
]

sizes = [(63, 63)] * len(positions)

def nailoong_sidestep(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 43
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
    "nailoong_sidestep",
    nailoong_sidestep,
    min_images=1,
    max_images=1,
    keywords=["闪身步", "奶龙闪身步"],
    date_created=datetime(2026, 10, 14),
    date_modified=datetime(2026, 10, 14),
)