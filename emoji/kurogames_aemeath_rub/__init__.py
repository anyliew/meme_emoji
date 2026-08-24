from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_aemeath_rub(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [
        (187, 145), (187, 144), (187, 140), (187, 135), (187, 132),
        (187, 132), (187, 133), (187, 137), (187, 142), (187, 145),
        (187, 144), (187, 140), (187, 136), (187, 133), (187, 130),
        (187, 133), (187, 137), (187, 142)
    ]
    sizes = [
        (111, 94), (111, 93), (111, 93), (111, 93), (111, 91),
        (111, 90), (111, 93), (111, 94), (111, 93), (111, 94),
        (111, 93), (111, 93), (111, 91), (111, 90), (111, 93),
        (111, 93), (111, 94), (111, 93)
    ]

    for frame_num in range(1, 19):
        bg = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        idx = (frame_num - 1) % len(avatar_frames)
        avatar = avatar_frames[idx]
        head = avatar.resize(sizes[frame_num - 1], keep_ratio=True)
        new_frame = BuildImage.new("RGBA", bg.size)
        new_frame.paste(head, positions[frame_num - 1], alpha=True)
        new_frame.paste(bg, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.06)


add_meme(
    "kurogames_aemeath_rub",
    kurogames_aemeath_rub,
    min_images=1,
    max_images=1,
    keywords=["爱弥斯搓"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 8, 24),
    date_modified=datetime(2026, 8, 24),
)