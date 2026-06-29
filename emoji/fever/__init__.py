from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def fever(images: list[BuildImage], texts, args):
    user_head = images[0].resize((155, 100)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (74, 222), (73, 237), (73, 253), (74, 258), (73, 253),  
        (76, 249), (76, 231), (76, 231), (76, 250), (74, 257),  
        (74, 258), (73, 253), (75, 235),  
    ]
    for i in range(13):
        frame_num = (i % 13) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.09)
add_meme(
    "fever",  
    fever,  
    min_images=1,  
    max_images=1,  
    keywords=["为爱发烧","发烧"],  
    date_created=datetime(2025, 7, 17),  
    date_modified=datetime(2025, 7, 17),  
)
