from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif
img_dir = Path(__file__).parent / "images"
def kurogames_roccia_draw(images: list[BuildImage], texts, args):
    user_head = images[0].convert("RGBA")
    frames: list[IMG] = []
    positions = [None] * 74
    resize_dimensions = [None] * 74
    positions[31] = (131, 265)
    positions[32] = (128, 262)
    positions[33] = (129, 261)
    positions[34] = (127, 256)
    positions[35] = (128, 250)
    positions[36] = (131, 246)
    positions[37] = (135, 242)
    positions[38] = (140, 238)
    positions[39] = (147, 235)
    positions[40] = (153, 233)
    positions[41] = (159, 230)
    positions[42] = (164, 229)
    positions[43] = (168, 228)
    positions[44] = (171, 227)
    positions[45] = (172, 227)
    positions[46] = (172, 226)
    positions[47] = (172, 225)
    positions[48] = (172, 225)
    positions[49] = (172, 224)
    positions[50] = (172, 224)
    positions[51] = (173, 223)
    positions[52] = (172, 223)
    positions[53] = (172, 223)
    positions[54] = (172, 223)
    positions[55] = (172, 223)
    positions[56] = (172, 223)
    positions[57] = (172, 223)
    positions[58] = (172, 223)
    positions[59] = (172, 223)
    positions[60] = (172, 223)
    positions[61] = (172, 223)
    positions[62] = (172, 223)
    positions[63] = (172, 223)
    positions[64] = (172, 223)
    positions[65] = (172, 223)
    positions[66] = (172, 223)
    positions[67] = (172, 223)
    positions[68] = (172, 223)
    positions[69] = (172, 223)
    positions[70] = (172, 223)
    positions[71] = (172, 223)
    positions[72] = (172, 223)
    positions[73] = (172, 223)
    resize_dimensions[31] = (43, 35)
    resize_dimensions[32] = (49, 38)
    resize_dimensions[33] = (50, 39)
    resize_dimensions[34] = (59, 44)
    resize_dimensions[35] = (65, 50)
    resize_dimensions[36] = (70, 52)
    resize_dimensions[37] = (74, 53)
    resize_dimensions[38] = (77, 53)
    resize_dimensions[39] = (78, 54)
    resize_dimensions[40] = (78, 53)
    resize_dimensions[41] = (79, 54)
    resize_dimensions[42] = (79, 54)
    resize_dimensions[43] = (80, 54)
    resize_dimensions[44] = (79, 55)
    resize_dimensions[45] = (79, 54)
    resize_dimensions[46] = (79, 55)
    resize_dimensions[47] = (79, 55)
    resize_dimensions[48] = (79, 54)
    resize_dimensions[49] = (79, 55)
    resize_dimensions[50] = (79, 54)
    resize_dimensions[51] = (78, 55)
    resize_dimensions[52] = (79, 55)
    resize_dimensions[53] = (79, 55)
    resize_dimensions[54] = (79, 55)
    resize_dimensions[55] = (79, 55)
    resize_dimensions[56] = (79, 55)
    resize_dimensions[57] = (79, 55)
    resize_dimensions[58] = (79, 55)
    resize_dimensions[59] = (80, 55)
    resize_dimensions[60] = (79, 55)
    resize_dimensions[61] = (79, 55)
    resize_dimensions[62] = (79, 55)
    resize_dimensions[63] = (79, 55)
    resize_dimensions[64] = (79, 55)
    resize_dimensions[65] = (79, 55)
    resize_dimensions[66] = (79, 55)
    resize_dimensions[67] = (79, 55)
    resize_dimensions[68] = (79, 55)
    resize_dimensions[69] = (79, 55)
    resize_dimensions[70] = (79, 55)
    resize_dimensions[71] = (79, 55)
    resize_dimensions[72] = (79, 55)
    resize_dimensions[73] = (79, 55)
    for i in range(74):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        new_frame = BuildImage.new("RGBA", frame.size)
        if i >= 31 and positions[i] is not None and resize_dimensions[i] is not None:
            resized_head = user_head.resize(resize_dimensions[i], keep_ratio=True)
            new_frame.paste(resized_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.03)
add_meme(
    "kurogames_roccia_draw",
    kurogames_roccia_draw,
    min_images=1,
    max_images=1,
    keywords=["洛可可画画"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 5, 8),
    date_modified=datetime(2026, 5, 8),
)
