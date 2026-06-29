from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def sending_love(images: list[BuildImage], texts, args):
    user_head = images[0].resize((159, 128)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (76, 76), (84, 78), (76, 76), (67, 76), (76, 76),  
        (76, 78), (75, 82), (75, 82), (75, 82), (75, 82),  
        (75, 82), (75, 82), (75, 82), (75, 82), (75, 82),  
    ]
    for i in range(15):
        frame_num = (i % 15) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.16)
add_meme(
    "sending_love",  
    sending_love,  
    min_images=1,  
    max_images=1,  
    keywords=["比心"],  
    date_created=datetime(2025, 9, 12),  
    date_modified=datetime(2025, 9, 12),  
)
