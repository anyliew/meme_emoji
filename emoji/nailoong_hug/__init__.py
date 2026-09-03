from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def nailoong_hug(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]
    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions_18 = [
        (207, 26), (207, 26), (195, 24), (189, 24), (184, 25),
        (178, 26), (173, 26), (168, 26), (164, 27), (161, 27),
        (159, 27), (157, 27), (154, 27), (152, 27), (152, 27),
        (150, 27), (150, 27), (150, 27), (149, 26), (149, 26),
        (149, 26), (149, 26), (149, 26), (149, 26), (149, 26),
        (149, 26), (149, 26), (149, 26), (149, 26), (149, 26),
        (149, 26), (149, 26), (147, 27), (147, 27), (147, 27),
        (147, 27), (147, 27), (147, 27), (147, 27), (147, 27),
        (147, 25), (148, 26), (148, 26), (148, 26), (147, 26),
        (147, 26), (147, 26), (147, 26), (147, 26), (145, 25),
        (144, 27), (144, 27), (141, 26), (141, 26), (139, 26),
        (139, 26), (136, 26), (136, 26), (135, 26), (135, 26),
        (135, 26), (135, 26), (135, 26), (134, 26), (134, 26),
        (134, 26), (134, 26), (134, 26), (134, 26), (134, 26),
        (134, 26), (134, 26), (134, 26), (131, 26), (129, 26),
        (129, 26), (128, 26), (131, 26), (128, 29), (113, 34),
        (113, 34), (115, 32), (116, 29), (111, 31), (109, 38),
        (109, 38), (111, 35), (111, 38), (116, 36), (120, 37),
        (126, 36), (135, 27), (145, 25), (151, 25), (149, 24),
        (144, 25), (131, 28), (120, 37)
    ]

    sizes_18 = [
        (33, 47), (33, 47), (45, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (50, 53), (50, 53), (50, 53), (50, 53), (50, 53),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (55, 55),
        (55, 55), (55, 55), (55, 55), (55, 55), (67, 67),
        (67, 67), (67, 67), (67, 67), (67, 67), (67, 67),
        (67, 67), (67, 67), (67, 67), (67, 67), (67, 67),
        (67, 67), (67, 67), (67, 67), (67, 67), (67, 67),
        (67, 67), (67, 67), (67, 67)
    ]

    for frame_num in range(1, 116):
        bg = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", bg.size)

        if frame_num >= 18:
            idx = (frame_num - 18) % len(avatar_frames)
            orig_pos = positions_18[frame_num - 18]
            orig_size = sizes_18[frame_num - 18]
            pos = (orig_pos[0] - 6, orig_pos[1] - 6)
            size = (orig_size[0] + 9, orig_size[1] + 9)
            head = avatar_frames[idx].resize(size, keep_ratio=True)
            new_frame.paste(head, pos, alpha=True)

        new_frame.paste(bg, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.07)


add_meme(
    "nailoong_hug",
    nailoong_hug,
    min_images=1,
    max_images=1,
    keywords=["奶龙抱"],
    date_created=datetime(2026, 9, 3),
    date_modified=datetime(2026, 9, 3),
)