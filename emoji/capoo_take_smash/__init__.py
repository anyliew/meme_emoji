from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def capoo_take_smash(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
    (95, 155), (84, 194), (80, 204), (95, 155), (84, 194),
    (80, 204), (95, 155), (84, 194), (80, 204), (95, 155),
    (84, 116), (80, 204), (95, 155), (84, 194), (80, 204),
    (95, 155), (84, 194), (80, 204), (95, 155), (84, 194)
    ]
    sizes = [
    (49, 81), (86, 51), (74, 32), (49, 81), (86, 51),
    (74, 32), (49, 81), (86, 51), (74, 32), (49, 81),
    (86, 129), (74, 32), (49, 81), (86, 51), (74, 32),
    (49, 81), (86, 51), (74, 32), (49, 81), (86, 51)
    ]
    for i in range(20):
        frame_num = (i % 20) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "capoo_take_smash",  
    capoo_take_smash,  
    min_images=1,  
    max_images=1,  
    keywords=["咖波砸"],  
    tags=MemeTags.capoo,
    date_created=datetime(2025, 10, 3),  
    date_modified=datetime(2025, 10, 3),  
)
