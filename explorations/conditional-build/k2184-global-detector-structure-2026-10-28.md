---
title: "K2184 Nonconvexity on exact detector-contrast slices"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2184_global_detector_structure_probe.py
---

# K2184 Nonconvexity on exact detector-contrast slices

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2184 exact-contrast nonconvexity and optimized curvature
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

The squeeze-optimized profile energy is not convex, even after fixing a positive
contrast exactly. For every contrast d in (0,129/102400], two explicitly given
admissible infinite-occupation profiles have that contrast, while their midpoint
has strictly greater optimized energy than the average endpoint energy.
Outcome exchange supplies the corresponding negative contrasts.

This closes the proposed global-convexity route to optimizer uniqueness and
threshold saturation. It does **not** disprove either conclusion: nonconvex
objectives can have unique minima and increasing constrained minima. The
exact-contrast frontier F(d), global threshold saturation, and joint-squeeze
uniqueness remain open. K2182's local endpoint theorem is unchanged.
The quantitative gap also separates this profile functional from its convex
envelope at the specified midpoint; it is not a certified gap between the
actual minimum and a particular relaxed optimization problem.

This is GU-independent mathematics of the supplied positive free scalar Fock
binary diagonal instrument. It concerns vacuum output field energy only, with
no apparatus, clock, preparation, switching or reset account. SC-META-53 remains
UNCERTAIN; ledger0.263, LT-SM8/LT-GR6b, canon and physical quotient are unchanged.
No source, novelty, external-expert or proof-assistant claim is made.

## Model and reduction

Reuse [K2180](k2180-detector-contrast-frontier-2026-10-28.md) and
[K2182](k2182-uniform-detector-endpoints-2026-10-28.md):

    p_n=(3/4)4^-n, q_n=3n-1, 0<=x_n<=p_n, y=p-x,
    R(x)=sum(n+1/2)x_n, T(x)=sum(n+1)sqrt(x_n x_(n+1)),
    C=40/3, A(s)=41s²/6+3/(2s²), S=[2/3,113/100].

The optimized profile energy is

    H(x)=g(R(x),T(x))+g(R(y),T(y))+35/18,
    g(R,T)=min_(s>0) [R A(s)-CsT]=R f(T/R).

For R>0 the squeeze minimizer is unique because A''=41/3+9/s^4>0.
Every admissible profile has a representative minimizer in S; for the profiles
below it lies strictly inside S. Differentiation at this minimizer gives

    A'(s(t))=Ct, f'(t)=-Cs(t), f''(t)=-C²/A''(s(t)).       (1)

On S, A''<=2843/48, so f''<=-m, m=25600/8529.
The strict concavity in t is the effect of optimizing a shared squeeze.
Fixed-squeeze convexity in x does not survive automatically.

## Two profiles on the same contrast hyperplane

Let u have only u1=129/2048=(43/128)p1 nonzero. Let v have only
v3=p3=3/256 and v4=p4=3/1024 nonzero. Then

    d(u)=d(v)=129/1024,
    Ru=387/4096, Tu=0, Rv=111/2048, Tv=3/128,
    Tu/Ru=0, Tv/Rv=16/37.

For 0<epsilon<=1/100 set x_theta=epsilon[(1-theta)u+theta v],
0<=theta<=1. All coordinates obey their caps, all profiles have the same
contrast d=129epsilon/1024, and the click tail is identically zero.
The occupied blocks {1} and {3,4} are separated by the zero coordinate2.
Consequently R and T are both affine in theta: there is no cross-block
square-root edge hidden in this calculation.

Strong concavity of f in (1), with the perspective weights
Ru/(Ru+Rv) and Rv/(Ru+Rv), proves the click midpoint gap

    g(R(x_1/2),T(x_1/2))
      -(g(R(x_0),T(x_0))+g(R(x_1),T(x_1)))/2 >= epsilon D,
    D=m Ru Rv/(4(Ru+Rv)) (16/37)^2=103200/21353773.       (2)

## The infinite complement cannot cancel the gap

Write a=43/128, z1=1-epsilon a(1-theta), z3=1-epsilon theta.
Only occupation factors1,3,4 differ from the geometric complement p.
Summing every edge, including the exact infinite tail, gives

    T(y_theta)=2/3-(9/16)(1-sqrt(z1))
      -(159/2048)(1-sqrt(z3))-(3/128)(1-z3).             (3)

Edges0+1 give9/16, edges2+4 give159/2048, and internal edge3 gives3/128.
For epsilon<=1/2 all z>=1/2, hence z^-3/2<=2sqrt(2)<3 and

    -T''(y_theta)<=3epsilon² J/4,
    J=(9/16)a²+159/2048=36993/262144.

