from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def ikun_kfc(images: list[BuildImage], texts, args):
    frames: list[IMG] = []
    positions = [
        (51, 51), (53, 51), (59, 44), (60, 0), (64, 0),
        (69, 36), (71, 33), (69, 36), (64, 0), (60, 0),
        (59, 44), (53, 51)
    ]
    sizes = [
        (184, 121), (175, 121), (170, 119), (161, 161), (169, 159),
        (166, 122), (163, 118), (166, 122), (169, 159), (161, 161),
        (170, 119), (175, 121)
    ]
    for i in range(12):
        frame_num = (i % 12) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        user_head = images[0].resize(sizes[i]).convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "ikun_kfc",  
    ikun_kfc,  
    min_images=1,  
    max_images=1,  
    keywords=["肯德坤"],  
    date_created=datetime(2025, 12, 11),  
    date_modified=datetime(2025, 12, 11),  
)
