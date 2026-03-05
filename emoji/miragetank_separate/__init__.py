from datetime import datetime
from typing import List

from PIL import Image, ImageEnhance
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

def miragetank_separate(
    images: List[BuildImage],
    texts: List[str],
    args: MemeArgsModel,
) -> BuildImage:
    """
    分离幻影坦克图片为表图和里图
    :param images: [0] 幻影坦克图片（需为 RGBA PNG）
    :param texts: 可选第一个文本为亮度增强因子（默认 2.0，建议范围 1~6）
    """
    # 解析亮度增强因子
    bright_factor = 2.0
    if texts and texts[0].strip():
        try:
            bright_factor = float(texts[0].strip())
            bright_factor = min(max(bright_factor, 0.1), 6.0)  # 限制合理范围
        except ValueError:
            pass

    tank_img = images[0].convert("RGBA")

    def make(imgs: List[BuildImage]) -> BuildImage:
        current_tank = imgs[0].convert("RGBA")

        # 创建白色背景和黑色背景
        white_bg = BuildImage.new("RGBA", current_tank.size, (255, 255, 255, 255))
        black_bg = BuildImage.new("RGBA", current_tank.size, (0, 0, 0, 255))

        # 将幻影坦克粘贴到背景上（使用自身透明度作为遮罩）
        white_bg.paste(current_tank, (0, 0), alpha=True)
        black_bg.paste(current_tank, (0, 0), alpha=True)

        # 对黑色背景图像进行亮度增强（恢复里图）
        black_pil = ImageEnhance.Brightness(black_bg.image).enhance(bright_factor)

        # 转换为 RGB 模式（去除透明度，便于保存为 JPEG 风格）
        white_rgb = white_bg.convert("RGB")
        black_rgb = BuildImage(black_pil).convert("RGB")

        # 水平拼接两张图：左表图（白底），右里图（黑底）
        total_width = white_rgb.width + black_rgb.width
        max_height = max(white_rgb.height, black_rgb.height)
        result = BuildImage.new("RGB", (total_width, max_height), (255, 255, 255))
        result.paste(white_rgb, (0, 0))
        result.paste(black_rgb, (white_rgb.width, 0))

        # 可选：添加文字标签（为保持简洁，此处省略）
        return result

    return make_png_or_gif(images, make)


# 注册到 meme 生成器
add_meme(
    "miragetank_separate",
    miragetank_separate,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["幻影分离", "坦克分离"],
    date_created=datetime(2026, 3, 5),
    date_modified=datetime(2026, 3, 5),
)