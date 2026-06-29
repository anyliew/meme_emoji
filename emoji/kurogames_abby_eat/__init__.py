from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_abby_eat(images: list[BuildImage], texts, args):
    user_head = images[0].resize((78, 78)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (157, 186), (156, 183), (152, 180), (152, 178), (154, 181),  
        (154, 184), (154, 184), (153, 180), (153, 178), (154, 180),  
        (153, 182), 
    ]
    for i in range(11):
        frame_num = (i % 11) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "kurogames_abby_eat",  
    kurogames_abby_eat,  
    min_images=1,  
    max_images=1,  
    keywords=["阿布吃"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 14),  
    date_modified=datetime(2025, 7, 14),  
)
