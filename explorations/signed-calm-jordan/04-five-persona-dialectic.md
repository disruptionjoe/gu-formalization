---
title: "04 — Five-Persona Dialectic: JD-CALM and AC-CALM as Bridge Repairs"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# 04 — Five-Persona Dialectic: JD-CALM and AC-CALM as Bridge Repairs

**Card:** WRK-396
**Status.** Local-only draft. Generated 2026-05-31.
**Predecessor inputs.** `01-jordan-calm-formalization.md`, `02-option-b-metric-cointegration.md`, `03-bridge-to-gw-tests.md`; the card body persona seed (five personas: distributed-systems theorist, CRDT specialist, probability theorist, skeptical mathematical physicist, honest-verdict gatekeeper).
**Web-search corroboration.** PN-counter CRDT (Shapiro et al. 2011); Jordan-Hahn decomposition for signed lattice measures (Khare-Singh; orthomodular σ-lattice generalization); CALM theorem (Hellerstein-Alvaro 2020 CACM); approximate-consistency CRDT literature (observable-atomic-consistency for CvRDTs, arxiv 1802.09462; PBS Bailis et al. 2012). No published "signed CALM" or "metric-cointegration CALM" extension found; both JD-CALM and AC-CALM are constructed-here as `[speculation]`.

This document runs the five personas from the card body's seed, then synthesizes their verdict on whether JD-CALM, AC-CALM, or neither RECOVERS BRIDGE.

---

## P1 — Distributed-systems theorist (Hellerstein-school)

### Thesis

JD-CALM and AC-CALM are both *real* distributed-systems primitives in the sense that each maps to a coordination-free distributed implementation. JD-CALM is essentially "PN-counter lifted to signed-real-valued aggregate" — a well-known and reliable CRDT-family construction (PN-counter G-counter `P, N` merge inherits semilattice; lifting from integer increment to bounded-real increment is straightforward). AC-CALM is essentially "bounded-radius CALM at parameterized truncation, with explicit error bound from the influence-weight decay" — also a clean construction.

The hard question is *whether the coordination-free property CALM requires actually holds for these repairs.* For JD-CALM: each `Q⁺` and `Q⁻` is a standard non-negative-real aggregate, and aggregate-CALM at this level is well-established (monotone-aggregate CALM, Laddad et al. 2023). For AC-CALM: each fixed-`r` truncated query is bounded-radius CALM, also well-established. The repairs hold at the propagation layer.

### Antithesis

Both repairs *dodge* rather than *solve* the CALM exclusion that V2 named. CALM's whole point is to characterize *which queries* admit coordination-free realization, and **signed-real-valued queries with thresholded readouts are exactly the queries CALM excludes**. JD-CALM repackages the signed query as two non-negative queries with a final non-CALM subtraction at readout — this is *changing the query*, not satisfying CALM for the original query. AC-CALM repackages the integer-index query as a parameterized real-valued query with bounded error — *also* changing the query.

A purist reading: "neither framework satisfies CALM for the original GW axial-charge integer-index query; both are reformulations to a different (CALM-satisfiable) query." The honest framing is "we restricted scope to the propagation layer and the signed-real readout layer; the integer-index layer is unrepairable."

### Synthesis

The repairs are real *as restatement-and-restrict moves*, not as direct refutations of WRK-387/V2. The distributed-systems content is: **"the GW axial charge admits a coordination-free distributed propagation under JD-CALM or AC-CALM, with the readout layer carrying the cost of either a non-CALM subtraction (JD) or a bounded error bar (AC). The integer-index readout requires either an unbounded `r → ∞` limit or a non-CALM coordination step."**

This is a *useful* and *publishable* characterization. It is *not* a recovery of the WRK-387 strong claim that "GW is in the CALM-monotonic class." It is a *layer-split refinement* that confirms the 21-persona meta-assessment's structural diagnosis.

**Verdict from P1:** RECOVERS at the propagation-and-signed-real-readout layer; NOT at the integer-index layer. The honest publication-grade claim should be the layer-split one.

---

## P2 — CRDT specialist (PN-counter family)

