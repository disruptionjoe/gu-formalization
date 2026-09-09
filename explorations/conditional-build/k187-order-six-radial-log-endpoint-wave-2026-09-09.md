---
title: "K187 order-six radial-log endpoint wave"
document_role: active_research
doc_type: conditional_native_K139_K187_order_six_radial_log_endpoint_obstruction_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned proof that the K186 Bessel regularizers have a nonzero rho^2 log(rho) term on an admissible rational angular profile for every one of the 53 nontrivial factor patterns, so their second radial derivative is unbounded at rho=0 and an ordinary smooth-endpoint Jacobi remainder cannot certify the zero-inclusive compact core; K186 time-coalescent continuity and positivity remain valid, but no all-angular coefficient-sign theorem, outward log-aware or split-domain total error, accurate order-six prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is obtained
manifest: lab/process/k187-order-six-radial-log-endpoint-wave.json
solver: tests/channel-swings/k187_order_six_radial_log_endpoint.py
probe: tests/channel-swings/k187_order_six_radial_log_endpoint_probe.py
target_claim: INTERNAL_TARGET:K186_ZERO_INCLUSIVE_SMOOTH_JACOBI_DERIVATIVE_GATE
target_claim_verdict: ORDINARY_BOUNDED_C2_OR_HIGHER_RADIAL_ENDPOINT_PREMISE_FALSE__LOG_AWARE_OR_SPLIT_DOMAIN_CERTIFICATION_REMAINS_OPEN
canon_verdict_change: none
---

# K187 order-six radial-log endpoint wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: K186's fixed K139/K156 hard-core `C3` impurity control, auxiliary chart
`lambda=256`, equal couplings one, three normalized K162 zero-bath seed orbits,
and complete K184/K185 order-six time-Gram family. K187 changes no operator,
extension, state, domain, polarization or scalar center. It tests only the
radial endpoint regularity of K186's already factored size-two/three Bessel
regularizers.

```gu-typed-objects
result: on the admissible angular profile with all fourteen primitive coordinates equal to 1/14, every one of the 53 K186 nontrivial factor patterns has an exact positive rho^2 log(rho) coefficient; the ten distinct coefficients range from 8/49 to 169/98, so the second radial derivative is unbounded at rho=0 and the proposed ordinary smooth-endpoint Jacobi remainder is inapplicable
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 specieswise Andreief reduction and coherent path-pair assembly remain unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times, the convergent integer-order K1 series, and exact rational Cauchy determinant differentiation
grading: K184 coherent group and Gram-entry identity, K186 factor-pattern identity, canonical species time order, radial scale rho, equal-angular rational witness, exact logarithmic coefficient, occurrence propagation and ordinary-versus-log-aware remainder class
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, K179 fixes the coefficient family, K184 fixes the time Grams, K185 fixes face/tail bounds and K186 fixes the regularizers; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: decide the radial smoothness premise before attempting high-dimensional compact-core cubature, preserve the valid time-coalescent factorization, and route the remaining proof to analytic logarithm subtraction or a certified positive-radius split MAP-TYPE=intertwiner
```

## Inline preflight bookend

K186 proved that all 468 nontrivial determinant occurrences reduce to 53
positive continuous regularizer patterns after exact Cauchy--Vandermonde
factorization. Its proposed next route asked for outward mixed Duffy/Jacobi
derivatives on a compact core including `rho=0`. Continuity at zero does not
imply the bounded second and higher derivatives used by an ordinary Jacobi
remainder, and integer-order `K_1` has a logarithmic small-argument series.

The incumbent question was therefore tested at the theorem-applicability
level before interval cubature. The strongest independently framed source-to-
physics challenger remains the positive physical quotient and emergent count/
chirality bridge: `SC-META-53` is `UNCERTAIN`; ledger-v0.263 rows `LT-SM8`,
`RA-F1` and `AC-F1` still require an action-owned stationary background,
functional BV/BFV domain, positive physical pairing and typed count or chiral
carrier. Those inputs remain absent, so the challenger has no executable
discriminator that outranks K186's complete mathematical input.

The route census compared direct interval subdivision, generic Taylor models,
arbitrary precision, the analytic K1 series, Andreief expectation bounds,
Chebyshev approximation after a radial split and log-weighted quadrature. The
analytic series gives the cheapest route-changing discriminator: compute the
coefficient of `rho^2 log(rho)` in the determinant ratio exactly. Generic
smooth Taylor models are rejected if it is nonzero; arbitrary precision is a
control only. Log-aware integration and a positive-radius interval split remain
the two live successor classes.

## 1. Exact scaled-kernel expansion

For fixed positive angular sum `a=t_i+u_j`, the convergent integer-order series
used by K186 gives

```text
2 K_1(x)
  = 2/x + x [log(x/2) + gamma - 1/2] + O(x^3 log x).
```

After `x=rho*a` and multiplication by `rho`,

```text
rho 2 K_1(rho a)
  = 2/a
    + rho^2 a log(rho)
    + rho^2 a [log(a/2) + gamma - 1/2]
    + O(rho^4 log(rho)).
```

Let

```text
A_ij = 2/(t_i+u_j),
B_ij = t_i+u_j.
```

The common `rho^-m` determinant scaling cancels in K186's Bessel/Cauchy
ratio. Differentiating the determinant at `A` in direction `B` therefore gives

```text
R_m(rho t,rho u)
  = 1 + rho^2 [c_m(t,u) log(rho) + d_m(t,u)]
    + O(rho^4 log(rho)^2),

c_m(t,u)
  = D det_A[B] / det(A)
  = sum_(i,j) cofactor_ij(A) B_ij / det(A).
```

This coefficient is exact whenever `t,u` are rational.

## 2. Complete K186 pattern witness

