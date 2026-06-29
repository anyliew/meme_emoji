from datetime import datetime
from pathlib import Path
from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage
img_dir = Path(__file__).parent / "images"
def wheelchair(images: list[BuildImage], texts, args):
    self_locs = [
        (303, 117), (303, 117), (303, 117), (303, 117), (304, 117),
        (313, 120), (330, 126), (352, 139), (366, 153), (365, 157),
        (353, 154), (330, 140), (309, 126), (304, 120), (304, 117),
        (303, 117), (302, 117), (302, 117), (303, 117), (303, 117)
    ]
    user_locs = [
        (167, 250), (167, 250), (167, 250), (167, 250), (168, 250),
        (173, 250), (181, 250), (186, 250), (185, 249), (180, 249),
        (169, 250), (161, 250), (157, 250), (161, 250), (167, 250),
        (167, 250), (167, 250), (167, 250), (167, 250), (167, 250)
    ]
    self_head = (
        images[0]
        .convert("RGBA")
        .resize((54, 54), keep_ratio=True)
        .rotate(-30)
    )
    base_user_head = (
        images[1]
        .convert("RGBA")
        .resize((124, 124), keep_ratio=True)
    )
    frames: list[IMG] = []
    for i in range(20):
        angle = -15 * (i + 1)
        user_head = base_user_head.rotate(angle)
        frame = BuildImage.open(img_dir / f"{i+1}.png")
        frame.paste(user_head, user_locs[i], alpha=True, below=True)
        frame.paste(self_head, self_locs[i], alpha=True, below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.02)
add_meme(
    "wheelchair",
    wheelchair,
    min_images=2,
    max_images=2,
    keywords=["轮椅"],
    date_created=datetime(2026, 5, 26),
    date_modified=datetime(2026, 5, 26),
)
