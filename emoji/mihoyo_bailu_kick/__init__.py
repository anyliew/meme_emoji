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

def mihoyo_bailu_kick(images: list[BuildImage], texts, args):

    user_head = images[0].resize((60, 60)).convert("RGBA")
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
    (49, 67), (49, 67), (49, 67), (49, 67), (31, 35),    # 1-5
    (11, 32), (1, 47), (2, 60), (3, 62), (7, 64),   # 6-10
    (9, 70), (8, 76), (4, 106), (2, 157), (11, 156), # 11-15
    (29, 47), (47, 1), (56, -28), (66, -26), (92, -36),   # 16-20
    (127, 4), (150, 56), (130, 63), (86, 46), (28, 54), # 21-25
    (-25, 151), (13, 99), (132, 29), (167, 6), (207, 1), # 26-30
    (220, 29), (227, 61), (159, 17), (104, -28), (76, -39)  # 31-35
    ]

    # 处理所有帧
    for i in range(35):
        frame_num = (i % 35) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，动图平均帧率: 0.09
    return save_gif(frames, 0.09)

add_meme(
    "mihoyo_bailu_kick",  # 模板的唯一标识符
    mihoyo_bailu_kick,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["白露踢"],  # 搜索关键词
    tags=MemeTags.star_rail,
    date_created=datetime(2025, 9, 30),  # 创建日期
    date_modified=datetime(2025, 9, 30),  # 修改日期
)