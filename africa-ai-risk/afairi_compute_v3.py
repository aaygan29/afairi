import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)

# ============================================================================
# AFAIRI v3 — fully mechanized, per-country-sourced component inputs.
# Every value below traces to a specific cited statistic verified during
# research for this paper (see paper Table 1 / Appendix A for full citations).
# No value is analyst-judgment-only; where a criterion could not be sourced
# per-country (biosecurity/DNA-screening compliance), it is DROPPED from the
# rubric rather than estimated, and this is disclosed as a limitation.
# ============================================================================

countries = ["Egypt", "South Africa", "Nigeria", "Kenya"]

# --- Exposure (E): World Bank IT.NET.USER.ZS, 2023 (verified, §3) ---------
E = {"Egypt": 74.0, "South Africa": 78.3, "Nigeria": 40.1, "Kenya": 32.1}

# --- Susceptibility (S): % adults using digital/mobile financial services,
# each from a distinct but directly-cited national source (methodologies
# differ slightly across sources — disclosed, not a single harmonized survey):
#   Egypt: 74.8% financial inclusion incl. mobile wallets, end-2024 (Central Bank of Egypt)
#   South Africa: 88% (100% - 12% financially excluded, FinScope/FinMark Trust 2023)
#   Nigeria: 57% mobile-money-app adoption among adults, 2023 (EFInA Access to Finance)
#   Kenya: 82% digital financial services adoption, 2025 (Central Bank of Kenya, conservative
#          bound of the 82-92% CBK/Afrobarometer 2025 range)
S = {"Egypt": 74.8, "South Africa": 88.0, "Nigeria": 57.0, "Kenya": 82.0}

# --- Governance Deficit (G): mechanized 2-criterion rubric (criterion 3,
# biosecurity/DNA-synthesis screening compliance, DROPPED — no country-level
# public data exists per IBBIS 2025; see paper §4.4 and Appendix A).
#   Criterion A - National AI strategy status (0/25/50):
#     50 = published/launched national strategy; 25 = draft/unfinalized only
#   Criterion B - Cybercrime statute AI-specificity (0/12.5/25):
#     25 = statute w/ documented AI-specific legislative activity (e.g. active
#          amendment process explicitly targeting AI-driven threats);
#     12.5 = general cybercrime statute in force, no AI-specific provisions found
criterion_A = {
    "Egypt": 50,         # Egypt National AI Strategy, 2nd ed., launched 2025 (MCIT)
    "South Africa": 50,  # National AI Policy Framework, published Aug 2024
    "Nigeria": 25,       # National AI Strategy (NAIS), draft only, published Aug 2024, not finalized
    "Kenya": 50,         # Kenya National AI Strategy 2025-2030, launched Mar 2025
}
criterion_B = {
    "Egypt": 12.5,        # Law 175/2018 (cybercrime), no AI-specific provisions found
    "South Africa": 12.5, # Cybercrimes Act 19 of 2020, in force, no AI-specific provisions found
    "Nigeria": 25,        # Cybercrimes Act 2015 amended 2024 + active Senate push (2025) for
                           # AI-driven-threat-specific overhaul (documented, in progress)
    "Kenya": 12.5,         # Computer Misuse and Cybercrimes Act (2018) + Data Protection Act enforcement,
                           # no AI-specific provisions found
}
MAX_CAPACITY = 75.0  # 50 + 25
capacity = {c: (criterion_A[c] + criterion_B[c]) for c in countries}
capacity_rescaled = {c: capacity[c] / MAX_CAPACITY * 100 for c in countries}
G = {c: 100 - capacity_rescaled[c] for c in countries}

# --- Infrastructural Fragility (I): Our World in Data / Ember grid carbon
# intensity (gCO2/kWh, most recent year available), rescaled /10, PLUS a
# reliability penalty grounded in documented incident counts for the most
# recent complete reporting period (not a stale/prior-year snapshot):
#   Nigeria: 12 documented national grid collapses in 2024 (Guardian/Tribune/
#            Intelpoint reporting, TCN incident timeline) -> penalty = min(25, 12*2) = 24
#   South Africa: Eskom suspended load-shedding for 325 of ~330 days, Apr 2024-
#            Feb 2025 (Eskom official releases) -> CURRENT-period penalty = 0
#            (NOTE: this reverses this paper's own v2 draft, which incorrectly
#            applied a "Stage 1-6, 2023-2025" penalty using stale 2023 data;
#            multi-year volatility 2022-2023 Stage 6 shedding is disclosed as
#            a caveat, not scored, since AFAIRI is a current-snapshot index)
#   Egypt, Kenya: no comparable documented chronic grid-instability record
#            located during this research -> penalty = 0 (absence of evidence
#            disclosed explicitly, not treated as evidence of stability)
grid_intensity_gco2 = {"Egypt": 563.23, "South Africa": 872.62, "Nigeria": 650.69, "Kenya": 95.44}
grid_intensity_scaled = {c: v / 10.0 for c, v in grid_intensity_gco2.items()}
reliability_penalty = {"Egypt": 0.0, "South Africa": 0.0, "Nigeria": 24.0, "Kenya": 0.0}
I = {c: min(100.0, grid_intensity_scaled[c] + reliability_penalty[c]) for c in countries}

