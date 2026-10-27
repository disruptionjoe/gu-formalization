---
title: "K2129: Global smooth-selector rigidity from rotated raw equations"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: C1 rigidity of the fixed Ptheta family under the fixed common-H upper raw contraction; isolated algebraic jets and other families not classified
scripts:
  - tests/channel-swings/k2129_rotated_positive_sector_raw_equations_probe.py
---

# K2129: Global smooth-selector rigidity from rotated raw equations

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
result: exact rotated systems and analytic smooth-selector rigidity
carrier: K2120 complex32 Ptheta inside original Jc complex128 and raw complex1920 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: SAME inherited current S=i Jc* H D0 Jc, Ptheta S Ptheta=(9/280)Ptheta ON=declared_carrier
real_structure: arbitrary complex raw coefficients; fixed common-H adjoint
grading: Clifford grade and current sign distinct from source ambient halves
action_owner: repository-construction -- unchanged K2028 raw upper contraction
target: C1 motion of this entire positive32 family under current-conserving full-output equations MAP-TYPE=intertwiner
```

## 1. Result and exact quantifiers

On a connected open spacetime domain, any C1 selector Ptheta from the K2120
circle family that satisfies K2126's full-output, selected-invariance and
current-conservation equations in the SAME raw upper common-H class is constant.
This remains true with the entire lower return unrestricted. Thus a lower-only
or southeast-only repair cannot support a nonconstant smooth selector in this
family. No complement invariance is imposed.

This is stronger than K2126's P0-only jet result. It does NOT assert that every
isolated algebraic jet at every exceptional angle has been excluded. It does
not classify other positive families, changed upper contractions, derivative-
dependent observations, or source-selected physical quotients. K2131 constructs
a changed-contraction repair preserving the same inherited form.

## 2. Fixed analytic family and exact rotated test

Retain the original J_a,D0,H, Clifford generators, all-grade common-form kernels,
and induced unknown elimination in K2126. Set

    Rtheta=cos(theta) R+i sin(theta) ZR,
    Ptheta=(I+iT)(I+Rtheta)/4.

All selected equations are polynomial in cos(theta),sin(theta), of degree at
most2, when written before numeric row normalization. Raw coefficients range
over the complete fixed K2028 basis with real and imaginary parts independent.
The source current and common-H equations are not fitted to theta.

In coordinates normalized by J_z, direct reconstruction gives Z the Clifford
word gamma10 gamma11 gamma12 gamma13 and XOR shift15. This does not establish
raw-class covariance; the lifted transformation of an upper interior block
contains column-dependent rotations absent from its upper-right coefficient.
We instead solve the actual rotated equations at cos(theta*)=3/5,sin(theta*)=4/5.
P has denominator20 and support subgroup

    Hshift={0,1,14,15,48,49,62,63}.

Right/left multiplication and adjoint in the equations preserve the associated
XOR cosets. Every raw output row has the same fixed translate as in K2126.
Only two cosets meet the derivative targets; all other cosets are homogeneous
and cannot cancel their equations. Importantly spatial2 and3 now belong to
one coset and must be tested JOINTLY.

| derivatives | top-row shifts | real+imaginary columns |
|---|---|---:|
| t,1 |0,1,14,15,48,49,62,63|584+452=1036|
| 2,3 |80,81,94,95,96,97,110,111|528+520=1048|

The full selected equations are those of K2126 with P replaced by Ptheta.
No raw variable from these cosets is discarded. Per-grade common-H completeness
is inherited from K2028, not claimed as a new229376-variable exhaustion.

Exact rational row reduction, right-kernel substitution into every original
selected equation, and independent finite-field minor checks give:

| derivatives | coefficient rank | augmented rank | augmented determinant mod101 |
|---|---:|---:|---:|
| t,1 |1034|1036|75|
| 2,3 |1046|1048|54|

The SAME ranks and residues hold after deleting every lower-return equation.
Raw contractions are independently reconstructed on representative complete
output blocks. The report retains primitive-equation hashes, rational kernel
vectors, modular pivot columns, and representative ORIGINAL row indices and
fixed divisors. Undoing those nonzero fixed row scalings recovers a genuine
minor of the unnormalized analytic family. We never analytically extend an
angle-dependent gcd, pivot choice or row-deduplication rule.

Integer arithmetic is bounded before execution. Original raw numerator bounds
are those of K2126. Eight projector shifts with numerator magnitude at most5
and denominator20 bound right products below2^33, leakage below2^40 and
conservation below2^49; every dense product additionally checks its actual
integer bound before int64 multiplication. Rank elimination uses exact rationals
and finite fields, not floating rank thresholds.

## 3. Two universal kernels prevent hidden generic rank increases

A rank gap at one angle alone would NOT prove a generic obstruction: coefficient
rank could increase elsewhere. Here explicit homogeneous kernels prohibit that.
For k=0,7,8,9 separately choose

    Omega_k=(2i/3)I, all other Omega=0.

These yield K=(2i/3)D_k and A=(2i/3){I,C1,C2,C3}, respectively. They preserve
all Ptheta and are skew-Hermitian. Their exact stored two-blade basis coordinates
are reconstructed by the probe, including every full output row. The k0,7
vectors lie in the first coset, and k8,9 in the second. Each pair is linearly
independent (their induced matrices are independent), for all angles.
Therefore coefficient rank is always at most n-2 for n=1036 or1048. This remains
true with the lower rows omitted. No numerical continuity assumption supplies
this upper bound.

## 4. Analytic minors imply global C1 rigidity

Choose the two fixed augmented minors certified nonzero at theta*. They are
nonzero trigonometric polynomials of theta. Each has finitely many zeros modulo
2pi. Let E be the union of those exceptional angles. Outside E, each augmented
rank is at least n; the universal kernel bound makes coefficient rank at most
n-2. Thus both appended derivative columns are independent modulo the raw image.
All four components of dtheta must vanish there.

Suppose a C1 theta had a nonzero derivative somewhere. That component remains
nonzero in a neighborhood. Along a short coordinate line, theta then has an
interval of values, which contains a value outside the discrete set E. At
that point the derivative must vanish, a contradiction. Hence dtheta=0
everywhere, and theta is constant on a connected domain. For circle-valued
theta use local lifts; the same conclusion makes Ptheta globally constant.

This avoids solving each exceptional pointwise system and avoids an enormous
symbolic rank elimination. No algebraic jet is claimed impossible at every
exceptional angle. Such isolated jets could not integrate to a nonconstant C1
solution satisfying the equations on an open domain. Raw coefficients need
not themselves be continuous for this argument; theta's C1 regularity is the
load-bearing premise. Singular selectors are a different domain problem.

## 5. Consequences and acceptance

K2126's P0 result is retained as exact local evidence, not overwritten. The
new analytic composition closes smooth motion of this entire family under the
frozen upper class, including arbitrary lower repair. Constant selectors with
K2123 scalar/vector potentials remain positive controls. K2131 shows that
common-H alone is not the obstruction; changed contraction is a real branch.

The probe checks actual equations, exact ranks, universal kernels and genuine
input faults. The trigonometric-minor/C1 argument is a written proof subject
to independent internal review, not a finite-sample inference. No external or
proof-assistant certification or novelty claim is made. Next compare a native
justification of changed upper contraction against a genuinely different positive
family/observation, rather than testing more isolated angles in this circle.
SC-OP-04 ASSERTS candidate grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN;
SC-META-56 DISAVOWS an odd-action prerequisite. LT-SM8/LT-GR6b, ledger0.263,
source register and canon are unchanged.
