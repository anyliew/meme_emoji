# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def lemonade(images: list[BuildImage], texts, args):
    # 将用户头像调整为1147x1147像素，并转换为RGBA模式以支持透明度
    user_head = images[0].resize((280, 280)).convert("RGBA").circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    # 生成147个相同的坐标 (53, 54)
    # 所有帧都在相同位置粘贴用户头像
    positions = [(53, 54)] * 147

    # 处理所有147帧
    for i in range(147):
        # 计算当前帧的图片编号 (1-147循环)
        frame_num = (i % 147) + 1
        # 打开对应的背景帧图片
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，尺寸与当前帧相同
        new_frame = BuildImage.new("RGBA", frame.size)
        # 在固定位置(47,47)粘贴用户头像作为背景
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面（覆盖头像的一部分，形成遮罩效果）
        new_frame.paste(frame, (0, 0), alpha=True)
        
        # 将处理后的帧添加到列表中
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.04秒（约25帧/秒）
    return save_gif(frames, 0.04)

# 注册meme模板
add_meme(
    "lemonade",  # 模板的唯一标识符
    lemonade,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["柠檬水"],  # 搜索关键词
    date_created=datetime(2026, 2, 16),  # 创建日期
    date_modified=datetime(2026, 2, 16),  # 修改日期
)