### Thesis

The PN-counter (Shapiro et al. 2011) is *exactly* the discrete-Jordan-decomposed signed-counter CRDT. The natural generalization to signed-real-valued aggregates is straightforward: two `G_sum` (positive-real grow-only sum) CRDTs `P, N`, merge by component-wise max-or-sum (depending on whether contributions are state-based or operation-based), readout `P - N`. This is the JD-CALM primitive in CRDT vocabulary.

The CRDT field has not formally written down "signed-real grow-only-aggregate PN-CRDT" as a named primitive, but the construction is mechanical and the soundness properties follow from the PN-counter soundness. **There is no obstruction to JD-CALM as a CRDT-realizable framework.**

AC-CALM is a different beast — it is a *parameterized* CRDT family, indexed by truncation radius `r`. Each fixed-`r` CRDT is standard (bounded-radius computation, CALM-monotonic at fixed `r`). The cross-replica consistency bound `2 ε(r)` is the closest construction in the literature to "ε-bounded approximate-consistency CRDT" (analog of PBS-style probabilistic-bounded-staleness, but with deterministic decay rather than probabilistic).

### Antithesis

The CRDT literature has *not* produced a "signed-CALM" iff theorem to match the original CALM theorem. PN-counter merge is *not* CALM-monotonic at the signed-value level; it's CALM-monotonic at the (P, N) component level. The Hellerstein-Alvaro CALM theorem statement requires *the query* to be monotone, not the *propagation aggregates*. **Calling JD-CALM "CALM-satisfying" requires either (a) reframing CALM to allow per-component monotonicity with non-CALM readout, or (b) restricting the bridge claim to a per-component substructure.**

The CRDT specialist's honest read: the constructions are real CRDTs; they are *not* witnesses to "GW axial charge satisfies CALM." They are witnesses to "GW axial charge admits a PN-CRDT-style coordination-free implementation with a non-CALM readout step." This is a meaningful and publishable claim but it is not the WRK-387 strong claim recovered.

### Synthesis

The PN-CRDT-style lifting of JD-CALM is real, sound, and exactly the right CRDT primitive for signed-real-valued lattice-aggregate observables. The framework is genuinely novel in the *signed-real-valued GW* application context (PN-counters are widely used for integer counters; lifting to bounded-real signed aggregates with metric-decay influence weights is the new content). AC-CALM is a less-novel construction (closer to existing PBS-style approximate-consistency CRDTs) but is the cleaner match for the *truncation-rounding* failure V2 named.

**Verdict from P2:** The right framing is "JD-CALM gives a PN-CRDT-style coordination-free distributed implementation of the GW signed-real propagation layer; AC-CALM gives the bounded-error readout. Neither directly establishes a 'CALM-monotonic' classification of the integer-index readout."

---

## P3 — Probability theorist (Jordan-Hahn lineage)

### Thesis

The Jordan-Hahn decomposition is the canonical mathematical home for signed measures: every signed measure `μ` decomposes uniquely (up to a common base measure) as `μ = μ⁺ - μ⁻` with `μ⁺, μ⁻` mutually-singular non-negative measures. The decomposition is *constructive* (Hahn decomposition gives a positive-negative partition of the underlying space) and *fundamental* (Vitali-Hahn-Saks convergence theorem for signed measures relies on it).

Lifting Jordan-Hahn to lattice measures is non-trivial but established: Khare-Singh (and earlier Birkhoff lineage) proved Jordan-Hahn decomposition for signed measures on *orthomodular σ-lattices*. The join-semilattice setting we need for CALM is *weaker* than orthomodular σ-lattices (no orthocomplementation required) but the Jordan-Hahn machinery extends.

The application to GW axial charge: `Q_A` is a signed real-valued aggregate over the configuration-space lattice. The per-site density `q_A(x)` is a signed-real-valued function on sites. The pointwise Jordan decomposition `q_A = q⁺ - q⁻` is the canonical Jordan-Hahn move. The integrated index-theorem result `Σ q_A(x) = n₊ - n₋` is the *Atiyah-Singer instance* of Vitali-Hahn-Saks-style convergence to the global topological invariant.

