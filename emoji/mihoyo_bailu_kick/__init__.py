from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def mihoyo_bailu_kick(images: list[BuildImage], texts, args):
    user_head = images[0].resize((60, 60)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
    (49, 67), (49, 67), (49, 67), (49, 67), (31, 35),    
    (11, 32), (1, 47), (2, 60), (3, 62), (7, 64),   
    (9, 70), (8, 76), (4, 106), (2, 157), (11, 156), 
    (29, 47), (47, 1), (56, -28), (66, -26), (92, -36),   
    (127, 4), (150, 56), (130, 63), (86, 46), (28, 54), 
    (-25, 151), (13, 99), (132, 29), (167, 6), (207, 1), 
    (220, 29), (227, 61), (159, 17), (104, -28), (76, -39)  
    ]
    for i in range(35):
        frame_num = (i % 35) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.09)
add_meme(
    "mihoyo_bailu_kick",  
    mihoyo_bailu_kick,  
    min_images=1,  
    max_images=1,  
    keywords=["白露踢"],  
    tags=MemeTags.star_rail,
    date_created=datetime(2025, 9, 30),  
    date_modified=datetime(2025, 9, 30),  
)
