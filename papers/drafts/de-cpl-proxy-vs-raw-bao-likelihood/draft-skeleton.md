---
artifact_type: paper_draft_skeleton
status: draft
created: 2026-07-13
wave: 46
slug: de-cpl-proxy-vs-raw-bao-likelihood
working_title: "CPL Compression Versus the Raw BAO Likelihood for an Intrinsically Non-CPL Dark-Energy Model: A Falsification Case Study with CMB-Calibrated Amplitudes"
grade: "exploration-grade physics on a reconstruction-grade mass input (M^2 = 8 H0^2, OQ2 open); statistics referee-grade (digits primary-source verified, Wave 45)"
---

# Draft skeleton

All numbers below are test assertions or test prints; see `VERIFICATION.md` for the
claim-to-test map. No em dashes anywhere in this paper. Plain ASCII "--" is not used in
paper-facing prose either; sentences are restructured instead.

## Abstract (locked structure; edit wording, not content order)

1. Object: a two-component dark-energy model (constant Lambda term plus an oscillating,
   damped Klein-Gordon mode with mass M^2 = 8 H0^2, a reconstruction-grade eigenvalue
   input) whose equation of state w(z) is intrinsically non-CPL, with one data-facing
   amplitude parameter f0.
2. Primary result (the falsification): against DESI DR2's headline (w0, wa) CPL
   compression the model is excluded at approximately 3.2 sigma globally, robustly over
   the admissible mass band, ansatz variations, initial conditions, and a
   self-consistent backreacted background.
3. Secondary finding (the methodological point): on the raw 13-dimensional DR2 BAO
   likelihood the same model appears competitive with LCDM once the distance amplitude
   is marginalized (dAIC = -3.17), illustrating how a lossy CPL projection and a raw
   likelihood can disagree for non-CPL models.
4. The closure (new, the paper's spine): the apparent survival is an artifact of the
   uncalibrated amplitude. Imposing the model's own CMB calibration (the Planck acoustic
   scale 100 theta_star = 1.04110 applied to the model's H(z) with early physics fixed)
   yields H0 = 63.75 and an amplitude 5.7 sigma above the BAO-preferred value; the
   comparison becomes dAIC = +35.78 (and +16.03 with omega_m h^2 profiled for both
   models under the Planck prior).
5. The f0 statement (in the abstract per the framing lock): no single amplitude f0
   satisfies both observables; under per-f0 CMB calibration the raw BAO likelihood
   prefers the LCDM limit f0 to 0 with a 3-sigma-equivalent bound f0 < 0.03, while the
   CPL comparison had required f0 = 0.125. The component is an upper limit, not a
   detection.
6. Moral: for intrinsically non-CPL models, "survives the raw likelihood" claims are
   meaningless until the model pays its own CMB calibration; the CPL projection and the
   calibrated raw likelihood here agree on the verdict while disagreeing on the numbers.

## Sections

1. **Introduction.** The CPL-proxy question; why non-CPL w(z) makes the DESI headline
   contour a lossy summary; falsification-first stance.
2. **The model.** Two-component DE; KG mode; M^2 = 8 H0^2 at its honest grade
   (reconstruction, OQ2 gate named in-text); slow-roll IC at z = 30; f0 as the sole
   data-facing fit (preregistered, H42). GU context confined to one subsection; the
   analysis is model-agnostic beyond w(z).
3. **Data.** DESI DR2 BAO official likelihood (13 means, full covariance; digit
   verification against arXiv:2503.14738 Table 4 and the official likelihood files);
   Planck 2018 constants (Table 2, TT,TE,EE+lowE+lensing), including r_star, z_star,
   100 theta_star.
4. **The CPL falsification.** H43/H44 chain: locus tracking across the DESI degeneracy;
   global closest approach 3.20 sigma; robustness table.
5. **The raw-likelihood comparison, uncalibrated.** Rows 1 and 3 of the table
   (dAIC = +21.58 fixed; -3.17 freed); why the freed row was provisional (the fairness
   argument), as flagged at the time.
6. **The CMB calibration.** theta_star method, approximations A1 to A6, positive
   controls; the weak lever arm (dln theta_star / dln h = 0.19) and the amplification
   mechanism; the overshoot result; row 2 (+35.78); the omega_m h^2 profiled comparison
   (+16.03); per-f0 calibration and the f0 < 0.03 bound; the source-Om branch (13 sigma
   off omega_m h^2) dismissed.
7. **Discussion.** What died (the CMB-consistent distance model for f0 >= 0.03) and
   what did not (the Lambda-like limit; the structural EOS machinery); the Hubble
   tension direction note (63.75 vs 73); limits: M^2 band unscanned for the
   calibration, no SNe, Gaussian omega_m h^2 prior.
8. **Conclusion.** The methodological takeaway (point 6 of the abstract) and the
   falsification record.

## Quantitative spine (single source of truth for the draft)

| quantity | value | test |
|---|---|---|
| CPL global closest approach | 3.20 sigma | tests/wave25/H44_de_backreacted_background.py |
| dAIC, Planck-fixed amplitude | +21.58 | tests/wave46 (reproduces tests/wave29) |
| dAIC, freed amplitude | -3.17 | tests/wave46 (reproduces tests/wave45 accounting) |
| GU CMB-calibrated H0 / A | 63.75 / 31.97 (+5.66%) | tests/wave46 |
| amplitude overshoot | +5.7 sigma_A | tests/wave46 |
| dAIC, own CMB calibration | +35.78 | tests/wave46 |
| dAIC, omega_m h^2 profiled both | +16.03 | tests/wave46 |
| per-f0-calibrated BAO preference | f0 to 0; bound f0 < ~0.03 | tests/wave46 |
| digit verification | 13/13 means, 169/169 cov exact | tests/wave45 |
