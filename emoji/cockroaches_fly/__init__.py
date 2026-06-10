from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def cockroaches_fly(images: list[BuildImage], texts, args):
    user_head = images[0].convert("RGBA")
    frames: list[IMG] = []

    positions = [
        (121, 307), (121, 307), (121, 307), (121, 306), (121, 306),
        (120, 304), (120, 304), (119, 302), (119, 302), (119, 298),
        (119, 295), (118, 294), (118, 291), (118, 290), (127, 284),
        (136, 278), (146, 272), (156, 265), (166, 262), (172, 257),
        (183, 250), (192, 245), (203, 237), (203, 233), (203, 232),
        (204, 229), (204, 228), (198, 226), (197, 222), (197, 220),
        (191, 216), (191, 215), (182, 203), (182, 203), (174, 190),
        (170, 189), (162, 176), (150, 164), (150, 164), (145, 150),
        (145, 150), (135, 135), (135, 135), (124, 125), (123, 123),
        (123, 115), (115, 108), (116, 108), (116, 99), (116, 99),
        (87, 71), (87, 71)
    ]

    sizes = [
        (4, 4), (4, 4), (4, 4), (5, 5), (5, 5),
        (6, 6), (6, 6), (9, 9), (9, 9), (9, 9),
        (9, 9), (10, 10), (11, 11), (11, 11), (11, 11),
        (15, 15), (15, 15), (15, 15), (15, 15), (23, 23),
        (23, 23), (23, 23), (23, 23), (30, 30), (30, 30),
        (30, 30), (30, 30), (41, 41), (46, 46), (46, 46),
        (61, 61), (61, 61), (82, 82), (82, 82), (97, 97),
        (105, 105), (123, 123), (146, 146), (146, 146), (159, 159),
        (159, 159), (181, 181), (181, 181), (203, 203), (203, 203),
        (203, 203), (220, 220), (220, 220), (220, 220), (220, 220),
        (277, 277), (277, 277)
    ]

    for i in range(61):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)

        if 8 <= frame_num <= 59:
            idx = frame_num - 8
            pos = positions[idx]
            size = sizes[idx]
            resized_head = user_head.resize(size)
            new_frame.paste(resized_head, pos, alpha=True)

        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.07)

add_meme(
    "cockroaches_fly",
    cockroaches_fly,
    min_images=1,
    max_images=1,
    keywords=["飞天小强","飞天蟑螂"],
    date_created=datetime(2026, 6, 10),
    date_modified=datetime(2026, 6, 10),
)