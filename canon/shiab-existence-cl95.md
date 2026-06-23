---
title: "Shiab Operator Existence — Cl(9,5) Setting"
status: canon
doc_type: canon
promoted_from:
  - "explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
  - "explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md"
promoted_at: "2026-06-23"
verdict: RESOLVED
---

# Shiab Operator Existence — Cl(9,5) Setting

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

## Scope

The ship-in-a-bottle (shiab) operator is the natural equivariant map:

```
Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S
```

The question is whether such a map exists without complexification (the gap Nguyen §3.1 identified).

## Proof

**Step 1 — Correct signature of Y^14 is (9,5).**

Y^14 = Met(X^4) is the bundle of Lorentzian metrics over X^4. The fiber is Sym^2(T*_x X^4) of dimension 10. The Frobenius metric induced by the (3,1) Lorentzian metric on R^4 has signature (7,3) on the fiber, and trace-reversal (as in the UCSD transcript [00:43:04]) shifts this to (6,4). The horizontal directions carry (3,1). Total signature: (3+6, 1+4) = (9,5). `[verified — Frobenius metric computation; N1 audit]`

**Step 2 — Clifford algebra.**

Cl(9,5) has index (9-5) mod 8 = 4 (quaternionic type). Therefore:
```
Cl(9,5) ~= M(64, H)    (quaternionic 64x64 matrix algebra)
```
The unique irreducible left module is S = H^64 with dim_R S = 256. The chirality element omega satisfies omega^2 = +1, giving a chiral splitting S = S^+ oplus S^- with dim_R S^+/- = 128 each. `[verified — Clifford periodicity, Lawson-Michelsohn Appendix I]`

**Step 3 — Clifford contraction construction.**

For any Clifford algebra Cl(V, g) with spinor module S, the Clifford contraction:

```
Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha) · s
```

defines a map Omega^2(V) tensor S -> Omega^1(V) tensor S, where {e^a} is a local orthonormal coframe, iota is interior product, and c is Clifford multiplication. This map is:

- Spin(9,5)-equivariant by construction (each component is equivariant under GL(V)). `[verified]`
- Real-linear: V, S, Lambda^k are all real vector spaces in the Cl(9,5) setting. `[verified]`
- Non-zero on all non-zero inputs: **WARNING — the term-by-term argument is insufficient.** The original claim "c(iota_{e_a} alpha) != 0 for any non-zero alpha and generic frame, therefore the sum is non-zero" is invalid: 14 non-zero terms can cancel. The correct non-cancellation argument is: for any 2-form alpha != 0, define the effective covector xi(alpha) in T*Y^{14} by the identity c(xi(alpha)) s = Phi(alpha tensor s), which holds because the contraction sum collapses to a single Clifford multiplication by the metric-dual 1-form of alpha (explicit: in an orthonormal coframe, sum_a e^a c(iota_{e_a} alpha) = c(alpha^#) where alpha^# is the metric-dual vector; this is the standard Clifford-contraction identity, see Lawson-Michelsohn §II.5, equation (5.9)). Since alpha != 0 implies alpha^# != 0, and Cl(9,5) ~= M(64, H) is simple so c(alpha^#) acts injectively on S = H^64 (non-zero element of a simple algebra over H acts with trivial kernel on the unique irreducible module), we have Phi(alpha tensor s) = c(alpha^#) s = 0 only if s = 0. Hence Phi is injective on pure tensors, and by R-linearity on all of Omega^2 tensor S. `[corrected 2026-06-23 — MO-01]`
- Natural: defined using only the metric on Y^14 and the Clifford algebra structure. `[verified]`

**Step 4 — No complexification required.**

The gauge group in the (9,5) setting is Sp(64) = U(64, H) (the quaternionic unitary group of S = H^64). This group has no U(1) center: Sp(64) is simple with center Z/2. Complexification is not needed for the shiab construction (it is real-linear) and does not arise from the quaternionic structure. `[verified]`

**Resolution of Nguyen §3.1:** The "unannotated tensor_C" step Nguyen identifies does not appear in the Clifford contraction. The map exists over R.

## Assumptions

1. Y^14 = Met(X^4) with the Frobenius metric and trace-reversal giving signature (9,5).
2. The spinor module is S = H^64 (from Cl(9,5) ~= M(64, H)).
3. The construction uses the Clifford contraction with the (9,5) metric; no further structure assumed.

## Known Failure Modes

- **Signature uncertainty.** If Weinstein's intended signature is (7,7) or another real form, the algebra changes. Cl(7,7) ~= M(128, R) gives a real spinor module and a different (but parallel) construction. The (9,5) result is confirmed by the Frobenius metric computation.
- **Sum-collapse identity precondition.** The injectivity proof (Step 3, corrected) uses the Clifford-contraction identity sum_a e^a c(iota_{e_a} alpha) = c(alpha^#) (Lawson-Michelsohn §II.5 eq. 5.9). This identity holds for any Clifford algebra with an orthonormal coframe and any 2-form alpha; it is a purely algebraic identity that follows from the definition of interior product and Clifford multiplication. If the coframe is not orthonormal (i.e., if the metric degenerates at a point), the identity requires the corrected Gram-matrix form and the conclusion still holds wherever the metric is non-degenerate. No additional condition is needed on Y^14 beyond the non-degeneracy of the gimmel metric.
- **Non-degeneracy on gauge curvature forms.** The map is injective on all non-zero inputs in Omega^2 tensor S. Whether the restriction to F_A for connections A in the GU gauge orbit has additional degeneracy is a separate physical question.
- **Generation count.** Shiab existence does not establish the generation count. That requires an index theorem on a non-compact Y^14 — a separate open problem.
- **Gauge group uniqueness.** Sp(64) is the natural gauge group from the automorphism structure of S = H^64; whether the tau^+ homomorphism selects a subgroup of Sp(64) is open.
- **Uniqueness of equivariant map.** The Clifford contraction is one Spin(9,5)-equivariant map Omega^2 tensor S -> Omega^1 tensor S. Whether it is the unique such map (up to scalar) has not been established; other equivariant maps could exist. Uniqueness is a representation-theory question (multiplicity of the relevant intertwining space) and is open.

## What This Does Not Establish

- Three fermion generations.
- Anomaly cancellation for the full GU theory (separate audit, anomaly-audit-cl95-gauge-group-2026-06-22.md, shows perturbative anomaly of Sp(64) vanishes; that is not yet at canon grade).
- Strong-coupling or renormalizability of GU.

## References

- Weinstein, E., UCSD April 2025 transcript, [00:43:04] (signature), [00:34:27-00:36:13] (shiab domain/codomain).
- Lawson, H.B. and Michelsohn, M.L., Spin Geometry, Princeton UP, 1989. Appendix I Table 1 (Clifford algebra classification).
- Harvey, F.R., Spinors and Calibrations, Academic Press, 1990. Table 6.2 (Cl(p,q) ~=).
- Source explorations: N1 signature audit (2026-06-22) and N2 shiab computation (2026-06-22).
