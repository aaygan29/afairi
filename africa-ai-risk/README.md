# African Frontier AI Risk Index (AFAIRI)

Multi-region risk index + threat actor characterization for frontier AI misuse/risk on the African continent, organized by spatial region (North/West/East/Southern Africa) with a fully mechanized, citation-audited composite index.

**Current version: `AFAIRI_v4_regional.md`** — organized by region, includes the sourced Threat Actor Characterization section (Boko Haram/ISWAP, Al-Shabaab, "Yahoo Boys"/"AI Boys", Black Axe), plain-text math (paste-ready for Google Docs).

**Superseded: `AFAIRI_v2_hardened.md`** — kept for audit trail only. This was the citation-hardening pass (killed a fabricated ASR benchmark table, corrected the Eskom emissions factor, etc.) and a council-review-driven methodology mechanization pass, both folded into v4. Do not cite v2 directly; see v4's Appendix A for the full correction log.

**Figures:**
- `afairi_v3_montecarlo.png` — Monte Carlo sensitivity (N=10,000 Dirichlet weight draws + input-jitter robustness layer), by region
- `afairi_v3_components_by_region.png` — grouped bar chart of the four AFAIRI components (Exposure/Susceptibility/Governance Deficit/Infra. Fragility) by region

**Code:** `afairi_compute_v3.py` (current, mechanized inputs) and `afairi_compute.py` (superseded, retained for audit trail). Seed fixed at 42, fully reproducible — see v4 Appendix B.

**Status:** not yet submitted anywhere; a standalone piece exploring the same core evidence (Boko Haram/Juelich 2026) is being adapted for GNET — see `../gnet-insight-africa/`.

**v5 extension (2026-08-24, `afairi_v5_workflow_run/`):** 33-agent workflow
following a 5-step methodology (risk vectors → prior-study methodology
survey → replication → cross-validation → application). Extended coverage
to 8 more countries (Morocco, Tunisia, Ghana, Senegal, Ethiopia, Tanzania,
Zambia, Zimbabwe) and validated AFAIRI against real terrorism/AI-incident
tracking methodologies (GTI, GTD, AIID, RAND, UN CTED) rather than generic
political-risk indices. **Caught a real methodology flaw in the process**:
governance_deficit scoring is unrubricked and converged on an arbitrary
round number (55) for 6 of 8 new countries — flagged, not hidden, with a
proposed fix. See `afairi_v5_workflow_run/AFAIRI_v5_extension_report.md`
for the full honest write-up before citing any v5 figures.

**Provenance note:** every quantitative claim in v4 traces to a cited primary or authoritative secondary source (World Bank, Eskom, TransUnion Africa, SABRIC, Our World in Data/Ember, national AI-strategy documents, Juelich 2026, etc.) — see the paper's own Appendix A (citation audit log) and Appendix D (methodology mechanization log) for the full trail, including what was cut from earlier drafts and why.
