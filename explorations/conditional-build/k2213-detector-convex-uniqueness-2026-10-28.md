---
title: "K2213 Unique certified detector and convex-envelope energy growth"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unique compact-squeeze-box minimizer and unique stationary point in an explicit convex envelope; global optimum over all squeezes remains open
scripts:
  - tests/channel-swings/k2213_detector_convex_uniqueness_probe.py
---

# K2213 Unique certified detector and convex-envelope energy growth

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: unique compact-box infinite detector minimizer with uniform weighted energy growth on a convex profile envelope
carrier: supplied positive scalar Fock detector with binary occupation effects at exact contrast1/2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and weighted sequence norm ON=declared_carrier
real_structure: real effects and positive outcome squeezes
grading: occupation number, not ambient chirality or family count
action_owner: repository-construction -- supplied output-field energy, excludes apparatus preparation and reset
target: uniqueness and quantitative stability in a certified enclosure MAP-TYPE=intertwiner
```

## Result

[K2210](k2210-detector-stationary-certificate-2026-10-28.md) already proves
existence of an infinite jointly stationary detector and cap-local stability.
Its minimizer over the specified squeeze rectangle and ALL cap-feasible
exact-contrast profiles is now proved **unique**. A stronger quantitative
statement holds on the explicitly convex enclosure C below:

    E(x,s)-E(x*,s*) >= (1/20000) sum_n (n+1)(x_n-x*_n)^2/p_n
                        +(3/1600)|s-s*|².             (1)

It is also the only fully stationary point within C. This does not exclude
other stationary points outside C, even when their squeezes lie in the same
rectangle; it does not prove the global optimum over every positive squeeze.
The detector model remains supplied, independent of source-native GU physics.

## 1. Exact convex enclosure and the dependency distinction

Retain K2210's p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n-x_n=p_n f_n,
q_n=3n-1 and exact constraint sum q_n x_n=1/2. Its energy is

    E=A(s1)R(x)+A(s0)R(y)-C0[s1 T(x)+s0 T(y)]+35/18,
    A(s)=41s²/6+3/(2s²), C0=40/3.

Let C contain exactly the profiles/squeezes satisfying the cap/contrast and:

- The seven exact rational coordinate boxes and two squeeze boxes exported by
  [the K2213 report](../../lab/process/k2213-detector-convex-uniqueness.json).
- e_n>=3/20 for every n.
- f_n/9<=f_(n+1)<=4f_n/9 for every n.
- f_(n+1)<=f_n/4 for n>=2.

All these constraints are affine inequalities/equalities in e and f=1-e,
plus a squeeze rectangle; their intersection is convex. Head bounds imply
0<f0<1; the lower ratio and e lower bound make each x_n,y_n strictly positive.
The inherited optimizer theorem admits EVERY compact-box minimizer to C.

The new probe recomputes boxes from K2210's outward energy upper bound and
unchanged free dual slopes. It then RECOMPUTES the entire residual/Schur bound
on those fresh boxes, exporting their exact rational endpoints. K2210's rounded
JSON boxes are not silently treated as its narrower internal intervals.
The inherited boundary existence certificate is consumed by exact dependency
hashes; the unchanged thirty-six boundary evaluations need not be rerun.

Stationarity is used to admit each minimizer to the envelope, using the
K2210 coordinate-gap and all-tail ratio theorem. It is NOT used in the
subsequent residual calculation. The approximate Riesz vectors and multipliers
are arbitrary trial inputs. K2204's weighted coercivity, residual identity,
junction contribution and tail estimate require only these profile/squeeze
bounds. Consequently the fresh calculation proves at EVERY point of C

    S>=D/100,  Q(v)>=(1/50)||v||_p²,  D>=(3/4)I,       (2)
    ||v||_p²=sum_n (n+1)v_n²/p_n.

Here Q is the constrained effect Hessian, D the diagonal squeeze Hessian,
and S its infinite Schur complement. The residual includes its n=4 junction
and all n>=5. To see the last constant independently, e0>=3/20 gives
R(x)>=9/160, f0>=4/5 gives R(y)>=3/10, and A''>=41/3.
These imply both entries of D exceed3/4.

## 2. The chord proof does not assume cap-close endpoints

For any two points of C, form (x_tau,s_tau)=(1-tau)(x0,s0)+tau(x1,s1)
and let (v,t)=(x1-x0,s1-s0). At every 0<tau<1,

    sup_n |v_n|/min(x_tau,n,y_tau,n)
       <=max(1/tau,1/(1-tau)).                         (3)

This elementary inequality follows separately from 0<=x0,x1<=p and their
complements. Thus the chord direction belongs to the energy completion at
interior points, whether or not its endpoints are mutually cap-close.
In particular, two complementary tails decaying as4^-n and9^-n obey the same
ratio bounds but have unbounded mutual relative-cap distance. A tiny squeeze
rectangle alone cannot justify applying K2207's cap-local theorem to them.

K2207's joint quadratic estimate is an algebraic consequence of(2), so

    d²E/dtau² >= (1/200)(Q_tau(v)+t^T D_tau t)
              >= ||v||_p²/10000+3|t|²/800.             (4)

For completeness, if b_j(v) is the effect/squeeze mixed form, S>=eta D
implies |b(v) dot t|<=sqrt((1-eta)Q(v)t^TDt). Therefore the complete
quadratic form is at least `[1-sqrt(1-eta)](Q+t^TDt)>=eta(Q+t^TDt)/2`.
Here eta=1/100. This argument needs no optimizer premise.

All derivatives used on a closed interior subsegment are justified by the
geometric cap and ratio bounds. In particular coherence gradients are O(n+1)
uniformly along the entire chord: e>=3/20 bounds the x ratios, and the f ratios
are bounded above and below. Since |v_n|<=p_n, first derivatives are dominated
by a constant times(n+1)p_n. They therefore extend to the endpoints by dominated
summation. At a fully stationary point, exact contrast and squeeze stationarity
make that endpoint derivative zero. Integrating(4) twice proves(1), with the
factor1/2 retained.

## 3. Uniqueness consequences and quantitative use

Every minimizer over the original compact rectangle belongs to C and is fully
stationary by K2210. Applying(1) to two such minima forces both weighted effect
difference and squeeze difference to vanish. Thus the compact-box minimizer is
unique, without requiring every feasible profile to lie in C.
If two fully stationary points lay in C, apply the integrated strict derivative
inequality between them; their endpoint derivatives cannot both be zero unless
they coincide. This proves the stated stationary uniqueness within C.

For an approximate feasible point in C whose energy exceeds E(x*,s*) by at
most delta, (1) immediately supplies ||x-x*||_p<=sqrt(20000 delta) and
|s-s*|<=sqrt(1600 delta/3). This is a certified stability implication, not an
algorithm that already knows the unknown minimum energy exactly. Global
search outside C and global comparison over all squeezes remain necessary
for global optimizer certification.

## Verification and limits

The new interval consumer proves the same positive Schur threshold on its
own exact exported enclosure and checks the coercivity constants. Exact finite
controls exercise convex ratio preservation, the squared ratio conversion,
the chord cap bound, integration constants and the unequal-tail countercontrol.
Planted faults change a ratio coefficient or omit the integration half; they
must produce genuine failed checks after a clean baseline. The new universal
chord proof, fresh interval residual result, inherited boundary certificate,
and finite algebraic controls are distinct evidence types.

No source, physics-ledger, canon, apparatus/reset/preparation, proof-assistant,
external-expert or novelty claim changes. This closes confined uniqueness,
not global joint uniqueness for the supplied detector family.
