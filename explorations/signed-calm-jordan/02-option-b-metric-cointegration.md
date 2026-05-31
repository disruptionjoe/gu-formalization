---
title: "02 — Option B: Metric Cointegration with ε-Bounded Approximate Consistency"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# 02 — Option B: Metric Cointegration with ε-Bounded Approximate Consistency

**Card:** WRK-396
**Status.** Local-only draft. Generated 2026-05-31.
**Predecessor inputs.** V2's Option B naming (in conversation; not on disk); WRK-387 `extension-formalization.md` §3 (ε-local CALM extension that V2 killed); Bailis et al. "Probabilistically Bounded Staleness" PVLDB 2012; observable-atomic-consistency-for-CvRDTs (arxiv 1802.09462) for the closest published analog.

This document states V2's Option B precisely as a candidate repair, quantifies the ε-bound, and prepares the bridge-to-GW test in `03-bridge-to-gw-tests.md` §2.

---

## 1. The Option B repair as V2 named it

V2 named two repair paths after killing ε-local CALM:

- **Option A — Pure CALM with compactly-supported finite-radius cutoffs.** Drop the exponentially-decaying tail entirely; require strict finite radius `r < ∞`. This makes the truncation exact (no tail beyond radius). The cost: GW physics has exponentially-decaying but *not* strictly-bounded support; a strict-radius cutoff *violates the GW relation* and reintroduces additive chiral-symmetry breaking. Option A trades the CALM-monotonicity gain against the GW-relation loss; the net effect is to reintroduce the very problem GW was designed to solve. We mention Option A only for completeness; the GW-bridge consequence is "Option A fails GW automatically — not a viable repair." This is not the focus of WRK-396.

- **Option B — Metric cointegration with ε-bounded approximate consistency.** Keep the exponentially-decaying support. Replace the *exact* CALM-monotonicity requirement with an *ε-bounded approximate consistency* requirement: distributed replicas agree on the observable's value up to an additive (or relative) ε-bound, where the bound is controlled by a *metric cointegration* between the observable's spatial decay scale and the replicas' coordination radius.

The "cointegration" terminology V2 used has two natural readings:

- **Statistical-econometric reading:** in time-series econometrics, two series `X_t, Y_t` are *cointegrated* if a linear combination `aX_t + bY_t` is stationary even though `X_t` and `Y_t` individually are not. By analogy: two distributed replicas' truncated observable estimates may individually drift, but a metric-weighted combination stays bounded.
- **Topological-spatial reading:** the truncated estimate's error decays with the metric distance from the observation site. "Cointegration" here means the error bound is integrated (in the analysis sense) against the metric, producing a global bound from local-decay assumptions.

`[speculation]` — V2's intended reading is plausibly the topological-spatial one (we are doing local-rule physics on a metric lattice), but Option B is consistent with either reading. We use the topological-spatial reading below.

---

## 2. Option B: precise statement

`[speculation]` — the framework below is constructed here from V2's naming + the standard ε-bounded-staleness CRDT literature lifted to the metric-lattice setting.

**Setup.** Same as JD-CALM in `01-jordan-calm-formalization.md` §2: vertex-transitive graph `G = (V, E)`, graph metric `d`, signed-real-valued aggregate query `Q` with per-site contribution function `q : site × inputs → ℝ` whose influence weight on remote sites satisfies the exponential-decay bound `|w(x, y)| ≤ C exp(-γ d(x,y) / a)` from WRK-387 §3.

**Definition (ε-bounded approximate-consistency CALM, **AC-CALM**).** `Q` is **AC-CALM with metric cointegration** iff there exists a family of truncated queries `{Q_r}_{r ≥ 0}` such that:

**(B1)** **Metric-cointegration bound.** For every site `x` and every input `I`:

> `|Q(x, I) - Q_r(x, I)| ≤ ε(r) := C' · ∫_r^∞ exp(-γ s / a) ds = (C' · a / γ) · exp(-γ r / a)`

i.e., the truncation error at site `x` is bounded by the integrated tail of the influence weight beyond radius `r`. This makes `ε(r)` a *deterministic* function of the truncation radius `r`, decaying exponentially in `r`.

**(B2)** **Per-truncation CALM.** For every fixed `r`, the truncated query `Q_r` is standard-CALM-monotonic in the bounded-radius sense — i.e., `Q_r` admits a coordination-free distributed implementation that converges on every distribution of the input.

**(B3)** **Approximate consistency.** Two replicas computing `Q_r(x, I)` with the same `r` and the same input multiset `I` agree exactly (this follows from standard CALM at fixed `r`). Two replicas computing the full `Q(x, I)` agree up to `2ε(r)` (each may differ from `Q(x, I)` by `ε(r)`).

**(B4)** **Consistency-radius parameter.** The system operator chooses `r` based on a target consistency tolerance `ε_target`: set `r ≥ (a / γ) · log(C' · a / (γ · ε_target))`. Then the replica-level disagreement is bounded by `2 ε_target`.

**The "cointegration" content.** The ε-bound `ε(r)` is *not* an arbitrary parameter — it is determined by the metric integration of the exponential-decay influence weight beyond radius `r`. This couples the consistency tolerance to the *spatial-decay scale* of the underlying physics, making `ε(r)` a *physically-meaningful* quantity (in the GW case: `ε(r)` is bounded by the integrated lattice-side tail of the GW kernel beyond radius `r`).

