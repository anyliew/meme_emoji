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

def capoo_take_dump(images: list[BuildImage], texts, args):
    user_img = images[0].convert("RGBA")  # 原始用户头像
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (34, 55), (34, 55), (38, 59), (91, 79), (148, 104),  # 1-5
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),  # 6-10
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),    # 11-15
        (1, 1), (1, 1), (1, 1), (1, 1),   # 16-19

    ]

    # 定义每一帧的头像尺寸 (width, height)
    sizes = [
        (86, 75), (86, 75), (79, 69), (51, 52), (35, 36),  # 1-5
        (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),  # 6-10
        (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),  # 11-15
        (2, 2), (2, 2), (2, 2), (2, 2),  # 16-19
    ]

    # 处理所有帧
    for i in range(19):
        frame_num = (i % 19) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 根据当前帧索引获取对应的头像尺寸
        width, height = sizes[i]
        user_head = user_img.resize((width, height))
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.1秒
    return save_gif(frames, 0.1)

add_meme(
    "capoo_take_dump",  # 模板的唯一标识符
    capoo_take_dump,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["咖波拉"],  # 搜索关键词
    tags=MemeTags.capoo,
    date_created=datetime(2025, 9, 27),  # 创建日期
    date_modified=datetime(2025, 9, 27),  # 修改日期
)