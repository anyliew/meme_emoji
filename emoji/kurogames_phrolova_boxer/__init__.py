from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_phrolova_boxer(images: list[BuildImage], texts, args):
    user_head = images[0].resize((100, 100), keep_ratio=True).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (164, 162), (143, 151), (165, 163), (141, 152),
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.1)
add_meme(
    "kurogames_phrolova_boxer",  
    kurogames_phrolova_boxer,  
    min_images=1,  
    max_images=1,  
    keywords=["弗洛洛拳击"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 1, 12),  
    date_modified=datetime(2026, 1, 12),  
)
