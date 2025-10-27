# KVMARM 邮件列表周报告生成器

自动从 KVMARM 邮件列表 Git 仓库生成周报告，支持 AI 总结（OpenAI/Claude）和基于规则的总结。

## 🌐 在线查看报告

**GitHub Pages**: https://onlinefchen.github.io/kvm-ai-robot/

- 📅 **最新周报（上周）**: https://onlinefchen.github.io/kvm-ai-robot/ （自动跳转）
- 📚 **历史归档**: https://onlinefchen.github.io/kvm-ai-robot/archive.html
- 🤖 **GitHub Actions**: https://github.com/onlinefchen/kvm-ai-robot/actions

每周一上午 8:00（北京时间）自动生成上周完整报告！

---

## 快速开始

### 1. 生成本周报告（默认）
```bash
python3 analyze_with_ai_summary.py
```

### 2. 生成指定日期范围的报告
```bash
# 从2025年初到现在的所有周报告
python3 analyze_with_ai_summary.py --start 2025-01-01

# 生成第一季度的所有周报告
python3 analyze_with_ai_summary.py --start 2025-01-01 --end 2025-03-31

# 生成特定几周
python3 analyze_with_ai_summary.py --start 2025-03-10 --end 2025-03-23
```

### 3. 使用 AI 模型生成总结

#### OpenAI
```bash
# 设置 API Key
export OPENAI_API_KEY='your-api-key'

# 使用默认模型 (gpt-4o-mini)
python3 analyze_with_ai_summary.py --ai openai

# 批量生成（使用 OpenAI）
python3 analyze_with_ai_summary.py --start 2025-01-01 --end 2025-03-31 --ai openai

# 指定模型
python3 analyze_with_ai_summary.py --ai openai --model gpt-4o
```

#### Claude
```bash
# 设置 API Key
export ANTHROPIC_API_KEY='your-api-key'

# 使用默认模型 (claude-3-5-sonnet-20241022)
python3 analyze_with_ai_summary.py --ai claude

# 指定模型
python3 analyze_with_ai_summary.py --ai claude --model claude-3-haiku-20240307
```

## 功能特性

### 📅 智能周范围计算
- 自动计算 start 所在周到 end 所在周的所有完整周
- 每周从周一开始，到周日结束（ISO 8601 标准）

### 🔄 智能文件管理
- **定时任务（周一）**：强制覆盖上周报告，确保数据最完整
- **当前周**：总是重新生成（数据可能更新）
- **历史周**：已存在则跳过（避免重复生成，节省 API 费用）
- **空周**：没有邮件自动跳过
- **强制模式（--force）**：覆盖所有已存在的报告

### 🤖 多种 AI 后端支持
- **OpenAI**: GPT-4o, GPT-4o-mini
- **Claude**: Claude 3.5 Sonnet, Claude 3 Haiku
- **基于规则**: 无需 API，本地生成

### 📊 双格式输出
- **HTML**: 适合网页浏览，带样式和归档页面
- **Markdown**: 适合文本查看和版本控制

## 输出文件

```
docs/
├── kvmarm_2025_week01.html    # HTML 格式周报告
├── kvmarm_2025_week01.md      # Markdown 格式周报告
├── kvmarm_2025_week02.html
├── kvmarm_2025_week02.md
├── ...
└── archive.html               # 历史归档索引页面
```

## 命令行参数

```bash
python3 analyze_with_ai_summary.py [选项]
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `--start DATE` | 起始日期（包含该日期所在周） | `--start 2025-01-01` |
| `--end DATE` | 结束日期（包含该日期所在周，默认为今天） | `--end 2025-03-31` |
| `--ai BACKEND` | AI 后端: `openai`, `claude`, `none`（默认） | `--ai openai` |
| `--model MODEL` | AI 模型名称 | `--model gpt-4o-mini` |
| `--force` | 强制重新生成（覆盖已存在的历史报告） | `--force` |
| `--git-dir DIR` | Git 仓库路径（默认: `git/0.git`） | `--git-dir /path/to/repo` |
| `-o FILE` | 输出文件路径（不含扩展名，仅单周模式） | `-o report` |
| `-h, --help` | 显示帮助信息 | `-h` |

## 工作原理

1. **日期计算**: 根据 start/end 参数计算需要生成的周列表
2. **邮件获取**: 从 Git 仓库获取每周的邮件（通过 `git log --since --until`）
3. **Thread 构建**: 根据邮件头（Message-ID, In-Reply-To, References）构建讨论线程
4. **分类整理**: 将 Thread 分类（PATCH, RFC, Bug Report, Question 等）
5. **AI 总结**: 对每个 Thread 生成中文总结（200-300字）
6. **双格式输出**: 生成 HTML 和 Markdown 两种格式
7. **归档页面**: 自动生成所有历史报告的归档索引

## 使用场景

### 场景1: GitHub Actions 自动化（推荐）
- 每周一上午 8:00（北京时间）自动生成上周完整报告
- 自动强制覆盖，确保数据最完整
- 支持手动触发，可选择：
  - 周报（上周完整报告）
  - 本周报告
  - 自定义日期范围

### 场景2: 本地生成本周报告
```bash
# 生成本周报告（默认）
python3 analyze_with_ai_summary.py
```

### 场景3: 批量生成历史报告
```bash
# 生成2025年第一季度所有报告（使用 OpenAI）
export OPENAI_API_KEY='your-key'
python3 analyze_with_ai_summary.py --start 2025-01-01 --end 2025-03-31 --ai openai
```

### 场景4: 补充生成缺失的周
```bash
# 从年初到现在，已存在的周会自动跳过
python3 analyze_with_ai_summary.py --start 2025-01-01
```

### 场景5: 强制重新生成历史报告
```bash
# 使用 --force 覆盖已存在的报告
python3 analyze_with_ai_summary.py --start 2025-10-01 --end 2025-10-31 --force
```

## 🚀 GitHub Actions 手动触发

访问 [GitHub Actions](https://github.com/onlinefchen/kvm-ai-robot/actions) 页面，点击 "Generate Weekly KVMARM Report" → "Run workflow"

### 可选参数

1. **报告类型**（下拉选择）
   - 📅 **周报（上周完整报告）** - 默认，生成上周一到上周日的完整报告
   - 📅 **本周报告** - 生成本周一到本周日的报告
   - 📅 **自定义日期范围** - 灵活指定任意日期范围

2. **起始日期**（仅自定义日期范围时填写）
   - 格式：YYYY-MM-DD
   - 示例：2025-01-01

3. **结束日期**（仅自定义日期范围时填写，可选）
   - 格式：YYYY-MM-DD
   - 不填写则默认为今天
   - 示例：2025-03-31

4. **强制重新生成**（开关，默认关闭）
   - 开启后覆盖已存在的历史报告
   - 适用于所有报告类型

### 使用示例

**快速生成上周报告**
1. 报告类型：选择"周报（上周完整报告）"
2. 点击 "Run workflow" ✅

**查看本周进展**
1. 报告类型：选择"本周报告"
2. 点击 "Run workflow" ✅

**生成某个月的所有报告**
1. 报告类型：选择"自定义日期范围"
2. 起始日期：2025-10-01
3. 结束日期：2025-10-31（或留空默认到今天）
4. 强制重新生成：勾选（如果需要覆盖）
5. 点击 "Run workflow" ✅

## 安装依赖

### 基础依赖
Python 3.7+ 标准库（无需额外安装）

### AI 功能（可选）
```bash
# 使用 OpenAI
pip3 install openai

