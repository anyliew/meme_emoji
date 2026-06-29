from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def cheer(images: list[BuildImage], texts, args):
    user_head = images[0].resize((69, 69)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (71, 165), (74, 75), (75, 75), (71, 166), (71, 166),
        (75, 76), (71, 167), (72, 166), (75, 76), (72, 166)
    ]
    for i in range(10):
        frame_num = (i % 10) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "cheer",  
    cheer,  
    min_images=1,  
    max_images=1,  
    keywords=["欢呼"],  
    date_created=datetime(2026, 4, 1),  
    date_modified=datetime(2026, 4, 1),  
)
