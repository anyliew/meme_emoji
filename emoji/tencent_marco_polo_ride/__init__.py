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

    user_head = images[0].resize((49, 49)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
            (32, 34), (32, 34), (35, 31), (37, 29), (37, 29),
            (37, 29), (38, 29), (39, 29), (41, 30), (38, 38),
            (30, 52), (33, 75), (40, 78), (48, 77), (63, 72),
            (78, 67), (67, 71), (45, 78), (40, 67), (22, 86),
            (26, 112), (33, 117), (57, 70), (66, 44), (68, 53),
            (61, 86), (51, 87), (62, 76), (85, 53), (105, 39),
            (101, 61), (104, 61), (110, 48), (110, 55), (104, 75),
            (99, 82), (98, 73), (110, 54), (115, 62), (120, 61),
            (120, 61), (120, 61), (120, 61), (121, 59), (121, 59),
            (119, 61), (120, 60), (121, 59), (121, 59), (121, 59),
            (121, 60), (122, 59), (122, 59), (122, 59), (122, 59),
            (122, 59), (122, 59), (121, 60), (121, 60), (121, 60),
            (121, 60), (120, 62), (120, 61), (122, 59), (122, 59),
            (120, 61), (121, 61), (121, 61), (121, 61), (119, 63),
            (119, 63), (120, 60), (117, 60)
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
    tags=MemeTags.capoo,
    date_created=datetime(2026, 1, 9),  # 创建日期
    date_modified=datetime(2026, 1, 9),  # 修改日期
)
