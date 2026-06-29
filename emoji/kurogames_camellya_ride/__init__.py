from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_camellya_ride(images: list[BuildImage], texts, args):
    user_head = images[0].resize((48, 48)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (101, 200), (100, 203), (98, 209), (93, 208), (84, 209),
        (77, 213), (77, 224), (87, 221), (104, 223), (109, 223),
        (106, 230), (92, 227), (75, 236), (70, 233), (71, 239),
        (81, 224), (92, 214), (96, 210), (92, 216), (78, 210),
        (67, 223), (71, 220), (74, 228), (90, 216), (111, 224),
        (113, 216), (101, 222), (80, 223), (73, 233), (79, 235),
        (94, 224), (116, 232), (117, 226), (108, 231), (99, 227),
        (87, 226), (88, 227), (94, 230), (107, 230), (108, 235),
        (107, 233), (97, 225), (80, 232), (73, 243), (79, 239),
        (95, 236), (121, 237), (130, 233), (124, 234), (118, 235)
    ]
    for i in range(11):
        frame_num = (i % 11) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "kurogames_camellya_ride",  
    kurogames_camellya_ride,  
    min_images=1,  
    max_images=1,  
    keywords=["椿骑","大傻椿骑"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 2, 16),  
    date_modified=datetime(2026, 2, 16),  
)
