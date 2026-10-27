---
title: "K2150: The mobile raw locus and its regularity boundary"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no full raw rigidity, continuum apparatus or GU recovery
scripts:
  - tests/channel-swings/k2150_raw_mobile_locus_regularity_probe.py
---

# K2150: The mobile raw locus and its regularity boundary

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
result: K2150: The mobile raw locus and its regularity boundary
carrier: K2132 conserving graph manifold and K2141 real1280 joint jets LAYER=toy CHIRALITY=N/A
pairing: inherited S and unchanged common-H raw coefficient class ON=declared_carrier
real_structure: real coordinates or complex Hilbert adjoint as declared
grading: graph multiplicity, not physical chirality
action_owner: repository-construction -- supplied conditional objects below
target: necessary locus for nonconstant compatible selectors MAP-TYPE=intertwiner
```

## 1. A sharper necessary set, without another rank computation

[K2147](k2147-moving-raw-kernel-prolongation-2026-10-27.md) confines every
nonconstant C1 raw-compatible selector to the proper analytic deficient-augmented-rank
set E_bad. That set contains P0, although P0 has NO compatible nonzero joint jets.
Under path-integrable coefficient cost, the necessary set can be sharpened to

    E_move = {z : rank[F(z),T(z)] - rank F(z) < 1280}.             (1)

Every nonconstant solution satisfying the regularity hypothesis below stays entirely
in E_move. This is a direct generalization and consumption of
[K2144](k2144-raw-neighborhood-rank-budget-2026-10-27.md)'s fixed-annihilator
argument, not a new native matrix certificate. E_move is a STRICT subset of E_bad:
K2147 excludes its open dense complement, while K2141's ranks at P0 are16604 and17884,
whose difference is1280, so P0 is in E_bad but not E_move. Nothing here constructs
E_move, proves it nonempty, or proves a nonconstant solution exists inside it.

## 2. No departure at any zero-jet point

Work in any local smooth graph chart with locally Lipschitz finite matrices F,T,
with the exact equations F(z)c+T(z)v=0 and v=vec Dz. There are n=1280 target columns.
Let z* satisfy rank[F*,T*]-rank F*=n. Choose the orthogonal projection L onto
(im F*) perpendicular. Then LT* is injective; let alpha>0 be its least singular
value. Because LF*=0, local Lipschitz constants give

    alpha ||v|| <= LF |z-z*| ||c|| + LT |z-z*| ||v||.

In a small ball absorb the second term, obtaining

    ||Dz|| <= C |z-z*| ||c||.                                  (2)

Coordinate norm equivalences are included in C. No constant-rank hypothesis is used.
For any arc-length-parametrized piecewise C1 path gamma in spacetime, w=z∘gamma-z*
satisfies ||w'||<=C||c∘gamma||||w|| as long as it remains in this ball. Require
integrability on the WHOLE compact path segment, including a hitting time:

    integral_0^ell ||c(gamma(s))|| ds < infinity.                 (3)

Local integrability only for s>0 is insufficient. Gronwall gives w=0 from w(0)=0;
continuation prevents first exit. Thus if a C1 pointwise solution on a connected
open domain hits z*, it is constant when every point is accessible by such finite
paths with(3). In particular locally bounded c suffices. A stronger convenient
hypothesis is(3) on every compact piecewise smooth arc-length segment. For other
AC parametrizations the correct condition is the WEIGHTED integral of
||c∘gamma||||gamma'||; the chain rule and equations must hold pathwise almost
everywhere. Ambient almost-everywhere equations alone do not supply path traces.

Where w!=0, the same estimate implies the logarithmic cost

    |log(|w(b)|/|w(a)|)| <= C integral_a^b ||c∘gamma|| ds.        (4)

Reaching zero through a nonzero branch requires divergent cost. This is a local
coordinate estimate, not a globally uniform radius, constant or physical energy.
It refines the necessary moving locus only for this regularity class; K2147's
weaker E_bad confinement does not require the added coefficient regularity.

## 3. The smaller locus is not necessarily closed

For analytic F,T, (1) has the finite rank-stratum description

    union_r {rank F=r and rank[F,T]<=r+n-1}.                    (5)

Each rank equality/inequality is expressed by vanishing minors and nonvanishing
minors, so the set is locally semianalytic. It need not be closed or open. As an
abstract scalar-target control, take F(z,w)=(z,0)^T and T(z,w)=(1,w)^T.
The mobile set is exactly {(z,0):z!=0}. Its limit(0,0) has zero allowable target.
This two-parameter rank control is not a GU solution or a native exceptional
component. Do not inherit E_bad's closed-analytic-set property for E_move.

## 4. Sharp regularity countercontrols

The analytic scalar equation zc+z'=0 admits the smooth solution z=0 for t<=0,
z=exp(-1/t²) for t>0, c=-2/t³ on t>0 and c=0 otherwise. It satisfies the equation
at0 with every derivative of z zero, yet departs. The coefficient norm is not
integrable at0. Smoothness of the selector, even infinite-order contact, does
not replace the coefficient hypothesis. This is a scalar control, not a native
raw realization.

In d-dimensional spacetime let z(x)=|x|², F(z)=z I_d, T=I_d and
c(x)=-2x/|x|² away from0, c(0)=0. Then F(z)c+∇z=0 everywhere and
Dz(0)=0. Its coefficient norm is2/|x|, so c is in ambient L^p_loc exactly
for p<d (p>0), while its restriction to any radial ray has divergent integral.
At d=4 this defeats an ambient L1, L2 or L3 replacement of(3). It does not
establish sufficiency at the critical exponent p=d, nor give a native raw
counterexample. A punctured scalar z=exp(t), c=-1 also shows that zero jets at
one point do not imply neighborhood-wide rigidity.

## 5. Consequence for the next raw calculation

The remaining native task is quotient-rank and tangent/integrability analysis
on E_move, with a declared coefficient regularity class, or a genuinely changed
upper-contraction branch. Repeating maximal generic minors is dominated. P0
and all other zero-jet points cannot be passages for regular solutions; singular
controls explain exactly why unrestricted coefficient claims remain unproved.
The probe checks exact abstract ranks, differential identities and the radial
integrability exponent, and pins the reused K2141/44/47 evidence. It does not
replay16620 raw columns or classify a320-dimensional exceptional variety.

## Evidence and inference boundary

The proofs and finite exact controls are separate evidence kinds. Independent internal
specialists review the actual statements and probe seams. No external certification,
proof assistant, novelty or GU recovery is claimed. SC-OP-04 ASSERTS candidate
four-field grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS
requiring an odd action as a prerequisite. LT-SM8/LT-GR6b, ledger0.263, source
register and canon are unchanged. The scalar-equation controls are abstract hypothesis tests, not native raw
solutions, a physical quotient, fermionic grading or observed2+1.
