---
title: "DE-AMP diagnostic closure audit"
status: exploration
doc_type: research_register
created_at: "2026-07-15"
claim_status: OPEN
scope: "DE-AMP-DIAGNOSTIC closure recommendation for daily steward reconciliation"
inputs:
  - explorations/W242-desi-intake-and-hourly-prediction-queue-2026-07-15.md
  - explorations/wave45/H46B-referee-grade-desi-verification-2026-07-13.md
  - explorations/wave46/H46C-theta-star-gu-cmb-calibration-2026-07-13.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
machine_receipt:
  - process_gates/de_amp_diagnostic_closure_audit.py
governance: "Exploration-tier closure recommendation only. No canon, verdict, claim-status, public-posture, paper, or external-action move."
---

# DE-AMP Diagnostic Closure Audit

## Result

Operational result: CLOSED for the bounded diagnostic question.

The recommended daily-steward disposition is that `DE-AMP-DIAGNOSTIC` no longer needs another
hourly technical run merely to prove H46B-locality or repeat the amplitude audit. The diagnostic lane is closable
because the local chain already contains:

- H46B primary-source verification of the official DESI DR2 BAO likelihood mean/covariance and Planck
  digits;
- H46C re-solve of GU's own `theta_star` calibrated amplitude using that likelihood machinery;
- W129 sweep across the OQ2 `M^2` band and ansatz variants at the same calibration standard.

This is not a prediction. It is data hygiene and normalization adjudication. It does not fix a native
quantity, produce a blind relation, promote the theta dark-energy verdict, or change `bar(b)` / `H59`.

## Construction Fork

The calculation intentionally combines two different constructions without flattening them:

- GU-side object: the theta-sector background family already built in the H44/H46/H46C machinery.
- Observational side: the standard late-time cosmology likelihood apparatus, seeded only by H46B-verified
  official DESI DR2 and Planck inputs.

The reason for using the observational apparatus is narrow: `DE-AMP-DIAGNOSTIC` asks whether the
CMB-calibrated amplitude leg survives the same official likelihood inputs that H46B verified. It does not
make that apparatus a GU-native derivation, and it does not convert a fitted amplitude into a native
prediction.

## Load-Bearing Source Objects

- `tests/wave45/H46B_referee_grade_desi_verification.py` embeds and verifies the official 13-element DESI
  DR2 likelihood mean and covariance and the Planck digits used by the chain.
- `tests/wave46/H46C_theta_star_cmb_calibration.py` consumes the H46 raw-likelihood machinery, computes
  GU's own CMB-calibrated amplitude, and records the row-2 `theta_star` adjudication.
- `tests/W129_oq2_m2_band_sweep.py` imports H46C and runs the OQ2 band sweep, ansatz variants, and
  profiled `omega_m h^2` checks.
- `lab/process/recovery-certification-matrix.json` classifies `DE-AMP-DIAGNOSTIC` as `DIAGNOSTIC`, not as
  a distinctive prediction.

## Closure Condition

The first closure condition was: verified H46B inputs must be local, and the follow-on diagnostic must use
those inputs without target-fitting language or prediction framing.

That condition is met locally. H46B is present as both a script and exploration note; H46C and W129 consume
the H46/H46B machinery and record the amplitude result and band-wide diagnostic result. The source-quality
guard from W242 remains intact: secondary report tables are not allowed to seed GU likelihood arrays.

## Residuals

The residuals are real but outside this bounded diagnostic:

- SNe integration remains named residual evidence hygiene.
- A second BAO dataset can harden robustness but is not needed to close the H46B-locality and amplitude
  re-solve diagnostic.
- Future official DESI or Euclid releases are monitor events, not hourly work until verified data exist.

## Unchanged Status

No canon, verdict, claim-status, public-posture, paper, or external-action move is made here. The theta
dark-energy verdict remains OPEN at the existing recorded grade and scope. The recommended action is daily
steward reconciliation of the stale `DE-AMP-DIAGNOSTIC` pointer, not a public status update.

## Next Work

After steward reconciliation, hourly Progress should return to the protected `RECOVERY-CERTIFICATION`
lane, starting with `RECOVERY-CONTRACT`, unless a valid portfolio switch signal appears first. The strongest
reserve alternative remains `PROOF-STABLE-KERNELS`, but it should not outrank the North Star merely because
it is easier to finish.
