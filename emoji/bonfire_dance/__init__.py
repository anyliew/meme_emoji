from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def bonfire_dance(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
        (167, 56), (167, 56), (167, 56), (167, 56), (139, 59),  
        (139, 59), (139, 59), (129, 82), (111, 68), (111, 68),  
        (111, 68), (111, 68), (84, 61), (84, 61), (72, 95),  
        (72, 95), (72, 95), (69, 101), (69, 101), (63, 107),  
        (63, 107), (60, 122), (60, 122), (60, 122), (62, 156),  
        (62, 156), (63, 177), (63, 177), (63, 177), (66, 170),  
        (66, 170), (66, 170), (63, 206), (63, 206), (93, 245),  
        (93, 245), (136, 267), (136, 267), (136, 267), (154, 261),  
        (154, 261), (184, 259), (184, 259), (200, 285), (200, 285),  
        (200, 285), (194, 229), (194, 229), (196, 225), (196, 225),  
        (196, 225), (199, 286), (199, 286), (194, 230), (195, 230),  
        (195, 230), (195, 224), (195, 224), (200, 286), (200, 286),  
        (228, 275),   
    ]
    sizes = [
    (110, 110), (110, 110), (110, 110), (110, 110), (110, 110),  
    (110, 110), (110, 110), (110, 110), (110, 110), (110, 110),  
    (110, 110), (110, 110), (110, 110), (110, 110), (110, 110),  
    (110, 110), (110, 110), (110, 110), (110, 110), (110, 110),  
    (110, 110), (110, 110), (110, 110), (110, 110), (110, 110),  
    (110, 110), (110, 110), (110, 110), (110, 110), (110, 110),  
    (110, 110), (110, 110), (126, 126), (126, 126), (126, 126),  
    (126, 126), (126, 126), (126, 126), (126, 126), (126, 126),  
    (126, 126), (126, 126), (126, 126), (126, 126), (126, 126),  
    (126, 126), (126, 126), (126, 126), (126, 126), (126, 126),  
    (126, 126), (126, 126), (126, 126), (126, 126), (126, 126),  
    (126, 126), (126, 126), (126, 126), (126, 126), (126, 126),  
    (126, 126),   
    ]
    for i in range(61):
        frame_num = (i % 61) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "bonfire_dance",  
    bonfire_dance,  
    min_images=1,  
    max_images=1,  
    keywords=["篝火舞","圈舞"],  
    date_created=datetime(2025, 9, 27),  
    date_modified=datetime(2025, 9, 27),  
)
