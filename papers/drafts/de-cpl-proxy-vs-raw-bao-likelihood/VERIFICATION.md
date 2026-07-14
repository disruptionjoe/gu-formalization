# VERIFICATION map -- de-cpl-proxy-vs-raw-bao-likelihood

Every quantitative claim in the draft ties to a deterministic Python test (exit 0).
Re-run order is bottom-up; each later test imports earlier machinery verbatim rather
than re-implementing it.

| # | claim | test (exit 0) | assertion type |
|---|---|---|---|
| 1 | DESI DR2 digits: 13/13 likelihood means and 169/169 covariance entries exact vs the official likelihood files; Table 4 and Planck Table 2 digits verbatim | `tests/wave45/H46B_referee_grade_desi_verification.py` (33/33) | hard PASS/FAIL |
| 2 | CPL falsification: global closest approach 3.20 sigma on the backreacted background; no admissible M^2 within 2 sigma | `tests/wave25/H44_de_backreacted_background.py` | hard PASS/FAIL |
| 3 | CPL falsification, fixed-LCDM background + full (M^2, f0) plane | `tests/wave20/H43_de_shape_falsifier.py` | hard PASS/FAIL |
| 4 | f0 preregistration (f0 is the sole data-facing fit) | `tests/wave19/H42_f0_prereg.py` | hard PASS/FAIL |
| 5 | Raw-likelihood rows: chi^2 = 52.26/30.68 fixed (dAIC +21.58); 10.99/14.15 freed (dAIC -3.17) | `tests/wave29/H46_de_raw_bao_likelihood.py`, re-asserted to <0.05 in `tests/wave46/H46C_theta_star_cmb_calibration.py` | hard PASS/FAIL |
| 6 | LCDM positive controls: pipeline reproduces 100 theta_star = 1.04110 to 2.3e-4 and recovers h = 0.6736 to 0.12% | `tests/wave46/H46C_theta_star_cmb_calibration.py` PC1/PC2 | hard PASS/FAIL |
| 7 | GU CMB calibration: H0 = 63.75, A = 31.97 (+5.66%), overshoot +5.7 sigma_A; direction and lever-arm (0.194) guards; f0->0 continuity to 7e-9 | `tests/wave46/H46C_theta_star_cmb_calibration.py` Q1/Q2 | hard PASS/FAIL |
| 8 | dAIC = +35.78 at GU's own calibration; +/-0.2% scale band stays decisive | `tests/wave46/H46C_theta_star_cmb_calibration.py` Q2 | hard PASS/FAIL + printed band |
| 9 | per-f0 CMB calibration: chi^2(f0) monotone increasing; f0 = 0.125 excluded (dchi^2 = +35.8); 3-sigma-equivalent bound f0 < ~0.027 | `tests/wave46/H46C_theta_star_cmb_calibration.py` Q3 | hard PASS/FAIL |
| 10 | omega_m h^2 profiled for BOTH models under the Planck prior: dAIC = +16.03, minima interior | `tests/wave46/H46C_theta_star_cmb_calibration.py` Q4 | hard PASS/FAIL |
| 11 | Frozen-theta early-physics check: rho_theta/rho_m at z = 30 is 3.4e-5 (late-time-only modification, r_star/r_drag fixing legitimate) | `tests/wave46/H46C_theta_star_cmb_calibration.py` Q1 | hard PASS/FAIL |

Grade ledger (must appear in the draft): M^2 = 8 H0^2 is reconstruction-grade (OQ2
open; `canon/theta-field-flrw-dark-energy-eos.md` corrections DARK-ENERGY-01..05);
all likelihood results are exploration-grade computations on that input; the digit
verification (row 1) is referee-grade. Known gaps carried into the draft's limits
section: M^2-band calibration scan unexecuted; no SNe term; Gaussian omega_m h^2 prior
approximation with (omega_m h^2)^(-0.25) sound-horizon rescaling.
