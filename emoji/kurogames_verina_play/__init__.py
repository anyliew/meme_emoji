from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_verina_play(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]

    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions_raw = [
        (74, 96), (71, 79), (79, 68), (75, 59), (70, 36),
        (71, 10), (70, 0), (69, 0), (68, 0), (71, 0),
        (73, 0), (75, 0), (75, 0), (73, 0), (68, 0),
        (66, 3), (67, 46), (71, 86)
    ]

    sizes_raw = [
        (182, 106), (187, 121), (180, 121), (190, 112), (199, 111),
        (199, 111), (205, 106), (207, 87), (208, 71), (202, 60),
        (197, 55), (193, 58), (191, 64), (190, 75), (192, 96),
        (194, 124), (193, 120), (191, 115)
    ]

    positions = [(x - 2, y - 2) for x, y in positions_raw]
    sizes = [(w + 4, h + 4) for w, h in sizes_raw]

    for i in range(len(positions)):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        avatar = avatar_frames[i % len(avatar_frames)]
        head = avatar.resize(sizes[i])

        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)

        frames.append(new_frame.image)

    return save_gif(frames, 0.03)


add_meme(
    "kurogames_verina_play",
    kurogames_verina_play,
    min_images=1,
    max_images=1,
    keywords=["维里奈顶", "小维顶"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 7, 21),
    date_modified=datetime(2026, 7, 21),
)