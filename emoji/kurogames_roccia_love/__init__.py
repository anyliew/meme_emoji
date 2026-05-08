from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def kurogames_roccia_love(images: list[BuildImage], texts, args):
    user_head = images[0].convert("RGBA")
    frames: list[IMG] = []

    positions = [
        (106, 242), (105, 244), (103, 246), (102, 247), (101, 249),
        (100, 250), (99, 251), (98, 251), (98, 251), (97, 250),
        (97, 249), (97, 248), (98, 247), (99, 246), (99, 244),
        (101, 243), (103, 242), (104, 241), (105, 239), (107, 238),
        (108, 237), (109, 236), (110, 235), (110, 235), (111, 234),
        (111, 234), (111, 235), (111, 236), (110, 236), (109, 237),
        (108, 238), (107, 240), (106, 242)
    ]

    sizes = [
        (94, 57), (94, 56), (95, 54), (95, 53), (95, 51),
        (95, 50), (95, 49), (95, 49), (95, 49), (96, 50),
        (96, 51), (97, 51), (96, 51), (96, 52), (97, 54),
        (95, 54), (94, 54), (95, 55), (95, 57), (93, 57),
        (94, 58), (94, 59), (93, 60), (94, 60), (93, 61),
        (93, 61), (93, 61), (92, 60), (93, 60), (93, 60),
        (94, 59), (94, 58), (94, 57)
    ]

    for i in range(33):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        resized_head = user_head.resize((width, height), keep_ratio=True).convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(resized_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.03)

add_meme(
    "kurogames_roccia_love",
    kurogames_roccia_love,
    min_images=1,
    max_images=1,
    keywords=["洛可可喜欢"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 5, 8),
    date_modified=datetime(2026, 5, 8),
)