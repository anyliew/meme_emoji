from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_fished_out(images: list[BuildImage], texts, args):
    user_head = images[0].resize((95, 95)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),  
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),  
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),  
        (57, 84), (35, 117), (21, 102), (27, 112), (28, 112),  
    ]
    for i in range(20):
        frame_num = (i % 20) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.10)
add_meme(
    "capoo_fished_out",  
    capoo_fished_out,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波掏"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 9, 4),  
    date_modified=datetime(2025, 9, 5),  
)
