---
title: "05 — Verdict and Joe's Walkthrough Packet"
status: active_research
doc_type: synthesis
updated_at: "2026-05-31"
---

# 05 — Verdict and Joe's Walkthrough Packet

**artifact:** internal origin artifact
**Status.** Local-only draft. Generated 2026-05-31. Single-page summary for Joe's walkthrough_review at validation/4.
**Predecessor inputs.** `01-jordan-calm-formalization.md`, `02-option-b-metric-cointegration.md`, `03-bridge-to-gw-tests.md`, `04-five-persona-dialectic.md`.

---

## TL;DR

**Verdict: PARTIAL — layer-split recovery.**

- **At the signed-real-valued readout layer:** BOTH JD-CALM and AC-CALM RECOVER the bridge. The signed-real GW axial-charge aggregate admits a coordination-free distributed implementation under either framework.
- **At the integer-topological-index readout layer:** NEITHER RECOVERS. Integer recovery requires either an unbounded-truncation limit (outside bounded-radius CALM) or a non-CALM rounding step.

The verdict is a **fourth option** not in internal origin artifact's seed list (JORDAN RECOVERS / OPTION B RECOVERS / NEITHER). The honest answer is layer-split: signed-real layer recovers, integer-index layer does not.

This *confirms* the 21-persona meta-verdict's "layer-split" structural diagnosis (issue B, surfaced by 5 personas) and *strengthens* the internal origin artifact Option II-Retreat publication path by providing concrete technical machinery (JD-CALM and AC-CALM) for the propagation-layer positive result and the decision-layer negative result.

---

## 1. Jordan-CALM precise statement + counterexample re-test outcome

**Jordan-decomposed signed-CALM (JD-CALM) — `01` §2:**

A signed real-valued aggregate query `Q` is JD-CALM iff there exist `Q⁺, Q⁻ : 2^Inputs → ℝ₊` with:
- (J1) `Q = Q⁺ - Q⁻`
- (J2) Each of `Q⁺, Q⁻` is standard-CALM-monotonic over `(ℝ₊, +, ≤)`
- (J3) The sign classification `sign(x, I) ∈ {+, -}` at each site is computable from local data without coordination (Jordan-admissibility)
- (J4) Readout is the signed subtraction `Q⁺ - Q⁻`

This is the lifted-to-signed-real generalization of the PN-counter CRDT (Shapiro et al. 2011); the construction matches the internal origin artifact §19 Statistics persona's recommendation and aligns with Khare-Singh's signed-lattice-measure Jordan decomposition.

**Counterexample re-test outcome — `01` §4:**

V2's counterexample (disjoint A, B with `Q_ε(A) = Q_ε(B) = 0` but `Q(A ∪ B) = 1`) has two readings:

