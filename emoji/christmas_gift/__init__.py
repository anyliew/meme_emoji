from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def christmas_gift(images: list[BuildImage], texts, args):
    user_head = images[0].resize((300, 215), keep_ratio=True).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (0, 0), (0, 244), (0, 197), (0, 159),      
        (0, 129), (0, 105), (0, 87), (0, 74), (0, 67),     
        (0, 61), (0, 57), (0, 53), (0, 51), (0, 49),      
        (0, 48), (0, 46), (0, 48), (0, 51), (0, 56),      
        (0, 62), (0, 66), (0, 67), (0, 67), (0, 67),      
        (0, 65), (0, 65), (0, 61), (0, 60), (0, 60),      
        (0, 60), (0, 67), (0, 92), (0, 141), (0, 201),    
        (0, 245), (0, 0), (0, 0), (0, 0), (0, 0),        
        (0, 0), (0, 0)                                    
    ]
    for i in range(41):
        frame_num = (i % 41) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        if positions[i][1] != 0:  
            new_frame = frame.copy()
            new_frame.paste(user_head, positions[i], alpha=True, below=True)
            frames.append(new_frame.image)
        else:
            frames.append(frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "christmas_gift",  
    christmas_gift,  
    min_images=1,  
    max_images=1,  
    keywords=["圣诞礼物"],  
    date_created=datetime(2025, 12, 23),  
    date_modified=datetime(2025, 12, 30),  
)
