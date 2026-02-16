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

def kurogames_abby_play(images: list[BuildImage], texts, args):

    user_head = images[0].resize((177, 177)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (794, 402), (787, 402), (786, 402), (787, 423), (789, 354), #1-5
        (787, 262), (791, 172), (793, 128), (793, 131), (792, 140), #6-10
        (793, 154), (793, 174), (794, 198), (793, 223), (792, 250), #11-15
        (790, 276), (793, 301), (793, 330), (793, 352), (793, 373), #16-20
        (793, 390), (796, 399), (796, 402), (794, 403), (790, 422), #21-25
        (794, 354), (797, 264), (797, 174), (796, 124), (796, 127), #26-30
        (793, 138), (793, 157), (793, 180), (793, 204), (793, 232), #31-35
        (793, 265), (793, 291), (793, 322), (793, 348), (793, 368), #36-40
        (793, 387), (792, 399), (792, 402), (792, 402), (792, 402), #41-45
        (793, 402), (793, 402) #46-47
    ]

    # 处理所有帧
    for i in range(47):
        frame_num = (i % 47) + 1
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
    "kurogames_abby_play",  # 模板的唯一标识符
    kurogames_abby_play,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["阿布顶","阿布玩"],  # 搜索关键词
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2026, 2, 16),  # 创建日期
    date_modified=datetime(2026, 2, 16),  # 修改日期
)