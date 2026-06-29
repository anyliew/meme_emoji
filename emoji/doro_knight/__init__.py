from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_knight(images: list[BuildImage], texts, args):
    user_head = images[0].resize((133, 133)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (126, 203), (125, 197), (125, 204), (125, 209), (128, 197),  
        (125, 200), (124, 207), (125, 201), (125, 201), (125, 207),  
        (125, 209), (126, 201), (125, 205), (125, 198), (127, 197),  
        (127, 206),  
    ]
    for i in range(16):
        frame_num = (i % 16) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "doro_knight",  
    doro_knight,  
    min_images=1,  
    max_images=1,  
    keywords=["骑士","doro骑士","Doro骑士","DORO骑士"],  
    date_created=datetime(2025, 9, 13),  
    date_modified=datetime(2025, 9, 13),  
)
