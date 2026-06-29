from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG  
from pil_utils import BuildImage  
from meme_generator.tags import MemeTags
from meme_generator import add_meme  
from meme_generator.utils import save_gif  
img_dir = Path(__file__).parent / "images"
def mihoyo_sangonomiya_kokomi_love(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  
    frames: list[IMG] = []
    positions = [
    (239, 234), (243, 234), (250, 231), (258, 229), (260, 228),  
    (254, 230), (245, 233), (239, 234), (246, 233), (255, 230),  
    (260, 228), (257, 229), (248, 232), (245, 233), (239, 234),  
    (239, 234), (239, 234), (239, 234), (239, 234), (239, 234),  
    (239, 234), (239, 234), (239, 234), (239, 234), (239, 234),  
    (239, 234), (239, 234), (239, 234), (239, 234), (239, 234)   
    ]
    sizes = [
    (185, 144), (180, 145), (170, 155), (158, 164), (156, 167),
    (164, 159), (177, 148), (186, 144), (176, 150), (163, 160),
    (156, 167), (160, 163), (173, 156), (178, 147), (185, 144),
    (185, 144), (185, 144), (185, 144), (185, 144), (185, 144),
    (185, 144), (185, 144), (185, 144), (185, 144), (185, 144),
    (185, 144), (185, 144), (185, 144), (185, 144)
    ]
    for i in range(29):
        frame_num = (i % 29) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)
    return save_gif(frames, 0.04)
add_meme(
    "mihoyo_sangonomiya_kokomi_love",  
    mihoyo_sangonomiya_kokomi_love,  
    min_images=1,  
    max_images=1,  
    keywords=["心海爱心"],  
    tags=MemeTags.genshin,
    date_created=datetime(2025, 10, 2),  
    date_modified=datetime(2025, 10, 2),  
)
