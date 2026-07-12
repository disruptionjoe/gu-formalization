# H46 -- DE raw-H(z) / BAO-likelihood test (Wave 29)

**Object.** The ONE dark-energy comparison the H43/H44 CPL falsification did not settle:
does the self-consistent theta-BACKREACTED GU H(z) (Wave 25, `H44_de_backreacted_background.py`)
fit the ACTUAL DESI DR2 BAO likelihood -- the real D_M/r_d, D_H/r_d, D_V/r_d measurements
and their published covariance -- rather than the lossy (w0,wa)-CPL projection DESI headlines?

**Test.** `tests/wave29/H46_de_raw_bao_likelihood.py` -- deterministic, exit 0, all checks PASS.
Imports `solve_backreacted` from H44 verbatim (identical physics; NOT re-implemented).

**Verdict: MARGINAL (degeneracy-fragile).** RE-RANK signal: **MARGINAL**.

---

## Q1 -- the actual data used (COMPUTED, cited)

The full DESI DR2 BAO Gaussian likelihood (13-dim data vector + 13x13 covariance), taken
VERBATIM from the official public likelihood files
`desi_gaussian_bao_ALL_GCcomb_mean.txt` / `_cov.txt` at
`github.com/CobayaSampler/bao_data` (`desi_bao_dr2/`) -- the inputs used for
**arXiv:2503.14738** ("DESI DR2 Results II: BAO", Table IV). Retrieved 2026-07-12.

| Tracer | z_eff | observable | value +/- sigma |
|---|---|---|---|
| BGS | 0.295 | D_V/r_d | 7.942 +/- 0.076 |
| LRG1 | 0.510 | D_M/r_d ; D_H/r_d | 13.588 +/- 0.168 ; 21.863 +/- 0.429 (r = -0.45) |
| LRG2 | 0.706 | D_M/r_d ; D_H/r_d | 17.351 +/- 0.180 ; 19.455 +/- 0.334 |
| LRG3+ELG1 | 0.934 | D_M/r_d ; D_H/r_d | 21.576 +/- 0.162 ; 17.641 +/- 0.201 |
| ELG2 | 1.321 | D_M/r_d ; D_H/r_d | 27.601 +/- 0.325 ; 14.176 +/- 0.225 |
| QSO | 1.484 | D_M/r_d ; D_H/r_d | 30.512 +/- 0.764 ; 12.817 +/- 0.518 |
| Lya | 2.330 | D_H/r_d ; D_M/r_d | 8.632 +/- 0.101 ; 38.989 +/- 0.532 |

The FULL covariance is used (block-diagonal per tracer, with the real D_M-D_H
anticorrelations -0.40..-0.50), not a diagonal approximation. Cross-checked against the
paper's Table IV rounded errors; the covariance file is the authoritative likelihood input.

