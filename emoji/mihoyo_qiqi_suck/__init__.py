from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def mihoyo_qiqi_suck(images: list[BuildImage], texts, args):
    user_head = images[0].resize((155, 155)).convert("RGBA") 
    frames: list[IMG] = []
    positions = [
        (78, 641), (92, 617), (123, 589), (144, 550), (230, 542),  
        (328, 546), (375, 552), (375, 552), (375, 552), (375, 552),  
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  
        (375, 552), (375, 552), (375, 552), (327, 546), (229, 542),  
        (143, 548), (122, 588), (91, 616), (77, 640), (77, 640),  
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  
        (77, 640), (77, 640), (77, 640),  
    ]
    for i in range(68):
        frame_num = (i % 68) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "mihoyo_qiqi_suck",  
    mihoyo_qiqi_suck,  
    min_images=1,  
    max_images=1,  
    keywords=["七七舔"],  
    tags=MemeTags.genshin,
    date_created=datetime(2025, 8, 13),  
    date_modified=datetime(2025, 8, 13),  
)
