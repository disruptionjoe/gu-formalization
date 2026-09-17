---
title: "K203 order-six positive common-weight moment rule"
document_role: active_research
doc_type: conditional_native_K139_K203_order_six_positive_moment_cubature
created: 2026-09-17
date: 2026-09-17
claim_ceiling: positive 28-node rule exact for radial polynomials through degree three and angular polynomials through total degree two under K202's common reference, with all eighteen complete signed K184 groups evaluated and an exact 14912-factor linear-argument support audit; the same broad full-domain error remains, not an accurate order-six prefix or any source/physics result
manifest: lab/process/k203-order-six-positive-moment-rule.json
solver: tests/channel-swings/k203_order_six_positive_moment_rule.py
probe: tests/channel-swings/k203_order_six_positive_moment_rule_probe.py
target_claim: INTERNAL_TARGET:K202_COMMON_WEIGHTED_RULE_AND_COMPLETE_QUOTIENT_DERIVATIVE_GATE
target_claim_verdict: POSITIVE_LOW_DEGREE_EXACT_RULE_AND_ALL_ARGUMENT_SUPPORTS_CERTIFIED__NO_USEFUL_GROUP_ERROR_OR_FULL_QUOTIENT_DERIVATIVE_BOUND
canon_verdict_change: none
---

# K203 positive common-weight moment rule

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: fixed K139/K156 `C3` hard-core impurity and positive four-species Fock
model, auxiliary `lambda=256`, equal couplings one, K162 seed orbits and
K184/K185's complete order-six signed time-Gram formula. This is a
repository-selected mathematical rule; it does not select a GU action,
physical extension, state, domain, quotient or scalar center.

```gu-typed-objects
result: a 28-node positive common-reference rule is exact on radial degree at most three times angular total degree at most two; all eighteen complete signed groups are evaluated, and the exact linear argument supports of all 14912 Bessel-factor occurrences are checked; the retained global error is broad
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), K139 chart and K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock Hilbert pairing for K184 order-six output, with specieswise Andreief determinants and signed coherent path-pair assembly ON=repository_signed_point_control
real_structure: CAR adjoint, real positive Bessel K1 kernel at every interior node, positive Gamma/Dirichlet reference, exact rational moment identities and outward Arb group evaluations
grading: eighteen groups, 234 unordered entries, 1864 Leibniz support terms, 2928 ordered terms, fourteen primitive increments and eight factors per term
action_owner: repository-construction -- K139/K156/K179/K184/K185/K202 fix the conditional calculation and reference, not a source or interacting physical action
target: supply a low-degree-exact complete signed weighted rule and exact derivative geometry without transferring polynomial exactness to a useful full-integral error MAP-TYPE=intertwiner
```

## Question and selected route

K202's one-node rule was a genuine complete weighted rule, but its error
`<9.683e-7` dwarfs the observed numerical group scale near `1e-21`.
The next cheap structural question is whether the *same* reference admits a
small positive rule with exact moments and complete signed evaluation.
This is a method within the K184 consumer, not a new GU physical branch.
The alternative native I1B mixed-grade Hessian plus full fermion insertion
would be closer to `SC-ACT-01/02` (both source `ASSERTS`) but has no
stationary non-gauge mode on the common background that can be borrowed from
the archived central-Maxwell model. `SC-META-53` is source `UNCERTAIN`;
the current v0.263 ledger's `LT-SM8`, `LT-GR6b`, `RA-F1` and `AC-F1`
remain `NEEDS`. The ledger has 88 canonical targets, not 88 recovered
physical quantities. A positive-Fock integral does not discharge those rows.

## Exact positive rule

Normalize the K202 reference to independent variables
`rho ~ Gamma(6,256)` and `z ~ Dirichlet(1/3,...,1/3)` on the
thirteen-dimensional simplex with fourteen coordinates.
Its unnormalized mass is

```text
Z = (120/256^6) Gamma(1/3)^14 / Gamma(14/3).
```

The two roots of the monic generalized Laguerre polynomial
`L_2^(5)(x)` are `x_-=7-sqrt(7)`, `x_+=7+sqrt(7)`. Put
`rho_±=x_±/256` and positive probabilities
`p_-=(1+1/sqrt(7))/2`, `p_+=(1-1/sqrt(7))/2`.
Direct expansion gives scaled Gamma moments `1,6,42,336` through
degree three. Independently set `theta=sqrt(3/17)` and, for each
`k=0,...,13`, define the interior angular point

