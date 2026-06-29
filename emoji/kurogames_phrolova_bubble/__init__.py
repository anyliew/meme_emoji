from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif
img_dir = Path(__file__).parent / "images"
def kurogames_phrolova_bubble(images: list[BuildImage], texts, args):
    frames: list[IMG] = []
    positions_raw = [
        (299, 298), (310, 297), (316, 295), (321, 292), (325, 288),
        (328, 282), (330, 274), (330, 264), (329, 252), (328, 238),
        (324, 222), (322, 207), (320, 192), (319, 177), (315, 160),
        (315, 148), (316, 136), (318, 126), (319, 115), (320, 105),
        (323, 98), (327, 91), (328, 83), (332, 77), (333, 71),
        (336, 66), (339, 62), (339, 57), (340, 54), (341, 51),
        (339, 47), (339, 45), (339, 43), (339, 42), (336, 39),
        (335, 39), (346, 49), (288, 283), (287, 286), (286, 288),
        (287, 291), (286, 292), (299, 296), (299, 298)
    ]
    sizes_raw = [
        (125, 125), (125, 125), (125, 125), (125, 125), (125, 125),
        (125, 125), (125, 125), (126, 126), (126, 126), (126, 126),
        (130, 130), (130, 130), (130, 130), (130, 130), (137, 137),
        (137, 137), (137, 137), (138, 138), (140, 140), (143, 143),
        (143, 143), (143, 143), (147, 147), (147, 147), (151, 151),
        (151, 151), (151, 151), (155, 155), (155, 155), (155, 155),
        (159, 159), (159, 159), (159, 159), (159, 159), (162, 162),
        (162, 162), (138, 138), (125, 124), (131, 123), (134, 124),
        (133, 123), (133, 124), (120, 120), (124, 124)
    ]
    positions = [(x - 5, y - 5) for x, y in positions_raw]
    sizes = [(w + 10, h + 10) for w, h in sizes_raw]
    extra_positions_raw = {
        32: (300, 262),
        33: (294, 265),
        34: (292, 270),
        35: (292, 273),
        36: (288, 276),
        37: (286, 280),
    }
    extra_sizes_raw = {
        32: (64, 128),
        33: (70, 126),
        34: (83, 127),
        35: (94, 125),
        36: (111, 127),
        37: (120, 126),
    }
    extra_positions = {k: (x - 5, y - 5) for k, (x, y) in extra_positions_raw.items()}
    extra_sizes = {k: (w + 10, h + 10) for k, (w, h) in extra_sizes_raw.items()}
    for i in range(44):
        frame_num = (i % 44) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        head1 = images[0].resize(sizes[i], keep_ratio=True).convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(head1, positions[i], alpha=True)
        if frame_num in extra_positions:
            head2 = images[0].resize(extra_sizes[frame_num], keep_ratio=True).convert("RGBA")
            new_frame.paste(head2, extra_positions[frame_num], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "kurogames_phrolova_bubble",
    kurogames_phrolova_bubble,
    min_images=1,
    max_images=1,
    keywords=["弗洛洛吹泡泡", "吹泡泡"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 6, 19),
    date_modified=datetime(2026, 6, 19),
)
