---
artifact_type: exploration
status: exploration
created: 2026-07-13
wave: 46
title: "H46C -- Wave 45 blocker B1 discharged: GU's OWN CMB-calibrated amplitude via the acoustic scale theta_star. The result reverses the expected direction: theta_star's weak h-sensitivity (dln theta*/dln h ~ 0.19) amplifies GU's percent-level late-time H(z) deformation into a -5.4% calibrated H0 (63.75 km/s/Mpc), so GU's own CMB amplitude OVERSHOOTS the BAO-preferred amplitude by +5.7 sigma_A. Three-way table: dAIC = +21.58 (Planck-fixed A) / +35.78 (GU's own theta_star calibration) / -3.17 (amplitude freed, now shown to have no CMB-consistent realization). With per-f0 CMB calibration the BAO-preferred f0 is the LCDM limit f0 -> 0 (3-sigma-equivalent bound f0 < ~0.03); omega_m h^2 profiled for BOTH models under the Planck prior leaves profiled dAIC = +16.03. Verdict: the Wave 45 f0 inconsistency is FALSIFICATION-HARDENED and the 'competitive as a distance model' rescue DISSOLVES against GU."
grade: "computation + statistics (tests/wave46/H46C_theta_star_cmb_calibration.py, deterministic, exit 0, 20/20; LCDM positive controls reproduce Planck theta_star and recover h = 0.6736). Exploration grade; M^2 = 8 H0^2 stays reconstruction-grade (OQ2 open); canon verdict OPEN unchanged; DARK-ENERGY-05 scope correction applied per the claim-status consistency runbook."
depends_on:
  - tests/wave46/H46C_theta_star_cmb_calibration.py
  - tests/wave45/H46B_referee_grade_desi_verification.py
  - tests/wave29/H46_de_raw_bao_likelihood.py
  - tests/wave25/H44_de_backreacted_background.py
  - explorations/wave45/H46B-referee-grade-desi-verification-2026-07-13.md
  - canon/theta-field-flrw-dark-energy-eos.md
scripts:
  - tests/wave46/H46C_theta_star_cmb_calibration.py
---

# Wave 46 -- H46C: the theta_star re-solve of GU's own CMB-calibrated amplitude (B1)

## Object

Wave 45 (H46B) cleared the DESI DR2 digit gate and left ONE named decisive blocker before
the dark-energy distance-model result could be paper-scaffolded: **B1 -- compute GU's own
CMB-calibrated amplitude** by imposing the Planck acoustic angular scale theta_star on
GU's own H(z), instead of arguing the Planck amplitude onto GU via the fixed-Om fairness
argument. The freed-amplitude "competitive on shape" reading (dAIC = -3.17) rested
entirely on that argument. This wave executes the computation. Five personas run inline,
then synthesis.

Reproduction: `python -u tests/wave46/H46C_theta_star_cmb_calibration.py`
(deterministic, exit 0, 20/20 PASS).

**Headline: the fairness argument, once replaced by the computation it stood in for,
fails in GU's disfavor.** GU's own CMB calibration does not deliver the amplitude the
BAO data prefer; it overshoots it by 5.7 sigma, and every rescue direction Wave 45
catalogued closes.

---

## Persona 1 -- CMB cosmologist: the calibration itself

