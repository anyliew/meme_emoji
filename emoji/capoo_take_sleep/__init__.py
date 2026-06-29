from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_take_sleep(images: list[BuildImage], texts, args):
    user_head = images[0].resize((65, 47)).convert("RGBA").rotate(35, expand=True)
    frames: list[IMG] = []
    positions = [
        (1, 103), (1, 103), (1, 103), (1, 103), (1, 103),  
        (1, 103), (1, 103), (1, 103), (1, 103), (1, 103),  
        (1, 103), (1, 103), (1, 103), (1, 103), (1, 103),  
        (1, 103), (1, 103), (1, 103), (1, 103), (1, 103),  
        (1, 103), (1, 103), (1, 103), (1, 103), (1, 103),  
        (1, 103), (1, 103), (1, 103),   
    ]
    for i in range(27):
        frame_num = (i % 27) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "capoo_take_sleep",  
    capoo_take_sleep,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波睡觉","睡觉"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 9, 27),  
    date_modified=datetime(2025, 9, 27),  
)
