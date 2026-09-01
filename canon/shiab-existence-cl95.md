---
title: "Shiab Operator Existence — Cl(9,5) Setting"
status: canon
doc_type: canon
carrier_scope: scoped_historical_k95_branch
current_carrier: false
promoted_from:
  - "explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
  - "explorations/shiab-operator/n2-shiab-computation-spin77-branching-rules-2026-06-22.md"
promoted_at: "2026-06-23"
verdict: "RESOLVED (existence only)"
scope_correction: "CORRECTION SHIAB-01 (2026-06-25): RESOLVED means existence of at least one natural real-linear Spin(9,5)-equivariant Clifford-contraction map. It does not claim injectivity, non-vanishing on every non-zero input, uniqueness, source-forced selector identity, anomaly cancellation, or generation count."
---

# Shiab Operator Existence — Cl(9,5) Setting

> **CURRENT-CARRIER SCOPE (2026-09-01).** This is the scoped historical K95 branch
> theorem. Its real `Cl(9,5)=M(64,H)` mathematics and correction history
> remain citable inside that branch, but K95 is not the repository's current
> selected carrier. For current K77 statements, including the separate
> `1,274 x 1,274` Hodge--Shiab isomorphism, use
> `canon/shiab-existence-k77.md`. Do not port this file's quaternionic module,
> `Sp(64)` constraint or selector-family counts to real `Cl(7,7)`.

## Scope

The ship-in-a-bottle (shiab) operator is the natural equivariant map:

```
Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S
```

The question is whether such a map exists without complexification (the gap Nguyen §3.1 identified).

## Proof

**Step 1 — K95 branch signature used by this result.**

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

- **Carrier currentness.** The current repository-selected/source-aligned
  carrier is K77. This file preserves the K95 branch obtained from the
  `(3,1)+(6,4)` sign convention; it does not establish that K95 is the current
  GU carrier. `Cl(7,7) ~= M(128,R)` has a different real module and is treated
  independently in `canon/shiab-existence-k77.md`.
- **Full-domain kernel/rank — RESOLVED for the literal constructed map (AR-5,
  2026-08-16).** The exact signed-companion/right-inverse computation gives
  `rank_R(Phi)=3,584` and `dim_R ker(Phi)=19,712`, so this literal
  `Cl(9,5)` contraction is surjective and non-injective. See
  `lab/active-research/joe-directed/archaeology/ar5-cl95-full-shiab-rank-crosswalk-2026-08-16.md`
  and its exact certificate. This closes only the rank/kernel gap for the map
  constructed in this file. It does **not** identify Weinstein's preferred
  shiab, select the supplied `192`, or transfer any rank or kernel statement
  to the distinct current-K77 `1,274 x 1,274` Hodge--Shiab operator.
- **Non-degeneracy on gauge curvature forms.** The restriction of Phi to curvature inputs arising from GU connections may have additional degeneracy or selection structure. That is a separate physical question and is not settled by algebraic existence of Phi.
- **Generation count.** Shiab existence does not establish the generation count. That requires an index theorem on a non-compact Y^14 — a separate open problem.
- **Gauge group uniqueness.** Sp(64) is the natural gauge group from the automorphism structure of S = H^64; whether the tau^+ homomorphism selects a subgroup of Sp(64) is open.
- **Uniqueness of equivariant map — RESOLVED (negative), SHIAB-03 (2026-06-26).** The Clifford contraction is NOT the unique Spin(9,5)-equivariant map Omega^2 tensor S -> Omega^1 tensor S. The intertwining-space multiplicity was computed THREE independent ways (Racah-Speiser; Kostant/Klimyk Weyl sum over |W(D_7)|=322560; from-scratch Freudenthal decomposition, zero shared code): the COMPLEX Hom dimension is 2 per natural chirality block (4 for the full Dirac spinor), and GU's actual REAL quaternionic spinor (Cl(9,5)=M(64,H)) doubles this to real Hom dimension >= 8 `[real count corrected by SHIAB-06, 2026-08-03: exactly 16 — see below]`. So equivariance ALONE does not pin the shiab — there is an (at least 8-real-dimensional) family of natural equivariant maps; the two complex channels are the Clifford-trace channel (S+) and the Rarita-Schwinger channel (omega_1+omega_6). The separate "source-forced selector identity" — WHICH map in this family is GU's specific shiab — remains OPEN. See DERIVATION-PROGRESS SHIAB-03 and explorations/shiab-operator/shiab-codiff-intertwiner-dim-2026-06-26.md (tests/shiab_codiff_intertwiner_dim.py). Corollary (SHIAB-A, same run): GU's shiab is NOT the metric codifferential d_A* — the shiab is Clifford-odd, d_A* is Clifford-even, so they cannot be proportional (||Phi - lambda*d_A*|| = full norm for all lambda); confirms this file's distinction and refutes a perspective-sprint convergence.

## What This Does Not Establish

