AFAIRI: anonymized supplementary code for double-blind review.

code/afairi_compute_v4.py  -- inputs, index, and Monte Carlo (Dirichlet(1,1,1,1), seed 42)
code/verify_afairi_v4.py   -- independent check: hand recomputation, analytic means, exact simplex grid
code/afairi_figures_v4.py  -- generates Figure 1 (components) and Figure 2 (sensitivity)

Run from the code/ directory:
  python3 afairi_compute_v4.py && python3 verify_afairi_v4.py && python3 afairi_figures_v4.py

All quantitative results in the paper are reproduced by these scripts. No author-identifying
information is included.
