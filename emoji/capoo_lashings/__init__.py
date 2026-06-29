from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_lashings(images: list[BuildImage], texts, args):
    user_head = images[0].resize((330, 330)).convert("RGBA").circle()
    frames: list[IMG] = []
    positions = [
        (100, 102), (100, 102), (100, 102), (100, 102), (100, 102),  
        (100, 102), (100, 102), (100, 102), (100, 102), (100, 102),  
        (100, 102), (100, 102),   
    ]
    for i in range(12):
        frame_num = (i % 12) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.02)
add_meme(
    "capoo_lashings",  
    capoo_lashings,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波捶打","捶打"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 12, 5),  
    date_modified=datetime(2025, 12, 5),  
)
