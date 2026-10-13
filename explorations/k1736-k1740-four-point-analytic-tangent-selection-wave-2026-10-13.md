---
title: "K1736--K1740 four-point analytic tangent selection wave"
status: active_research
document_role: exploration
claim_verdict: exact_tenth_order_law_and_unique_leading_tangent_with_separate_numerical_regression
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-13"
---

# K1736--K1740: the half-order cancels and the quintic square selects the tangent

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is
> repository trial-functional mathematics. It supplies no source-owned action,
> physical state, quotient, observed map, prediction or confirmation. Read
> `lab/methods/source-native-comparator-routing.md` before reusing it near a
> physical comparator.

Classification: `INTERNAL_STRUCTURAL_ONLY` with a separately graded numerical
regression in K1739.

```yaml
gu-typed-objects:
  carrier: symmetric_two_radius_four_point_scalar_seed_chart
  pairing_or_form: relative_fisher_form_plus_matched_negative_fourth_cumulant_defect
  real_structure: real_scalar_gaussian_interpolation
  grading: exact_tenth_order_hermite_law_and_local_path_asymptotics_plus_numerical_regression
  action_owner: repository_trial_functional_not_source_owned
  target_object: leading_analytic_tangent_through_the_k1727_equality_seed
  observed_intertwiner: UNTYPED
```

## Result and boundary

For a bounded symmetric centered unit-variance seed, expanding
`int phi (r_t')^2/r_t` through interpolation order ten gives the new terms

```text
-kappa6(9 h8 kappa4-855 kappa4^3+5 kappa6^2)t^9/360

+[h10^2-420 h10 kappa4 kappa6-1260 h8^2 kappa4
  +138600 h8 kappa4^3-3150 h8 kappa6^2
  -5658660 kappa4^5+680190 kappa4^2 kappa6^2]t^10/362880.       (1)
```

Put `s=sqrt(q)` and along a regular matched path write

```text
r(s)=kappa6/u^(3/2)=alpha s+beta s^2+O(s^3),
x(s)=h8/u^2=35+xi s+O(s^2),
y0=h10(X0)/u0^(5/2).
```

At quartic equality, `alpha=35/3`. Composing (1) with the complete K1706 law
does not produce a tangent selector at `q^(9/2)`: that entire coefficient is
zero. The first varying coefficient is instead

```text
j(q)=q^2/6+q^3/4+(11/108)q^4
    +[139/432+y0^2/362880+beta^2/120+xi^2/5040]q^5+o(q^5).     (2)
```

The second-order chart coefficients can impose `beta=0`. Equation (2) then
selects `xi=0`. In the exact `(p,a)` chart the two first-order equations have
Jacobian

```text
J=det d(kappa6,h8/u^2)/d(p,a)=97048.7740746550... != 0,
```

so they select the unique leading velocity

```text
p(s)=p0-0.1037580726956868... s+O(s^2),
a(s)=a0-0.1285250038860326... s+O(s^2).                       (3)
```

This is not K1728's fixed-raw-radii representative. It proves uniqueness only
of the first chart velocity. One second-order degree of freedom remains after
`beta=0`, and remote boundaries, global continuation and all-seed optimization
remain open.

## Route choice and daily comparison

K1734 made the first tangent-varying coefficient the cheapest decisive gate.
The exact contraction has a short dependency chain and directly distinguishes
all members of K1732's null line. Quantitative translation-Haar saving remains
the strongest independent scalar alternative, but no cutoff-uniform lower
estimate for posterior translated-score variance is available. Correlated
tensors and an unrestricted stationary lower bound still lack a transfer
principle. The compact-circle/source-action route remains limited by the
missing source-owned circle, kinetic normalization, physical carrier/domain,
positive quotient and faithful observation. SC-ACT-01/02/06 and SC-META-53
therefore retain their source statuses.

What changed is the expected analytic order: the anticipated post-`t^8`
calculation first proves a complete half-order cancellation and then selects
the tangent at `q^5`. What survives is K1726's floor, K1731's chart, K1732's
affine tangent family and K1733's computed finite-strength branch. What wins
next after (3) is the first later coefficient that resolves the remaining
second-order freedom, paired with interval-controlled finite-strength
comparison. Either a coercive next coefficient continues a unique local
branch or renewed flatness exposes a higher-order/singular scale; remote
boundary, Haar and correlated-law work remain independently available.

## K1736: exact fixed-seed law through order ten

Mehler expansion includes `h10 t^5 H10/10!`. Exact Gaussian contraction of
the score quotient yields (1). The ninth term contains no new moment; `h10`
first enters at tenth order. Boundedness controls the fixed-seed remainder.
No uniform growing-support or singular-boundary theorem follows.

## K1737: matched half-order cancellation

Substitute the scaled coordinates into the full expansion. At
`alpha=35/3`, the coefficient of every third-order path term is
`alpha/60-7/36=0`. At `x=35`, the first derivative of
`x^2/5040-x/72` is also zero. These identities cancel `q^(9/2)` exactly.
Collecting `q^5` gives (2), a sum of two path squares plus the seed constant.

For K1727,

```text
h10=-730u^2+840u-120,
y0=1253.042586099042...,
139/432+y0^2/362880=4.648577277826763....
```

## K1738: unique leading tangent

The first equation is K1732's quartic constraint. The second is `xi=0`.
Arbitrary-precision evaluation inside K1727's isolating root interval gives
the displayed nonzero Jacobian, so Cramer's rule yields (3). Every other point
on the affine quartic-optimal line has `xi!=0` and pays the strict excess
`xi^2 q^5/5040`.

## K1739: finite-channel regression

The exact theorem does not rely on fitting. As a separate consistency check,
the K1733 quadrature is rerun at `q=0.001,0.0015,0.002` with orders 120 and
180 and four starts. Quadratic extrapolation of the velocity ratios gives

```text
order 180: (-0.1040829661, -0.1291471442),
order 120: (-0.1023667741, -0.1263107838).
```

Both are within `0.0023` componentwise of (3). Objectives agree below
`6e-21`, while coordinate differences expose the expected shallow numerical
conditioning. This is reproducible numerical regression, not interval
certification or a proof of the branch.

## K1740: protected integration and hostile review

The bridge census becomes 440 rows: 361 satisfied, ten conditional, 65
excluded and four missing. `SC-ACT-01/02/06` remain `ASSERTS`, `SC-META-53`
remains `UNCERTAIN`, and the standing physics ledger remains 33 SAME / 22
DIFFERS / 31 NEEDS / 2 OVER-DETERMINED. K1145/K1150 remain 0/7. No source,
ledger, canon, paper, prediction, confirmation or public verdict moves.

Hostile review preserves five boundaries: the fixed-seed expansion is not a
uniform boundary theorem; the `q^(9/2)` cancellation is conditional on the
quartic equality data; K1738 selects only the first chart velocity; numerical
regression is not interval certification; and no trial-functional result is a
source-owned physical state.
