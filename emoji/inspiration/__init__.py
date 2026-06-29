from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def inspiration(images: list[BuildImage], texts, args):
    user_head = images[0].resize((112, 112)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [(50, 50)] * 15
    for i in range(15):
        frame_num = (i % 15) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "inspiration",  
    inspiration,  
    min_images=1,  
    max_images=1,  
    keywords=["灵机一现","灵感","灵光一动"],  
    date_created=datetime(2026, 6, 29),  
    date_modified=datetime(2026, 6, 29),
)
