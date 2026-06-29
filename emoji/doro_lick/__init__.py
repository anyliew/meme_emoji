from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_lick(images: list[BuildImage], texts, args):
    user_head = images[0].resize((31, 31)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (103, 73), (103, 73),(103, 73), (103, 73),(103, 73),   
    ]
    for i in range(5):
        frame_num = (i % 5) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.09)
add_meme(
    "doro_lick",  
    doro_lick,  
    min_images=1,  
    max_images=1,  
    keywords=["桃乐丝舔","doro舔","Doro舔","DORO舔"],  
    date_created=datetime(2025, 7, 20),  
    date_modified=datetime(2025, 7, 20),  
)
