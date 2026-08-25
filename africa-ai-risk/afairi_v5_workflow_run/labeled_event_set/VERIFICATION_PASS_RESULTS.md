# Verification pass results

20 `plausible_needs_verification` events were sent to independent
adversarial fact-checkers (fresh agents instructed to actively try to
refute each claim, not confirm it) with primary-source lookup.

## Outcome

- **7 confirmed → promoted, with a genuine primary source now attached**
  (e.g. Kenya's KE-CIRT/CC AI-phishing finding traced to independent
  corroboration beyond the single original article; Saudi Arabia's
  600%-deepfake-fraud claim traced to its actual origin, a Sumsub press
  release, not the secondary blog posts that had recycled it; Lebanon's
  AI-fusion targeting system traced to the primary investigative piece,
  The Dial, with a named acknowledged case).
- **10 rejected outright** — see `rejected_claims_log.json` for the full
  reasoning per claim. Two catches worth naming specifically: the Nigeria
  water-stress claim cited an ACM paper as showing Nigeria has "high water
  consumption per model inference among African data-center sites" — the
  paper explicitly **excludes Nigeria** from that analysis; the Zambia
  AI-fraud claim's cited source (a DarkReading article) turned out to be
  about a **different, unrelated Zambian cybercrime case entirely** — a
  source mismatch the original search pass missed.
- **1 stayed plausible_needs_verification** (Ghana's Contender 3.0 case):
  both underlying facts are real and independently sourced, but the
  specific link between them (AI methods used in that particular arrest
  operation) isn't supported by any source found — correctly identified as
  a conflation rather than confirmed or rejected outright.

## What this changed, and what it didn't

Re-running the scoped pilot experiment (rubric-corrected governance_deficit
vs. verified positive-event count, n=13, South Africa excluded) after
applying these verdicts:

| | Before verification | After verification |
|---|---|---|
| Spearman rho | -0.261 | -0.222 |
| p-value | 0.389 | 0.467 |
| Significant at n=13? | No | No |
| Minimum detectable rho (80% power) | 0.709 | 0.709 |

**The correlation barely moved.** This is itself the useful finding: data
*quality* was a real problem (10 of 20 flagged claims didn't hold up), and
fixing it was worth doing on its own terms, but it was never the reason
the pilot failed to find a significant relationship. The bottleneck is
sample size (n=13, MDE=0.709), exactly as the original identifiability
check predicted. **Verification pass: done and worth having done. Next
bottleneck: more labeled country-years, not better cleaning of the
existing ones.**

Full data: `../scoped_pilot_experiment_v2_post_verification.json` (the
"before" run's numbers are the ones in the table above; the raw
pre-verification file was superseded and removed once its results were
folded into this comparison), `rejected_claims_log.json` (what was cut and
why).
