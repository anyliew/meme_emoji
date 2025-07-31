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

def kurogames_iuno_kick(images: list[BuildImage], texts, args):

    user_head = images[0].resize((130, 130)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (88, 40), (88, 40), (122, 49), (134, 54), (142, 61),  # 1-5
        (143, 69), (128, 77), (110, 77), (95, 77), (65, 99),  # 6-10
        (28, 53), (26, 47), (29, 46), (43, 39), (75, 10),  # 11-15
        (86, 0), (90, -16), (94, -16), (92, -16), (85, -4),  # 16-20
        (59, 30), (45, 41), (29, 47), (26, 48), (40, 62),  # 21-25
        (65, 70), (95, 76), (110, 77), (136, 74), (142, 69),  # 26-30
        (141, 61), (135, 54), (102, 44), (89, 39),   # 31-34
    ]

    # 处理所有帧
    for i in range(34):
        frame_num = (i % 34) + 1
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
    "kurogames_iuno_kick",  # 模板的唯一标识符
    kurogames_iuno_kick,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["尤诺踢"],  # 搜索关键词
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 31),  # 创建日期
    date_modified=datetime(2025, 7, 31),  # 修改日期
)