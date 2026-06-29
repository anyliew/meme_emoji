from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def ignite(images: list[BuildImage], texts, args):
    user_head = images[0].resize((170, 170)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (35, 32), (35, 32), (35, 32), (35, 32), (35, 32),  
        (35, 32), (35, 32), (35, 32), (35, 32), (35, 32),  
        (35, 32), (35, 32), (35, 32), (35, 32), (35, 32),  
        (35, 32), (35, 32), (35, 32), (35, 32), (35, 32),  
        (35, 32),   
    ]
    for i in range(21):
        frame_num = (i % 21) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "ignite",  
    ignite,  
    min_images=1,  
    max_images=1,  
    keywords=["燃起来了"],  
    date_created=datetime(2025, 9, 9),  
    date_modified=datetime(2025, 9, 9),  
)
