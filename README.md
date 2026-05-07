<!-- daizhouchen-banner-begin -->
<p align="center">
  <img src="assets/hero.png" alt="prism-research" width="100%"/>
</p>

> **横纵分析法（Horizontal-Vertical Analysis）深度研究 · 索绪尔历时-共时 · 商学院案例 · 竞争战略。**
>
> *horizontal-vertical analysis · prism research methodology.*
<!-- daizhouchen-banner-end -->

# 棱镜研究 (Prism Research)

一个用于 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 的深度研究 Skill。当你想系统性地摸清一个产品、公司、概念、技术或人物时，它会引导 Claude 从多个层次进行穿透式研究，最终产出一份排版精美的 HTML 报告（可打印为 PDF）。

## 它做什么

以纵轴（时间深度）和横轴（竞争广度）为骨架，然后逐层深挖：

| 层次 | 回答的问题 | 主要工具 |
|------|-----------|---------|
| 事件层 | 发生了什么，谁在场 | 多尺度纵轴叙事 + 横轴竞品对比 |
| 机制层 | 怎么运转的 | 反馈飞轮、因果传动装置、延迟效应 |
| 结构层 | 为什么必须是这样 | 第一性原理、7 Powers、价值链、不可压缩约束 |
| 范式层 | 放到最大画布上看 | 技术革命周期（Perez）、产业生命周期、文明趋势 |

在所有层之上，叠加两个横切透镜：
- **反身性分析**：主流叙事如何自我实现又自我瓦解
- **跨域同构**：其他领域已走完的历史如何照亮当前领域的未来

最终报告 15,000-40,000 字，包含信号绑定的未来推演、时间尺度套利分析和一段「终极判断」。

## 安装

### 前提条件

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 已安装并可用
- Python 3.x（用于生成 HTML 报告）
- 能联网搜索（Skill 依赖 Claude Code 的 WebSearch/WebFetch 工具收集信息）

### 第一步：克隆到 skills 目录

**macOS / Linux：**

```bash
git clone https://github.com/daizhouchen/prism-research.git ~/.claude/skills/prism-research
```

**Windows：**

```bash
git clone https://github.com/daizhouchen/prism-research.git %USERPROFILE%\.claude\skills\prism-research
```

### 第二步：安装 Python 依赖

```bash
pip install markdown
```

这是 HTML 报告生成脚本的唯一依赖。

### 验证安装

安装完成后，启动 Claude Code，输入类似以下内容即可触发：

```
帮我深度研究一下 Cursor
```

如果 Claude 开始进行联网搜索和结构化分析，说明安装成功。

## 使用方式

在 Claude Code 中用自然语言触发即可，不需要记住特定命令。以下都会触发：

- "帮我研究一下 XX"
- "XX 是怎么回事，帮我深度分析一下"
- "帮我做个竞品分析"
- "帮我做个 deep research"
- "帮我摸清楚 XX 这个东西"

Skill 会自动启动多个子 Agent 并行收集信息，构建分析框架，然后按照方法论逐步撰写报告，最后转为 HTML 交付。

## 文件结构

```
prism-research/
├── SKILL.md                  # 核心：完整的方法论定义和工作流指令
├── references/
│   └── schema.json           # 分析框架的 JSON Schema（供参考）
└── scripts/
    └── md_to_html.py         # Markdown → HTML 转换脚本（含封面、目录、排版）
```

- **SKILL.md** 是 Claude Code 实际加载和执行的文件，包含所有方法论细节、子 Agent prompt 模板、写作风格指南和质检清单。
- **schema.json** 是分析框架的结构化描述，帮助 Claude 在构建分析骨架时参考。
- **md_to_html.py** 负责将最终的 Markdown 报告转为排版精美的 HTML，支持封面生成、自动目录、打印优化（A4 分页）。

## 方法论来源

这套方法论融合了多个学科和领域的核心思想：

- **索绪尔**的历时-共时分析（语言学）
- **Braudel** 的多尺度历史分析（事件/局势/结构三个时间尺度）
- 社会科学的纵向-横截面研究设计
- 商学院案例研究法
- **Porter** 五力分析
- **Hamilton Helmer** 的 7 Powers 竞争战略框架
- **Christensen** 的 Jobs-to-be-Done 需求理论
- **Carlota Perez** 的技术革命周期理论
- **George Soros** 的反身性理论
- **Andy Grove** 的战略拐点概念

## 自定义

SKILL.md 是纯文本，你可以根据自己的需求修改：

- 调整子 Agent 的搜索策略和 prompt 模板
- 增减分析维度（比如为特定行业添加专属分析角度）
- 修改写作风格指南
- 调整篇幅要求
- 修改 HTML 报告的 CSS 样式（在 `scripts/md_to_html.py` 中）

## 许可

MIT License

---
<!-- daizhouchen-footer-begin -->

Part of [**daizhouchen 实验集**](https://github.com/daizhouchen) → 一个 AI 应用创造者的实验现场。
<!-- daizhouchen-footer-end -->
