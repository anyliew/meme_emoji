from datetime import datetime
from typing import Any, Dict
import os
import colorsys
import io
import random
import numpy as np
from pathlib import Path
import sys

from pil_utils import BuildImage
from pydantic import Field
from meme_generator import MemeArgsModel, add_meme
from meme_generator import (
    MemeArgsType,
    ParserArg,
    ParserOption,
)
import cv2
from PIL import Image, ImageFilter, ImageChops, ImageOps
from meme_generator.utils import make_png_or_gif

"""
# 🧸 致谢 itorr/one-last-image 项目
#
# 本项目参考并使用了 itorr/one-last-image 开源项目的算法和设计思路。
# One Last Image 卢浮宫生成器是一个将赛璐珞风格动画截图或插画转换为 One Last Kiss
# 封面风格的在线生成器，支持自定义线条处理方案、Kiss风格色彩映射、铅笔调子、水印等效果。
#
# 项目地址: https://github.com/itorr/one-last-image
# 在线演示: https://lab.magiconch.com/one-last-image/
#
# 致谢 one-last-image 项目作者 itorr 卜卜口！
# 感谢 Q. 提供pycairo思路
# 依赖说明：本插件需要安装 'pycairo' 库以生成 One Last Kiss 风格的彩色渐变。
# 安装命令：pip install pycairo
"""

# 尝试导入cairo，如果失败则输出错误信息
try:
    import cairo
    CAIRO_AVAILABLE = True
except ImportError as e:
    CAIRO_AVAILABLE = False
    print("\n" + "="*60)
    print("错误: 缺少必要的依赖库 'pycairo'")
    print("="*60)
    print("原因: 无法导入cairo库，这会导致无法生成彩色渐变")
    print("")
    print("解决方案:")
    print("1. 安装pycairo:")
    print("   - 在Windows上运行: pip install pycairo")
    print("   - 在macOS上运行: pip install pycairo")
    print("   - 在Linux上运行: pip install pycairo")
    print("")
    print("2. 如果安装遇到问题，可以尝试:")
    print("   pip install pycairo-win  (Windows专用)")
    print("")
    print("3. 或者手动下载并安装:")
    print("   https://pypi.org/project/pycairo/")
    print("="*60)
    print("")
    # 重新抛出异常，使程序终止
    raise


# 修正后的帮助文本：7种线迹模式 + 随机选择
help_text = "线迹模式: 0=随机选择, 1=精细, 2=一般, 3=稍粗, 4=超粗, 5=极粗, 6=浮雕, 7=线稿(彩色)"


# 定义参数模型
class Model(MemeArgsModel):
    number: int = Field(0, description=help_text)


args_type = MemeArgsType(
    args_model=Model,
    parser_options=[
        ParserOption(
            names=["-n", "--number"],
            args=[ParserArg(name="number", value="int")],
            help_text=help_text,
        ),
    ],
)


# 卷积核定义
def kernel_average(size: int) -> np.ndarray:
    return np.full((size, size), 1 / size**2)


# 卷积核映射
KERNELS: Dict[str, np.ndarray] = {
    "精细": kernel_average(5),      # 精细模式
    "一般": kernel_average(7),      # 一般模式
    "稍粗": kernel_average(9),      # 稍粗模式
    "超粗": kernel_average(11),     # 超粗模式
    "极粗": kernel_average(13),     # 极粗模式
    "浮雕": np.array([              # 浮雕模式
        [1, 1, 1],
        [1, 1, -1],
        [-1, -1, -1],
    ]),
    "线稿(彩色)": kernel_average(5),      # 线稿模式（使用精细卷积核）
}


# 模式映射（1-7对应7种线迹模式）
MODE_MAPPING = {
    1: "精细",
    2: "一般",
    3: "稍粗",
    4: "超粗",
    5: "极粗",
    6: "浮雕",
    7: "线稿(彩色)"
}


# 阴影和光参数
SHADE_LIGHT = 108
LIGHT_CUT = 128


def make_gradient(width: int, height: int) -> BuildImage:
    """创建Kiss色彩渐变"""
    if not CAIRO_AVAILABLE:
        raise ImportError("cairo库不可用，无法生成彩色渐变。请先安装pycairo库。")
    
    with cairo.ImageSurface(cairo.FORMAT_RGB24, width, height) as surface:
        cr = cairo.Context(surface)
        gradient = cairo.LinearGradient(0, 0, width, height)
        
        # 添加颜色停止点，创建Kiss风格渐变
        gradient.add_color_stop_rgb(0.0, 0.984, 0.729, 0.188)  # 金色
        gradient.add_color_stop_rgb(0.4, 0.988, 0.447, 0.208)  # 橙色
        gradient.add_color_stop_rgb(0.6, 0.988, 0.208, 0.306)  # 红色
        gradient.add_color_stop_rgb(0.7, 0.812, 0.212, 0.875)  # 紫色
        gradient.add_color_stop_rgb(0.8, 0.216, 0.710, 0.851)  # 蓝色
        gradient.add_color_stop_rgb(1.0, 0.243, 0.714, 0.855)  # 蓝绿色
        
        cr.set_source(gradient)
        cr.rectangle(0, 0, width, height)
        cr.fill()
        
        file = io.BytesIO()
        surface.write_to_png(file)
        file.seek(0)
        return BuildImage.open(file)


