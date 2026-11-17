from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (266, 35), (266, 35), (266, 35), (266, 35), (265, 35),
    (265, 35), (263, 35), (261, 35), (258, 35), (251, 30),
    (248, 30), (244, 27), (241, 27), (238, 26), (233, 24),
    (230, 23), (226, 21), (221, 20), (222, 20), (223, 19),
    (219, 19), (217, 18), (217, 19), (223, 18), (221, 18),
    (215, 18), (219, 17), (216, 17), (214, 17), (215, 15),
    (216, 15), (213, 15), (213, 15), (217, 13), (222, 13),
    (222, 13), (226, 13), (228, 13)
]

sizes = [(78, 78)] * 38

def nailoong_scratchead(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames = []
    total_frames = 38
    for i in range(1, total_frames + 1):
        frame = BuildImage.open(img_dir / f"{i}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        idx = i - 1
        pos = positions[idx]
        size = sizes[idx]
        user_head = user_img.resize(size)
        new_frame.paste(user_head, pos, alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.07)

add_meme(
    "nailoong_scratchead",
    nailoong_scratchead,
    min_images=1,
    max_images=1,
    keywords=["奶龙挠痒痒", "挠痒痒"],
    date_created=datetime(2026, 11, 17),
    date_modified=datetime(2026, 11, 17),
)