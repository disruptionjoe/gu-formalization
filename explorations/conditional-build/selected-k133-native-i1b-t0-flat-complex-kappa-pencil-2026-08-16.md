---
title: "Selected-K133 native I1B T=0 flat-complex and kappa-pencil classification"
status: active_research
doc_type: exact_flat_symbol_square_and_universal_nondegenerate_parameter_pencil
created: "2026-08-16"
registry: lab/process/selected-k133-native-i1b-t0-flat-complex-kappa-pencil.json
probe: tests/channel-swings/selected_k133_native_i1b_t0_flat_complex_kappa_pencil_probe.py
grade: "K133 CLOSES THE FLAT OR CURVATURE-CENTRAL KAPPA-ZERO EXCEPTION: REMOVING D_B SQUARED EQUALS AD(F_B) DOES NOT MAKE THE SELECTED-SHIAB EULER OPERATOR A COMPLEX. ITS TIMELIKE, SPACELIKE AND NULL SYMBOL-SQUARE RANKS ARE 130912,130912,122746, EQUAL TO ITS NONZERO SYMBOL RANKS; EACH EXCEEDS THE 114688 MAXIMUM FOR A SQUARE-ZERO ENDOMORPHISM ON THE 229376-DIMENSIONAL CARRIER. FOR P_N(KAPPA)=C_1(N)+KAPPA K WITH K NONDEGENERATE, EACH FIXED-COVECTOR DETERMINANT HAS DEGREE 229376 AND NONZERO LEADING COEFFICIENT DET(K), SO THE COMPLEX EXCEPTIONAL SET IS FINITE AND THE FROZEN-FREQUENCY MAP IS GENERICALLY INVERTIBLE. NONDEGENERACY ALONE DOES NOT DETERMINE REAL ROOTS, INERTIA OR A UNIFORM INVERSE. KAPPA K IS LOWER ORDER, SO ALL CAUSAL CONORMALS REMAIN PRINCIPAL-CHARACTERISTIC AND NO CLOSED ULTRAHYPERBOLIC DOMAIN, KT/BFV QUOTIENT OR PHYSICAL COHOMOLOGY FOLLOWS. K134 MUST CONSTRUCT THE ACTUAL ALL-GRADE K STRUCTURE FINGERPRINT BEFORE ROOT, INERTIA OR DOMAIN CLASSIFICATION."
target_claim: K132_NEXT_GATE__FLAT_OR_CENTRAL_CURVATURE_KAPPA_ZERO_COMPLEX_AND_NONZERO_KAPPA_ALL_GRADE_PARAMETER_PENCIL
target_verdict: FLAT_OR_CENTRAL_CURVATURE_REMOVES_ADF_BUT_SELECTED_EULER_SYMBOL_IS_NOT_SQUARE_ZERO__FIXED_COVECTOR_KAPPA_PENCIL_IS_GENERICALLY_INVERTIBLE_WITH_FINITE_COMPLEX_EXCEPTIONAL_SET__REAL_ROOTS_AND_INERTIA_REQUIRE_ACTUAL_K_FINGERPRINT__PRINCIPAL_CHARACTERISTICS_AND_DOMAIN_OBSTRUCTIONS_PERSIST
canon_verdict_change: none
---

# Selected-K133 native I1B T=0 flat-complex and kappa-pencil classification

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, full-adjoint Clifford-grade, mixed-order symbol and
> algebraic-pencil calculation. Ordinary Einstein-action, fermionic K77,
> particle-spectrum, Higgs/VEV, family-index, chirality, anomaly and symmetry-
> breaking constructions do not adjudicate it without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this result binds K132's selected displayed `comm/symi/symi` Euler
coefficient on the complete real `Omega1(Cl(7,7))` carrier at K127's local
Ricci-flat `T=0` fixed-boundary germ. It resolves the flat/curvature-central
zero-`kappa_1` symbol horn and the statements licensed by nondegeneracy of the
quadratic-`T` map `K`. It does not construct the full all-grade matrix of `K`,
determine its real pencil roots or inertia, select `kappa_1`, or construct a
global closed operator, inverse, BFV quotient or physical cohomology.

## Result in plain English

K132 found two possible ways the generic distortion-complex obstruction might
change: set the background curvature action to zero, or restore the
nondegenerate algebraic `kappa_1 K` term. Neither produces a distortion
cohomology.

The flat horn fails for a simpler reason than curvature. The selected Euler
symbol is an endomorphism of a `229376`-dimensional carrier. Any square-zero
endomorphism has image contained in its kernel, hence rank at most `114688`.
But K132's exact ranks are

