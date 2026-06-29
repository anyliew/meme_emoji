from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_iuno_kick(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
        (88, 40), (88, 40), (122, 49), (134, 54), (142, 61),  
        (142, 69), (129, 78), (111, 78), (96, 78), (66, 70),  
        (29, 54), (26, 47), (29, 46), (43, 39), (75, 10),     
        (86, 0), (90, -10), (94, -16), (92, -12), (85, -4),   
        (59, 30), (45, 41), (29, 47), (26, 48), (42, 63),     
        (67, 71), (96, 77), (111, 78), (137, 74), (142, 69),  
        (141, 61), (135, 54), (102, 44), (89, 39),            
    ]
    sizes = [
        (108, 108), (108, 108), (105, 105), (105, 105), (105, 105),  
        (110, 110), (105, 105), (110, 110), (110, 110), (112, 112),  
        (108, 108), (105, 105), (96, 96), (86, 86), (70, 70),  
        (67, 67), (61, 61), (58, 58), (62, 62), (66, 66),  
        (77, 77), (84, 84), (97, 97), (105, 105), (110, 110),  
        (110, 110), (110, 110), (110, 110), (105, 105), (105, 105),  
        (105, 105), (105, 105), (105, 105), (105, 105),              
    ]
    for i in range(34):
        frame_num = (i % 34) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "kurogames_iuno_kick",  
    kurogames_iuno_kick,  
    min_images=1,  
    max_images=1,  
    keywords=["尤诺踢","优诺踢"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 31),  
    date_modified=datetime(2025, 8, 1),  
)
