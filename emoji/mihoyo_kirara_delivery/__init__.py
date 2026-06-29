from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def mihoyo_kirara_delivery(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
    (226, 74), (226, 74), (226, 74), (226, 74)
    ]
    sizes = [
    (141, 120), (141, 120), (141, 120), (141, 120)
    ]
    for i in range(4):
        frame_num = (i % 4) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "mihoyo_kirara_delivery",  
    mihoyo_kirara_delivery,  
    min_images=1,  
    max_images=1,  
    keywords=["绮良良派送","派送"],  
    tags=MemeTags.genshin,
    date_created=datetime(2025, 12, 5),  
    date_modified=datetime(2025, 12, 5),  
)
