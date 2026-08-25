# Pilot experiment: three passes, honest result

Testing the master framework's core prediction (higher AI-regulatory
deficit → more documented AI-harm events) against real, sourced data.

| Pass | n | Test | Result | Significant? |
|---|---|---|---|---|
| 1 | 13 | Spearman rho | -0.261 | No (critical rho 0.553) |
| 2 (post-verification) | 13 | Spearman rho | -0.222 | No |
| 3 (n expanded, +10 countries) | 23 | Spearman rho | -0.281 | No (critical rho 0.413) |
| 3, naive Poisson GLM | 23 | coefficient p-value | p=0.022 | **Looks significant — but is wrong** |
| 3, negative binomial (correct model) | 23 | coefficient p-value | p=0.076 | No |

## The real finding: a model-selection trap, caught in the act

The data is overdispersed (variance = 2.35x the mean event count).
Poisson regression assumes variance equals the mean; when that's violated,
Poisson standard errors are too small and p-values look artificially
significant. The naive Poisson fit here would have let this project claim
"n=23, p=0.02, significant relationship found" — and that claim would have
been a Type I error produced by using the wrong model, not real signal.
Negative binomial regression, which is built for overdispersed count data
(and is the actually-correct technique here, not just a stricter
alternative), shows p=0.076: not significant at conventional thresholds.

This is exactly the failure mode the whole AFAIRI program has been built
to catch (see the jspace-loyalty operating-characteristics paper this
framework already cites). Reporting the Poisson number alone, without
checking dispersion, would have been the project's own worst-case outcome:
a confident, wrong, statistically-dressed-up finding.

## What the data actually shows, three times over

Across all three passes — smaller n, larger n, verified vs. unverified,
correct model vs. naive model — the relationship between AFAIRI's
governance_deficit score and documented event count is **never
significant, and its direction is consistently backwards** from the
framework's core prediction (more events associate with *lower* scored
governance deficit, not higher).

Two honest readings, both worth stating rather than picking one:

1. **The framework's core mechanism may be wrong, or wrong at this
   resolution.** A country's static, current governance_deficit score may
   not causally predict harm events the way the framework's structural
   claim (regulation reduces jump *rate*) assumes — especially since the
   dataset has no time dimension (one snapshot per country, not a panel of
   governance-status-over-time matched to when events occurred).
2. **The measurement may not yet be sensitive enough.** governance_deficit
   is a coarse 0-100 tier score from qualitative rationale, not a
   continuously time-varying regulatory-capacity signal; event count is a
   noisy, English-language-search-limited proxy for true incident rate.
   Both are exactly the kind of measurement-validity gap Gate 8 of a
   council-review would flag.

**What would actually distinguish these two explanations, concretely**:
build the panel version of this dataset — governance_deficit *at the time
of each event*, not a current snapshot — so the test is "did the
regulatory gap predict the event," not "does the current score correlate
with historical event counts regardless of when the gap opened or
closed." That is real, additional work, not a re-run of what's already
here.

## What this means for the master framework document

The council-review-driven identifiability check that gated this
experiment did its job: it stopped the project from fitting the full
multi-dimensional jump-diffusion/HJB model on data that, now tested three
times, does not support even the simplest univariate version of its core
claim. **The responsible next step is not more compute on the current
design — it's the panel-data redesign above, or an honest published
negative result if that redesign isn't pursued.**

Full data: `scoped_pilot_experiment_v2_post_verification.json` (n=13),
`../scoped_pilot_experiment_v3_n23.json` (n=23, both models).
