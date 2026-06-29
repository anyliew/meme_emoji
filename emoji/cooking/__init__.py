from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def cooking(images: list[BuildImage], texts, args):
    user_head = images[0].resize((95, 95)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
    (80, 59), (80, 59), (80, 61), (80, 61), (80, 67),  
    (80, 67), (80, 59), (80, 59), (80, 61), (80, 62),  
    (80, 67), (80, 67), (80, 59), (80, 58), (80, 61),  
    (80, 62), (80, 67), (80, 67), (80, 58), (79, 59),  
    (80, 61), (80, 61), (80, 67), (80, 67), (80, 59),  
    (80, 59), (80, 61), (80, 61), (80, 67), (80, 67),  
    (80, 59), (80, 59), (80, 61), (80, 62), (80, 67),  
    (80, 67), (80, 58), (80, 59), (80, 63), (80, 64),  
    (78, 68), (79, 68), (80, 64), (80, 63), (80, 58),  
    (80, 59), (80, 64), (80, 63), (79, 67), (79, 67),  
    (80, 63), (80, 63),  
    ]
    for i in range(52):
        frame_num = (i % 52) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "cooking",  
    cooking,  
    min_images=1,  
    max_images=1,  
    keywords=["炒菜"],  
    date_created=datetime(2025, 9, 29),  
    date_modified=datetime(2025, 9, 29),  
)
