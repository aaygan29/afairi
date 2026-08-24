# AFAIRI v5 extension: methodology survey, replication, validation, application

Produced by a 33-agent multi-agent workflow (Sonnet 5), 2026-08-24. Raw structured
output: `raw_result.json`. Figures: `fig_tranche2_components.png`,
`fig_validation_benchmark.png`.

## What this is

An extension of the existing [AFAIRI v4](../AFAIRI_v4_regional.md) risk index
following a 5-step methodology, per instruction:

- **(a)** Establish AI-relevant risk vectors per country
- **(b)** Survey prior studies that actually track AI safety / AI-enabled
  terrorism, and extract their real mathematical methodology
- **(c)** Replicate those studies' analysis on our countries
- **(d)** Validate AFAIRI's own methodology against those same prior studies,
  on countries they already cover
- **(e)** Apply AFAIRI to 8 new countries (Morocco, Tunisia, Ghana, Senegal,
  Ethiopia, Tanzania, Zambia, Zimbabwe)

Every step includes a per-country citation audit by a second, independent
agent instructed to treat every figure as an unverified claim. **This is not
a finished, publication-ready result** — it's a structured first pass with
real sourcing, real self-caught errors, and one real methodological flaw
described below. Treat it as a draft to correct, not a final number set.

---

## Step (b): what the prior studies actually measure

None of the frameworks surveyed publish a single "AI-enabled terrorism risk
score." That absence is itself the accurate finding, not a search failure:

| Framework | What it actually measures | Has a public formula? |
|---|---|---|
| **Global Terrorism Index** (GTI, IEP) | Weighted terrorism-*impact* composite per country, built from incidents/fatalities/injuries/property-damage, 5-year decay-weighted, banded 0-10 | **Yes** — `Raw = 1×incidents + 3×fatalities + 0.5×injuries + weighted hostages/damage`, then 5-yr weighted average, then log-banded to 0-10 |
| **Global Terrorism Database** (GTD, START/U. Maryland) | Raw event-level terrorism incidents (~120 coded variables/incident), no scoring | No — flat dataset, GTI is built on top of it |
| **AI Incident Database** (AIID) | Real-world AI *safety/harm* incidents generally (bias, crashes, deepfakes, etc.) — not terrorism-specific, not scored | No — unweighted incident/issue repository with overlapping taxonomies |
| **RAND** (AI-cyber nexus, AGI wargames, biosecurity capability-uplift work) | Qualitative: wargame/tabletop exercises, structured decision-frameworks, capability-uplift narratives | No published formula |
| **UN CTED** (Algorithms and Terrorism report, 2023-24 briefings) | Qualitative threat-landscape taxonomy + country-assessment practice tied to UNSCR 2341 | No published formula |

**Implication for validation:** the only quantitative benchmark available is
GTI/GTD (general terrorism, not AI-specific). AIID, RAND, and UN CTED are
real and relevant but qualitative — they can corroborate a specific
documented case (as they do for Nigeria, below) but can't be correlated
numerically. This is a genuine limitation of the *field*, not of this
workflow.

---

## Step (c): replicating GTI on our countries

Real, cited GTI scores were found for 8 of 14 countries (Egypt, Nigeria,
Kenya, South Africa, Ethiopia, Zimbabwe, Somalia, Iraq); Morocco, Tunisia,
Ghana, Senegal, Tanzania, and Zambia returned `data_unavailable=true` rather
than an invented score, because no specific current-edition figure could be
verified. Full per-country sourcing is in `raw_result.json` →
`step_b_and_c_prior_study_replication`.

---

## Step (d): validating AFAIRI against real terrorism/AI-incident data

Benchmark set: the 4 already citation-audited AFAIRI anchors (Egypt,
Nigeria, Kenya, South Africa) + Somalia and Iraq (high-terrorism-density
contrast cases). See `fig_validation_benchmark.png`.

**Result, stated honestly:**

- Rank correlation between AFAIRI's infrastructural-fragility read and real
  GTI terrorism-impact ranking: **Spearman ρ ≈ 0.88-0.89**. Governance
  deficit vs. GTI: **ρ ≈ 0.81-0.85**.
- **But n=6, and the critical ρ for significance at p<.05 is ≈0.886** — the
  stronger estimate just brushes significance and would not survive
  replication with a larger sample. **This is directional agreement, not a
  validated correlation.** Do not cite this as "AFAIRI is statistically
  validated."
- **The single strongest piece of evidence is not the correlation at all**:
  the Juelich/Cambridge 2026 field study (57 interviews with former Boko
  Haram/ISWAP members) directly documents AI-tool use for bomb-making
  guidance and jailbreak circumvention — in Nigeria, the exact country
  AFAIRI independently scores as highest infrastructural fragility (89.1) in
  the sample. That's a real hit on the actual construct AFAIRI claims to
  measure, not a coincidence of rank statistics.
