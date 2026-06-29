from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_iuno_peeking(images: list[BuildImage], texts, args):
    user_head = images[0].resize((505, 505)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (324, 0), (324, 0), (324, 0), (324, 0), (324, 0),
        (324, 0), (324, 0), (324, 0), (324, 0), (324, 0),
        (324, 0), (324, 0), (324, 0), (324, 0), (324, 0),
        (324, 0), (324, 0), (324, 0), (324, 0), (324, 0),
        (324, 0), (324, 0), (324, 0), (324, 0), (324, 0),
        (324, 0), (324, 0), (324, 0), (324, 0), (324, 0),
        (324, 0), (324, 0), (324, 0),
    ]
    for i in range(33):
        frame_num = (i % 33) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "kurogames_iuno_peeking",  
    kurogames_iuno_peeking,  
    min_images=1,  
    max_images=1,  
    keywords=["尤诺探头"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 1, 12),  
    date_modified=datetime(2026, 1, 12),  
)
