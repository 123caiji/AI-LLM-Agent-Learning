# -*- coding: utf-8 -*-
"""为《13-自托管个人Agent》生成配图(2 张 PNG):能力雷达 + 社区热度。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.executable).parent.parent.parent))
from daimon_runtime import setup_plot

import matplotlib.pyplot as plt
import numpy as np

setup_plot()

OUT = Path("assets/agent-compare")
OUT.mkdir(parents=True, exist_ok=True)

# ---------- 图 4:OpenClaw vs Hermes Agent 能力雷达 ----------
dims = ["上手容易度", "自进化与记忆", "安全默认值", "生态与渠道", "可定制/白盒", "轻量与成本"]
scores = {
    "OpenClaw(小龙虾)":    [3, 2, 2, 5, 5, 4],
    "Hermes Agent(爱马仕)": [4, 5, 4, 4, 4, 5],
}
colors = {"OpenClaw(小龙虾)": "#cf222e", "Hermes Agent(爱马仕)": "#d97706"}
angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
angles += angles[:1]
fig, ax = plt.subplots(figsize=(8.4, 7.0), subplot_kw=dict(polar=True))
for name, s in scores.items():
    vals = s + s[:1]
    ax.plot(angles, vals, color=colors[name], linewidth=2.2, label=name)
    ax.fill(angles, vals, color=colors[name], alpha=0.08)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(dims, fontsize=11)
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
ax.set_title("OpenClaw vs Hermes Agent 能力画像(编辑评分,5 分制,2026-07)", fontsize=13.5, pad=22)
ax.legend(loc="upper right", bbox_to_anchor=(1.38, 1.12), fontsize=10)
fig.tight_layout()
fig.savefig(OUT / "chart4-selfhosted-radar.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ---------- 图 5:GitHub Star 社区热度(报道口径) ----------
fig, ax = plt.subplots(figsize=(9.6, 4.6))
rows = [
    ("OpenClaw(小龙虾)", 280, "约 28 万(2026-03 报道)", "#cf222e"),
    ("Hermes Agent(爱马仕)", 66, "6.6 万+(2026-04 报道,上线约 2 个月)", "#d97706"),
]
y = np.arange(len(rows))[::-1]
vals = [r[1] for r in rows]
bars = ax.barh(y, vals, color=[r[3] for r in rows], alpha=0.88, height=0.5)
for yi, v, r in zip(y, vals, rows):
    ax.text(v + 4, yi, r[2], va="center", fontsize=10.5)
ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in rows], fontsize=11)
ax.set_xlim(0, 340)
ax.set_xlabel("GitHub Stars(千)", fontsize=11.5)
ax.set_title("自托管个人 Agent 社区热度(GitHub Stars,报道口径)", fontsize=13.5, pad=12)
ax.grid(axis="x", alpha=0.25)
fig.text(0.02, 0.02, "注:数字来自 2026 年上半年公开报道,时点与口径各异,精确数字以 GitHub 实时为准;两者均为 MIT 开源。",
         fontsize=8.5, color="#57606a")
fig.tight_layout(rect=(0, 0.08, 1, 1))
fig.savefig(OUT / "chart5-selfhosted-stars.png", dpi=200, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(OUT.glob('chart[45]*.png'))])
