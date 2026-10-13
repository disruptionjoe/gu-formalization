---
title: "K1776--K1780 full-Fisher boundary and interior-entry wave"
status: active_research
document_role: exploration
claim_verdict: boundary_excluded_and_strict_rational_descent_with_three_slab_interval_newton_open
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-13"
---

# K1776--K1780: close the singular boundary and enter the interior

> **GU-COMPARATOR-ROUTING — scope before inference.** This is repository
> trial-functional mathematics. It supplies no source-owned action, physical
> state, observed map, prediction or confirmation.

Classification: `INTERNAL_STRUCTURAL_AND_CERTIFIED_SCALAR_TRIAL_ONLY`.

## A structural replacement for singular boundary quadrature

K1773 proposed two sector charts for directly integrating its legal
Rademacher-score lower functional. K1776 replaces that more expensive route
with a global semiconvexity theorem.

Put `beta=t/(1-t)`,

```text
h_t(r)=E tanh(beta r+sqrt(beta)Z),
k_t(r)=E tanh(beta r+sqrt(beta)Z)^2,
F_t(s)=2 sqrt(s) h_t(sqrt(s))-k_t(sqrt(s)).
```

The exact derivative identities, together with
`|tanh''|<=77/100` and `|(tanh^2)'''|<=41/10`, give

```text
F_t''(s) >= -[(231/400)beta^2+(41/80)beta^3]/sqrt(s).       (1)
```

For the two-radius squared radius `S`, variance matching gives the two exact
identities `E S=1` and `E(S-1)^2=c`. Since `S>=1-z`, Taylor's theorem and the
cancelled linear term yield

```text
E F_t(S) >= F_t(1)
 - c[(231/400)beta^2+(41/80)beta^3]/[2 sqrt(1-z)].          (2)
```

This statement is uniform even when the rare radius diverges. It never forms
the raw quantity `c/z` at `z=0`.

## Boundary exclusion

Across the complete physical intersections of K1772's two cells, the right
side penalty in the K1773 full-Fisher lower functional is at most

```text
1.4174298470174598e-10.
```

K1756's Arb certificate places the Rademacher face more than
`2.20120827506605e-10` above the old candidate, while OU relative Fisher is
nondecreasing from `t0=sqrt(q/2)`. The residual lower margin is therefore
strictly above `7.8377e-11`. Both microscopic boundary cells are excluded.
Only K1771's three interior slabs remain.

## Derivative tails and the atom chart

For `Phi(A,sigma)=E phi(A+sigma Z)`, K1778 certifies all omitted Gaussian
tails through total natural derivative order three using

```text
partial_A^i partial_sigma^j Phi
 = E[Z^j phi^(i+j)(A+sigma Z)].
```

On `|Z|>11`, the four required Gaussian moment budgets are below
`3.86e-28`, `4.24e-27`, `4.70e-26` and `5.22e-25`; after the derivative
envelopes, the largest admitted tail is below `2.14e-24`. Compact-window
chain-rule evaluation in `(t,z)` remains open.

At `z=1`, K1779 uses `c` directly. The law is

```text
P(X=0)=c/(1+c),
P(X=+sqrt(1+c))=P(X=-sqrt(1+c))=1/[2(1+c)].
```

Its positive-density denominator contains the explicit atom term `p`, so the
chart is regular throughout the first slab. This does not yet exclude that
edge or supply the required KKT test.

## The incumbent moves again

The exact rational point

```text
(c,z)=(827040678413,281761482867)/500000000000
```

Arb-certifiably improves the K1753 rational point. The whole-line gap
`J_old-J_new` lies in a positive ball centered at
`3.0263020866086291e-22` with radius at most `6.00e-24`. Thus K1753's named
point is not locally optimal. The improvement is intentionally reported as a
two-point comparison, not as a certified locator, stationary point or
optimizer.

## Admitted result and next gate

K1776--K1780 close the singular boundary and supply two pieces of the interior
certificate infrastructure. The exact remaining domain is three slabs. Next
build a directed compact-window value/gradient/Hessian evaluator, adaptively
exclude slabs one and two, isolate every stationary box in slab three, and
compare their certified values. Existence, stationarity, uniqueness and global
optimality remain open.

The bridge census is 480 rows: 401 satisfied, ten conditional, 65 excluded
and four missing. Protected source, standing ledger, canon, papers,
predictions, confirmations and public posture do not move; K1145/K1150 remain
`0/7`.
