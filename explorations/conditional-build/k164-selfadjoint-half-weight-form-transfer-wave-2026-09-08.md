---
title: "K164 self-adjoint half-weight form-transfer wave"
status: active_research
doc_type: conditional_selfadjoint_half_weight_interpolation_form_residual_coercivity_and_spectral_transfer_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned topology and certificate-interface result for the supplied equal-coupling two-edge signed point-Fock control; K156 self-adjoint normal ordering plus K161's one-sided full-energy tail admits a half-weight interpolation bound at the regular-form level, while an exact non-normal counterexample forbids the same inference for complex contour denominators; the resulting compiler transfers form-dual residual, coercivity, next-spectrum and left-floor margins from a same-family anchor with explicit thresholds, but that native anchor and its complete spectral data remain absent, so no native count, K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k164-selfadjoint-half-weight-form-transfer-wave.json
solver: tests/channel-swings/k164_selfadjoint_half_weight_form_transfer.py
probe: tests/channel-swings/k164_selfadjoint_half_weight_form_transfer_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K164 self-adjoint half-weight form-transfer wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, observable or Hamiltonian. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet asks whether K161's complete right-weighted tail can be
used at the self-adjoint regular-form level needed by K152. It distinguishes
that question from the already-killed complex-contour inverse route. It proves
a topology conversion and an exact conditional transfer compiler; it does not
supply the still-missing same-family anchor or its global spectral margins.

```gu-typed-objects
result: self-adjoint half-weight interpolation of the complete regular-core tail, exact non-normal obstruction for complex-contour reuse, and conditional residual coercivity next-spectrum and native-left-floor transfer thresholds
carrier: K139's hard-core C3 impurity tensor antisymmetric Fock carrier over the K162 dyadic common momentum-cell family, with K148's unbounded spectator-energy operator A=1+S LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive exterior-Fock Hilbert pairing and the A-half-weight form pairing; K152 residuals live in the shifted form dual and spectral transfer uses the complete same-family min-max form ON=repository_signed_point_control
real_structure: CAR adjoint pairs the four polarity exchange blocks and makes the K156 normal-ordered regular-core difference self-adjoint; no such adjoint closure is asserted for a non-real contour denominator
grading: conserved incidence charge, regular self-adjoint form versus complex contour operator, right full-energy weight versus symmetric half-weight form, anchor residual versus transferred residual, trial line versus complete spectral complement
action_owner: repository-construction -- operator, extension, polarization, couplings, domain, trial anchor and physical state are not selected by Weinstein's source or a GU action
target: convert the K161 five-tail topology into the exact K152 form interface where legal and expose the remaining same-family anchor and complete spectral-floor obligations MAP-TYPE=intertwiner
```

## Inline preflight bookend

K163 correctly refused to call a fixed-cylinder column estimate a complete
form-dual residual. The obvious response would be to compute more columns.
That is not the first question: one must decide whether the one-sided topology

```text
||(W_Lambda-W)A^-1|| <= epsilon_Lambda,  A=1+S       (1)
```

can control the symmetric form sandwich. For a general operator it cannot.
For the self-adjoint K156 normal-ordered regular difference it can, by an
endpoint interpolation theorem that does not require K161's impossible
`AD_W(z)^-1` smoothing factor.

Mechanism retrieval found K156's exact self-adjoint normal-ordered core,
K161's complete five-component right-weighted bound, K162's common carrier,
K163's Galerkin obstruction and K152's shifted form-dual contract. No held
artifact applies the half-weight interpolation step or gives its sharp failure
for non-normal contour differences.

The route census compared column enumeration, direct high-cutoff spectra,
Kato/Heinz interpolation, graph-norm completion, boundary-triple inverses,
non-normal pseudospectral controls, generalized Ritz, min--max, Schur exterior
floors and Lehmann--Goerisch. The half-weight discriminator dominates: it
upgrades all five form tails at once if self-adjointness is available, and an
exact two-dimensional counterexample prevents accidental reuse on the complex
contour. Computation is exact rational certification, not a broad numerical
search.

`SC-META-53` remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain
`NEEDS`. The v0.263 ledger remains 88/88 mapped with `33 SAME / 22 DIFFERS /
31 NEEDS / 2 OVER_DETERMINED`. No source or ledger row changes.

## 1. A one-sided weighted estimate is insufficient in general

Let

```text
A_n = diag(1,n^2),
T_n = [[0, epsilon n^2],[0,0]].                        (2)
```

Then exact singular-value arithmetic gives

```text
||T_n A_n^-1|| = epsilon,
||A_n^-1/2 T_n A_n^-1/2|| = epsilon n.                (3)
```

The right-weighted norm stays fixed while the half-weight norm diverges. At
`n=1024`, `epsilon=1/1000`, the two norms are exactly `1/1000` and
`128/125`. Thus K161's complex-contour denominator difference cannot be
promoted from its one-sided estimate alone. Non-normality is a topology
obstruction even before any inverse or rank calculation.

## 2. Self-adjointness supplies the missing endpoint

Now let `T=T*` be the z-free regular-core difference on the common positive
carrier and assume (1). Taking adjoints yields the second endpoint

```text
||A^-1 T|| <= epsilon_Lambda.                          (4)
```

Apply the three-lines theorem to
`F(z)=A^-z T A^(z-1)`; imaginary powers of `A` are unitary. At `z=1/2`,

```text
||A^-1/2 T A^-1/2|| <= epsilon_Lambda.                (5)
```

Equivalently,

```text
|t[x,y]| <= epsilon_Lambda ||x||_A ||y||_A.           (6)
```

