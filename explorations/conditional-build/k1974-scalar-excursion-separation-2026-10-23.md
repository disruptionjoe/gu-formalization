---
title: "K1974: Exact full scalar optimum from measurable-cut reduction"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1974_scalar_excursion_separation.py
  - tests/channel-swings/k1974_scalar_excursion_separation_probe.py
---

# K1974: Exact full scalar optimum from measurable-cut reduction

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
result: all measurable cuts reduce to a left interval; exact full optimum and mandatory pulse saturation
carrier: fixed scalar two-characteristic width9 tube and phase on [-3,3] LAYER=toy CHIRALITY=N/A
pairing: Lebesgue marginal constraints and Dirichlet phase energy ON=three_free_intervals
real_structure: real H1 phase and measurable bounded pulse
grading: two characteristic directions, not source chirality
action_owner: repository-construction -- fixed conditional model
target: full scalar measurable-pulse energy minimum MAP-TYPE=intertwiner
```

## 1. Full result

Keep EXACTLY [K1969](k1969-scalar-continuum-separation-2026-10-22.md)'s
algebraic phase phi, M=23/100, c=1, T=9/2, width9, trace and plateau data.
Its all-halfcut optimum is now proved feasible for EVERY measurable cut.
Consequently the full measurable-pulse energy minimum is

    J_star=4+2D(t)^2/K(t), approximately4.000917578239,
    101t^4-102t^3-168t^2+392t-138=0, 9/20<t<23/50,
    K=1/6-t^2/2+2t^3/3-t^4/4,
    D=-7/100+69t/200-77t^2/200.                         (1)

The exact polynomial and isolating interval, not the decimal, define it.
The unique optimal PHASE is K1969's phase. The inherited cut-sufficiency
 theorem supplies a bounded measurable pulse realizing it. This is an
existence result, not an explicit pulse array or smooth-pulse attainment.
K1969's perturbed halfcut-feasible counterexample remains valid: the theorem
below uses additional sign and shape properties that its ripple violates.

The new proof has three exact reductions. It replaces a global search over
all disconnected cuts with the already-certified interval inequalities in
[K1971](k1971-scalar-all-cut-optimizer-2026-10-22.md).

## 2. Remove reflection-paired points by submodularity

Let R x=-x and let C(A) be the exact sliding-window capacity from K1942.
It is complement symmetric, reflection invariant and submodular:

    C(A intersection B)+C(A union B)<=C(A)+C(B).         (2)

For each window its contribution is f(a)=min(a,ell-a), a concave function
of the occupancy measure. Writing the intersection measure as z and the
two disjoint remainders as p,q, concavity gives
f(z)+f(z+p+q)<=f(z+p)+f(z+q); integrate over windows. This proof applies to
arbitrary measurable sets, not just finite unions.

For any A set B=R(A^c), I=A intersection B and U=A union B. Then
U=R(I^c), so C(U)=C(I), while C(B)=C(A). Thus C(I)<=C(A).
I contains at most one point from almost every reflected pair. The removed
part A intersection R(A) is symmetric, and oddness of phi gives

    int_I phi=int_A phi, |I|<=3.                       (3)

Hence removal does not decrease the positive signed deficit.

## 3. Fold every remaining point into the positive half

Let P=(I union R(I)) intersection[-3,0]. It has the same mass s as I,
and int_P phi>=int_I phi because phi>=0 on[-3,0] and is odd.
It also has NO GREATER capacity. Here is the exact convexity argument.
For0<=x<=3 let L and H be I's occupancies in[-3,-3+x] and[3-x,3].
Define f_s(w)=dist(w,[2s-6,0]). K1969's cumulative-path identity, paired
at x and6-x, expresses I's excursion contribution as

    f_s(2L-x)+f_s(2H-x).

For P the corresponding contribution is

    f_s(2(L+H)-x)+f_s(-x).

The second pair has the same sum as the first, a no-smaller maximum and a
no-larger minimum. Convexity of distance to an interval therefore makes its
sum no smaller. Integrating gives greater excursion area, hence
C(P)<=C(I), since C=9s-excursion_area. We have proved

    int_A phi-(M/2)C(A) <= int_P phi-(M/2)C(P), P subset[-3,0]. (4)

This covers cuts of ANY original mass; (3) supplied s<=3. Reflection changes
the sign of the integral while preserving capacity, so it suffices to control
the positive deficit. These two set reductions use only oddness and the
one-half sign condition, not the special quartic equation.

## 4. Every one-half measurable cut is dominated by an interval

Fix s in[0,3], use x in[0,3] for the negative phase half, and relax the
indicator to0<=a(x)<=1 with int a=s. Let F(x)=int_0^x a and W=2F-x.
No lower excursion is possible: F>=max(0,s-3+x) implies W>=2s-6.
The part beyond x=3 is fixed by s. Thus the positive deficit equals

    D_s(a)=int_0^3 phi(x-3)a(x)dx -9Ms/2
           +(M/2)[int_0^3 (2F(x)-x)_+ dx +(2s-3)_+^2/2]. (5)

This is a continuous convex functional on a weak-star compact slice of L-infinity.
For completeness, weak-star convergence makes each F(x) converge; the uniform
Lipschitz bound upgrades it to uniform convergence, so the nonlinear integral
is continuous. The linear term is weak-star continuous. A maximum a_star exists.

Choose theta(x) in the subgradient of w_+ at W_star(x): theta=1 for W>0,
0 for W<0 and any measurable value in[0,1] for W=0. A subgradient of(5) is

    h(x)=phi(x-3)+M int_x^3 theta(y)dy,
    h'=phi'(x-3)-M theta(x).                           (6)

K1969's exact lambda in(0.06,0.07) gives phi'>=1-lambda/2>M on[0,1],
phi'=0 on[1,2], and phi'<0 on[2,3]. Therefore h strictly increases up to1
and is nonincreasing thereafter (strictly decreasing after2). Its upper-level
sets are intervals. Filling its highest levels with total mass s yields an
INTERVAL indicator b, including any needed contiguous portion of a flat level.

The subgradient inequality gives D_s(b)>=D_s(a_star)+int h(b-a_star).
The last integral is nonnegative because b maximizes that linear functional.
But a_star already maximizes D_s, so equality holds and b is also a global
maximizer. This step is deliberately in the correct direction for a CONVEX
MAXIMIZATION; an unsupported stationarity/minimum argument would be wrong.
Thus every measurable P is dominated by an interval of the same measure.
K1971 proves all such intervals pass for the exact phase. Combined with(4)
and reflection, EVERY signed measurable cut passes.

## 5. Released optimality, stability and mandatory saturation

K1942/K1914 give measurable-pulse existence from all cuts, so phi is feasible
at M. K1969 gives the matching halfcut lower bound and strict-convex phase
uniqueness. This proves(1) without a finite-grid-to-continuum inference.
The two algebraic halfcuts at -t,+t carry the matching positive multipliers
lambda=D/K. They need not be rational members of K1942's rational enumeration;
its rational supremum converges to the same value.

For any admissible physical pulse of energy U, the now-known exact optimum
gives the effective phase-error bounds

    ||(phi_p-phi)'||_2^2 <= U-J_star,
    ||phi_p-phi||_infinity^2 <= (U-J_star)/2.            (7)

These are inherited projection inequalities with a newly closed exact target,
not an assertion that pulse fields themselves are close or unique.

There is also new necessary information about EVERY optimal pulse. In
characteristic coordinates v(u,z), each row has integral0 and |v|<=M, and
2phi(u)=int v(u,z)dz. Saturation of either contact cut means its rowwise
inequality is saturated for almost every z. If the cut occupies no more than
half the row, v=+M almost everywhere on the cut; if it occupies at least half,
v=-M on the row complement. At equality both conditions apply. The two
contact cuts are nested, so their forced signs never conflict.
In the full-window rectangle z in[3,6], every optimizer therefore obeys

    v(u,z)=+M for -3<u<-t,
    v(u,z)=-M for t<u<3,
    int_(-t)^t v(u,z)du=0.                             (8)

This gives actual forced regions and a remaining marginal construction problem,
not a manufactured smooth representative. A pulse kept uniformly below M on
all these positive-measure regions cannot attain J_star.

## 6. Verification and hostile scope

The producer checks4096 exact left-side grid subsets plus1024 arbitrary full
cuts under removal/folding for a rational surrogate. The separate probe checks
7622 rational window/convexity/capacity/rearrangement obligations and rejects
six mathematical faults. Universal coverage follows sections2-4, not those
finite examples. Algebraic root/energy, interval feasibility and cut-sufficiency
are explicitly reused dependencies; no change to their formulas or toolchains.
The [Bauer maximum-principle literature](https://arxiv.org/abs/1812.07243)
is background for convex maxima; the proof above uses a direct interval
subgradient construction and establishes its hypotheses here.
No novelty, external expert or proof-assistant certification is claimed.

The prior general halfcut insufficiency and grid counterexamples remain in
force. Only this typed phase now has full feasibility. An explicit measurable
pulse, regularity/uniqueness of pulse fields, other amplitudes and short tubes
remain separate questions. This is GU-independent scalar mathematics;
SC-META-53 remains UNCERTAIN and LT-SM8/LT-GR6b/AC-F1 remain NEEDS. No source,
physics-ledger or canon verdict moves.
