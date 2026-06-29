from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_trampoline(images: list[BuildImage], texts, args):
    user_head = images[0].resize((79, 66)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (31, 94), (30, 96), (33, 68), (33, 66), (29, 65),  
        (32, 62), (31, 76), (31, 95), (30, 95), (30, 95),  
        (32, 67), (32, 66), (33, 65), (36, 65), (34, 74),  
    ]
    for i in range(15):
        frame_num = (i % 15) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "doro_trampoline",  
    doro_trampoline,  
    min_images=1,  
    max_images=1,  
    keywords=["跳床","蹦床","doro蹦床","桃乐丝蹦床","doro跳床","桃乐丝跳床"],  
    date_created=datetime(2025, 8, 1),  
    date_modified=datetime(2025, 8, 1),  
)
