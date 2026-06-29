from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_mornye_raise(images: list[BuildImage], texts, args):
    frames: list[IMG] = []
    positions = [
        (92, 281), (92, 281), (91, 280), (91, 279), (91, 279),
        (90, 277), (89, 276), (88, 274), (87, 272), (86, 270),
        (85, 269), (84, 267), (84, 266), (83, 264), (82, 263),
        (82, 263), (81, 263), (81, 263), (81, 263), (81, 263),
        (81, 263), (81, 263), (81, 263), (81, 263), (81, 263),
        (81, 263), (81, 263), (81, 263), (81, 263)
    ]
    for i in range(29):
        frame_num = (i % 29) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        user_head = images[0].resize((176, 176)).convert("RGBA")
        if i < 13:
            user_head = user_head.rotate(13, expand=False)
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "kurogames_mornye_raise",  
    kurogames_mornye_raise,  
    min_images=1,  
    max_images=1,  
    keywords=["莫宁举"],  
    date_created=datetime(2026, 1, 20),  
    date_modified=datetime(2026, 1, 20),  
)