```text
z_i^(k) = (1-theta)/14 + theta delta_(i,k), probability 1/14.
```

All coordinates are positive, their sum is one, and the rule's first and
second moments are `E z_i=1/14`, `E z_i^2=2/119`, and
`E z_i z_j=1/238` for `i!=j`, exactly the Dirichlet moments. The
tensor product has 28 positive nodes with mass `Z p_±/14`. It is exact
for every `rho^a P(z)` with `a<=3` and total angular degree of `P<=2`.
It is not exact for the Bessel determinant quotient merely by that theorem.

At each node the solver evaluates **original complete species determinants**,
both old-position `2K1` factors, all coherent signs, and the common-weight
quotient; the K185 Leibniz terms are used for proof-safe majorants, never
for cancellation-sensitive numerical evaluation. Ninety-digit independent
mpmath code reconstructs all 28 points and eighteen group sums, agreeing
with 100-digit Arb balls to less than `1e-70`. The new group point-rule
values range from approximately `2.16e-25` to `2.08e-20`. The changed
values relative to K202's one-node rule do **not** certify convergence or
which value is closer to the integral.

## Complete argument geometry and exact stopping point

For primitive vector `x=(s1,...,s7,v1,...,v7)=rho*z`, every Bessel argument
in a Leibniz support term is `rho L_m(z)`, where
`L_m(z)=sum_(i in mask_m) z_i` for its exact fourteen-bit support mask.
The two old-position masks and six species-pair masks are reconstructed
directly from K184's time-position data and each K185 permutation, then
checked against the allocation catalog. This checks all 1,864 terms and
14,912 factor occurrences, finding 31 distinct linear masks. In particular,

```text
partial_rho (rho L_m) = L_m,
partial_z_i (rho L_m) = rho * 1_(i in mask_m),
partial_z_i partial_z_j (rho L_m) = 0.
```

This closes the *argument-level* primitive-to-radial/angular chain and
detects a real mask corruption that passes K202's allocation-weight subset
test. It does not bound derivatives of `2K1`, old factors, normalized
regularizers, other determinant factors, the prefactor
`rho^8 prod z_i^(2/3)`, or their signed group products. The latter is
singular under naive high-order differentiation at simplex faces; K191's
fixed-slice R3 ceiling cannot be substituted for it.

The same positive-support proof used by K202 bounds every node of the
complete quotient by `n/pi^8` for a group with `n` ordered support terms,
and its integral by `n E`, with K202's rational per-term ceiling `E`.
The rule probabilities are positive and sum to one, so the rigorous
full-domain error remains `2nE` per group and exactly
`412009773890262587145/425541888504349469496573952` after summing
the eighteen groups. It is *not* a smaller derivative-based error.

A useful positive-radius-core bound must enclose the **complete signed
quotient's** relevant derivatives after all product and Bessel chains,
and allocate their weighted remainders by group. If the K185 face/tail
cutoffs are used, the restricted reference law no longer has these
unconditional exact moments: the discarded mass and the rule's truncated
moment defect need explicit accounting. Farther a/c determinant-positive
shells, K185/K188 boundary composition, K171/K168 columns, `R_ref`, floors,
the separate scalar center and K152 interval remain open. Nothing here
changes source adherence, the physics ledger, canon, prediction or
confirmation.

## Reproduction and hostile review

```sh
_local/cas-venv/bin/python tests/channel-swings/k203_order_six_positive_moment_rule.py --write
_local/cas-venv/bin/python tests/channel-swings/k203_order_six_positive_moment_rule_probe.py
```

The independent probe checks every declared radial and angular moment,
one mixed moment, all eighteen group values and the unchanged rational
error. It rejects a sign mutation, a wrong Dirichlet covariance parameter,
equal radial weights, an angular-weight rescaling, and an actual old-position
support mutation that K202's weaker subset condition admits.

Strongest overclaim: low-degree exactness is not a certified improvement for
this nonpolynomial quotient, and the 28-node values cannot replace an
outward integral interval. Strongest contrary example: restricting to an
interior core destroys unconditional moment exactness; the face correction
is not optional. Weakest propagation seam: only argument support/Jacobian,
not complete higher derivatives or a usefully small error, is certified.
No negative source or physical verdict is licensed.
