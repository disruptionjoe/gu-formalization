---
title: "Shiab Operator Existence — Cl(9,5) Setting"
status: canon
doc_type: canon
promoted_from:
  - "explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
  - "explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md"
promoted_at: "2026-06-23"
verdict: RESOLVED
scope_correction: "CORRECTION SHIAB-01 (2026-06-25): RESOLVED means existence of at least one natural real-linear Spin(9,5)-equivariant Clifford-contraction map. It does not claim injectivity, non-vanishing on every non-zero input, uniqueness, source-forced selector identity, anomaly cancellation, or generation count."
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
- Non-zero as a map: choose a local orthonormal coframe and a simple 2-form alpha = e^1 wedge e^2. Then the displayed formula gives output components containing c(e^2)s and -c(e^1)s. Clifford multiplication by a non-null covector is invertible, so for any s != 0 at least one displayed component is non-zero. This proves Phi is a non-zero natural map. **It does not prove injectivity or non-vanishing on every non-zero element of Omega^2 tensor S.** In fact Phi cannot be injective as a map Lambda^2 V tensor S -> V tensor S in 14 dimensions, since dim(Lambda^2 V tensor S) = 91 dim(S) and dim(V tensor S) = 14 dim(S). The previous alpha^# collapse argument was invalid: a 2-form has no canonical metric-dual 1-form. `[corrected 2026-06-25 — SHIAB-01]`
- Natural: defined using only the metric on Y^14 and the Clifford algebra structure. `[verified]`

**Step 4 — No complexification required.**

The gauge group in the (9,5) setting is Sp(64) = U(64, H) (the quaternionic unitary group of S = H^64). This group has no U(1) center: Sp(64) is simple with center Z/2. Complexification is not needed to CONSTRUCT a natural Spin(9,5)-equivariant Clifford contraction (it is real-linear) and does not arise from the quaternionic structure. This is a statement about the constructed map's existence, NOT a claim that GU's specific shiab operator is identified with it (see Known Failure Modes "Uniqueness of equivariant map" and "What This Does Not Establish"). `[verified for the constructed map's existence; identification with GU's operator is OPEN]`

**Resolution of Nguyen §3.1 (existence only — SHIAB-02, 2026-06-26).** Nguyen §3.1 flags a possible forced complexification (an "unannotated tensor_C" step). The existence result above is a COUNTEREXAMPLE to the universal claim "every natural Spin(9,5)-equivariant Clifford contraction of this type must complexify": at least one such map exists over R, and the tensor_C step does not appear in it. This rebuts the universal form of the objection. It does NOT establish that GU's actual shiab operator IS this real map, nor that GU's operator is thereby well-defined or complexification-free — that requires the source-forced selector identity this file holds OPEN (frontmatter scope_correction from SHIAB-01; Known Failure Modes "Uniqueness of equivariant map"; "What This Does Not Establish"). Existence-only, not an identification of GU's operator.

## Assumptions

1. Y^14 = Met(X^4) with the Frobenius metric and trace-reversal giving signature (9,5).
2. The spinor module is S = H^64 (from Cl(9,5) ~= M(64, H)).
3. The construction uses the Clifford contraction with the (9,5) metric; no further structure assumed.

## Known Failure Modes

- **Signature uncertainty.** If Weinstein's intended signature is (7,7) or another real form, the algebra changes. Cl(7,7) ~= M(128, R) gives a real spinor module and a different (but parallel) construction. The (9,5) result is confirmed by the Frobenius metric computation.
- **Kernel/rank not computed.** The map is non-zero, but it is not injective dimensionally. Its kernel, image, and rank on the full domain Lambda^2 V tensor S have not been computed. Any future use of Shiab that needs injectivity must replace this canon entry with an explicit representation-theoretic rank/kernel computation.
- **Non-degeneracy on gauge curvature forms.** The restriction of Phi to curvature inputs arising from GU connections may have additional degeneracy or selection structure. That is a separate physical question and is not settled by algebraic existence of Phi.
- **Generation count.** Shiab existence does not establish the generation count. That requires an index theorem on a non-compact Y^14 — a separate open problem.
- **Gauge group uniqueness.** Sp(64) is the natural gauge group from the automorphism structure of S = H^64; whether the tau^+ homomorphism selects a subgroup of Sp(64) is open.
- **Uniqueness of equivariant map.** The Clifford contraction is one Spin(9,5)-equivariant map Omega^2 tensor S -> Omega^1 tensor S. Whether it is the unique such map (up to scalar) has not been established; other equivariant maps could exist. Uniqueness is a representation-theory question (multiplicity of the relevant intertwining space) and is open.

## What This Does Not Establish

- Three fermion generations.
- Injectivity or non-vanishing on every non-zero input of Omega^2 tensor S.
- Uniqueness of the equivariant map.
- Anomaly cancellation for the full GU theory. The separate anomaly audit defuses
  Nguyen's U(128) pincer by replacing it with the Sp(64) setting, but full local/global
  GU anomaly cancellation remains OPEN and non-canon pending an explicit 14D
  `I_16`/index-density computation and spin-bordism/Dai-Freed/eta check.
- Strong-coupling or renormalizability of GU.

## References

- Weinstein, E., UCSD April 2025 transcript, [00:43:04] (signature), [00:34:27-00:36:13] (shiab domain/codomain).
- Lawson, H.B. and Michelsohn, M.L., Spin Geometry, Princeton UP, 1989. Appendix I Table 1 (Clifford algebra classification).
- Harvey, F.R., Spinors and Calibrations, Academic Press, 1990. Table 6.2 (Cl(p,q) ~=).
- Source explorations: N1 signature audit (2026-06-22) and N2 shiab computation (2026-06-22).
