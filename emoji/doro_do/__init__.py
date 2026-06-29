from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_do(images: list[BuildImage], texts, args):
    user_head = images[0].resize((640, 640)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (0, 600), (0, 645), (0, 680), (0, 720),
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.05)
add_meme(
    "doro_do",  
    doro_do,  
    min_images=1,  
    max_images=1,  
    keywords=["doro撅","Doro撅","桃乐丝撅"],  
    date_created=datetime(2026, 1, 15),  
    date_modified=datetime(2026, 1, 15),  
)
