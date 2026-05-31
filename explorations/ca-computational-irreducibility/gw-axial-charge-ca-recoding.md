---
title: "WRK-395 — GW Axial Charge Q_A: Recoding as a CA-Class Projected Invariant"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# WRK-395 — GW Axial Charge Q_A: Recoding as a CA-Class Projected Invariant

**Status.** Local-only artifact. WRK-395 implementation/1.
**Generated.** 2026-05-31.
**Companion to.** `ca-class-hypothesis-precise.md`, `rr-axis-empirical-validation.md`.
**Hard rules.** `[speculation]` tagging throughout. No public claims, no canon writes.

---

## 0. Goal

Per DoD item 2: for the GW axial-charge query `Q_A` (the WRK-387 canonical counterexample), (i) find the smallest local CA alphabet + neighborhood that can propagate signed/chiral contribution data, and (ii) determine whether the readout is computationally reducible (admits monotone shortcut) or irreducible (requires running the evolution).

The verdict will feed both the rr-axis test and the CI-vs-BvN structural verdict.

---

## 1. What `Q_A` is, in CA-class translatable terms

The GW axial charge, from WRK-387 §2 and `query-formalization.md`:

```
Q_A = Σ_x ψ̄_x γ_5 (1 - aRD)_{xx} ψ_x
```

with `D` the Ginsparg-Wilson Dirac operator satisfying `{D, γ_5} = a D γ_5 R D`. The per-site density is signed; the canonical falsifier is an instanton/anti-instanton pair where `Q_A: 1 → 0` as gauge input grows.

**Atiyah-Singer / Hasenfratz-Laliena-Niedermayer 1998 fact:** on a GW lattice with a smooth-enough gauge background, `Q_A = n_+ − n_−` where `n_±` are the numbers of zero modes of the GW Dirac operator with chirality `±` (the discrete index). The index `(n_+ − n_−)` equals the topological charge `Q_top = (1/32π²) ∫ tr(F ∧ F̃)` of the underlying gauge configuration (lattice version).

So at the *physics* level, `Q_A` is computed by:

1. Take a gauge configuration `U` (the input).
2. Compute the GW Dirac operator `D(U)`.
3. Find its zero modes and their chirality.
4. Output `n_+ − n_−`.

This is a four-step pipeline. The question is whether any subset of these steps admits a CA-class local-rule recoding, and whether the final readout admits a shortcut.

---

## 2. The recoding attempt — what CA-class can carry

**[speculation, construction-here]**

The minimal CA-class substrate that can carry signed chiral contribution data:

### 2.1 Alphabet

`Σ = {±1, 0} × G_gauge_link` where:

