---
title: "K2013: Energy-sensitive cutoff for hard-budget thermal optima"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2013_energy_sensitive_thermal_cutoff.py
  - tests/channel-swings/k2013_energy_sensitive_thermal_cutoff_probe.py
---

# K2013: Energy-sensitive cutoff for hard-budget thermal optima

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
result: physical energy-sensitive truncation, nonconvex finite-attainment criterion and near-optimal tail bound
carrier: fixed extreme four-state channel and positive-gap finite or countable catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance and upper mean energy ON=independent_initial_registers
real_structure: complex conserving unitaries and real diagonal populations
grading: physical energy components, not source chirality
action_owner: repository-construction -- unchanged K2008 exact thermal class
target: hard-budget finite-support reduction and exact optimal return MAP-TYPE=intertwiner
```

## 1. New transfer and its exact scope

K2008 truncates high populations while preserving the energy budget. Keeping
track of the energy **saved**, rather than discarding it, yields a useful
finite-attainment criterion even when the full Lagrange dual has a strict gap.
Keep that note's exact finite or countable positive-spacing model, including
nondegenerate nonnegative pure-point spectrum, ground zero, normal finite-mean
state, independent input registers, four bath levels, exact channel and exact
spectral-projection conservation. Fix bath t=1/2 for the supporting constants
below. No continuum spectrum, degeneracy or free classical flag is admitted.
Write B(E)=63/100-3E/20 and F_d(delta,E) for the at-most-d optimum.

For an integer N>E and a sharp diagonal preparation of return R, mean e<=E,
and population q above N, there is an actual at-most-(2N+7)-level protocol with

    energy <= E_N(q) := (E-Nq)/(1-q),
    return <= R+q/(1-q).                                  (1)

In particular

    R >= F_(2N+7)(delta,E_N(q))-q/(1-q).                   (2)

K2008 already proves the physical truncation, dimension count and return
inequality. The retained lower budget is the new load-bearing information.
This is a construction at the SAME positive spacing, not a priced optimizer
or a convexification. [K2012](k2012-thermal-duality-gap-and-bath-stability-2026-10-24.md)
shows that strong Lagrange duality cannot be used on the exposed interval.

## 2. Proof of the budget-sensitive inequality

Pinch the initial state and use the inherited sharp shell implementation;
this keeps the mean and cannot increase the original worst-input return.
Let h=sum_(s>N) s p_s. Then h>=Nq, and the normalized retained mean is
(e-h)/(1-q)<=E_N(q). Since every occupied energy is at least1,
q<=(E-1)/(N-1)<1 and E_N(q)>=1. Thus normalization is legitimate.
Keep every physical level through N+3, not just occupied levels through N.
Every retained input shell keeps all its old positions. Delete entire
zero-weight components after the inherited two-component reweighting, then
translate to ground zero. Both operations weakly decrease mean and return,
and preserve spacing. There are at most2N+7 physical completion levels.
The K2008 bound gives(1); finite-dimensional optimality gives(2).
For countable inputs truncate first, then reduce finite components. No
interchange of an unbounded observable with a trace-norm limit is required.
For unpinched inputs the same inequalities hold with their original R on the
right; q is their diagonal high-energy population.

K1950/K2010's tail supporting inequality supplies, when
c_N=(3/20)N-63/100-1/2>0,

    R-B(E) >= c_N q.                                     (3)

Indeed the canonical surplus R+(3/20)e-63/100 bounds the tail
sum [(3/20)s-63/100-1/2]p_s, and R-B(E) is that surplus plus
(3/20)(E-e)>=0. This uses absolute energies, not component offsets alone.

## 3. Sufficient criterion for exact hard-budget finite attainment

Put d=2N+7 and u=F_d(delta,E), which is attained in the finite model.
Assume q0=(u-B(E))/c_N lies in[0,1), E_N(q0)>=1, and for every
x in[E_N(q0),E] one has the finite-budget slope bound

    F_d(delta,x) >= u+m(E-x),   m>0,
    kappa := m(N-E)-1 >0.                                (4)

Then the finite-or-countable optimum is EXACTLY u. Every optimizer has
zero diagonal population above N. This does not assert uniqueness of its
spectrum, populations, unused levels, or unitary.

Proof: any protocol with R<=u has q<=q0 by(3), so (2) and(4) give

    R >= u+[m(N-E)-1] q/(1-q) >=u.                       (5)

A protocol with R>u cannot improve u. Since a finite d-level minimizer exists,
the unrestricted optimum equals u and is finitely attained. For an optimizer,
strict kappa in(5) forces q=0. Infima need not first be attained in the
countable class. No supporting multiplier, convexity of F_d, or differentiability
is assumed: a one-sided secant inequality on a specified budget interval is
enough. If m(N-E)<=1 the argument does NOT supply exactness.

## 4. Released quantitative stability of near optimizers

For epsilon>=0, replace q0 by
q_epsilon=(u+epsilon-B(E))/c_N. If q_epsilon<1, E_N(q_epsilon)>=1,
and(4)'s slope inequality holds throughout[E_N(q_epsilon),E], every protocol
with R<=u+epsilon obeys

    q <= epsilon/(kappa+epsilon).                        (6)

For epsilon=0 this recovers exact support exclusion. For epsilon>0 it
quantifies discarded population, not tail ENERGY or trace-distance proximity
to one distinguished optimizer. The energy of tiny populations at extremely
large levels need not follow from a population bound alone.
A smaller known feasible upper u_bar can replace u for the preliminary tail
estimate, but cannot replace the finite exact value u in the equality conclusion.

## 5. Executed consumers and hostile boundaries

The producer constructs low A/B endpoint mixtures plus actual high pure
components, retaining physical completion levels, at three temperatures and
multiple cutoffs. It calculates exact shell returns, normalized retained
energies, minimum spacing and the two resource inequalities. At t=1/2 it also
checks(3). A separate checker reconstructs bath-label maxima and shell counts
and mutates actual energy shifts, population normalization, physical shell
completion and return normalization. The universal theorem rests on sections2–4 and
the cited physical shell results, not the finite examples.

The numerical slope consumers are the explicit two-ladder subproblem and
are labeled as such; they do NOT certify global F_d at sampled spacings.
[K2014](k2014-unrestricted-ten-level-onset-2026-10-24.md) supplies the missing
uniform finite-program identification in an existential small-spacing regime.
No arbitrary-budget or arbitrary-spacing finite-support theorem is claimed.
The strongest contrary route is a flat finite frontier: m=0 cannot pay for
truncation loss, so the criterion fails, without implying infinite support.
Source register, physics ledger and canon stay unchanged. Same-author exact
checks are not independent specialist or proof-assistant acceptance.
