from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_abby_play(images: list[BuildImage], texts, args):
    user_head = images[0].resize((177, 177)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (794, 402), (787, 402), (786, 402), (787, 423), (789, 354), 
        (787, 262), (791, 172), (793, 128), (793, 131), (792, 140), 
        (793, 154), (793, 174), (794, 198), (793, 223), (792, 250), 
        (790, 276), (793, 301), (793, 330), (793, 352), (793, 373), 
        (793, 390), (796, 399), (796, 402), (794, 403), (790, 422), 
        (794, 354), (797, 264), (797, 174), (796, 124), (796, 127), 
        (793, 138), (793, 157), (793, 180), (793, 204), (793, 232), 
        (793, 265), (793, 291), (793, 322), (793, 348), (793, 368), 
        (793, 387), (792, 399), (792, 402), (792, 402), (792, 402), 
        (793, 402), (793, 402) 
    ]
    for i in range(47):
        frame_num = (i % 47) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "kurogames_abby_play",  
    kurogames_abby_play,  
    min_images=1,  
    max_images=1,  
    keywords=["阿布顶","阿布玩"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 2, 16),  
    date_modified=datetime(2026, 2, 16),  
)
