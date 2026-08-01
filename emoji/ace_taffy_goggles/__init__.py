from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def ace_taffy_goggles(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]

    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    positions = [(14, 30)] * 34
    sizes = [(191, 191)] * 34

    for i in range(34):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        avatar = avatar_frames[i % len(avatar_frames)]
        head = avatar.resize(sizes[i]).circle()

        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)

        frames.append(new_frame.image)

    return save_gif(frames, 0.06)


add_meme(
    "ace_taffy_goggles",
    ace_taffy_goggles,
    min_images=1,
    max_images=1,
    keywords=["护目镜"],
    date_created=datetime(2026, 8, 2),
    date_modified=datetime(2026, 8, 2),
)