from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def merry_christmas(images: list[BuildImage], texts, args):
    user_head = images[0].resize((93, 77)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (60, 90), (60, 90), (60, 90), (60, 90), (60, 90), (60, 90), (60, 90), (60, 90), 
    ]
    for i in range(8):
        frame_num = (i % 8) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "merry_christmas",  
    merry_christmas,  
    min_images=1,  
    max_images=1,  
    keywords=["圣诞快乐","圣诞节快乐"],  
    date_created=datetime(2025, 12, 9),  
    date_modified=datetime(2025, 12, 9),  
)
