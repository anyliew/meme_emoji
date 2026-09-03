from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_denia_hug(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [
        (60, 146), (60, 146), (61, 145), (61, 145), (61, 145),
        (61, 145), (61, 145), (61, 145), (61, 145), (61, 145),
        (61, 145), (61, 145), (61, 145), (61, 145), (60, 146),
        (60, 146), (60, 146), (60, 145), (60, 145), (60, 146),
        (60, 146), (60, 146), (60, 146), (60, 146), (60, 145),
        (60, 145), (60, 145), (61, 145), (61, 145), (60, 146),
        (60, 146), (60, 146), (59, 146), (59, 146), (60, 145),
        (60, 145), (60, 145), (61, 145), (61, 145), (60, 145),
        (60, 145), (60, 145), (60, 146), (60, 146), (61, 144),
        (61, 144), (61, 144), (60, 145), (60, 145), (60, 145)
    ]

    sizes = [
        (81, 54), (81, 54), (80, 55), (80, 55), (80, 55),
        (80, 55), (80, 55), (80, 55), (80, 55), (80, 55),
        (80, 55), (80, 55), (80, 55), (80, 55), (81, 54),
        (81, 54), (81, 54), (80, 55), (80, 55), (81, 54),
        (81, 54), (81, 54), (80, 54), (80, 54), (82, 55),
        (82, 55), (82, 55), (80, 55), (80, 55), (81, 54),
        (81, 54), (81, 54), (82, 54), (82, 54), (81, 55),
        (81, 55), (81, 55), (79, 55), (79, 55), (82, 55),
        (82, 55), (82, 55), (81, 54), (81, 54), (80, 56),
        (80, 56), (80, 56), (81, 55), (81, 55), (82, 55)
    ]

    for frame_num in range(1, 51):  # 50 frames
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
    "kurogames_denia_hug",
    kurogames_denia_hug,
    min_images=1,
    max_images=1,
    keywords=["达妮娅抱"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 9, 3),
    date_modified=datetime(2026, 9, 3),
)