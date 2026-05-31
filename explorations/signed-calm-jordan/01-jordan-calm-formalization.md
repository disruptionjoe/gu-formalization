---
title: "01 — Jordan-Decomposed Signed-CALM: Precise Statement and Counterexample Re-Test"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# 01 — Jordan-Decomposed Signed-CALM: Precise Statement and Counterexample Re-Test

**Card:** WRK-396 (GU Signed-CALM / Jordan Decomposition / Metric Cointegration Exploration)
**Status.** Local-only draft. Generated 2026-05-31 in `work/drafts/wrk-396-signed-calm-jordan-exploration/`.
**Hard rules.** Zero writes to `Github Repos/`. Zero public push. Zero canon writes. Zero work.json edits. `[speculation]` tags throughout for constructed-here content.
**Predecessor inputs.** WRK-387 `extension-formalization.md` §1-5 (ε-local CALM extension definition); WRK-387 `falsification-result.md` (FAILS verdict + counterexample); WRK-394 21-persona §19 Statistics persona (Jordan/Hahn reframe); 2026-05-31 six-persona meta-layer dialectic §4 (signed-measure / PN-counter).

This document states the Jordan-decomposed signed-CALM framework precisely, then re-tests Validator V2's disjoint-state counterexample against it. The verdict is a precondition for the GW-bridge test in `03-bridge-to-gw-tests.md`.

---

## 1. Recap: what V2 killed and why

**V2's counterexample (as transmitted in conversation; not previously on disk):**

> Consider a finite lattice partitioned into two disjoint spatial regions A and B. Place an instanton localized inside A with topological charge `+1`, and an anti-instanton localized inside B with topological charge `-1`. Let `Q_ε` be the ε-truncated axial-charge query from WRK-387 `extension-formalization.md` §3. Choose the truncation radius `r(ε)` small enough that the tails of A's instanton extending into B (and vice versa) lie below the ε-truncation threshold for both A-localized and B-localized observations.
>
> Then:
> - `Q_ε(A) = 0` (the in-A observer's truncated view of A's instanton has cumulative tail energy below the ε threshold for crossing into integer index `±1`; the truncation rounds it down to `0`).
> - `Q_ε(B) = 0` (symmetric).
> - But the actual physics on `A ∪ B` is `Q(A ∪ B) = 0` from the index theorem (instanton + anti-instanton cancel cleanly) — and *if* we set up the truncation differently (say, the two configurations are NOT cancelling but reinforcing, e.g., A and B both contain instantons that individually fall below ε but together cross threshold via cumulative tail energy), we get `Q_ε(A) = Q_ε(B) = 0` while `Q(A ∪ B) = 1`.

The load-bearing failure is **not** the instanton/anti-instanton cancellation (that is a *separate* failure mode covered by WRK-387 `falsification-result.md` §3 P3). The load-bearing failure V2 named is **truncation-induced non-linearity at the integer-rounding threshold**: the ε-truncation `Q_ε` introduces a scale-dependent rounding step `[< ε threshold ↦ 0, ≥ ε threshold ↦ integer]` that destroys the linearity of the join. Sub-threshold contributions in disjoint pieces individually round to 0 but together cross threshold and round to 1, violating join-semilattice monotonicity (`Q_ε(A) ∨ Q_ε(B) = 0 < 1 = Q_ε(A ∪ B)`).

This is V2's structurally important addition to WRK-387's instanton/anti-instanton story. WRK-387 killed CALM via *signed cancellation*; V2 killed it via *truncation rounding non-linearity*. The signed-CALM repair must address **both** failure modes to constitute recovery.

---

## 2. Jordan-decomposed signed-CALM: precise statement

`[speculation]` — the framework below is constructed here from the union of the WRK-394 Statistics-persona recommendation, the six-persona dialectic §4 synthesis, and the standard PN-counter CRDT primitive (Shapiro et al. 2011) lifted to the bounded-variation-aggregate setting. It is not in the published CALM literature.

**Setup.** Let `G = (V, E)` be a vertex-transitive communication graph with graph metric `d`. Let `Q : 2^Inputs → ℝ` be a signed real-valued aggregate query over a distributed input multiset (one input tuple per site, with values in a signed real range).

