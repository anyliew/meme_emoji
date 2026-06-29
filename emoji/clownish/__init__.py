from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def clownish(images: list[BuildImage], texts, args):
    user_head = images[0].resize((60, 60)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (55, -7), (57, -4), (61, 1), (70, -3), (98, 14),  
        (103, 16), (99, -4), (94, 1), (91, 3), (83, -1),  
        (54, 14), (47, 18),  
    ]
    for i in range(12):
        frame_num = (i % 12) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.08)
add_meme(
    "clownish",  
    clownish,  
    min_images=1,  
    max_images=1,  
    keywords=["滑稽"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 14),  
    date_modified=datetime(2025, 8, 14),  
)
