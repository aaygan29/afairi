# PhenoFin: Neuro-Grounded Drift-Diffusion Modeling of Financial Risk-Taking Phenotypes

**Status:** Proposed idea (2026-08-24), not yet started. Team lead: the author,
financial AI / legal AI research collaboration program.

## Idea

Use accumulator/drift-diffusion models (DDM), fit to real neural and
behavioral risk-choice data, to derive individual-level behavioral phenotypes
(loss aversion, risk sensitivity, evidence-accumulation rate). Test whether
those phenotypes predict deviations from rational-agent pricing (disposition
effect, momentum, herding) better than standard behavioral-finance proxies.

Two halves:
1. **Neuroscience half.** Fit calibrated DDM / prospect-theory parameters to
   gamble-choice tasks with fMRI/EEG ground truth.
2. **Finance half.** Use those parameters as a behavioral factor tested
   against real market/trading data.

Direct extension of the existing AIM-DDM work in
[`decision_phenotype`](../projects/Neuroscience/decision_phenotype) out of
general decision-making and into financial choice specifically.

## Project type

Computational neuroeconomics / quantitative behavioral finance. A methods
contribution (a validated, neurally-grounded individual-difference model)
plus an empirical test (does the phenotype carry predictive signal in real
financial behavior data).

Math/stats load: stochastic differential equation (DDM) fitting, hierarchical
Bayesian individual-differences estimation, prospect-theory parameter
recovery, time-series/panel regression against market anomalies.

## Databases

### Neuroscience / behavioral decision-making
- **NARPS** (mixed gambles / loss-aversion fMRI task, large N):
  https://openneuro.org/datasets/ds001734
- **Tom et al. 2007 gain/loss fMRI dataset** (original loss-aversion task,
  OpenNeuro ds000005): https://openneuro.org/datasets/ds000005
- **HCP gambling task** (fMRI, large N): https://db.humanconnectome.org
- **International Brain Laboratory (IBL)** (standardized decision task,
  electrophysiology + behavior): https://data.internationalbrainlab.org
- **Choices13k** (Peterson et al. 2021; ~13,000 human risky-choice decisions,
  built to benchmark cognitive/DDM-style models):
  https://github.com/jcpeterson/choices13k
- **OpenNeuro** (general search for gambling/risk-task fMRI/EEG datasets):
  https://openneuro.org

### Financial / market
- **Kenneth French Data Library** (standard factor returns: momentum, value,
  size, to test whether a behavioral factor adds signal):
  https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- **SEC EDGAR** (filings, insider trading, fund flows):
  https://www.sec.gov/edgar
- **CRSP / WRDS** (institutional-grade trading and returns data; needs
  university/institutional access — likely bottleneck, flag early)
- **Robintrack (archived)** (retail-trader popularity/position data from
  Robinhood, used in disposition-effect and herding studies):
  https://github.com/rreichel3/RobinTrack
- **Yahoo Finance / Nasdaq Data Link (Quandl)** (free daily price/volume
  data for the market-outcome side): https://finance.yahoo.com,
  https://data.nasdaq.com

## Table-style one-line summary

| Title | Type | Lead |
|---|---|---|
| PhenoFin: Neuro-Grounded Drift-Diffusion Modeling of Financial Risk-Taking Phenotypes | Computational Modeling / Empirical Paper | The author |
