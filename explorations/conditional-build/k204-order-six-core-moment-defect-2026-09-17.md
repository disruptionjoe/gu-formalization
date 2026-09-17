---
title: "K204 order-six common-reference compact-core moment defect"
document_role: active_research
doc_type: conditional_native_K139_K204_order_six_core_mass_and_moment_bound
created: 2026-09-17
date: 2026-09-17
claim_ceiling: exact full-reference low-degree moments and proof-safe rational compact-core lost-mass and moment-defect bounds for K203's 28-node rule; no complete signed-quotient error, accurate order-six prefix or physical/source result
manifest: lab/process/k204-order-six-core-moment-defect.json
solver: tests/channel-swings/k204_order_six_core_moment_defect.py
probe: tests/channel-swings/k204_order_six_core_moment_defect_probe.py
target_claim: INTERNAL_TARGET:K203_TRUNCATED_CORE_MOMENT_ACCOUNTING
target_claim_verdict: COMMON_REFERENCE_CORE_LOSS_AND_POLYNOMIAL_DEFECT_BOUNDED__SIGNED_QUOTIENT_REMAINDER_OPEN
canon_verdict_change: none
---

# K204 common-reference compact-core moment defect

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: K139/K156 fixed hard-core `C3` impurity with auxiliary `lambda=256`,
equal couplings one, K184/K185's complete signed order-six time-Gram formula,
and **K202/K203's common positive reference**, not each K185 term-specific
Dirichlet law. The calculation restricts that reference to K185's stated
`rho<=1/4` and `z_i>=2^-180` core. It does not select a GU action or state.

```gu-typed-objects
result: the K203 full-reference polynomial rule has an explicit conditional-core moment defect and all 28 nodes strictly inside the declared core; its complete signed nonpolynomial quotient remains unbounded at useful accuracy
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), K139 chart and K162 seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock pairing for signed K184 order-six output; separate normalized Gamma/Dirichlet reference probability and truncated conditional reference ON=repository_polynomial_control
real_structure: CAR adjoint, real positive Bessel K1 interior factors, exact rational Gamma moments and proof-safe beta/gamma inequalities
grading: 18 complete signed groups, 234 Gram entries, 1864 support terms; 14 primitive increments and 480 low-degree radial/angular monomials represented by 16 permutation orbits
action_owner: repository-construction -- K139/K156/K184/K185/K202/K203 specify this conditional calculation, not a source or interacting physical action
target: bound the moment-accounting loss upon core truncation while retaining the unsolved complete signed-quotient derivative and error allocation MAP-TYPE=intertwiner
```

## Question and native route

K203 exactly integrates polynomials `rho^a P(z)` with `a<=3` and angular
total degree `<=2` against the *full* reference
`rho~Gamma(6,256)`, `z~Dirichlet(1/3)^14`. Its 28 node values are not an
accurate integral. To use a positive-radius compact derivative domain, one
must account for both lost reference mass and lost polynomial moments.
The source-facing rival remains an actual non-gauge mixed-grade mode of the
native `I1B` Hessian (SC-ACT-01/02, both ASSERTS) with its full fermion
insertion on a common stationary background. K129's mixed-order Green
radical/domain work does not provide that mode; the supplied central-Maxwell
control is not a substitute. The conditional Fock construction here does not
change the source's indefinite-spectrum uncertainty (SC-META-53, UNCERTAIN)
or the `NEEDS` ledger rows LT-SM8, LT-GR6b, RA-F1 and AC-F1.

## Exact deletion and conditional moments

Write `C={rho<=1/4, min_i z_i>=2^-180}` and `q=P(C^c)`. The radial Gamma
survival at `1/4` is `e^-64 sum_(j=0)^5 64^j/j!`. The elementary series
inequality `e>8/3` gives the strict rational upper bound

```text
R_s = (3/8)^64 sum_(j=0)^(s-1) 64^j/j!,
P(rho>1/4) < R_6.
```

Every marginal `z_i` is `Beta(1/3,13/3)`. On `[0,1/2]`, its beta
denominator exceeds `(1/16) 3 2^(-1/3)>3/32`: indeed
`(1-z)^(10/3)>=(1/2)^4` and `2^(-1/3)>1/2`. Thus the one-face probability
is `<32 delta^(1/3)` and the union of fourteen faces is bounded by

```text
F = 448/2^60 = 3.885780586188048e-16,
q < Q=F+R_6 < 3.885834e-16.
```

The manifest preserves the exact rational `Q`, not the rounded display.
These inequalities use the common reference only; K185's term-specific
face ceilings are separate and remain in force. The two radial nodes satisfy
`rho_+<(7+3)/256<1/4`; every angular coordinate exceeds
`(1-1/2)/14=1/28>2^-180`. All 28 positive K203 nodes therefore lie
strictly in `C` without floating enclosure assumptions.

For an angular monomial `z^n` of degree at most two and `0<=a<=3`, define
`P=rho^a z^n` and its exact full-reference moment

```text
m_(a,n) = (6)_a/256^a * product_i(1/3)_(n_i)/(14/3)_(|n|).
```

There are 120 angular monomials, covered by four permutation types:
`1`, `z_1`, `z_1^2`, and `z_1 z_2`. Combining each with four radial
degrees accounts for all 480 polynomial moments. With
`D_(a,n)=E[P 1_(C^c)]`, positivity and independence give

```text
0 <= D_(a,n) < ((6)_a/256^a) F + m_(a,n) R_(6+a) =: D_upper.
```

The radial term is exact Gamma size-bias up to the proved exponential
ceiling; the face term uses `z^n<=1`. The truncated **unnormalized** core
moment is `m-D`, not `m`. For the conditional core law, whose true mass is
`p=1-q`, the full-reference K203 rule has the explicit moment defect

```text
E[P|C]-m = (m q-D)/(1-q),
|E[P|C]-Q_28(P)| <= (m Q+D_upper)/(1-Q).
```

The constant has zero conditional defect exactly. This is a safe but broad
polynomial estimate, not a remainder theorem for the Bessel determinant
quotient. For an unnormalized core integral, multiply `D_upper` by K202's
exact reference normalizer; for a conditional cubature, keep the displayed
normalization denominator. Neither convention permits reusing unconditional
moment exactness silently.

## Release boundary and review

An independent 90-digit mpmath probe checks the actual beta marginal and
Gamma tail against the rational ceilings, reconstructs the sixteen rational
moment orbits, checks the 28 node coordinates, and catches five hostile
cutoff, mass, normalization and error plants. Special-function controls are
not the proof: the beta integral and exponential inequalities above are.

Strongest overclaim: this does not reduce K202/K203's full-domain signed
absolute error
`412009773890262587145/425541888504349469496573952` (<9.683e-7).
The numerator is the *complete signed-group quotient*, not a polynomial.
Its Bessel/old-position/species determinant/prefactor products, high-order
core derivatives and a useful coherent-group remainder allocation remain
unbounded. A truncated face/tail correction also needs the existing K185
termwise quotient majorants; `Q` alone does not control the quotient.
The contrary construction of simply discarding faces and calling the 28-node
rule exact fails by the nonzero `D`; the weakest transfer seam is still the
complete product/chain derivative rather than the linear argument masks.
Farther a/c shells, K171/K168 columns, residual/floor, scalar center and K152
remain open. No source, physics, canon, prediction or confirmation moves.

Reproduce with:

```sh
_local/cas-venv/bin/python tests/channel-swings/k204_order_six_core_moment_defect.py --write
_local/cas-venv/bin/python tests/channel-swings/k204_order_six_core_moment_defect_probe.py
```
