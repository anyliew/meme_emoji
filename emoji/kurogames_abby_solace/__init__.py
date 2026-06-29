from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_abby_solace(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
    (7, 149), (7, 149), (7, 149), (7, 149), (7, 150),
    (7, 150), (7, 150), (7, 151), (7, 151), (7, 151),
    (7, 151), (7, 152), (7, 152), (7, 152), (7, 152),
    (7, 151), (7, 151), (7, 151), (7, 150), (7, 150),
    (7, 150), (7, 149), (7, 149), (7, 149)
    ]
    sizes = [
    (144, 109), (144, 109), (144, 109), (144, 109), (144, 109),
    (144, 109), (144, 109), (144, 109), (144, 109), (144, 109),
    (144, 109), (144, 109), (144, 109), (144, 109), (144, 109),
    (144, 109), (144, 109), (144, 109), (144, 109), (144, 109),
    (144, 109), (144, 109), (144, 109), (144, 109),
    ]
    for i in range(24):
        frame_num = (i % 24) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.08)
add_meme(
    "kurogames_abby_solace",  
    kurogames_abby_solace,  
    min_images=1,  
    max_images=1,  
    keywords=["安慰","阿布安慰"],  
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 10, 3),  
    date_modified=datetime(2025, 10, 3),  
)