K156's CAR adjoint pairing makes the diagonal normal-ordered term and the sum
of the four polarity exchange tails self-adjoint at the regular-form level.
K161's conservative triangle bound therefore supplies (1) for that complete
sum. This closes the form-topology conversion. It does not resurrect K160:
for non-real `z`, `D_Lambda(z)-D(z)` is not self-adjoint, and (4)--(6) do not
follow.

## 3. Residual and coercivity transfer

Let `a_Lambda` be a same-family anchor form and suppose, on the complete
carrier,

```text
a_Lambda+c >= kappa A,       |a-a_Lambda| <= epsilon A. (7)
```

Then

```text
a+c >= (kappa-epsilon)A.                              (8)
```

For any trial vector `u`, if `r_Lambda` is its anchor residual in `A*`,

```text
||r||_(A*) <= ||r_Lambda||_(A*) + epsilon ||u||_A.    (9)
```

Thus K161's tail can become the complete shifted form-dual residual increment,
not merely a list of columns. The strict threshold is `epsilon<kappa`.
Crucially, (7) must hold on the complete same-family carrier. K155's arbitrary
two modes and K157's zero-fill block do not supply it.

## 4. Exact next-spectrum and native-left-floor transfer

Put `delta=epsilon/kappa<1`. Equation (7) implies

```text
(1-delta)(a_Lambda+c) <= a+c
                         <= (1+delta)(a_Lambda+c).     (10)
```

The min--max principle transfers every complete anchor eigenvalue bound:

```text
(1-delta)(E_j,Lambda+c)-c <= E_j
                         <= (1+delta)(E_j,Lambda+c)-c. (11)
```

For a declared anchor with ground upper `-1`, next lower `2`, complete left
floor `-4`, shift `c=6`, and target threshold `b=0`, the strict lower bounds
on `kappa` are

```text
ground remains below 0:        kappa > 5 epsilon,
next value remains above 0:    kappa > 4 epsilon,
left floor remains above -5:   kappa > 2 epsilon.      (12)
```

At `Lambda=4096`, K161 has `epsilon=79277/319488`; the combined demand is
`kappa>396385/319488`, so a `kappa=1/2` positive-control anchor fails the
count margin even though its transferred left floor remains above `-5`.

At `Lambda=65536`, `epsilon=6622297/123076608`; the combined demand is
`kappa>33111485/123076608`. The exact `kappa=1/2` control passes:

```text
ground upper = -28426819/61538304 < 0,
next lower   =  8762279/7692288   > 0,
left floor   = -129698905/30769152 > -5.              (13)
```

This is a nonvacuous exact compiler control, not native GU data. It proves the
cutoff scale can be quantitatively adequate once a same-family anchor supplies
the named margins.

## 5. Native K152 replay

The current chain now supplies two items that K163 listed as open:

- the complete self-adjoint regular-tail form topology, from K156 + K161 +
  (5); and
- the complete signed flavor transport, from K162.

Native admission still fails closed because no conforming same-family anchor
serializes its global coercivity, trial residual, next-distinct-spectrum floor
and complete native left floor. Therefore (9)--(13) are conditional interfaces,
not a native count or K152 interval.

## Inline postflight bookend

- **Strongest advance:** self-adjointness converts the complete one-sided
  K161 regular tail into the symmetric half-weight form bound K152 needs.
- **Strongest obstruction:** the exact non-normal family (2) makes the same
  inference arbitrarily false on a complex contour.
- **Strongest quantitative result:** equations (9)--(12) give exact residual,
  coercivity, ground/next-gap and below-`-5` transfer thresholds. The K161
  `65536` tail passes a nonvacuous `kappa=1/2` synthetic anchor control.
- **Strongest overclaim:** “K164 closes the native K152 count.” Refused. The
  same-family anchor and all of its complete spectral data are absent.
- **Strongest contrary route:** a direct complex-contour theorem with a
  second independently proved left-weight bound could still avoid
  self-adjointness. K161 supplies no such endpoint, and its inverse route is
  already killed.
- **Weakest reproducibility seam:** K161's conservative denominator bound must
  be attached explicitly to the z-free self-adjoint regular-core difference
  on the chosen anchor family; an untyped contour reference is inadmissible.

All five admitted arcs were attempted inline. The self-adjoint and non-normal
discriminators completed, the residual/coercivity and spectral compilers
closed conditionally, and native K152 replay failed only on the exact anchor
data named above. No external retrieval or second writer was used.

## Next condition

Construct one physical K162 dyadic same-family anchor by compressing the fixed
normal-ordered K139 form, not by independent rediscretization. On the complete
charge carrier, prove `a_Lambda+6 >= kappa(1+S)` and certify ground upper,
next-distinct lower, complete left floor and trial residual. Choose a cutoff
whose K161 `epsilon` is below the exact combined `kappa` margin; `65536` is
already viable for the displayed `kappa=1/2` control, whereas `4096` is not.
Then apply (9)--(13), transport `q=(0,1)` through K162 and feed the complete
packet to K152. If the anchor floors cannot be proved by a free-gap/exterior
minorant, switch to form-level Lehmann--Goerisch on the same fixed form. Do not
reuse a contour operator as self-adjoint, identify K155/K157 regulator matrices
as native, or count a bounded island as the complete spectrum.

## Reproduction

```bash
python3 tests/channel-swings/k164_selfadjoint_half_weight_form_transfer.py --demo
python3 tests/channel-swings/k164_selfadjoint_half_weight_form_transfer_probe.py
python3 tests/channel-swings/k164_selfadjoint_half_weight_form_transfer_probe.py --selftest
```
