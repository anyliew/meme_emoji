from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def deer_help(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
        (14, 9), (14, 10), (14, 10), (7, 9), (8, 9),  
    ]
    sizes = [
    (60, 50), (55, 55), (55, 55), (67, 43), (71, 42),  
    ]
    for i in range(5):
        frame_num = (i % 5) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.07)
add_meme(
    "deer_help",  
    deer_help,  
    min_images=1,  
    max_images=1,  
    keywords=["帮鹿","帮🦌"],  
    date_created=datetime(2025, 9, 28),  
    date_modified=datetime(2025, 9, 28),  
)
