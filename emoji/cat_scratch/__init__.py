from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def cat_scratch(images: list[BuildImage], texts, args):
    user_head = images[0].resize((90, 90)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (245, 631), (245, 631), (158, 601), (141, 550), (141, 550),  
        (141, 550), (141, 550), (141, 550), (141, 550), (141, 550),  
    ]
    for i in range(10):
        frame_num = (i % 10) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.12599999999999997)
add_meme(
    "cat_scratch",  
    cat_scratch,  
    min_images=1,  
    max_images=1,  
    keywords=["猫抓","猫猫抓"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 9, 4),  
    date_modified=datetime(2025, 9, 4),  
)
