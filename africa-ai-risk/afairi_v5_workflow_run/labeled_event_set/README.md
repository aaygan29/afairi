# AFAIRI labeled event set — v1

20 countries (12 African + Somalia + 7 Middle Eastern), each with a
multi-domain (not just terrorism) AI-harm incident search, an independent
citation-quality audit, and (for the MENA batch) explicit reproducibility
scoring. Full data: `merged_labeled_event_set.json`.

## Build process, for reproducibility

Three workflow runs, merged by hand, not blindly concatenated:

1. `afairi-labeled-event-set` (14 African/Iraq/Somalia countries) — hit the
   session token limit partway through; **7 agents failed outright** and
   were re-run via `Workflow.resume`, which replays completed agents from
   cache and only re-executes what failed. Final: 28/28 agents clean.
2. `afairi-labeled-event-set-mena` (6 MENA countries) — same limit, same
   resume pattern. **Two entries came back as literal unfilled placeholder
   templates** (Yemen, Lebanon) rather than real failures — the harness
   counted them as "succeeded" because they returned schema-valid but
   empty/fake content, so a plain resume would have replayed the same junk
   forever. A third run with slightly reworded prompts was needed to force
   genuine re-execution. **UAE also silently degraded to a placeholder on
   its resume run** despite real data existing from the first pass — this
   was caught only by manually diffing the resume output against the
   original notification, and was patched by hand rather than trusted from
   the "completed, no errors" status alone. **Lesson for future runs of
   this kind: a workflow reporting 0 errors is not sufficient evidence the
   data is real — schema validity and actual content have to be checked
   separately, every time.**
3. `afairi-labeled-event-set-yemen-lebanon-retry` — fresh, forced run for
   the two placeholder failures, with an explicit `is_real_data` field
   added to the verifier schema so this specific failure mode gets an
   automated check next time, not just a manual catch.

**South Africa and UAE's already-established positive events** (TransUnion
Africa deepfake-fraud surge; the $35M Dubai voice-cloning bank fraud) were
**manually restored** into the final dataset — the fresh-search agents,
correctly following instructions to focus on *other* domains for
already-known cases, left those array fields empty rather than re-listing
the established finding, which would have silently dropped real, solid
data from the compiled set if not caught by hand.

## What's actually in here

- **Solid, multi-source-corroborated positive events**: Nigeria (Boko
  Haram/ISWAP AI use, SEC deepfake-investment-scam alerts, INTERPOL's 55%
  AI-implicated-cybercrime finding), UAE ($35M voice-cloning fraud), South
  Africa (1,200% YoY deepfake fraud surge), Kenya (multiple domains beyond
  the already-known election-moderation case).
- **`plausible_needs_verification` events** that should NOT be treated as
  confirmed without a follow-up pass: Syria's AI-amplified sectarian
  violence claim (single secondary-source chain), Yemen's AQAP
  generative-AI propaganda claim (movement-level, not AQAP-specific),
  Yemen's Houthi-drone AI-guidance claim (capability speculation, not
  confirmed).
- **Genuine negatives** (searched, not found, not just unchecked): e.g.
  Yemen's environmental/compute-siting domain — explicitly reasoned as
  implausible given Yemen's collapsed grid and active conflict, not a lazy
  null.
- **Real, honestly-disclosed gaps**: every entry's `domains_not_searched`
  field lists what wasn't covered (most commonly: Arabic-language local
  sources, since all searches ran in English — a real, acknowledged
  blind spot across the whole dataset, not just one country).

## Known limitations before this is used for anything

1. English-language search only, across all 20 countries. Arabic and
   French-language local reporting was not searched; this dataset likely
   undercounts true incidence, especially for MENA and Francophone West
   African countries.
2. `plausible_needs_verification` events need a dedicated follow-up
   verification pass before being promoted to `confirmed` and used as
   positive labels in any calibration.
3. Negative labels mean "searched this domain, found nothing in English-
   language sources," not "verified absent." Treat as weak negatives, not
   strong ones.
4. This is n=20, one search pass each. Real model calibration (per the
   [unified framework](../../../proposed/afairi_financial_unified_framework.md))
   needs this repeated over time (multiple search passes, ideally
   multilingual) before frequency/rate parameters can be estimated with any
   confidence.