### Antithesis

**Two structural worries.**

First: the Jordan-Hahn decomposition is a *property of the measure* (or the signed-real function), not of any particular *computation* of the measure. JD-CALM's claim is that the decomposition can be *computed coordination-free distributed* — which requires not just that the decomposition exists, but that the sign-classification at each site is a *local* function of inputs. This holds pointwise (`sgn(q_A(x))` is computable from local data) but the *correctness* of the per-site sign relative to the global Jordan-Hahn partition requires more care. In particular, the global Hahn decomposition of `q_A` into positive-set and negative-set on sites may *not* match the pointwise positive-and-negative parts: there can be sites where `q_A(x) > 0` but the integrated measure restricted to that site's neighborhood is signed-negative, and vice versa. **The pointwise Jordan and the Hahn-decomposition Jordan are NOT generally the same.** `[speculation]` for the specific GW case — we have not verified this gap rigorously, but it is a generic feature of signed measures on lattices with non-trivial topology.

Second: the *index theorem* equality `Σ q_A = n₊ - n₋` is not a generic Vitali-Hahn-Saks fact — it is a deep topological fact specific to the Dirac operator's index. The Jordan-decomposition framework does *not* automatically inherit the index-theorem structure; it only inherits the *sign-decomposition* structure. **The integer-index claim requires extra topological input beyond Jordan decomposition.**

### Synthesis

JD-CALM is the right *mathematical home* for the propagation layer of the GW signed-real-valued density. It is *not* a complete framework for the integer-index readout — that requires additional topological structure (Atiyah-Singer / Hasenfratz-Laliena-Niedermayer 1998) that lives one level above Jordan decomposition.

The right convergence theorem to cite (per WRK-394 §19) is *Vitali-Hahn-Saks for signed measures*, with the explicit caveat that the convergence is to a signed-real value; the integer-index readout uses the additional fact that the limit happens to be integer-valued (by Atiyah-Singer).

**Verdict from P3:** JD-CALM gets the *probability-theoretic* framework right. The bridge claim should be stated in *signed-measure language* with explicit Vitali-Hahn-Saks reference. The integer-index claim sits at a separate (topological) level and should not be conflated with the signed-measure-CALM claim.

---

## P4 — Skeptical mathematical physicist

### Thesis

Even granting JD-CALM and AC-CALM as sound distributed-systems repairs, the GW side has *additional structure* that signed-CALM does not capture. Specifically:

- The GW relation `{D, γ_5} = a D γ_5 R D` is the load-bearing algebraic constraint that defines the GW class. **JD-CALM and AC-CALM do not reference the GW relation at all** — they are generic frameworks for signed-real-valued bounded-variation aggregates. The bridge claim, to be GW-specific rather than generic-signed-aggregate, must show how the GW relation *interacts* with the JD-CALM or AC-CALM structure, not just that the signed aggregate satisfies the framework.

- The GW operator has *exact chiral symmetry* in the modified Lüscher sense (lattice-modified chiral transformation `δψ = γ_5(1 - aRD/2)ψ`, `δψ̄ = ψ̄(1 - aRD/2)γ_5`). This exact symmetry is *broken* by sharp-radius truncation (the truncated `R_r D_r` no longer satisfies the GW relation). AC-CALM's fixed-`r` truncation therefore *breaks chiral symmetry* at fixed `r`, with the breaking decaying exponentially as `r → ∞`. **AC-CALM at fixed `r` produces a non-chiral approximation to `Q_A`; the chiral-symmetry-preservation property is only recovered in the unbounded limit.**

- The anomaly content of `Q_A` — the fact that `Σ q_A = n₊ - n₋` carries 't Hooft anomaly information about the chiral symmetry — lives at the *cohomological / SPT-classification* level (per 21-persona §3 Anomaly theorist). JD-CALM and AC-CALM operate at the *observable-aggregate* level. **The anomaly bridge is one categorical level above where the signed-CALM repairs live.**

### Antithesis

