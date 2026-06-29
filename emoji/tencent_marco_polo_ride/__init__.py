from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def tencent_marco_polo_ride(images: list[BuildImage], texts, args):
    user_head = images[0].resize((52, 52)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (30, 32), (30, 32), (33, 29), (35, 27), (35, 27),
        (35, 27), (36, 27), (37, 27), (39, 28), (36, 36),
        (28, 50), (31, 73), (38, 76), (46, 75), (61, 70),
        (76, 65), (65, 69), (43, 76), (38, 65), (20, 84),
        (24, 110), (31, 115), (55, 68), (64, 42), (66, 51),
        (59, 84), (49, 85), (60, 74), (83, 51), (103, 37),
        (99, 59), (102, 59), (108, 46), (108, 53), (102, 73),
        (97, 80), (96, 71), (108, 52), (113, 60), (118, 59),
        (118, 59), (118, 59), (118, 59), (119, 57), (119, 57),
        (117, 59), (118, 58), (119, 57), (119, 57), (119, 57),
        (119, 58), (120, 57), (120, 57), (120, 57), (120, 57),
        (120, 57), (120, 57), (119, 58), (119, 58), (119, 58),
        (119, 58), (118, 60), (118, 59), (120, 57), (120, 57),
        (118, 59), (119, 59), (119, 59), (119, 59), (117, 61),
        (117, 61), (118, 58), (115, 58)
    ]
    for i in range(73):
        frame_num = (i % 73) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.12)
add_meme(
    "tencent_marco_polo_ride",  
    tencent_marco_polo_ride,  
    min_images=1,  
    max_images=1,  
    keywords=["马克骑","马可波罗骑"],  
    date_created=datetime(2026, 1, 9),  
    date_modified=datetime(2026, 1, 9),  
)
