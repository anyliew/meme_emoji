# GitHub Bot 自动回复设置指南

本项目已集成GitHub Actions驱动的自动回复机器人，可以自动处理Issues和Pull Requests。

## 🚀 功能特性

### ✅ 已实现功能
- **Issue自动回复**: 根据标题关键词智能回复
- **PR自动回复**: 欢迎新贡献者并提供审核清单
- **智能标签**: 根据内容自动添加相关标签
- **定期状态更新**: 每周检查并更新长期无响应的issue
- **生成周报**: 统计项目活动数据

### 🤖 自动回复类型

#### Issue回复模板
- 🐛 **Bug报告**: 引导用户提供复现步骤和环境信息
- 🚀 **功能建议**: 说明评估流程和时间安排
- 📖 **文档问题**: 承诺改进文档质量
- 👋 **通用回复**: 感谢反馈并说明处理流程

#### PR回复模板
- 🎉 **欢迎贡献者**: 感谢贡献并说明审核流程
- 📋 **审核清单**: 提醒代码规范、测试、文档等要求
- 📊 **PR统计**: 显示修改文件数和PR类型
- 🏷️ **自动标签**: 根据内容和规模自动分类

## 📋 设置步骤

### 1. 创建所需标签

在仓库的 **Issues** → **Labels** 页面创建以下标签：

#### 基础标签
```
bug - 🐛 - #d73a49 - Bug报告
enhancement - ✨ - #a2eeef - 功能增强
documentation - 📖 - #0075ca - 文档相关
question - ❓ - #d876e3 - 问题咨询
performance - ⚡ - #fbca04 - 性能优化
security - 🔒 - #b60205 - 安全相关
```

#### 优先级标签
```
priority/high - 🔴 - #b60205 - 高优先级
priority/medium - 🟡 - #fbca04 - 中优先级  
priority/low - 🟢 - #0e8a16 - 低优先级
```

#### PR大小标签
```
size/small - S - #28a745 - 小型PR (≤3文件)
size/medium - M - #ffc107 - 中型PR (4-10文件)
size/large - L - #dc3545 - 大型PR (>10文件)
```

#### 平台标签
```
platform/windows - 🪟 - #0078d4 - Windows平台
platform/linux - 🐧 - #f89820 - Linux平台
platform/mac - 🍎 - #999999 - macOS平台
```

#### 组件标签
```
component/bilibili - 📺 - #00a1d6 - B站相关
component/tiktok - 🎵 - #ff0050 - 抖音相关
component/youtube - ▶️ - #ff0000 - YouTube相关
component/music - 🎵 - #1db954 - 音乐功能
component/summary - 📄 - #6f42c1 - 链接总结功能
```

#### 状态标签
```
stale - ⏰ - #795548 - 长期无响应
needs-response - 💬 - #8e44ad - 需要回复
refactor - ♻️ - #00d4aa - 重构相关
test - 🧪 - #17becf - 测试相关
```

### 2. 启用GitHub Actions

1. 进入仓库 **Settings** → **Actions** → **General**
2. 选择 **Allow all actions and reusable workflows**
3. 在 **Workflow permissions** 部分选择 **Read and write permissions**
4. 勾选 **Allow GitHub Actions to create and approve pull requests**

### 3. 创建里程碑（可选）

为bug自动分配功能创建里程碑：
1. 进入 **Issues** → **Milestones**
2. 创建如 `v1.1.0`、`v1.2.0` 等版本里程碑
3. bot会自动将bug分配到最近的开放里程碑

### 4. 测试设置

创建一个测试issue验证：
1. 标题包含 "bug" 或 "功能" 关键词
2. 查看是否收到自动回复
3. 检查是否自动添加了相关标签

## 🔧 自定义配置

### 修改回复模板

编辑 `.github/workflows/` 目录下的workflow文件：
- `auto-reply-issues.yml` - Issue回复模板
- `auto-reply-prs.yml` - PR回复模板  
- `auto-label.yml` - 标签规则
- `status-update.yml` - 定期更新规则

### 调整触发条件

修改workflow文件中的 `on` 部分：
```yaml
on:
  issues:
    types: [opened, labeled]  # 添加labeled触发
  pull_request:
    types: [opened, edited]   # 添加edited触发
```

### 修改定时任务

在 `status-update.yml` 中调整cron表达式：
```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 每天凌晨2点运行
```

## 📈 监控和维护

### 查看运行日志
1. 进入 **Actions** 页面
2. 点击具体的workflow运行记录
3. 查看详细日志和错误信息

### 常见问题排查
- **权限错误**: 检查Actions权限设置
- **标签不存在**: 确保创建了所有必需的标签
- **API限制**: GitHub API有频率限制，大量操作时可能触发

### 性能优化建议
- 限制单次处理的issue数量（当前设置为50）
- 合理设置触发条件避免重复运行
- 定期清理过时的workflow运行记录

## 🎯 最佳实践

1. **渐进式部署**: 先在测试仓库验证功能
2. **定期审查**: 每月检查自动回复效果和用户反馈
3. **模板优化**: 根据项目特点调整回复内容
4. **标签管理**: 保持标签体系简洁清晰
5. **用户反馈**: 收集用户对自动回复的意见

---

📝 **注意**: 此bot完全基于GitHub Actions，无需外部服务器，维护成本极低。所有配置都通过workflow文件管理，便于版本控制和团队协作。