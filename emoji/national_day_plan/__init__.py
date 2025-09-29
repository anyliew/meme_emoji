from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def national_day_plan(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    # 随机选择 0-3 张图片
    num_frames = random.randint(0, 3)
    
    # 定义不同图片的参数配置
    frame_configs = [
        {
            "frame_file": "0.png",
            "avatar_pos": (152, 28),
            "avatar_size": (210, 210),
            "text_bbox": (412, 28, 1175, 238),
            "font_families": ["FZXS14"]
        },
        {
            "frame_file": "1.png",  #鸣潮
            "avatar_pos": (18, 12),
            "avatar_size": (125, 125),
            "text_bbox": (152, 12, 694, 137),
            "font_families": ["FZXS14"]
        },
        {
            "frame_file": "2.png", #原神
            "avatar_pos": (54, 25),
            "avatar_size": (220, 220),
            "text_bbox": (300, 25, 1000, 240),
            "font_families": ["FZXS14"]
        },
        {
            "frame_file": "3.png", #使命召唤
            "avatar_pos": (38, 16),
            "avatar_size": (118, 118),
            "text_bbox": (168, 16, 697, 133),
            "font_families": ["FZXS14"]
        }
    ]

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の国庆计划"

    def make(imgs: list[BuildImage]) -> BuildImage:
        # 随机选择配置
        config = random.choice(frame_configs)
        
        # 加载底图
        frame = BuildImage.open(img_dir / config["frame_file"])
        
        # 绘制文本
        try:
            frame.draw_text(
                config["text_bbox"],
                text,
                fill=(0, 0, 0),
                max_fontsize=120,
                min_fontsize=15,
                lines_align="left",
                font_families=config["font_families"],
            )
        except ValueError:
            raise TextOverLength(name)

        # 处理头像
        img = imgs[0].convert("RGBA").circle().resize(config["avatar_size"])
        return frame.copy().paste(img, config["avatar_pos"], alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "national_day_plan",
    national_day_plan,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["国庆计划","国庆节计划"],
    date_created=datetime(2025, 9, 28),
    date_modified=datetime(2025, 9, 29),
)