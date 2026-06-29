from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_iuno_play(images: list[BuildImage], texts, args):
    user_head = images[0].resize((130, 130)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (199, 26), (214, 26), (240, 37), (254, 44), (266, 48), (266, 57), (258, 65), (247, 70), (229, 70), (212, 70), (176, 61), (149, 52), (129, 36), (118, 30), (120, 21), (141, 13), 
    ]
    for i in range(16):
        frame_num = (i % 16) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.09)
add_meme(
    "kurogames_iuno_play",  
    kurogames_iuno_play,  
    min_images=1,  
    max_images=1,  
    keywords=["尤诺玩", "优诺玩"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 30),  
    date_modified=datetime(2025, 7, 30),  
)
