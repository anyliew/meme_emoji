import os
import ast
from datetime import datetime

MEMES_DIR = "./emoji"
OUTPUT_DIR = "./docs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "meme_keywords.md")

# GitHub 仓库信息 - 用于 Wiki 链接
GITHUB_REPO = os.getenv("GITHUB_REPOSITORY", "anyliew/meme_emoji")
# 表格列宽配置
# 格式: "列名": {"type": "width/max-width", "value": "数值"} 或 None (自适应)
TABLE_COLUMN_WIDTHS = {
    "index": {"type": "width", "value": "50"},           # # (固定宽度)
    "preview": None,                                        # 预览 (自适应)
    "keywords": {"type": "max-width", "value": "180"},   # 关键词 (最大宽度)
    "images": {"type": "width", "value": "70"},          # 图片 (固定宽度)
    "texts": {"type": "width", "value": "70"},           # 文字 (固定宽度)
    "defaults": {"type": "max-width", "value": "180"},   # 默认文字 (最大宽度)
    "module": None,                                      # 模块 (自适应)
    "date": {"type": "width", "value": "135"}            # 创建日期 (固定宽度)
}

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
    # 使用HTML表格来更好地控制列宽
    def get_style_attr(width_config):
        if not width_config:
            return ''
        width_type = width_config["type"]
        width_value = width_config["value"]
        return f' style="{width_type}: {width_value}px;"'
    
    lines = [
        '<table>',
        '<thead>',
        '<tr>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["index"])}>#</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["preview"])}>预览</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["keywords"])}>关键词</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["images"])}>图片</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["texts"])}>文字</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["defaults"])}>默认文字</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["module"])}>模块</th>',
        f'<th{get_style_attr(TABLE_COLUMN_WIDTHS["date"])}>创建日期</th>',
        '</tr>',
        '</thead>',
        '<tbody>'
    ]
    
    for idx, (module, info) in enumerate(modules_info, 1):
        kw_str = "<br/>".join(info["keywords"]) if info["keywords"] else "&nbsp;"
        module_link = f'<a href="https://github.com/{GITHUB_REPO}/tree/master/memes/{module}">{module}</a>'
        date_str = info["date_created"].strftime("%Y-%m-%d") if info["date_created"] else "&nbsp;"
        image_count = str(info.get("min_images")) if info.get("min_images") is not None else "&nbsp;"
        text_count = str(info.get("min_texts")) if info.get("min_texts") is not None else "&nbsp;"
        default_texts = "<br/>".join(t.replace("\n", "<br/>") for t in info["default_texts"]) if info["default_texts"] else "&nbsp;"
        
        if module in previews_by_module:
            preview = f'<img src="{previews_by_module.get(module)}" width="50">'
        else:
            preview = "&nbsp;"
            
        lines.append(f'<tr>')
        lines.append(f'<td align="center">{idx}</td>')
        lines.append(f'<td align="center">{preview}</td>')
        lines.append(f'<td>{kw_str}</td>')
        lines.append(f'<td align="center">{image_count}</td>')
        lines.append(f'<td align="center">{text_count}</td>')
        lines.append(f'<td>{default_texts}</td>')
        lines.append(f'<td>{module_link}</td>')
        lines.append(f'<td align="center">{date_str}</td>')
        lines.append(f'</tr>')
    
    lines.extend(['</tbody>', '</table>'])
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
                    # 使用 GitHub raw 链接，让 Wiki 能正确显示图片
                    # 去掉路径开头的 './' 
                    clean_path = image_path.lstrip("./")
                    github_raw_path = f"https://raw.githubusercontent.com/{GITHUB_REPO}/master/{clean_path}"
                    previews_by_module[folder] = github_raw_path

    # 按创建时间倒序
    modules_info.sort(key=lambda x: x[1]["date_created"] or datetime.min, reverse=True)
    meme_count = len(modules_info)
    header = f"# ✨Meme Keywords\n\n**🎈总表情数：{meme_count}**\n"
    
    html_table = generate_markdown_table(modules_info, previews_by_module)
    markdown = header + "\n\n" + html_table

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ 输出完成：{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
