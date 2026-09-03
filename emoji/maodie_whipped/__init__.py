from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def maodie_whipped(images: list[BuildImage], texts, args):
    user_head = images[0].convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (70, 73), (71, 69), (71, 69), (65, 66), (52, 61),
        (41, 65), (38, 68), (38, 69), (44, 72), (50, 71),
        (58, 69), (63, 68), (60, 71), (55, 74), (53, 74),
        (54, 73), (64, 71), (77, 72), (81, 72), (81, 72),
        (73, 71), (58, 70), (33, 70), (31, 71), (40, 73),
        (44, 76), (48, 76), (54, 74)
    ]
    sizes = [
        (59, 59), (59, 59), (59, 59), (59, 59), (59, 59),
        (59, 59), (59, 59), (59, 59), (59, 59), (59, 59),
        (59, 59), (59, 59), (59, 59), (59, 59), (59, 59),
        (59, 59), (59, 59), (59, 59), (59, 59), (59, 59),
        (59, 59), (59, 59), (59, 59), (59, 59), (59, 59),
        (59, 59), (59, 59), (59, 59)
    ]
    for i in range(28):
        frame_num = (i % 28) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        head_resized = user_head.resize(sizes[i])
        new_frame.paste(head_resized, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)

add_meme(
    "maodie_whipped",
    maodie_whipped,
    min_images=1,
    max_images=1,
    keywords=["耄耋打"],
    date_created=datetime(2026, 7, 13),
    date_modified=datetime(2026, 7, 13),
)