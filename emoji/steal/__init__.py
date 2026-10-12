from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [(61, 34)]
sizes = [(376, 376)]

def steal(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 1
    for i in range(total_frames):
        frame = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        pos = positions[i]
        size = sizes[i]
        user_head = user_img.resize(size).circle()
        new_frame.paste(user_head, pos, alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.13)

add_meme(
    "steal",
    steal,
    min_images=1,
    max_images=1,
    keywords=["偷"],
    date_created=datetime(2026, 3, 31),
    date_modified=datetime(2026, 10, 12),
)