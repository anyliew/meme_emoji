from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif
img_dir = Path(__file__).parent / "images"
def kurogames_sigrika_love(images: list[BuildImage], texts, args):
    user_head = images[0].convert("RGBA")
    frames: list[IMG] = []
    positions = [
        (126, 388), (128, 393), (129, 405), (127, 420), (123, 433),
        (119, 438), (115, 437), (112, 433), (115, 427), (124, 418),
        (129, 405), (129, 391), (129, 387), (129, 396), (129, 414),
        (126, 438), (120, 439), (115, 437), (108, 430), (112, 413)
    ]
    sizes = [
        (253, 112), (249, 107), (247, 95), (251, 80), (259, 67),
        (266, 62), (274, 63), (279, 67), (274, 73), (257, 82),
        (247, 95), (247, 109), (247, 113), (247, 104), (248, 86),
        (253, 62), (264, 61), (274, 63), (286, 70), (279, 87)
    ]
    for i in range(20):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        resized_head = user_head.resize((width, height), keep_ratio=True).convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(resized_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "kurogames_sigrika_love",
    kurogames_sigrika_love,
    min_images=1,
    max_images=1,
    keywords=["西格莉卡喜欢","耙耙柑喜欢"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 5, 8),
    date_modified=datetime(2026, 5, 8),
)
