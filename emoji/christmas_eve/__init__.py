from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def christmas_eve(images: list[BuildImage], texts, args):
    user_head = images[0].resize((118, 89)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (70, 120), (70, 120), (70, 120),   
    ]
    for i in range(3):
        frame_num = (i % 3) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.5)
add_meme(
    "christmas_eve",  
    christmas_eve,  
    min_images=1,  
    max_images=1,  
    keywords=["平安夜","平安夜快乐"],  
    date_created=datetime(2025, 8, 18),  
    date_modified=datetime(2025, 12, 9),  
)