**CMB prior (NOT DESI):** Planck 2018 base-LCDM (arXiv:1807.06209 Table 2):
Omega_m = 0.3153, H0 = 67.36 km/s/Mpc, r_drag = 147.09 Mpc, omega_m h^2 = 0.1430.
These set Omega_m (which COINCIDES with GU's source value 0.315) and the dimensionless BAO
amplitude A = (c/H0)/r_d = 30.258. Because GU's source Omega_m = 0.315 plus the CMB
omega_m h^2 pins h = 67.4, the "Planck amplitude" IS GU's own CMB-calibrated amplitude, not
an LCDM value imposed on GU. No DESI number enters the model.

## Q2 -- GU's BAO observables and chi^2 (COMPUTED)

GU predictions from the backreacted H(z), canonical M^2 = 8 (BC_1 ground), f0 = 0.125,
amplitude from CMB (fixed). dof = 13 (Omega_m and A both fixed by CMB; 0 fitted params).

| quantity | GU (backreacted, canonical) | flat LCDM (Om=0.315, same CMB A) |
|---|---|---|
| chi^2 | **52.26** | **30.68** |
| chi^2/dof | 4.02 | 2.36 |

- **delta-chi^2 (GU - LCDM) = +21.58** (~4.6 sigma, 1-dof-equivalent). ln(B_GU/LCDM) = -10.79.
- The largest single GU pull is D_H/r_d at z=0.934: -3.5 sigma. GU systematically
  UNDERSHOOTS the distances at the CMB-fixed amplitude on the D_M side while matching D_H;
  the net is a coherent miss.
- **LCDM itself fits poorly at the fixed Planck prior** (chi^2/dof = 2.36, the known
  Planck-vs-DESI-DR2 ~1% amplitude tension). The delta-chi^2 is the GU-vs-LCDM increment
  ON TOP of that shared tension.

### The two degeneracy directions (COMPUTED) -- why the verdict is MARGINAL, not EXCLUDED

- **Amplitude-marginalized (shape-only) chi^2** (analytic marginalization over A, flat prior;
  the DARK-ENERGY-03 degeneracy direction; dof = 12):
  chi^2_GU = **10.99** (A* = 30.81) vs chi^2_LCDM = **14.15** (A* = 29.92).
  **delta-chi^2 (A marg) = -3.17 -- GU fits the SHAPE as well as or BETTER than LCDM.**
- **Free-f0 envelope at fixed CMB A** (f0 is a genuinely free amplitude, per H42 -- not
  source-derivable): the canonical f0 = 0.125 OVERSHOOTS, but a smaller f0 ~ 0.05 gives
  chi^2 = 12.28, **delta vs LCDM = -18.40 -- better than LCDM.** (Reported as an envelope,
  NOT adopted: choosing f0 to fit BAO is forbidden tuning and is inconsistent with the
  CPL-tuned 0.125.)

So the exclusion appears at exactly ONE configuration -- canonical f0 AND the CMB-fixed
amplitude -- and evaporates the moment EITHER the overall amplitude OR f0 is freed. That is
the signature of the LCDM-amplitude degeneracy operating at the distance level.

## Q3 -- verdict

**MARGINAL (degeneracy-fragile).**
- At the disciplined point (canonical f0 = 0.125, CMB-fixed amplitude): **EXCLUDED**,
  delta-chi^2 = +21.58 vs LCDM (~4.6 sigma).
- Shape-marginalized: **competitive/better** (-3.17).
- Free f0 at fixed A: **competitive/better** (-18.40 at f0 ~ 0.05).

The raw-H(z) BAO test does **not** deliver an INDEPENDENT clean distance-level kill. It
CONFIRMS the DARK-ENERGY-03 amplitude degeneracy that H43 and H44 both flagged as their
honest limit: the raw non-CPL GU H(z) CAN mimic the DESI DR2 distances. What the BAO
likelihood excludes is the SPECIFIC CPL-tuned, CMB-calibrated point (f0 = 0.125 at the
Planck amplitude), not GU's H(z) SHAPE.

## Q4 -- adversarial / scope

- **f0 -> 0 bug guard:** two-part. (a) H^2(f0=1e-6) reduces to LCDM with max|dH2| = 3.5e-6
  (~machine, exact physics). (b) chi^2_GU - chi^2_LCDM -> 0 LINEARLY: |delta| = 9.95e-4 at
  f0=1e-6 and 9.95e-6 at f0=1e-8, ratio exactly 100.0. The small residual at f0=1e-6 is the
  genuine O(f0) theta density (near f0=0 the chi^2 slope is large and negative -- f0=0.02
  already gives delta ~ -14), NOT an integration artifact. Pipeline verified.
- **Full covariance:** the real 13x13 block-anticorrelated DESI covariance is used.
- **No tuning to DESI:** Omega_m and A come from the CMB (Planck) prior; f0 = 0.125 and
  M^2 = 8 come from the theta model. The f0 ~ 0.05 BAO-optimum is reported only as an
  envelope, never adopted.
- **CPL-vs-raw scope (explicit):** these are DISTINCT observables. DESI's headline (w0,wa)
  CPL contour still EXCLUDES GU's CPL projection (H43/H44, global closest ~3.2 sigma, robust
  to root-system M^2, ansatz, and backreaction). The raw BAO DISTANCES do NOT independently
  exclude GU -- so H43/H44 is NOT overturned (the CPL falsification stands) and NOT
  independently reproduced at the distance level (no second clean kill).