**Coordination claim** `[speculation]`: an AC-CALM query admits a coordination-free distributed implementation at every fixed `r`, with cross-replica agreement up to `2 ε(r)`. There is no inter-replica coordination during propagation; the consistency tolerance is a system-level parameter, not an emergent property of inter-replica negotiation.

---

## 3. What AC-CALM repairs vs. what it does not

**Repairs:**

- **The truncation-rounding non-linearity V2 named.** Under AC-CALM, the observable's value is a *signed real number with bounded error*, not an integer index produced by rounding. There is no rounding step. The sub-threshold-tail-accumulation failure mode V2 named does *not apply* because there is no threshold-rounding readout: the readout is `Q_r(x, I) ± ε(r)`, a real number with explicit error bar.
- **The propagation-layer claim.** Each per-replica computation at fixed `r` is a strictly-bounded-radius CALM query — directly CALM-realizable by published machinery (Ameloot et al. 2013).
- **The cross-replica consistency claim.** Bounded by `2 ε(r)`, deterministically.

**Does not repair:**

- **The integer-index readout.** If publication requires the readout to be the integer index `n₊ - n₋` (as the index theorem returns), AC-CALM does *not* provide it. AC-CALM provides a real-number readout with explicit error bar. The integer index can only be recovered in the limit `r → ∞` (`ε(r) → 0`), which is *not* a bounded-radius CALM query.
- **The signed-cancellation failure under input growth (WRK-387 P3).** AC-CALM is silent on this: if the truncated `Q_r` includes both an instanton and an anti-instanton, the signed sum can decrease under input growth (adding the anti-instanton to a single-instanton configuration decreases the signed result). AC-CALM does not classify this as a CALM violation only because it is silent on the signed-aggregate semilattice question — it treats `Q_r` as a *real-valued query with bounded error*, where "CALM" is interpreted as the set-monotonicity of contributions, not of the final signed value. **AC-CALM dodges the signed-cancellation question rather than resolving it.**
- **The discrete-topological-invariant structure.** The GW axial charge is an integer (`Σ q_A(x) ∈ ℤ` by Atiyah-Singer). AC-CALM returns a real number with error bar `O(exp(-γ r / a))`. For practical lattice-physics applications this is *useful* (you can choose `r` large enough that the error is well below `1/2` and round to the nearest integer with high confidence). For *theoretical* claims about discrete topological invariants in the abstract `r → ∞` limit, AC-CALM does not directly apply.

---

## 4. Comparison: AC-CALM vs. JD-CALM

| Property | JD-CALM (from `01`) | AC-CALM (this doc) |
|---|---|---|
| What it splits | Sign: positive vs negative contributions | Scale: full vs truncated query |
| Per-component CALM | Yes (per-sign component) | Yes (per fixed radius) |
| Readout | `Q⁺ - Q⁻` exact, signed real or integer | `Q_r ± ε(r)`, signed real with error |
| Handles V2 truncation-rounding | No (case a); Yes (case b ≈ AC-CALM) | Yes (no rounding step) |
| Handles WRK-387 sign-cancellation | Yes, classified as Jordan-aggregate feature | Dodges (silent on signed-aggregate semantics) |
| Bridges to integer-index GW readout | Yes for the per-site density; weaker for global index | No (only in `r → ∞` limit, which isn't CALM) |
| Bridges to signed-real GW readout | Yes | Yes |
| Cost vs. exact CALM | Two streams, subtraction at readout | One stream per `r`, error bar at readout |
| Cost vs. ε-local CALM | Removes rounding via Jordan split | Removes rounding via error-bar readout |

**Observation.** JD-CALM and AC-CALM repair *different* failure modes of ε-local CALM. JD-CALM repairs the signed-cancellation failure (WRK-387 P3) by per-sign splitting. AC-CALM repairs the truncation-rounding failure (V2's counterexample) by replacing the rounded-integer readout with a bounded-error real-valued readout.

**A combined JD+AC-CALM framework** is straightforward to state: split per-sign (JD), then per-radius (AC), giving two parameterized families `{Q⁺_r}, {Q⁻_r}` each per-component CALM, with readout `(Q⁺_r - Q⁻_r) ± 2ε(r)`. This combined framework repairs both failure modes simultaneously, at the cost of a four-way parameterized class (per-sign × per-radius). `[speculation]` — this combined framework is the strongest signed-CALM candidate this exploration surfaces.

---

## 5. Verdict on Option B as a recovery framework

**AC-CALM repairs ε-local CALM's truncation-rounding failure mode cleanly**, at the cost of *abandoning the integer-index readout in favor of a signed-real readout with explicit ε-bound*. The bridge-to-GW consequence depends on what kind of readout the GW bridge claim targets:

- If the bridge targets the *integer index* (the topological invariant from Atiyah-Singer / Hasenfratz-Laliena-Niedermayer 1998): AC-CALM does *not* directly bridge. The integer recovery requires `r → ∞`, which is outside the bounded-radius CALM class.
- If the bridge targets a *signed-real-valued axial-charge density* (the per-site density `q_A(x)`, or its truncated aggregate): AC-CALM bridges cleanly at the approximate level, with bound `2 ε(r)` exponentially decaying in `r`.

**Net verdict on AC-CALM:** RECOVERS at the approximate signed-real-valued level; does NOT directly recover at the integer-index level. Whether this counts as "OPTION B RECOVERS BRIDGE" depends on the publication-grade claim's readout target. The bridge-to-GW consequence is taken up in `03-bridge-to-gw-tests.md` §2.

---

End of `02-option-b-metric-cointegration.md`.
