"""Figures for AFAIRI index v4 (manuscript AFAIRI_v6_revised_manuscript.txt).

Reads inputs and simulation directly from afairi_compute_v4.py so figures
cannot drift from the reported numbers. Seed 42 (via that module).
  afairi_v4_components_by_region.png  - Table 1 component matrix
  afairi_v4_sensitivity.png           - Table 2: score ranges + share ranked first
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import afairi_compute_v4 as v4

COLORS = {"Egypt": "#2a78d6", "Nigeria": "#eb6834", "Kenya": "#1baf7a", "South Africa": "#eda100"}
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3dd"
plt.rcParams.update({"font.size": 10, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False,
                     "axes.spines.right": False})
LABEL = {"Egypt": "Egypt (North)", "Nigeria": "Nigeria (West)", "Kenya": "Kenya (East)",
         "South Africa": "South Africa (Southern)"}

M = v4.matrix()
comps = ["Exposure (E)", "Scam victimization (H)", "Governance deficit (G)", "Infrastructure disruption (I)"]

# ---- Figure 1: components ---------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.6))
x = np.arange(4); bw = 0.19
for k, c in enumerate(v4.R):
    xs = x + (k - 1.5) * (bw + 0.01)
    ax.bar(xs, M[k], bw, color=COLORS[c], label=LABEL[c], zorder=3)
    for xi, val in zip(xs, M[k]):
        ax.text(xi, val + 1.2, (f"{val:.0f}" if float(val).is_integer() else f"{val:.1f}"), ha="center", va="bottom", fontsize=7.5, color=INK)
ax.set_xticks(x, comps)
ax.set_ylim(0, 100); ax.set_ylabel("Component score (0-100)")
ax.yaxis.grid(True, color=GRID, zorder=0)
ax.set_title("AFAIRI v4 component scores by anchor state", loc="left", color=INK, fontsize=12)
ax.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.1))
fig.text(0.01, 0.005, "Sources: World Bank WDI 2023 (E); GASA State of Scams in Africa 2025 (H); "
         "rubric in Section 6.3 (G, I).", fontsize=7.5, color=MUTED)
plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("afairi_v4_components_by_region.png", dpi=200)
plt.close()

# ---- Figure 2: sensitivity (two panels, no dual axis) -----------------------
S = v4.simulate(M)                       # N=10,000 Dirichlet(1,1,1,1), weights only
order = np.argsort(-S.mean(0))
top = np.bincount(S.argmax(1), minlength=4) / len(S)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1.4, 1]})
for row, i in enumerate(order):
    c = v4.R[i]; y = len(order) - 1 - row
    lo, q1, med, q3, hi = np.percentile(S[:, i], [2.5, 25, 50, 75, 97.5])
    a1.plot([lo, hi], [y, y], color=COLORS[c], lw=2, zorder=2)
    a1.plot([q1, q3], [y, y], color=COLORS[c], lw=7, solid_capstyle="round", zorder=3)
    a1.scatter([S[:, i].mean()], [y], s=60, color="white", edgecolor=INK, zorder=4)
    a1.text(hi + 1, y, f"mean {S[:, i].mean():.1f}", va="center", fontsize=8, color=INK)
    a2.barh(y, 100 * top[i], color=COLORS[c], height=0.55, zorder=3)
    a2.text(100 * top[i] + 1, y, f"{100 * top[i]:.1f}%", va="center", fontsize=9, color=INK)
labels = [LABEL[v4.R[i]] for i in order][::-1]
a1.set_yticks(range(4), labels); a2.set_yticks(range(4), [])
a1.set_xlim(20, 90); a1.set_ylim(-0.5, 3.5); a2.set_ylim(-0.5, 3.5); a1.set_xlabel("AFAIRI score across sampled weightings")
a1.xaxis.grid(True, color=GRID, zorder=0)
a1.set_title("Score range: thin 2.5-97.5th pct, thick 25-75th, dot = mean", loc="left", fontsize=9.5, color=INK)
a2.set_xlim(0, 60); a2.set_xlabel("Share of weightings ranked first (%)")
a2.xaxis.grid(True, color=GRID, zorder=0)
a2.set_title("Share ranked first (not a probability)", loc="left", fontsize=9.5, color=INK)
fig.suptitle("AFAIRI v4 weight sensitivity: no robust top-ranked state (N=10,000 Dirichlet(1,1,1,1) draws, seed 42)",
             x=0.01, ha="left", fontsize=11, color=INK)
plt.tight_layout()
plt.savefig("afairi_v4_sensitivity.png", dpi=200)
plt.close()
print("mean:", dict(zip(v4.R, S.mean(0).round(2))), "share#1:", dict(zip(v4.R, (100 * top).round(1))))