---

## COMPUTED vs ARGUED

**COMPUTED** (on the actual model + actual data):
- GU's D_M/r_d, D_H/r_d, D_V/r_d at all 13 DESI bins from the backreacted H(z).
- chi^2_GU = 52.26, chi^2_LCDM = 30.68, delta-chi^2 = +21.58 (fixed CMB amplitude, dof 13).
- Shape-marginalized chi^2_GU = 10.99 vs 14.15 (delta -3.17, dof 12).
- Free-f0 envelope; best chi^2 12.28 at f0 ~ 0.05.
- f0 -> 0 reduction to LCDM (H^2 machine-exact; chi^2 delta linear in f0).

**ARGUED:**
- That the CMB-fixed amplitude is fair to GU because GU's Om=0.315 + CMB omega_m h^2 pins
  h ~ 67.4 (so the amplitude is GU's own CMB calibration, not LCDM's imposed). This uses a
  fixed-Om argument; a full theta_star re-solve of GU's h with its own D_M(z*) would shift
  the amplitude by <1% and would not change EXCLUDED-at-canonical.
- The 1-dof-equivalent "~4.6 sigma" reading of delta-chi^2 = 21.58 (GU vs LCDM differ
  essentially by the one backreaction/amplitude direction).

## Honest limits (esp. data I could not source precisely)

1. **Data quality: HIGH.** The data vector and full covariance are the official public
   DESI DR2 BAO likelihood files (Cobaya `bao_data`), matching arXiv:2503.14738 Table IV.
   No proxy or invented number was used. The only sub-percent inconsistency is between the
   covariance-file diagonal and the paper's rounded published errors (e.g. LRG3+ELG1 D_M
   0.162 from cov vs 0.152 in Table IV); the covariance file is authoritative for the
   likelihood and is what enters chi^2.
2. **CMB amplitude vs full theta_star re-solve.** I fixed A from Planck (Om=0.315 + r_d) and
   argued this equals GU's own CMB calibration. A rigorous test would re-solve GU's h by
   matching the CMB acoustic scale theta_star with GU's OWN D_M(z*) (which needs the z>30
   matter/radiation tail, model-independent there). Expected shift < 1%; does not overturn
   the canonical-point exclusion, and does not touch the shape-marginalized result.
3. **f0 is free (H42).** GU has no source-first f0; canonical 0.125 was itself DESI-CPL-tuned.
   The distance data prefer a DIFFERENT f0 (~0.05) than the CPL contour (0.125) -- the two
   observables pull f0 apart, which is itself informative but means "the GU prediction" at
   the distance level is only as sharp as the (unfixed) f0.
4. **Systematics floor.** BAO reconstruction/HOD systematics are folded into the DESI
   covariance as published; no extra theory-systematic was added to GU.

## RE-RANK signal for the DE sector

**MARGINAL.** The dark-energy sector verdict is UNCHANGED in its headline and SHARPENED in
its scope:
- **CPL falsification stands** (H43/H44): GU's (w0,wa) projection is robustly excluded by
  DESI's headline CPL contour (~3.2 sigma, no rescue). H46 does not overturn this.
- **No second, independent distance-level kill.** The raw non-CPL GU H(z) is NOT
  independently excluded by the actual DESI DR2 BAO distances: it is EXCLUDED only at the
  precise CPL-tuned + CMB-calibrated point (delta-chi^2 +21.58), and is competitive-to-better
  than LCDM once the amplitude or f0 is freed (shape delta -3.17). This quantitatively
  CONFIRMS the DARK-ENERGY-03 amplitude degeneracy on the real likelihood.
- **Net:** GU dark energy is falsified as a CPL FIT but not as a distance MODEL. The DE
  sector is cornered (the same free f0 cannot satisfy both the CPL contour and the raw BAO
  distances), but the honest distance-level verdict is MARGINAL, not a full kill.
