---
title: "K1256--K1260 kappa/Casimir channel boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1256--K1260 kappa/Casimir channel boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact starts
> from the action-owned source-epsilon cotangent parent but deliberately grants
> the displayed scalar `kappa_1` a favorable quotient-Casimir interpretation
> that has not been derived from the source action. It proves a necessary
> channel-rank boundary and constructs an internal finite repair; it does not
> derive a source boundary law or functional deformation complex. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the regular quotient question and
`INTERNAL_STRUCTURAL_ONLY` for the channel theorem and selector repair.

Scope: local smooth laws on the regular seven-dimensional quotient and one
globally proper polynomial on its ambient formal invariant-coordinate base.
No claim is made that the full split-real orbit image is all of that base, that
the source torsion norm is the charge Casimir, or that finite properness is
functional BV-BFV properness.

```gu-typed-objects
result: invariant-channel Hessian-rank bound, favorable kappa/Casimir shape-nullity obstruction, scale/shape channel census and globally proper finite selector repair
carrier: regular source-epsilon quotient coordinates plus the ambient formal invariant base R7 LAYER=source-print CHIRALITY=N/A
pairing: ordinary finite quotient Hessian; no completed physical pairing ON=regular_formal_quotient
real_structure: real split-D7 invariant coordinates on the I2-positive horn, with global repair only on the formal base
grading: primitive degrees 2,4,6,7,8,10,12; one radial and six shape channels
action_owner: repository-construction owns the favorable transfer, channel theorem and polynomial repair; source-action owns only the torsion norm coefficient and cotangent parent
target: K949 regular seven-lock plus K1145/K1150 functional admission MAP-TYPE=evaluation
```

## Channel-rank theorem

Let `z` be regular quotient coordinates, let `P:U subset R7 -> Rm` have rank
`m` at `z*`, and suppose a candidate selector factors as `V=F o P`. At a
critical point of `V`, the transpose of `dP` is injective, so `dF=0`. The
second-derivative chain rule therefore loses its outer-gradient term and gives

```text
Hess_z*(V) = transpose(dP_z*) Hess_P(z*)(F) dP_z*.
```

Hence `rank Hess(V)<=m` and `nullity Hess(V)>=7-m`. A nondegenerate regular
seven-lock needs at least seven locally independent response channels. This
counts channel rank, not free scalar parameters: one scalar can label a fixed
family that already contains seven channel functions, but the scalar does not
manufacture those functions.

## Most favorable `kappa_1`/Casimir grant

The source displays `kappa_1` multiplying a quadratic torsion term. The
cotangent boundary charge and its primitive invariants are different typed
objects, and the source does not derive a map from that torsion norm to
`I2(mu)`. Grant the strongest helpful finite surrogate anyway:

```text
V_kappa = F_kappa(I2) = F_kappa(r^2).
```

At a regular critical point `I2*>0`, its radial/shape Hessian is

```text
diag(4 I2* F_kappa''(I2*),0,0,0,0,0,0).
```

It has rank at most one and at least six shape nulls. The literal linear norm
surrogate `kappa_1 I2` is even weaker: for nonzero `kappa_1` it has no critical
point on the regular quotient and its Hessian in invariant coordinates is
zero. Thus a Casimir-only reading cannot supply the six missing shape locks.
This does not show that `kappa_1` actually selects the scale; that transfer is
unproved.

The exact K1251 channels make the remaining burden explicit. `I2` has rank
one. The six ratios

```text
I4/I2^2, I6/I2^3, I7/I2^(7/2), I8/I2^4, I10/I2^5, I12/I2^6
```

have joint rank six and annihilate the weighted radial vector. Together with
`I2` they have rank seven. Even granting a `kappa_1`-labelled scale condition
therefore leaves six locally independent shape responses to derive.

## Finite properness is repairable, but ownership is not

K1254's escape through the open radial/shape chart is a defect of that
particular formula, not a universal finite obstruction. For target values
`I_d*=(r0^2,r0^4 c4,...,r0^12 c12)`, define on the ambient formal base

```text
U(I) = 1/2 sum_d ((I_d-I_d*)/r0^d)^2.
```

This inhomogeneous multi-weight polynomial is globally proper on `R7`, finite
at `I2=0`, and has the unique minimum `I=I*`. Its Hessian is diagonal with
entries `r0^(-2d)`, rank seven, inertia `(7,0,0)`, and determinant `r0^-98`
because the primitive degrees sum to `49`.

The repair is deliberately honest about what it buys. It imports exactly the
same one scale and six shape values as K1252. It is not source-owned, does not
classify the realized split-real orbit image, and does not define fields,
operators, boundary traces, closed range, a quotient gap, Green operators, a
maximal generator, or physical cohomology.

## Admission boundary

K1260 records two satisfied finite rows, two excluded Casimir-only routes, one
conditional favorable scale row, and seven missing source, orbit-image or
functional rows. K1145 and K1150 remain `0/7`. The exact effect is

`KAPPA_CASIMIR_ONLY_CANNOT_LOCK_SHAPES_AND_FINITE_PROPERNESS_IS_REPAIRABLE_WITH_SEVEN_IMPORTED_DATA__SOURCE_FUNCTIONAL_GAPS_UNCHANGED`.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`. Charged boundary symmetry remains the
honest default. The next useful input is an action-derived boundary or Green
law with seven locally independent quotient responses, including six shape
channels, on the realized orbit space and one common closed functional domain.
