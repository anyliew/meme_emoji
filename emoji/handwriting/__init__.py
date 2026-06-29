from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage, Text2Image
from meme_generator import add_meme
img_dir = Path(__file__).parent / "images"
def handwriting(images, texts: list[str], args):
    text = texts[0][:500]  
    text_img = (
        Text2Image.from_text(text, 200, 
                            font_families=["FZSJ-QINGCRJ"], 
                            fill="black")
        .wrap(2360)  
        .to_image()
    )
    text_img = (
        BuildImage(text_img)
        .resize_canvas((2000, 1800), direction="northwest")  
        .rotate(17, expand=True)  
    )
    frame = BuildImage.open(img_dir / "0.jpg")
    text_position = (580, 500)
    frame.paste(text_img, text_position, alpha=True)
    return frame.save_jpg()
add_meme(
    "handwriting",
    handwriting,
    min_texts=1,
    max_texts=1,
    default_texts=["你好，世界！"],  
    keywords=["手写"],
    date_created=datetime(2025, 6, 11),
    date_modified=datetime(2025, 6, 11),
)
