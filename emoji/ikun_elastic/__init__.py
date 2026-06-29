from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def ikun_elastic(images: list[BuildImage], texts, args):
    user_head = images[0].resize((112, 112)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (89, 82), (90, 83), (87, 83), (87, 83), (87, 83),
        (87, 83), (86, 84), (87, 84), (89, 84), (92, 87),
        (95, 88), (94, 86), (88, 83)
    ]
    for i in range(13):
        frame_num = (i % 13) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "ikun_elastic",  
    ikun_elastic,  
    min_images=1,  
    max_images=1,  
    keywords=["弹坤"],  
    date_created=datetime(2025, 12, 11),  
    date_modified=datetime(2025, 12, 11),  
)
