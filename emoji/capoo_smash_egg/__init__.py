from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_smash_egg(images: list[BuildImage], texts, args):
    user_head = images[0].resize((65, 65)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (24, 57), (23, 95), (29, 116),   
    ]
    for i in range(3):
        frame_num = (i % 3) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.11)
add_meme(
    "capoo_smash_egg",  
    capoo_smash_egg,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波砸蛋"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 9, 5),  
    date_modified=datetime(2025, 9, 5),  
)
