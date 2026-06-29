from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def kurogames_chisa_creative_pioneer(images: list[BuildImage], texts, args):
    user_head = images[0].resize((164, 164)).convert("RGBA").circle()
    frames: list[IMG] = []
    positions = [(47, 47)] * 90
    for i in range(90):
        frame_num = (i % 90) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.07)
add_meme(
    "kurogames_chisa_creative_pioneer",  
    kurogames_chisa_creative_pioneer,  
    min_images=1,  
    max_images=1,  
    keywords=["创作先锋"],  
    date_created=datetime(2026, 2, 16),  
    date_modified=datetime(2026, 2, 16),  
)
