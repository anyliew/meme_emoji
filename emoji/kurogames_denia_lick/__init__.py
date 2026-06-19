from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

positions = [
    (45, 299), (45, 297), (44, 295), (43, 293), (41, 292),
    (39, 292), (37, 291), (35, 292), (34, 293), (31, 296),
    (30, 299), (30, 301), (29, 304), (31, 306), (31, 308),
    (32, 310), (33, 311), (35, 311), (37, 311), (39, 311),
    (41, 309), (43, 306), (45, 304), (45, 302)
]

sizes = [
    (153, 153), (153, 153), (153, 153), (153, 153), (153, 153),
    (153, 153), (153, 153), (153, 153), (153, 153), (153, 153),
    (153, 153), (153, 153), (153, 153), (153, 153), (153, 153),
    (153, 153), (153, 153), (153, 153), (153, 153), (153, 153),
    (153, 153), (153, 153), (153, 153), (153, 153)
]

def kurogames_denia_lick(images: list[BuildImage], texts, args):
    frames: list[IMG] = []
    for i in range(24):
        frame = BuildImage.open(img_dir / f"{i+1}.png").convert("RGBA")
        user_head = images[0].resize(sizes[i], keep_ratio=True).convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)

add_meme(
    "kurogames_denia_lick",
    kurogames_denia_lick,
    min_images=1,
    max_images=1,
    keywords=["达妮娅舔"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 6, 19),
    date_modified=datetime(2026, 6, 19),
)