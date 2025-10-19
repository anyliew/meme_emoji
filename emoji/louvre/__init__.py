from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage
from PIL import Image, ImageFilter
import colorsys

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif

img_dir = Path(__file__).parent / "images"


def louvre(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    def make(imgs: list[BuildImage]) -> BuildImage:
        # 将BuildImage转换为PIL Image进行处理
        img = imgs[0].convert("RGBA").resize((500, 500))
        pil_img = img.image  # 获取底层的PIL Image对象
        
        # 转换为灰度图
        gray_img = pil_img.convert('L')
        
        # 轻微高斯模糊减少噪点
        blurred = gray_img.filter(ImageFilter.GaussianBlur(radius=0.5))
        
        # 使用简单的边缘检测方法，保留更多细节
        edges = blurred.filter(ImageFilter.FIND_EDGES)
        
        # 增强边缘对比度，但不使用过于严格的阈值
        edges_enhanced = edges.point(lambda x: min(255, x * 2))  # 简单增强对比度
        
        # 创建白色背景
        white_bg = Image.new('RGBA', pil_img.size, (255, 255, 255, 255))
        
        # 创建渐变色彩线稿
        color_edges = Image.new('RGBA', pil_img.size, (0, 0, 0, 0))
        
        # 获取边缘像素数据
        edge_data = edges_enhanced.getdata()
        
        # 为边缘像素添加渐变色彩
        width, height = edges_enhanced.size
        
        for y in range(height):
            for x in range(width):
                pixel_value = edge_data[y * width + x]
                # 使用较低的阈值，保留更多线条
                if pixel_value > 20:  # 降低阈值，保留更多细节
                    # 计算从左上方到右下方的渐变因子
                    gradient_factor = (x + y) / (width + height)
                    
                    # 根据渐变因子调整色相
                    # 左上角使用暖色调（0.0-0.1 红色/橙色），右下角使用冷色调（0.6-0.7 蓝色/紫色）
                    hue = 0.05 + 0.65 * gradient_factor  # 从暖色渐变到冷色
                    
                    # 调整饱和度，使颜色更鲜艳
                    saturation = 0.9  # 高饱和度
                    
                    # 调整亮度，使线条更明亮
                    brightness = 0.8 + 0.1 * (1 - gradient_factor)  # 左上角更亮，右下角稍暗
                    
                    # 根据边缘强度调整不透明度，使强边缘更明显，弱边缘更柔和
                    alpha = min(255, pixel_value * 2)
                    
                    # 确保值在有效范围内
                    hue = max(0.0, min(1.0, hue))
                    saturation = max(0.0, min(1.0, saturation))
                    brightness = max(0.0, min(1.0, brightness))
                    
                    # 转换为RGB颜色
                    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, saturation, brightness)]
                    color_edges.putpixel((x, y), (r, g, b, alpha))
        
        # 将彩色线条合并到白色背景上
        result = Image.alpha_composite(white_bg, color_edges)
        
        # 将PIL Image转换回BuildImage
        return BuildImage(result)

    return make_png_or_gif(images, make)


add_meme(
    "louvre",
    louvre,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["卢浮宫"],
    date_created=datetime(2025, 5, 29),
    date_modified=datetime(2025, 5, 29),
)