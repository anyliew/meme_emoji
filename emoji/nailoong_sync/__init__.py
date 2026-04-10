from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def nailoong_sync(images: list[BuildImage], texts, args):
    # 头像尺寸改为 70x70
    size = (70, 70)
    user_head = images[0].resize(size).convert("RGBA")

    frames: list[IMG] = []

    # 原始坐标每个 (x, y) 减 2
    positions = [
        (73, 60), (61, 60), (58, 60), (56, 59), (65, 59),
        (76, 59), (77, 59), (82, 59), (78, 59), (68, 59),
        (58, 59), (55, 59)
    ]

    for i in range(12):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)

        frames.append(new_frame.image)

    return save_gif(frames, 0.11)

add_meme(
    "nailoong_sync",
    nailoong_sync,
    min_images=1,
    max_images=1,
    keywords=["奶龙合拍"],
    date_created=datetime(2026, 4, 10),
    date_modified=datetime(2026, 4, 10),
)