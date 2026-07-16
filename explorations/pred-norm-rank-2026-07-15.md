---
artifact_type: exploration
label: PRED-NORM-RANK
status: "exploration (normalization rank endpoint; NO_GO for current fixed-range and fixed-pole prediction routes at built-structure grade; no canon/verdict/claim-status/posture movement)"
created: 2026-07-15
title: "PRED-NORM-RANK: the built normalization structure leaves only scale-relative invariants; no native absolute pole or range scale is fixed"
posture: "adversarial Track B prediction extraction; native scale audit; target data not used as construction input"
grade: "COMPUTED for the monomial-rank certificate in tests/normalization-scoping/pred_norm_rank.py; SOURCE-GROUNDED in W229 and W239 for the free-scale ledger; ARGUED for the route disposition"
depends_on:
  - explorations/W229-close-a2-source-action-znu-completion-2026-07-14.md
  - explorations/W239-track-b-distinctive-prediction-scan-2026-07-15.md
  - explorations/pred-flavor-rank-2026-07-15.md
scripts:
  - tests/normalization-scoping/pred_norm_rank.py
---

# PRED-NORM-RANK

## Result

**Operational result: `NO_GO` for the current fixed-range and fixed-pole prediction routes.**

The built GU normalization structure preserves useful scale-relative invariants, but it does not fix a
native absolute value for `mu_DW`, `Z_U*kappa`, or source normalization. Therefore the present structure
cannot emit a calibration-independent pole mass, force range, or dark-energy-to-pole scale.

This does not say the route is mathematically impossible. It says the current built objects leave the scale
free at the grade available now. A future native source datum or normalization dynamics could reopen it.

## Construction fork

The fork is the native DeWitt/gimmel ratio-only geometry versus the standard massive-spin-2 normalization.

- Native side used here: `mu_DW` is the DeWitt/gimmel scale, W229 leaves `{kappa, Z_U}` as normalization
  magnitudes, and the screening combination `ell^2 = Z_U*kappa` is invariant under the local field
  normalization.
- Standard physics side compared but not imported: a higher-derivative spin-2 pole has a standard
  `alpha = 1/3` Yukawa trace factor and a dimensionless pole coefficient. Those do not make the absolute
  GU scale native.

The test deliberately does not use the observed dark-energy density, torsion-balance bounds, or target
data to select `mu_DW`.

## Rank model

The certificate uses log-monomial exponents for:

```text
kappa, Z_U, mu_DW, m_pole, lambda_pole, rho_quarter, source_norm
```

and three free rescalings:

| rescaling | nonzero weights |
|---|---|
| field normalization | `kappa:+1`, `Z_U:-1` |
| DeWitt scale | `mu_DW:+1`, `m_pole:+1`, `lambda_pole:-1`, `rho_quarter:+1` |
| source normalization | `source_norm:+1` |

The exact scaling matrix has rank `3`, so the invariant quotient has dimension `4`.

## Invariants that survive

| invariant | what it means | why it does not fix a prediction |
|---|---|---|
| `Z_U*kappa` | screening length squared `ell^2` survives the field normalization | the product is still a free native scale |
| `m_pole/mu_DW` | dimensionless pole mass ratio survives | no absolute `mu_DW` value is supplied |
| `lambda_pole*mu_DW` | range in DeWitt units survives | no absolute range is supplied |
| `rho_quarter/mu_DW` | density-quarter scale ratio survives | using observed `rho_quarter` would be target calibration |

No invariant basis element contains `source_norm`. Any route that depends on source normalization must wait
for a native source-normalization rule.

## Route disposition

| route | disposition | reason |
|---|---|---|
| fixed-range gravity | `NO_GO` at current grade | `m_pole` and `lambda_pole` move with the free `mu_DW` scale |
| H36 dark-energy density lock | killed as native prediction route | the numerical scale uses observed `rho_Lambda` to solve for `mu_DW` |
| source screening length | underdetermined | `ell^2 = Z_U*kappa` is invariant but not numerically fixed |

The dimensionless coefficients recorded by W239 still survive as coefficients:

```text
c_L = 3/8
alpha = 1/3
m2_eff in [5/6, 5/4]
```

They are not enough to fix a native absolute scale.

## What changed

- `PRED-FLAVOR-RANK` had already closed the current zero-parameter flavor route.
- This run closes the next scale-normalization route at the current built-structure grade.
- Track B now needs either a new native normalization/source datum, a physical mirror observable, or another
  daily-steward-selected lane. The daily steward owns portfolio reconciliation.

## What did not change

- No canon, verdict, claim-status, public-posture, paper, `bar(b)`, or H59 status changed.
- This note does not claim GU is false, does not use target data as a construction input, and does not convert
  a conditional coefficient into a prediction.

## Machine receipt

Run:

```text
python tests/normalization-scoping/pred_norm_rank.py
```

Expected endpoint:

```text
RESULT :: NO_GO for current fixed-range/fixed-pole prediction routes
```
