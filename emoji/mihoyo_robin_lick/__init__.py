from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def mihoyo_robin_lick(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [
        (244, 57), (244, 58), (244, 57), (244, 56), (244, 57),
        (244, 57), (244, 57), (223, 58), (254, 57), (223, 58),
        (254, 57), (223, 58), (254, 57), (223, 58), (254, 57),
        (191, 62), (235, 62), (251, 56), (258, 60), (262, 57),
        (263, 56), (264, 55), (257, 56), (241, 56), (241, 60),
        (243, 58), (244, 57), (244, 57)
    ]

    sizes = [
        (184, 147), (184, 148), (184, 147), (184, 148), (184, 147),
        (184, 147), (184, 147), (173, 140), (182, 148), (172, 140),
        (182, 148), (172, 140), (182, 148), (172, 140), (182, 148),
        (169, 143), (180, 138), (182, 149), (184, 145), (184, 147),
        (184, 148), (184, 151), (184, 148), (184, 148), (184, 146),
        (184, 146), (184, 147), (184, 147)
    ]

    for frame_num in range(1, 29):  # 对应 1.png ~ 28.png
        bg = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        idx = (frame_num - 1) % len(avatar_frames)
        avatar = avatar_frames[idx]
        head = avatar.resize(sizes[frame_num - 1], keep_ratio=True)
        new_frame = BuildImage.new("RGBA", bg.size)
        new_frame.paste(head, positions[frame_num - 1], alpha=True)
        new_frame.paste(bg, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.04)


add_meme(
    "mihoyo_robin_lick",
    mihoyo_robin_lick,
    min_images=1,
    max_images=1,
    keywords=["知更鸟舔"],
    tags=MemeTags.star_rail,
    date_created=datetime(2026, 9, 9),
    date_modified=datetime(2026, 9, 9),
)