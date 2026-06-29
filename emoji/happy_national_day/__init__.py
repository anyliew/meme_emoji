from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def happy_national_day(images: list[BuildImage], texts, args):
    user_head = images[0].resize((190, 160)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (55, 92), (55, 81), (55, 76), (55, 84), 
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.08)
add_meme(
    "happy_national_day",  
    happy_national_day,  
    min_images=1,  
    max_images=1,  
    keywords=["国庆快乐","国庆节快乐"],  
    date_created=datetime(2025, 9, 13),  
    date_modified=datetime(2025, 9, 13),  
)
