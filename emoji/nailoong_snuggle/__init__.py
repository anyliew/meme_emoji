from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (112, 1), (112, 1), (112, 1), (112, 1), (112, 0),
    (111, 0), (106, 0), (104, 0), (97, 0), (92, 0),
    (89, 0), (83, 0), (80, 0), (75, 0), (73, 0),
    (72, 0), (70, 0), (70, -1), (72, 0), (75, 0),
    (80, 0), (85, 0), (95, 0), (99, 0), (106, 0),
    (113, 1), (117, 1), (122, 3), (123, 3), (124, 3),
    (123, 4), (123, 4), (115, 4), (113, 2), (107, 1),
    (99, 0), (97, -1), (86, -2), (81, -2), (77, -2),
    (72, 0), (70, 1), (70, 1), (70, 1), (70, 1),
    (73, 0), (77, 0), (83, -1), (91, -2), (97, -1),
    (108, 0), (115, 0), (116, 0), (123, 2), (126, 3),
    (128, 4), (128, 4), (126, 5), (117, 3), (114, 2),
    (110, 0), (99, 0), (96, -1), (88, -1), (81, -1),
    (79, -1), (72, -1), (70, 0), (68, 1), (66, 2),
    (66, 2), (66, 2), (69, 2), (73, 0), (77, 0)
]

sizes = [
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (93, 93), (93, 93), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 90), (91, 90), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (93, 93), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91),
    (91, 91), (91, 91), (91, 91), (91, 91), (91, 91)
]

def nailoong_snuggle(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 75
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
    return save_gif(frames, 0.13)

add_meme(
    "nailoong_snuggle",
    nailoong_snuggle,
    min_images=1,
    max_images=1,
    keywords=["奶龙贴贴"],
    date_created=datetime(2026, 10, 10),
    date_modified=datetime(2026, 10, 10),
)