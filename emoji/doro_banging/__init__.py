from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def doro_banging(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
        (149, 109), (149, 109), (149, 109), (139, 133), (134, 140),
        (143, 127), (149, 109), (149, 109), (149, 109), (149, 109),
        (149, 109)
    ]
    sizes = [
        (82, 82), (82, 82), (82, 82), (102, 52), (112, 45),
        (89, 60), (82, 82), (82, 82), (82, 82), (82, 82),
        (82, 82)
    ]
    for i in range(11):
        frame_num = (i % 11) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "doro_banging",  
    doro_banging,  
    min_images=1,  
    max_images=1,  
    keywords=["doro敲","Doro敲","桃乐丝敲"],  
    date_created=datetime(2026, 1, 20),  
    date_modified=datetime(2026, 1, 20),  
)
