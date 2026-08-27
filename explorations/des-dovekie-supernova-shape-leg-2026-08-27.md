---
title: "The current DES Dovekie supernova pure-shape leg independently retains the GU comparator penalty"
status: exploration
doc_type: determination
created: "2026-08-27"
grade: "OFFICIAL-DATA LIKELIHOOD REPLAY WITH FULL STAT+SYS PRECISION AND ANALYTIC ABSOLUTE-MAGNITUDE MARGINALIZATION; GU BACKGROUND REMAINS RECONSTRUCTION-GRADE"
scripts:
  - tests/de-certification/de14_des_dovekie_supernova_shape.py
target_claim: "M-M18 / DE-14"
target_claim_verdict: "SUPERNOVA-PURE-SHAPE-PENALTY-RETAINED"
comparator_classification: STANDARD_FIELD_CONTROL_ONLY
canon_verdict_change: none
---

# DES Dovekie supernova pure-shape leg

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `STANDARD_FIELD_CONTROL_ONLY`

```gu-typed-objects
result: DES Dovekie supernova pure-shape likelihood replay
carrier: 1820 released distance moduli with full statistical-plus-systematic precision LAYER=observed CHIRALITY=N/A
pairing: released inverse covariance ON=distance-modulus residual vector after additive-offset projection
real_structure: real Gaussian residual space
grading: likelihood contribution only
action_owner: comparator -- DES release owns data; GU M2=8 f0=0.125 background is repository reconstruction
target: pure late-time distance-shape comparison MAP-TYPE=evaluation by an FLRW luminosity-distance likelihood
```

Scope: this result evaluates the existing reconstruction-grade GU dark-energy
background as a standard FLRW distance comparator. It is not a source-action
derivation, a family-wide exclusion, a prediction, or an `H0` measurement.

## Frozen official inputs

The replay uses the current official
[`des-science/DES-SN5YR`](https://github.com/des-science/DES-SN5YR) release at
commit `c9a4fcafc4cbd19bd750dee47fc76194a45c181f`:

| input | SHA-256 | role |
|---|---|---|
| `4_DISTANCES_COVMAT/DES-Dovekie_HD.csv` | `2f57019d783eaa976df80a41b0054171a2d994ee9808d715ce850c2df5720aaf` | 1,820 `zHD`, `zHEL`, `MU` rows |
| `4_DISTANCES_COVMAT/STAT+SYS.npz` | `ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b` | released upper-triangular inverse covariance |

The repository's official likelihood prescription is followed exactly at the
essential step: for residual `d`, precision `P` and all-ones vector `1`, the
additive absolute-magnitude offset is marginalized as

```text
chi2_Mmarg = d^T P d - (1^T P d)^2 / (1^T P 1).
```

This makes the statistic invariant under a constant shift in all model distance
moduli. Supernovae therefore contribute shape information here, not `H0`.

## Result

The current official data give:

| model | fixed/fit inputs | marginalized chi2 |
|---|---|---:|
| flat LCDM | `Omega_m=0.315` | `1632.45156` |
| flat LCDM | `Omega_m=0.3518722`, matching the calibrated GU comparator | `1633.35213` |
| flat LCDM | SN-only best fit `Omega_m=0.3303173` | `1631.42056` |
| GU theta comparator | `M2=8`, `f0=0.125`, theta-star-calibrated `h=0.6374932`, `Omega_m=0.3518722` | `1652.55789` |

Thus

```text
Delta chi2(GU - same-Omega_m LCDM) = +19.20577
Delta chi2(GU - best flat LCDM)    = +21.13734.
```

The same-`Omega_m` row is the decisive shape control: the roughly `+19.2`
penalty is not created by the calibrated matter fraction. The previously open
possibility that an absolute-magnitude-marginalized supernova leg might rescue
the comparator does not occur in the current Dovekie release. This independently
matches the scale of the earlier DESI amplitude-marginalized shape residue, but
the two likelihoods are not combined here and numerical similarity is not an
identity.

## Claim ceiling and next condition

DE-14 is executed at official-data comparator grade. M-M18 remains live because
DE-13 still needs the exact official DESI posterior correlation and DE-15 still
needs an owner-frozen compressed Planck likelihood. Neither missing addition can
erase or be inferred from this independent supernova result. No canon, source,
prediction, confirmation or public posture moves.

Reproduce after acquiring the two frozen official files:

```text
python3 tests/de-certification/de14_des_dovekie_supernova_shape.py \
  --data-dir /path/to/DES-SN5YR/4_DISTANCES_COVMAT --selftest
```
