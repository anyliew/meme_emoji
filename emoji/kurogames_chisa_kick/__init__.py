from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_chisa_kick(images: list[BuildImage], texts, args):
    user_head = images[0].resize((84, 84)).convert("RGBA")  
    frames: list[IMG] = []
    positions = [
        (321, 82), (321, 82), (320, 77), (321, 80), (321, 85),
        (322, 90), (321, 85), (317, 78), (313, 78), (309, 81),
        (307, 85), (306, 83), (303, 79), (301, 78), (298, 79),
        (294, 81), (294, 84), (294, 91), (303, 97), (329, 99),
        (368, 102), (397, 105), (397, 105), (397, 105)
    ]
    for i in range(33):
        frame_num = (i % 33) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        if i < len(positions):
            new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "kurogames_chisa_kick",  
    kurogames_chisa_kick,  
    min_images=1,  
    max_images=1,  
    keywords=["千咲踢"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 12, 1),  
    date_modified=datetime(2025, 12, 30),  
)
