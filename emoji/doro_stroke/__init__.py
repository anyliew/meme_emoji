from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_stroke(images: list[BuildImage], texts, args):
    user_head = images[0].resize((81, 81)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (148, 306), (148, 306), (148, 306), (148, 306), (148, 306),
        (148, 306), (148, 306), (148, 306), (148, 306), (148, 306),
        (148, 306), (148, 306), (148, 306), (148, 306), (148, 306),
        (148, 306), 
    ]
    for i in range(16):
        frame_num = (i % 16) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.07)
add_meme(
    "doro_stroke",  
    doro_stroke,  
    min_images=1,  
    max_images=1,  
    keywords=["抚摸","doro抚摸","Doro抚摸","桃乐丝抚摸"],  
    date_created=datetime(2026, 1, 15),  
    date_modified=datetime(2026, 1, 15),  
)
