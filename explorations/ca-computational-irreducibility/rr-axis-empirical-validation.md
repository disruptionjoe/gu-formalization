---
title: "WRK-395 — rr-Axis Empirical Validation Against Actual CA Behavior"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# WRK-395 — rr-Axis Empirical Validation Against Actual CA Behavior

**Status.** Local-only artifact. WRK-395 implementation/1.
**Generated.** 2026-05-31.
**Companion to.** `ca-class-hypothesis-precise.md`, `gw-axial-charge-ca-recoding.md`.
**Hard rules.** `[speculation]` tagging throughout. No public claims, no canon writes.

---

## 0. Goal

Per DoD item 3: test whether the WRK-390 v3 rr-axis values `{monotone-reducible, signed-BV, phase-cancel, comp-irred}` actually distinguish CA observables. Specifically:

- Are the four values empirically distinguishable for canonical CA observables?
- Does Class-4 CA behavior (Rule 110-style) correspond to `rr = comp-irred`?
- Do reversible CA correspond to a clean signed-BV cell?

The rr-axis was introduced in `v2-rr-axis-formalization.md` as a typing of observables. v2 admitted that two of the four values (`phase-cancel`, `comp-irred`) were `[speculation]`-only — not exercised on concrete cases. WRK-395 exercises them on concrete CA.

---

## 1. Four canonical CA + canonical observables

For each rr-value, find a concrete CA + observable pair and classify by the v2 §3 decision procedure.

### 1.1 Candidate for `rr = monotone-reducible`: G-counter CA / particle-counting

**CA:** Elementary CA over `Σ = {0, 1}` on `Z`, rule "stay" (`f(a_{-1}, a_0, a_1) = a_0`). Trivial dynamics — no rule applies, sites keep their initial states.

**Observable:** `O(s) = Σ_x s_x` (total population).

**Classification:**
- Per-site contribution `s_x` is non-negative (0 or 1).
- Aggregator is `Σ` (additive monoid on `Z_≥0`).
- Monotone in the "more sites turned on" partial order: adding a 1 strictly grows `O`.
- No simulation needed; sum the snapshot.

**Verdict: `rr = monotone-reducible`.** Clean fit. (This is the G-counter CRDT realized as a CA.)

**More interesting `rr = mono-red` instance:** **Rule 18** (XOR-style) — emergent Sierpinski-like fractal structure. Observable `O(s) = max_x density_x` (max-of-locals) is monotone after a single time step (assuming standard partial order on density values). This shows `rr = mono-red` does not require trivial dynamics; it requires a monotone-aggregator-shortcut-able observable.

---

### 1.2 Candidate for `rr = signed-bounded-variation`: number-conserving CA with signed motion

**CA:** **Boccara-Fukś 2002 traffic-flow CA** (Rule 184 / Rule 226). Cells move right if they can; conserved total particle number; signed local flux.

**Observable:** `O(s) = Σ_x j(x, t)` where `j(x, t) = (s_x flowed from x to x+1) − (s_x flowed from x+1 to x)`. This is the **signed net flux**.

**Classification:**
- Per-link contribution `j(x, t)` is signed (positive for rightward flow, negative for leftward; can be 0).
- Aggregator is `Σ` over links — additive but signed.
- Jordan decomposition: `O = O^+ − O^−` where `O^±` are total rightward / leftward flows. Each `O^±` is monotone (you can only add to it, not subtract).
- No simulation needed for `O^±` separately; the subtraction at readout is non-monotone in input-set order.

**Verdict: `rr = signed-bounded-variation`.** Clean fit. (This is the PN-counter CRDT realized as a CA.)

**Number-conserving CA literature confirms** (per Wolfram-search; Boccara-Fukś; Formenti-Pivato; Pivato 2002): such CA admit a "continuity-equation" decomposition `f = move-left + stay + move-right`, with the signed flux as the natural readout. The signed flux IS NOT monotone in input growth but admits clean PN-counter decomposition.

**This matches the GW Q_A recoding exactly** — `Q_A^CA` is a signed-density-sum CA observable that decomposes via PN-counter. The traffic-flow CA is the structural analog at the CA level of the GW physics.

---

### 1.3 Candidate for `rr = phase-cancellation`: complex-valued CA / interference observable

**CA:** Quantum-CA-on-classical-substrate (Wolfram MathWorld; Arrighi-Nesme line of work). Or: a finite Z/4-valued CA where the alphabet `Σ = {1, i, −1, −i}` (4th roots of unity), local rule is multiplication of neighbor values.

**Observable:** `O(s) = |Σ_x s_x · phase(x)|²` where `phase(x)` is a fixed complex phase factor. This is an *intensity* observable from an interferometric sum.

