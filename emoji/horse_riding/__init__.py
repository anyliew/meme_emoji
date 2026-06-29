from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def horse_riding(images: list[BuildImage], texts, args):
    user_head = images[0].resize((58, 58)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (76, 44), (81, 44), (100, 47), (101, 46),
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.01)
add_meme(
    "horse_riding",  
    horse_riding,  
    min_images=1,  
    max_images=1,  
    keywords=["骑马"],  
    date_created=datetime(2025, 9, 13),  
    date_modified=datetime(2025, 9, 13),  
)
