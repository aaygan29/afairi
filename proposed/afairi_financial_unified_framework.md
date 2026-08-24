# AFAIRI-Financial: A Unified Financial-Risk and Behavioral-Governance Model of AI Regulatory Deficit

**Status:** Proposed theoretical framework (2026-08-24), not yet executed.
Synthesizes [AFAIRI](../submissions/ai-safety/africa-ai-risk/) and
[PhenoFin](phenofin_neuro_ddm_financial_risk.md). Not a finished
methodology — a specification for what would need to be built and tested.

## The core idea, stated plainly

AFAIRI currently measures *where* AI misuse risk concentrates. It does not
yet answer: what does that risk actually **cost**, in the same units
financial markets already use to price low-probability/high-severity
events, and does the **size of the regulatory gap itself** predict that
cost the way it predicts costs in every other domain already priced this
way (climate, cyber, catastrophe insurance)?

Separately, the decision to delay AI safety regulation is itself a
**decision under risk**, made by a government the same way an individual
investor decides whether to hedge, made under uncertainty, with
present-biased incentives, and with a real cost to acting versus waiting.
PhenoFin already builds a neurally-grounded model of *individual*
risk-taking (drift-diffusion + prospect theory). The bridge proposed here:
**apply the same behavioral-decision mathematics to government regulatory
behavior**, treating "pass an AI safety law" as the choice a DDM models for
an individual, and see whether the same math that predicts individual
risk-taking predicts regulatory delay.

Put together, this is one framework with two coupled halves:

1. **Pricing half** — quantify the financial cost of AI regulatory deficit
   using the actual mathematics catastrophe finance already uses for
   low-probability/high-severity risk.
2. **Behavioral half** — model *why* a government is or isn't closing that
   deficit, using the same decision-under-risk math PhenoFin applies to
   individuals, then use that to forecast trajectory, not just snapshot.

## The master equation: one unified state-space model, many computable outputs

The user's ask is specific: not five separate models (one for financial
outcomes, one for environmental, one for bio, ...) but **one equation**
that different people can apply to compute different outcomes, the way a
single option-pricing PDE computes the price of a call, a put, or a
barrier option depending only on which payoff function you plug in at the
end. Quant finance already has the exact calculus for this shape of
problem — two pieces of it, both standard, both real:

1. **Jump-diffusion processes** (Merton, 1976) — the standard tool for
   assets whose value moves smoothly most of the time but occasionally
   jumps discontinuously on rare, severe events (a market crash, a default).
   This is the right mathematical object for AI-misuse risk: routine
   exposure grows smoothly (more internet penetration, more model access),
   but a documented harm event (the Nigeria Boko Haram/ISWAP case, a
   deepfake-fraud spike) is a discrete jump, not a smooth drift.
