#!/usr/bin/env python3
"""meme_emoji 表情代码静态检查。

用法:
  python check_memes.py            # 检查本次暂存(staged)的表情文件 (pre-commit 默认)
  python check_memes.py --all      # 扫描 emoji/ 下全部表情
  python check_memes.py --files a b ...  # 检查指定文件/路径
  python check_memes.py --install-hook   # 安装为 .git/hooks/pre-commit

检查项:
  [ERROR] A. max_texts>0 但代码从不消费 texts[]  -> 声明不一致
  [ERROR] B. 导入 TextOverLength 但从未使用       -> 死导入
  [ERROR] D. make_jpg_or_gif 且模板含透明像素      -> 输出黑底(需 PIL)
  [WARN ] C. 缺少 tags=MemeTags.xxx              -> 分批补全中, 暂不阻塞

ERROR 存在时退出码 1 (阻塞提交); 仅 WARN 时退出码 0。
"""
import os
import re
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
EMOJI_DIR = os.path.join(HERE, "emoji")


def get_staged_emoji_files():
    try:
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=HERE, text=True, stderr=subprocess.DEVNULL,
        )
    except Exception:
        return []
    files = []
    for rel in out.splitlines():
        if re.match(r"emoji/[^/]+/__init__\.py$", rel):
            files.append(os.path.join(HERE, rel))
    return files


def scan_file(path):
    errors = []
    warnings = []
    s = open(path, encoding="utf-8").read()
    name = os.path.basename(os.path.dirname(path))

    m = re.search(r"max_texts=(\d+)", s)
    max_t = int(m.group(1)) if m else 0
    has_texts = "texts[" in s
    to_count = s.count("TextOverLength")
    has_tags = "tags=" in s
    uses_jpg = "make_jpg_or_gif" in s

    # A. texts vs max_texts
    if max_t > 0 and not has_texts:
        errors.append(f"{name}: max_texts={max_t} 但代码从不消费 texts[] (声明不一致)")

    # B. 死导入 TextOverLength
    if to_count == 1:
        errors.append(f"{name}: 导入了 TextOverLength 但未使用 (死导入)")

    # C. tags (警告)
    if not has_tags:
        warnings.append(f"{name}: 缺少 tags=MemeTags.xxx (建议补全)")

    # D. jpg + 透明模板
    if uses_jpg:
        try:
            from PIL import Image
            d = os.path.dirname(path)
            p = os.path.join(d, "images", "0.png")
            j = os.path.join(d, "images", "0.jpg")
            tgt = p if os.path.exists(p) else (j if os.path.exists(j) else None)
            if tgt:
                im = Image.open(tgt)
                trans = False
                if im.mode in ("RGBA", "LA") and im.split()[-1].getextrema()[0] < 255:
                    trans = True
                elif im.mode == "P" and "transparency" in im.info:
                    trans = True
                if trans:
                    errors.append(
                        f"{name}: 使用 make_jpg_or_gif 但模板 {os.path.basename(tgt)} "
                        f"含透明像素 (会黑底, 应改 make_png_or_gif)"
                    )
        except Exception as e:
            warnings.append(f"{name}: 无法检测模板透明度 ({e}); 请手动确认 jpg 是否安全")

    return errors, warnings


def main():
    args = sys.argv[1:]
    if "--install-hook" in args:
        install_hook()
        return

    if "--all" in args:
        targets = sorted(
            os.path.join(EMOJI_DIR, d, "__init__.py")
            for d in os.listdir(EMOJI_DIR)
            if os.path.isfile(os.path.join(EMOJI_DIR, d, "__init__.py"))
        )
    elif args:
        targets = [a if os.path.isabs(a) else os.path.join(os.getcwd(), a) for a in args]
    else:
        targets = get_staged_emoji_files()

    if not targets:
        print("没有需要检查的文件。")
        return

    all_err, all_warn = [], []
    for p in targets:
        e, w = scan_file(p)
        all_err += e
        all_warn += w

    for w in all_warn:
        print("WARN :", w)
    for e in all_err:
        print("ERROR:", e)
    print(f"\n扫描 {len(targets)} 个文件: ERROR={len(all_err)}, WARN={len(all_warn)}")
    sys.exit(1 if all_err else 0)


def install_hook():
    hook_dir = os.path.join(HERE, ".git", "hooks")
    os.makedirs(hook_dir, exist_ok=True)
    hook_path = os.path.join(hook_dir, "pre-commit")
    script = os.path.join(HERE, "check_memes.py")
    content = f"""#!/bin/sh
# meme_emoji pre-commit 静态检查 (由 check_memes.py 安装)
PY="$(command -v python3 || command -v python)"
if [ -z "$PY" ]; then
  echo "[check_memes] 未找到 python, 跳过检查"
  exit 0
fi
"$PY" "{script}"
"""
    with open(hook_path, "w", encoding="utf-8") as f:
        f.write(content)
    try:
        os.chmod(hook_path, 0o755)
    except Exception:
        pass
    print("pre-commit hook 已安装:", hook_path)
    print("如需跳过: git commit --no-verify")


if __name__ == "__main__":
    main()
