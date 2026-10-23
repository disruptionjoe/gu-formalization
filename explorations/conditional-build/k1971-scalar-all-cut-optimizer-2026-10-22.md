---
title: "K1971: Every interval passes, but arbitrary cuts remain open"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1971_scalar_all_cut_optimizer.py
  - tests/channel-swings/k1971_scalar_all_cut_optimizer_probe.py
---

# K1971: Every interval passes, but arbitrary cuts remain open

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
result: all-interval and complement-interval feasibility, plus a universal small-mass cut exclusion
carrier: K1969 fixed scalar two-characteristic tube of width9 on [-3,3] LAYER=toy CHIRALITY=N/A
pairing: Lebesgue cut marginals and Dirichlet phase energy ON=three_free_intervals
real_structure: real H1 phase and measurable cut indicators
grading: characteristic directions only; no source chirality
action_owner: repository-construction -- fixed scalar control
target: constrain full measurable-cut feasibility without asserting it MAP-TYPE=intertwiner
```

## 1. New scope and retained open question

Keep the EXACT algebraic phase phi of
[K1969](k1969-scalar-continuum-separation-2026-10-22.md), with M=23/100,
its isolated quartic root t, multiplier lambda and energy J_half.
Every interval A=[a,b] in[-3,3], and every complement of an interval, obeys

    |int_A phi| <= (M/2) C(A).                          (1)

This includes arbitrary real endpoints and both signs, not just a finer grid
of halfcuts. Moreover every measurable cut with
min(|A|,6-|A|)<=7/23 passes. A finite-union violation therefore needs a genuinely
disconnected shape that is not just two exterior tails, and sufficient mass.

The all-measurable-cut problem is STILL OPEN. Exact finite min-cut scouts on
48,96 and192 cells found no violation of a rational surrogate. Those scouts
are not a continuum certificate of phi, and this result does not claim the
full scalar optimum or the existence of a pulse with energy J_half.
The inherited all-halfcut counterexample was a DIFFERENT perturbed phase.

## 2. Closed interval capacity

Put s=b-a, u=a+3 and v=3-b. Direct sliding-window integration gives

    C([a,b])=9s-(s-u)_+^2-(s-v)_+^2,   s<=3;
    C([a,b])=9(u+v)-u^2-v^2,           s>=3.            (2)

One derivation uses K1969's cumulative path. In the first case its excursions
above0 and below2s-6 are triangular with heights(s-u)_+ and(s-v)_+;
their areas are the two squares. In the second case use the complement's two
exterior intervals of lengths u,v: its excursion areas are u^2 and v^2.
Both formulas agree at s=3. The factor from characteristic coordinates is
already in the fixed cut convention; no Jacobian is changed.

## 3. All intervals on the positive-phase half

On[-3,0], phi is nonnegative and at most the affine tent/plateau phi0.
It equals1 on[-2,-1]. On[-3,-2] its derivative is at least
1-lambda/2>193/200>4M. K1969 proves every halfcut, using the exact quartic
contact. These properties suffice for the following proof.

For a<=b<=0 write u=a+3, z=b+3. If u>=z/2, (2) gives C=9(b-a).
Since phi<=1 and9M/2-1=7/200>0, (1) is strict for a nonempty interval.
Only u<z/2 needs work.

First suppose b>=-3/4. With b fixed, let
D(a)=int_a^b phi-(M/2)C([a,b]). In the active-capacity region,

    D'(a)=-phi(a)+(M/2)(21+8a-4b).

At a=-3, D'=M(-3-4b)/2<=0. On[-3,-2],
D''=-phi'+4M<0, so D decreases from its halfcut value, which is nonpositive.
From a=-2 to the active-region endpoint a=(b-3)/2, the start lies in the
plateau: D is convex because D''=4M. Its maximum is at an endpoint;
one endpoint was just bounded, and the other has C=9(b-a) and strict slack.
This proves the late-endpoint region.

For b<=-3/4, replace phi by its upper bound phi0. If z<=1, active u<z/2
makes the average phi0=(u+z)/2<=3/4, while C/(b-a)>=9-z>=8.
The cut demand is therefore strictly below its capacity.

For1<=z<=2 and0<=u<=min(1,z/2), the exact affine deficit is

    (23/200)z^2-(7/200)z-1/2
       +(23/200)(9-4z)u-u^2/25.                       (3)

For fixed u it is convex in z, so only z=2, z=1 when allowed, and z=2u
need inspection. At z=2 it is at most-7/200 for0<=u<=1.
At z=1 and u<=1/2 it is at most-57/400. The z=2u boundary is the strict
C=9s case already handled.

For2<=z<=9/4 and0<=u<=1, the exact deficit is

    D0(u,z)=-(77/200)z^2+(393/200)z-5/2
       +(23/200)(9-4z)u-u^2/25.                       (4)

Its Hessian has negative determinant, so it has no interior local maximum.
On u=0 it increases up to the upper endpoint; on u=1 it decreases from z=2;
on z=2 it increases up to u=1; and on z=9/4 it is
-89/3200-u^2/25. All four edges are negative (the other maximum is-7/200).
If1<=u<=z/2, the start is in the plateau and the deficit is convex in u;
its endpoints u=1 and u=z/2 are already covered. This proves all left-half
intervals. Odd reflection proves all right-half intervals with the opposite sign.

## 4. Cross-zero intervals and complements

For a=-r<0<b with s=r+b<=3, reflection permits assuming r>=b:
the integral is then nonnegative because the primitive of the odd sign-definite
phase decreases with distance from0. Formula(2) gives

    dC/db=9-2(2r+b-3)_+-4(r+2b-3)_+ >=0.              (5)

If neither excursion occurs this is9; if only the first occurs it is at
least3; the second cannot occur alone since r>=b. If both occur it is
27-8(r+b)-2b>=0, using r+b<=3 and b<=3/2.
Adding the negative-phase part[0,b] thus reduces the signed integral and
cannot reduce capacity. The already-proved interval[a,0] controls this case.

If s>=3, its complement consists of exterior tails of lengths u,v with
u+v<=3. Its capacity is the SUM of the two halfcut capacities
u(9-u)+v(9-v), by(2). The absolute integral is at most the sum of their
absolute integrals, so the inherited halfcut bounds prove (1).
Finally C(A)=C(A^c) and int phi=0 prove every complement-interval assertion.
No uncrossing theorem for arbitrary unions was used or assumed.

## 5. Released whole-measurable-cut exclusion

For any measurable A of mass s<=3, the cumulative path has total upward
variation s. Each excursion outside[2s-6,0] has equal up/down length q_j and
area at most q_j^2: the unit-speed triangular excursion is the largest one
with that up length. The disjoint excursion up lengths sum to at most s.
Hence the total exterior area is at most sum q_j^2<=s^2, also for countably
many excursions by monotone limits. K1969's exact path identity therefore gives

    C(A)>=s(9-s).                                      (6)

Since |phi|<=1, |int_A phi|<=s. If s<=9-2/M=7/23, (6) implies (1).
Use the complement when |A|>3. This is a universal measurable-set estimate,
not a finite-union approximation. It narrows the remaining separator search;
it does not eliminate larger disconnected cuts.

## 6. Verification and next discriminator

The producer compares(2) against full sliding-window integration for300 exact
rational intervals and checks the analytic sign/boundary constants. The separate
probe reconstructs465 capacities and the polynomial boundary argument, plus
excursion partition controls; four actual mathematical faults follow a green
baseline. The all-interval quantifier follows sections3-4's proof, not those
samples. The finite graph scouts use t equal to the midpoint of the certified
root interval and lambda=D(t)/K(t); exact arithmetic certifies their grid cuts
only. They are explicitly not claimed as algebraic-phi or continuum certification.

The first producer run exposed an accidental Python integer division producing
a floating zero in the polynomial helper; converting both arguments to exact
rationals repaired it before the final replay. This was a harness error, not
an adverse mathematical result or a counted mutation.

[Capacity-constrained transport duality](https://arxiv.org/abs/1307.7774) is
prior mathematical context; its abstract was rechecked. It does not supply the
missing all-cut certificate for this phase. Next seek a genuinely disconnected
violating cut of sufficient mass or construct the full path/HJB certificate.
No source, ledger or canon verdict moves. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b/AC-F1 remain NEEDS. This scalar model is not identified with GU.
