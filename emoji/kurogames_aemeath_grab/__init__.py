from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif
img_dir = Path(__file__).parent / "images"
def kurogames_aemeath_grab(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (9, 91), (9, 91), (9, 91), (8, 91), (8, 91),
        (8, 91), (8, 91), (8, 91), (8, 91), (8, 91),
        (8, 91), (8, 91), (9, 91), (8, 91), (12, 130),
        (19, 153), (19, 159), (19, 156), (18, 169), (19, 181),
        (19, 172), (19, 161), (19, 165), (19, 169), (19, 169),
        (19, 169), (19, 169), (19, 169), (19, 169), (19, 169),
        (19, 169), (19, 169), (19, 169), (19, 169), (19, 169),
        (19, 169)
    ]
    sizes = [
        (244, 209), (244, 209), (244, 209), (245, 209), (245, 209),
        (245, 209), (246, 209), (245, 209), (245, 209), (245, 209),
        (245, 209), (246, 209), (245, 209), (245, 209), (188, 170),
        (145, 147), (133, 141), (127, 144), (125, 131), (124, 119),
        (124, 128), (124, 139), (124, 135), (125, 131), (125, 131),
        (125, 131), (125, 131), (125, 131), (127, 131), (125, 131),
        (125, 131), (125, 131), (125, 131), (125, 131), (125, 131),
        (125, 131)
    ]
    for i in range(36):
        frame_num = (i % 36) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        resized_user = user_img.resize(sizes[i], keep_ratio=True)
        new_frame.paste(resized_user, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.06)
add_meme(
    "kurogames_aemeath_grab",
    kurogames_aemeath_grab,
    min_images=1,
    max_images=1,
    keywords=["爱弥斯抓"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 6, 10),
    date_modified=datetime(2026, 6, 10),
)
