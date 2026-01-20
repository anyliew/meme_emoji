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

def kurogames_mornye_raise(images: list[BuildImage], texts, args):
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (92, 281), (92, 281), (91, 280), (91, 279), (91, 279),
        (90, 277), (89, 276), (88, 274), (87, 272), (86, 270),
        (85, 269), (84, 267), (84, 266), (83, 264), (82, 263),
        (82, 263), (81, 263), (81, 263), (81, 263), (81, 263),
        (81, 263), (81, 263), (81, 263), (81, 263), (81, 263),
        (81, 263), (81, 263), (81, 263), (81, 263)
    ]

    # 处理所有帧
    for i in range(29):
        frame_num = (i % 29) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 获取用户头像
        user_head = images[0].resize((176, 176)).convert("RGBA")
        
        # 对于前13帧（帧号0-12），将头像旋转13°
        if i < 13:
            user_head = user_head.rotate(13, expand=False)
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.04秒
    return save_gif(frames, 0.04)

add_meme(
    "kurogames_mornye_raise",  # 模板的唯一标识符
    kurogames_mornye_raise,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["莫宁举"],  # 搜索关键词
    date_created=datetime(2026, 1, 20),  # 创建日期
    date_modified=datetime(2026, 1, 20),  # 修改日期
)