#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横纵分析法报告 Markdown → HTML 转换脚本
生成排版精美的HTML文件，可在浏览器中直接打印为PDF。

用法: python md_to_html.py input.md output.html [--title "报告标题"] [--author "作者"]
依赖: pip install markdown
"""

import sys
import os
import re
import argparse
import markdown

# ────────────────────────────────────────
# CSS 样式
# ────────────────────────────────────────

CSS = """
/* ── 基础变量 ── */
:root {
    --color-primary: #1a365d;
    --color-secondary: #2d6a4f;
    --color-accent: #2563eb;
    --color-accent-light: #3b82f6;
    --color-text: #1e293b;
    --color-text-secondary: #64748b;
    --color-border: #e2e8f0;
    --color-bg-subtle: #f8fafc;
    --color-bg-quote: #f0f9ff;
    --color-bg-table-header: #1e293b;
    --font-sans: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
    --font-serif: "Noto Serif SC", "Source Han Serif SC", "SimSun", Georgia, serif;
    --font-mono: "JetBrains Mono", "Fira Code", "Consolas", monospace;
}

/* ── 全局 ── */
*, *::before, *::after { box-sizing: border-box; }

html {
    font-size: 15px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

body {
    font-family: var(--font-sans);
    color: var(--color-text);
    line-height: 1.8;
    max-width: 780px;
    margin: 0 auto;
    padding: 0 24px;
    background: #fff;
}

/* ── 封面 ── */
.cover {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 60px 40px;
    page-break-after: always;
}

.cover-title {
    font-family: var(--font-serif);
    font-size: 2.6rem;
    font-weight: 700;
    color: var(--color-primary);
    letter-spacing: 0.02em;
    line-height: 1.3;
    margin-bottom: 16px;
}

.cover-subtitle {
    font-size: 1.1rem;
    color: var(--color-text-secondary);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 32px;
}

.cover-divider {
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, var(--color-primary), var(--color-secondary));
    border: none;
    margin: 0 auto 32px;
    border-radius: 2px;
}

.cover-meta {
    font-size: 0.9rem;
    color: var(--color-text-secondary);
    line-height: 2;
}

.cover-meta .author {
    font-size: 1rem;
    color: var(--color-text);
    font-weight: 500;
}

/* ── 目录 ── */
.toc {
    page-break-after: always;
    padding: 60px 0 40px;
}

.toc-title {
    font-family: var(--font-serif);
    font-size: 1.6rem;
    color: var(--color-primary);
    margin-bottom: 32px;
    padding-bottom: 12px;
    border-bottom: 2px solid var(--color-primary);
}

.toc-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.toc-list li {
    margin: 0;
    padding: 0;
}

.toc-list a {
    display: flex;
    align-items: baseline;
    padding: 8px 0;
    color: var(--color-text);
    text-decoration: none;
    border-bottom: 1px solid var(--color-border);
    transition: color 0.15s;
}

.toc-list a:hover {
    color: var(--color-accent);
}

.toc-h2 a {
    font-weight: 600;
    font-size: 1.05rem;
}

.toc-h3 a {
    padding-left: 24px;
    font-size: 0.95rem;
    color: var(--color-text-secondary);
}

.toc-h3 a:hover {
    color: var(--color-accent);
}

/* ── 标题 ── */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-serif);
    line-height: 1.35;
    margin-top: 0;
}

h1 {
    font-size: 1.85rem;
    color: var(--color-primary);
    margin-top: 64px;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid var(--color-primary);
    page-break-before: always;
}

h2 {
    font-size: 1.4rem;
    color: var(--color-secondary);
    margin-top: 48px;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid #d1fae5;
}

h3 {
    font-size: 1.15rem;
    color: var(--color-accent);
    margin-top: 32px;
    margin-bottom: 12px;
}

h4 {
    font-size: 1.02rem;
    color: #6d28d9;
    margin-top: 24px;
    margin-bottom: 8px;
}

/* 正文中第一个h1不分页 */
.content > h1:first-child,
.content > h2:first-child {
    page-break-before: auto;
    margin-top: 40px;
}

