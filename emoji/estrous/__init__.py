from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def estrous(images: list[BuildImage], texts, args):
    user_head = images[0].resize((98, 66)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (105, 229), (104, 230), (103, 232), (101, 232), (98, 233),  
        (96, 233), (93, 233), (91, 235), (89, 235), (86, 235),  
        (85, 235), (84, 234), (83, 235), (81, 232), (82, 233),  
        (82, 231), (85, 231), (87, 230), (89, 229), (92, 228),  
        (94, 227), (97, 227), (100, 226), (101, 226), (104, 225),  
        (106, 225), (106, 225), (109, 226), (109, 227), (108, 228),  
        (108, 229), (106, 230), (105, 227), 
    ]
    for i in range(33):
        frame_num = (i % 33) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "estrous",  
    estrous,  
    min_images=1,  
    max_images=1,  
    keywords=["发情"],  
    date_created=datetime(2025, 8, 11),  
    date_modified=datetime(2025, 8, 11),  
)
