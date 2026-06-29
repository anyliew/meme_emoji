from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_abby_lift_high(images: list[BuildImage], texts, args):
    user_head = images[0].resize((170, 156)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (145, 111), (142, 97), (133, 73), (132, 73), (132, 73),  
        (132, 73), (132, 73),  
    ]
    for i in range(7):
        frame_num = (i % 7) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.15)
add_meme(
    "kurogames_abby_lift_high",  
    kurogames_abby_lift_high,  
    min_images=1,  
    max_images=1,  
    keywords=["举高高"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 3),  
    date_modified=datetime(2025, 8, 3),  
)
