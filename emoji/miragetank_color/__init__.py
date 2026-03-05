from datetime import datetime
from pathlib import Path
from typing import List

import numpy as np
from PIL import Image, ImageEnhance
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

def resize_and_center(img: BuildImage, target_size: tuple[int, int]) -> BuildImage:
    """
    将图像缩放至目标尺寸内（保持比例），并居中放置在透明背景上。
    """
    # 计算缩放比例
    target_w, target_h = target_size
    img_w, img_h = img.size
    scale = min(target_w / img_w, target_h / img_h)
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)

    # 缩放图像
    resized = img.resize((new_w, new_h), keep_ratio=False)  # 直接指定尺寸

    # 创建透明画布
    canvas = BuildImage.new("RGBA", target_size, (0, 0, 0, 0))

    # 计算粘贴位置（居中）
    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    canvas.paste(resized, (x, y), alpha=True)
    return canvas

def miragetank_color(
    images: List[BuildImage],
    texts: List[str],
    args: MemeArgsModel,
    wlight: float = 1.0,
    blight: float = 0.18,
    wcolor: float = 0.5,
    bcolor: float = 0.7,
) -> BuildImage:
    """
    彩色幻影坦克合成
    :param images: [0] 上层封面图, [1] 下层底图
    """
    cover_img = images[0].convert("RGBA")
    base_img = images[1].convert("RGBA") if len(images) > 1 else cover_img

    def make(imgs: List[BuildImage]) -> BuildImage:
        current_cover = imgs[0].convert("RGBA")
        current_base = imgs[1].convert("RGBA") if len(imgs) > 1 else current_cover

        # 统一尺寸：以封面图为基准，底图缩放并居中
        target_size = current_cover.size
        current_base = resize_and_center(current_base, target_size)

        # 应用亮度增强/减弱
        cover_pil = ImageEnhance.Brightness(current_cover.image).enhance(wlight)
        base_pil = ImageEnhance.Brightness(current_base.image).enhance(blight)

        # 转为 numpy 数组
        wpix = np.array(cover_pil.convert("RGB")).astype(np.float64) / 255.0
        bpix = np.array(base_pil.convert("RGB")).astype(np.float64) / 255.0

        # 计算灰度
        wgray = np.dot(wpix[..., :3], [0.334, 0.333, 0.333])
        bgray = np.dot(bpix[..., :3], [0.334, 0.333, 0.333])

        # 色彩保留
        wpix = wpix * wcolor + wgray[..., None] * (1.0 - wcolor)
        bpix = bpix * bcolor + bgray[..., None] * (1.0 - bcolor)

        # 差值 d
        d = 1.0 - wpix + bpix
        d_luma = np.dot(d, [0.222, 0.707, 0.071])

        # 避免除零
        mask = np.abs(d_luma) > 1e-6
        p = np.zeros_like(bpix)
        p[mask] = (bpix[mask] / d_luma[mask, None]) * 255.0
        p[~mask] = 255.0

        # 透明度
        a = np.clip(d_luma * 255.0, 0, 255).astype(np.uint8)

        # RGB 截断
        rgb = np.clip(p, 0, 255).astype(np.uint8)

        # 合并为 RGBA
        result_arr = np.dstack([rgb, a])
        result_img = Image.fromarray(result_arr, "RGBA")
        return BuildImage(result_img)

    return make_png_or_gif(images, make)

# 注册
add_meme(
    "miragetank_color",
    miragetank_color,
    min_images=2,
    max_images=2,
    min_texts=0,
    max_texts=0,
    keywords=["彩色幻影坦克", "彩幻"],
    date_created=datetime(2026, 3, 5),
    date_modified=datetime(2026, 3, 5),
)