# 横纵分析法 (Horizontal-Vertical Analysis)

Claude Code 深度研究 Skill，由**数字生命卡兹克（Khazix）**提出。

融合索绪尔的历时-共时分析、社会科学纵向-横截面研究设计、商学院案例研究法与竞争战略分析的核心思想，形成一套适用于产品/公司/概念/技术/人物的通用深度研究框架。

## 核心理念

- **纵轴**：追踪研究对象从诞生到当下的完整生命历程，以叙事故事呈现
- **横轴**：在当下时间截面上与竞品/同类进行系统性横向对比
- **交叉洞察**：两条轴交汇产出独到判断

最终产出一份排版精美的 HTML 研究报告（可通过浏览器打印为 PDF）。

## 文件结构

```
├── SKILL.md                 # 主Skill定义文件（方法论 + 工作流）
├── references/
│   └── schema.json          # 分析框架JSON Schema
└── scripts/
    └── md_to_html.py        # Markdown → HTML 转换脚本
```

## 安装到 Claude Code

将本仓库克隆到 Claude Code 的 skills 目录：

```bash
git clone https://github.com/daizhouchen/hv-analysis.git ~/.claude/skills/hv-analysis
```

安装 Python 依赖（用于 HTML 报告生成）：

```bash
pip install markdown
```

## 使用方式

在 Claude Code 中对话时，使用以下触发词即可启动：

- "帮我用横纵分析法研究 XX"
- "帮我深度研究一下 XX"
- "XX 是怎么回事，帮我调研一下"
- "帮我做个竞品分析"

## 许可

MIT License
