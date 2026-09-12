"""Independent check of afairi_compute_v4.py using different methods.

1. Recomputes G and I from the rubric by hand (no shared code paths).
2. Mean check: with w ~ Dirichlet(1,1,1,1), E[w_k] = 1/4, so the expected
   score is the plain component average. Compares against a fresh MC.
3. Exact share-of-weight-space for "#1" on a deterministic simplex grid
   (step 1/100, ~176k points) instead of random sampling.
4. Pairwise: for each pair, exact share of the weight simplex where one
   state outscores the other.
"""
import itertools
import numpy as np
import afairi_compute_v4 as v4

hand = {  # E, H, G = 100-(A+B+C), I = grid + cable
    "Egypt":        [74.0, 39.0, 100 - (25 + 12.5 + 0),  50 + 0],
    "Nigeria":      [40.1, 73.0, 100 - (12.5 + 25 + 50), 50 + 25],
    "Kenya":        [32.1, 83.0, 100 - (25 + 12.5 + 25), 25 + 25],
    "South Africa": [78.3, 77.0, 100 - (25 + 12.5 + 25), 25 + 25],
}
M = v4.matrix()
assert np.allclose(M, np.array([hand[c] for c in v4.R])), M
print("components match hand recomputation")

analytic = M.mean(1)
mc = v4.simulate(M, n=200000)
assert np.allclose(mc.mean(0), analytic, atol=0.15)
print("analytic means:", dict(zip(v4.R, analytic.round(3))))
print("MC means      :", dict(zip(v4.R, mc.mean(0).round(3))))

steps = 100
grid = np.array([(a, b, c, steps - a - b - c)
                 for a in range(steps + 1) for b in range(steps + 1 - a)
                 for c in range(steps + 1 - a - b)]) / steps
S = grid @ M.T
win = S >= S.max(1, keepdims=True) - 1e-9
share = (win / win.sum(1, keepdims=True)).mean(0)
print("grid share#1:", dict(zip(v4.R, (100 * share).round(1))))
print("MC   share#1:", dict(zip(v4.R, (100 * np.bincount(mc.argmax(1), minlength=4) / len(mc)).round(1))))
for i, j in itertools.combinations(range(4), 2):
    print(f"  P_grid({v4.R[i]} > {v4.R[j]}) = {100 * (S[:, i] > S[:, j]).mean():.1f}%")
print("all assertions passed")