Take all fourteen primitive angular coordinates equal to `1/14`. Their sum is
one and each is greater than K185's face floor `2^-180`, so this is an interior
point of the admitted face-stripped core. Every cumulative `t_i,u_j`, every
Cauchy entry, every cofactor and every `c_m` is rational.

The exact census covers all 53 K186 patterns and propagates to all 468
nontrivial occurrences in the 234 time-Gram entries. Every coefficient at this
profile is positive. There are ten distinct values:

```text
coefficient  pattern count
8/49         1
25/98        2
18/49        6
1/2          8
32/49       11
81/98        9
50/49        7
121/98       4
72/49        4
169/98       1
```

Thus the exact range is

```text
8/49 <= c_m <= 169/98
```

at this declared profile. This is not promoted to an all-angular sign or range
theorem. Such a theorem is unnecessary for the present discriminator: one
nonzero point in the claimed compact domain already refutes a uniform bounded
second-derivative enclosure on that whole domain.

## 3. Radial endpoint obstruction

Differentiating the asymptotic twice gives

```text
d^2/d rho^2 R_m(rho t,rho u)
  = c_m(t,u) [2 log(rho)+3] + 2 d_m(t,u) + o(1).
```

Because every exact witness coefficient is positive, the second derivative
tends to minus infinity along the declared radial ray. The regularizer is
continuous and `C^1` at `rho=0`, but it is not C^2 there. Any ordinary Jacobi
or Taylor remainder that assumes a bounded second or higher radial derivative
on the zero-inclusive compact core is therefore inapplicable.

This is a route obstruction, not a failure of the integral. K185's radial
weight is `rho^5 exp(-256 rho)`, so the logarithmic endpoint term remains
integrable. K187 rejects only the unmodified smooth-endpoint remainder class.

## 4. Time-coalescent faces remain valid

The radial endpoint and the ordered-time collision faces are distinct
boundaries. K186's Newton row/column divided differences still divide out the
time Vandermonde zeros and extend the quotient continuously through coincident
times. They do not and should not remove the `rho^2 log(rho)` term inherited
from the Bessel series.

Accordingly K186's exact factorization, strict open-chamber positivity and
coalescent continuity are preserved. K187 makes no uniform mixed Duffy-
derivative claim on the angular boundary and no all-angular sign claim for
`c_m`.

## 5. Independent numerical controls

The solver evaluates K186's convergent-series mixed-divided-difference
regularizer and compares

```text
[R_m(rho t,rho u)-1] / [rho^2 log(rho)]
```

against each exact rational coefficient. Across all 53 patterns, the maximum
absolute discrepancy decreases monotonically:

```text
rho=2^-20   2.130978173930e-2
rho=2^-40   1.065489086952e-2
rho=2^-80   5.327445434759e-3
```

The slow approximately inverse-log convergence is expected because the
unscaled `O(rho^2)` term becomes `O(1/log rho)` in this quotient. These values
are high-precision controls, not outward intervals.

## 6. Replacement certification route

The retired route is now exact:

```text
ordinary bounded-C2-or-higher Jacobi remainder across rho=0.
```

The strongest replacement is either:

1. subtract the explicit `rho^2 log(rho)` endpoint term and prove an outward
   remainder for the desingularized integrand, then use a log-weight-aware
   radial rule; or
2. prove a small-`rho` strip bound, choose an explicit positive split
   `epsilon`, and interval the remaining core on
   `epsilon <= rho <= 1/4` where ordinary derivatives are bounded.

Either successor must preserve all 234 signed entries, all 53 regularizer
patterns, old-position factors, primitive gap sums, complete determinants and
shared time nodes. Its final error must combine the small-radius endpoint,
K185's `z_i<2^-180` face strips, the compact interior and the `rho>1/4` tail.

The accurate order-six prefix remains through order five. No K171/K168 action
column, `R_ref` residual, complete complement or flux floor, scalar-center
floor or K152 interval is claimed.

The source and physics-ledger statuses remain unchanged: `SC-META-53` remains
`UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`. No physical/source
selection, Born derivation, prediction, confirmation, canon, paper, release or
public-posture conclusion follows.

## Inline postflight bookend

- **Strongest advance:** the radial endpoint smoothness premise is decided
  exactly before expensive cubature; all 53 patterns have nonzero rational log
  coefficients at one admissible common profile.
- **Strongest negative result:** the zero-inclusive regularizer is not C^2 in
  `rho`, so an ordinary bounded-derivative Jacobi remainder cannot certify it.
- **Strongest structural switch:** the compact-core proof must isolate the
  logarithm analytically or split away from zero; merely raising precision or
  subdivision does not repair the theorem hypothesis.
- **Strongest overclaim:** “positive coefficients at one profile give a
  uniform all-angular bound.” Refused; only the exact witness and the global
  non-C2 consequence are claimed.
- **Strongest contrary route:** Andreief positivity may eventually give global
  expectation bounds, but it does not by itself provide the derivative
  remainder and is not needed for this discriminator.
- **Weakest reproducibility seam:** the successor must produce a genuinely
  outward small-radius or desingularized remainder, not another asymptotic
  sample.

All seven admitted arcs completed. The exact coefficient census, endpoint
theorem, coalescent audit, Jacobi applicability test, high-precision controls,
complete occurrence propagation and replacement-route selection are banked.
The result changes the numerical method, not any scientific or source verdict.

## Reproduction

```bash
python3 tests/channel-swings/k187_order_six_radial_log_endpoint.py --summary
python3 tests/channel-swings/k187_order_six_radial_log_endpoint.py --write --summary
python3 tests/channel-swings/k187_order_six_radial_log_endpoint_probe.py
python3 tests/channel-swings/k187_order_six_radial_log_endpoint_probe.py --selftest
```