# 使用 Claude
pip3 install anthropic
```

## 批量生成示例输出

```
==================================================
KVMARM 邮件列表周报告批量生成
==================================================

📅 日期范围: 2025-01-01 到 2025-03-31
📅 周范围: 2025年第1周 到 2025年第13周

==================================================
[1/13] 2025年第1周
==================================================
📅 日期范围: 2024-12-30 到 2025-01-05
📧 邮件数量: 29
✅ 2025年第1周报告生成完成

==================================================
[2/13] 2025年第2周
==================================================
📅 日期范围: 2025-01-06 到 2025-01-12
ℹ️  历史报告已存在，跳过

...

==================================================
🎉 批量生成完成！
==================================================

📊 生成统计：
   总周数: 13
   成功: 10
   跳过: 3
   失败: 0

📁 生成的报告位于 docs/ 目录：
   HTML 文件: 13
   Markdown 文件: 13

🌐 查看归档页面: docs/archive.html
```

## 注意事项

### ⚠️ API Key 安全
- **永远不要**将 API Key 硬编码在代码中
- 使用环境变量: `export OPENAI_API_KEY='your-key'`
- 如果 API Key 泄露，立即撤销并重新生成

### 📊 API 速率限制
- 脚本在批量生成时会自动延迟 3 秒（仅使用 AI 时）
- 如果遇到速率限制，可以分批次生成

### 🔍 ISO 周编号说明
- ISO 8601 标准：周一是一周的开始
- 2025年第1周: 2024-12-30（周一）到 2025-01-05（周日）
  - 因为这一周有超过4天在2025年，所以属于2025年第1周
- 这意味着第1周可能包含去年12月的日期

### 💾 Git 仓库要求
- 邮件存储在 Git 仓库中，每个 commit 对应一封邮件
- 邮件内容在文件 `m` 中
- 使用 `git log --all --since --until` 获取邮件

## 故障排除

### 问题：找不到 git/0.git 目录
```
fatal: not a git repository
```
**解决**: 
- 确保当前目录下有 `git/0.git` 目录
- 或使用 `--git-dir` 参数指定正确路径

### 问题：Python 版本过低
```
AttributeError: module 'datetime' has no attribute 'fromisocalendar'
```
**解决**: 升级到 Python 3.7 或更高版本

### 问题：AI 总结失败
```
[AI 总结失败: ...]
```
**解决**:
1. 检查 API Key 是否正确: `echo $OPENAI_API_KEY`
2. 检查网络连接
3. 查看具体错误信息
4. 检查 API 配额是否用完

### 问题：邮件数量为 0
```
ℹ️  该周没有邮件，跳过
```
这是正常的，该周确实没有邮件活动（可能是假期或周末）。

## 项目结构

```
kvmarm/
├── analyze_with_ai_summary.py  # 主脚本
├── README.md                   # 本文档
├── git/
│   └── 0.git/                  # 邮件列表 Git 仓库
└── docs/                       # 生成的报告输出目录
    ├── kvmarm_2025_week01.html
    ├── kvmarm_2025_week01.md
    └── archive.html
```

## 高级用法

### 自定义输出目录
脚本默认输出到 `docs/` 目录，可以修改脚本中的 `output_dir` 变量。

### 调整 AI 总结长度
修改 `OpenAISummarizer` 或 `AnthropicSummarizer` 中的 `max_tokens` 参数。

### 修改总结语言
修改 prompt 中的语言要求（当前为中文）。

## 许可证

MIT License
