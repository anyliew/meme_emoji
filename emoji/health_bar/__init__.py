from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def health_bar(images: list[BuildImage], texts, args):
    user_head = images[0].resize((210, 210)).convert("RGBA")
    
    frames: list[IMG] = []

    positions = [(7, 10)] * 435

    for i in range(435):
        frame_num = (i % 435) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    return save_gif(frames, 0.03)

add_meme(
    "health_bar",
    health_bar,
    min_images=1,
    max_images=1,
    keywords=["血条","HP","hp"],
    date_created=datetime(2026, 3, 30),
    date_modified=datetime(2026, 3, 30),
)