def make_grayscale_gradient(width: int, height: int) -> BuildImage:
    """创建黑白渐变（用于线稿模式）"""
    gradient = Image.new("RGB", (width, height))
    
    for y in range(height):
        for x in range(width):
            # 计算渐变因子
            gradient_factor = (x + y) / (width + height)
            gray_value = int(255 * (1 - gradient_factor * 0.3))  # 轻微渐变
            gradient.putpixel((x, y), (gray_value, gray_value, gray_value))
    
    return BuildImage(gradient)


def make_mask(
    im: Image.Image,
    pencil: Image.Image,
    kernel: np.ndarray,
    dark_cut: int = 118,
    shade_limit: int = 120,
    denoise: bool = True,
    enable_shade: bool = True,
) -> Image.Image:
    """创建图像掩膜"""
    # 创建阴影
    if enable_shade:
        shade = im.point(lambda v: 0 if v > shade_limit else 255, "L")
        shade = shade.filter(ImageFilter.BoxBlur(3))
        shade = ImageChops.multiply(shade, ImageChops.invert(pencil))
        shade = ImageChops.multiply(shade, Image.new("L", shade.size, SHADE_LIGHT))
    else:
        # 禁用阴影时创建空白图层
        shade = Image.new("L", im.size, 0)
    
    # 降噪
    if denoise:
        im = im.filter(ImageFilter.Kernel((3, 3), [1] * 9, 9))
    
    # 卷积处理
    im_array = np.array(im)
    im1 = Image.fromarray(cv2.filter2D(im_array, -1, kernel))
    
    # 计算差值
    im = ImageChops.subtract(im, im1, 1, 128)
    
    # 调整对比度
    scale = (255 - LIGHT_CUT - dark_cut) / 255
    im = ImageChops.subtract(im, Image.new("L", im.size, dark_cut), scale)
    
    # 合并阴影
    return ImageChops.lighter(ImageChops.invert(im), shade)


def louvre(images: list[BuildImage], texts: list[str], args: Model):
    # 根据参数选择模式
    if args.number == 0:
        mode_number = random.randint(1, 7)
    elif 1 <= args.number <= 7:
        mode_number = args.number
    else:
        raise ValueError("模式编号错误，请选择 1~7 或 0（随机）")
    
    # 获取模式名称
    mode_name = MODE_MAPPING[mode_number]
    
    # 获取对应卷积核
    kernel = KERNELS[mode_name]
    
    # 加载铅笔纹理
    current_dir = Path(__file__).parent
    pencil_path = current_dir / 'images' / 'pencil-texture.jpg'
    
    if not pencil_path.exists():
        # 如果没有纹理图片，创建一个简单的纹理
        pencil = BuildImage.new("L", (100, 100), 255)
    else:
        pencil = BuildImage.open(pencil_path).convert("L")
    
    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0]
        
        # 所有模式都使用彩色渐变，并开启阴影和纹理
        gradient = make_gradient(img.width, img.height)
        enable_shade = True
        texture_intensity = 0.4
        
        # 分离亮度和透明度通道
        l, a = img.convert("LA").image.split()
        
        # 创建白色背景
        frame = BuildImage.new("L", l.size, 255)
        frame.image.paste(l, mask=a)
        
        # 调整铅笔纹理大小
        resized_pencil = pencil.resize(img.size)
        
        # 创建掩膜
        mask = make_mask(
            frame.image,
            resized_pencil.image,
            kernel=kernel,
            dark_cut=118,  # 线迹轻重
            shade_limit=120,  # 调子阈值
            denoise=True,  # 降噪
            enable_shade=enable_shade,
        )
        
        # 创建最终图像
        result = BuildImage.new("RGB", l.size, (255, 255, 255))
        result.image.paste(gradient.image, (0, 0), mask=mask)
        
        # 添加铅笔纹理
        if texture_intensity > 0:
            texture = Image.open(pencil_path).convert('L').resize((img.width, img.height))
            texture = ImageOps.invert(texture)
            
            alpha = int(100 * texture_intensity)
            texture_layer = Image.new('RGBA', (img.width, img.height), (0, 0, 0, 0))
            
            for y in range(img.height):
                for x in range(img.width):
                    tex_val = texture.getpixel((x, y))
                    if tex_val > 100:
                        current_color = result.image.getpixel((x, y))
                        r = max(0, current_color[0] - 20)
                        g = max(0, current_color[1] - 20)
                        b = max(0, current_color[2] - 20)
                        texture_layer.putpixel((x, y), (r, g, b, alpha))
            
            result = BuildImage(Image.alpha_composite(result.image.convert("RGBA"), texture_layer).convert("RGB"))
        
        return result
    
    return make_png_or_gif(images, make)


# 注册表情
add_meme(
    "louvre",
    louvre,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=0,
    keywords=["卢浮宫"],
    args_type=args_type,
    date_created=datetime(2025, 5, 29),
    date_modified=datetime(2026, 5, 26),
)