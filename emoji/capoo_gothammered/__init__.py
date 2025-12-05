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

def capoo_gothammered(images: list[BuildImage], texts, args):

    user_head = images[0].resize((80, 80)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (82, 147), (77, 116), (79, 128), (76, 135), (80, 146),
        (77, 127), (80, 127), (78, 137), (81, 146), (78, 130),
        (81, 129), (81, 139), (81, 147), (80, 131), (81, 130),
        (79, 137), (81, 146), (78, 131), (79, 130), (80, 138)
    ]

    # 处理所有帧
    for i in range(20):
        frame_num = (i % 20) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，动图平均帧率: 0.05
    return save_gif(frames, 0.05)

add_meme(
    "capoo_gothammered",  # 模板的唯一标识符
    capoo_gothammered,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["咖波被锤"],  # 搜索关键词
    tags=MemeTags.capoo,
    date_created=datetime(2025, 12, 5),  # 创建日期
    date_modified=datetime(2025, 12, 5),  # 修改日期
)