- `±1` represents per-site chirality eigenvalue (positive/negative chirality projection eigenvalue of `(1 − aRD)_{xx}` at site `x`, in a basis where it's diagonal).
- `0` represents non-zero-mode sites (vast majority).
- `G_gauge_link` represents the per-link gauge group element (typically SU(2) or SU(3); finite-discretized for CA purposes — e.g., `Z/N` for an N-step discretization).

So `Σ = {±1, 0} × G_disc` with `|Σ| = 3 · |G_disc|`. For `G_disc = Z/8`, `|Σ| = 24`. **This is a small finite local alphabet.**

### 2.2 Neighborhood

For lattice fermions in d-dimensions with a GW operator of locality range `r`, the local rule needs neighborhood `N = {x : |x| ≤ r}` (the GW operator is exponentially-local but its near-locality range determines the CA neighborhood). For Neuberger's overlap operator on standard backgrounds, `r ≈ 2-3` lattice sites is the operational locality scale (HJL 1999 form).

So `N` is a finite ball of radius `~3` in `Z^d`. This is a **standard CA neighborhood**.

### 2.3 Local update

The local update `f : Σ^N → Σ` computes the per-site chirality eigenvalue from local gauge data. The chirality projector `P_± = (1 ± γ_5(1 − aRD))/2` acts on local fermion modes; the local rule determines which sites are zero-mode-host sites and what chirality they have.

**This is the load-bearing recoding question:** can the chirality eigenvalue at site `x` be computed from a finite neighborhood `N` of gauge data alone?

**Answer (partial, [speculation]):** *not directly*. The GW operator's zero modes are *globally-correlated* eigenstates of `D(U)`, and a single-site chirality assignment requires solving the global eigenvalue problem. The local rule can compute the *operator matrix element* `(1 − aRD)_{xx}` from local data, but the **zero-mode chirality assignment is non-local**.

**However:** the Atiyah-Singer index `n_+ − n_−` is *topological*, meaning it depends only on the gauge configuration's homotopy class, which **can** be computed from local field-strength data integrated over the lattice. The relevant local invariant is the per-cell topological charge density `q_top(x) = (1/32π²) tr(F_μν F̃_μν)(x)`, which IS a finite-neighborhood function of gauge data.

So the recoding splits into two sub-cases:

**Sub-case A: chirality-eigenvalue per-site readout** — **NOT CA-class encodable at finite locality**. Requires solving global eigenvalue problem; only emerges after running global evolution.

**Sub-case B: topological-charge density readout** — **IS CA-class encodable**. `q_top(x)` is a local rule output (a polynomial in local gauge field-strength components), and `Q_top = Σ_x q_top(x)` is the aggregator. By the Atiyah-Singer / HLN 1998 index theorem, `Q_A = Q_top` on smooth-enough backgrounds.

### 2.4 The recoded observable

Take the CA-class observable:

```
Q_A^CA(U) = Σ_x q_top(x; U|_N(x))
```

where `q_top(x; U|_N(x))` is the local topological charge density computed from gauge data in neighborhood `N(x)`. This is a **CA-class projected invariant**: local rule output, signed per-site density, sum-aggregation over sites.

**Verdict:** the recoding works at the topological-density level. It captures `Q_A` on smooth (admissible) gauge backgrounds where the index theorem applies. On non-smooth or rough configurations the recoding can drift from the eigenvalue-based `Q_A` definition (HJL 1999 admissibility bound).

---

## 3. Is the recoded observable computationally reducible?

The recoded `Q_A^CA(U) = Σ_x q_top(x; U|_N(x))` has the form:

- per-site signed density `q_top(x)` ∈ R
- finite-neighborhood local rule
- additive aggregation `Σ_x`

This is NOT `rr = monotone-reducible`. The per-site density is signed; adding gauge configuration components (anti-instanton next to instanton) decreases the aggregate. The instanton/anti-instanton cancellation works exactly the same way as in the original `Q_A` — adding the anti-instanton produces a negative `q_top` contribution that cancels the instanton's positive contribution.

It IS `rr = signed-bounded-variation`:

- Decompose `q_top(x) = q_top^+(x) − q_top^−(x)` with `q_top^±(x) = max(±q_top(x), 0)`.
- Each `Q_A^{CA,±} = Σ_x q_top^±(x)` is monotone (G-counter / non-negative aggregate).
- The readout is `Q_A^CA = Q_A^{CA,+} − Q_A^{CA,−}`, which is PN-counter / Jordan-decomposition.

**This is the *exact* WRK-387 finding, reproduced at the CA-class substrate level.** The recoding does NOT escape the signed-BV character of `Q_A`; it makes the signed-BV character a property of the local rule (the topological-density formula is intrinsically signed), not an artifact of the GW operator's spectral properties.

It is NOT `rr = phase-cancellation` — the local rule does not require complex phase data to compute `q_top(x)`; field-strength tensor components are real-valued.

It is NOT `rr = computationally-irreducible` — `Q_A^CA(U)` admits the PN-counter shortcut. Once you have the gauge configuration, you can compute it without simulating any non-trivial CA evolution; it's a sum-of-locals over the static configuration.

**Recoding verdict: `Q_A` is CA-class projected, `rr = signed-bounded-variation`, computationally reducible to PN-counter.**

---

## 4. What does the recoding tell us?

Three findings, each load-bearing for the final verdict.

### 4.1 The recoding is faithful but does NOT change the rr value

The CA-class recoding preserves the signed-BV character of `Q_A`. WRK-387's CALM-falsification verdict is *not* dissolved by moving to CA-class; it is *reproduced* as a feature of the topological-density local rule.

**Implication:** the rr-axis is substrate-stable. Whether you formulate `Q_A` as a GW-Dirac-spectral-trace (the v1/v2/v2.1 formulation) or as a topological-charge-density CA observable (this section), it lives in the same `rr = signed-BV` cell.

### 4.2 The eigenvalue-based readout has a deeper obstruction

Sub-case A (chirality-eigenvalue per-site readout) is *not* CA-class encodable at finite locality. The eigenvalue assignment requires solving a global eigenvalue problem on the GW Dirac operator. This is a **non-finite-locality** observable — the per-site value depends on the entire gauge configuration, not just a finite neighborhood.

Two ways to read this:

**Reading A1 (`[speculation]`):** the eigenvalue-based readout is *computationally irreducible* in the Wolfram sense — there's no local-rule shortcut; you have to "run" (solve) the global eigenvalue problem. This would put the original `Q_A` (as eigenvalue trace) at `rr = comp-irred` and the recoded `Q_A^CA` (as topological density) at `rr = signed-BV`. The Atiyah-Singer index theorem is then *the shortcut* that reduces comp-irred to signed-BV.

**Reading A2 (`[speculation]`):** the eigenvalue-based readout is *finitely-non-local but algebraically reducible* — you can compute it by diagonalizing a finite (though potentially large) matrix in finite time. This is "irreducible in the polynomial-time sense" but reducible in the Turing-computability sense. The Wolfram CI notion requires more (the lack of *any* shortcut, including time-polynomial ones); the matrix-diagonalization shortcut, even if expensive, prevents A1's strong CI claim.

**Honest reading:** Reading A2 is more defensible. The chirality eigenvalues of a finite GW Dirac operator are computable in polynomial time (essentially `O((vol)^3)` for matrix diagonalization). The Wolfram CI notion requires that *no* shortcut exists, which is not the case here. So `Q_A` as eigenvalue trace is **finitely-non-local but reducible**, not computationally irreducible.

The Atiyah-Singer index theorem gives a *faster* shortcut (local topological density sum), but the eigenvalue computation isn't *irreducible* — it's just slower.

### 4.3 The structural insight: index theorems are computational reducibility witnesses

This is the most interesting finding of the recoding. **The Atiyah-Singer index theorem is, in CA-class vocabulary, a statement that the topological invariant `n_+ − n_−` (which a priori requires solving a global eigenvalue problem) admits a local-rule shortcut (the topological charge density sum).** It is the *reducibility theorem* that takes `Q_A` from "non-local global trace" to "sum of local topological densities."

In rr-axis vocabulary: the index theorem moves `Q_A` from "non-local readout, naively non-reducible" to "`rr = signed-BV` via per-site topological density." It is a *categorical-level shortcut* that turns a global readout into a CA-class observable.

**[speculation]** This suggests a broader pattern: *every classical topological invariant of a gauge field that admits an integral-density formula is CA-class reducible to signed-BV.* The signed-BV character comes from the topological density being signed (it changes sign under orientation reversal / parity). The "monotone shortcut" exists at the level of positive and negative variations separately, but not at the signed-aggregate level.

---

## 5. Honest gaps

- **[speculation]** The recoding is at the *index-density* level, which is valid for smooth (admissible) gauge configurations. Rough configurations may violate the locality assumption (HJL 1999); the recoding fails there. WRK-395 does not characterize the boundary precisely.
- **[speculation]** The Atiyah-Singer index theorem is not provably valid on all GW-modified lattices; the HLN 1998 form is the canonical case. Generalized GW operators may have weaker index theorems.
- **No exhaustive treatment of non-abelian gauge groups.** The discretization `G_disc = Z/N` is a placeholder; SU(3) with finite-precision link variables is a real practical question for CA implementation but does not change the rr-axis verdict.
- **No quantum-CA generalization.** The recoding is classical; quantum CA (Heunen-Reyes) may allow finer reducibility classifications. Out of scope.
- **[speculation]** Reading A2's "polynomial-time reducible vs Wolfram-CI irreducible" boundary is itself imprecise. The strict Wolfram CI notion requires no shortcut of *any* kind; finite-volume matrix problems always have *some* shortcut (compute in finite time). The CI/reducible boundary may be ill-defined for finite-system observables — see `ci-vs-bvn-structural-verdict.md` §4.

---

## 6. Summary

| Item | Verdict |
|---|---|
| Minimum CA alphabet | `Σ = {±1, 0} × G_disc` (e.g. `\|Σ\| = 24` for `G_disc = Z/8`) |
| Minimum CA neighborhood | `N = ball of radius ~3` in `Z^d` |
| Recoding-at-topological-density level | WORKS for smooth (admissible) backgrounds |
| Recoding-at-eigenvalue level | requires non-finite locality; doesn't fit CA at finite radius |
| rr value of recoded observable | `rr = signed-bounded-variation` |
| Computational reducibility | REDUCIBLE (PN-counter / Jordan decomposition) |
| Substrate-stability of rr-axis | CONFIRMED (matches WRK-387 spectral-trace verdict) |
| Atiyah-Singer index theorem (reframed) | "topological invariants admit local-density shortcut" → `rr = signed-BV` reducibility theorem |

End of `gw-axial-charge-ca-recoding.md`.
