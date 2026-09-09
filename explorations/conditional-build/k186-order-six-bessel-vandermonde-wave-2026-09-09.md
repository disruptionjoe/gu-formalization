---
title: "K186 order-six Bessel Cauchy--Vandermonde wave"
document_role: active_research
doc_type: conditional_native_K139_K186_order_six_bessel_cauchy_vandermonde_factorization_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned factorization of all 468 nontrivial size-two and size-three Bessel determinants in K185's 234 factorial-free order-six time-Gram entries into their canonical sign, Cauchy denominator product, two ordered-time Vandermonde zero families and a strictly positive regular Bessel quotient; a mixed-divided-difference evaluator and high-precision face/small-radius controls remove subtractive determinant loss, but no outward regularizer-derivative enclosure or determinant-preserving compact-core quadrature remainder is yet proved, so no accurate certified order-six prefix, action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is obtained
manifest: lab/process/k186-order-six-bessel-vandermonde-wave.json
solver: tests/channel-swings/k186_order_six_bessel_vandermonde.py
probe: tests/channel-swings/k186_order_six_bessel_vandermonde_probe.py
target_claim: INTERNAL_TARGET:K185_ORDER_SIX_BESSEL_VANDERMONDE_FACTOR_GATE
target_claim_verdict: ALL_468_NONTRIVIAL_BESSEL_DETERMINANTS_HAVE_EXACT_SIGN_AWARE_CAUCHY_VANDERMONDE_FACTORIZATIONS_AND_POSITIVE_COALESCENT_REGULARIZERS__OUTWARD_REGULARIZER_DERIVATIVE_AND_COMPACT_CORE_CUBATURE_ERROR_OPEN
canon_verdict_change: none
---

# K186 order-six Bessel Cauchy--Vandermonde wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: K185's fixed K139/K156 hard-core `C3` impurity control with auxiliary
chart `lambda=256`, equal couplings one and the three normalized K162 zero-bath
seed orbits. K186 changes no operator, extension, state, domain, polarization
or scalar center. It preserves all K179 coefficients, K184 coherent Gram
entries, old-position factors, species determinants and shared primitive time
nodes.

```gu-typed-objects
result: every one of K185's 468 nontrivial size-two/three Bessel determinants factors exactly into its canonical permutation sign, 2^m, two ordered-time Vandermonde products, the full Cauchy denominator product and a strictly positive regularizer R_m; all 234 Gram entries replay with 53 unique factor patterns, and mixed Newton divided differences remain stable at 2^-180 primitive gaps and rho=2^-200
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-six output sector; K184 specieswise Andreief reduction and coherent path-pair assembly remain unchanged ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, positive Laplace times, the Stieltjes/Laplace representation of 2 K1 and exact ordered Cauchy determinants
grading: K184 coherent group and Gram-entry identity, left/right path, old positions, canonical species time order, row/column parity, primitive Vandermonde gaps, Cauchy cross supports and regularizer size m in {1,2,3}
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W=(E_R-256)I-X, K179 fixes the coefficient family, K184 fixes the time Grams and K185 fixes the weighted faces; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: remove subtraction loss from every compact-core Bessel determinant while refusing to convert high-precision controls into an outward cubature certificate MAP-TYPE=intertwiner
```

## Inline preflight bookend

K185 closes the singular-support allocation, every simplex face strip and the
large-radius tail. Its exact next dependency is the determinant-preserving
compact core: direct interval entries near coincident cumulative times lose
the very Vandermonde cancellation that makes the species determinant small.

The incumbent question is whether every size-two and size-three kernel can be
factored before enclosure. The strongest independently framed source-to-
physics challenger remains the positivity/state bridge: `SC-META-53` is
explicitly `UNCERTAIN`; ledger-v0.263 rows `LT-SM8`, `RA-F1` and `AC-F1`
still require an action-owned stationary background, functional BV/BFV
domain, positive physical pairing and typed count or chiral carrier. Those
inputs remain absent, so the challenger has no executable first discriminator
that outranks K185's complete internal input.

The route comparison included direct determinant boxes, generic arbitrary
precision, mixed divided differences, exact Cauchy factorization, the
Andreief energy representation and coalescent derivative jets. Direct boxes
repeat subtraction loss, while arbitrary precision alone supplies no proof.
The selected route factors the singular Cauchy skeleton and both zero families
exactly, proves the remaining quotient positive and continuous, and uses a
separately implemented divided-difference evaluator as a stress control.

## 1. Complete determinant census

The 234 time-Gram entries inherited from K184 contain 872 species determinants:

```text
size one:    404
size two:    404
size three:   64
```

Every entry has exactly two nontrivial determinants. Thus K186 factors 468
size-two/three occurrences. Their position data reduce to 53 unique canonical
factor patterns. The resulting skeleton inventory contains 2,596 Cauchy
denominator factors and 1,192 primitive-time Vandermonde gap factors.

All source occurrence lists are already in increasing position order, hence
all 872 serialized determinant permutation signs are `+1`. This is a checked
fact about K184's current family, not an assumed convention: the solver stores
row and column parity independently, and its probe plants odd permutations.
The 234 full entry signs therefore remain exactly K184's 146 positive and 88
negative coefficient products.

For positions `a<b`, cumulative times obey

```text
T_a - T_b = s_a + ... + s_(b-1),
U_a - U_b = v_a + ... + v_(b-1).
```

Every such primitive support is serialized. No determinant zero is represented
as a subtraction of nearly equal Bessel products in the new skeleton.

## 2. Exact Cauchy--Vandermonde factorization

For one canonically ordered size-`m` species block, let

