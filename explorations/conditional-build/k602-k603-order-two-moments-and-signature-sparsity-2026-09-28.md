---
title: "K602-K603 order-two moments and all-order signature sparsity"
status: working_draft_verified
status_axis: operational_state
classification: INTERNAL_CONDITIONAL_MATHEMATICS
direction: observed_to_native
target_claim: NONE-NOT-A-KILL
claim_ceiling: Certified order-two numerical moment intervals plus an exact order-two-through-twelve impurity/exterior-signature sparsity atlas; no surviving higher-order moment, complete uniform leakage bound, noncyclic floor, K473/K152 result, source, ledger, canon, paper, public, novelty or physical conclusion follows.
---

# K602-K603 order-two moments and all-order signature sparsity

## Question and route

K601 reduced the first nonzero K179 exchange family to three positive scalar
integrals: the cyclic norm `n`, the cyclic/action overlap `a`, and the exchange
norm `b`. K180 already owns a rigorous outward enclosure for `b`. K602 reuses
that enclosure and evaluates only the two missing integrals. K603 separately
extends K601's exact impurity/exterior-signature orthogonality through orders
three to twelve so later quadrature is commissioned only on products that can
survive.

The source register and v0.263 physics ledger do not move. `SC-ACT-01/02/06`
remain source assertions at their existing ceilings, `SC-META-53` remains
`UNCERTAIN`, and `LT-SM8`, `LT-GR6b`, `RA-F1` and `AC-F1` remain `NEEDS`.

## K602: outward order-two moments

For one fixed impurity/exterior signature, put

```text
h(p,q)=(2*pi)^-1 / [(256+E_p)(256+E_p+E_q)],
g(p,q)=(2*pi)^-2 K(p,q),
```

where `K` is K180's positive contracted exchange kernel. Then
`n=int h^2`, `a=int h g`, and `b=int g^2` on `R^2`. Both kernels decrease in
`|p|` and `|q|`, so the same 60,516-cell positive-quadrant dyadic mesh used by
K180 gives monotone lower and upper sums.

The cyclic tail is controlled directly. On the `q`-tail,
`h^2 <= (256+E_p)^-2 E_q^-2`, while integrating the second denominator first
controls the `p`-tail. At cutoff `2^40`, their full-plane union is below
`1.421085471685637e-14` before point normalization. Cauchy on the common
outside-box domain bounds the cross tail by `5.311129763521540e-12` after
normalization.

The resulting common-moment enclosures are

```text
6.8632403655301529e-7 <= n <= 8.7261345444545247e-7,
1.9350847130320616e-7 <= a <= 2.4603748407218119e-7,
6.1596631041161942e-8 <= b <= 7.8363416468845510e-8.
```

The last line is K180 reused, not requadrature. Interval composition with
K601's exact formulas gives

```text
0 <= lambda_2(q00)^2 <= 0.06500211807648015,
0.05294150926223116 <= lambda_2(q10/q01)^2
                    <= 0.10188436896151036.
```

The strict q10/q01 lower uses K601's Cauchy inequality and is robust to the
dependency loss of independent endpoint arithmetic. These are order-two
truncation values only.

## K603: exact finite signature sparsity

For each seed and order, let `c_s` count K177 cyclic paths and `a_s` count
K179 exchange terms in impurity/exterior signature `s`. Exact CAR exterior
orthogonality reduces the required pair counts to

```text
N pairs: sum_s c_s(c_s+1)/2,
A pairs: sum_s c_s a_s,
B pairs: sum_s a_s(a_s+1)/2.
```

The complete order-two-through-twelve census retains all 626 cyclic paths and
all 2,958 action terms. Of 131,076 possible cyclic/action products, 109,732
are exactly zero and 21,344 survive. At order two the surviving counts are
`2,1,1` for q00, q10 and q01, reproducing K601 independently.

This atlas removes only forced zeros. Every surviving block still needs its
coefficient signs, determinant-simplex kernel, outward quadrature and
within-block interference retained.

## Verification and next condition

K602 deterministically replays its enclosure, passes `5/5` headline controls
and rejects `19/19` hostile mutations. K603 replays all 33 seed/order blocks,
passes `5/5` headline controls and rejects `21/21` hostile mutations.

Next group the 21,344 surviving order-three-through-twelve cyclic/action pairs
by exact determinant-simplex kernel and outwardly enclose the distinct blocks.
Compose the resulting finite `N,A_F,B_F` intervals, then apply K599 with
K574's tail exactly once and prove the supported-level upper uniform. The
separate complete-sector noncyclic floor remains required before K473 or K152
can move.
