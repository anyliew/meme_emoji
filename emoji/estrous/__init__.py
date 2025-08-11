# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def estrous(images: list[BuildImage], texts, args):

    user_head = images[0].resize((98, 66)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (105, 229), (104, 230), (103, 232), (101, 232), (98, 233),  # 1-5
        (96, 233), (93, 233), (91, 235), (89, 235), (86, 235),  # 6-10
        (85, 235), (84, 234), (83, 235), (81, 232), (82, 233),  # 11-15
        (82, 231), (85, 231), (87, 230), (89, 229), (92, 228),  # 16-20
        (94, 227), (97, 227), (100, 226), (101, 226), (104, 225),  # 21-25
        (106, 225), (106, 225), (109, 226), (109, 227), (108, 228),  # 26-30
        (108, 229), (106, 230), (105, 227), # 31-33
    ]

    # 处理所有帧
    for i in range(33):
        frame_num = (i % 33) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.03秒
    return save_gif(frames, 0.03)

add_meme(
    "estrous",  # 模板的唯一标识符
    estrous,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["发情"],  # 搜索关键词
    date_created=datetime(2025, 8, 11),  # 创建日期
    date_modified=datetime(2025, 8, 11),  # 修改日期
)