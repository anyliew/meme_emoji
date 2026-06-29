from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_take_dump(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
        (34, 55), (34, 55), (38, 59), (91, 79), (148, 104),  
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),  
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),    
        (1, 1), (1, 1), (1, 1), (1, 1),   
    ]
    sizes = [
        (86, 75), (86, 75), (79, 69), (51, 52), (35, 36),  
        (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),  
        (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),  
        (2, 2), (2, 2), (2, 2), (2, 2),  
    ]
    for i in range(19):
        frame_num = (i % 19) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "capoo_take_dump",  
    capoo_take_dump,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波拉"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 9, 27),  
    date_modified=datetime(2025, 9, 27),  
)
