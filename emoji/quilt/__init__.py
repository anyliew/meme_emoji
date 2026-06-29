from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def quilt(images: list[BuildImage], texts, args):
    user_head = images[0].resize((142, 146)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (68, 68), (68, 68), (68, 72), (69, 74), (69, 74),  
        (69, 73), (69, 72), (69, 74), (68, 72), (68, 68),  
        (68, 68), (68, 68), (68, 72), (68, 72), (69, 73),  
        (69, 73), (69, 73), (69, 75), (68, 72), (68, 68),  
        (68, 68),  
    ]
    for i in range(21):
        frame_num = (i % 21) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "quilt",  
    quilt,  
    min_images=1,  
    max_images=1,  
    keywords=["被窝"],  
    date_created=datetime(2025, 9, 12),  
    date_modified=datetime(2025, 9, 12),  
)