- **Kenya is an instructive non-failure**: real terrorism exists (rank 21
  globally, cross-border Al-Shabaab attacks) but AFAIRI scores it low on
  fragility/governance-deficit, and no AI-enabled incidents were found there
  either — consistent with AFAIRI correctly separating "terrorism exists"
  from "AI-enabled terrorism infrastructure exists," which is the
  discrimination it's supposed to make.
- **Egypt is the weak link**: moderate AFAIRI fragility score but low,
  declining real terrorism activity and no AI-terrorism evidence found at
  all. Could be an AFAIRI over-weighting issue or a genuine reporting gap —
  the data can't distinguish those, and Egypt's AFAIRI values were reused
  from the prior v4 study rather than freshly computed. Flagged
  inconclusive, not agrees/disagrees.
- **South Africa can't be used as evidence either way**: its AFAIRI
  governance-deficit/fragility values are missing-data placeholders (v4
  never actually computed them), not real zeros. Counting them would have
  artificially inflated apparent agreement with SA's real GTI=0.

Full text: `raw_result.json` → `step_d_validation.correlation_synthesis`.

---

## Step (a)+(e): applying AFAIRI to 8 new countries — and a real methodology flaw this process caught

Per-country scores in `app_rows.json` / `fig_tranche2_components.png`.

**The independent citation audit is what caught this, and it's worth taking
seriously rather than smoothing over:** governance_deficit landed on
**exactly 55** for 6 of 8 countries (Morocco, Tunisia, Ghana, Senegal,
Ethiopia, Zambia), each backed by genuinely different, real, well-sourced
qualitative rationale (different named strategies, different years,
different legal instruments) — but converging on the same round number
because **there is no actual rubric translating a qualitative governance
description into a 0-100 score.** The per-country verifiers caught this in
isolation for Morocco and Zimbabwe individually ("reads as an analyst's gut
call dressed as a metric," "the pattern most consistent with fabricated
precision"); only comparing across all 8 results together (which no single
verifier agent could see) reveals it's systemic, not a one-off.

**This does not mean the underlying research is fake.** The qualitative
findings behind each score are real and specifically sourced (e.g. Ghana's
April 2026 National AI Strategy and September 2025 Data Protection
Commission guidance; Zambia's November 2024 National AI Strategy and
National AI Council). What's unreliable is the *numeric encoding step* —
converting "has a strategy but no binding AI-specific law" into a precise
integer with no stated formula.

**Fix before using these numbers for anything comparative:** replace the
free-floating governance_deficit number with an explicit rubric, e.g.:

| Tier | Score | Criterion |
|---|---|---|
| 0 | 0-10 | Comprehensive, binding AI-specific law in force |
| 1 | 15-25 | AI-specific provisions in force (partial) |
| 2 | 40-50 | Binding adjacent-domain law (data/cyber) but no AI-specific provision |
| 3 | 55-65 | Published national AI strategy/policy, no binding law |
| 4 | 70-80 | Draft/proposed AI framework only |
| 5 | 90-100 | No AI governance activity found |

Other flagged issues (Morocco: 2 of 5 fields unverifiable as stated;
Zimbabwe: 2 unpinned fraud statistics, 1 regional-proxy figure mislabeled as
country-specific) are in `app_rows.json` per-country `citation_issues` and
should be corrected before this data is cited anywhere.

**Countries with real, specific documented AI/terrorism-adjacent risk
vectors found** (not invented — see `risk_vectors` field per country in
`app_rows.json` for full sourcing): Zimbabwe (EcoCash mobile-money fraud
patterns, unpinned statistics need re-verification), Ghana and Senegal
(published AI strategies create a governance baseline but no documented
misuse case found), Ethiopia and Tanzania (institutional AI governance
anchors exist, no documented AI-enabled incident found), Morocco and
Tunisia and Zambia (governance activity documented, no incident found).
**Absence of a found incident is reported as absence, not filled with a
plausible-sounding invented one** — this discipline held across all 8
countries per the verifier audits.

---

## Honest bottom line

- The prior-study methodology survey (step b) is solid and can be cited: it
  correctly distinguishes GTI (quantitative, general terrorism) from GTD
  (raw data), AIID (AI-safety incidents, not terrorism), and RAND/UN CTED
  (qualitative, no formula) — a distinction the original request risked
  collapsing.
- The validation (step d) is genuinely informative but statistically weak
  (n=6): the real finding is the single case-level hit (Nigeria/Boko
  Haram/ISWAP), not the correlation coefficient. Report it that way, not as
  "validated."
- The application (step e) surfaced a real, fixable methodology gap
  (unrubricked governance_deficit scoring) rather than hiding it — that's
  the system working as intended, not a failure of the workflow.
- **Do not treat any of these 8 new countries' governance_deficit=55 values
  as comparable numbers until the rubric above (or an equivalent) is
  applied and the scores are recomputed.** Exposure, susceptibility, and
  infrastructural_fragility figures are generally better-sourced (named
  datasets, specific indicators) and safer to cite as-is, with the specific
  flagged exceptions noted per country.
