---
title: "w2(Y14) = pi*w2(X4) — Y14 is Spin iff X4 is Spin (CORRECTION W2-01; the earlier unconditional 'Spin for any orientable X4' is RETRACTED)"
status: canon
doc_type: canon
promoted_from:
  - "explorations/anomaly-and-bordism/n6-w2-y14-gysin-spin-structure-2026-06-22.md"
promoted_at: "2026-06-23"
verdict: CONDITIONALLY_RESOLVED
correction: "W2-01 (2026-06-26) — unconditional spin claim RETRACTED; corrected to: Y14 spin iff X4 spin"
---

# w2(Y14) — Y14 is Spin iff X4 is Spin

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

> **CORRECTION W2-01 (2026-06-26) — headline RETRACTED.** The original unconditional claim ("w2(Y14) = 0 / Y14 spin for any orientable X4, even CP2 / D_gimmel needs no section choice") is **mathematically false**. The Step 3 assembly dropped a `w2(V)` term in the `(R^3 tensor sgn)` factor — an error that the prior CORRECTION MO-02 restated (sub-step 4) rather than caught. The corrected result is **w2(Y14) = pi*w2(X4)**, i.e. **Y14 is spin if and only if X4 is spin**. Orientability (`w1(Y14) = 0`) is unaffected and stays unconditional. Independent check: for any rank-4 bundle E, `w2(Sym^2 E) = w1(E)^2` (Newton identity on the six mixed splitting roots, `e2 = 3 sigma1^2 + 2 sigma2 ≡ w1^2 mod 2`), which is 0 for oriented X4 — so the vertical bundle contributes no w2 to cancel the base obstruction. Title, Scope, Steps 3–4, Result, and Geometric Explanation below are corrected inline; the retracted consequences are flagged. Cascade: `canon/no-go-class-relative-map.md` cites the retracted "spin for any orientable X4 / CP2" premise (see CORRECTION W2-01 cascade note in DERIVATION-PROGRESS.md).

## Scope

Y14 = Met(X4) is the fiber bundle of pointwise Lorentzian metrics over a smooth oriented 4-manifold X4. The corrected claim (see CORRECTION W2-01) is:

```
w1(Y14) = 0            (Y14 is always orientable — unconditional)
w2(Y14) = pi*w2(X4)    (Y14 is spin IFF X4 is spin)
```

Orientability is unconditional, but Y14 inherits the spin obstruction of its base: it is spin when X4 is spin and NON-spin when X4 is non-spin (e.g. X4 = CP2). The canonical Dirac operator D_gimmel is well-defined without a section choice ONLY when X4 is spin; for non-spin X4, a spin (or spin-c) structure must be supplied separately — OPEN.

## Formal Certificate Boundary

```yaml
formal_certificate:
  lean_module: GUFormalization.W2Polynomial
  lean_file: Lean/GUFormalization/W2Polynomial.lean
  certified_theorems:
    - w2Sym2Rank3_eq_e1_sq_add_e2
    - w2TensorLineRank3_eq_e2_add_l_sq
    - vertical_w2_cancels
    - y14_w2_equals_base_when_vertical_zero
  scope: algebraic_F2_splitting_principle_polynomial_identities_only
  does_not_claim:
    - topological_construction_of_stiefel_whitney_classes
    - monodromy_triviality
    - noncompact_index_theory
    - analytic_generation_count
```

## Proof Outline

**Step 1 — Fiber homotopy type.**

The fiber of pi: Y14 -> X4 at x in X4 is the space of Lorentzian inner products on T_x X4:

```
F = GL(4,R) / O(3,1)
```

Via Gram-Schmidt (GL(4,R) ~= O(4)) and Cartan decomposition (O(3,1) ~= O(3) x O(1)):

```
F ~= O(4) / (O(3) x O(1)) ~= S3 / Z2 = RP3
```

RP3 is homotopy equivalent to SO(3), hence a Lie group. Lie groups are parallelizable: T(RP3) ~= RP3 x R3, so w(RP3) = 1 (all SW classes zero on the fiber). `[verified — Gram-Schmidt, Cartan decomposition, Hatcher §3.2]`

**Step 2 — Monodromy triviality (condition, now verified).**

The Serre spectral sequence for RP3 -> Y14 -> X4 requires determining the monodromy of the local system H*(RP3; Z/2) over X4.

The monodromy of H^1(RP3; Z/2) under the GL(4,R) structure group action is trivial. Proof: the tautological line bundle gamma^1 -> RP3 is preserved by any g in GL(4,R): the bundle map phi_{[v]}: lambda·v |-> lambda·gv is a well-defined bundle isomorphism gamma^1 -> g*(gamma^1). Therefore g*(w1(gamma^1)) = w1(gamma^1) = alpha for all g in GL(4,R), and the monodromy on alpha (the generator of H^1(RP3; Z/2)) is trivial. By cup products, all H^q(RP3; Z/2) have trivial monodromy. `[verified — explicit bundle isomorphism; N6 §8.1]`

