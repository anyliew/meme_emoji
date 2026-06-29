from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_zani_aloft(images: list[BuildImage], texts, args):
    user_head = images[0].resize((203, 203)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (-16, 13), (-16, 13), (-16, 118), (31, 156), (25, 159),  
        (85, 182), (162, 157), (195, 111), (194, 110), (200, 4),  
        (106, -42), (106, -42), (85, -42), 
    ]
    for i in range(13):
        frame_num = (i % 13) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "kurogames_zani_aloft",  
    kurogames_zani_aloft,  
    min_images=1,  
    max_images=1,  
    keywords=["赞妮举"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 8, 25),  
    date_modified=datetime(2025, 8, 25),  
)
