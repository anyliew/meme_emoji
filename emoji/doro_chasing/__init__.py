from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_chasing(images: list[BuildImage], texts, args):
    user_head = images[0].resize((96, 96)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (268, 147), (267, 148), (268, 146), (267, 148)
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.07)
add_meme(
    "doro_chasing",  
    doro_chasing,  
    min_images=1,  
    max_images=1,  
    keywords=["doro追","Doro追","桃乐丝追"],  
    date_created=datetime(2025, 12, 2),  
    date_modified=datetime(2025, 12, 2),  
)
