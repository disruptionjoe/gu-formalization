---
title: "K188 order-six small-rho strip wave"
document_role: active_research
doc_type: conditional_native_K139_K188_order_six_small_rho_strip_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned outward bound for the complete K185/K186 order-six contribution on 0<=rho<2^-20, obtained from the common normalized Gamma-shape-six lower tail P(6,x)<=x^6/720 and propagated through all 18 coherent groups, 234 time-Gram entries, 1,864 Leibniz terms and 53 nontrivial regularizer patterns; together with K185 this closes the small-radius, angular-face and large-radius regions and leaves only the positive-radius face-stripped determinant core open, but supplies no interval error on that core, complete order-six total error, accurate order-six prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation
manifest: lab/process/k188-order-six-small-rho-strip-wave.json
solver: tests/channel-swings/k188_order_six_small_rho_strip.py
probe: tests/channel-swings/k188_order_six_small_rho_strip_probe.py
target_claim: INTERNAL_TARGET:K187_SPLIT_DOMAIN_SMALL_RHO_STRIP_GATE
target_claim_verdict: SMALL_RHO_STRIP_CLOSED_AT_EPSILON_2_POWER_MINUS_20__POSITIVE_RADIUS_FACE_STRIPPED_CORE_INTERVAL_ERROR_REMAINS_OPEN
canon_verdict_change: none
---

# K188 order-six small-rho strip wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: K185's exact absolute-majorant reduction of the complete K184 order-six
time-Gram family, K186's determinant-preserving Cauchy--Vandermonde
factorization, and K187's radial logarithm obstruction. K188 changes no
operator, extension, state, domain, polarization or scalar center. It closes
only the all-angular small-radius strip under the already proved K185
majorant.

```gu-typed-objects
result: the complete order-six absolute contribution on 0<=rho<2^-20 has an exact proof-safe groupwise ceiling from 1.426373846741254e-34 to 1.283736462067129e-33; the normalized common radial fraction is at most 1/3400103867666144553861120 by P(6,x)<=x^6/720 at x=2^-12
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 coherent path-pair assembly and K186 specieswise determinant factorization remain unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times, exact rational AM--GM allocations and the normalized Gamma-shape-six radial measure
grading: K185 absolute majorant, exact normalized lower-tail inequality, selected dyadic split, complete group propagation, four-region domain cover, independent floating control and withheld positive-core release
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, K179 fixes the coefficient family, K184 fixes the time Grams, K185 fixes the absolute majorant and K186/K187 fix the determinant regularizers and endpoint obstruction; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: remove rho=0 from the determinant-preserving interval domain with an outward all-angular strip bound, compose it with K185's face and tail bounds, and isolate the positive-radius face-stripped core as the only remaining order-six integration region MAP-TYPE=intertwiner
```

## Inline preflight bookend

K187 proved that every current nontrivial determinant pattern has a nonzero
`rho^2 log(rho)` coefficient at one common admissible angular profile. Thus an
ordinary bounded-`C2` radial remainder cannot include zero. That obstruction
does not threaten integrability: K185 already dominates every determinant-
expanded absolute term by a common radial weight `rho^5 exp(-256 rho)` times a
positive Dirichlet density.

The incumbent question is therefore whether that common majorant can remove a
whole endpoint strip without differentiating any regularizer there. The
strongest independently framed source-to-physics challenger remains the
positive physical quotient and count/chirality bridge. `SC-META-53` is
`UNCERTAIN`; ledger-v0.263 rows `LT-SM8`, `RA-F1` and `AC-F1` still require an
action-owned stationary background, functional BV/BFV domain, positive
physical pairing and typed count or chiral carrier. Those inputs remain
absent, so that challenger is dependency-limited.

The route census compared direct interval evaluation of the regularizers near
zero, analytic subtraction of their angular log coefficients, generic
subdivision, and the K185 Gamma majorant. The Gamma route is structurally
strongest for this gate: it is exact, uniform in all angular coordinates,
already covers all determinant terms, and needs no unproved regularizer
derivative. Analytic subtraction may still help the positive core, but it is
not needed to close the endpoint strip.

## 1. Exact normalized lower-tail bound

K185's termwise AM--GM allocation separates every absolute majorant as a
Dirichlet angular weight times

```text
rho^5 exp(-256 rho).
```

After normalization, this is a Gamma density of shape six and rate 256. Let
`x=256 epsilon`. Its lower-tail fraction is

```text
P(6,x)
  = [1/Gamma(6)] integral_0^x u^5 exp(-u) du.
```

For `u>=0`, `exp(-u)<=1`, and `Gamma(6)=5!=120`. Therefore

```text
P(6,x)
  <= [1/120] integral_0^x u^5 du
  = x^6 / 720.
```

This is an exact outward inequality. It is independent of the angular
Dirichlet parameters and of all radial derivatives of the K186 regularizers.

## 2. Explicit split radius

Choose

```text
epsilon = 2^-20,
x = 256 epsilon = 2^-12.
```

Then the normalized lower-tail fraction is bounded by the exact rational