/* ── 段落 ── */
p {
    margin: 0 0 16px;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

/* ── 粗体 ── */
strong {
    font-weight: 600;
    color: #0f172a;
}

/* ── 引用块 ── */
blockquote {
    margin: 24px 0;
    padding: 16px 20px 16px 24px;
    background: var(--color-bg-quote);
    border-left: 4px solid var(--color-accent);
    border-radius: 0 8px 8px 0;
    color: var(--color-text-secondary);
    font-size: 0.95rem;
    line-height: 1.7;
}

blockquote p {
    margin: 0 0 8px;
}

blockquote p:last-child {
    margin-bottom: 0;
}

/* ── 表格 ── */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 24px 0;
    font-size: 0.9rem;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

thead th {
    background: var(--color-bg-table-header);
    color: #f8fafc;
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
    font-size: 0.85rem;
    letter-spacing: 0.03em;
}

tbody td {
    padding: 10px 16px;
    border-bottom: 1px solid var(--color-border);
    vertical-align: top;
}

tbody tr:nth-child(even) {
    background: var(--color-bg-subtle);
}

tbody tr:last-child td {
    border-bottom: none;
}

/* ── 列表 ── */
ul, ol {
    margin: 12px 0 20px;
    padding-left: 28px;
}

li {
    margin-bottom: 6px;
    line-height: 1.7;
}

li > ul, li > ol {
    margin-top: 4px;
    margin-bottom: 4px;
}

/* ── 行内代码 ── */
code {
    font-family: var(--font-mono);
    background: #fef3c7;
    color: #92400e;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.88em;
}

/* ── 代码块 ── */
pre {
    background: #1e293b;
    color: #e2e8f0;
    padding: 20px 24px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 0.85rem;
    line-height: 1.6;
    margin: 20px 0;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
    border-radius: 0;
    font-size: inherit;
}

/* ── 分隔线 ── */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--color-border), transparent);
    margin: 40px 0;
}

/* ── 链接 ── */
a {
    color: var(--color-accent);
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.15s;
}

a:hover {
    border-bottom-color: var(--color-accent-light);
}

/* ── 来源列表 ── */
.sources h2,
.sources h1 {
    page-break-before: auto;
}

.sources ul {
    columns: 1;
    padding-left: 0;
    list-style: none;
}

.sources li {
    font-size: 0.85rem;
    line-height: 1.6;
    padding: 4px 0;
    border-bottom: 1px solid var(--color-border);
    word-break: break-all;
}

.sources li::before {
    content: "→ ";
    color: var(--color-accent);
    font-weight: 600;
}

/* ── 方法论说明 ── */
.methodology {
    margin-top: 40px;
    padding: 20px 24px;
    background: var(--color-bg-subtle);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    font-size: 0.88rem;
    color: var(--color-text-secondary);
}

/* ── 页眉页脚（打印） ── */
@media print {
    html { font-size: 11pt; }

    body {
        max-width: none;
        padding: 0;
    }

    .cover {
        min-height: auto;
        padding: 180px 40px 60px;
    }

    h1 { page-break-before: always; }
    .content > h1:first-child { page-break-before: auto; }
    h2, h3, h4 { page-break-after: avoid; }
    p { orphans: 3; widows: 3; }
    table { page-break-inside: avoid; }
    blockquote { page-break-inside: avoid; }

    a { color: var(--color-text) !important; border-bottom: none !important; }
    .sources a { color: var(--color-accent) !important; }

    @page {
        size: A4;
        margin: 22mm 18mm 20mm 18mm;

        @bottom-center {
            content: counter(page);
            font-family: var(--font-sans);
            font-size: 9pt;
            color: #94a3b8;
        }
    }

    @page :first {
        @bottom-center { content: none; }
    }
}

