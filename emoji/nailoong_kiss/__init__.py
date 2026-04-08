from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (68, 57), (67, 57), (69, 54), (81, 51), (98, 57),
    (99, 57), (99, 57), (95, 55), (62, 46), (60, 45),
    (60, 45), (49, 48), (46, 48), (38, 50), (38, 51),
    (30, 61), (27, 63)
]

sizes = [
    (69, 69), (69, 69), (69, 69), (69, 69), (69, 69),
    (69, 69), (69, 69), (69, 69), (69, 69), (69, 69),
    (69, 69), (76, 76), (76, 76), (85, 85), (85, 85),
    (85, 85), (85, 85)
]

def nailoong_kiss(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []

    total_frames = 20  # 总帧数 1~20
    for i in range(1, total_frames + 1):
        frame = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)

        if i >= 4:  # 第4帧开始粘贴头像
            idx = i - 4
            pos = positions[idx]
            size = sizes[idx]
            user_head = user_img.resize(size)
            new_frame.paste(user_head, pos, alpha=True)

        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.13)

add_meme(
    "nailoong_kiss",
    nailoong_kiss,
    min_images=1,
    max_images=1,
    keywords=["奶龙吻"],
    date_created=datetime(2026, 4, 8),
    date_modified=datetime(2026, 4, 8),
)