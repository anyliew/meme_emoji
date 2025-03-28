# meme_emoji 
## 表情包扩展仓库 meme_emoji 

🚀 基于 [meme-generator](https://github.com/MemeCrafters/meme-generator) 插件做的扩展表情包仓库

*✨* 为你的聊天机器人添加更多趣味表情生成功能！

## 特性

- ✅ **海量模板** 偶尔做做热门表情包模板
- ⚡ **实时生成** 支持通过指令快速生成表情
- 🔄 **搭配使用** 需要搭配 [meme-generator](https://github.com/MemeCrafters/meme-generator) 一起使用


## 已实现表情示例

（此处可添加你的特色表情包截图，例如）
- 杯子系列 `[夏日琉璃子、琉璃子、圣修女、纪念版圣修女、限定版圣修女、对魔忍、偶像心跳、杰士邦、空气玩法]`<img src="./picture/liulizi.png" alt="image-20250312190444844" style="zoom:50%;" />
- 名人名言 `[大伟哥嘲笑指]`
- 芙芙指 `[芙宁娜嘲笑]`
- 表情三连 `[三连 内容]`


## 配置参考

### Windows Config:

> 文件参考路径 C:\Users\liew\AppData\Roaming\meme_generator\config.toml
>

```bash
[meme]
load_builtin_memes = true  # 是否加载内置表情包
meme_dirs = ["D:/meme_emoji/aircraft_cup","D:/meme_emoji/emoji"]  # 加载其他位置的表情包，填写文件夹路径
meme_disabled_list = []  # 禁用的表情包列表，填写表情的 `key`

[gif]
gif_max_size = 10.0  # 限制生成的 gif 文件大小，单位为 Mb
gif_max_frames = 100  # 限制生成的 gif 文件帧数

[log]
log_level = "INFO"  # 日志等级

```

### Linux Config:

> 文件参考路径 /root/.config/meme_generator/config.toml
>

```bash
[meme]
load_builtin_memes = true  # 是否加载内置表情包
meme_dirs = ["/opt/meme_emoji/aircraft_cup","/opt/meme_emoji/emoji"]  # 加载其他位置的表情包，填写文件夹路径
meme_disabled_list = []  # 禁用的表情包列表，填写表情的 `key`

[gif]
gif_max_size = 10.0  # 限制生成的 gif 文件大小，单位为 Mb
gif_max_frames = 100  # 限制生成的 gif 文件帧数

[log]
log_level = "INFO"  # 日志等级
```

## 相关链接

-  [meme-generator](https://github.com/MemeCrafters/meme-generator) 插件的Wiki：[--> Wiki <--](https://github.com/MemeCrafters/meme-generator/wiki)


其他表情仓库：
- [MemeCrafters/meme-generator-contrib](https://github.com/MemeCrafters/meme-generator-contrib) meme-generator 额外表情仓库


## 声明
本仓库的表情素材等均来自网络，如有侵权请联系作者删除


![芙宁娜dome](./picture/logo.png)
