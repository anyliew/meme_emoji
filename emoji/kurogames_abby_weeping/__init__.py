from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_abby_weeping(images: list[BuildImage], texts, args):
    user_head = images[0].resize((80, 80)).convert("RGBA").circle()
    frames: list[IMG] = []
    positions = [
        (2, 77), (2, 75), (2, 73), (2, 72), (2, 70),  
        (2, 70), (2, 70), (2, 70), (2, 70), (2, 70),  
        (2, 70), (2, 70), (2, 70), (2, 70), (2, 70),  
        (2, 70),  
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
    "kurogames_abby_weeping",  
    kurogames_abby_weeping,  
    min_images=1,  
    max_images=1,  
    keywords=["抱头痛哭"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 15),  
    date_modified=datetime(2025, 7, 15),  
)
