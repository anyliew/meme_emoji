<div align="center">
<img src="./docs/picture/logo.png" width=200 />

# meme_emoji 

<p align="center">
  <img src="https://img.shields.io/github/license/MemeCrafters/meme-generator" alt="license">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python">
  <a href="https://pypi.org/project/meme-generator">
    <img src="https://badgen.net/pypi/v/meme-generator" alt="pypi">
  </a>
</p>
</div>

## meme_emoji 表情包扩展仓库 

🚀 基于 [meme-generator](https://github.com/MemeCrafters/meme-generator) 做的表情包扩展仓库~

*✨* 为你的聊天机器人添加更多趣味表情生成！

> [!NOTE]
>
> 请注意，本仓库的内容仅支持以下特定版本的依赖库：
>
> - `meme_generator == 0.1.14`（最高兼容版本）
> - `nonebot-plugin-memes == 0.7.12`（最高兼容版本）
>
> 为确保功能正常运行，请勿使用高于指定版本的依赖库。
>
> 若您已安装更高版本，建议使用以下命令进行版本调整：
>
> ```
> pip install meme_generator==0.1.14
> ```
>
> Nonebot用户请使用：
> ```
> pip install nonebot-plugin-memes==0.7.12 && pip install meme_generator==0.1.14
> ```
> Nonebot的目录下pyproject.toml文件新增添加：
> ```
> plugins = ["nonebot_plugin_memes"]
> ```
> 

## ✨特性

- ✅ **海量表情** 偶尔做做热门表情包，也欢迎投稿高清有趣的素材
- ⚡ **实时生成** 支持通过指令快速生成表情
- 🔄 **搭配使用** 需要搭配 [meme-generator](https://github.com/MemeCrafters/meme-generator) 一起使用

- ✨**搭配演示架构图所示(仅供参考)：**

<img src="./docs/picture/meme_emoji.jpg" alt="架构图" style="zoom:30%;" />



## 🤣表情示例

### 🖼参考预览图：

<details><summary>🖼点击展开 预览图 "夏日琉璃子"</summary><p>
<a><img src="./docs/picture/Phone.png"></a>
</details>

### 🖼简略清单

- 杯子系列 `[夏日琉璃子、琉璃子、圣修女、纪念版圣修女、限定版圣修女、对魔忍、偶像心跳、杰士邦、空气玩法]`

### 🖼完整清单

表情详细信息、表情预览等可以在 [--> 表情列表 <--](./docs/meme_emoji_keywords.md) 查看


## 📄使用教程

------
### 🐧Linux 系统使用教程
#### 下载

> [!TIP]
>
> 推荐下载在 linux系统的 /opt 目录下 亦可以自行调整


```
git clone https://github.com/anyliew/meme_emoji /opt/meme_emoji/
```
> [!TIP]
>
> 网络不好推荐这个
```
git clone https://ghfast.top/https://github.com/anyliew/meme_emoji /opt/meme_emoji/
```



#### 添加配置文件
> [!IMPORTANT]
> 文件名以及路径 : /root/.config/meme_generator/config.toml
>
> 我默认使用root账户的，非root用户请自行判断替换
>
>  [meme-generator](https://github.com/MemeCrafters/meme-generator) 第一次运行会生成这个文件，没有的话自行手动创建

config.toml 配置内容如下：

```
[meme]
load_builtin_memes = true  # 是否加载内置表情包
meme_dirs = ["/opt/meme_emoji/emoji"]  # 加载其他位置的表情包，填写文件夹路径
```
#### 更新 
> [!CAUTION]
> 通过Git 版本控制系统中一个常用的命令，用于从远程仓库获取最新代码并合并到本地
> 从而到达更新获取最新的 meme_emoji 表情包内容
```
cd /opt/meme_emoji/ && git pull
```

### 🪟Windows 系统使用教程

#### 下载

> [!TIP]
>
> 推荐下载在 Windows 系统的 C盘 目录下 亦可以自行调整


```
git clone https://github.com/anyliew/meme_emoji C:\meme_emoji
```
> [!TIP]
>
> 网络不好推荐这个
```
git clone https://ghfast.top/https://github.com/anyliew/meme_emoji C:\meme_emoji
```



#### 添加配置文件
> [!IMPORTANT]
> 文件名以及路径 : C:\Users\Administrator\AppData\Roaming\meme_generator\config.toml
>
> 我默认使用Administrator账户的，非Administrator用户请自行判断替换
>
>  [meme-generator](https://github.com/MemeCrafters/meme-generator) 第一次运行会生成这个文件，没有的话自行手动创建

config.toml 配置内容如下：

```
[meme]
load_builtin_memes = true  # 是否加载内置表情包
meme_dirs = ["C:/meme_emoji/emoji"]  # 加载其他位置的表情包，填写文件夹路径
```
#### 更新 
> [!CAUTION]
> 通过Git 版本控制系统中一个常用的命令，用于从远程仓库获取最新代码并合并到本地
> 从而到达更新获取最新的 meme_emoji 表情包内容
```
cd C:\meme_emoji\ && git pull
```
------



## 💐鸣谢

感谢以下开发者对 meme_emoji 仓库作出的贡献

<a href="https://github.com/anyliew/meme_emoji/graphs/contributors">
  <img src="./docs/picture/partner.jpg" />
</a>


## 📝 反馈
### ⁉issues

单个表情有问题反馈请附带日志和截图
答复受限网络没那么快及时处理

> issues https://github.com/anyliew/meme_emoji/issues 


## 🗳投稿

> 🚧欢迎投稿高清素材，看到一些有趣的素材图片会制作成表情更新到本仓库！
>
> 通过issues中的模板 “投稿素材” 进行投稿，如果能Pr则更加完美，实在是泰裤辣~


## 🔗相关链接

### meme-generator
- [meme-generator](https://github.com/MemeCrafters/meme-generator) 

### wiki 文档
- [meme-generator wiki](https://github.com/MemeCrafters/meme-generator/wiki)
- [meme_emoji wiki](https://github.com/anyliew/meme_emoji/wiki)

### 额外表情仓库

- [meme-generator-contrib](https://github.com/MemeCrafters/meme-generator-contrib) 
- [meme_emoji](https://github.com/anyliew/meme_emoji) 
- [meme-generator-jj](https://github.com/jinjiao007/meme-generator-jj) 


## 📌声明

本仓库的表情素材等均来自网络，如有侵权请通过issues联系作者删除
