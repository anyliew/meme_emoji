from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_suoming_takeout(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]

    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    # 18~36帧共19帧，统一坐标和尺寸
    positions = [(51, 180)] * 19
    sizes = [(115, 115)] * 19

    for i in range(36):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        if frame_num <= 17:
            frames.append(frame.image)
        else:
            idx = frame_num - 18          # idx 从 0 开始，对应 positions[0]~positions[18]
            avatar = avatar_frames[idx % len(avatar_frames)]
            head = avatar.resize(sizes[idx])
            new_frame = BuildImage.new("RGBA", frame.size)
            new_frame.paste(head, positions[idx], alpha=True)
            new_frame.paste(frame, (0, 0), alpha=True)
            frames.append(new_frame.image)

    return save_gif(frames, 0.06)


add_meme(
    "kurogames_suoming_takeout",
    kurogames_suoming_takeout,
    min_images=1,
    max_images=1,
    keywords=["锁暝掏"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 7, 22),
    date_modified=datetime(2026, 7, 24),
)