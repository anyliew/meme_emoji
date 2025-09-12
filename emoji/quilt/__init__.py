# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def quilt(images: list[BuildImage], texts, args):

    user_head = images[0].resize((142, 146)).convert("RGBA")
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (68, 68), (68, 68), (68, 72), (69, 74), (69, 74),  # 1-5
        (69, 73), (69, 72), (69, 74), (68, 72), (68, 68),  # 6-10
        (68, 68), (68, 68), (68, 72), (68, 72), (69, 73),  # 11-15
        (69, 73), (69, 73), (69, 75), (68, 72), (68, 68),  # 16-20
        (68, 68),  # 21
    ]

    # 处理所有帧
    for i in range(21):
        frame_num = (i % 21) + 1
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
    "quilt",  # 模板的唯一标识符
    quilt,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["被窝"],  # 搜索关键词
    date_created=datetime(2025, 9, 12),  # 创建日期
    date_modified=datetime(2025, 9, 12),  # 修改日期
)