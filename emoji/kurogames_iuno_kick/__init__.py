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
    user_img = images[0].convert("RGBA")  # 原始用户头像
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (88, 40), (88, 40), (122, 49), (134, 54), (142, 61),  # 1-5
        (142, 69), (129, 78), (111, 78), (96, 78), (66, 70),  # 6-10
        (29, 54), (26, 47), (29, 46), (43, 39), (75, 10),     # 11-15
        (86, 0), (90, -10), (94, -16), (92, -12), (85, -4),   # 16-20
        (59, 30), (45, 41), (29, 47), (26, 48), (42, 63),     # 21-25
        (67, 71), (96, 77), (111, 78), (137, 74), (142, 69),  # 26-30
        (141, 61), (135, 54), (102, 44), (89, 39),            # 31-34
    ]

    # 定义每一帧的头像尺寸 (width, height)
    sizes = [
        (108, 108), (108, 108), (105, 105), (105, 105), (105, 105),  # 1-5
        (110, 110), (105, 105), (110, 110), (110, 110), (112, 112),  # 6-10
        (108, 108), (105, 105), (96, 96), (86, 86), (70, 70),  # 11-15
        (67, 67), (61, 61), (58, 58), (62, 62), (66, 66),  # 16-20
        (77, 77), (84, 84), (97, 97), (105, 105), (110, 110),  # 21-25
        (110, 110), (110, 110), (110, 110), (105, 105), (105, 105),  # 26-30
        (105, 105), (105, 105), (105, 105), (105, 105),              # 31-34
    ]

    # 处理所有帧
    for i in range(34):
        frame_num = (i % 34) + 1
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

    # 将所有帧保存为GIF，帧间隔为0.06秒
    return save_gif(frames, 0.06)

add_meme(
    "kurogames_iuno_kick",  # 模板的唯一标识符
    kurogames_iuno_kick,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["尤诺踢","优诺踢",],  # 搜索关键词
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 7, 31),  # 创建日期
    date_modified=datetime(2025, 8, 1),  # 修改日期
)