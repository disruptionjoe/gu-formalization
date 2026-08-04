---
title: "Hostile review: K77 Wave-2 draft-9.16 primalizer and preboundary templates"
date: 2026-08-04
status: complete
verdict: "REPAIRED_PARTIAL__SOURCE_AND_TEMPLATES_PASS__ACTUAL_D916_K77_ASSEMBLY_OPEN"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Hostile review: K77 Wave-2 draft-9.16 packet

## Verdict

The rendered source transcription and the exact mathematical templates pass
at their stated grades. The initial summary's claim of actual global K77
closure fails.

All three reviewers independently identified the same Layer-0 error: an exact
generic theorem or finite model was being reported as though the sixteen-block
draft operator had been instantiated in the real K77 geometry. The packet was
repaired, the campaign was reverted to Wave 2 partial, and the probe was
rerun after the corrections.

Final status:

```text
PARTIAL__DRAFT916_SOURCE_MATRIX_AND_FORMAL_PRIMALIZER_TEMPLATES_BUILT__ACTUAL_D916_K77_ASSEMBLY_OPEN
```

## Review 1: Krein/operator and hyperbolic-PDE charge

Charge: find where a formal variational statement is promoted to a physical
or operator-domain theorem.

Findings:

1. `D916:E->E!` was being treated as a square endomorphism before constructing
   a primalizer `R:E!->E`.
2. The correct adjoint question is about `D_pr=R D916`, or must be phrased as
   an intrinsic transpose pairing.
3. In signature `(7,7)`,
   `star^2|Omega^p=(-1)^(p(14-p)+7)`: degrees `1,13` have sign `+1`, while
   degrees `0,14` have sign `-1`. The zero-form primalizer therefore carries
   a relative minus sign.
4. The Green identity must be a density identity with a partial derivative,
   not an equality between a scalar integrand and a density-valued current.
5. A compact-support test space is a candidate variational core, not a closed
   physical domain and not yet a proven common invariant core for the actual
   bosonic and fermionic operators.

Disposition: accepted and repaired.

## Review 2: primary-source and global-geometry charge

Charge: find where the summary outruns the source or where a model is called
the actual geometric object.

Findings:

1. The page-46 equation-9.16 transcription is identity-grade and passes.
2. `rho(epsilon)` is a displayed covariance ansatz, not a proof of global
   overlap descent for the real-K77 bundle.
3. The exact rational three-patch `O(1,1)` fixture proves a useful model
   theorem but does not instantiate the `Y14` atlas, K77 transitions,
   Hodge/Shiab coefficients, or sixteen D916 blocks.
4. The draft displays southeast zero and admits a nonzero rival; the 2025
   conversation reiterates zero prospectively. None supplies uniqueness.
5. The source asserts the three-family interpretation with hedges but does
   not derive an observed chiral index. It is inaccurate to call the source
   simply silent about the family assertion.

Disposition: accepted. Source verbs and model labels were repaired.

## Review 3: representation/variational-proof charge

Charge: find ill-typed decompositions, tautological tests, or finite controls
reported as the actual action theorem.

Findings:

1. `Gamma:Omega1(S)->Omega0(S)`, so `im Gamma` is not a subspace of
   `Omega1(S)`. The kinematic middle piece requires a chosen splitting
   `s_Gamma(im Gamma) subset Omega1(S)`.
2. The principal-adjoint test compared an expression with itself. It had to
   extract the coefficients of independent symbolic field derivatives from
   the computed formal adjoint.
3. The finite K-skew southeast example proves only that algebraic K-skewness
   alone does not force zero. It does not construct a nonzero block with the
   actual form degrees, gauge equivariance, and real-K77 structures.
4. The finite connection-insertion derivative and conjugation identity do
   not recompute the predecessor's actual `J_D+J_F` current or full moving
   even-IG Ward identity.
5. No graded/Berezin Hessian was checked; the action control remains at
   classical independent-field grade.
6. The provenance--observer--symbol incidence census is a Wave-3 preflight,
   not evidence that Wave 3 is admitted.

Disposition: accepted and repaired.

## Required actual closure burden

Wave 2 can close only after one construction instantiates and tests:

1. all sixteen D916 blocks with real K77 form degrees and coefficients;
2. the density-dual lift and actual Hodge/Krein primalizer;
3. the full multi-index formal adjoint;
4. the lower-left comparison after the displayed row permutation;
5. actual `rho(epsilon)` transition/descent data;
6. one common compact-support core for bosonic and fermionic variations;
7. the `J_D+J_F` connection variation exactly once; and
8. the moving even-IG Ward identity on that same core.

## Repairs verified

- added exact Hodge-sign and finite primalizer inverse controls;
- replaced the tautological symbol comparison by derivative-coefficient
  extraction from symbolic functions;
- relabeled overlap, current, Ward, and southeast fixtures at model/finite
  grade;
- repaired gamma-trace typing;
- changed common domain to candidate common core;
- separated source assertions from source derivations;
- reverted campaign frontier from Wave 3 to Wave 2 partial; and
- preserved Wave-3 incidence as a preflight only.

Final deterministic rerun:

```text
7 source + 23 type + 19 exact + 5 planted = 54 PASS.
```

No P1/P2/P3 use, physics recovery, generation count, claim-status change,
canon change, lane change, third-lane promotion, or public-posture change is
made.
