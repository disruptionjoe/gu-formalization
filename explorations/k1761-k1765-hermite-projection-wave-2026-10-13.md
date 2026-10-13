---
title: "K1761--K1765 Hermite projection wave"
status: active_research
document_role: exploration
claim_verdict: exact_hermite_fisher_lower_hierarchy_with_interval_engine_reselection
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-13"
---

# K1761--K1765: moment projections lower Fisher without density quadrature

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is
> repository trial-functional mathematics. It supplies no source-owned action,
> physical state, quotient, observed map, prediction or confirmation. Read
> `lab/methods/source-native-comparator-routing.md` before reusing it near a
> physical comparator.

Classification: `INTERNAL_STRUCTURAL_AND_INTERVAL_ONLY`.

```yaml
gu-typed-objects:
  carrier: symmetric_unit_variance_two_radius_four_point_scalar_seed_chart
  pairing_or_form: relative_fisher_score_projection_under_gaussian_interpolation
  real_structure: real_symmetric_scalar_channel
  grading: exact_lower_bound_hierarchy_plus_named_arb_certificates
  action_owner: repository_trial_functional_not_source_owned
  target_object: fixed_q_two_radius_fisher_minimization_domain
  observed_intertwiner: UNTYPED
```

## A universal finite projection hierarchy

Let `s_Y=rho_Y+Y` be the relative score and let `H_n` be the probabilists'
Hermite polynomials. Integration by parts and the Hermite recurrence give

```text
E[s_Y(Y) H_n(Y)] = E[H_(n+1)(Y)].                         (1)
```

For any finite odd index set, put `b_n=E[H_(n+1)(Y)]` and
`G_(mn)=E[H_m(Y)H_n(Y)]`. The Fisher variational formula yields, for every
fixed coefficient vector `alpha`,

```text
J(Y) >= 2 alpha^T b-alpha^T G alpha.                       (2)
```

When `G` is positive definite the optimized lower bound is
`b^T G^(-1)b`. Enlarging the odd-Hermite span can only increase this lower
bound. Finite-degree equality with full Fisher is not automatic: it would
require the true relative score to lie in the selected polynomial span.

## Exact two-radius moment closure

Write `U=X^2` and center it at its exact mean one. The two centered support
values are `-z` and `c/z`, so every central moment satisfies

```text
mu_0=1, mu_1=0, mu_2=c,
mu_r=(c/z-z)mu_(r-1)+c mu_(r-2).                          (3)
```

Together with `E[U^r]=sum_k binom(r,k)mu_k` and OU Hermite transport, this
closes every finite Gram matrix without density quadrature. Through degree
nine, the required output Hermite moments are

```text
h4  = t^2(c-2) = -q,
h6  = t^3(c^2-cz^2-12cz+16z)/z,
h8  = t^4(c^3-c^2z^2-24c^2z+cz^4+24cz^3+132cz^2-132z^2)/z^2,
h10 = t^5(c^4-c^3z^2-40c^3z+c^2z^4+40c^2z^3+460c^2z^2
           -cz^6-40cz^5-460cz^4-1520cz^3+1216z^3)/z^3.   (4)
```

The apparent rare-face divergences in the individual moments are not by
themselves divergences of the optimized projection. In the degree-five span
`{H3,H5}`, substituting `c=2-q/t^2` and cancelling before taking the limit
gives

```text
lim_(z->0+) L5(t,z)
  = 2t^4/(3-2q+2qt-5t^2+4t^3).                           (5)
```

This identifies symbolic cancellation and correlated coordinates as part of
the interval method, rather than treating `z=0` as a raw-moment singularity.

## Arb candidate upper bound and degree escalation

At K1753's exact rational candidate, 352 rational cells on `[-11,11]`,
order-11 Taylor remainders and analytic Gaussian tails certify

```text
J(candidate)
  in [1.59178645304977141426027422063564370896043048e-7
      +/- 3.01e-24].                                      (6)
```

The tail is below `2.90e-27`. The same Arb backend certifies the exact
degree-3/5/7/9 projection hierarchy at four named controls. Degree five
already places the Rademacher face and `(c,z)=(33/20,2/5)` strictly above
(6). At the nearer control `(167/100,1107/2000)`, degree seven remains below
(6), while degree nine is strictly above it. At the candidate itself, degree
nine remains below (6) by about `2.54e-14`; the finite span therefore cannot
close the local optimizer region by itself.

## Failed global-cover pilot and engine decision

A fail-closed pilot applied direct independent Arb balls in `(c,z)` and
interval Gram elimination to K1760's complete rectangle. At a leaf budget of
one million it pruned `999718` leaves but retained or had not yet visited 282;
the queue still included initial boxes, so its unresolved hull was the full
rectangle. No durable exact partition was emitted. Those counts diagnose
wrapping and scheduling cost only; they prove no scientific exclusion.

The direct engine is therefore rejected. The next exact gate is to substitute
`c=2-q/t^2`, cancel the degree-5/7 projection rationally before interval
evaluation, prove denominator positivity, and cover the resulting sublevel set
with a replayable exact partition. Full Fisher interval Newton is reserved for
the surviving local tube. This is a method correction, not global completion.

## Review and limits

K1761--K1765 add five satisfied bridge rows, for 465 total: 386 satisfied,
ten conditional, 65 excluded and four missing. Source claims, the standing
physics ledger, canon, papers, predictions, confirmations and public posture
do not move; K1145/K1150 remain `0/7`.

Hostile review rejects reversing the variational inequality, treating a finite
projection as the full score, substituting divergent raw moments directly at
`z=0`, promoting named-point orderings to a box cover, or claiming global
completion from a capped queue without a replayable exact partition.
