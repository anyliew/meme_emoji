# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def bird_lgnoring(images: list[BuildImage], texts, args):

    user_head = images[0].resize((55, 55)).convert("RGBA")
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    # 只有y坐标不等于0的位置需要贴头像
    # 格式: (x, y) 当y=0时表示不贴头像
    positions = [
        (95, 69), (95, 69), (95, 66), (95, 64), (95, 61),
        (95, 60), (96, 58), (96, 60), (96, 61), (96, 65),
        (96, 66), (95, 67), (95, 66), (95, 65), (95, 63),
        (96, 60), (96, 60), (96, 61), (96, 62), (96, 65),
        (96, 66), (96, 69), (96, 69), (95, 68), (95, 64),
        (95, 63), (95, 60), (95, 59), (95, 59), (95, 59),
        (96, 62), (96, 64), (96, 66), (96, 68), (96, 70),
        (95, 70), (95, 68), (95, 65), (96, 63), (96, 60),
        (96, 59), (96, 59), (96, 61), (96, 62), (96, 64)
    ]

    # 处理所有帧
    for i in range(45):
        frame_num = (i % 45) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 如果该位置需要贴头像
        if positions[i][1] != 0:  # y坐标不为0时贴头像
            # 首先复制背景帧
            new_frame = frame.copy()
            # 然后在指定位置贴上用户头像
            new_frame.paste(user_head, positions[i], alpha=True, below=True)
            frames.append(new_frame.image)
        else:
            # 不需要贴头像，直接使用原帧
            frames.append(frame.image)

    # 将所有帧保存为GIF，帧间隔为0.07秒
    return save_gif(frames, 0.07)

add_meme(
    "bird_lgnoring",  # 模板的唯一标识符
    bird_lgnoring,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["不鸟你","我鸟都不鸟你"],  # 搜索关键词
    date_created=datetime(2025, 12, 23),  # 创建日期
    date_modified=datetime(2025, 12, 23),  # 修改日期
)