/* ── 响应式（屏幕阅读） ── */
@media screen and (max-width: 600px) {
    html { font-size: 14px; }
    body { padding: 0 16px; }
    .cover { padding: 40px 20px; }
    .cover-title { font-size: 2rem; }
    table { font-size: 0.82rem; }
    thead th, tbody td { padding: 8px 10px; }
}
"""


def slugify(text):
    """生成URL友好的ID"""
    text = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', text)
    text = re.sub(r'\s+', '-', text.strip())
    return text.lower()


def extract_headings(html_body):
    """从HTML中提取h1/h2/h3标题用于目录生成"""
    headings = []
    pattern = re.compile(r'<(h[123])\b[^>]*>(.*?)</\1>', re.DOTALL)
    for match in pattern.finditer(html_body):
        level = match.group(1)
        text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        slug = slugify(text)
        headings.append((level, text, slug))
    return headings


def add_heading_ids(html_body):
    """给h1/h2/h3添加id属性"""
    def replacer(match):
        tag = match.group(1)
        attrs = match.group(2) or ''
        content = match.group(3)
        text = re.sub(r'<[^>]+>', '', content).strip()
        slug = slugify(text)
        return f'<{tag}{attrs} id="{slug}">{content}</{tag}>'

    return re.sub(
        r'<(h[1234])(\s[^>]*)?>(.*?)</\1>',
        replacer,
        html_body,
        flags=re.DOTALL
    )


def build_toc_html(headings):
    """构建目录HTML"""
    if not headings:
        return ''

    items = []
    for level, text, slug in headings:
        css_class = f'toc-{level}'
        items.append(f'<li class="{css_class}"><a href="#{slug}">{text}</a></li>')

    return f'''
    <nav class="toc">
        <h2 class="toc-title">目录</h2>
        <ul class="toc-list">
            {"".join(items)}
        </ul>
    </nav>
    '''


def detect_sources_section(html_body):
    """检测并标记来源/参考文献部分"""
    # 找到「信息来源」或「参考文献」标题，给后续内容加class
    patterns = [
        r'(<h[12][^>]*>.*?(?:信息来源|参考文献|来源|Sources|References).*?</h[12]>)',
    ]
    for pattern in patterns:
        match = re.search(pattern, html_body, re.IGNORECASE | re.DOTALL)
        if match:
            pos = match.start()
            html_body = html_body[:pos] + '<div class="sources">' + html_body[pos:]
            # Find the next h1/h2 or end of content to close the div
            remaining = html_body[pos + len('<div class="sources">') + len(match.group(0)):]
            next_h = re.search(r'<h[12]\b', remaining)
            if next_h:
                insert_pos = pos + len('<div class="sources">') + len(match.group(0)) + next_h.start()
                html_body = html_body[:insert_pos] + '</div>' + html_body[insert_pos:]
            else:
                html_body += '</div>'
            break
    return html_body


def detect_methodology(html_body):
    """检测并标记方法论说明"""
    match = re.search(
        r'(<blockquote>\s*<p>\s*\*\*方法论说明\*\*.*?</blockquote>)',
        html_body, re.DOTALL
    )
    if not match:
        match = re.search(
            r'(<blockquote>\s*<p>.*?方法论说明.*?</blockquote>)',
            html_body, re.DOTALL
        )
    if match:
        html_body = html_body.replace(
            match.group(0),
            f'<div class="methodology">{match.group(0)}</div>'
        )
    return html_body


def md_to_html(md_text, title=None, author=None):
    """将Markdown转为排版精美的HTML"""

    # 提取第一个h1作为封面标题
    cover_title = title or "横纵分析报告"
    h1_match = re.match(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if h1_match:
        cover_title = h1_match.group(1).strip()
        md_text = md_text[:h1_match.start()] + md_text[h1_match.end():]

    # 提取元信息行
    meta_line = ""
    meta_match = re.search(r'^>\s*(研究时间.*|.*所属领域.*)$', md_text, re.MULTILINE)
    if meta_match:
        meta_line = meta_match.group(1).strip()
        md_text = md_text[:meta_match.start()] + md_text[meta_match.end():]

    # Markdown → HTML
    extensions = ['tables', 'fenced_code', 'toc', 'smarty']
    html_body = markdown.markdown(md_text, extensions=extensions, output_format='html5')

    # 添加标题ID
    html_body = add_heading_ids(html_body)

    # 提取目录
    headings = extract_headings(html_body)

    # 标记特殊部分
    html_body = detect_sources_section(html_body)
    html_body = detect_methodology(html_body)

    # 构建目录
    toc_html = build_toc_html(headings)

    # 构建封面
    meta_parts = []
    if meta_line:
        for part in re.split(r'\s*\|\s*', meta_line):
            meta_parts.append(f'<div>{part.strip()}</div>')

    cover_html = f'''
    <div class="cover">
        <div class="cover-title">{cover_title}</div>
        <div class="cover-subtitle">横纵分析法深度研究报告</div>
        <hr class="cover-divider">
        <div class="cover-meta">
            <div class="author">{author}</div>
            {"".join(meta_parts)}
        </div>
    </div>
    '''

    # 组装完整HTML
    full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cover_title} — 横纵分析法深度研究报告</title>
    <style>{CSS}</style>
</head>
<body>
{cover_html}
{toc_html}
<div class="content">
{html_body}
</div>
</body>
</html>'''

    return full_html


def main():
    parser = argparse.ArgumentParser(description="横纵分析法报告 Markdown → HTML")
    parser.add_argument("input", help="输入的 Markdown 文件路径")
    parser.add_argument("output", help="输出的 HTML 文件路径")
    parser.add_argument("--title", default=None, help="报告标题（默认从Markdown第一个H1提取）")
    parser.add_argument("--author", default=None, help="作者名")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = md_to_html(md_text, title=args.title, author=args.author)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = os.path.getsize(args.output) / 1024
    print(f"[OK] HTML 已生成: {args.output} ({size_kb:.1f} KB)")
    print(f"[提示] 在浏览器中打开此文件，按 Ctrl+P 即可打印为排版精美的 PDF")


if __name__ == "__main__":
    main()
