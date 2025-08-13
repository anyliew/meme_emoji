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

def mihoyo_qiqi_suck(images: list[BuildImage], texts, args):

    user_head = images[0].resize((155, 155)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (78, 641), (92, 617), (123, 589), (144, 550), (230, 542),  # 1-5
        (328, 546), (375, 552), (375, 552), (375, 552), (375, 552),  # 6-10
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  # 11-15
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  # 16-20
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  # 21-25
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  # 26-30
        (375, 552), (375, 552), (375, 552), (375, 552), (375, 552),  # 31-35
        (375, 552), (375, 552), (375, 552), (327, 546), (229, 542),  # 36-40
        (143, 548), (122, 588), (91, 616), (77, 640), (77, 640),  # 41-45
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  # 46-50
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  # 51-55
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  # 56-60
        (77, 640), (77, 640), (77, 640), (77, 640), (77, 640),  # 61-65
        (77, 640), (77, 640), (77, 640),  # 66-68
    ]

    # 处理所有帧
    #18 舌头 25 36 33 34 39 变帧数位置 57=58
    for i in range(68):
        frame_num = (i % 68) + 1
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
    "mihoyo_qiqi_suck",  # 模板的唯一标识符
    mihoyo_qiqi_suck,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["七七舔"],  # 搜索关键词
    tags=MemeTags.genshin,
    date_created=datetime(2025, 8, 13),  # 创建日期
    date_modified=datetime(2025, 8, 13),  # 修改日期
)