**What Planck actually pins.** The acoustic angular scale
theta_star = r_star / D_M(z_star), measured essentially model-independently:
100 theta_star = 1.04110 +/- 0.00031 (a 0.03% measurement). Primary source: arXiv
1807.06209 Table 2, base-LCDM TT,TE,EE+lowE+lensing column -- the SAME column as every
Planck digit already verified in Wave 45. Three new digits extracted from the PDF this
wave (retrieval 2026-07-13, direct text extraction): r_star = 144.43 +/- 0.26 Mpc,
z_star = 1089.92 +/- 0.25, 100 theta_star = 1.04110 +/- 0.00031 (abstract cross-check
1.0411 +/- 0.0003). Note: the figure 1.04109 sometimes quoted is the no-lensing
TT,TE,EE+lowE column (the paper's Eq. 9); the difference is 0.03 sigma and irrelevant
at the sensitivity of anything below.

**How the constraint is imposed on a non-LCDM late-time H(z), honestly.** GU's theta
field turns on below z_start = 30 (slow-roll attractor IC); above it the field is frozen
(w = -1) and its density is checked to be < 1e-3 of matter at z_start (measured:
3.4e-5). So the model does not touch pre-recombination physics, and the standard
late-time-model procedure applies:

- r_star, z_star, r_drag, z_drag: FIXED at Planck values (they are pre-recombination
  integrals over omega_b h^2, omega_m h^2, N_eff, none of which GU's theta touches).
- omega_m h^2 = 0.1430: FIXED (CMB-pinned); the calibration unknown is h, with the
  fractional Om = omega_m h^2 / h^2 floating.
- Solve theta_star(h; model) = theta_star(Planck) for h. The solved h is the model's
  own CMB-calibrated H0; its BAO amplitude is A = (c/H0)/r_drag.

**Every approximation, named** (A1-A6 in the test header): additive radiation keeping
E(0) = 1 exactly (error O(9e-5) in today's budget); the 0.06 eV neutrino treated as
matter (~0.1% in D_M(z_star), SHARED by both pipelines); pipeline systematics cancelled
by ratio-correcting against the LCDM control; frozen theta density above z_start
(exactly continuous at z_start by construction); central values for the shared 0.18%
r_star/r_drag scale with a +/-0.2% amplitude sensitivity band on the verdict row; and
the (omega_m h^2)^(-0.25) sound-horizon rescaling in the profiled scan.

**Positive controls.** PC1: the LCDM pipeline at the Planck point reproduces
100 theta_star = 1.04134 vs 1.04110 (+2.3e-4 fractional, inside the named A1+A2 budget;
grid-doubling shifts < 1e-6). PC2: inverting the calibration for LCDM recovers
h = 0.67280 vs 0.6736 (-0.12%, the shared systematic that the ratio correction divides
out).

**The result and its mechanism.** At the Planck h, GU (f0 = 0.125) misses the measured
angle by +44 sigma. theta_star is famously weakly h-sensitive at fixed omega_m h^2
(this pipeline measures dln theta_star / dln h = 0.194), so rematching the 0.03% angle
against GU's ~1% D_M(z_star) deficit (extra matter-like theta density in the past,
<w> = 0 below z_osc ~ 1.85) requires Delta ln h ~ -1%/0.19: the calibration lands at
**H0_GU = 63.75 km/s/Mpc** (Om drifts to 0.352), i.e. **A_GU(CMB) = 31.97, +5.66%
above the Planck/LCDM amplitude 30.26**. The Wave 45 expectation "shift < 1%" was
wrong; the weak lever arm is exactly why theta_star anchors w0waCDM fits. Side note:
the shift is AWAY from local H0 ~ 73, worsening the Hubble-tension direction for GU;
not used as a chi^2 input here.

**The branch that keeps GU's source Om = 0.315 instead**: at h = 0.6375 it would need
omega_m h^2 = 0.128, which is ~13 sigma below Planck's 0.1430 +/- 0.0011. That branch
abandons CMB compatibility outright; it is a rejection of the CMB, not a calibration.

## Persona 2 -- statistician: the three-way table, with consistent k

AIC = chi^2 + 2k on the official DESI DR2 13-dim BAO Gaussian likelihood (digits
verified in Wave 45); dAIC = AIC_GU - AIC_LCDM; |dAIC| < 4 not decisive, > 10 decisive.
Rows 1 and 3 reproduce H46/H46B to < 0.05 as hard assertions.

| row | amplitude treatment | k (GU, LCDM) | chi^2_GU | chi^2_LCDM | dAIC |
|---|---|---|---|---|---|
| 1 | CMB-fixed Planck amplitude on both | 0, 0 | 52.26 | 30.68 | **+21.58** |
| 2 | EACH model's OWN theta_star calibration (NEW, the B1 row) | 0, 0 | 66.46 | 30.68 | **+35.78** |
| 3 | amplitude freed on both (shape only) | 1, 1 | 10.99 | 14.15 | **-3.17** |
| 4 | f0 refit on BAO, per-f0 CMB calibration (envelope) | 1, 0 | 31.88 | 30.68 | **+3.20** |

Findings:

1. **Row 2 is the honest replacement of the Wave 45 fairness argument, and it is WORSE
   for GU than row 1.** LCDM's theta_star calibration is the Planck point itself (PC2),
   so its row-2 chi^2 equals row 1. GU's own calibration gives A = 31.97, but the
   BAO-preferred amplitude for GU's calibrated shape is A* = 31.47 (sigma_A = 0.087):
   the calibration OVERSHOOTS by +5.7 sigma_A, hard-asserted in the test. Under the
   +/-0.2% shared-scale band (A5) the row-2 chi^2 stays in [58.6, 75.4]: decisive
   either way.
2. **Row 3 is now exposed as unrealizable.** The freed-amplitude shape win required
   A ~ 30.8-31.5 depending on shape; GU's own CMB calibration supplies 31.97. "GU is
   competitive on shape" is a true statement about a shape family with a free amplitude
   that the model, once CMB-calibrated, does not possess.
3. **Row 4 kills the f0 ~ 0.05 rescue.** With each f0 given its own theta_star
   calibration (a genuine joint BAO+theta_star fit, k = 1), chi^2(f0) is monotone
   increasing over the scan (hard assertion): the preferred value is the LCDM limit
   f0 -> 0, dAIC -> +2 (pure parameter penalty). The 3-sigma-equivalent crossing is
   **f0 < ~0.027**: the theta component is an upper limit, not a detection. The Wave 45
   "BAO prefers f0 ~ 0.05" was an artifact of holding A at the Planck value.
4. **No double counting.** theta_star enters ONLY through the amplitude; no CMB chi^2
   term is added to the BAO likelihood in any row.
5. **The omega_m h^2 escape hatch is closed with the correct statistics.** A naive scan
   shows the f0 = 0.125 exclusion weakening to dchi^2 ~ +5 at omega_m h^2 2 sigma low;
   but that ignores the Planck prior penalty AND that LCDM profiles the same nuisance
   (the known Planck-DESI amplitude tension relaxes at low omega_m h^2). Profiling
   total(n) = chi^2_BAO(n) + n^2 for BOTH models (equal k): GU minimum 33.36 at
   n = -3.5 sigma; LCDM minimum 17.33 at n = -2.0 sigma; **profiled dAIC = +16.03**,
   still decisive, both minima interior to the scan.

## Persona 3 -- dark-energy theorist: gates kept visible

- **M^2 = 8 H0^2 remains reconstruction-grade (OQ2 open).** Nothing here promotes it.
  This wave's calibration was run at M^2 = 8 only. The mechanism that drives the result
  (an oscillating theta mode has <w> = 0, so its density grows ~ a^-3 into the past,
  shrinking D_M(z_star)) is generic for every admissible M^2 above the BF-type bound,
  so the DIRECTION of the calibrated shift is band-generic; the MAGNITUDES quoted are
  M^2 = 8 numbers. An M^2-band scan of the calibration is the obvious cheap hardening
  step and is listed as an honest limit, not assumed.
- **f0 is a fit parameter, not a GU prediction (H42 preregistration).** What died this
  wave is not "GU's prediction" but the last CMB-consistent region of the one free
  amplitude: the family survives only as f0 < ~0.03, i.e. as a component too small to
  be the dark-energy story it was introduced to be. The DeWitt-Lambda (w = -1) part of
  the sector is indistinguishable from LCDM and untouched.
- **What would rescue the family** (named, per the constructive-obstruction protocol):
  a mechanism that modifies pre-recombination physics to shrink r_star by ~1% (GU-theta
  has none: the field is frozen above z = 30 by its own slow-roll IC), or a source
  derivation forcing f0 < 0.03 from the start (which would concede the DESI-facing
  content and return the sector to "LCDM-mimic").

## Persona 4 -- hostile referee: strongest attacks, faced

1. **"Fixing r_drag/r_star while changing late-time H(z) is illegitimate."** The
   standard answer: the sound horizons are integrals of c_s/H over the PRE-recombination
   era; a model that only modifies z < 30 leaves them untouched, and this is precisely
   how DESI/Planck treat w0waCDM and other late-time extensions. Its limits: it fails
   for early dark energy, extra relativistic species, or varying-alpha models; the test
   asserts GU-theta is not in that class (frozen-theta/matter ratio 3.4e-5 at z = 30).
   The (omega_m h^2)^(-0.25) rescaling used in the profiled scan is an approximation,
   named A6; it affects only the profiled row, whose margin (+16) dwarfs the scaling
   error.
2. **"You chose the calibration that kills the model."** No: this calibration is the
   one Wave 45's own honest-limits section demanded (H46 honest limit 2, B1), specified
   BEFORE its outcome was known, with the opposite expectation recorded ("expected
   shift < 1%"). Executing a pre-named test that then fails the model is the discipline
   working, not comparison-shopping.
3. **"Percent-level D_M deformation forcing a 6% H0 shift smells like a bug."** The
   lever arm dln theta_star/dln h = 0.194 is measured inside the test on the LCDM
   control; the f0 -> 0 limit of the GU calibration reproduces the LCDM calibration to
   7e-9; the direction (extra past DE -> smaller D_M -> lower calibrated h) is asserted.
   The amplification is real and is the standard reason theta_star is powerful against
   late-time modifications.
4. **"Does any framing bury the CPL falsification?"** The opposite now holds. The CPL
   falsification (H43/H44, ~3.2 sigma, robust) was the headline with a surviving
   scoped caveat ("but not independently excluded as a distance model"). This wave
   removes most of the caveat: the distance-level escape existed only while the
   amplitude went uncalibrated. The paper framing (below) leads with the falsification
   and reports the dissolution of its own strongest counter-reading.
5. **What would still worry me** (kept): SNe are not in the likelihood (BAO+theta_star
   only; adding SNe can only hurt a model whose calibrated H0 is 63.75); the M^2-band
   calibration scan is unexecuted; the profiled scan treats the Planck prior as
   Gaussian in omega_m h^2 alone rather than using the full CMB likelihood. None of
   these plausibly flips a +16-to-+36 margin, but they bound the claim's grade:
   exploration, not verified.

## Persona 5 -- honesty auditor: reconciliation and corrections

- **Canon verdict OPEN: unchanged.** No verdict label moves. The falsified object is
  scoped: the theta-sector DE family AS A CMB-CONSISTENTLY-CALIBRATED DISTANCE MODEL,
  at exploration grade, at M^2 = 8. Not "GU is falsified"; the source-action bottleneck
  and the located-not-forced spine are untouched.
- **A Wave 45 expectation is corrected on the record.** H46B wrote "Expected shift
  < 1%" for this calibration. Measured: -5.4% in h. The error had a direction: it made
  the fairness argument look safer than it was. Recorded here and in the correction
  note; the Wave 45 exploration is historical prose and is not rewritten (runbook rule).
- **DARK-ENERGY-05 applied** (claim-status consistency runbook: "historical prose that
  could be read as the current claim"). The DARK-ENERGY-04 language "raw-distance
  comparison ... MARGINAL ... shape-competitive once amplitude marginalized" is now
  stale as an unscoped statement: the shape-competitive reading has no CMB-consistent
  realization, and the raw-BAO comparison under the model's own CMB calibration is
  EXCLUDED for f0 >= ~0.03 and prefers the LCDM limit. Annotation added to
  `canon/theta-field-flrw-dark-energy-eos.md` with matching rows in
  `RESEARCH-STATUS.md` and `CANON.md`. Verdict label stays OPEN; no promotion.
- **Verdict does not exceed computation.** Every number above is a test assertion or a
  test print; the strongest claim made is exploration-grade and carries its M^2 = 8 and
  BAO+theta_star-only scope explicitly.

---

## Synthesis and verdict

**B1: DISCHARGED (computed, with positive controls).** GU's own CMB-calibrated
amplitude exists and is A_GU = 31.97 (+5.66% vs Planck; H0_GU = 63.75, Om = 0.352 at
canonical f0 = 0.125), obtained by imposing 100 theta_star = 1.04110 on GU's own H(z)
with early physics fixed.

**The three-way answer to the B1 question.** CMB-fixed: dAIC = +21.58. GU-CMB-
calibrated (the new, correct row): dAIC = +35.78. Amplitude-freed: dAIC = -3.17, now
demoted from "the fair comparison pending B1" to "a shape statement with no
CMB-consistent realization". With omega_m h^2 profiled for both models under the Planck
prior, the calibrated comparison still gives dAIC = +16.03.

**f0 dual-observable inconsistency: FALSIFICATION-HARDENED, and the rescue side
DISSOLVES against GU.** Under per-f0 CMB calibration the BAO-preferred f0 is the LCDM
limit f0 -> 0 (bound f0 < ~0.027 at 3-sigma-equivalent); the CPL-tuned f0 = 0.125 is
excluded at dchi^2 = +35.8. There is no longer a two-way tension between two preferred
f0 values; there is a CPL-tuned point excluded on the raw likelihood and a raw
likelihood that wants the theta component absent. The Wave 45 sentence "competitive,
not decisive" applied to a comparison that no longer exists once the model is
CMB-calibrated.

**Distance-level status of the sector** (supersedes the H46 MARGINAL reading, at
exploration grade, M^2 = 8): falsified as a CPL fit (unchanged, H43/H44); EXCLUDED as a
CMB-consistently-calibrated distance model on the raw DESI DR2 BAO likelihood for all
f0 >= ~0.03; surviving only as an undetected component with f0 < ~0.03 riding on a
DeWitt-Lambda that mimics LCDM.

**Paper-readiness (Wave 45 B1/B2):** B1 discharged; B2 (falsification-first structure,
f0 finding in the abstract) is now the NATURAL structure, since the positive leg
dissolved. Scaffolded at `papers/drafts/de-cpl-proxy-vs-raw-bao-likelihood/` (draft
skeleton + VERIFICATION map). NOTE: the Wave 45 text said "papers/candidates/", but
`papers/candidates/README.md` gates that folder on Joe explicitly stating publish
intent; the scaffold therefore enters at `papers/drafts/` and promotion is Joe-gated.

## Honest limits

1. Calibration executed at M^2 = 8 only; the mechanism is band-generic but the numbers
   are not band-scanned. Cheap follow-up.
2. BAO + theta_star only; no SNe term (adding SNe at H0 = 63.75 can only worsen GU).
3. The profiled omega_m h^2 scan approximates the Planck prior as an independent
   Gaussian and rescales sound horizons by (omega_m h^2)^(-0.25).
4. A1-A5 pipeline approximations are shared between models and ratio-corrected; the
   residual second-order systematic is far below the +16-to-+36 margins.
5. M^2 = 8 H0^2 stays reconstruction-grade (OQ2 open); every positive-shape statement
   in the sector still inherits that grade.

## RE-RANK signal

**Dark-energy sector: MARGINAL -> EXCLUDED-AT-CMB-CALIBRATION (exploration grade,
M^2 = 8).** The CPL falsification headline is unchanged; what changed is the caveat
under it: the raw-distance escape closed when the model was made to pay its own CMB
calibration. Next single objects for the sector: (i) the M^2-band calibration scan;
(ii) the paper draft build-out from the scaffold.

---

*Filed 2026-07-13. Wave 46 (H46C). Reproduced:
`python -u tests/wave46/H46C_theta_star_cmb_calibration.py` (exit 0, 20/20).
Personas run inline (CMB cosmologist, statistician, dark-energy theorist, hostile
referee, honesty auditor). Primary-source digits fetched read-only with retrieval dates
recorded; fetched content treated as data; no external action taken.*