```text
x^6/720
  = 1 / 3400103867666144553861120
  = 2.941086622410765e-25.
```

This ceiling is about `1.8028e4` times smaller than K185's proof-safe
`rho>1/4` tail fraction and about `7.927e9` times smaller than its angular-face
fraction. The split is therefore safely below both already closed boundary
budgets without relying on a floating optimization.

## 3. Complete coherent-group propagation

Multiplying the universal lower-tail fraction by each K185 proof-safe whole-
group ceiling gives

```text
1.426373846741254e-34
  <= small-rho group ceiling
  <= 1.283736462067129e-33.
```

The propagation covers all eighteen coherent groups, all 234 time-Gram
entries, all 1,864 Leibniz terms, all 53 nontrivial regularizer patterns and
all 468 nontrivial occurrences. It does not evaluate the signed determinant
sum on the strip; it bounds its absolute contribution using K185's proved
finite majorant. Thus no cancellation is needed for the outward claim.

For every group, the new small-strip bound is below both its K185 face and
large-radius tail bounds. Adding the three known boundary bounds gives
groupwise ceilings from `1.130722576890900e-24` to
`1.017650319201810e-23`. These sums are valid union bounds; they are not yet
the complete order-six error because the central positive core remains open.

## 4. Four-region domain cover

The complete radialized positive orthant now has the following four-region
cover:

1. `0<=rho<2^-20`, all angular coordinates: **closed by K188**.
2. `2^-20<=rho<=1/4`, some `z_i<2^-180`: **closed by K185's face bound**, which was proved on a superset and remains valid after restriction.
3. `2^-20<=rho<=1/4`, all `z_i>=2^-180`: **open positive-radius face-stripped core**.
4. `rho>1/4`, all angular coordinates: **closed by K185's radial-tail bound**.

This cover is non-overlapping at the level of domains. The inherited K185
face estimate is intentionally looser because it integrates a superset; that
does not invalidate its use on region two.

The only remaining numerical region is now compact and bounded away from both
the radial origin and every primitive angular face. K187's logarithm is no
longer a smooth-endpoint obstruction there. Time-coalescent determinant faces
still use K186's mixed divided differences and must remain unexpanded.
The positive-radius face-stripped core remains open until that interval error
is serialized.

## 5. Independent controls

SciPy's independently implemented regularized incomplete gamma function was
evaluated at `epsilon=2^-16, 2^-20, 2^-24, 2^-28`. At the selected split,

```text
P(6,2^-12) control = 2.940471226379152e-25,
exact rational ceiling = 2.941086622410765e-25.
```

All four controls lie strictly below their rational ceilings. The ratio tends
to one as the split shrinks, as expected. These binary64 values are checks,
not interval arithmetic and not the proof.

## 6. What remains open

K188 does not serialize a determinant-preserving interval error on region
three. The next certificate must derive outward value and mixed-derivative
enclosures for the 53 K186 divided-difference regularizers on

```text
2^-20 <= rho <= 1/4,
z_i >= 2^-180,
```

and use them in a weighted Duffy/Jacobi remainder without expanding the
determinants in the numerical core. It must then add the K188 small-radius,
K185 angular-face and K185 radial-tail errors to obtain one complete outward
order-six error.

The accurate order-six prefix remains through order five. No K171/K168 action
column, `R_ref` residual, complete complement or flux floor, scalar-center
floor or K152 interval is claimed.

The source and physics-ledger statuses remain unchanged: `SC-META-53` remains
`UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`. No physical/source
selection, Born derivation, prediction, confirmation, canon, paper, release or
public-posture conclusion follows.

## Inline postflight bookend

- **Strongest advance:** the radial endpoint is now removed by an exact all-angular error bound rather than an invalid smoothness assumption.
- **Strongest quantitative result:** every coherent group's `rho<2^-20` contribution is below `1.284e-33` under the proof-safe K185 majorant.
- **Strongest structural switch:** three of the four integration regions are closed; only the positive-radius face-stripped determinant core remains.
- **Strongest overclaim:** “the order-six total error is now complete.” Refused; region three has no interval remainder yet.
- **Strongest contrary route:** analytic logarithm subtraction may reduce positive-core derivative cost, but it is unnecessary for endpoint closure and supplies no outward core bound by itself.
- **Weakest reproducibility seam:** future cubature must retain K186 divided differences and complete signed group assembly; evaluating nearly coincident raw determinants would reopen the cancellation failure.

All seven admitted arcs completed. The exact lower-tail theorem, dyadic split,
complete propagation, domain cover, independent control, hostile suite and
positive-core handoff are banked. The result moves the numerical proof
boundary and no source or scientific verdict.

## Reproduction

```bash
python3 tests/channel-swings/k188_order_six_small_rho_strip.py --summary
python3 tests/channel-swings/k188_order_six_small_rho_strip.py --write --summary
python3 tests/channel-swings/k188_order_six_small_rho_strip_probe.py
python3 tests/channel-swings/k188_order_six_small_rho_strip_probe.py --selftest
```
