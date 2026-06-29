from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def fart(images: list[BuildImage], texts, args):
    user_head = images[0].resize((93, 93)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (32, 4), (36, 4), (36, 4), (36, 4), (33, 4),  
        (33, 4), (31, 4), (31, 4),  
    ]
    for i in range(8):
        frame_num = (i % 8) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.14)
add_meme(
    "fart",  
    fart,  
    min_images=1,  
    max_images=1,  
    keywords=["放屁"],  
    date_created=datetime(2025, 9, 9),  
    date_modified=datetime(2025, 9, 9),  
)
