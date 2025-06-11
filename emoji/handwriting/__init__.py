from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage, Text2Image
from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"

def handwriting(images, texts: list[str], args):
    # 截取文本（可根据需要调整最大长度）
    text = texts[0][:500]  # 暂定最大500字符
    
    # 生成手写体文字（字号调整为60更接近手写效果）
    text_img = (
        Text2Image.from_text(text, 200, 
                            font_families=["FZSJ-QINGCRJ"], 
                            fill="black")
        .wrap(2360)  # 换行宽度设为750（适配800px底图）
        .to_image()
    )
    
    # 旋转处理（逆时针15度）
    text_img = (
        BuildImage(text_img)
        .resize_canvas((2000, 1800), direction="northwest")  # 扩大垂直空间
        .rotate(17, expand=True)  # 正角度表示逆时针旋转
    )

    # 加载800x800底图模板
    frame = BuildImage.open(img_dir / "0.jpg")
    
    # 预估定位（需要根据实际效果微调）
    # 主文本定位（X/Y轴偏移量）
    text_position = (580, 500)
    frame.paste(text_img, text_position, alpha=True)

    return frame.save_jpg()

add_meme(
    "handwriting",
    handwriting,
    min_texts=1,
    max_texts=1,
    default_texts=["你好，世界！"],  # 更符合手写体的示例文本
    keywords=["手写"],
    date_created=datetime(2025, 6, 11),
    date_modified=datetime(2025, 6, 11),
)