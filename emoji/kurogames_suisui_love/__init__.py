from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_suisui_love(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [
        (0, 68), (0, 73), (0, 77), (0, 81), (0, 86),
        (0, 92), (0, 97), (0, 100), (0, 92), (0, 82),
        (0, 71), (0, 60), (0, 48), (0, 36), (0, 25),
        (0, 20), (0, 21), (0, 21), (0, 22), (0, 24),
        (0, 26), (0, 28), (0, 31), (0, 35), (0, 40),
        (0, 46), (0, 51), (0, 57), (0, 63), (0, 68)
    ]
    sizes = [
        (143, 102), (144, 97), (145, 93), (147, 89), (150, 84),
        (153, 78), (157, 73), (161, 70), (162, 78), (164, 88),
        (165, 99), (166, 110), (166, 122), (166, 134), (166, 140),
        (167, 146), (167, 149), (166, 149), (165, 148), (163, 146),
        (160, 144), (157, 142), (155, 139), (152, 135), (149, 130),
        (147, 124), (145, 119), (144, 113), (143, 107), (143, 102)
    ]

    for frame_num in range(1, 31):
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
    "kurogames_suisui_love",
    kurogames_suisui_love,
    min_images=1,
    max_images=1,
    keywords=["穗穗爱心"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)