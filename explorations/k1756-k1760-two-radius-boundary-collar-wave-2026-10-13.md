---
title: "K1756--K1760 two-radius boundary-collar wave"
status: active_research
document_role: exploration
claim_verdict: quantitative_rare_atom_and_zero_noise_collars_with_compact_residual_rectangle
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-13"
---

# K1756--K1760: the two singular faces cannot hide the scalar minimum

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is
> repository trial-functional mathematics. It supplies no source-owned action,
> physical state, quotient, observed map, prediction or confirmation. Read
> `lab/methods/source-native-comparator-routing.md` before reusing it near a
> physical comparator.

Classification: `INTERNAL_STRUCTURAL_AND_INTERVAL_ONLY`.

```yaml
gu-typed-objects:
  carrier: symmetric_unit_variance_two_radius_four_point_scalar_seed_chart
  pairing_or_form: relative_fisher_form_under_gaussian_interpolation
  real_structure: real_symmetric_scalar_channel
  grading: certified_face_order_plus_quantitative_boundary_exclusion
  action_owner: repository_trial_functional_not_source_owned
  target_object: fixed_q_two_radius_fisher_minimization_domain
  observed_intertwiner: UNTYPED
```

## Certified Rademacher margin

At `q=1/1024`, K1756 applies K1749's positive-denominator Arb integrand to
the `c=0` Rademacher face and K1753's exact rational candidate. On 352
rational cells over `[-11,11]`, with order-11 Taylor remainders and analytic
Gaussian tails, it certifies

```text
J(Rademacher)-J(candidate)
  in [2.201208275066055e-10 +/- 3.52e-24] > 2.20e-10.       (1)
```

This is the boundary margin consumed below, not a whole-chart result.

## A quantitative rare-atom stability theorem

Write `Y=sqrt(t)X+sqrt(v)Z`, `v=1-t`. Relative Fisher has the variational
form

```text
J(Y)=sup_f E[2(Yf-f')-f^2].                                (2)
```

For the Rademacher channel use its exact relative score

```text
f_t(y)=sqrt(t)/v tanh(sqrt(t)y/v)-t y/v.                   (3)
```

Couple each signed radius of the `(c,z)` law to the same-sign Rademacher
atom. Exact variance algebra and `(sqrt(1+x)-1)^2<=x` give

```text
W2(X_(c,z),R)^2<=z+z^2<=2z.                               (4)
```

On `t<=31/32`, `v>=1/32`, direct differentiation of (3) bounds the derivative
of the variational integrand in (2) by `K0+K1|y|`, with
`K0<=198720`, `K1<=67646`. Cauchy--Schwarz and unit output variance therefore
give the explicit one-sided estimate

```text
J(X_(c,z);t)>=J(R;t)-400000 sqrt(2z).                      (5)
```

This uses a fixed legal test in the variational formula. It does not assume
continuity of Fisher information under weak convergence and remains uniform
in `c` on the declared noise range.

## The zero-noise face and joint corner

Every channel input here has at most four atoms. Hence

```text
h(Y) <= H(X)+h(sqrt(v)Z) <= log(4)+(1/2)log(2 pi e v).
```

Since `Var(Y)=1`, Gaussian log-Sobolev yields

```text
J(Y)>=2D(Y||gamma)>=-log(v)-2log(4).                       (6)
```

For `v<=1/32`, the right side is at least `log 2>1/2`. The K1753 candidate
obeys `J(candidate)<=t/(1-t)<1/16`, because the exact inequality
`289q<u_candidate=691835097/2000000000` implies `t<1/17`. Thus the entire
collar

```text
c >= 2-1/961                                               (7)
```

is excluded at `q=1/1024`, uniformly for every `0<z<1`. Its width from the
singular face `c=2-q` is exactly `63/984064`. In particular, (6) handles the
joint rare-atom/zero-noise corner without inserting `v=0` into the interior
density.

## Rare-atom collar and remaining compact rectangle

Outside (7), `t<=31/32`. OU Fisher monotonicity makes the Rademacher control
at least its `c=0` value. Combining (1) and (5), for

```text
0<z<=10^-34
```

the stability loss is less than `6e-12`, leaving a strict gap above the
candidate exceeding `2.14e-10`. Inside (7), the entropy argument already
covers every `z`. Therefore the full rare face has an explicit uniform
collar, and the joint corner is closed independently.

The remaining global certification problem is the closed rectangle

```text
0<=c<=2-1/961,  10^-34<=z<=1.                             (8)
```

The lower edge is conservative and far too small for a practical uniform
mesh; its value is proof of boundary exclusion, not an efficient subdivision
scale. The next step is adaptive interval branch-and-bound on (8), exploiting
analytic rare-tail bounds rather than resolving `10^-34` by uniform boxes.

## Review and limits

K1756--K1760 add five satisfied bridge rows, for 460 total: 381 satisfied,
ten conditional, 65 excluded and four missing. Source claims, the standing
physics ledger, canon, papers, predictions, confirmations and public posture
do not move; K1145/K1150 remain `0/7`.

Hostile review rejects reversing Gaussian log-Sobolev, replacing the four-atom
entropy upper bound by a density evaluation at `v=0`, using weak convergence
as Fisher continuity, dropping the OU parameter restriction in (5), calling
the extremely thin rare collar numerically practical, or promoting boundary
exclusion to stationarity, uniqueness, global scalar optimality or physical
admission.