The mathematical-physicist skepticism is *fair* but may be over-applied. The bridge claim does not need to capture every aspect of GW; it needs to capture the *characterization-level structural correspondence* (which observables admit local-only realization on a translation-invariant substrate). The 21-persona §1 Lattice QFT theorist's recommendation was "drop CALM-monotonicity as the bridge property; the bridge property is anomaly-matching, not monotone refinement" — but that recommendation was specifically for the *strong* (now-killed) WRK-378 / WRK-388 claims. The WRK-396 exploration is *weaker*: just test whether *some* signed-CALM framework gives a distributed-consistency model that bridges to *some* GW observable.

For the weaker bridge claim — "the signed-real-valued GW axial-charge aggregate admits a JD-CALM / AC-CALM coordination-free distributed implementation, with the integer-index recoverable per-configuration but not uniformly" — the skeptical mathematical physicist's objections are *real* but do *not block* the claim. They block strong / strong-form claims that go beyond what WRK-396 is testing.

### Synthesis

The right claim shape, surviving the mathematical-physicist's skepticism, is:

> "The signed-real-valued axial-charge aggregate `Q_A = Σ q_A(x)` over a finite lattice respecting the GW relation admits a coordination-free distributed implementation under either Jordan-decomposed signed-CALM or metric-cointegration CALM, with the standard caveats: (a) the integer topological index is recovered per-configuration but not uniformly; (b) the GW relation's chiral-symmetry-preservation is preserved exactly only in the unbounded-truncation limit; (c) the anomaly-classification structure lives at a higher categorical level and is not captured by either signed-CALM framework."

This is a *narrow* but *honest* claim. It is the strongest claim the exploration supports.

**Verdict from P4:** JD-CALM and AC-CALM RECOVER a *narrow signed-real-valued propagation-layer bridge* to GW; they do *not* recover the *strong characterization-level bridge* the original WRK-378 / WRK-388 claims attempted. This is consistent with the 21-persona meta-verdict's layer-split framing.

---

## P5 — Honest-verdict gatekeeper

### What is the claim being tested?

Per the WRK-396 card body §3: three possible verdicts —

- **JORDAN-CALM RECOVERS BRIDGE:** signed-readout works; publication path reopens with reframed `(⇐)` direction
- **OPTION B RECOVERS BRIDGE:** metric cointegration gives bounded-error consistency; bridge survives at approximate level
- **NEITHER RECOVERS:** deeper signed-monotonicity obstruction; honest negative result.

The four personas above converge on **a fourth option not in the seed card's verdict list:**

> "BOTH RECOVER PARTIALLY, AT THE PROPAGATION-AND-SIGNED-REAL-READOUT LAYER. NEITHER RECOVERS THE INTEGER-INDEX LAYER."

This is a *layer-split verdict*, consistent with the 21-persona meta-assessment's structural recommendation. The gatekeeper's job is to check whether this fourth option is being smuggled or is honestly load-bearing.

### Smuggling check

**Is the verdict being smuggled by definition?** The JD-CALM and AC-CALM definitions are constructed-here (`[speculation]`). If the definitions were chosen to make the verdict come out positive, the verdict is unreliable.

- JD-CALM definition (`01` §2): essentially "PN-counter lifted to signed-real-valued aggregate with monotone-CALM per-component." This is the canonical construction from the WRK-394 §19 Statistics persona's recommendation and the six-persona dialectic §4 synthesis. **Not constructed to bias toward RECOVERS.** The construction matches Khare-Singh-style signed-lattice-measure Jordan decomposition.
- AC-CALM definition (`02` §2): essentially "fixed-`r` bounded-radius CALM at each truncation, with explicit error bound from influence-weight decay." This is the natural mathematical formalization of V2's Option B as transmitted in conversation. **Not constructed to bias toward RECOVERS.** The construction matches PBS-style approximate-consistency CRDTs.

Neither definition is smuggled. The verdict comes from honest application.

**Is the verdict being smuggled by readout target?** The four personas converge that the bridge survives at the *signed-real readout* level and fails at the *integer-index readout* level. This is a *real distinction*, not a smuggling: integer-index recovery requires either an unbounded-truncation limit (not bounded-radius CALM) or a rounding step (breaks CALM at readout). **Not smuggled — the readout-target distinction is structurally load-bearing.**

