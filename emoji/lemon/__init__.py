# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def lemon(images: list[BuildImage], texts, args):
    # 处理用户提供的图像：
    # 1. 调整大小为80x80
    # 2. 转换为圆形
    user_head = images[0].resize((90, 90)).convert("RGBA").circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    # 定义所有帧的头像位置（现在扩展到92帧）
    # 格式: (x坐标, y坐标)
    # 92帧数的坐标太多,有没有大佬帮我修一修
    positions = [
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 1-5
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 6-10
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 11-15
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 16-20
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 21-25 done
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 26-30
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 31-35
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 36-40
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 41-45
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15),  # 46-50
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 51-55
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 56-60
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 61-65
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 66-70
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 71-75
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 76-80
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 81-85
        (18, 15), (18, 15), (18, 15), (18, 15), (18, 15), # 86-90
        (18, 15), (18, 15),  # 91-92
    ]

    # 处理所有92帧
    for i in range(92):
        frame_num = (i % 92) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.06秒
    return save_gif(frames, 0.06)


# 将"lemon"meme模板添加到生成器中
add_meme(
    "lemon",  # 模板的唯一标识符
    lemon,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["柠檬"],  # 搜索关键词
    date_created=datetime(2025, 7, 11),  # 创建日期
    date_modified=datetime(2025, 7, 11),  # 修改日期
)