---
title: "K2222 Uniform detector contrast continuation and differentiable energy"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unique global minimizer and C1 energy on a tiny explicit contrast interval; no all-contrast or apparatus claim
scripts:
  - tests/channel-swings/k2222_detector_contrast_continuation_probe.py
---

# K2222 Uniform detector contrast continuation and differentiable energy

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
result: K2222 uniform infinite detector minimizer and energy response
carrier: supplied positive scalar Fock detector at contrast in [1/2-1e-18,1/2+1e-18] LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and scalar moments ON=declared_carrier
real_structure: real effects and positive outcome squeezes
grading: occupation number; no physical chirality
action_owner: repository-construction -- supplied scalar instrument energy
target: uniform all-profile all-squeeze global optimum MAP-TYPE=intertwiner
```

## Exact construction and new endpoint

Let I=[1/2-10^-18,1/2+10^-18]. Fresh exact checks establish that every d in I has one unique global minimizing profile/squeeze pair. The minimizer is continuous in d (coordinate topology and squared weighted norm sum |x_n-x'_n|²/p_n), and its energy F is C1 on the interior, with F'(d)=eta(d), the actual contrast multiplier. No C2/analytic branch or global-in-contrast uniqueness is inferred.

No new stationary witness is required. Existing global existence applies separately for every d. The complete exterior certificate places all minimizers in the same basin. Fresh admission and uniform Schur bounds admit any two minimizers at the SAME d to one common convex envelope; their chord preserves contrast, so strict convexity proves uniqueness. K2210's particular stationary candidate is needed only as a feasible upper bound at d=1/2, not as an asserted continued stationary solution.

## A feasible uniform upper bound

Use K2210's repaired exact finite constant-tail profile at CENTER. Change x0 to x0-(d-1/2), holding all other x and squeezes fixed. Since q0=-1 this is exact contrast repair. Check the whole repaired e0 interval lies inside [3/20,1/5]. No tail is changed. With s in [2/3,113/100], A<=13, x1/x0<=5/3<(4/3)^2, y1/y0<=5/16<(3/5)^2,

|partial E/partial x0| <=13/2+(C/2)(113/100)(4/3+3/5)<100.

Thus U(d)<=U0+100 epsilon. All quantities are exact rationals or certified outward intervals.

## Uniform localization and Taylor constants

For d in I: w_lo=(d-1/4)/2 <= w <= 1-d=w_hi,
Rx=(2d+5w)/6, Rx_min=3d/4-5/48, Rx_max=(5-3d)/6,
Ry_min=d/2, Ry_max=15/16-3d/4.

Cauchy bounds (Tx/Rx)^2<=1-(w_lo/Rx_min)^2/4 and (Ty/Ry)^2<=1-((1-w_lo)/Ry_max)^2/4. Both mass/moment ratios increase with w at fixed d>0. K2194 optimizer monotonicity gives Tx/Rx >=(d+4w_lo)/(2d+5w_lo). Outward interval comparisons retain exactly G=(.9,1.11)x(.68,.91), and fixed-profile squeeze Hessian upper bounds 16,32. These steps cannot merely inherit the d=1/2 numbers.

## Uniform duals, basin and exterior

For each free positive AM-GM slope set u and fixed squeeze center c, its dual is affine in contrast:
D(c,d)=D(c,1/2)+eta_u(c)(d-1/2),
eta_u(c)=-(A(c1)-A(c0))/2+C(c1*u1[0]-c0*u0[0])/2.

Each K2219 leaf survives if its recomputed half-contrast margin exceeds (100+|eta_u|)epsilon. Retain one actual passing slope choice per leaf. Reuse partition identities only; all margins are newly checked. At the basin center, the fixed-profile stationary Taylor transfer yields the uniform coordinate-gap budget

U0+100 epsilon-D(c,1/2)+|eta_center|epsilon+24R²,
R=1/5000000.

Recompute head coordinate boxes, actual optimizer multiplier enclosure, K2198 recurrence barrier, linear all-tail cone, and full finite-trial/infinite-tail Schur estimate using that enlarged gap. The probe explicitly copies and reevaluates these calculations; it does not transfer old output numbers to a wider set. Fixed-d tangent space q-perp is unchanged, so the constrained Schur argument applies to each d. The actual multiplier enclosure is exposed separately from the historical Schur parameter also called eta.

## Continuity and C1 proof without infinite IFT

1. All minimizers lie in a fixed compact product of capped profiles and bounded squeezes, with uniformly convergent moment and energy series. Given d_j->d, any cluster point is feasible at d. Head repair of the optimizer at d produces feasible competitors at d_j whose energies tend to F(d), proving limsup F(d_j)<=F(d). Lower semicontinuity and optimality of cluster points give the reverse bound. Global uniqueness forces every cluster point to be the unique minimizer at d, so the entire minimizing branch is continuous.
2. Weighted norm continuity follows dominated convergence: |x_n(d_j)-x_n(d)|²/p_n<=p_n and sum p_n=1. This gives an honest norm statement without relative-tail assumptions.
3. The n=0 KKT identity gives eta=-partial E/partial x0. It is continuous as a function of s1,s0,e0,e1, which remain away from head caps. It involves no infinite derivative sum.
4. For small h with d,d+h in I, head repair at optimizer d yields F(d+h)<=F(d)+eta(d)h+C0 h². Head repair of optimizer d+h back to d yields F(d+h)>=F(d)+eta(d+h)h-C0 h². A uniform bound |partial² E/partial x0²|<200 is certified on the head box; take C0=100 where the entire repair segment stays inside it. Subtract eta(d)h and divide in absolute value: error/|h| <=|eta(d+h)-eta(d)|+C0|h| ->0. Hence F'=eta, and F is C1 on int(I), with one-sided endpoint derivatives.

The tiny interval is a certified robustness neighborhood, not a large-contrast phase diagram. Changing d changes tail rates; a uniform relative-cap Banach space or infinite-dimensional implicit-function theorem is NOT justified by these data. There is no C2 or derivative-of-profile theorem here.

## Verification, inherited evidence and scope

The fresh exact computation passes17 coefficient/localization/repair controls,
all221 exterior leaves with minimum uniform margin above2.20e-14, and a
recomputed infinite-tail Schur margin above0.38737>1/3. Its actual contrast
multiplier enclosure is approximately[4.72976455,4.72986006], interpreted only
through the exact rational endpoints in
[the report](../../lab/process/k2222-detector-contrast-continuation.json).
This supplies a quantitative slope bound on the certified interval; it does
not determine second derivatives or extend uniqueness to other contrasts.
Four baseline-first genuine faults change head-repair sign, dual sign,
upper-family cost or remove an actual partition leaf.

The fixed-model global existence, fixed-squeeze optimizer and tail recurrence
are inherited from [K2194](k2194-detector-optimizer-structure-2026-10-28.md),
[K2198](k2198-detector-profile-certificates-2026-10-28.md),
and [K2219](k2219-detector-global-capture-2026-10-28.md), with their pinned
probe dependencies. The all-contrast compactness statements are reused, not
the half-contrast stationary witness as a claimed branch.
The finite certificate is independently reviewable exact arithmetic; the
continuity/differentiability argument is a written proof, not proof-assistant
or external-expert certification. No numerical optimizer runs in reproduction.

SC-META-53 remains UNCERTAIN; source polarities, ledger0.263 and physical
claim grades do not change. This is the supplied positive scalar instrument,
not source GU geometry or physical observation. Apparatus, clock, preparation,
reset and total resources remain separate from the energy objective.
