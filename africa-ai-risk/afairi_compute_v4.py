"""AFAIRI v4: construct-revised index (responds to external review, Sept 2026).

Changes from v3 (see manuscript Section 6 and Appendix A items 13-20):
  * Susceptibility (financial inclusion) REPLACED by H, reported scam
    victimization: % of adults with a scam experience in the past 12 months,
    GASA State of Scams in Africa 2025 (one harmonized 4-country survey).
  * Infrastructural Fragility (grid carbon intensity) REPLACED by I,
    infrastructure disruption: 2024 grid-disruption tier + 2024 subsea-cable
    outage events with documented national connectivity impact.
  * Governance Deficit adds Criterion C, enforcement capacity (data protection
    authority monetary penalties), and halves the weight of strategy existence.
  * The S x I coupling term is dropped from the main specification (no
    mechanism links fraud harm to outages); lambda=0.15 kept only as a
    sensitivity run.
  * Input jitter is now INDEPENDENT per component (v3 applied one factor per
    country to all four components, contrary to the v3 text).

Outputs are shares of the sampled weight space, not probabilities that a
region "is" riskiest. Seed 42.
"""
import itertools
import numpy as np

rng = np.random.default_rng(42)
R = ["Egypt", "Nigeria", "Kenya", "South Africa"]

# ---- E: World Bank IT.NET.USER.ZS, 2023 (API-verified) ----------------------
E = {"Egypt": 74.0, "Nigeria": 40.1, "Kenya": 32.1, "South Africa": 78.3}

# ---- H: reported scam victimization, past 12 months ------------------------
# GASA "State of Scams in Africa 2025" (Global Anti-Scam Alliance, launched
# March 2026): one harmonized survey, 4,000 adults 18+ across exactly these
# four countries. % of adults reporting a scam experience in the last 12 months.
# (Corroborated across GASA summary page ranking + CfMA + Africa.com coverage.)
# National loss statistics (NIBSS/CBK/SABRIC) are NOT used as index inputs:
# Egypt publishes none and the three scopes differ; kept as a cross-check only.
H = {"Egypt": 39.0, "Nigeria": 73.0, "Kenya": 83.0, "South Africa": 77.0}

# ---- G: Governance deficit = 100 - (A + B + C) ------------------------------
# A strategy status (25 launched / 12.5 draft / 0 none)
# B cybercrime statute AI-specificity (25 dated AI-specific legislative
#   process / 12.5 general statute only / 0 none)
# C enforcement capacity (50 DPA has issued a single monetary penalty
#   >= USD 1M / 25 penalties issued, all < USD 1M / 0 no penalty issued)
A = {"Egypt": 25, "Nigeria": 12.5, "Kenya": 25, "South Africa": 25}
B = {"Egypt": 12.5, "Nigeria": 25, "Kenya": 12.5, "South Africa": 12.5}
C = {"Egypt": 0,          # PDPL 151/2020 exec. regs Nov 2025; enforcement from Oct 2026; no fine
     "Nigeria": 50,       # NDPC: Meta USD 32.8M (Feb 2025), Fidelity NGN 555.8M, MultiChoice NGN 766M
     "Kenya": 25,         # ODPC: >= KES 26.3M cumulative across >= 9 entities by Sept 2024
     "South Africa": 25}  # Information Regulator: ZAR 5M, DoJ&CD, July 2023
G = {c: 100 - (A[c] + B[c] + C[c]) for c in R}

# ---- I: infrastructure disruption, calendar 2024 ----------------------------
# grid tier: 50 = >= 6 national grid collapses OR national rolling load-shedding
#            in force >= 90 days; 25 = 1-5 nationwide blackout events or
#            load-shedding < 90 days; 0 = none located
grid = {"Nigeria": 50,       # 12 national grid collapses (TCN timeline, Guardian NG)
        "Egypt": 50,         # national load-shedding 1 Jan - 21 Jul 2024 (~202 days)
        "Kenya": 25,         # nationwide/near-nationwide blackouts May 2024, 30 Aug 2024
        "South Africa": 25}  # load-shedding ended 26 Mar 2024 (< 90 days in 2024)
# cable events with documented national impact (ISOC 2024 outage reports)
cable_events = {"Nigeria": 1,       # 14 Mar 2024 WACS/SAT-3/ACE/MainOne
                "South Africa": 1,  # same event (listed affected country)
                "Kenya": 1,         # 12 May 2024 SEACOM/EASSy
                "Egypt": 0}         # Feb 2024 Red Sea cuts: no documented national impact located
I = {c: grid[c] + 50 * min(1, cable_events[c] / 2) for c in R}


def matrix():
    return np.array([[E[c], H[c], G[c], I[c]] for c in R])


def simulate(M, n=10000, jitter=0.0, lam=0.0):
    w = rng.dirichlet(np.ones(4), size=n)                       # (n,4)
    X = np.broadcast_to(M, (n, *M.shape)).copy()                # (n,4,4)
    if jitter:
        X *= rng.uniform(1 - jitter, 1 + jitter, size=X.shape)  # independent per cell
        X = np.minimum(X, 100)
    S = np.einsum("nk,nrk->nr", w, X) + lam * X[:, :, 1] * X[:, :, 3] / 100
    return S


def report(label, S):
    top = np.bincount(S.argmax(1), minlength=4) / len(S)
    orders = {}
    for row in np.argsort(-S, 1):
        k = " > ".join(R[i] for i in row)
        orders[k] = orders.get(k, 0) + 1
    print(f"\n[{label}]")
    for i, c in enumerate(R):
        print(f"  {c:<13} mean={S[:, i].mean():6.2f} sd={S[:, i].std():5.2f} "
              f"2.5-97.5%=[{np.percentile(S[:, i], 2.5):6.2f},{np.percentile(S[:, i], 97.5):6.2f}] "
              f"share#1={100 * top[i]:5.1f}%")
    for k, v in sorted(orders.items(), key=lambda x: -x[1])[:3]:
        print(f"    {100 * v / len(S):5.1f}%  {k}")


if __name__ == "__main__":
    M = matrix()
    print(f"{'Region':<13}{'E':>7}{'H':>7}{'G':>7}{'I':>7}")
    for c, row in zip(R, M):
        print(f"{c:<13}" + "".join(f"{v:>7.1f}" for v in row))
    report("weights only", simulate(M))
    report("weights + independent +/-10% jitter", simulate(M, jitter=0.10))
    report("weights + independent +/-25% jitter", simulate(M, jitter=0.25))
    report("lambda=0.15 coupling sensitivity", simulate(M, lam=0.15))
    print("\nComponent-wise dominance (weight-invariant):")
    for i, j in itertools.permutations(range(4), 2):
        if np.all(M[i] >= M[j]) and np.any(M[i] > M[j]):
            print(f"  {R[i]} >= {R[j]} on every component")