**Classification:**
- Per-site contribution `s_x · phase(x)` is complex-valued.
- Aggregator is `Σ` over `C`.
- Observable is `|sum|²` — not signed-real-decomposable; the magnitude depends on complex interference patterns.
- A signed Jordan decomposition `O = O^+ − O^−` requires splitting into magnitude of positive vs. negative *components*, but the sum's magnitude isn't decomposable that way (cross-terms `Re(s_x · s̄_y · phase(x) · conj(phase(y)))` are signed and depend on phase angle).
- Phase information MUST be propagated; magnitude-only ledger discards the cross-terms.

**Verdict: `rr = phase-cancellation`.** Clean fit, BUT [speculation] the literature on this case is thin. The CA is constructed; the natural physics-side instance is in quantum-CA models (Arrighi-Nesme; D'Ariano-Perinotti). For *classical* CA, the closest analog is probabilistic CA where the "phase" is replaced by stochastic weighting, but those are not pure phase-cancellation systems.

**Honest gap:** `rr = phase-cancellation` is empirically distinguishable from `rr = signed-BV` on the constructed example but the natural-occurrence case is in quantum CA, which is outside WRK-395 scope.

---

### 1.4 Candidate for `rr = computationally-irreducible`: Rule 110 / Game of Life

**CA:** **Rule 110** (Cook 2004, universal one-dimensional elementary CA). Or **Game of Life** (Berlekamp-Conway-Guy 1982, universal two-dimensional CA).

**Observable:** *long-term presence of a specific glider configuration* `O(s_0) = 1` iff `F^t(s_0)` contains pattern `G` at some `t ≤ T_max`, else `0`.

**Classification:**
- The local rule is fixed (Rule 110); the question is whether `O(s_0)` admits any shortcut from `s_0` to the answer.
- By Cook's theorem (Rule 110 is Turing complete) + halting-problem undecidability: there exists no general algorithm that decides `O(s_0)` faster than simulating `F^t(s_0)` for `t = T_max` steps.
- For specific instances `s_0` you might shortcut; for general `s_0`, no shortcut exists.

**Verdict: `rr = computationally-irreducible`** — at the level of general observables on universal CA.

**BUT subtlety:** for *finite* observables on finite lattices, "irreducible" is bounded by the finite-state-machine size. The Wolfram CI notion is asymptotic; on bounded systems, irreducibility is a finite-but-large concern. **For asymptotic / large-system observables on universal CA, `rr = comp-irred` is well-defined and matches the Rule 110 instance.**

**Class-4 / `rr = comp-irred` correspondence: confirmed.** Universal Class-4 CA observables sit at `rr = comp-irred`. Non-universal Class-1 / Class-2 / Class-3 CA may admit shortcuts:

- **Class-1** (uniform attractor, e.g. Rule 0, Rule 8): trivial; observables are `rr = mono-red` (constant function).
- **Class-2** (periodic / fixed-points, e.g. Rule 4): periodic observables admit shortcuts; `rr = mono-red`.
- **Class-3** (chaotic, e.g. Rule 30): statistical observables may be `rr = mono-red` (sampling-based) or `rr = comp-irred` (specific pointwise queries on long-range). Mixed cell.
- **Class-4** (Rule 110, GoL): universal; `rr = comp-irred` for general observables.

---

## 2. Reversible CA: do they correspond to a clean signed-BV cell?

Per DoD item 3 sub-question: "Do reversible CA correspond to a clean signed-BV cell?"

**Answer: not uniformly.** Reversible CA can sit at multiple rr values depending on the observable.

**Reversible CA structural facts (from web search):**
- Reversible CA admit conservation laws (number, parity, momentum) by construction (Margolus-Toffoli; Critters rule).
- Block-CA realization (Margolus neighborhood) is the standard form.
- Inverse rule exists; the system is bijective.

**Per-observable classifications on reversible CA:**

| Observable | rr value |
|---|---|
| Conserved particle number (G-counter style) | `rr = mono-red` |
| Signed conserved current (PN-counter style, e.g. left-minus-right flux) | `rr = signed-BV` |
| Block parity (the discrete Z/2 parity tracker) | `rr = mono-red` (per block) or `rr = signed-BV` (signed alternation) |
| Total energy (when reversible CA carries momentum/energy conservation) | `rr = mono-red` |
| **Pattern recurrence time** ("first t at which initial pattern reappears") | `rr = comp-irred` (if the reversible CA is universal-restricted; reversibility allows complex orbits) |

**Verdict:** reversibility does NOT pin the rr value. Reversibility constrains *dynamics* (bijective global rule, often number-conserving); it does NOT constrain the *readout*. A reversible CA can carry observables at any rr value.

This is a useful negative finding: rr-axis is a property of *(substrate, observable)* pairs, not of the substrate alone.

---

## 3. The four rr values: empirical distinguishability summary

| rr value | Canonical CA + observable | Empirical distinguishability |
|---|---|---|
| `mono-red` | Rule "stay" + total population; Rule 184 + total density | CLEAN (textbook G-counter analog) |
| `signed-BV` | Rule 184 + net flux; GW Q_A via topological-density recoding | CLEAN (textbook PN-counter analog; matches WRK-387) |
| `phase-cancel` | Z/4-valued CA + intensity readout; quantum CA + interferometric observable | DISTINGUISHABLE on constructed examples; natural-occurrence in quantum CA (out of scope) |
| `comp-irred` | Rule 110 + long-term glider-presence; GoL + long-term population query | CLEAN at asymptotic level (Cook 2004 + halting-problem undecidability); subtle on finite systems |

**Verdict on empirical distinguishability:** the four rr values ARE distinguishable as a classification scheme. The boundaries between them are operationally clean on the canonical examples.

**However:** the rr-axis is not provably a *partition* (mutually exclusive + collectively exhaustive). The honest reads:

- `mono-red ∩ signed-BV ≠ ∅` in the trivial sense (any monotone observable is also signed-BV with `O^− = 0`). The decision procedure (`v2-rr-axis-formalization.md` §3) handles this by trying mono-red first.
- `signed-BV ∩ phase-cancel`: a signed-real observable on a complex-valued CA — does it sit at signed-BV (Jordan-decomposable) or phase-cancel (genuinely complex)? Depends on whether the complex structure is essential or just convenient encoding.
- `phase-cancel ∩ comp-irred`: a universal quantum CA observable — can be both genuinely-complex-readout AND comp-irred. The decision procedure tries phase-cancel first; this is a choice, not a forced ordering.
- `comp-irred ∩ (any other)`: comp-irred is "everything that has no shortcut"; if any shortcut exists (mono / signed / phase), the observable is NOT comp-irred. This makes comp-irred *exclusive of the other three* by definition.

The decision procedure's "try more-restrictive first" ordering is a reasonable heuristic but not the only one. Different orderings could classify edge cases differently.

---

## 4. Honest empirical findings

Three findings from running the rr-axis through actual CA cases:

### 4.1 The rr-axis is real but not partition-clean

Three of the four cells (`mono-red`, `signed-BV`, `comp-irred`) have clean canonical instances; one (`phase-cancel`) has a constructed-only instance with natural occurrence only in quantum CA (out of scope).

The four cells are *operationally distinguishable* but *not provably disjoint*. The decision procedure (try most-restrictive first) makes the classification deterministic; with a different ordering, edge cases (signed-real-on-complex-substrate, universal-quantum-CA) could land differently.

### 4.2 Class-4 ↔ `comp-irred` correspondence: confirmed

Rule 110 + general long-term observables → `rr = comp-irred`. Game of Life + long-term population queries → `rr = comp-irred`. The Class-4 = comp-irred correspondence holds at the level of universal CA + general observables.

But: **Class-4 ≠ comp-irred uniformly across all observables.** Specific observables on Rule 110 (e.g., "after one step, what's the cell at site 0") are trivially `mono-red`. The classification is per-observable, not per-rule.

### 4.3 Reversibility doesn't pin rr; the observable does

Reversible CA can carry observables at any rr value. This contradicts a naive reading of "reversible CA correspond to signed-BV"; the correct statement is "reversibility *permits* signed-conservation-law observables that sit at signed-BV, but doesn't force any specific rr value."

This is consistent with the substrate/observable factorization: rr is a property of `(S, O)` pairs.

---

## 5. Implication for rr-axis as classifier

The rr-axis is **a real four-cell classification with empirically-distinguishable canonical instances**. v2's `[speculation]` tag on `phase-cancel` and `comp-irred` can be downgraded to `[speculation, but with constructed-or-asymptotic canonical instance]` after WRK-395 — these cells are not just hypothetical; they have witnesses.

The strong claim "rr-axis is a partition" remains open. The operational claim "rr-axis is a deterministic classification given the decision-procedure ordering" holds on the canonical instances.

For the v3 9-tuple's `rr` element: the WRK-395 empirical validation **strengthens the rr-axis from `[speculation]` to `[constructed and operationally distinguished]`**. It does NOT prove the rr-axis is partition-complete; that's still open.

---

## 6. Honest gaps

- **`rr = phase-cancel` natural-instance gap.** Only quantum-CA instances; out of scope.
- **Decision procedure ordering choice.** "Try most-restrictive first" is a convention; different orderings would reclassify edge cases. Choice is not proven canonical.
- **Finite-system CI subtlety.** The Wolfram CI notion is asymptotic; on bounded systems, "irreducible" is finite-but-large concern. WRK-395 stays at asymptotic level for the comp-irred verdict.
- **No exhaustive Wolfram-class survey.** Class-1/2/3 CA can host observables at multiple rr values; full survey out of scope.
- **No quantitative complexity-class refinement.** The rr-axis is four cells; finer classifications by computational complexity class (e.g., P vs NP vs PSPACE vs decidable vs undecidable) could subdivide each cell but are not pursued.

---

End of `rr-axis-empirical-validation.md`.
