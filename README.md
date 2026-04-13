# 横纵分析法 v3.0 (Horizontal-Vertical Analysis)

Claude Code 深度研究 Skill。

在原有横纵双轴分析的基础上，引入**四层深度模型**和**双横切透镜**，形成一套从表层事件到深层结构的穿透式研究框架。

## 方法论架构

### 四层深度模型（由浅入深）

1. **事件层**：发生了什么，谁在场 — 纵轴故事 + 横轴对比
2. **机制层**：怎么运转的 — 反馈飞轮、因果传动装置、延迟效应
3. **结构层**：为什么必须是这样 — 第一性原理、不可压缩约束、必然 vs 偶然
4. **范式层**：放到最大画布上看 — 技术革命周期、产业生命周期、文明趋势

### 双横切透镜（贯穿所有层）

- **反身性分析**：主流叙事如何自我实现又自我瓦解（Soros）
- **跨域同构**：其他领域已走完的历史如何照亮当前领域的未来

### 理论融合

索绪尔历时-共时分析 / 社会科学纵向-横截面研究设计 / 商学院案例研究法 / Porter 五力 / Hamilton Helmer 7 Powers / Christensen Jobs-to-be-Done / Carlota Perez 技术革命周期 / Soros 反身性理论 / Braudel 多尺度历史分析 / Andy Grove 战略拐点

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
- "帮我做个 deep research"

## 产出

一份 15,000-40,000 字的排版精美 HTML 研究报告，可在浏览器中打印为 PDF。

## 许可

MIT License
