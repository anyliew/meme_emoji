from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_gothammered(images: list[BuildImage], texts, args):
    user_head = images[0].resize((80, 80)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (82, 147), (77, 116), (79, 128), (76, 135), (80, 146),
        (77, 127), (80, 127), (78, 137), (81, 146), (78, 130),
        (81, 129), (81, 139), (81, 147), (80, 131), (81, 130),
        (79, 137), (81, 146), (78, 131), (79, 130), (80, 138)
    ]
    for i in range(20):
        frame_num = (i % 20) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "capoo_gothammered",  
    capoo_gothammered,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波被锤"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 12, 5),  
    date_modified=datetime(2025, 12, 5),  
)
