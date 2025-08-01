# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def peas(images: list[BuildImage], texts, args):

    user_head = images[0].resize((83, 70)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (30, 47), (30, 47), (30, 47), (30, 47), (30, 47),  # 1-5
        (30, 47), (30, 47), (30, 47), (30, 47), (30, 47),  # 6-10
        (30, 47), (30, 47), (30, 47), (30, 47), (30, 47),  # 11-15
        (30, 47), (30, 47), (30, 47), (30, 47), (30, 47),  # 16-20
        (30, 47), (30, 47), (30, 47), (30, 47), (30, 47),  # 21-25 done
        (30, 47), (30, 47), (30, 47), (30, 47), (30, 47), # 26-30
        (30, 47), (30, 47), (30, 47),   # 31-33
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

    # 将所有帧保存为GIF，帧间隔为0.06秒
    return save_gif(frames, 0.06)

add_meme(
    "peas",  # 模板的唯一标识符
    peas,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["我嘞个豆","豆"],  # 搜索关键词
    date_created=datetime(2025, 7, 13),  # 创建日期
    date_modified=datetime(2025, 7, 13),  # 修改日期
)