from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def finger(images: list[BuildImage], texts, args):
    user_head = images[0].resize((94, 94)).convert("RGBA").circle()
    frames: list[IMG] = []
    position = (241, 11)
    for i in range(93):
        frame_num = (i % 93) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, position, alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "finger",  
    finger,  
    min_images=1,  
    max_images=1,  
    keywords=["指"],  
    date_created=datetime(2026, 1, 13),  
    date_modified=datetime(2026, 1, 13),  
)
