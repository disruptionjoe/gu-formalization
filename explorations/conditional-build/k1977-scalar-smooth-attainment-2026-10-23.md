---
title: "K1977: Smooth nonattainment and a quantitative curvature cost"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1977_scalar_smooth_attainment.py
  - tests/channel-swings/k1977_scalar_smooth_attainment_probe.py
---

# K1977: Smooth nonattainment and a quantitative curvature cost

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
result: C1 pulse nonattainment and fixed-curvature positive energy penalty
carrier: fixed scalar width9 two-characteristic strip and plateau phase LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginals and Dirichlet phase energy ON=three_free_intervals
real_structure: real bounded pulses, C1 or C2 only when expressly required
grading: characteristic directions, not source chirality
action_owner: repository-construction -- fixed conditional scalar model
target: smooth attainment and necessary pulse spatial-curvature cost MAP-TYPE=intertwiner
```

## 1. No continuously differentiable pulse attains the measurable optimum

Keep the EXACT scalar model of
[K1974](k1974-scalar-excursion-separation-2026-10-23.md): c=1, width9,
M=23/100, I=[-3,3], phase plateaux+1 on[-2,-1] and-1 on[1,2], zero
endpoint trace/area, opposite phase0. The full bounded-measurable optimum
J_star=4+2D(t)^2/K(t) and its unique phase phi_star are reused at that scope.
The root t and lambda=D/K are as defined in
[K1969](k1969-scalar-continuum-separation-2026-10-22.md), with
0.06<lambda<0.07.

In characteristic coordinates write v(u,z)=V((z-u)/2,(z+u)/2). Then

    phi(u)=(1/2) int_0^9 v(u,u+s) ds.                       (1)

If v is C1 on the closed moving strip, differentiation under the fixed
s-integral makes phi C1 for interior u. The same conclusion holds for a
C1 extension to a neighborhood, including smooth compactly supported pulses.
No boundary-zero convention is needed for this statement.

But on[2,3] the unique optimum is

    phi_star(x)=x-3+(lambda/2)(x-2)(3-x),
    phi_star'(2+)=a=1+lambda/2>1,

whereas the plateau forces phi_star'(2-)=0. The continuous phase has a
nonzero derivative jump; an a.e.-equal C1 function would equal it everywhere,
which is impossible. Strict phase uniqueness therefore rules out attainment
of J_star by EVERY C1 pulse in this declared class. It rules out smooth
attainment, not the existence of the bounded measurable optimizer.

No claim is made that the infimum over smooth exact-endpoint pulses equals
J_star. Smoothing while preserving amplitude, both marginals and exact
plateaux requires a separate construction; nonattainment alone proves no
strict infimum gap without a fixed derivative bound.

## 2. A positive energy penalty at any fixed phase-curvature bound

Let phi be any fully feasible phase with globally Lipschitz derivative and
|phi''|<=L almost everywhere on the free intervals, with C1 matching to the
plateaux. Then phi'(2)=0 and phi(3)-phi(2)=1 imply

    phi'(2+y)<=Ly, 1=int_0^1 phi'(2+y)dy<=L/2,

so necessarily L>=2. For the optimum,
phi_star'(2+y)=a-lambda y. Hence on0<=y<=h=a/(L+lambda)<1,

    phi_star'(2+y)-phi'(2+y) >= a-(L+lambda)y >=0.

The left outer free interval gives the identical estimate without assuming
that the competitor is odd. The exact projection inequality from K1974 is
J(phi)-J_star>=||(phi-phi_star)'||_2^2. Integrating these two disjoint
triangles gives the quantitative theorem

    J(phi)-J_star >= 2a^3/[3(L+lambda)] >0.                (2)

The factor2 is for the two outer ramps; no contribution from the central
corners is needed. This is a conservative universal lower bound, not a
sharp curvature-constrained optimum or an equality construction.

## 3. Released physical pulse-resolution law

If the physical pulse is C2 and ||partial_x^2 V||_infinity<=B, then
(partial_u+partial_z)^2 v is exactly partial_x^2 V. Equation(1) gives

    ||phi''||_infinity <=9B/2.

Thus every feasible such pulse requires B>=4/9 and obeys

    J(V)-J_star >=2a^3/[3(9B/2+lambda)].                   (3)

Conversely, a requested energy excess at most epsilon>0 necessarily requires

    B >= max(4/9, (2/9)[2a^3/(3epsilon)-lambda]).          (4)

This is a NECESSARY curvature cost, not a sufficient pulse design. It locates
one concrete resource diverging in any C2 sequence that might approach the
measurable optimum. The claim does not assume such a sequence exists at the
fixed amplitude, and makes no assertion about its time derivative or bandwidth.

## 4. Checks and hostile review

The producer re-isolates the algebraic contact and records10 exact positive
curvature-gap certificates from L=2 through1024. The separate symbolic probe
reconstructs the phase corner, integrates the ramp error, differentiates an
actual polynomial on moving characteristic limits, checks the root bracket
and certificates, and rejects four mathematical faults. Its16 checks are
algebraic/rational obligations, not16 independent theorems. A structural
SymPy equality needed simplification before its baseline passed; this was a
harness issue, not counted as a hostile mathematical fault.

The principal overclaim to avoid is equating smooth nonattainment with a
strict smooth infimum gap. The strongest contrary possibility remains an
unbounded-curvature sequence at fixed amplitude and exact endpoints. The
weakest unbuilt seam is precisely that constrained smoothing/disintegration,
not another scalar cut certificate. Explicit measurable pulse construction
remains useful; smooth optimum search at J_star is retired.
This is GU-independent conditional scalar mathematics, with no external
expert, formal certification or novelty claim. SC-META-53 stays UNCERTAIN;
LT-SM8/LT-GR6b/AC-F1/RA-F1 and all source/ledger/canon verdicts are unchanged.
