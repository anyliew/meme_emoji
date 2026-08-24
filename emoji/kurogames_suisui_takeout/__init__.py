from datetime import datetime
from pathlib import Path

from PIL import ImageSequence
from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"


def kurogames_suisui_takeout(images: list[BuildImage], texts, args):
    frames: list[IMG] = []

    avatar_frames = [
        BuildImage(frame.copy().convert("RGBA")).square()
        for frame in ImageSequence.Iterator(images[0].image)
    ]

    if not avatar_frames:
        avatar_frames = [images[0].convert("RGBA").square()]

    # 总共5帧，1~2不加头像，3~5加头像，各自坐标和尺寸
    positions = [
        (15, 266),  # 第3帧
        (32, 260),  # 第4帧
        (32, 262)   # 第5帧
    ]
    sizes = [
        (87, 77),   # 第3帧
        (83, 69),   # 第4帧
        (83, 70)    # 第5帧
    ]

    for frame_num in range(1, 6):  # 1~5
        bg = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        if frame_num <= 2:
            # 不加头像，直接使用背景图
            frames.append(bg.image)
        else:
            idx = frame_num - 3  # 0,1,2
            avatar = avatar_frames[idx % len(avatar_frames)]
            head = avatar.resize(sizes[idx])
            new_frame = BuildImage.new("RGBA", bg.size)
            new_frame.paste(head, positions[idx], alpha=True)
            new_frame.paste(bg, (0, 0), alpha=True)
            frames.append(new_frame.image)

    return save_gif(frames, 0.3)


add_meme(
    "kurogames_suisui_takeout",
    kurogames_suisui_takeout,
    min_images=1,
    max_images=1,
    keywords=["穗穗掏"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 8, 24),
    date_modified=datetime(2026, 8, 24),
)