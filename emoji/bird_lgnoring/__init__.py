from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def bird_lgnoring(images: list[BuildImage], texts, args):
    user_head = images[0].resize((55, 55)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (95, 69), (95, 69), (95, 66), (95, 64), (95, 61),
        (95, 60), (96, 58), (96, 60), (96, 61), (96, 65),
        (96, 66), (95, 67), (95, 66), (95, 65), (95, 63),
        (96, 60), (96, 60), (96, 61), (96, 62), (96, 65),
        (96, 66), (96, 69), (96, 69), (95, 68), (95, 64),
        (95, 63), (95, 60), (95, 59), (95, 59), (95, 59),
        (96, 62), (96, 64), (96, 66), (96, 68), (96, 70),
        (95, 70), (95, 68), (95, 65), (96, 63), (96, 60),
        (96, 59), (96, 59), (96, 61), (96, 62), (96, 64)
    ]
    for i in range(45):
        frame_num = (i % 45) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        if positions[i][1] != 0:  
            new_frame = frame.copy()
            new_frame.paste(user_head, positions[i], alpha=True, below=True)
            frames.append(new_frame.image)
        else:
            frames.append(frame.image)
    return save_gif(frames, 0.07)
add_meme(
    "bird_lgnoring",  
    bird_lgnoring,  
    min_images=1,  
    max_images=1,  
    keywords=["不鸟你","我鸟都不鸟你"],  
    date_created=datetime(2025, 12, 23),  
    date_modified=datetime(2025, 12, 23),  
)
