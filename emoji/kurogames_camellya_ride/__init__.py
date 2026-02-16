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

def kurogames_camellya_ride(images: list[BuildImage], texts, args):

    user_head = images[0].resize((48, 48)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (101, 200), (100, 203), (98, 209), (93, 208), (84, 209),
        (77, 213), (77, 224), (87, 221), (104, 223), (109, 223),
        (106, 230), (92, 227), (75, 236), (70, 233), (71, 239),
        (81, 224), (92, 214), (96, 210), (92, 216), (78, 210),
        (67, 223), (71, 220), (74, 228), (90, 216), (111, 224),
        (113, 216), (101, 222), (80, 223), (73, 233), (79, 235),
        (94, 224), (116, 232), (117, 226), (108, 231), (99, 227),
        (87, 226), (88, 227), (94, 230), (107, 230), (108, 235),
        (107, 233), (97, 225), (80, 232), (73, 243), (79, 239),
        (95, 236), (121, 237), (130, 233), (124, 234), (118, 235)
    ]

    # 处理所有帧
    for i in range(11):
        frame_num = (i % 11) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.1秒
    return save_gif(frames, 0.1)

add_meme(
    "kurogames_camellya_ride",  # 模板的唯一标识符
    kurogames_camellya_ride,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["椿骑","大傻椿骑"],  # 搜索关键词
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 2, 16),  # 创建日期
    date_modified=datetime(2026, 2, 16),  # 修改日期
)