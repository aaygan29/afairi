# AFAIRI — African Frontier AI Risk Index

A multi-region risk index and threat-actor characterization for
frontier-AI misuse/risk, organized by spatial region, with a fully
mechanized, citation-audited composite index — plus an open, verified
labeled dataset of documented AI-enabled harm events, and a proposed
(not yet validated) theoretical framework for pricing and forecasting
AI-regulatory-deficit risk.

## Start here

- **[africa-ai-risk/](africa-ai-risk/)** — the index itself. Current
  version: `AFAIRI_v6_revised_manuscript.txt` (September 2026 revision
  after external review; index v4 with revised constructs, figures
  `afairi_v4_*.png`, independent verification script). Previous version
  `AFAIRI_v4_regional.md` is retained for the audit trail. Both cover
  North/West/East/Southern Africa, one deeply-documented anchor country
  per region, Monte Carlo sensitivity analysis, threat-actor characterization for Boko Haram/ISWAP,
  Al-Shabaab, "Yahoo Boys"/"AI Boys", Black Axe).
- **[africa-ai-risk/afairi_v5_workflow_run/](africa-ai-risk/afairi_v5_workflow_run/)**
  — extension to 8 more African countries plus Middle Eastern countries,
  validated against real terrorism/AI-safety-tracking methodologies (GTI,
  GTD, AI Incident Database, RAND, UN CTED) rather than generic
  political-risk indices. **Read this before citing any number in here** —
  it documents a real methodology flaw the process caught (an unrubricked
  governance-deficit score that converged on an arbitrary 55 for 6 of 8
  countries) and how it was fixed.
- **[africa-ai-risk/afairi_v5_workflow_run/labeled_event_set/](africa-ai-risk/afairi_v5_workflow_run/labeled_event_set/)**
  — an open, sourced dataset of documented AI-enabled harm events across
  20 countries (African + Middle Eastern), spanning terrorism/security,
  cyber, financial fraud, biosecurity, neuropsychological/behavioral, and
  environmental domains. Every claim was independently adversarially
  fact-checked: 10 of the original 20 unconfirmed claims were **rejected**
  after failing primary-source verification (see
  `VERIFICATION_PASS_RESULTS.md` and `rejected_claims_log.json`) —
  this dataset shows its work, including what it threw out.
- **[proposed/afairi_financial_unified_framework.md](proposed/afairi_financial_unified_framework.md)**
  — a **proposed, not-yet-validated** theoretical framework coupling
  catastrophe-finance-style pricing (jump-diffusion, compound Poisson loss
  models) with a behaviorally-grounded model of government regulatory
  decision-making (Hamilton-Jacobi-Bellman / real options, drift-diffusion
  decision modeling). A scoped pilot experiment testing this framework's
  core predictor already ran and found **no significant effect at current
  sample size** (n=13, Spearman ρ=-0.22, p=0.47) — reported honestly as a
  negative/underpowered result, not hidden.
- **[proposed/phenofin_neuro_ddm_financial_risk.md](proposed/phenofin_neuro_ddm_financial_risk.md)**
  — a related, separately-proposed project (neuro-grounded drift-diffusion
  modeling of financial risk-taking phenotypes) that the framework above
  borrows its behavioral-modeling approach from.

## What this project has been careful about

This index assigns risk-relevant scores to specific countries. That is a
genuine dual-use concern (see the "Dual-use and fairness" section of the
proposed framework doc), and this project has tried to build in the
disciplines that keep it honest rather than just useful-looking:

- **No invented numbers.** Multiple drafts of AFAIRI had fabricated
  figures caught and removed (a fabricated benchmark table, an invented
  biosecurity compliance percentage) — see `AFAIRI_v4_regional.md`
  Appendix A for the correction log. Countries/regions without real,
  citable data are marked as gaps, not filled in with placeholders.
- **Adversarial self-verification.** The labeled event set went through
  an independent fact-checking pass that rejected half of its unconfirmed
  claims rather than accepting the first search result.
- **Honest statistical power.** Correlations and pilot experiments report
  their own significance thresholds and minimum-detectable-effect sizes,
  and are described as underpowered when they are, rather than rounded up
  to "validated."
- **Stated intended use.** Donor/multilateral AI-safety capacity-allocation
  decision support. **Stated non-use**: commercial insurance underwriting,
  credit scoring, or investment screening without a separate fairness and
  disparate-impact review.

## Status

Active, incomplete, published as work-in-progress rather than a finished
result. See each subfolder's own README/status notes for what's validated
versus proposed.
