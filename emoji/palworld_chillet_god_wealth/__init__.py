from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def palworld_chillet_god_wealth(images: list[BuildImage], texts, args):
    user_head = images[0].resize((205, 205)).convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (139, 167), (139, 160), (156, 154), (177, 153), (198, 156),  
        (215, 160), (223, 163), (219, 168), (188, 157), (164, 156)   
    ]
    for i in range(10):
        frame_num = (i % 10) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.08)
add_meme(
    "palworld_chillet_god_wealth",  
    palworld_chillet_god_wealth,  
    min_images=1,  
    max_images=1,  
    keywords=["财源滚滚","财神到"],  
    date_created=datetime(2025, 9, 28),  
    date_modified=datetime(2025, 9, 28),  
)