```text
rank C_1(n) = 130912, 130912, 122746                 (1)
```

on timelike, spacelike and null conormals. Every value exceeds the square-zero
ceiling. Exact replay of all `56/56/49` invariant block types sharpens this:

```text
rank C_1(n)^2 = 130912, 130912, 122746.              (2)
```

In compact causal order, the symbol-square ranks are
`130912/130912/122746`.

Thus flatness removes the separate covariant-curvature obstruction
`D_B^2=ad(F_B)`, but the selected Shiab-projected Euler operator itself is not
a differential. Its image is not contained in its kernel, so there is no
symbol cohomology of `C_1` as a repeated differential to promote to KT or BFV.

For nonzero `kappa_1`, the universal frozen-frequency pencil is

```text
P_n(kappa_1) = C_1(n) + kappa_1 K,   det K != 0.      (3)
```

For each fixed covector, its determinant is a degree-`229376` polynomial with
leading coefficient `det K`. It is therefore not the zero polynomial: over the
complex numbers it has only a finite exceptional multiset, and the frozen-
frequency map is invertible away from that set. At zero frequency it is
invertible for every nonzero `kappa_1`.

That is the strongest conclusion available without the actual `K` fingerprint.
Nondegeneracy does not determine which exceptional roots are real. Already in
two dimensions, the same skew coefficient with `K=I` gives determinant
`kappa^2+1`, while `K=diag(1,-1)` gives `1-kappa^2`. Both `K` matrices are
nondegenerate; only the second has real nonzero roots. Hence no real-root,
inertia or uniform inverse claim is licensed by the word "nondegenerate."

## 1. Flat or curvature-central zero-kappa horn

The relevant distinction is

```text
covariant input:       D_B^2 = ad(F_B),
selected Euler symbol: C_1(n) = antisymmetrized Shiab-projected coefficient.
```

Flat or central curvature sets the first line to zero. It does not set
`C_1(n)^2` to zero. The exact block matrices are real skew, so their nonzero
eigenvalues occur in imaginary pairs and `ker C_1(n)^2=ker C_1(n)`. Equation
(2) is therefore an exhaustive all-grade certificate, not a single-block
counterexample.

The exceptional background is consequently simpler but not cohomological.
It may still admit ordinary solutions of `C_1(D)T=0`, but these are equations
on a characteristic ultrahyperbolic operator, not cycles modulo boundaries of
the same selected differential.

## 2. Nonzero-kappa parameter pencil

Equation (3) gives three exact levels:

| level | established | not established |
| --- | --- | --- |
| zero frequency | `kappa_1 K` is invertible for `kappa_1!=0` | a physical mass or selected coupling |
| fixed covector | generic complex-parameter invertibility; finite exceptional multiset | real roots, inertia, uniform bounds |
| PDE principal symbol | unchanged from K132 because `K` is zero order | ellipticity, hyperbolicity or a closed domain |

The fixed-covector exceptional condition is the algebraic hypersurface

```text
det(C_1(n)+kappa_1 K)=0.                              (4)
```

Scaling `n` rescales `C_1(n)` but not `kappa_1 K`, so the roots move with
frequency. A pointwise generic inverse is not a uniform Fourier multiplier,
and it supplies neither estimates nor a common closed domain.

## 3. Characteristic, Noether, KT and BFV disposition

The lower-order term cannot change K132's principal ranks. Every causal
conormal remains principal-characteristic, with the same null rank jump.
Flatness also creates no new action owner: at `T=0`, distortion transforms
tensorially and the only owned gauge columns remain the four metric
diffeomorphisms.

Therefore:

- the flat selected Euler map is not a distortion differential;
- the nonzero-`kappa_1` frozen-frequency pencil is generically invertible but
  is not a principal-symbol repair;
- no distortion KT tower or nilpotent BV completion is selected;
- the cross-stratum constant-rank BFV obstruction remains; and
- the ambient ultrahyperbolic problem still needs an explicitly supplied
  signature-appropriate domain and boundary data.

## 4. Next gate

K134 must construct the actual all-grade quadratic-`T` structure fingerprint:
carrier, pairing, real involution, grading action and invariant-block form of
`K`. It must then compute the real exceptional roots and inertia of (4) on the
three causal representatives, test whether any frequency-uniform gap exists,
and compare the resulting admissible data with a signature-appropriate closed
domain. Without that fingerprint, a root list would be an invented
attribution.

No ledger, canon, public posture, particle, phenomenology or GU truth-status
claim changes. Joe input is not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k133_native_i1b_t0_flat_complex_kappa_pencil_probe.py
```