```text
F_ij = 2 K_1(T_i+U_j),
C_ij = 2/(T_i+U_j),
V_T  = product_(i<j) (T_i-T_j),
V_U  = product_(i<j) (U_i-U_j),
```

where increasing positions make the cumulative times strictly decreasing.
The Cauchy identity gives exactly

```text
det C = 2^m V_T V_U / product_(i,j) (T_i+U_j).
```

Define

```text
R_m(T,U) = det F / det C.
```

Then the desired determinant is

```text
det F = 2^m V_T V_U R_m(T,U)
        / product_(i,j) (T_i+U_j).
```

For an uncanonicalized occurrence, multiply by the independently serialized
row and column permutation signs. This is the exact cancellation-free target
for a later interval rule: the denominator supports, zeros and sign are all
explicit, and only the regular quotient remains to be enclosed.

## 3. Positivity and coalescent extension

The integral representation

```text
2 K_1(x) = integral_R exp(-x sqrt(1+p^2)) dp
```

places `F` in the strictly totally positive Laplace-kernel family. Andreief
writes its canonical determinant as an integral of the product of two
exponential alternants against a positive infinite-support energy measure.
For distinct equally ordered `T` and `U`, the two alternants have the same
sign, so `det F` is strictly positive. The canonical Cauchy determinant is also
strictly positive; hence `R_m>0`.

Successive Newton row divided differences divide `det F` by the ordinary
Vandermonde in `T`; the same column operation divides by the Vandermonde in
`U`. At coincident nodes the transformed entries extend to the corresponding
mixed derivative jets, with the all-coincident value

```text
F^(i+j)(T+U)/(i! j!).
```

The Cauchy quotient has the same extension and is nonzero away from
`T_i+U_j=0`. Therefore `R_2` and `R_3` extend continuously across all ordered-
time coincidence faces in the positive domain.

Finally `K_1(x)=x^-1+O(x log x)` at the origin. Consequently

```text
R_m(rho t, rho u) -> 1
```

for each positive angular point. Combined with the coalescent extension, this
proves a bounded positive regularizer on K185's face-stripped compact angular
simplex and `0<=rho<=1/4`. It does not supply a usable outward bound on the
regularizer or its Duffy derivatives.

## 4. Independent numerical controls

The solver implements the integer-order convergent series for `K_1`, then a
Newton row/column divided-difference transform independent of the direct
determinant quotient.

- All 468 canonical nontrivial determinants are positive at the fixed interior
  replay point, and all original occurrence signs match the serialized parity.
  The sampled regularizers lie in `[0.8858988128835127,
  0.9812577648472200]`.
- Across three deterministic profiles for all 53 patterns, 159 direct and
  divided-difference regularizers agree within `2.00e-27` relatively. Their
  sampled range is `[0.8804248822657249, 0.9880041699766289]`.
- At primitive gaps `2^-180`, size two and three controls give regularizers
  `0.8770103341061004937` and `0.7888945164217040929`; the direct and divided-
  difference paths agree within `3.95e-193` and `3.15e-198` relatively.
- At `rho=2^-200`, both sizes approach one; their recorded distances from one
  are `1.14e-119` and `8.88e-119`.

These are high-precision controls, not outward intervals. In particular, the
sampled apparent range below one is not promoted to a theorem.

## 5. Honest release boundary

K186 removes the algebraic and numerical subtraction obstruction. It does not
close the numerical-analysis obligation. A decision-grade compact-core rule
still needs explicit outward enclosures for `R_2`, `R_3` and the mixed Duffy/
Jacobi derivatives used by its remainder theorem. Only then may it integrate
the exact Cauchy--Vandermonde skeleton and combine that error with K185's face
and radial-tail bounds.

Accordingly the accurate certified prefix remains through order five. No
complete K171/K168 action column, `R_ref` residual, complete complement or flux
floor, scalar-center floor or K152 interval is claimed.

The determinant-preserving compact-core quadrature error remains open.

The source and physics-ledger statuses remain unchanged: `SC-META-53` remains
`UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`. No physical/source
selection, Born derivation, prediction, confirmation, canon, paper, release or
public-posture conclusion follows.

## Inline postflight bookend

- **Strongest advance:** all 468 nontrivial determinants now have exact
  sign-aware Cauchy--Vandermonde skeletons and positive coalescent regularizers.
- **Strongest negative result:** factorization alone does not certify the
  compact-core integral; a uniform outward derivative enclosure is still
  absent.
- **Strongest structural switch:** future interval work acts on only 53 smooth
  regularizer patterns, not 468 subtraction-sensitive determinants or 1,864
  Leibniz terms.
- **Strongest overclaim:** “the sampled regularizers below one prove `R_m<=1`.”
  Refused; no such outward theorem is claimed.
- **Strongest contrary route:** direct arbitrary precision can reproduce
  interior points, but without a remainder theorem it cannot certify the
  weighted integral.
- **Weakest reproducibility seam:** the next solver must outwardly enclose the
  mixed Duffy derivatives, including the `rho=0` extension, rather than merely
  raise precision.

All seven admitted arcs were attempted. The inventory, exact factorization,
positivity/coalescence proof, divided-difference evaluator, all-entry replay and
two stress regimes completed. The final release replay correctly withheld the
order-six prefix because the outward regularizer-derivative certificate is not
yet present.

## Reproduction

```bash
python3 tests/channel-swings/k186_order_six_bessel_vandermonde.py --summary
python3 tests/channel-swings/k186_order_six_bessel_vandermonde.py --write --summary
python3 tests/channel-swings/k186_order_six_bessel_vandermonde_probe.py
python3 tests/channel-swings/k186_order_six_bessel_vandermonde_probe.py --selftest
```
