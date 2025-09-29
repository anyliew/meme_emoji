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

def cooking(images: list[BuildImage], texts, args):

    user_head = images[0].resize((95, 95)).convert("RGBA")
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
    (80, 59), (80, 59), (80, 61), (80, 61), (80, 67),  # 1-5
    (80, 67), (80, 59), (80, 59), (80, 61), (80, 62),  # 6-10
    (80, 67), (80, 67), (80, 59), (80, 58), (80, 61),  # 11-15
    (80, 62), (80, 67), (80, 67), (80, 58), (79, 59),  # 16-20
    (80, 61), (80, 61), (80, 67), (80, 67), (80, 59),  # 21-25
    (80, 59), (80, 61), (80, 61), (80, 67), (80, 67),  # 26-30
    (80, 59), (80, 59), (80, 61), (80, 62), (80, 67),  # 31-35
    (80, 67), (80, 58), (80, 59), (80, 63), (80, 64),  # 36-40
    (78, 68), (79, 68), (80, 64), (80, 63), (80, 58),  # 41-45
    (80, 59), (80, 64), (80, 63), (79, 67), (79, 67),  # 46-50
    (80, 63), (80, 63),  # 51-52
    ]

    # 处理所有帧
    for i in range(52):
        frame_num = (i % 52) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.05秒
    return save_gif(frames, 0.05)

add_meme(
    "cooking",  # 模板的唯一标识符
    cooking,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["炒菜"],  # 搜索关键词
    date_created=datetime(2025, 9, 29),  # 创建日期
    date_modified=datetime(2025, 9, 29),  # 修改日期
)