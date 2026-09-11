from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_xuanling_love(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [
        (62, 197), (63, 197), (62, 196), (62, 196), (62, 195),
        (62, 195), (62, 195), (62, 195), (62, 195), (62, 195),
        (61, 196), (60, 194), (58, 193), (56, 193), (55, 192),
        (54, 191), (53, 191), (53, 190), (51, 190), (51, 190),
        (52, 190), (51, 191), (50, 189), (50, 189), (50, 189),
        (50, 189), (50, 189), (50, 189), (50, 189), (50, 189),
        (50, 189), (50, 189), (50, 189), (50, 189), (50, 189),
        (50, 189), (50, 189), (50, 189), (50, 189), (51, 189),
        (50, 191), (50, 190), (50, 190), (50, 190), (50, 190),
        (50, 191), (50, 190), (51, 191), (50, 191), (50, 191),
        (50, 191), (50, 191), (51, 191), (50, 191), (50, 191),
        (50, 192), (50, 192), (50, 192), (50, 192), (52, 192)
    ]
    sizes = [
        (110, 79), (109, 79), (110, 80), (109, 80), (109, 81),
        (110, 80), (110, 81), (109, 80), (110, 81), (110, 81),
        (110, 80), (111, 82), (113, 83), (114, 83), (115, 85),
        (116, 85), (116, 85), (116, 87), (118, 86), (118, 86),
        (116, 87), (118, 86), (118, 87), (119, 87), (119, 88),
        (119, 87), (118, 87), (118, 87), (119, 87), (118, 88),
        (119, 87), (119, 87), (118, 88), (118, 87), (119, 87),
        (119, 87), (119, 87), (119, 87), (118, 87), (118, 87),
        (118, 86), (118, 87), (119, 86), (119, 87), (118, 88),
        (119, 86), (119, 87), (118, 86), (119, 87), (118, 87),
        (119, 87), (118, 86), (117, 87), (118, 87), (119, 88),
        (118, 86), (118, 87), (119, 86), (119, 87), (117, 86)
    ]

    for frame_num in range(1, 61):
        bg = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        idx = (frame_num - 1) % len(avatar_frames)
        avatar = avatar_frames[idx]
        head = avatar.resize(sizes[frame_num - 1], keep_ratio=True)
        new_frame = BuildImage.new("RGBA", bg.size)
        new_frame.paste(head, positions[frame_num - 1], alpha=True)
        new_frame.paste(bg, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.03)


add_meme(
    "kurogames_xuanling_love",
    kurogames_xuanling_love,
    min_images=1,
    max_images=1,
    keywords=["玄翎爱心"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 9, 11),
    date_modified=datetime(2026, 9, 11),
)