**Definition (Jordan-decomposed signed-CALM-monotonicity, **JD-CALM**).** `Q` is **JD-CALM** iff there exist two queries `Q⁺, Q⁻ : 2^Inputs → ℝ₊` such that:

**(J1)** **Decomposition.** `Q(I) = Q⁺(I) - Q⁻(I)` for every input set `I`.

**(J2)** **Per-component CALM.** Each of `Q⁺` and `Q⁻` is individually standard-CALM-monotonic in the Hellerstein-Alvaro 2020 / Ameloot et al. 2013 sense over the non-negative-real aggregate semilattice `(ℝ₊, +, ≤)`. Equivalently: `I ⊆ I'` implies `Q⁺(I) ≤ Q⁺(I')` and `Q⁻(I) ≤ Q⁻(I')`.

**(J3)** **Existence and uniqueness on a Jordan-admissible class.** The decomposition `(Q⁺, Q⁻)` exists and is unique up to a common additive non-negative measure (the standard Jordan-Hahn ambiguity, resolved by minimality: take `Q⁺` and `Q⁻` mutually singular). For this to be well-posed the per-site signed contribution function `q : site × inputs → ℝ` must admit a sign-classification rule `sign : site × inputs → {+, -}` that is computable from local data without coordination. We call queries satisfying (J3) **Jordan-admissible**.

**(J4)** **Readout.** The final scalar readout is `Q(I) = Q⁺(I) - Q⁻(I)`, computed via two independent CALM-monotonic aggregations followed by a subtraction at readout time.

**Coordination claim** `[speculation]`: a JD-CALM query admits a coordination-free distributed implementation in the sense that *propagation of `Q⁺` contributions* and *propagation of `Q⁻` contributions* can each proceed without coordination (each is a standard CALM aggregate over a non-negative-real semilattice). Coordination is required *only* at the final readout subtraction, and only in the sense that the readout must wait for both `Q⁺` and `Q⁻` aggregates to be settled at the read site — there is no inter-site coordination during propagation.

**Architectural analog.** This is the lifted-to-real-valued generalization of the PN-counter CRDT (Shapiro et al. 2011): two independent G-counters, one for positive contributions and one for negative, with the readout `value = P - N`. JD-CALM extends this from integer-counter aggregates to signed-real-aggregate queries by requiring per-component CALM rather than per-component G-counter structure.

---

## 3. Critical pre-test: does Jordan-admissibility hold for the GW axial charge?

Before re-testing V2's counterexample under JD-CALM, we must check whether the GW axial charge is *Jordan-admissible* in the sense of (J3). This is the load-bearing applicability question.

The per-site axial-charge density at site `x` in the GW formalism is

> `q_A(x) = ψ̄_x γ_5 (1 - a R D)_{xx} ψ_x`

This is a signed real number. The sign of `q_A(x)` depends on the local fermion bilinear and the local value of the GW kernel `(1 - a R D)_{xx}`, which depends on the gauge field in an exponentially-decaying neighborhood of `x`.

**Question:** can we write `q_A(x) = q⁺(x) - q⁻(x)` with `q⁺(x), q⁻(x) ≥ 0` *and* with a sign-classification `sign(x, I)` computable from local data without coordination?

**Answer:** Yes, trivially in the per-site sense: `q⁺(x) = max(q_A(x), 0)`, `q⁻(x) = max(-q_A(x), 0)`. This is the standard pointwise Jordan-Hahn decomposition of a signed real function. The sign-classification `sign(x, I) = sgn(q_A(x))` is a pure local function of the gauge field in the exponentially-decaying neighborhood of `x`, so it satisfies (J3) at fixed gauge configuration.

**However** — and this is the load-bearing subtlety — the *integrated* index theorem gives `Σ_x q_A(x) = index(D) = n₊ - n₋` where `n₊` and `n₋` are the *global* counts of positive- and negative-chirality zero modes of the Dirac operator. The Jordan decomposition `q_A = q⁺ - q⁻` at the per-site level does *not* match the global `(n₊, n₋)` chirality decomposition: a single zero mode contributes to `q_A(x)` at every site `x` in its spatial support, with a sign that depends on the *interference pattern* of the mode wavefunction with the gauge background at `x`, not on the mode's global chirality.

This means there are **two distinct Jordan decompositions in play:**

