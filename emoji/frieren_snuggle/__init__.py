from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def frieren_snuggle(images: list[BuildImage], texts, args):
    user_head = images[0].resize((78, 78)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (57, 132), (57, 132), (57, 137), (57, 137), (56, 138),  
        (56, 138), (56, 138), (55, 140), (55, 140), (55, 140),  
        (57, 137), (57, 137), (58, 135), (57, 132), (57, 132),  
        (57, 132), (57, 132),       
    ]
    for i in range(17):
        frame_num = (i % 17) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "frieren_snuggle",  
    frieren_snuggle,  
    min_images=1,  
    max_images=1,  
    keywords=["芙莉莲贴贴"],  
    date_created=datetime(2026, 1, 20),  
    date_modified=datetime(2026, 1, 20),  
)
