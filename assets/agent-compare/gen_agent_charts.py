# -*- coding: utf-8 -*-
"""为《12-主流Agent对比分析》生成配图(3 张 PNG)。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.executable).parent.parent.parent))
from daimon_runtime import setup_plot

import matplotlib.pyplot as plt
import numpy as np

setup_plot()

OUT = Path("assets/agent-compare")
OUT.mkdir(parents=True, exist_ok=True)

# ---------- 图 1:编程 Agent 定位图(自主性 × 入门成本) ----------
agents = [
    # (名称, 自主性, 入门价, 颜色, 备注, 文字偏移 dx, dy)
    ("GitHub Copilot", 5.0, 0, "#2da44e", "Free 档可用", 0.1, 2.6),
    ("Gemini CLI", 6.8, 0, "#f9ab00", "开源免费", -0.15, -5.0),
    ("Google Jules", 7.3, 0, "#1a73e8", "Free 15 任务/天", 0.12, 2.6),
    ("OpenCode", 7.9, 0, "#6e7781", "开源免费", 0.12, -5.0),
    ("Cursor", 6.2, 20, "#8250df", "$20 Pro", 0.0, 3.0),
    ("OpenAI Codex", 8.3, 20, "#10a37f", "随 ChatGPT Plus $20", -0.35, 4.6),
    ("Claude Code", 8.8, 20, "#d97706", "$20 Pro / $200 Max", -0.1, 7.6),
    ("Devin", 9.4, 20, "#cf222e", "$20 + $2.25/ACU", -0.35, -6.4),
]
fig, ax = plt.subplots(figsize=(10, 6.2))
for name, auto, price, color, note, dx, dy in agents:
    ax.scatter(auto, price, s=340, c=color, alpha=0.85, edgecolors="white", linewidths=1.5, zorder=3)
    ax.annotate(f"{name}\n{note}".replace("$", "\\$"), (auto, price), xytext=(auto + dx, price + dy),
                fontsize=9, ha="center", va="center", zorder=4,
                arrowprops=dict(arrowstyle="-", color="#8c959f", lw=0.8, shrinkA=0, shrinkB=8))
ax.set_xlabel("自主性(编辑辅助 ←→ 完全委托)", fontsize=12)
ax.set_ylabel("入门价格(美元/月)", fontsize=12)
ax.set_title("主流编程 Agent 定位图:自主性 × 入门成本(2026-07)", fontsize=14, pad=14)
ax.set_xlim(4, 10.6)
ax.set_ylim(-9, 34)
ax.axvspan(8, 10.6, color="#fff7ed", zorder=0)
ax.text(9.3, 31.5, "高自主区:可委派完整任务", fontsize=9, color="#9a3412", ha="center")
ax.grid(alpha=0.25, zorder=1)
fig.tight_layout()
fig.savefig(OUT / "chart1-positioning.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ---------- 图 2:基准对比(SWE-bench Verified / Terminal-Bench 2.0) ----------
fig, ax = plt.subplots(figsize=(10, 5.2))
rows = [
    ("Claude Opus 4.7\n(Claude Code)", 87.6, "SWE-bench Verified", "#d97706"),
    ("gpt-5-codex\n(Codex)", 78.5, "SWE-bench Verified(报道区间 77~80)", "#10a37f"),
    ("gpt-5-codex\n(Codex)", 77.3, "Terminal-Bench 2.0", "#0e7490"),
]
y = np.arange(len(rows))[::-1]
vals = [r[1] for r in rows]
labels = [f"{r[2]}  {r[1]}%" for r in rows]
colors = [r[3] for r in rows]
bars = ax.barh(y, vals, color=colors, alpha=0.88, height=0.55)
for yi, v, lab in zip(y, vals, labels):
    ax.text(v + 1.0, yi, lab, va="center", fontsize=10)
ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in rows], fontsize=10)
ax.set_xlim(0, 108)
ax.set_xlabel("得分(%)", fontsize=12)
ax.set_title("编程 Agent 底层模型基准对比(2026-07 公开报道口径)", fontsize=14, pad=14)
ax.grid(axis="x", alpha=0.25)
fig.text(0.02, 0.015, "注:基准衡量的是底层模型能力,真实任务成功率还取决于 Agent 框架(harness)、沙箱与提示设计;\nDevin/Jules/Copilot 等未公开统一口径成绩。数据为 2026-07 公开报道口径。",
         fontsize=8.5, color="#57606a")
fig.tight_layout(rect=(0, 0.07, 1, 1))
fig.savefig(OUT / "chart2-benchmark.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ---------- 图 3:Agent 框架能力雷达图 ----------
dims = ["编排控制力", "上手速度", "多智能体", "持久化/长任务", "生态与集成", "类型安全"]
frameworks = {
    "LangGraph 1.0":        [5, 3, 4, 5, 5, 4],
    "CrewAI 1.14":          [3, 5, 5, 3, 4, 3],
    "OpenAI Agents SDK":    [3, 5, 4, 3, 4, 3],
    "Claude Agent SDK":     [4, 4, 4, 4, 4, 3],
    "MS Agent Framework":   [4, 3, 4, 4, 4, 5],
    "Pydantic AI V2":       [3, 4, 3, 4, 3, 5],
}
palette = ["#8250df", "#1a7f37", "#10a37f", "#d97706", "#0969da", "#cf222e"]
angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
angles += angles[:1]
fig, ax = plt.subplots(figsize=(8.6, 7.2), subplot_kw=dict(polar=True))
for (name, scores), color in zip(frameworks.items(), palette):
    s = scores + scores[:1]
    ax.plot(angles, s, color=color, linewidth=2, label=name)
    ax.fill(angles, s, color=color, alpha=0.06)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(dims, fontsize=11)
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
ax.set_title("Agent 框架能力画像(编辑评分,5 分制,2026-07)", fontsize=14, pad=22)
ax.legend(loc="upper right", bbox_to_anchor=(1.34, 1.12), fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "chart3-framework-radar.png", dpi=200, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(OUT.glob('*.png'))])