- **Local Jordan decomposition** `(q⁺, q⁻)_local`: per-site pointwise positive and negative parts of `q_A(x)`. Trivially Jordan-admissible. Gives the per-site signed-real-valued aggregate the JD-CALM structure.
- **Global chirality decomposition** `(n₊, n₋)`: counts of positive- and negative-chirality zero modes globally. Each `n_+` and `n_-` is non-negative and equals `dim ker D|_{γ_5 = ±1}`. These are global topological invariants.

The index theorem says `Σ_x q_A(x) = n₊ - n₋`. But the per-site Jordan decomposition `(q⁺, q⁻)_local` does *not* sum to `(n₊, n₋)`: it sums to `(Σ_x q⁺(x), Σ_x q⁻(x))`, which is generically *larger* than `(n₊, n₋)` in absolute terms because of internal cancellation within the support of each zero mode (parts of one mode contribute positively to `q⁺` and negatively to `q⁻` at different sites; only the integrated signed sum gives the index).

`[speculation]` — this is the constructed-here observation that the local Jordan decomposition over-counts; the equality `Σ q⁺ - Σ q⁻ = n₊ - n₋` holds but neither `Σ q⁺ = n₊` nor `Σ q⁻ = n₋` holds in general.

---

## 4. Re-test of V2's counterexample under JD-CALM

We re-test V2's counterexample (§1) using the local Jordan decomposition `(q⁺, q⁻)_local`.

**Setup.** Disjoint regions A and B. Configuration is chosen so that the truncation-rounding failure mode applies: the per-site contributions in A and the per-site contributions in B individually fall below the ε-rounding threshold of the original `Q_ε`, but cumulative tails cross threshold in the union.

**Apply JD-CALM:**

- `Q⁺_ε(A) = Σ_{x ∈ A} q⁺(x)` truncated to radius `r(ε)`. This is a non-negative-real CALM aggregate.
- `Q⁻_ε(A) = Σ_{x ∈ A} q⁻(x)` truncated to radius `r(ε)`. This is a non-negative-real CALM aggregate.
- `Q_ε(A) = Q⁺_ε(A) - Q⁻_ε(A)`.

**The critical question.** Does the truncation-rounding non-linearity that broke ε-local CALM persist when applied per-component?

**Two cases:**

**Case (a) — V2's framing read as "the integer-rounding step is part of `Q_ε`":** under this reading, `Q_ε` includes a final rounding step `round_ε : ℝ → ℤ` that maps real-valued aggregates to integer indices, with the rule `|x| < ε ↦ 0, |x| ≥ ε ↦ sgn(x) · ⌈|x|⌉`. The JD-CALM repair *does not address this rounding step* — it only restructures the propagation as two non-negative streams. If the rounding is applied to the readout `Q_ε(A) = Q⁺_ε(A) - Q⁻_ε(A)`, then sub-threshold values in A and B individually rounding to 0 while their union's signed difference crosses threshold *still violates join-semilattice monotonicity at the readout level*. **JD-CALM does not recover.**

**Case (b) — V2's framing read as "the truncation introduces sub-threshold tail energies that accumulate non-linearly":** under this reading, the failure is that the *truncation radius* `r(ε)` cuts off tail contributions that individually are below `ε` but cumulatively cross threshold. The JD-CALM repair *partially addresses this*: each per-component aggregate `Q⁺_ε`, `Q⁻_ε` is now a positive-real sum, and positive-real sums *are* join-monotone (more terms ⇒ larger sum). The truncation-cumulative-tail effect is no longer rounding-induced — it's a genuine approximation error in the per-component aggregates. **In this reading, JD-CALM gives per-component CALM cleanly**, and the join-semilattice violation of the original `Q_ε` dissolves into an *approximation-error bound* on the readout subtraction: `|Q_ε(I) - Q(I)| ≤ |Q⁺_ε(I) - Q⁺(I)| + |Q⁻_ε(I) - Q⁻(I)|`, which is `O(ε)` in the per-component approximation bound.

**Honest reading.** V2's counterexample as transmitted in conversation is ambiguous between (a) and (b). The strongest reading — which V2 plausibly intended given the "actual physics `Q(A∪B) = 1`" framing that implies an integer index readout — is **case (a)**. Under case (a), **JD-CALM does NOT recover**, because the rounding-induced non-linearity at the readout is orthogonal to the propagation-layer Jordan split.

