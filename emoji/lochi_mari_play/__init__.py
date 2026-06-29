from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def lochi_mari_play(images: list[BuildImage], texts, args):
    user_head = images[0].resize((62, 62)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (85, 178), (85, 178), (88, 177), (91, 178), (91, 178),  
        (86, 178), (86, 178), (86, 178), (86, 178), (86, 178),  
        (88, 178), (91, 179), (91, 179), (91, 179), (90, 178),  
        (87, 178),  
    ]
    for i in range(16):
        frame_num = (i % 16) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "lochi_mari_play",  
    lochi_mari_play,  
    min_images=1,  
    max_images=1,  
    keywords=["玛丽玩","伊落玛丽玩"],  
    tags=MemeTags.blue_archive,
    date_created=datetime(2025, 8, 8),  
    date_modified=datetime(2025, 8, 8),  
)
