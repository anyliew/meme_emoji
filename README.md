<div align="center">
<img src="https://upload-bbs.miyoushe.com/upload/2025/05/08/365152535/0a154b759159adf6beb79d1582528fae_4082085489423633137.png" width=200 />

# meme_emoji 

<p align="center">
  <img src="https://img.shields.io/github/license/MemeCrafters/meme-generator" alt="license">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python">
  <a href="https://pypi.org/project/meme-generator">
    <img src="https://badgen.net/pypi/v/meme-generator" alt="pypi">
  </a>
  <a href="https://qm.qq.com/q/DVb9aGPmaQ">
    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-743103809-orange">
  </a>
</p>
</div>

## 表情包扩展仓库 meme_emoji 

🚀 基于 [meme-generator](https://github.com/MemeCrafters/meme-generator) 做的扩展表情包仓库
*✨* 为你的聊天机器人添加更多趣味表情生成！

## 特性

- ✅ **海量表情** 偶尔做做热门表情包，也欢迎投稿高清有趣的素材
- ⚡ **实时生成** 支持通过指令快速生成表情
- 🔄 **搭配使用** 需要搭配 [meme-generator](https://github.com/MemeCrafters/meme-generator) 一起使用

- ✨**搭配演示架构图所示(仅供参考)：**
![架构图](./picture/meme_emoji.jpg)



## 已实现表情示例
### 简略清单
- 杯子系列 `[夏日琉璃子、琉璃子、圣修女、纪念版圣修女、限定版圣修女、对魔忍、偶像心跳、杰士邦、空气玩法]`
- OP `[名人名言大伟哥嘲笑指]`
- 芙芙指 `[芙宁娜嘲笑]`
- 表情三连 `[三连 内容]`
### 参考预览图：
<img src="./picture/Phone.png" alt="image-20250312190444844" style="zoom:50%;" />

## 表情包清单

```

1. aircraft_cup_air_play (空气玩法)
2. aircraft_cup_cleaning_liquid (清洗液)
3. aircraft_cup_commemorative_edition_saint_sister (纪念版圣修女)
4. aircraft_cup_hoshino_alice (拉拉队偶像)
5. aircraft_cup_idol_heartbeat (偶像心跳)
6. aircraft_cup_jissbon (杰士邦)
7. aircraft_cup_limited_edition_saint_sister (限定版圣修女)
8. aircraft_cup_liuli_zi (琉璃子)
9. aircraft_cup_pure_buttocks (纯洁臀)
10. aircraft_cup_saint_sister (圣修女)
11. aircraft_cup_selena (魔女之森)
12. aircraft_cup_summer_liuli_zi (夏日琉璃子)
13. aircraft_cup_taimanin_asgi (对魔忍)
14. all_the_days (一生一世)
15. atri_like (亚托莉喜欢)
16. begged_me (求我)
17. congyu_dislike (丛雨讨厌)
18. contract (⭐️💢契约/橙喵契约/卖身契)
19. deer_help (帮鹿/帮🦌)
20. deer_se (🦌/鹿)
21. dinosaur_head (恐龙头)
22. dog_face (🐶)
23. fbi_photo (fbi/FBI)
24. fireworks_head (烟花头像)
25. funina_finger (芙芙指)
26. gong_xi_fa_cai (恭喜发财)
27. hitachi_mako_together (和她在一起)
28. ice_tea_head (冰红茶)
29. ikun_durian_head (榴莲坤头)
30. ikun_head (小黑子)
31. kfc_head (KFC/kfc)
32. kun_like (坤坤喜欢)
33. kurogames_mp (鸣批/鸣P/鸣p/鸣潮玩家/鸣潮男)
34. kurogames_phoebe_say (菲比说)
35. kurogames_songlun (松伦哥指/潮批)
36. mahiro_fuck (真寻中指/中指/🖕🏻)
37. mi_monkey (米猴/🐒/🐵)
38. mihoyo_elysia_come (爱莉希雅降临)
39. mihoyo_funina_death_penalty (死刑)
40. mihoyo_funina_round_head (芙芙圆形头像)
41. mihoyo_funina_square_head (芙芙方形头像)
42. mihoyo_genshin_impact_op (OP/op/Op/oP)
43. mihoyo_genshin_impact_players (原批/原神玩家)
44. miss_in_my_sleep (睡梦中想念)
45. murasame_blackboard (丛雨黑板)
46. murasame_husband (丛雨老公)
47. murasame_like (丛雨喜欢)
48. s_ninja (S忍/s忍)
49. spend_christmas (一起圣诞)
50. swimsuit_group_photo (泳衣合影)
51. together_two (在一起)
52. torture_yourself (折磨自己)
53. xinxi_news (新喜报)
54. youzi_kitchen (柚子厨)
55. youzi_question_mark (震惊柚子厨)

```



### 仓库文件信息

| Name      | Info                   |
| --------- | ---------------------- |
| ----      |                        |
| docker    | docker compose编排文件 |
| emoji     | 表情包文件             |
| picture   | 文档引用图片           |
| LICENSE   | 许可文件               |
| README.md | 说明文档               |


### Windows Config:
> 文件参考路径 C:\Users\liew\AppData\Roaming\meme_generator\config.toml
```bash
[meme]
load_builtin_memes = true  # 是否加载内置表情包
meme_dirs = ["D:/meme_emoji/emoji"] # 加载其他位置的表情包，填写文件夹路径
```

### Linux Config:
> 文件参考路径 /root/.config/meme_generator/config.toml
```bash
[meme]
load_builtin_memes = true  # 是否加载内置表情包
meme_dirs = ["/opt/meme_emoji/emoji"]  # 加载其他位置的表情包，填写文件夹路径
```

## 相关链接

- [meme-generator](https://github.com/MemeCrafters/meme-generator) 的Wiki：[--> Wiki <--](https://github.com/MemeCrafters/meme-generator/wiki)

- [MemeCrafters/meme-generator-contrib](https://github.com/MemeCrafters/meme-generator-contrib) meme-generator 额外表情仓库

## 反馈
单个表情有问题反馈请附带日志和截图

答复受限网络没那么快及时处理

> issues https://github.com/anyliew/meme_emoji/issues 

### meme_emoji 交流群 743103809 

> 欢迎进来投稿高清素材，看到一些有趣的素材图片会制作成表情更新到本仓库

## 声明

本仓库的表情素材等均来自网络，如有侵权请联系作者删除
