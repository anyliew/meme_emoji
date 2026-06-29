from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_abby_rub(images: list[BuildImage], texts, args):
    user_head = images[0].resize((156, 141)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (5, 124), (7, 122), (10, 121), (12, 120), (10, 121),  
        (7, 123), (5, 124), (8, 124), (10, 121), (12, 121),  
        (10, 121), (7, 124), (5, 125), (5, 124), (5, 124),  
        (5, 124), (5, 124), (5, 124), (5, 124), (5, 124),  
        (5, 124), (5, 124), (5, 124), (5, 124),             
    ]
    for i in range(24):
        frame_num = (i % 24) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.08)
add_meme(
    "kurogames_abby_rub",  
    kurogames_abby_rub,  
    min_images=1,  
    max_images=1,  
    keywords=["阿布贴贴"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 3),  
    date_modified=datetime(2025, 8, 3),  
)