- Three fermion generations.
- Injectivity or non-vanishing on every non-zero input of Omega^2 tensor S.
- The source-forced selector identity: WHICH of the family of natural equivariant maps is GU's specific shiab. (Uniqueness ITSELF is RESOLVED negative by SHIAB-03 — the map is NOT unique; the open question is the SELECTION.) **SHARPENED by SHIAB-04 (2026-06-26, selector search):** GU's gu_derived symmetries narrow the family but do NOT pin it. The quaternionic / Sp(64) right-H structure (the SAME J-commutation constraint, forced by Cl(9,5)=M(64,H) — and contingent on the (9,5) signature; under a (7,7) alternative the real spinor has no J and this cut collapses) reduces the natural family from real dim 8 to **real dim 4**, and GU-derived content STOPS there. `[chain corrected by SHIAB-06, 2026-08-03: 16 -> 8 (J-commutation) -> 4 (full H-linearity/Sp(64)-equivariance) — see below]` GU's canon shiab is one element of that 4-real-dim space (Clifford-trace channel, real coords (1,0,1,0)); its specific channel + chiral-tie + scale is GU's WRITTEN formula — a definitional postulate, NOT derived from tau+/IG/action. Residual freedom beyond GU's one map = **3 real dimensions** (Clifford-trace vs Rarita-Schwinger channel + two untied chiral-block weights). The candidate selectors that DO reach dim 1 all disqualify themselves: complex-closure / d^2=0 is UNSATISFIABLE (kills the whole family incl. the canon shiab — the obstruction does not vanish for any element; GU only asserts d^2=0 conditionally); seesaw self-adjointness is vacuous or forces the Clifford-even codifferential d_A* (which the Clifford-odd family cannot equal); gamma-trace/RS pins to 1 but EXCLUDES GU's Clifford-trace shiab (selects wedge − 6·contract). The bare zero-insertion family has no same-chirality scalar block; this does not exclude insertion-dependent same-corner pairing shapes, which ST-1 finds kinematically available after one declared class-2 insertion. Turning that availability into an operative self-mass still requires source-action selection, a reality map and a scale, all OPEN. So derivational selection genuinely requires the still-OPEN GU source action. See DERIVATION-PROGRESS SHIAB-04 and explorations/shiab-operator/shiab-selector-search-2026-06-26.md.

  **CORRECTION SHIAB-05 (2026-06-30, MOVE-4 chase; scope narrowed 2026-08-24) — bare zero-insertion same-chirality scalar absence COMPUTED.** The exact computation on the verified Cl(9,5)=M(64,H) representation gives, over the actual 128-dim Dirac spinor rep,
  `dim Hom_{Spin(9,5)}(S^+ tensor S^+, Lambda^0) = 0` — there is NO invariant scalar bilinear on the bare zero-insertion SAME-chirality product S^+ x S^+; the scalar (charge-conjugation) bilinear exists only OFF-diagonally, on S^+ <-> S^-. This binds that Hom domain only. It does not bind `Hom(S^+ tensor S^+ tensor T_2, Lambda^0)` after a class-2 insertion; exact Z/4 arithmetic removes the bare class obstruction there, and ST-1 independently constructs nonzero inserted shapes. Those shapes are kinematic availability, not a selected mass: source-action selection, the reality map, scale, domain and spectrum remain OPEN. HARD CHECKSUM: the total intertwiner dimension summed over all form-degrees Lambda^k equals `16384 = 128^2 = (dim S)^2` (End(S) = (+)_k Lambda^k, multiplicity 1 each, Lambda^7 splitting 1+1), with all component errors 0.00e+00. Minor note: the "Lambda^0 dim = 2" appearing in one intermediate is really Lambda^0 + Lambda^14 (the top form is a scalar under Spin, harmless bookkeeping — the k=0 invariant scalar bilinear on S^+ x S^+ is still exactly 0). This is EXACT, unconditional representation theory of Spin(9,5): it is INDEPENDENT of whether GU is correct and is NOT a physics derivation of any action. Runnable computation: `tests/chase/MOVE-4/move4_spinor_square_forms.py` (Jordan-Wigner Cl(9,5) gammas; trace-orthonormality of antisymmetrized Clifford words; nullspace solve for the Spin-invariant bilinear space with chirality-block support).

  **CORRECTION SHIAB-06 (2026-08-03, eleven-lens audit finding B17 / register M-M2) — real family dimension is 16, not 8; the 8 -> 4 step named the wrong constraint.** The REAL Spin(9,5)-equivariant family (SHIAB-03's object) has dim_R **16**, not ">= 8": the doubling argument counted only the complex-linear half of the spinor commutant and omitted its ANTILINEAR half — End_{Spin(9,5)}(S+/-_R) = H (dim_R 4, = C (+) jC), and the complexification cross-check S_R (x) C = 2 S_C gives dim_R Hom_R = 4 x 4 = 16 exactly (independently confirmed by a common-constituent count: 4 shared real irreducible channels x dim_R H = 16). SHIAB-04's reduction "from real dim 8 to real dim 4 by the SAME J-commutation constraint" conflated two different constraints: J-commutation alone cuts 16 to 8; it is FULL H-linearity (commuting with the whole right-H structure, i.e. Sp(64)-equivariance) that reaches 4. The correct chain is **16 -> 8 (J-commutation) -> 4 (full H-linearity/Sp(64)-equivariance)**. The dim-4 ENDPOINT — and with it SHIAB-04's placement of GU's canon shiab inside a 4-real-dim family with residual freedom 3 — survives IF AND ONLY IF full Sp(64)-equivariance is the imposed GU-derived constraint; under J-commutation alone the family is 8-dimensional (residual freedom 7). Which constraint GU's own structure earns belongs to the still-OPEN selector question (SHIAB-02/-04) and is not adjudicated here. Derivation and both real counts: `explorations/form-spinor-decomposition-and-shiab-family-dimension-2026-08-03.md` (which also re-derives the complex count 2-per-chirality-block from the multiplicity-free decompositions Lambda^2 V (x) S+ = S+ (+) Sigma_1+ (+) Sigma_2+ and V (x) S- = S+ (+) Sigma_1+, replacing the Weyl-sum machinery). **No verdict changes:** existence stays RESOLVED (existence only); the source-forced selector stays OPEN; this corrects a dimension count and a constraint name inside the discussion above.
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
