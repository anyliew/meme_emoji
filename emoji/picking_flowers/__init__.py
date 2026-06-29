from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def picking_flowers(images: list[BuildImage], texts, args):
    user_head = images[0].resize((212, 212)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (45, 13), (45, 13), (45, 13), (45, 13), (45, 13),  
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.2)
add_meme(
    "picking_flowers",  
    picking_flowers,  
    min_images=1,  
    max_images=1,  
    keywords=["摘花"],  
    date_created=datetime(2025, 8, 16),  
    date_modified=datetime(2025, 8, 16),  
)
