from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def ikun_trainee(images: list[BuildImage], texts, args):
    user_head = images[0].convert("RGBA")

    frames: list[IMG] = []

    # 每帧头像的位置和尺寸
    positions = [
        (58, 52), (56, 55), (59, 52), (60, 51), (59, 45),
        (62, 42), (63, 48), (60, 53), (63, 48), (62, 42),
        (59, 46), (60, 51)
    ]

    sizes = [
        (64, 42), (65, 42), (64, 42), (61, 43), (63, 51),
        (58, 50), (57, 49), (61, 43), (56, 49), (59, 50),
        (63, 50), (61, 43)
    ]

    for i in range(12):  # 总共12帧
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        # 根据当前帧的尺寸缩放头像
        target_size = sizes[i]
        resized_head = user_head.resize(target_size, keep_ratio=True)

        # 创建新画布
        new_frame = BuildImage.new("RGBA", frame.size)
        # 粘贴缩放后的头像
        new_frame.paste(resized_head, positions[i], alpha=True)
        # 粘贴模板帧
        new_frame.paste(frame, (0, 0), alpha=True)

        frames.append(new_frame.image)

    return save_gif(frames, 0.05)

add_meme(
    "ikun_trainee",
    ikun_trainee,
    min_images=1,
    max_images=1,
    keywords=["练习生"],
    date_created=datetime(2026, 4, 8),
    date_modified=datetime(2026, 4, 8),
)