With untwisted coefficients the Serre spectral sequence gives:
```
H^2(Y14; Z/2) ~= Z/2 oplus H^1(X4; Z/2) oplus H^2(X4; Z/2)
```

**Step 3 — w2(TV) via splitting principle.**

The vertical tangent bundle TV = Pi x_{O(3,1)} Sym^2(R^4) has SW class computed via the decomposition under O(3) x O(1) ~= O(3,1):

```
Sym^2(R^4) = Sym^2_0(R^3) oplus (R^3 tensor sgn) oplus R (relative-trace)
```

where V = R^3 is the spatial subbundle (acted on by the O(3) factor), sgn is the sign representation of O(1) = {±1} (the time-flip factor), and R is the relative-trace direction (trivial under both O(3) and O(1)). Dimensions: 5 + 3 + 1 = 9 (trace-free part) plus 1 (trace) = 10. `[verified — Besse, Einstein Manifolds §1.G; N6 §5.3]`

**Derivation of w2(Sym^2(V)) = w1(V)^2 + w2(V).**

Apply the splitting principle to V = R^3 (a 3-dimensional real vector bundle): formally write V = L1 oplus L2 oplus L3 with formal line bundles Li, w1(Li) = ai in H^1(X4; Z/2). Then:

```
Sym^2(V) = L1^2 oplus L2^2 oplus L3^2 oplus L1 L2 oplus L1 L3 oplus L2 L3
```

Over Z/2, w(Li^2) = 1 because Li^2 = Li tensor Li is a trivial real line bundle (w1(Li tensor Li) = 2 w1(Li) = 0 mod 2). For the mixed terms, w(Li Lj) = 1 + ai + aj. Therefore:

```
w(Sym^2(V)) = prod_{i <= j} w(Li Lj) = (1+a1+a2)(1+a1+a3)(1+a2+a3)
```

Expanding the degree-2 part (over Z/2, all cross-terms a_i a_j appear, and 2 a_i a_j = 0):

```
w2(Sym^2(V)) = a1^2 + a2^2 + a3^2 + a1 a2 + a1 a3 + a2 a3
             = (a1 + a2 + a3)^2 + (a1 a2 + a1 a3 + a2 a3)   [since (sum ai)^2 = sum ai^2 mod 2]
             = e1^2 + e2
             = w1(V)^2 + w2(V)
```

where e1 = w1(V) and e2 = w2(V) are the first and second SW classes of V (the elementary symmetric polynomials in the formal roots a1, a2, a3). `[computation — splitting principle; Milnor-Stasheff, Characteristic Classes, proof of Theorem 7.1; N6 §5.5]`

With w1(X4) = 0 (oriented X4), we have w1(V) = 0 (V is a sub-bundle of TX4 for oriented X4), so:

```
w2(Sym^2(V)) = 0 + w2(V) = w2(V)
```

**Identification w2(V) = w2(X4).** Write TX4 = V oplus L where L is the 1-dimensional time sub-bundle. By the Whitney formula: w(TX4) = w(V) w(L). Since L is a line bundle, w2(L) = 0. For oriented X4, w1(TX4) = 0 forces w1(V) + w1(L) = 0, i.e., w1(L) = 0. Therefore w2(TX4) = w2(V), i.e., w2(V) = w2(X4). `[computation; N6 §5.5]`

**The R^3 tensor sgn factor (CORRECTED — W2-01).** The (R^3 tensor sgn) piece is V tensor L (V = R^3 spatial, L = time line bundle). For a rank-3 bundle V and a line bundle L, w(V tensor L) gives w2(V tensor L) = w2(V) + 2 w1(V) w1(L) + 3 w1(L)^2 = w2(V) + w1(L)^2 (mod 2). The original derivation DROPPED the w2(V) term and wrote only w1(L)^2. With w1(L) = w1(X4) = 0 for oriented X4, the correct value is w2(R^3 tensor sgn) = w2(V) = w2(X4), NOT 0. `[computation — w(V tensor L); Milnor-Stasheff §7]`

**Assembly (CORRECTED — W2-01).** By the Whitney product formula across Sym^2_0(R^4) = Sym^2_0(R^3) oplus (R^3 tensor sgn) oplus R_{rel-trace}, with all factors having w1 = 0 for oriented X4, and using the corrected (R^3 tensor sgn) value:

```
w2(Sym^2(R^4)) = w2(Sym^2_0(R^3)) + w2(R^3 tensor sgn) + w2(R)
               = w2(X4) + w2(X4) + 0
               = 2 w2(X4)
               = 0     (mod 2)
```

Therefore: w2(TV) = 0 in H^2(Y14; Z/2). (Independent check: for any rank-4 bundle E, w2(Sym^2 E) = w1(E)^2 via the Newton identity on the six mixed splitting roots {ti+tj}, since e2 of those roots = 3 sigma1^2 + 2 sigma2 ≡ w1(E)^2 mod 2; for oriented X4 this is 0.) The original assembly used the dropped-term value w2(R^3 tensor sgn) = 0 and concluded w2(TV) = w2(X4); that is the error W2-01 corrects. `[computation; N6 §5.6, corrected]`

