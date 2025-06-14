from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"

def oral_sex(images: list[BuildImage], texts, args):
    # 坐标参数保持不变
    self_locs = [(30, 37), (36, 42)]  # 己方头像位置 (x,y)
    user_locs = [(67, 99), (71, 98)]  # 对方头像位置 (x,y)
    
    # 处理己方头像（添加旋转）
    self_head = (
        images[0]
        .convert("RGBA")
        .resize((58, 58), keep_ratio=True)
        .circle()
        .rotate(15)  # 保持15度旋转
    )
    
    # 处理对方头像（移除旋转）
    user_head = (
        images[1]
        .convert("RGBA")
        .resize((48, 48), keep_ratio=True)
        .circle()  # 移除rotate(90)
    )
    
    frames: list[IMG] = []
    for i in range(2):
        # 获取模板尺寸
        template = BuildImage.open(img_dir / f"{i}.png")
        
        # 创建透明画布（与模板同尺寸）
        frame = BuildImage.new("RGBA", template.size)
        
        # 先贴两个头像（底层）
        frame.paste(user_head, user_locs[i], alpha=True)  # 对方头像
        frame.paste(self_head, self_locs[i], alpha=True)  # 己方头像
        
        # 最后覆盖模板图（上层）
        frame.paste(template, (0, 0), alpha=True)  # 关键修改点
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)  # 保持原帧率

add_meme(
    "oral_sex",
    oral_sex,
    min_images=2,
    max_images=2,
    keywords=["口"],
    date_created=datetime(2025, 5, 27),
    date_modified=datetime(2025, 6, 14),
)