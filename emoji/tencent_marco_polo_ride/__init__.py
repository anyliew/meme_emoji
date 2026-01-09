# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类
from meme_generator.tags import MemeTags

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def tencent_marco_polo_ride(images: list[BuildImage], texts, args):

    user_head = images[0].resize((52, 52)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (30, 32), (30, 32), (33, 29), (35, 27), (35, 27),
        (35, 27), (36, 27), (37, 27), (39, 28), (36, 36),
        (28, 50), (31, 73), (38, 76), (46, 75), (61, 70),
        (76, 65), (65, 69), (43, 76), (38, 65), (20, 84),
        (24, 110), (31, 115), (55, 68), (64, 42), (66, 51),
        (59, 84), (49, 85), (60, 74), (83, 51), (103, 37),
        (99, 59), (102, 59), (108, 46), (108, 53), (102, 73),
        (97, 80), (96, 71), (108, 52), (113, 60), (118, 59),
        (118, 59), (118, 59), (118, 59), (119, 57), (119, 57),
        (117, 59), (118, 58), (119, 57), (119, 57), (119, 57),
        (119, 58), (120, 57), (120, 57), (120, 57), (120, 57),
        (120, 57), (120, 57), (119, 58), (119, 58), (119, 58),
        (119, 58), (118, 60), (118, 59), (120, 57), (120, 57),
        (118, 59), (119, 59), (119, 59), (119, 59), (117, 61),
        (117, 61), (118, 58), (115, 58)
    ]

    # 处理所有帧
    for i in range(73):
        frame_num = (i % 73) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，动图平均帧率: 0.12
    return save_gif(frames, 0.12)

add_meme(
    "tencent_marco_polo_ride",  # 模板的唯一标识符
    tencent_marco_polo_ride,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["马克骑","马可波罗骑"],  # 搜索关键词
    date_created=datetime(2026, 1, 9),  # 创建日期
    date_modified=datetime(2026, 1, 9),  # 修改日期
)
