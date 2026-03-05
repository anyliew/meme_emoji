from datetime import datetime
from typing import Any, Dict

from pil_utils import BuildImage
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import colorsys

from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif


def louvre(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    # 从 args 中提取配置参数
    params: Dict[str, Any] = {}
    if hasattr(args, 'kwargs') and args.kwargs:
        params = args.kwargs
    elif hasattr(args, 'extra'):
        params = args.extra

    # 边缘检测阈值（值越小保留线条越多）
    edge_threshold = params.get('edge_threshold', 20)
    # 高斯模糊半径（降噪用，设为0则不模糊）
    blur_radius = params.get('blur_radius', 1.0)          # 默认增强为1.0
    # 是否启用中值滤波（更精细的降噪，去除椒盐噪声）
    median_filter = params.get('median_filter', True)     # 默认开启
    # 边缘图像平滑半径（用于消除边缘图中的孤立噪点）
    edge_smooth = params.get('edge_smooth', 0.5)          # 新增参数，默认0.5
    # 渐变起始色相（暖色）
    hue_start = params.get('hue_start', 0.05)
    # 渐变结束色相（冷色）
    hue_end = params.get('hue_end', 0.7)
    # 饱和度
    saturation = params.get('saturation', 0.9)
    # 整体亮度调整（-100 ~ 100）
    light = params.get('light', 0)
    # 是否启用阴影效果
    enable_shade = params.get('enable_shade', False)
    # 阴影阈值（灰度值低于此的视为暗部）
    shade_limit = params.get('shade_limit', 80)
    # 阴影亮度/强度（0~255）
    shade_light = params.get('shade_light', 40)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA")
        pil_img = img.image

        # 1. 灰度化
        gray = pil_img.convert('L')

        # 2. 精细降噪
        if median_filter:
            # 中值滤波去除椒盐噪声
            gray = gray.filter(ImageFilter.MedianFilter(size=3))
        if blur_radius > 0:
            # 高斯模糊平滑图像
            gray = gray.filter(ImageFilter.GaussianBlur(radius=blur_radius))

        # 3. 边缘检测
        edges = gray.filter(ImageFilter.FIND_EDGES)

        # 4. 边缘平滑（消除孤立噪点）
        if edge_smooth > 0:
            edges = edges.filter(ImageFilter.GaussianBlur(radius=edge_smooth))

        # 5. 增强边缘对比度
        edges_enhanced = edges.point(lambda x: min(255, x * 2))

        # 6. 创建白色背景
        white_bg = Image.new('RGBA', pil_img.size, (255, 255, 255, 255))

        # 7. 创建彩色边缘图层
        color_edges = Image.new('RGBA', pil_img.size, (0, 0, 0, 0))
        width, height = edges_enhanced.size
        edge_data = edges_enhanced.getdata()

        # 8. 如果需要阴影，生成阴影层
        shade_layer = None
        if enable_shade:
            gray_data = gray.getdata()
            shade_img = Image.new('L', pil_img.size, 0)
            shade_data = []
            for val in gray_data:
                if val < shade_limit:
                    shade_val = int((shade_limit - val) / shade_limit * shade_light)
                else:
                    shade_val = 0
                shade_data.append(shade_val)
            shade_img.putdata(shade_data)
            # 模糊阴影边缘使其更自然
            shade_img = shade_img.filter(ImageFilter.GaussianBlur(radius=1))
            shade_layer = shade_img.convert('L')

        # 9. 遍历像素生成彩色线条
        for y in range(height):
            for x in range(width):
                pixel_value = edge_data[y * width + x]
                if pixel_value > edge_threshold:
                    # 渐变因子：从左上到右下
                    gradient_factor = (x + y) / (width + height)
                    # 计算色相
                    hue = hue_start + (hue_end - hue_start) * gradient_factor
                    hue = max(0.0, min(1.0, hue))
                    # 亮度：位置影响 + 整体亮度调节
                    base_brightness = 0.8 + 0.1 * (1 - gradient_factor)
                    brightness = max(0.0, min(1.0, base_brightness + light / 200.0))
                    # 不透明度与边缘强度相关
                    alpha = min(255, pixel_value * 2)

                    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, saturation, brightness)]
                    color_edges.putpixel((x, y), (r, g, b, alpha))

        # 10. 合成白色背景和彩色边缘
        result = Image.alpha_composite(white_bg, color_edges)

        # 11. 叠加阴影
        if enable_shade and shade_layer:
            shade_rgba = Image.new('RGBA', pil_img.size, (0, 0, 0, 0))
            for y in range(height):
                for x in range(width):
                    sv = shade_layer.getpixel((x, y))
                    if sv > 0:
                        shade_rgba.putpixel((x, y), (40, 40, 40, sv))
            result = Image.alpha_composite(result.convert('RGBA'), shade_rgba)

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
    date_modified=datetime(2026, 3, 5),
)