2. **Optimal stopping / stochastic control via the Hamilton-Jacobi-Bellman
   (HJB) equation** — the same PDE that prices American options (where
   you're deciding not just the price but *when* to exercise) and underlies
   real-options corporate-finance theory (deciding *when* to invest under
   uncertainty). This is the right mathematical object for a government's
   regulatory decision: not just "regulate or don't" but "regulate now,
   later, or never," which is exactly an optimal-stopping problem.

### The state-space

For country $i$, define a risk-state vector spanning every named domain:

$$R_i(t) = \big(R_i^{\text{bio}}(t),\ R_i^{\text{cyber}}(t),\ R_i^{\text{neuropsych}}(t),\ R_i^{\text{behavioral}}(t),\ R_i^{\text{environmental}}(t),\ \dots\big)$$

Each component is exactly what AFAIRI already scores per domain (Exposure,
Susceptibility, Infrastructural Fragility feed the diffusion term below;
Governance Deficit feeds the control term). New domains slot in as new
vector components without changing the equation, which is what makes this
"could be anything" — the state space is open-ended by construction.

### The dynamics: a jump-diffusion SDE, coupled to a regulatory control

$$dR_i(t) = \underbrace{\mu\big(R_i(t),\, u_i(t)\big)\,dt}_{\text{routine drift}} \;+\; \underbrace{\sigma\big(R_i(t)\big)\,dW_i(t)}_{\text{routine noise}} \;+\; \underbrace{dJ_i(t)}_{\text{catastrophic jumps}}$$

- $\mu(R_i, u_i)$: the routine drift of risk (rising exposure, rising
  susceptibility), *damped by the regulatory-control variable* $u_i(t) \in
  [0,1]$ (AFAIRI's governance deficit, inverted and made continuous/time-
  varying instead of a static score) — more regulation slows the drift.
- $\sigma(R_i)\,dW_i(t)$: ordinary Brownian noise, routine year-to-year
  volatility in each risk component.
- $dJ_i(t) = \sum_{k} Y_k \, \mathbb{1}[\tau_k \le t]$: a **compound
  Poisson jump process** — jump times $\tau_k$ arrive at rate $\lambda(R_i,
  u_i)$ (higher current risk and lower regulation raise the arrival rate of
  a catastrophic event, e.g. a documented AI-enabled terrorism incident),
  jump sizes $Y_k$ drawn from a severity distribution (this is literally
  the same compound-Poisson structure proposed for the pricing half above,
  now embedded directly in the state dynamics rather than treated
  separately).

This single SDE is the "map": it's the same equation regardless of which
domain of $R_i$ you're asking about, which is what makes it a genuinely
unified framework rather than five bolted-together models.

### The government's decision: solved via Hamilton-Jacobi-Bellman

The government chooses the regulatory-control path $u_i(t)$ to minimize
expected discounted total cost:

$$V_i(R, t) = \min_{u_i(\cdot)} \; \mathbb{E}\left[ \int_t^T e^{-r(s-t)} \Big( c(u_i(s)) + L\big(R_i(s)\big) \Big) ds \;+\; e^{-r(T-t)} L\big(R_i(T)\big) \right]$$

where $c(u_i)$ is the real, borrowable **real-options insight**: the cost
of regulating (institutional capacity-building, foreign-investment
friction — the "transition risk" from the NGFS analogy) and $L(R_i)$ is the
**loss function** (financial, environmental, or any other output —
see below). $V_i(R,t)$ satisfies the HJB equation:

$$\frac{\partial V_i}{\partial t} + \min_{u_i} \Big[ c(u_i) + \mu(R_i,u_i) \cdot \nabla V_i + \tfrac{1}{2}\sigma(R_i)^2 \nabla^2 V_i + \lambda(R_i,u_i)\,\mathbb{E}\big[V_i(R_i+Y) - V_i(R_i)\big] \Big] = r V_i - L(R_i)$$

This is the exact PDE structure used to price American options and to
solve real-options investment-timing problems, with one feature worth
being precise about: **the jump *arrival rate* $\lambda$ is itself a
function of the state and the control**, whereas in vanilla option-pricing
jump-diffusion models the jump process is exogenous. To be honest about
prior art: **controlled-intensity point processes are not new mathematics**
— they're standard in actuarial stochastic control (e.g. dividend/
reinsurance optimization, Schmidli's *Stochastic Control in Insurance*).
The novelty here is the domain application, not the structure: nobody has
used a controlled-intensity jump-diffusion to model AI-regulatory risk
specifically. Framed correctly, this is still useful as a **falsifiable
structural claim about this application**: it predicts that countries
which raise $u_i$ (regulatory capacity) should show a measurable
subsequent drop in jump arrival rate, checkable against the labeled event
set in the validation plan below — but the claim to defend is "this
structure fits AI-regulatory risk," not "this structure is new."

### How one equation produces many different computable outputs

The loss function $L(R_i)$ is a plug-in, the same way an option's payoff
function is a plug-in to the same underlying pricing PDE:

- **Financial outcome**: $L^{\text{fin}}(R_i) = $ the compound-Poisson loss
  cost from the pricing-half table above (Value-at-Risk / CVaR on the jump
  component), denominated in currency.
- **Environmental outcome**: $L^{\text{env}}(R_i) = $ an NGFS-style
  physical + transition cost specifically on the environmental component of
  $R_i$ (e.g., AI-compute-siting grid strain, as already flagged in AFAIRI
  v4's Southern Africa case).
- **Any other domain**: swap in a domain-specific severity/cost mapping for
  $Y_k$ (bio-risk severity in DALYs, cyber-risk severity in breach cost,
  etc.) — the state dynamics and the HJB structure do not change, only the
  loss function does.

This is the concrete answer to "a way for people to specifically apply the
model to calculate specific things": **solve the same $V_i(R,t)$ once per
country, then evaluate whichever $L(R_i)$ the user wants against the same
solved value function.** One computational object, many reports.

**This "solve numerically" step is not routine, and pretending otherwise
would be dishonest.** $R_i(t)$ is a 5+ dimensional continuous state vector
(bio, cyber, neuropsych, behavioral, environmental, ...). A grid-based
finite-difference HJB solver is intractable past roughly 3-4 dimensions —
this is the curse of dimensionality, a well-known hard problem, not a
solved implementation detail. Two honest paths forward, neither free: (a)
**scope the first working version down** to 1-2 state dimensions (e.g.
just the financial and terrorism/security components, where the labeled
event set is richest) and only extend to the full vector once that's
validated, or (b) use a high-dimensional-capable numerical method (deep
BSDE / deep Galerkin methods, which solve exactly this class of nonlinear
PDE by training a neural network against the HJB residual, or
Longstaff-Schwartz-style regression Monte Carlo for the optimal-stopping
piece). Route (a) is the responsible default given the current data — see
the identifiability point below.

### What is proposed math versus what is proven right now

To be exact about the honesty boundary this document already commits to:
the SDE structure, the HJB formulation, and the compound-Poisson jump
process are all *standard, established mathematics*, borrowed correctly
from their real domains (Merton jump-diffusion, American-option/real-
options HJB theory, actuarial compound-loss models). What is **new and
unproven** is (a) that AI-regulatory-deficit data actually behaves like a
state-dependent jump-rate process rather than some other structure, and
(b) the specific functional forms of $\mu$, $\sigma$, $\lambda$, and $c$
for this application, which do not exist yet and must be estimated from
the labeled event set. Presenting the equation before that estimation is
presenting a hypothesis with the right shape, not a validated model — the
validation plan below is what would turn it into one.

## Why "it could be anything" is a feature, not a scope problem

The ask (biosafety, cybersafety, neuropsychological safety, behavioral
safety, environmental safety, or anything else) maps cleanly onto how
**catastrophe insurance already handles multi-peril risk**: an
insurance-linked security doesn't need a different pricing formula per
peril (earthquake vs. flood vs. pandemic) — it needs a properly specified
**loss distribution per peril**, and the peril categories are exactly the
regulatory-gap categories here (an unregulated bio-AI interface is a peril,
an unregulated neurotech interface is a peril, an unregulated
environmental/AI-compute-siting interface is a peril). This is not a new
mathematical problem; it's the same multi-peril catastrophe-modeling
problem with new perils.

## What existing mathematics to actually borrow (real, established, not invented for this)

### For the pricing half

| Method | What it's for | Why it fits here |
|---|---|---|
| **Compound Poisson loss models** (actuarial science, standard in catastrophe/insurance pricing) | Models total loss as a random NUMBER of events (frequency) each with a random SIZE (severity) — `S = sum_{i=1}^N X_i`, N ~ Poisson(λ), X_i ~ a severity distribution | Directly maps to "how many AI-enabled harm incidents per year (frequency) × how costly each one is (severity)" — the exact structure GTD/GTI already half-builds for terrorism, just not priced in dollars |
| **Value-at-Risk (VaR) and Conditional VaR / Expected Shortfall (CVaR)** | Standard risk-management measures: VaR = the loss threshold not exceeded with probability p; CVaR = the expected loss GIVEN you're in the tail beyond VaR | Gives a single defensible number for "what's the 1-in-20-year AI-regulatory-deficit loss for this country," the same way banks report VaR for market risk |
| **Catastrophe bond / insurance-linked securities pricing** (real market: cat bonds already price earthquake, hurricane, pandemic risk) | Prices a bond whose payout is triggered by a parametric event (e.g., an earthquake above magnitude X) — the discount/yield embeds the market's own estimate of tail probability and severity | The closest EXISTING real-market analogue to "price the AI-regulatory-deficit tail risk of a country" — cat bond spreads are real, observable market data that could be used as an external validation benchmark if any AI-risk-linked instrument or proxy (e.g., cyber-insurance pricing in weak-regulation markets) exists |
| **Real options theory** (Black-Scholes-adjacent; used in corporate finance for "value of waiting") | Values the option to delay an investment/decision under uncertainty — the option has value because waiting lets you act on new information, but delay also has a cost if the underlying risk is growing | Directly models "why would a government rationally delay AI regulation" as an options problem: regulating now is irreversible (sunk institutional cost, foreign-investment friction) vs. waiting (keeps flexibility but the underlying risk, unlike a stock price, is not a martingale — it's asymmetrically growing), which is itself a testable divergence from the classical model, a genuine potential contribution |
| **NGFS/TCFD climate transition-risk and physical-risk framework** (real central-bank standard: Network for Greening the Financial System) | Splits climate financial risk into "physical risk" (realized disaster cost) and "transition risk" (cost of moving to compliance) — used by central banks worldwide to stress-test bank balance sheets | Gives a ready-made, already-regulator-legitimate template for splitting AI-regulatory risk the same way: "AI physical risk" (realized harm cost, e.g. Nigeria case) vs. "AI transition risk" (cost of building regulatory capacity) — this is the most direct, borrowable structure for the environmental-impact fold-in specifically, since NGFS already covers environmental financial risk and could be extended rather than reinvented |

### For the behavioral/governance half

| Method | What it's for | Why it fits here |
|---|---|---|
| **Drift-diffusion model (DDM)**, already used in PhenoFin | Models a decision as noisy evidence accumulating toward a threshold; parameters = drift rate (how fast evidence pushes toward a decision), threshold (how much evidence is required), starting bias | Reframe: "evidence" = documented AI-harm incidents + international pressure + peer-country regulation; "decision" = pass an AI safety law; drift rate = how fast a government responds to evidence; threshold = institutional inertia/veto-player count. This produces a testable prediction: countries with lower institutional threshold and higher incident-drift should show faster regulatory response, an empirically checkable claim against the real AI-strategy-timeline data already collected in Steps A/E |
| **Prospect theory / loss aversion** (Kahneman-Tversky, foundational to PhenoFin) | Decision-makers weight losses more than equivalent gains, and are risk-seeking in the loss domain | Predicts: a government already experiencing documented AI-harm losses (Nigeria/Boko Haram) may show DIFFERENT regulatory risk-appetite than one that hasn't (risk-seeking to recover vs. risk-averse to protect) — testable against the actual policy-response timeline data |
| **Bayesian hierarchical/multilevel modeling** | Pools data across countries/regions with partial pooling, appropriate for small-N cross-country panels | The honest fix for AFAIRI's n=6 statistical-power problem raised in the v5 report — hierarchical pooling across regions is the standard method for exactly this small-sample cross-country problem, more defensible than a flat Spearman correlation |
| **Epidemiological/contagion compartmental models (SIR-style)**, already used in cyber-risk contagion literature | Models how a risk (or capability, or harm pattern) spreads through a network of connected units over time | Could model how AI-misuse tactics diffuse across the threat-actor network already documented in AFAIRI (Boko Haram/ISWAP ↔ Al-Shabaab transnational jihadist linkage is explicitly named in AFAIRI v4) — treats tactic diffusion as a contagion process with an estimable reproduction number, a genuinely novel and testable extension |

## The genuinely new contribution, stated precisely

Not "we made up a new formula." The contribution is: **nobody has coupled
catastrophe-style financial pricing of AI-regulatory-deficit risk with a
behaviorally-grounded (DDM/prospect-theory) model of the regulatory
decision that creates that deficit, validated against real incident data
with a properly specified true-positive/true-negative framework.** Each
individual piece (cat-bond pricing, DDM, NGFS transition risk) is
established, real, and separately validated in its own field. The coupling
is new.

## How this gets validated empirically — the true-positive/true-negative framework, done honestly

This is the part the v5 AFAIRI report already flagged as the field's real
weakness (n=6, no significance), and it needs to be fixed structurally, not
just re-run with more countries.

1. **Build a labeled event set first, before any modeling.** Take every
   *documented* AI-enabled harm event across all named risk domains
   (bio/cyber/neuropsych/behavioral/environmental/terrorism) — the Nigeria
   Boko Haram/ISWAP case, South Africa's deepfake fraud surge, any future
   documented case — as positive labels. Take country-years with no
   documented event as negative labels. This is the hard, unglamorous,
   necessary step: **without it, "true positive/true negative" is not a
   real framework, it's a phrase.**
2. **Backtest, the way catastrophe models are backtested.** Cat bond and
   reinsurance pricing models are validated by checking whether their
   predicted loss frequency/severity, calibrated on historical data, holds
   out-of-sample against subsequent real losses. Do the same: fit the
   pricing half on a training window of country-years, predict which
   country-years in a held-out window should show a documented incident,
   and score it with ROC/AUC, precision/recall, and calibration curves, not
   just a point correlation.
3. **Report power honestly.** The v5 report already established the field
   has a real small-N problem (n=6, critical ρ≈0.886). This framework's
   validation plan must include an explicit minimum-detectable-effect
   calculation before claiming anything is "validated," the same discipline
   the jspace-loyalty/TAIG work already applies to AI audits — this
   framework should audit itself the same way it proposes auditing AI
   models.
4. **Validate against competing, already-existing models, not just AFAIRI's
   own numbers.** The GTI/GTD comparison in v5 is a start; add cyber-risk
   loss models (e.g., published cyber-insurance loss data where available)
   and NGFS-style climate transition-risk scores as competing predictors,
   and check whether the AI-regulatory-deficit term adds predictive power
   ON TOP OF those established models (an incremental-validity test), not
   just whether it correlates with them in isolation.
5. **Check identifiability before fitting anything, not after.** The
   labeled event set as it currently stands is n=20 countries, one
   English-language search pass, several events flagged
   `plausible_needs_verification` rather than confirmed (see the event
   set's own README). A nonlinear, multi-dimensional $\lambda(R_i,u_i)$ and
   $\mu(R_i,u_i)$ almost certainly cannot be identified from that — this is
   not a detail to discover after spending compute on a fit. Before
   estimating anything: (a) fix the state dimensionality to whatever the
   scoped-down first version uses (see the numerical-tractability note
   above), (b) run a pre-registered power/identifiability check — how many
   labeled country-years does this specific functional form need to pin
   down its parameters within a useful confidence interval — and (c) if the
   current n=20 doesn't clear that bar, either simplify the functional form
   (e.g. a low-dimensional parametric hazard model instead of a free-form
   $\lambda(R_i,u_i)$) or treat this step as "collect more labeled years
   first," not as a green light to fit the full model as specified.

## Data this would need (extending PhenoFin's + AFAIRI v5's source lists)

- **Cat bond / insurance-linked securities pricing data**: Artemis (deal
  database, artemisbm.com), Swiss Re / Munich Re annual catastrophe loss
  reports (publicly published)
- **NGFS climate scenario framework** (for the transition/physical-risk
  split template): ngfs.net/en/climate-scenarios-portal
- **Cyber-risk loss data**: Advisen Cyber Loss Data (partial public access),
  IBM Cost of a Data Breach Report (annual, public)
- **AI-harm incident labels**: AI Incident Database (incidentdatabase.ai),
  plus the manually-verified documented cases already found in AFAIRI v5
  (Juelich/Cambridge 2026 field study, TransUnion Africa deepfake fraud
  report)
- **Government regulatory-response timeline data**: already partially
  collected in AFAIRI v5's `governance_deficit.rationale` fields (national
  AI strategy dates, legal-instrument dates per country) — this is a real
  asset already sitting in the existing data and should be reused, not
  recollected
- **PhenoFin's existing neuro/behavioral database list** (NARPS, Choices13k,
  etc.) for calibrating the DDM parameters this framework reuses

## What I am NOT claiming right now

This document is a specification, not a result. No pricing has been
computed, no DDM has been fit to government decisions, no backtest has been
run. The v5 AFAIRI report's own discipline (flag what's unvalidated, don't
round up a directional finding into a validated one) applies here with
extra force, because this framework is more ambitious and further from
existing precedent than AFAIRI itself.

## What this would enable, once complete — stated specifically, not as a wishlist

Four concrete artifacts, in the order they actually become reachable (each
requires progressively more of the framework to be estimated, not just
specified):

1. **An open benchmark dataset.** The labeled event set
   (`../submissions/ai-safety/africa-ai-risk/afairi_v5_workflow_run/labeled_event_set/`,
   n=20 and growing) released publicly, with its honesty caveats intact
   (English-only search, `plausible_needs_verification` events flagged, not
   promoted to confirmed). This is reachable now, doesn't need the SDE/HJB
   machinery estimated at all, and gives other researchers something to fit
   competing models against — the role GTD played for terrorism research,
   for AI-enabled harm specifically, which currently has no open equivalent.
2. **A per-country marginal-value ranking for donor capacity allocation.**
   Once the scoped-down (1-2 dimension) first version of $V_i(R,t)$ is
   solved, $\partial V_i/\partial u_i$ is directly computable: how much
   expected harm a marginal dollar of regulatory capacity buys down, per
   country. A World Bank, AU, or bilateral aid program could rank funding
   requests by this instead of by GDP or population proxies, which is
   closer to current practice.
3. **A "cost of waiting" brief per government.** The real-options half,
   once fit, computes what delaying an AI safety law by 1/2/5 years costs
   in expected terms versus the institutional cost of passing it now — a
   country-specific number for a ministry or legislative drafting
   committee, not an abstract governance-gap score.
4. **A quantitative backbone for this program's existing qualitative
   tools.** WARDEN and council-review already do calibrated, abstaining
   risk judgment, qualitatively. A fitted $\lambda(R_i,u_i)$ gives them a
   real probability to cite instead of a verbal risk tier — the same
   upgrade a weather forecast gets going from "likely rain" to "70%
   chance."

(1) and, with the scoping fix above, (2) are reachable without solving the
full high-dimensional HJB. (3) and (4) need the fuller estimation. **What
this should not become**, per the section directly below: a commercial
insurance-underwriting or investment-screening input without a separate
fairness review — that application is a refusal, not a roadmap item.

## Dual-use and fairness, stated up front rather than discovered later

A model that outputs a quantitative "catastrophe risk price" per country is
exactly the kind of artifact that can be misused for de facto redlining —
an insurer, investor, or credit-rating consumer treating $V_i(R,t)$ or
$L(R_i)$ as grounds to restrict AI-sector investment or insurance access in
the flagged countries, reproducing the same harm pattern historical
catastrophe-model-driven redlining caused in other domains. This is not a
hypothetical concern for this specific repo: the Global South neuro-
persuasion paper this program has already published was explicit about
avoiding exactly this framing for AFAIRI's country scores. This document
inherits that obligation and does not get to skip it just because the
output here is a dollar figure instead of a 0-100 index score.

**Stated intended use**: donor/multilateral capacity-allocation decision
support (directing AI-safety governance funding to where it reduces the
most expected harm), matching the framing already established for AFAIRI
itself. **Stated non-use**: this framework should not be presented, sold,
or licensed as an input to commercial insurance underwriting, credit
scoring, or investment-screening decisions about a specific country without
a separate, explicit fairness and disparate-impact review — the same
discipline NGFS itself requires of climate-risk scores used in bank
stress tests. This restriction belongs in any future publication or tool
built from this framework, not just in this internal proposal document.

## Recommended next step

Before running this as a large workflow: build the labeled event set (step
1 of the validation plan) as a standalone, smaller task first — that
dataset is required by every other part of this framework and doesn't
exist yet. Everything else (pricing, DDM-fitting, backtesting) is
downstream of having real positive/negative labels to test against.

**The existing AFAIRI v5 work is not superseded by this document — it's the
first real input to it.** The v5 report
(`../submissions/ai-safety/africa-ai-risk/afairi_v5_workflow_run/`) already
contains: (1) a partial labeled event set (the Nigeria Boko Haram/ISWAP
case is a real positive label; Kenya's real-terrorism-but-no-AI-tooling
case is a real negative label; South Africa's deepfake fraud is a second
domain of positive label), (2) real per-country governance-deficit
timelines that are the raw material for estimating $u_i(t)$'s historical
path, and (3) an already-honest accounting of where the current AFAIRI
numbers are unreliable (the governance_deficit=55 flaw), which is exactly
the kind of measurement-error awareness this framework's parameter
estimation step needs to inherit rather than re-discover. Nothing here
should be built as a green-field replacement; it should be built as v6 on
top of v5's data and its self-audit.
