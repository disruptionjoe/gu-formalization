---
title: "K1986: A certified uncapped pulse and a strict amplitude penalty"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1986_pulse_primal_dual_certificates.py
  - tests/channel-swings/k1986_pulse_primal_dual_certificates_probe.py
---

# K1986: A certified uncapped pulse and a strict amplitude penalty

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact-marginal uncapped pulse, geometric convergence, amplitude violation and strict norm penalty
carrier: real width9 characteristic strip and actual K1969 optimal phase LAYER=toy CHIRALITY=N/A
pairing: area-weighted L2 pulse norm and Lebesgue row averages ON=characteristic_strip
real_structure: real measurable pulse, with and without the23/100 amplitude constraint
grading: two characteristic directions, not source chirality
action_owner: repository-construction -- scalar marginal problem
target: rigorous construction and separation of uncapped and capped norm optima MAP-TYPE=intertwiner
```

## A different optimization question

[K1980](k1980-constructive-minimum-norm-pulse-2026-10-23.md) defines the unique
minimum-L2 pulse with the actual optimal phase and amplitude cap M=23/100.
Its iterative construction does not give a strong error-to-limit modulus.
Here we solve the problem with the SAME two exact marginals but WITHOUT the
amplitude cap. The uncapped solution has a uniform geometric error bound,
and a certified open-set violation proves that it cannot replace the capped
optimizer. Every capped feasible pulse pays an explicit positive squared-norm
penalty. This secondary norm is not the already-settled Dirichlet phase energy.

Use D={(u,z):-3<=u<=3,u<=z<=u+9}, and K1980's orthogonal row and column
projections P,Q on L2(D). Let g(u)=2 phi_star(u)/9. The target is Pv=g,Qv=0.
The phase is odd, so g has mean zero. On row functions define K=PQ, equivalently
PQP after embedding row functions into L2(D).

## Exact contraction and marginal solution

Every row intersects the common rectangle3<=z<=6. On this rectangle Qf is
the full average of f over[-3,3], hence zero for any mean-zero f. The rest of
each row has length6. Conditional averaging is a sup-norm contraction, so

    ||Kf||_infinity <=(2/3)||f||_infinity.               (1)

K preserves mean zero: P,Q preserve the area integral and row length is9.
Consequently the uniformly convergent series

    h=sum_(j>=0) K^j g,     v0=(I-Q)h                  (2)

has Ph=h, Qv0=0 and Pv0=(I-K)h=g. The tail after N terms is at most
3(2/3)^N ||g||_infinity; ||g||_infinity=2/9.
Thus both marginals are EXACT for v0, with an effective uniform construction.

If w has the same marginals, then d=w-v0 satisfies Pd=Qd=0, and
<v0,d>=<h,d>-<Qh,d>=0. Therefore

    ||w||_2^2=||v0||_2^2+||w-v0||_2^2,
    ||v0||_2^2=<g,h>_D=9 int_(-3)^3 g(u)h(u)du.       (3)

This proves uniqueness and optimality, with h and -Qh furnishing the dual
potential in the orthogonal complement of the homogeneous constraints. No
surjectivity or closed-range theorem is assumed without a construction.

For an odd piecewise linear f with F(x)=int_(-3)^x f, direct column integration
also gives the independently useful one-dimensional formula

    Kf(u)=(1/9)[int_u^3 F(x)/(x+3)dx
                     -int_(-3)^u F(x)/(3-x)dx].        (4)

The endpoint singularities are removable because F(-3)=F(3)=0. In the
interior, (Kf)'=-2F/[3(9-u^2)]. In particular the exact primitive H'=h obeys
H''+2H/[3(9-u^2)]=g', H(-3)=H(3)=0, wherever the phase derivative exists.
This is an equivalent one-dimensional boundary equation, not a new smoothness
claim at phase breakpoints.

## Executed continuum certificate

The producer uses480 uniform row intervals and720 midpoint column samples.
Shared column integrals and prefix sums make each update linear in grid size;
it no longer recursively branches for every requested point. Forty updates
use exact rational arithmetic with bounded dyadic rounding. Odd reflection is
preserved exactly. The actual algebraic phase is enclosed through K1983's
isolating root, rather than replaced with an unrelated test marginal.

For piecewise linear f with Lipschitz constant L and sup bound B, the row
quadrature error is at most9L/(4m). Since |(Kf)'|<=2B/9, interpolation on
n intervals costs at most2B/(3n). The forcing interpolation error is at most
3G/n plus its root and rounding error, with G=23/100. Accumulate these local
errors with contraction factor2/3, then add the explicit Neumann tail.
The resulting rigorous enclosure is

    0.2917397591 < h(-2) < 0.3078870678.                 (5)

Exact rational endpoints are in the JSON; these decimals are rounded outward.
An independent probe integrates(4) over every linear segment using rational
logarithm bounds, obtained from the convergent atanh series. A posteriori
residual gives ||h_tilde-h||_infinity<=3||h_tilde-g-Kh_tilde||_infinity.
It independently certifies h(-2)>0.28. Neither certificate relies on
floating-point agreement. Both are continuum bounds, not just grid values.

## Released strict capped-norm penalty

On3<z<6, Qh=0, hence v0(u,z)=h(u). Equation(5) proves v0(-2,z)>M+1/20.
Moreover h is Lipschitz with

    L_h <= G+2||h||_infinity/9 <=23/100+4/27.

Put a=1/20. On |u+2|<=a/(2L_h),3<z<6, one has v0>=M+a/2.
Every capped feasible w therefore differs there by at least a/2. Combining
this rectangle's area with(3) gives

    ||w||_2^2-||v0||_2^2 >=3a^3/(4L_h)
       =81/326720 >0.0002479187.                        (6)

The report also encloses ||v0||^2 by exact integration of the linear grid
products plus the uniform forcing/solution error; adding(6) gives a genuine
lower bound on the capped optimum. The earlier forced-saturation bounds remain
available. No finite iterate here is declared amplitude-feasible.

## Verification and next boundary

The independent rational logarithm certificate covers481 row nodes plus a
whole-interval Lipschitz bound. Four genuine sign, scale, shape and claimed-gap
faults must fail after its green baseline. The contraction, orthogonality,
quadrature transfer and open-rectangle argument establish the analytic scope.
There is no external reviewer or proof-assistant certification.

The amplitude constraint is genuinely active. Clipping v0 destroys its exact
marginals in general; it is not a solution method. The useful next construction
is to solve the residual capped transport after the forced regions are removed,
or obtain a bounded dual potential on that residual problem. The uncapped
problem, its uniform convergence, and its admissibility test are now closed.
Capped pulse construction, its strong error modulus, and smooth exact-endpoint
approximation remain open. SC-META-53 is UNCERTAIN; source, physics-ledger and
canon verdicts stay unchanged. This is independent scalar mathematics.