**Is the verdict being smuggled away from NEITHER RECOVERS?** The card body §3 named three outcomes; the synthesis above lands on a fourth (BOTH RECOVER PARTIALLY). If the honest verdict were NEITHER, we should land on NEITHER. Let me check: is there a reading under which both JD-CALM and AC-CALM fail the bridge entirely?

- A reading that demands the *integer-index readout* and refuses to accept the *signed-real readout with explicit ε-bound* as a valid GW bridge: under this reading, both frameworks fail → NEITHER RECOVERS. This reading is *defensible* if the publication-grade claim must produce the integer topological invariant directly. It is *not* the only defensible reading.
- A reading that accepts the *signed-real readout* (which is what `q_A(x)` literally is — a signed real number per site) as a valid GW observable: under this reading, both frameworks recover at this level → BOTH RECOVER PARTIALLY. This is the publication-relevant reading if the paper's claim is at the propagation-and-signed-readout layer.

Both readings are honest. The verdict depends on the readout target.

### Honest-verdict synthesis

**The verdict is "BOTH RECOVER AT THE SIGNED-REAL READOUT LEVEL; NEITHER RECOVERS AT THE INTEGER-INDEX READOUT LEVEL."** This is a *layer-split* verdict, not a clean RECOVERS or NEITHER.

**Stronger structural classification by framework:**

- JD-CALM gives the *strongest structural classification* — positively classifies the signed-cancellation phenomenon as a Jordan-aggregate feature (rather than dodging it as AC-CALM does).
- AC-CALM gives the *strongest practical bound* — explicit `2 ε(r)` deterministic cross-replica consistency tolerance, decaying exponentially in `r`.
- Combined JD+AC-CALM gives both, with a four-way parameterized family `{Q⁺_r, Q⁻_r}`.

**Connection to 21-persona meta-verdict:** the layer-split verdict here *confirms* the 21-persona §S.2 issue B (layer conflation surfaced by 5 personas) and §S.4 honest-meta-verdict ("the validators are partially right but missed structural issues B, C, D"). The signed-CALM exploration does not overturn the meta-verdict; it provides the *technical machinery* for the layer-split restatement the meta-verdict recommended.

**What this exploration unlocks for Joe:**

- The propagation-layer bridge claim ("GW signed-real axial-charge aggregate is JD-CALM / AC-CALM") is publishable as a positive layer-split result.
- The integer-index bridge claim does NOT recover under any framework tested.
- The WRK-393 Option II-Retreat publication path (per 21-persona meta-verdict §S.5) is *strengthened* by this exploration: the technical machinery for the propagation-layer positive result and the decision-layer negative result is now JD-CALM + AC-CALM (a publishable contribution in its own right at TCS venues, per WRK-394 §19 Statistics persona's recommendation).

**Verdict from P5:** **PARTIAL RECOVERY AT THE SIGNED-REAL LAYER; NO RECOVERY AT THE INTEGER-INDEX LAYER.** This is a fourth option not in the card body's seed verdict list, and it is the *honest* verdict. The closest of the three seed verdicts is **"OPTION B RECOVERS BRIDGE"** (where Option B is generalized to include JD-CALM) read at the *bounded-error approximate level*; the integer-index extension is dead.

---

## Cross-persona convergence

All five personas converge on:

1. JD-CALM and AC-CALM are real, sound, coordination-free distributed-systems primitives at the propagation layer.
2. The bridge to GW survives at the signed-real-valued readout layer under both.
3. The bridge to GW does NOT survive at the integer-index readout layer under either.
4. The right publication framing is the layer-split one consistent with the 21-persona meta-verdict.

The dialectic *confirms* (rather than overturns) the 21-persona meta-assessment's structural diagnosis. The signed-CALM exploration provides the technical machinery for the layer-split publication, not a recovery of the strong WRK-378 / WRK-388 claims.

---

End of `04-five-persona-dialectic.md`.
