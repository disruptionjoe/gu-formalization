---
title: "K1990: Small-spacing rigidity and a sharp eight-level threshold"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1990_small_dimension_thermal_frontier.py
  - tests/channel-swings/k1990_small_dimension_thermal_frontier_probe.py
---

# K1990: Small-spacing rigidity and a sharp eight-level threshold

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
result: spacing independence through dimension7 and an actual dimension8 strict advantage
carrier: finite nondegenerate catalyst and four-level Gibbs bath in the fixed exact channel LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving unitaries with arbitrary coherent preparations
grading: actual energy resonance components, not source chirality
action_owner: repository-construction -- unchanged thermal channel
target: exact dimension threshold for benefit from subunit energy spacing MAP-TYPE=intertwiner
```

## Result on arbitrary real spectra

Let F_d(delta,E,t) be [K1987](k1987-thermal-spacing-parametric-frontier-2026-10-23.md)'s
exact-channel return optimum with AT MOST d physical levels, minimum spacing
delta>0, ground0, mean energy at most E and bath weights t^b/Z,0<t<1.
For every3<=d<=7, every0<delta<=1 and every E>=1,

    F_d(delta,E,t)=F_d(1,E,t).                          (1)

Thus reducing minimum spacing below1 gives NO advantage through dimension7,
without assuming the original spectrum is rational or commensurate.
Dimension8 is the sharp first possible exception: at t=1/2,E=7/5,

    F_8(1/20,7/5,1/2) <=101/230 <81/182
                         = F_8(1,7/5,1/2).            (2)

The first witness in(2) is an upper bound; the released optimization below
improves it and proves the EXACT optimum109/250 at delta=1/20, as part of a
complete fixed-budget spacing curve. This does not supply an all-d rate.

## Structural proof of rigidity, with coherent protocols included

Reuse [K1968](k1968-joint-thermal-finite-dimension-program-2026-10-22.md)'s
covariant pinching, shell-rank necessity/sufficiency and exact sharp return
formula. Pinching preserves energy/dimension and supplies a diagonal comparison
with no greater return. This establishes a lower bound for arbitrary coherent
protocols; diagonal shell constructions attain the corresponding values.

Join physical energies whenever their difference is1,2 or3. A connected
component has integer differences after translating its minimum to0; distinct
components have disjoint bath/catalyst shells. Every component carrying any
preparation mass needs at least3 physical levels. The same shell count gives
at most floor((n−1)/2) occupied energies in a component of n levels. Therefore
components of size3 or4 have exactly one occupied energy and sharp normalized
return1/2. Their arbitrary mixtures also have return1/2.

A component with any prospect of improvement needs at least5 levels. Under
a total bound d<=7, it cannot coexist with a second mass-carrying component,
which would need another3. Hence any protocol beating1/2 has ALL preparation
mass in one component. Delete unrelated unoccupied components and translate
that component's minimum to0. Its energies are distinct integers, its mean
energy can only decrease, its dimension does not increase, and its shell
construction/return are unchanged. It is feasible at spacing1.

For return>=1/2, the three-level spectrum{0,1,2} prepared at1 already attains
1/2 with energy1. Thus every original protocol admits a spacing1 comparison
no worse in both budget and return. This proves F_d(delta)>=F_d(1); inclusion
of the spacing1 feasible set gives the reverse inequality. The proof covers
all temperatures and all real spectra and does not round levels into collisions.

## Released complete low-dimensional curves

For d=3 or4, the optimum is1/2 on the feasible domain. For d=5 and0<delta<=1,
[K1984](k1984-commensurate-spectral-rounding-2026-10-23.md)'s COMPLETE
all-temperature spacing1 curve now applies without modification. Set q=t^2,
e_c=(1+2q)/(1+q), e_s=(1+4q)/(1+q), e_a=(2+3q)/(1+q). Then

    F_5 = (3−E)/4                         for1<=E<=e_c,
          (2+q)/(4(1+q))                  for e_c<=E<=e_s,
          (3−E)/4+q/(2(1+q))             for e_s<=E<=e_a,
          (1+2q)/(4(1+q))                for E>=e_a.     (3)

The old d6/d7 curves at t=1/2 from K1968 likewise become ACTUAL attained
positive-spacing optima throughout0<delta<=1; no colliding tagged limit is
needed. For1<delta<=2, every feasible d>=3 still has return1/2 and requires
E>=2 by K1981. These results retain K1987's full feasibility conditions.
No new all-temperature d6/d7 closed formula is asserted.

## Exact spacing1 dimension8 comparison

At spacing1, K1984's rounding/compression preserves an original protocol and
lowers its energy, leaving all gaps in{1,2,3}. Thus it suffices to enumerate
CONNECTED integer shapes with at most8 levels, including shapes created by
joining previously disconnected components. All3276 gap words with3--8 levels
are enumerated. Shell-rank tests and Pareto-safe pruning leave60 occupied
support/completion pairs. The existing exact cell-vertex method constructs
690 probability cells and1022 vertices; its complete connected-d8 budget
curve equals K1968's d7 curve at t=1/2. In particular the interval
[113/91,409/273] has value81/182 and contains E=7/5.

A separately assembled check enumerates shell occupancy, verifies coverage of
all valid supports, and at E=7/5 constructs all probability-arrangement
vertices from positivity, balance, deficit and budget hyperplanes. It directly
minimizes the shell-return formula and independently obtains81/182. This
fixed-budget check is the comparison needed for(2); it does not pretend to
independently prove every symbolic-temperature curve.

## Actual eight-level family and its useful range

For0<delta<=16/165 choose two components

    A={0,1,2,3,4},       B={delta,1+delta,2+delta}.

They are nondegenerate, their union has minimum spacing delta, and no
cross-component shell is resonant. On A use the known t=1/2 five-level
optimum at mean11/5: probabilities2/5 at1 and3/5 at3, return3/10.
On B prepare1+delta purely, with normalized return1/2. Give component A mass

    alpha=(2/5−delta)/(6/5−delta),

and component B mass1−alpha. The mean is EXACTLY7/5 and the sharp return is

    R_delta=1/2−alpha/5.                               (4)

Shell-rank sufficiency supplies actual conserving unitaries for this diagonal
preparation; this is not a tagged degenerate limit. Equation(4) is below81/182
precisely when delta<16/165, and equal at the displayed endpoint.
For delta=1/20 the physical spectrum is

    {0,1/20,1,21/20,2,41/20,3,4},

with probabilities14/115 at1,21/115 at3 and16/23 at21/20. Its exact return
is101/230. Every smaller dimension is ruled out as a spacing-benefit mechanism
by(1), proving sharpness of the dimension threshold8.

## Released follow-through: the COMPLETE eight-level spacing curve at this budget

The witness above is not optimal. Moving the LOWER-MASS five-level component
up by delta, while placing the pure component at ground0, costs less energy.
This leads to a matching lower bound and, for ALL0<delta<=1,

    F_8(delta,7/5,1/2)
       = min(81/182, 1/2 − 2/[5(6+5delta)]).            (5)

The strict-improvement threshold is delta<32/125. At delta=1/20 the exact
value is109/250, improving the earlier101/230 witness. For delta>1 the
energy budget7/5 is infeasible, as already settled by K1987.

Here is a complete classification behind(5), not interpolation of samples.
If all occupied components have size<=4, return is1/2. If all mass lies in
one component, integer translation and the connected-d8 certificate give
return>=81/182. The only remaining potentially improving partition is5+3.
K1984's complete five-level classification makes its improving component
{0,1,2,3,4} with normalized populations p at1 and1−p at3. A three-level
component has a single occupied level at least1 above its minimum.

Let alpha be the five-level component mass. The return benefit below1/2 is
alpha b(p), where, at t=1/2,

    b(p)=p/2                for0<=p<=2/5,
         2/5−p/2           for2/5<=p<=4/5,
         p/2−2/5           for4/5<=p<=9/10,
         (1−p)/2           for9/10<=p<=1.

One component minimum is0; the other's minimum is at least delta. The mean
is therefore at least one of

    1+alpha[2(1−p)+delta]                (five-level shifted),
    1+2alpha(1−p)+delta(1−alpha)          (pure component shifted). (6)

These are necessary lower bounds for every real placement, whether or not
placing components exactly at these offsets respects all intervening gaps.

For p>=4/5, b(p)<=1/20, so this region cannot beat81/182, whose benefit
is5/91>1/20. For p<=4/5 and the first case of(6), maximize
b(p)/[2(1−p)+delta]. It increases up to p=2/5 and decreases thereafter:
on the two linear pieces the derivative numerator is respectively
1+delta/2 and −1/5−delta/2. Since the available budget above1 is2/5,

    alpha b(p) <= 2/[5(6+5delta)].                     (7)

For the second case, if delta<=2/5 the same two-piece calculation maximizes
b(p)/[2(1−p)−delta] at p=2/5; its upper benefit is
(1/5)(2/5−delta)/(6/5−delta), no greater than(7). If delta>2/5 and p<4/5,
the two endpoint costs delta and2(1−p) both exceed2/5, so that case is
infeasible. The p=4/5 boundary has zero benefit. This proves the lower
bound in(5) for every real delta, without assuming a realizable relaxed placement.

For delta<=32/125<1/2, attain(7) with pure spectrum{0,1,2} and five-level
spectrum{delta,1+delta,2+delta,3+delta,4+delta}, alpha=(2/5)/(6/5+delta),
and p=2/5. All gaps are at least delta, all shell-rank constraints hold,
and the mean is EXACTLY7/5. For larger delta<=1 use the actual connected
spacing1 optimizer of value81/182. Thus the lower bound is matched on
every interval. At the transition both constructions attain the same value.

The separate checker independently solves the tagged three-population
piecewise-linear program at100 rational spacings plus the exact transition,
and checks the actual minimizing spectra where they are used. Those controls
validate the formulas; the case split and ratio derivatives prove the full
continuum of spacings. Other budgets/temperatures remain distinct questions.

## General two-template reduction and executed full energy curve

The same component proof has a stronger useful consequence. For ALL0<t<1,
ALL E>=1 and0<delta<=1/2, the dimension8 problem reduces exactly to:

1. the connected integer spectra with at most8 levels and gaps1,2,3;
2. the actual spectrum{0,1,2} union{delta,1+delta,...,4+delta}; and
3. the actual spectrum{0,1,2,3,4} union{delta,1+delta,2+delta}.

For the last two templates the five-level component uses its allowed support
1,3 relative to its minimum and the pure component uses relative level1.
Optimize their three populations using the existing exact shell formula and
the actual shifted energy coefficients. The component classification proves
exhaustion. Inequalities(6) prove every original5+3 placement is dominated
in energy by one of the two templates without changing normalized component
return. Both templates have the required minimum spacing when delta<=1/2.
All-pure components are dominated by{0,1,2}, while all-mass-in-one-component
protocols reduce to the first family. This proof handles arbitrary real
spectra and coherent preparations through the previously stated pinching.

For rational delta,t,E, these are finite rational probability programs on
actual nondegenerate spectra, so the optimum is rational and attained. At
fixed delta,t the full budget curve is a finite piecewise-affine lower envelope,
with exact rational pieces when those parameters are rational. No convex hull
across distinct physical templates is silently taken.

The complete curve at delta=1/20,t=1/2 was executed, with entries below
meaning value=mE+b on the stated interval; shared endpoints agree.

| E interval | m | b |
|---|---:|---:|
| [1,6/5] | −1/4 | 3/4 |
| [6/5,113/91] | −9/76 | 45/76 |
| [113/91,489/364] | 0 | 81/182 |
| [489/364,13/8] | −4/25 | 33/50 |
| [13/8,11/5] | −4/23 | 157/230 |
| [11/5,19/8] | −3/28 | 15/28 |
| [19/8,317/104] | 0 | 9/32 |
| [317/104,67/19] | −13/140 | 79/140 |
| [67/19,infinity) | 0 | 9/38 |

The producer enumerates the actual probability cells and their exact vertices,
then combines the connected and two tagged template envelopes. The separate
probe independently checks every breakpoint and an interior point of every
piece by direct arrangement minimization. Complete piecewise coverage comes
from the producer's exact envelope construction and the exhaustive template
proof, not those spot controls alone. The reused integer-gap rate routine
initially rejected rationally represented integer gaps; the caller now verifies
integrality before converting them. No coefficient rounding is used.

## Verification and next boundary

The producer checks100 all-temperature/spacing/budget instances of(3), the
complete connected-shape program, and four initial noninteger family members and nine optimal-spacing controls.
The independent probe has515 coverage/optimization/witness controls and rejects
four coverage, curve, spectrum and return faults after baseline. The arbitrary
real-spectrum and all-temperature assertions rely on the structural proof;
the finite checks validate its exact low-dimensional consumers. Both are
internal checks, without an external reviewer or formal proof certificate.

The remaining thermal question is a closed symbolic-temperature solution of
the explicit templates, the delta>1/2 placement problem away from E=7/5, or
a general dimension/spacing lower bound. The full delta1/20,t1/2 budget curve
and fixed t=1/2,E=7/5 spacing family are now matched; do not requeue it or small-spacing benefit
below dimension8. This independent
thermal model is not source-selected GU physics; SC-META-53 remains UNCERTAIN,
and source, physics-ledger and canon verdicts remain unchanged.
