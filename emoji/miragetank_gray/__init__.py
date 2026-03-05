from datetime import datetime
from typing import List

import numpy as np
from PIL import Image
from pil_utils import BuildImage
from meme_generator import MemeArgsModel, add_meme
from meme_generator.utils import make_png_or_gif

def miragetank_gray(
    images: List[BuildImage],
    texts: List[str],
    args: MemeArgsModel,
    chess: bool = False,
) -> BuildImage:
    """
    灰度幻影坦克合成
    :param images: [0] 上层封面图, [1] 下层底图
    :param chess: 是否启用棋盘格化效果
    """
    def make(imgs: List[BuildImage]) -> BuildImage:
        # 转换为灰度模式
        current_cover = imgs[0].convert("L")
        current_base = imgs[1].convert("L") if len(imgs) > 1 else current_cover

        target_size = current_cover.size

        # ---------- 处理封面图（置于白色背景） ----------
        cover_w, cover_h = current_cover.size
        scale_cover = min(target_size[0] / cover_w, target_size[1] / cover_h)
        new_cover_w = int(cover_w * scale_cover)
        new_cover_h = int(cover_h * scale_cover)
        cover_resized = current_cover.resize((new_cover_w, new_cover_h), keep_ratio=False)

        cover_bg = BuildImage.new("L", target_size, 255)  # 白色背景
        x = (target_size[0] - new_cover_w) // 2
        y = (target_size[1] - new_cover_h) // 2
        cover_bg.paste(cover_resized, (x, y))
        wpix = np.array(cover_bg.image).astype(np.float64)

        # ---------- 处理底图（置于黑色背景） ----------
        base_w, base_h = current_base.size
        scale_base = min(target_size[0] / base_w, target_size[1] / base_h)
        new_base_w = int(base_w * scale_base)
        new_base_h = int(base_h * scale_base)
        base_resized = current_base.resize((new_base_w, new_base_h), keep_ratio=False)

        base_bg = BuildImage.new("L", target_size, 0)  # 黑色背景
        x = (target_size[0] - new_base_w) // 2
        y = (target_size[1] - new_base_h) // 2
        base_bg.paste(base_resized, (x, y))
        bpix = np.array(base_bg.image).astype(np.float64)

        # ---------- 棋盘格化（可选） ----------
        if chess:
            wpix[::2, ::2] = 255.0
            bpix[1::2, 1::2] = 0.0

        # ---------- 核心算法（与原插件一致） ----------
        wpix = wpix * 0.5 + 128
        bpix = bpix * 0.5

        a = 1.0 - wpix / 255.0 + bpix / 255.0
        r = np.where(np.abs(a) > 1e-6, bpix / a, 255.0)

        rgb = np.clip(r, 0, 255).astype(np.uint8)
        alpha = np.clip(a * 255.0, 0, 255).astype(np.uint8)

        result_arr = np.dstack([rgb, rgb, rgb, alpha])
        result_img = Image.fromarray(result_arr, "RGBA")
        return BuildImage(result_img)

    return make_png_or_gif(images, make)


# 注册到 meme 生成器
add_meme(
    "miragetank_gray",
    miragetank_gray,
    min_images=2,
    max_images=2,
    min_texts=0,
    max_texts=0,
    keywords=["灰色幻影坦克", "灰幻"],
    date_created=datetime(2026, 3, 5),
    date_modified=datetime(2026, 3, 5),
)