**Step 4 — Base obstruction survives (CORRECTED — W2-01).**

From the Whitney product formula w(TY14) = w(TV) · pi*(w(TX4)), using the corrected w2(TV) = 0:

```
w1(Y14) = w1(TV) + pi*(w1(X4)) = pi*(w1(X4)) + pi*(w1(X4)) = 0     (mod 2)   [unaffected]
w2(Y14) = w2(TV) + w1(TV) · pi*(w1(X4)) + pi*(w2(X4))
        = 0 + 0 + pi*(w2(X4))
        = pi*(w2(X4))
```

There is no cancellation: the vertical bundle contributes w2(TV) = 0, so the pullback of the base obstruction survives. Y14 is spin iff w2(X4) = 0, i.e. iff X4 is spin. The original "doubles to zero" conclusion rested on the erroneous w2(TV) = pi*(w2(X4)). `[computation — Whitney product formula; N6 §7, corrected]`

## Result

For any orientable 4-manifold X4:
- Y14 = Met(X4) is orientable (w1 = 0): **unconditional** (correct, unaffected by W2-01).
- w2(Y14) = pi*w2(X4), so **Y14 is spin if and only if X4 is spin** (given the monodromy triviality, verified in Step 2).
- When X4 is NOT spin (e.g. X4 = CP2), Y14 is **NOT spin**. This RETRACTS the original "spin even for CP2 / the metric bundle absorbs the obstruction" claim.
- The canonical Dirac operator D_gimmel is well-defined without a section choice **only when X4 is spin**. For non-spin X4, Y14 is still spin-c (every orientable X4 has W3 = 0), but a U(1) spin-c structure does NOT carry GU's quaternionic index ind_H: the spin-c twist `S tensor_C L^{1/2}` breaks H-linearity and shifts the index off Â(K3) = 2. So **X4 spin is a genuine precondition for GU's generation-count machinery, not a free choice** (resolved as W2-FC1 in DERIVATION-PROGRESS.md; the only structure that could relax it is a quaternionic-compatible Spin^h — and W2-FC2 (2026-06-26) found that although Y14 IS Spin^h for any orientable X4, a non-trivial Sp(1) twist shifts the index off 8·Â(K3)=16, so **Spin^h does NOT relax the X4-spin precondition**; a canonical generation-preserving Spin^h remains OPEN).

## Geometric Explanation (CORRECTED — W2-01)

The fiber RP3 ~= SO(3) is a Lie group (parallelizable), so the fiber itself carries no Stiefel-Whitney classes. But the vertical bundle TV = Sym^2(T*X4) has w2(TV) = w1(X4)^2 = 0 for oriented X4 — it contributes NO w2, so there is nothing to cancel the pulled-back base obstruction pi*w2(X4). The earlier "parallelizable fiber doubles the obstruction to zero" picture was an artifact of the dropped-term error; the metric/Sym^2 structure does not absorb a non-trivial base spin obstruction.

## Assumptions

1. X4 is orientable (w1(X4) = 0). Y14 is always orientable, with or without this; but the spin result uses it for the cross-term simplification.
2. Monodromy triviality of H*(RP3; Z/2) over X4 — verified in Step 2 by explicit bundle isomorphism.

## Known Failure Modes

- **Non-compact index theory.** Y14 = Met(X4) is open (the Lorentzian signature condition is open in Sym^2(T*X4)). Standard compact index theorems do not apply. The spin structure exists when X4 is spin (W2-01 — NOT unconditionally), and even then the analytic index ind_H(D_gimmel) requires a separate Fredholm/APS-type analysis.
- **Generation count.** The spin structure is established; whether the L^2 kernel of D_gimmel has dimension 24 (giving 3 generations) requires the index computation — open.
- **Branching rules.** The computation of s*(S) (SM fermion content from section pullback) remains open.

## What This Does Not Establish

- The analytic index ind_H(D_gimmel) = 24 (i.e., three fermion generations). This is a separate computation requiring Fredholm theory on non-compact Y14.
- Choice of spin structure. w2 = 0 guarantees at least one spin structure exists; if multiple spin structures exist, GU must select one canonically (likely determined by the gimmel metric via the Atiyah-Patodi-Singer boundary condition).

## References

- Milnor, J. and Stasheff, J., Characteristic Classes, Princeton UP, 1974. (Whitney product formula, splitting principle, Theorem 4.5)
- McCleary, J., A User's Guide to Spectral Sequences, Cambridge UP, 2001. §5.2 (Serre spectral sequence for fiber bundles, transgression)
- Besse, A.L., Einstein Manifolds, Springer, 1987. §1.G (Sym^2(T*X) decomposition under O(p,q))
- Hatcher, A., Algebraic Topology, Cambridge UP, 2002. §3.2 (cohomology of RP3)
- Source exploration: N6 w2-y14-gysin-spin-structure-2026-06-22.md (full computation with discipline tags)
