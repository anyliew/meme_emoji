import os
import ast
from datetime import datetime

MEMES_DIR = "./emoji"
OUTPUT_DIR = "./docs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "meme_emoji_keywords.md")


def extract_meme_info(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"❌ 解析失败 {file_path}: {e}")
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'add_meme':
            info = {
                "keywords": [],
                "min_images": None,
                "min_texts": None,
                "default_texts": [],
                "date_created": None,
            }
            for kw in node.keywords:
                if kw.arg == 'keywords' and isinstance(kw.value, ast.List):
                    info["keywords"] = [elt.s for elt in kw.value.elts if isinstance(elt, ast.Str)]
                elif kw.arg == 'min_images' and isinstance(kw.value, ast.Constant):
                    info["min_images"] = kw.value.value
                elif kw.arg == 'min_texts' and isinstance(kw.value, ast.Constant):
                    info["min_texts"] = kw.value.value
                elif kw.arg == 'default_texts' and isinstance(kw.value, ast.List):
                    info["default_texts"] = [elt.s for elt in kw.value.elts if isinstance(elt, ast.Str)]
                elif kw.arg == 'date_created' and isinstance(kw.value, ast.Call) and getattr(kw.value.func, 'id', '') == 'datetime':
                    args = [a.n for a in kw.value.args if isinstance(a, ast.Constant)]
                    if len(args) >= 3:
                        info["date_created"] = datetime(*args)
            return info
    return None


def find_first_image_path(subdir):
    images_dir = os.path.join(subdir, "images")
    if not os.path.isdir(images_dir):
        return None

    for file in sorted(os.listdir(images_dir)):
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            return os.path.join(images_dir, file).replace("\\", "/")
    return None


def generate_markdown_table(modules_info, previews_by_module):
    lines = [
        "| # | 预览 | 关键词 | 图片数 | 文字数 | 默认文字 | 模块 | 创建日期 |",
        "|---|------|--------|-----------|--------|--------|------------|------|"
    ]
    for idx, (module, info) in enumerate(modules_info, 1):
        kw_str = "、 ".join(info["keywords"]) if info["keywords"] else "&nbsp;"
        module_link = f"[{module}](.{MEMES_DIR}/{module})"
        date_str = info["date_created"].strftime("%Y-%m-%d") if info["date_created"] else "&nbsp;"
        image_count = str(info.get("min_images")) if info.get("min_images") is not None else "&nbsp;"
        text_count = str(info.get("min_texts")) if info.get("min_texts") is not None else "&nbsp;"
        default_texts = "、 ".join(t.replace("\n", "") for t in info["default_texts"]) if info["default_texts"] else "&nbsp;"
        preview = f'<img src="{previews_by_module.get(module)}" width="100">' if module in previews_by_module else "&nbsp;"
        lines.append(f"| {idx} | {preview} | {kw_str} | {image_count} | {text_count} | {default_texts} | {module_link} | {date_str} |")
    return "\n".join(lines)


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    modules_info = []
    previews_by_module = {}

    for folder in os.listdir(MEMES_DIR):
        subdir = os.path.join(MEMES_DIR, folder)
        init_file = os.path.join(subdir, "__init__.py")

        if os.path.isdir(subdir) and os.path.isfile(init_file):
            info = extract_meme_info(init_file)
            if info:
                modules_info.append((folder, info))
                image_path = find_first_image_path(subdir)
                if image_path:
                    relative_path = os.path.relpath(image_path, OUTPUT_DIR).replace("\\", "/")
                    previews_by_module[folder] = relative_path

    # 按创建时间倒序
    modules_info.sort(key=lambda x: x[1]["date_created"] or datetime.min, reverse=True)
    meme_count = len(modules_info)
    header = f"# ✨meme_emoji 表情列表清单\n\n**🎈总表情数：{meme_count}**\n"
    markdown_table = generate_markdown_table(modules_info, previews_by_module)
    markdown = header + "\n\n" + markdown_table

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ 输出完成：{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
