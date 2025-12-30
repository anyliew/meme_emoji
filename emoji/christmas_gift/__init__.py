# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def christmas_gift(images: list[BuildImage], texts, args):

    user_head = images[0].resize((300, 215), keep_ratio=True).convert("RGBA")
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    # 只有y坐标不等于0的位置需要贴头像
    # 格式: (x, y) 当y=0时表示不贴头像
    positions = [
        (0, 0), (0, 244), (0, 197), (0, 159),      # 0-3
        (0, 129), (0, 105), (0, 87), (0, 74), (0, 67),     # 4-8
        (0, 61), (0, 57), (0, 53), (0, 51), (0, 49),      # 9-13
        (0, 48), (0, 46), (0, 48), (0, 51), (0, 56),      # 14-18
        (0, 62), (0, 66), (0, 67), (0, 67), (0, 67),      # 19-23
        (0, 65), (0, 65), (0, 61), (0, 60), (0, 60),      # 24-28
        (0, 60), (0, 67), (0, 92), (0, 141), (0, 201),    # 29-33
        (0, 245), (0, 0), (0, 0), (0, 0), (0, 0),        # 34-38
        (0, 0), (0, 0)                                    # 39-40
    ]

    # 处理所有帧
    for i in range(41):
        frame_num = (i % 41) + 1
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

    # 将所有帧保存为GIF，帧间隔为0.03秒
    return save_gif(frames, 0.03)

add_meme(
    "christmas_gift",  # 模板的唯一标识符
    christmas_gift,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["圣诞礼物"],  # 搜索关键词
    date_created=datetime(2025, 12, 23),  # 创建日期
    date_modified=datetime(2025, 12, 30),  # 修改日期
)