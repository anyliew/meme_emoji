from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (86, 83), (94, 1), (90, -2), (81, -3), (63, -3),
    (55, -3), (41, -3), (34, 0), (31, 5), (31, 11),
    (32, 15), (42, 30), (58, 50), (66, 64), (70, 76),
    (71, 88), (73, 90), (78, 92), (88, 93), (92, 95),
    (92, 88), (92, 85), (83, 70), (77, 56), (72, 46),
    (66, 33), (63, 29), (59, 20), (49, 23), (42, 20)
]

sizes = [
    (63, 63), (52, 52), (52, 52), (52, 47), (57, 49),
    (57, 49), (57, 52), (60, 60), (60, 60), (63, 63),
    (63, 63), (63, 63), (63, 63), (63, 63), (55, 55),
    (55, 55), (55, 55), (55, 55), (55, 55), (60, 60),
    (63, 63), (63, 63), (70, 70), (76, 76), (76, 76),
    (79, 79), (86, 86), (86, 86), (93, 93), (93, 93)
]

def nailoong_steady(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = len(positions)
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
    return save_gif(frames, 0.1)

add_meme(
    "nailoong_steady",
    nailoong_steady,
    min_images=1,
    max_images=1,
    keywords=["奶龙扶车", "扶车"],
    date_created=datetime(2026, 11, 21),
    date_modified=datetime(2026, 11, 21),
)