- **Case (a) — integer-index readout with rounding:** JD-CALM **does NOT recover.** The rounding step at readout is orthogonal to the per-component CALM split.
- **Case (b) — signed-real readout with bounded error:** JD-CALM **recovers** (collapses into AC-CALM's readout).

**internal origin artifact's *separate* instanton/anti-instanton failure** (input grows, signed result shrinks): JD-CALM **handles cleanly** — adding the anti-instanton grows `Q⁻` (correctly classified as a Jordan-aggregate feature); the signed-difference readout decrease is *not* a JD-CALM violation. This is the load-bearing structural win of JD-CALM over ε-local CALM.

---

## 2. Option B precise statement + ε-bound

**Approximate-consistency CALM with metric cointegration (AC-CALM) — `02` §2:**

A query `Q` over an influence-weight-bounded distributed input is AC-CALM iff there exists a family `{Q_r}_{r ≥ 0}` with:
- (B1) **Metric-cointegration bound:** `|Q(x, I) - Q_r(x, I)| ≤ ε(r) := (C' · a / γ) · exp(-γ r / a)` — the truncation error is the integrated tail of the exponentially-decaying influence weight beyond radius `r`
- (B2) Each fixed-`r` truncated query `Q_r` is standard-bounded-radius CALM-monotonic
- (B3) Cross-replica disagreement is bounded by `2 ε(r)` deterministically
- (B4) System operator chooses `r ≥ (a / γ) log(C' · a / (γ · ε_target))` to hit a target consistency tolerance `ε_target`

**The ε-bound is `ε(r) = (C' · a / γ) · exp(-γ r / a)`**, decaying exponentially in `r`. This is the *deterministic-decay* analog of probabilistically-bounded-staleness (Bailis et al. 2012), with the decay rate set by the GW kernel's locality scale `(a, γ)` from Hernández-Jansen-Lüscher 1999.

AC-CALM repairs V2's truncation-rounding failure by **replacing the rounded-integer readout with a bounded-error real-valued readout** — there is no rounding step to break.

---

## 3. Bridge-to-GW outcome per framework

Detail in `03` §1-2; summary table in `03` §5.

| Bridge claim | JD-CALM | AC-CALM |
|---|---|---|
| Signed-real per-site density `q_A(x)` locally computable | YES | YES |
| Signed-real aggregate `Q_A` propagation-layer CALM | YES (Jordan-split) | YES (per-r CALM) |
| Integer index `n₊ - n₋` recoverable as CALM readout | NO | Per-config YES, uniform NO |
| Instanton/anti-instanton input growth | YES (Jordan-aggregate feature) | YES (silent on signed-monotone) |
| V2 truncation-rounding counterexample | NO at integer readout, YES at signed-real | YES (no rounding) |
| Bridge to GW signed-real readout survives | YES | YES |
| Bridge to GW integer-index readout survives | NO | NO uniformly |

**JD-CALM** gives the *strongest structural classification* of signed-cancellation as a Jordan-aggregate feature.
**AC-CALM** gives the *strongest practical bound* on cross-replica consistency.
**Combined JD+AC-CALM** gives both, parameterized by per-sign × per-radius.

---

## 4. Honest verdict

**The bridge from a signed-CALM framework to GW observables survives at the signed-real-valued readout layer under both JD-CALM and AC-CALM. The bridge does NOT survive at the integer-topological-index readout layer under either framework.**

This is the fourth-option verdict: **PARTIAL RECOVERY AT THE SIGNED-REAL LAYER; NO RECOVERY AT THE INTEGER-INDEX LAYER.** The closest of the three seed verdicts is "OPTION B RECOVERS BRIDGE" (generalized to include JD-CALM) read at the *bounded-error approximate level*; the integer-index extension is dead.

Five-persona dialectic (`04`) converges 5/5 on this layer-split verdict. The 21-persona meta-assessment §S.2 issue B (layer conflation) and §S.4 honest-meta-verdict are *confirmed and strengthened* by this exploration: the signed-CALM repair gives concrete technical machinery (JD-CALM + AC-CALM) for the layer-split publication, not a recovery of the strong internal origin artifact / internal origin artifact claims.

**Smuggling check (per `04` P5):** definitions are not constructed to bias toward RECOVERS; the readout-target distinction (signed-real vs. integer-index) is structurally load-bearing, not an artifact of phrasing. The verdict is not being smuggled.

---

## 5. What Joe walks

At validation/4 + joe + walkthrough_review, Joe needs to decide:

**Q1. Is the layer-split verdict the right honest reading?**
Recommendation: yes. The signed-CALM exploration confirms (rather than overturns) the 21-persona meta-verdict's layer-split structural diagnosis. JD-CALM + AC-CALM are the technical machinery, not a strong-claim recovery.

**Q2. Does this change the internal origin artifact publication-path decision (Option II-Retreat from the 21-persona meta-verdict §S.5)?**
Recommendation: yes — *strengthen* Option II-Retreat by adding the JD-CALM and AC-CALM technical machinery to the single-paper scope. The propagation-layer positive result now has concrete content ("the GW signed-real axial-charge aggregate is JD-CALM via per-sign decomposition; cross-replica consistency is bounded by `2 ε(r)` under AC-CALM with metric cointegration to the GW kernel's locality scale"). The decision-layer negative result has explicit form ("the integer topological-index readout requires either an unbounded-truncation limit outside bounded-radius CALM or a non-CALM rounding step; V2's counterexample at the rounding step is unavoidable"). The retreat publication becomes a *better* paper with concrete CALM-side machinery, not just a layer-split observation.

**Q3. Should a separate pool candidate spawn for "Bounded-Variation CALM as a TCS contribution"?**
Recommendation: yes. The 21-persona §S.5 already named this as a pool candidate ("Jordan-decomposed signed-CALM for bounded-variation distributed observables"); this exploration confirms the construction is real and novel. A TCS-side paper at LMCS / Theory of Computing on "Signed-CALM: Jordan-Decomposed Coordination-Free Computation for Bounded-Variation Aggregates" is a genuinely-new TCS direction inspired by the GW-bridge failure and now technically grounded by internal origin artifact. Note: this would be a *separate* publication from the GW-bridge retreat paper, targeting a TCS audience with the GW-bridge use case as one motivating application.

**Q4. Any change to the repo public-surface refresh (internal origin artifact)?**
Recommendation: none beyond the 21-persona meta-verdict's existing recommendation (Option B Sector-I-and-DG-only, not Option A full bundle). The signed-CALM exploration is *local research*; it should not push to repo public surfaces until the internal origin artifact publication-path decision is reopened and the Option II-Retreat paper drafted.

**Q5. Hard rules — confirm no canon writes, no work.json edits, no repo writes.**
Confirmed. This artifact's output is entirely in internal draft artifact. No `Github Repos/` writes. No public push. No canon writes. No work.json edits.

---

## 6. Receipts for the Definition of Done (internal origin artifact artifact body Section: Definition of Done)

- ✓ DoD-1 (Jordan-decomposed signed-CALM stated precisely): `01-jordan-calm-formalization.md` §2 (J1-J4) + §3 (admissibility check for GW axial charge).
- ✓ DoD-2 (V2 counterexample re-test under Jordan): `01-jordan-calm-formalization.md` §4 (case (a) does not recover at integer readout; case (b) recovers at signed-real readout).
- ✓ DoD-3 (Option B precisely stated + ε-bound): `02-option-b-metric-cointegration.md` §2 (B1-B4) with explicit `ε(r) = (C' · a / γ) exp(-γ r / a)`.
- ✓ DoD-4 (bridge-to-GW tested for both frameworks, with explicit handling of instanton/anti-instanton sign cancellation): `03-bridge-to-gw-tests.md` §1-2 + summary table §5.
- ✓ DoD-5 (verdict assigned): this document, §4. PARTIAL — signed-real layer recovers under both, integer-index layer recovers under neither.

---

## 7. Advancement

This artifact advances from **implementation/1 + agent** to **validation/4 + joe + walkthrough_review** with `review_reason: walkthrough_review`. Joe's decision at the walkthrough determines:
- whether the layer-split verdict is accepted as the honest reading;
- whether to reopen internal origin artifact with strengthened Option II-Retreat that includes JD-CALM + AC-CALM machinery;
- whether to spawn a separate TCS-direction pool candidate.

The advancement receipt is appended to the artifact body as v1 (per internal origin artifact artifact body Definition of Done item 5).

---

End of `05-verdict-and-walkthrough-packet.md`.
