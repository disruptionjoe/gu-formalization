---
title: "K2219 Unique global half-contrast detector minimizer"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unique global optimum of the supplied scalar instrument; no apparatus or GU physics credit
scripts:
  - tests/channel-swings/k2219_detector_global_capture_probe.py
---

# K2219 Unique global half-contrast detector minimizer

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
result: K2219 Unique global half-contrast detector minimizer
carrier: scalar positive Fock detector at exact contrast1/2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and scalar moments ON=declared_carrier
real_structure: real effects and positive outcome squeezes
grading: occupation number; no spinor or physical chirality
action_owner: repository-construction -- supplied scalar instrument energy
target: all-profile all-positive-squeeze global optimum MAP-TYPE=intertwiner
```

## Result

The supplied detector at exact contrast d=1/2 has a **unique global
minimizer** over all cap-feasible infinite effects and all positive outcome
squeezes. It is the stationary profile already certified in
[K2210](k2210-detector-stationary-certificate-2026-10-28.md).
No finite-tail truncation or optimizer-convergence premise is used.

The new proof joins a larger rigorously admitted convex region to a complete
exterior exclusion. The basin radius is R=1/5000000 in each squeeze
coordinate, centered at the exact rational CENTER in the K2210 probe.
The fresh all-tail Schur lower bound exceeds1/3. Every exterior leaf passes
the stationary-global-minimizer exclusion;221 leaves plus the basin cover
all of K2216's localized rectangle G. There are no unresolved leaves.

Let D(c) be the recomputed exact lower dual at the center using the inherited
free positive slopes, U the inherited feasible upper bound, and r0=10^-14.
The global optimum E_star obeys the new exact bracket

    D(c)-24 r0² <= E_star <= U,
    0 < U-D(c)+24 r0² < 2.5*10^-27.                 (1)

Exact endpoints, full outward intervals, partition keys, arbitrary dual
inputs and dependency hashes are in the probe and
[certificate](../../lab/process/k2219-detector-global-capture.json).
The narrow bracket is a consequence of global uniqueness, not another
unjustified numerical extrapolation.

## 1. Stationary center-transfer

Use K2216's exact all-tail model p_n=(3/4)4^-n, x_n=p_n e_n,
0<=e_n<=1, sum(3n-1)x_n=1/2, with energy and fixed-profile squeeze
Hessian bounds16,32 on G. If a global minimizer (x,s) lies in the enlarged
basin, its squeeze gradient vanishes, so Taylor expansion with its OWN
profile gives

    E(x,c) <= E(x,s)+8(s1-c1)²+16(s0-c0)²
           <= U+24R².                              (2)

The same argument applies to K2210's stationary optimizing candidate,
whose energy is at most U. Therefore K2198's dual-gap coordinate enclosure
at FIXED c applies with

    eps_R=U-D(c)+24R².                              (3)

This removes the old interval-dual radius loss proportional to R. It is not
an energy bound for arbitrary profiles or every nonminimal stationary point.
Actual global minimizers and the inherited candidate are the endpoints used
below; both optimize the profile at their respective fixed squeezes.

## 2. Fresh tail admission and uniform Schur bound

The probe computes seven coordinate boxes from (3), retaining exact outward
rational arithmetic. For the true fixed-squeeze optimizers it recomputes the
multiplier interval from the n=0 equation, at the actual squeeze intervals:

    eta=C/4*(s1 sqrt(e1/e0)-s0 sqrt(f1/f0))
         -(A(s1)-A(s0))/2,
    C=40/3, A(s)=41s²/6+3/(2s²), f=1-e.

The K2198 recurrence barrier is freshly checked with start2,
sigma=1/3,rho=1/2. The head ratios sqrt(f_(n+1)/f_n) for n=0,1 are inside
(1/3,2/3), e0>3/20, and the resulting all-tail linear bounds are

    e_n>=3/20, f_n/9<=f_(n+1)<=4 f_n/9,
    f_(n+1)<=f_n/4 for n>=2.                        (4)

These are optimizer admission facts. Once admitted, their linear inequalities,
coordinate intervals and the squeeze rectangle define a convex set C_R.
They are not assumed to hold for every feasible profile.

On ALL of C_R, independently of stationarity, the fresh K2204/K2213
constrained Hessian/residual computation proves S>(1/3)I and S> D/100,
with D<30I, kappa>1/50 and D>(3/4)I. It recomputes the finite tridiagonal
trial solves, junction index4, complement tail from5, both score residuals
and the full Schur estimate. The sharper complement coercivity uses
f0_lower=1-e0_upper. No old bound is transferred to a larger box.

The convex-chord proof of [K2213](k2213-detector-convex-uniqueness-2026-10-28.md)
then applies: along the chord between an admitted global minimizer and the
K2210 candidate, the Hessian lower bound integrates to

    E(x,s)-E_star >= ||x-x_star||_p^-1²/20000
                         +3|s-s_star|²/1600.        (5)

Here ||v||_p^-1²=sum v_n²/p_n. Endpoint differentiation is justified by
(4), the summable tails and stationarity as in K2213. The chord need not
have bounded relative-cap distance at its endpoints; interior chords admit
the required relative bounds. Thus there is at most one global minimizer
inside the basin, and it is the inherited candidate. Equation(5) holds on
the admitted convex envelope, not globally outside it.

## 3. Complete exterior certificate

K2216 already proves that every global minimizer lies in
G=(9/10,111/100) times (17/25,91/100). Split closed G first at the four
basin faces into nine rectangles. Retain the central basin and subdivide
the other eight by rational midpoint. The split axis is the larger of
8*width1² and16*width0², with a fixed tie rule.

Every leaf q is accepted ONLY if its arbitrary valid positive-input dual
at its center satisfies

    D(center(q))-8 h1²-16 h0² > U.                  (6)

If a global minimizer were in that leaf, stationarity and the fixed-profile
Taylor bound would imply the reverse inequality. This excludes global
minimizers, not all arbitrary profiles or all stationary points there.

The executable certifier reconstructs the full binary partition from221
leaf keys: each nonleaf has both children, no duplicates or prefix-overlap
are allowed, all eight exterior roots are covered, and shared closed faces
are retained. It also checks exact area including the basin. All221 margins
are positive; the minimum exceeds2.2*10^-14.

Dual slopes come from positive clipped extrapolations of the old polynomial
and31 stored decimal profile seeds from numerical discovery. Every decimal
is interpreted as an exact rational; positivity is checked before the dual.
They are FREE AM-GM inputs, not certified approximate optimizers. Neither
polynomial interpolation error nor a floating solver's success is used in the
proof. The probe needs no numerical optimizer and recomputes complete affine
infinite tails, including the junction. A failed initial polynomial-only
cover motivated independent free seeds; it was not evidence of another
minimum. The supplied seeds close the entire cover.

## 4. Global conclusion and bracket

Global existence is inherited. Exterior exclusion forces every global
minimizer into the basin. Sections1–2 admit it and the known stationary
candidate into the same strictly convex envelope; hence they coincide.
This proves uniqueness over all positive squeezes and infinite profiles.
In particular the global minimizer lies in the ORIGINAL radius r0 box.
Apply (2) there and E(x,c)>=D(c) to obtain (1).

## Verification and ceiling

Fresh exact arithmetic certifies the221 exterior leaves and the enlarged
whole-tail Schur/tail-admission bounds. Genuine faults remove an exterior
branch, corrupt Taylor/center-transfer factors or violate actual slope
positivity. Unchanged K2210 boundary existence is reused with dependency
hashes, not recounted as a new proof. Internal independent review checks
the universal transfer and coverage, not just manifest assertions.

This settles the model's half-contrast global optimization question. It
neither selects a stable apparatus/preparation/reset implementation nor
proves the total-work resource account, other-contrast global uniqueness,
physical observation, GU confirmation or falsification. Source polarities,
ledger0.263 and prior scalar/thermal claim ceilings remain unchanged.
The meaningful successors are other-contrast global structure or the
independent shared apparatus model; repeating this half-contrast exterior
search is no longer needed.
