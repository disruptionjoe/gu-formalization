---
title: "w2(Y14) = 0 — Y14 is Spin for Any Orientable X4"
status: canon
doc_type: canon
promoted_from:
  - "explorations/n6-w2-y14-gysin-spin-structure-2026-06-22.md"
promoted_at: "2026-06-23"
verdict: RESOLVED
---

# w2(Y14) = 0 — Y14 is Spin for Any Orientable X4

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

## Scope

Y14 = Met(X4) is the fiber bundle of pointwise Lorentzian metrics over a smooth oriented 4-manifold X4. The claim is:

```
w1(Y14) = 0     (Y14 is always orientable)
w2(Y14) = 0     (Y14 is always spin)
```

for any orientable X4, without any assumption that X4 itself is spin. This implies the canonical Dirac operator D_gimmel on Y14 is well-defined without any section choice.

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

**The R^3 tensor sgn factor.** From TX4 = V oplus L and the decomposition Sym^2(R^4) above, the (R^3 tensor sgn) piece has w1 = w1(V) + w1(L) = 0 + w1(X4) = 0 for oriented X4, and w2(R^3 tensor sgn) = w1(L)^2 = w1(X4)^2 = 0 for oriented X4. `[computation; N6 §5.3]`

**Assembly.** By the Whitney product formula applied to Sym^2_0(R^4) = Sym^2_0(R^3) oplus (R^3 tensor sgn) oplus R_{rel-trace}, with all three factors having w1 = 0 for oriented X4:

```
w2(Sym^2(R^4)) = w2(Sym^2_0(R^3)) + w2(R^3 tensor sgn) + w2(R)
               = w2(V) + 0 + 0
               = w2(X4)
```

Therefore: w2(TV) = pi*(w2(X4)) as a class in H^2(Y14; Z/2). `[computation — Whitney product formula; N6 §5.6]`

**Step 4 — Cancellation.**

From the Whitney product formula w(TY14) = w(TV) · pi*(w(TX4)):

```
w1(Y14) = w1(TV) + pi*(w1(X4)) = pi*(w1(X4)) + pi*(w1(X4)) = 0     (mod 2)
w2(Y14) = w2(TV) + w1(TV) · pi*(w1(X4)) + pi*(w2(X4))
        = pi*(w2(X4)) + 0 + pi*(w2(X4))
        = 2 · pi*(w2(X4))
        = 0     (mod 2)
```

The contribution from the vertical bundle (which inherits w2 from the squared-TX structure of the fiber) cancels the pullback of the base obstruction over Z/2. `[computation — Whitney product formula; N6 §7]`

## Result

For any orientable 4-manifold X4:
- Y14 = Met(X4) is orientable (w1 = 0): unconditional.
- Y14 is spin (w2 = 0): unconditional (given the monodromy triviality, verified in Step 2).
- Y14 is spin even when X4 is NOT spin (e.g., X4 = CP2): the metric bundle "absorbs" the spin obstruction.
- The canonical Dirac operator D_gimmel on Y14 is well-defined for any orientable X4, without any section choice.

## Geometric Explanation

The fiber RP3 ~= SO(3) is a Lie group (parallelizable). It provides exactly the topological correction to cancel the spin obstruction from the base: the vertical bundle TV inherits a w2 equal to pi*(w2(X4)), and this doubles to zero over Z/2.

## Assumptions

1. X4 is orientable (w1(X4) = 0). Y14 is always orientable, with or without this; but the spin result uses it for the cross-term simplification.
2. Monodromy triviality of H*(RP3; Z/2) over X4 — verified in Step 2 by explicit bundle isomorphism.

## Known Failure Modes

- **Non-compact index theory.** Y14 = Met(X4) is open (the Lorentzian signature condition is open in Sym^2(T*X4)). Standard compact index theorems do not apply. The spin structure exists (established here), but the analytic index ind_H(D_gimmel) requires a separate Fredholm/APS-type analysis.
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