For a path with affine R, the optimized second derivative is

    (g(R,T))''=-Cs T''
      -(A'(s)R'-CT')²/(R A''(s)).                     (4)

The last term is nonpositive. Therefore the complement h(theta) satisfies
h''<=Cs(-T'')<=(226/15)(3J/4)epsilon². The elementary midpoint curvature
inequality (obtained by subtracting this bound times theta²/2 and using
concavity) gives h(1/2)-(h(0)+h(1))/2 >=-K epsilon², where

    K=(226/15)(3J/32)=4180209/20971520.

Combining with (2),

    H(x_1/2)-(H(x_0)+H(x_1))/2 >=epsilon(D-K epsilon)>0. (5)

At epsilon=1/100 the exact rational lower bound is
127162852321443/4478210775449600000. For every smaller positive epsilon,
D-K epsilon>=D-K/100>0. This proves a continuum of nonconvex fixed-contrast
slices, rather than one sampled numerical failure. The convex envelope at the
midpoint is at most the endpoint average, so (5) also bounds the pointwise
convexification defect from below. It says nothing about whether the constrained
minimum lies on this chord.

## Stronger successor: probability and contrast both fixed

The obstruction persists when the click probability is also fixed. Keep v
above and replace u by u1=42/5120, u6=33/5120, all other entries zero.
The unscaled u need not obey the caps; the actual profile epsilon u does.
For 0<epsilon<=1/10000, every profile epsilon[(1-theta)u+theta v] is capped,
and both endpoint profiles have

    sum u=sum v=15/1024, sum n u_n=sum n v_n=3/64,
    R(u)=R(v)=111/2048, d(u)=d(v)=129/1024,
    T(u)=0, T(v)=3/128.

Thus both branch masses and both radii are fixed along the chord. Its disconnected
click supports again make T affine. The factors changed in the complement are
z1=1-epsilon(7/160)(1-theta), z6=1-epsilon(176/5)(1-theta),
z3=z4=1-epsilon theta. They are all at least1/2. The exact full coherence is

    T(y)=2/3-(9/16)(1-sqrt(z1))-(93/32768)(1-sqrt(z6))
       -(159/2048)(1-sqrt(z3))-(3/128)(1-z3).

The new edge group93/32768 is edges5+6, not a finite-tail approximation.
The same proof now gives

    D2=400/105191,
    J2=(9/16)(7/160)^2+159/2048+(93/32768)(176/5)^2=58905/16384,
    K2=(226/15)(3J2/32)=1331253/262144,
    midpoint gap >=epsilon D2-K2 epsilon²>0.

At epsilon=1/10000 the lower bound is
908540165677/2757518950400000000. All smaller positive epsilon retain the
strict gap. This disproves joint optimized convexity even on a fixed
probability-and-contrast slice. It does not contradict the established unique
fixed-squeeze optimization problem: changing the shared squeeze is essential.

Randomly mixing the two endpoint instruments would permit different squeeze
pairs conditioned on a hidden random label. That is a larger instrument class
than one squeeze per reported binary outcome. Averaging their binary effects
inside the declared class gives the midpoint profile and incurs the proved
gap. This distinction supplies an explicit obstruction to using randomization
as a silent convexification of the original instrument class. These rare-click
witnesses are nonoptimal; no minimum-energy value is inferred from them.

## Released curvature criterion and next useful question

For a finitely supported affine perturbation x(theta), at a regular profile
with positive branch masses and differentiable coherence, apply (4) separately
to x and p-x. Its exact curvature is the fixed-squeeze positive coherence
curvature minus two explicitly displayed nonnegative squeeze-response terms.
Convexity along that path holds precisely when the former dominates the sum
of the latter. The counterprofiles above show this domination can fail even
on sum q_n x_n'=0. No positive-semidefinite Hessian may therefore be used as a
universal certificate for this optimized problem.

A global frontier theorem now needs a contrast-changing descent adapted to
optimizing squeezes, a minimizer-specific inequality, or a global certified
nonconvex solver. A fixed-squeeze convex solver remains valid for its own
subproblem and K2176's certificates remain valid; it cannot by itself certify
joint uniqueness. Testing such a descent is a genuine successor, not another
cutoff calculation. A physical controller additionally needs its own shared
Hamiltonian and preparation/reset account.

## Verification and evidence kind

The written proof treats the entire infinite occupation chain. The executable
probe independently reconstructs profile moments, contrast, changed-edge and
geometric-tail formulas, constants and optimized rational interval enclosures.
It checks genuine altered weights, missing edges/tails and the curvature sign
after a green baseline. Finite controls supplement the proof, not replace it.
Independent internal review must inspect (1)--(5) and the actual final
probe/report before acceptance. No global optimum or new half-contrast energy
bracket is reported.