The weakest reading — case (b) — gives JD-CALM a clean recovery at the cost of *abandoning the integer-index readout in favor of an approximate signed-real readout with bounded error*. This is the same scope as Option B (metric cointegration), addressed in `02-option-b-metric-cointegration.md`.

---

## 5. Secondary obstruction: WRK-387's instanton/anti-instanton failure under JD-CALM

WRK-387 `falsification-result.md` §3 P3 named a *separate* failure mode: a strictly larger gauge input (add an anti-instanton at distance) produces a strictly smaller signed readout (`Q_A: 1 → 0`).

**Does JD-CALM address this?**

Per the per-site local Jordan decomposition: adding an anti-instanton at distance increases the gauge-field input set. The per-site contributions `q⁺(x)` and `q⁻(x)` at sites *inside* the original instanton's support are essentially unchanged (the anti-instanton is at distance and its contribution decays exponentially). At sites *inside* the new anti-instanton's support, new positive contributions to `q⁻(x)` appear (the anti-instanton's chiral mode has negative contribution to `q_A`, hence positive contribution to `q⁻`). So `Q⁻(I)` strictly *grows* under input growth. Meanwhile `Q⁺(I)` also grows (very slightly, from cross-talk tails) but the gross effect is that `Q⁻` grows by ~1 unit. Then `Q(I) = Q⁺ - Q⁻` decreases.

**Does this violate JD-CALM?** No! JD-CALM only requires `Q⁺` and `Q⁻` individually to grow under input growth. Both do. The *signed difference* `Q⁺ - Q⁻` decreasing is *not* a CALM violation under JD-CALM — it's the expected behavior of a Jordan-decomposed signed aggregate, exactly analogous to how a PN-counter's signed value can decrease under input growth even though both `P` and `N` only grow.

**This is the structural win of JD-CALM over ε-local CALM**: it correctly classifies signed-cancellation observables as "propagation-CALM, readout-non-monotone" rather than as "non-CALM full stop." The signed-real-valued aggregate is *exactly* in the bounded-variation-aggregate class that JD-CALM is designed to capture.

---

## 6. Verdict on §3 + §4 (JD-CALM applicability + counterexample re-test)

**JD-CALM applicability to GW axial charge (J1-J4 check):**

- **(J1) Decomposition:** YES, via local Jordan decomposition `q_A(x) = q⁺(x) - q⁻(x)`.
- **(J2) Per-component CALM:** YES, in the *propagation* sense — each per-site non-negative contribution accumulates monotonically under input growth.
- **(J3) Jordan-admissibility:** YES, at the per-site pointwise level (sign classification is local). NOT at the global-chirality level (which is the topological invariant the index theorem returns).
- **(J4) Readout:** YES, signed-real readout `Q⁺ - Q⁻` is well-defined.

**Counterexample re-test outcomes:**

- **V2 counterexample under case (a) reading (integer-index readout with rounding):** JD-CALM **does not recover**. The rounding non-linearity at readout is orthogonal to the per-component CALM propagation.
- **V2 counterexample under case (b) reading (signed-real readout with bounded approximation error):** JD-CALM **recovers cleanly**. Per-component truncation errors compose additively at the readout.
- **WRK-387 instanton/anti-instanton failure:** JD-CALM **handles cleanly** — signed-readout decrease under input growth is correctly classified as a feature of the Jordan-decomposed-signed-aggregate class, not as a CALM violation.

**Net verdict on JD-CALM as a recovery framework for GW axial charge:**

`[speculation, this draft's read]` JD-CALM is a real and structurally-correct repair for the *signed-cancellation* failure mode WRK-387 named (instanton/anti-instanton). It is *not* a repair for the *truncation-rounding* failure mode V2 named, when the readout is the integer index. Whether this counts as "RECOVERS" depends on whether the publication-grade claim targets the integer-index readout (does not recover) or a signed-real readout with explicit approximation bound (recovers, but bridges to GW only at the approximate level).

The bridge-to-GW consequence is taken up in `03-bridge-to-gw-tests.md` §1.

---

End of `01-jordan-calm-formalization.md`.
