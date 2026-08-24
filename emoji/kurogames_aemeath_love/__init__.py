from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_aemeath_love(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [
        (35, 127), (37, 127), (37, 126), (38, 126), (36, 128),
        (38, 125)
    ]
    sizes = [
        (91, 35), (90, 35), (91, 36), (90, 36), (93, 34),
        (90, 37)
    ]

    for frame_num in range(1, 7):
        bg = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        idx = (frame_num - 1) % len(avatar_frames)
        avatar = avatar_frames[idx]
        head = avatar.resize(sizes[frame_num - 1], keep_ratio=True)
        new_frame = BuildImage.new("RGBA", bg.size)
        new_frame.paste(head, positions[frame_num - 1], alpha=True)
        new_frame.paste(bg, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.3)


add_meme(
    "kurogames_aemeath_love",
    kurogames_aemeath_love,
    min_images=1,
    max_images=1,
    keywords=["爱弥斯爱心"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 8, 24),
    date_modified=datetime(2026, 8, 24),
)