print("="*70)
print("AFAIRI v3 — mechanized, sourced component matrix (0-100)")
print("="*70)
print(f"{'Country':<15}{'E':>8}{'S':>8}{'G':>8}{'I':>8}")
for c in countries:
    print(f"{c:<15}{E[c]:>8.1f}{S[c]:>8.1f}{G[c]:>8.1f}{I[c]:>8.1f}")

LAMBDA = 0.15
N = 10000
results = {c: [] for c in countries}

for _ in range(N):
    w = np.random.dirichlet([1.0, 1.0, 1.0, 1.0])
    for c in countries:
        base = w[0]*E[c] + w[1]*S[c] + w[2]*G[c] + w[3]*I[c]
        compound = LAMBDA * (S[c] * I[c] / 100.0)
        results[c].append(base + compound)

arrs = {c: np.array(results[c]) for c in countries}
means = {c: arrs[c].mean() for c in countries}

print("\nMonte Carlo (N=10,000 Dirichlet(1,1,1,1) weight draws):")
for c in countries:
    print(f"  {c:<15} mean={arrs[c].mean():6.2f}  sd={arrs[c].std():5.2f}  "
          f"95% CI=[{np.percentile(arrs[c],2.5):6.2f}, {np.percentile(arrs[c],97.5):6.2f}]")

order_counts = {}
for i in range(N):
    ranking = tuple(sorted(countries, key=lambda c: -arrs[c][i]))
    order_counts[ranking] = order_counts.get(ranking, 0) + 1
sorted_orders = sorted(order_counts.items(), key=lambda x: -x[1])[:5]
print("\nTop 5 rank orderings by frequency:")
for order, count in sorted_orders:
    print(f"  {' > '.join(order):<60} {100*count/N:5.1f}%")

print("\nP(country ranked #1 = highest AFAIRI):")
for c in countries:
    top = sum(1 for i in range(N) if arrs[c][i] == max(arrs[x][i] for x in countries))
    print(f"  {c:<15} {100*top/N:5.1f}%")

# --- second-layer robustness: perturb the INPUT VALUES themselves (not just
# weights) by +/-10% uniform jitter, re-run, check if P(#1) is stable. This
# directly answers the Council's Gate 4 finding (input-value uncertainty was
# previously unaddressed).
print("\n" + "="*70)
print("Second-layer robustness: +/-10% input-value jitter x weight draws")
print("="*70)
jitter_results = {c: [] for c in countries}
for _ in range(N):
    w = np.random.dirichlet([1.0, 1.0, 1.0, 1.0])
    jitter = {c: 1.0 + np.random.uniform(-0.10, 0.10) for c in countries}
    for c in countries:
        Ej, Sj, Gj, Ij = E[c]*jitter[c], S[c]*jitter[c], G[c]*jitter[c], I[c]*jitter[c]
        Ej, Sj, Gj, Ij = min(100,Ej), min(100,Sj), min(100,Gj), min(100,Ij)
        base = w[0]*Ej + w[1]*Sj + w[2]*Gj + w[3]*Ij
        compound = LAMBDA * (Sj * Ij / 100.0)
        jitter_results[c].append(base + compound)
jarrs = {c: np.array(jitter_results[c]) for c in countries}
for c in countries:
    top = sum(1 for i in range(N) if jarrs[c][i] == max(jarrs[x][i] for x in countries))
    print(f"  {c:<15} P(#1) with input jitter = {100*top/N:5.1f}%  (mean={jarrs[c].mean():6.2f})")

# --- figure ---
fig, ax = plt.subplots(figsize=(7.5,4.2))
order = sorted(countries, key=lambda c: -means[c])
sds = {c: arrs[c].std() for c in countries}
ax.barh(order, [means[c] for c in order], xerr=[sds[c] for c in order], color='#3b6ea5', capsize=4)
ax.set_xlabel('AFAIRI v3 composite score (0-100)')
ax.set_title('AFAIRI v3: mechanized-input Monte Carlo sensitivity\n(N=10,000 Dirichlet weight draws; mean ± 1 SD)')
plt.tight_layout()
plt.savefig('afairi_v3_montecarlo.png', dpi=150)
print("\nchart saved: afairi_v3_montecarlo.png")
