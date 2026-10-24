---
title: "K2014: Exact ten-level optimum at unrestricted dimension near zero spacing"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2014_unrestricted_ten_level_onset.py
  - tests/channel-swings/k2014_unrestricted_ten_level_onset_probe.py
---

# K2014: Exact ten-level optimum at unrestricted dimension near zero spacing

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
result: compact-budget uniform finite-ray optimum and exact unrestricted ten-level small-spacing curve
carrier: fixed extreme four-state channel and positive-gap finite or countable catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance and upper mean energy ON=independent_initial_registers
real_structure: complex conserving unitaries and real diagonal populations
grading: physical energy components, not source chirality
action_owner: repository-construction -- unchanged K2008 exact thermal class
target: hard-budget finite-support reduction and exact optimal return MAP-TYPE=intertwiner
```

## 1. Main result

Keep K2008's finite-or-countable positive-spacing catalyst class, t=1/2 and
6/5<E<11/5. Put r=E-6/5 and B(E)=63/100-3E/20. There exists eta_E>0 such that
for EVERY0<delta<eta_E,

    F_infty(delta,E)=G(delta,E)
      := B(E)+(3/20)delta min(r/(1+delta),(1-r)/(1-delta)). (1)

The optimum is attained by an actual TEN-level catalyst: two five-level
ladders separated by delta, with the optimal A/B weights given below. This
settles hard-budget finite attainment and the full local spacing curve in
this regime despite the strict Lagrange duality gap. It does not settle the
whole positive-spacing frontier or arbitrary bath temperatures.

The threshold can be chosen uniformly for E in any compact subinterval of
(6/5,11/5). For rational interval endpoints a positive rational threshold is
computable by a finite exact program, but that25-level threshold calculation
has NOT been executed here. No sampled numerical delta is labeled globally
optimal merely because it is small. Formula(1) has an existential certified
regime; explicit candidate protocols at all sampled deltas are upper bounds.

This upgrades K1998's fixed-dimension eventual curve and K2012's unrestricted
Theta(delta) estimate. The missing ingredients were compact-budget uniformity
at ONE fixed dimension and the energy retained in the cutoff inequality.

## 2. Compact-budget uniformity at fixed finite dimension

Fix d>=10 and a compact interval K inside(6/5,11/5). For sufficiently small
delta, the complete K2006 programs have finitely many integer component
shapes, supports and return sign cones. The canonical offsets are0 for one
component or0,delta for two; connected single components are also included.
These cones and their normalized extreme rays do not depend on delta or E.
Within a product sign cone, lifting to its normalized single-component rays
makes return and mean linear in ray weights. Normalization and one energy
inequality admit an optimum on at most two rays. This is K1998's finite-ray
construction, now considered over ALL E in K at once.

Here is the uniformity proof, not a pointwise-to-uniform inference. Suppose
arbitrarily small deltas and E_j in K had a candidate beating G. Pass to a
subsequence with fixed ray labels and fixed shapes, E_j->E_* in K, and
convergent weights. G-B=O(delta) uniformly. The nonnegative supporting-gap
decomposition forces each positive limiting ray to have canonical equality
R+(3/20)e=63/100, zero limiting offset, and total limiting mean E_*.
K1950's complete equality census says every such normalized ray is precisely
A or B, with energies6/5 and11/5. Since E_* is strictly between these values,
BOTH ray weights are positive. There is no third vanishing ray: the chosen
vertex has at most two. Thus their fixed labels are exactly A and B, not
merely tending to them.

They cannot belong to the same sign cone in one component: linearity on that
cone would make their full segment a component equality face, contradicting
the two-point equality census. They therefore belong to distinct components.
Replace their unused completion levels by the actual five-level ladders,
with lower offset0 and higher offsetdelta. This preserves exact channel and
returns, cannot increase energies, and needs10 physical levels. Optimizing
its weights gives G, so the supposedly better candidate cannot beat G.
This contradiction proves a COMMON eta_(d,K)>0 on K.

All zero-delta singular bases are covered by the ray-weight argument. No
uniform finiteness in d is asserted. For rational K, exact finite sign cones,
ray enumeration and polynomial sign/root elimination over
0<delta<eta, E in K provide a terminating threshold procedure. Its large
program is specified, not run, and is not an efficient complexity claim.

## 3. Energy-sensitive removal eliminates unbounded dimension

Take a compact target interval I=[a,b] inside(6/5,11/5). Choose rho>0 so
K=[a-rho,b] remains inside that interval, and let eta_(25,K) be section2's
fixed25-level threshold. Set

    0<delta<min(eta_(25,K), 1/100, rho/6).                  (2)

Here N=9, d=2N+7=25, and c_N=11/50 in K2013. For any candidate
R<=G(delta,E), with E in I, its population q above9 satisfies

    q <= [G-B]/(11/50) <= (15/22)delta.                 (3)

The last inequality uses the feasible B-shift branch r/(1+delta)<=1.
Let E'=(E-9q)/(1-q). Since E>6/5 and delta<1/100,

    0<=E-E'=(9-E)q/(1-q)<6delta<rho.                  (4)

In particular E' belongs to K. K2013's physical truncation has at most25
levels, energy<=E' and return<=R+q/(1-q). Section2 therefore gives

    R >= G(delta,E')-q/(1-q).                           (5)

For fixed0<delta<=1/2, the two affine-in-E branches defining G have slopes
-3/[20(1+delta)] and -3/[20(1-delta)]. Each decreases with slope magnitude
at least m_delta=3/[20(1+delta)]. Their minimum obeys the same secant inequality, including
across the branch switch. Consequently

    R >= G(delta,E)+kappa_delta(E) q/(1-q) >=G(delta,E),
    kappa_delta(E)=[7-3E-20delta]/[20(1+delta)] >1/101.       (6)

The coefficient exceeds1/101 since E<11/5 and delta<1/100. Every R<=G is thus
at least G. The ten-level upper construction gives equality, including in
the countable class. This directly proves attainment; it does not exchange
an infimum over dimension with a fixed-d asymptotic.

The sharper exact branch slope permits cutoff9 and25 intermediate levels; the
coarser slope1/10 would need cutoff13 and33 levels. This reduces the finite
threshold program without asserting that either program has been executed.

The budget interval is essential. Substituting K1998's theorem only at E
would leave F_25(delta,E') unidentified. The compact proof in section2
closes that specific logical gap. Dropping the saved energy would recover
only K2012's weaker multiplicative comparison, not(6).

## 4. Actual optimizers, sharp coefficients and dimension threshold

A is prepared at1,3 with populations9/10,1/10; B with2/5,3/5.
For B shifted by delta, take w_B=r/(1+delta). For A shifted, take
w_B=(r-delta)/(1-delta), admissible when delta<r. Decrease the threshold
if needed so delta<min_(E in I) r. The physical union is
{0,1,2,3,4} union {delta,1+delta,2+delta,3+delta,4+delta}.
It has10 distinct levels and minimum spacing delta for0<delta<=1/2.
All shell ranks and exact channel constructions are inherited; the producer
recomputes the actual shell ranks, energy and sharp return.
The winning branch shifts B if r<=(1+delta)/2, and A otherwise.
The A/B placement is a known construction; its UNRESTRICTED optimality is new.

It follows at fixed E that

    lim_(delta->0+) (F_infty-B)/delta
      = (3/20)min(r,1-r).                               (7)

For E<=17/10 the second-order coefficient is -(3/20)r; for E>17/10 it is
+(3/20)(1-r). At E=17/10 the B-shift branch wins. These are now coefficients
of the unrestricted optimum, not an extrapolation of fixed-d limits.

K1975's strict unspaced dimension-nine gap on interior budgets also gives a
sharp eventual minimum dimension: F_9(delta,E)>=V_9(E)>B(E), while G->B.
Thus after reducing eta_E again, fewer than10 physical levels cannot attain
the unrestricted optimum. Sufficiency and necessity are pointwise in E;
no uniform claim up to the interval endpoints is made. Extra unused levels
remain possible, so the theorem does not classify every optimal spectrum.

## 5. Released near-optimal and bath-stability consumers

For epsilon>=0, if

    q_bar=(G(delta,E)+epsilon-B(E))/(11/50)<1,
    (9-E)q_bar/(1-q_bar)<=rho,

and the whole budget interval lies in section2's fixed25 regime, K2013 gives

    population(s>9) <= epsilon / (kappa_delta(E)+epsilon).    (8)

In particular every exact optimizer has zero diagonal population above9.
This is population stability, not uniqueness or control of tail energy.
The examples execute the algebraic budgets; they do not certify the unknown
threshold eta_(25,K) at a chosen numerical delta.

In regime(1), the exact reference-bath duality gap is
Gamma=(3/20)delta min(r/(1+delta),(1-r)/(1-delta))>0.
K2012's faithful-bath transfer now gives the explicit conditional guarantee

    F_b-D_b >=Gamma-2 TV(b,b_ref).

Thus any faithful bath with TV<Gamma/2 preserves strict nonconvex duality,
and |t-1/2|<Gamma/12 is a sufficient Gibbs-temperature neighborhood.
This is an evaluated radius once membership in the small-spacing regime is
certified, not a claim to have certified such membership at the sample points.
No analogous threshold formula for every bath or missing-support bath is inferred.

## 6. Verification and frontier

The exact producer executes both physical orientations, recomputes all shell
counts and returns, and verifies the sharp first/second-order identities,
branch switch, budget-window inequalities, secant slope and near-tail consumer.
The separate probe uses direct bath-label maxima, independent exact mixtures,
and deliberately wrong energy cost, return factor, branch choice and secant slope.
Finite controls test computations; sections2–3 carry the universal claim.
No new large25-level program, external expert review, proof assistant or
novelty certification is claimed. Same-author hostile review explicitly checks
the two-ray compactness argument and actual cutoff transfer.

Next is a certified useful numerical threshold/full-spacing frontier, not
another proof of the local coefficient or generic finite attainment near0.
Global hard-budget finite support at arbitrary positive spacing, a sharp
threshold and exact capped continuum pulse remain open. SC-META-53 remains
UNCERTAIN; LT-SM8/GR6b remain NEEDS. No source, physics-ledger or canon verdict
changes. The independent thermal theorem is not a GU realization.
