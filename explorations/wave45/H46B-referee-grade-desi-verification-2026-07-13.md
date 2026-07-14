---
artifact_type: exploration
status: exploration
created: 2026-07-13
wave: 45
title: "H46B -- referee-grade follow-through on the dark-energy distance-model result: the DESI DR2 digits are now VERIFIED against the primary source (arXiv:2503.14738 Table 4 + the official likelihood files; arXiv:1807.06209 Table 2), the H46 'competitive-to-better than LCDM once amplitude is freed' claim is re-derived with an explicit AIC metric (dAIC = -3.17 with amplitude freed for both models: competitive, NOT decisive), and the framing is hardened against the p-hacking reading: the CPL falsification (H43/H44, ~3.2 sigma robust) stays the headline; the distance-model viability is scoped, degeneracy-dependent, and internally strained by the f0 split (CPL wants 0.125, BAO wants ~0.05). Verdict: digit gate CLEARED; paper-candidate NOT YET (two named blockers)."
grade: "verification + statistics audit (tests/wave45/H46B_referee_grade_desi_verification.py, deterministic, exit 0, 33/33). No new physics; no canon verdict change (OPEN stays OPEN); a stale-prose correction (DARK-ENERGY-04 annotation) is applied per the claim-status consistency runbook."
depends_on:
  - tests/wave45/H46B_referee_grade_desi_verification.py
  - tests/wave29/H46_de_raw_bao_likelihood.py
  - tests/wave25/H44_de_backreacted_background.py
  - tests/wave20/H43_de_shape_falsifier.py
  - tests/wave19/H42_f0_prereg.py
  - tests/wave1/H3_desi_verified_and_intersection.py
  - explorations/wave29/H46-de-raw-bao-likelihood-2026-07-11.md
  - explorations/wave25/H44-de-backreacted-background-2026-07-11.md
  - explorations/wave20/H43-de-shape-falsifier-2026-07-11.md
  - canon/theta-field-flrw-dark-energy-eos.md
scripts:
  - tests/wave45/H46B_referee_grade_desi_verification.py
---

# Wave 45 -- H46B: referee-grade verification of the dark-energy distance-model result

## Object

H46 (Wave 29) left the dark-energy sector at MARGINAL: GU's theta-sector dark energy is
FALSIFIED as a (w0,wa) CPL fit against DESI DR2 (H43/H44, global closest ~3.2 sigma, robust
to root system, ansatz, IC, and backreaction), but the raw backreacted H(z) is NOT
independently excluded by the actual DESI DR2 BAO likelihood, and is competitive-to-better
than LCDM once the overall distance amplitude is freed. A JoeOps governance gate held all
DESI-facing numbers at NOT-publication-ready until the digits were verified against the
primary source. This wave clears (or fails) that gate and stress-tests the statistics and
the framing. Method: five personas run inline, then synthesis.

Reproduction: `python -u tests/wave45/H46B_referee_grade_desi_verification.py`
(deterministic, exit 0, 33/33 PASS; re-fetched primary-source digits embedded verbatim with
retrieval dates).

---

## Persona 1 -- observational cosmologist (BAO/DESI): the digit verification

Primary sources fetched read-only 2026-07-13 (all instruction-like web content treated as
untrusted data):

- arXiv:2503.14738v2 (DESI DR2 Results II: BAO), digits extracted from the arXiv HTML
  render by direct text extraction, not a summarizer.
- The official DESI DR2 BAO Gaussian likelihood files
  `desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt` / `_cov.txt` at
  `github.com/CobayaSampler/bao_data` (the exact likelihood inputs for the paper).
- arXiv:1807.06209 (Planck 2018 parameters), Table 2 base-LCDM TT,TE,EE+lowE+lensing.

**Table-number correction to the gate language.** The JoeOps card said "Table 3". In
arXiv:2503.14738 the BAO distance table is **Table 4** ("Constraints on the BAO scaling
parameters and distance ratios at effective redshifts z_eff"); Table 3 is the
tracer/redshift-bin sample-statistics table. The repo cited Table IV throughout; the repo
citation was right and the card's "Table 3" was the imprecise one.

### Verified-vs-repo comparison, per number

Repo = the arrays embedded in `tests/wave29/H46_de_raw_bao_likelihood.py`.

| # | tracer, z, quantity | likelihood file (re-fetched) | repo H46 | paper Table 4 | match |
|---|---|---|---|---|---|
| 1 | BGS 0.295 DV/rd | 7.94167639 | 7.94167639 | 7.942 +/- 0.075 | EXACT / rounds |
| 2 | LRG1 0.510 DM/rd | 13.58758434 | 13.58758434 | 13.588 +/- 0.167 | EXACT / rounds |
| 3 | LRG1 0.510 DH/rd | 21.86294686 | 21.86294686 | 21.863 +/- 0.425 | EXACT / rounds |
| 4 | LRG2 0.706 DM/rd | 17.35069094 | 17.35069094 | 17.351 +/- 0.177 | EXACT / rounds |
| 5 | LRG2 0.706 DH/rd | 19.45534918 | 19.45534918 | 19.455 +/- 0.330 | EXACT / rounds |
| 6 | LRG3+ELG1 0.934 DM/rd | 21.57563956 | 21.57563956 | 21.576 +/- 0.152 | EXACT / rounds |
| 7 | LRG3+ELG1 0.934 DH/rd | 17.64149464 | 17.64149464 | 17.641 +/- 0.193 | EXACT / rounds |
| 8 | ELG2 1.321 DM/rd | 27.60085612 | 27.60085612 | 27.601 +/- 0.318 | EXACT / rounds |
| 9 | ELG2 1.321 DH/rd | 14.17602155 | 14.17602155 | 14.176 +/- 0.221 | EXACT / rounds |
| 10 | QSO 1.484 DM/rd | 30.51190063 | 30.51190063 | 30.512 +/- 0.760 | EXACT / rounds |
| 11 | QSO 1.484 DH/rd | 12.81699964 | 12.81699964 | 12.817 +/- 0.516 | EXACT / rounds |
| 12 | Lya 2.330 DH/rd | 8.631545674846294 | 8.631545674846294 | 8.632 +/- 0.101 | EXACT / rounds |
| 13 | Lya 2.330 DM/rd | 38.988973961958784 | 38.988973961958784 | 38.988 +/- 0.531 | EXACT / quirk |

- **Mean vector: 13/13 EXACT** match between the repo arrays and the re-fetched official
  likelihood file, to every printed digit.
- **Covariance: 169/169 EXACT** match (all six per-tracer blocks, including the
  D_M-D_H anticorrelation off-diagonals).
- **Row ordering verified**, including the Lya quirk (the file orders DH before DM).
- **One last-digit rounding quirk, in the paper not the repo:** the file's Lya D_M
  38.98897 rounds to 38.989 while the paper prints 38.988. Every other value rounds
  exactly. Sub-0.001, physically irrelevant, recorded for completeness.
- **Covariance-diagonal sigmas vs paper printed errors:** cov sigmas are systematically
  equal-or-larger, ratio 1.0006 to 1.0644 (largest: LRG3+ELG1 D_M, 0.1618 vs 0.152). This
  is expected: the likelihood covariance carries systematic terms; the likelihood file is
  the authoritative chi^2 input. H46's honest-limits section already stated exactly this.
- **Per-tracer correlations** from the cov file vs the paper's r_M,H: differences 0.0004
  to 0.069 (largest LRG3+ELG1), consistent with sys-inflated diagonals diluting r.
- **Planck prior digits** used by H46 (H0 = 67.36 +/- 0.54, Omega_m = 0.3153 +/- 0.0073,
  r_drag = 147.09 +/- 0.26, omega_m h^2 = 0.1430 +/- 0.0011): all verified verbatim
  against the 1807.06209 Table 2 column.
- **CPL contour digits** used by H43/H3 (DESI+CMB+DESY5: w0 = -0.752 +/- 0.057,
  wa = -0.86 +0.23/-0.20): verified verbatim against the Section VII displayed equation.
  Also verified: DESI+CMB (-0.42 +/- 0.21, -1.75 +/- 0.58), +Pantheon+ (-0.838 +/- 0.055,
  -0.62 +0.22/-0.19), +Union3 (-0.667 +/- 0.088, -1.09 +0.31/-0.27). The w0-wa correlation
  rho = -0.8 is NOT published by DESI; the repo declares it as an assumption and scans
  rho in (-0.9, -0.8, -0.7) in tests/wave1. Declared, not fabricated: confirmed.

### Which likelihood did each repo claim actually use?

- H3 / H42 / H43 / H44 (the FALSIFICATION chain): the **(w0,wa) CPL posterior summary**,
  as a 2D Gaussian with verified marginals and scanned correlation. This is DESI's
  headline projection, a lossy 2-parameter compression.
- H46 (the MARGINAL distance-level result): the **raw 13-dimensional Gaussian BAO
  likelihood** (official mean + full covariance). This is the actual DR2 BAO likelihood.
- The two are DIFFERENT observables, and every repo claim correctly identifies which one
  it used. No claim was found that quotes the raw likelihood while actually using the
  CPL proxy, or vice versa.

**Digit gate verdict: CLEARED.** No repo digit disagrees with the primary source.

## Persona 2 -- statistician: is "competitive-to-better than LCDM" sound?

Re-derived (not re-asserted) in the wave45 test, importing the H46 model verbatim.
Metric: AIC = chi^2 + 2k with explicit parameter counts, plus absolute goodness-of-fit.

| configuration | k (GU, LCDM) | chi^2_GU | chi^2_LCDM | dAIC (GU-LCDM) | GOF p (GU, LCDM) |
|---|---|---|---|---|---|
| CMB-fixed amplitude, canonical f0 | 0, 0 | 52.26 (dof 13) | 30.68 (dof 13) | **+21.58** | 1.2e-06, 0.0038 |
| amplitude freed for BOTH | 1, 1 | 10.99 (dof 12) | 14.15 (dof 12) | **-3.17** | 0.530, 0.291 |
| f0 freed at fixed A (envelope) | 1, 0 | 12.28 (f0 ~ 0.05) | 30.68 | **-16.40** | envelope only |

Statistician's findings:

1. **The claim is sound but must be stated with its exact scope.** With the amplitude
   freed for both models (the like-for-like comparison, same k), GU's shape fits the DR2
   BAO data mildly better than LCDM's: dAIC = -3.17. Under the conventional reading,
   |dAIC| < 4 is below the positive-evidence line. So the defensible sentence is
   "competitive, with a statistically non-decisive edge", not "better than LCDM". Both
   models are acceptable fits in absolute terms (GOF p = 0.53 and 0.29).
2. **The amplitude-freeing is statistically legitimate but physically costly.** Analytic
   marginalization over a single linear amplitude with a flat prior is exact (all three
   BAO observables are linear in A), and comparing shapes is a standard move. But GU's
   own CMB calibration (source Omega_m = 0.315 + Planck omega_m h^2) PINS the amplitude;
   freeing A means suspending part of GU's own predictive content. The preferred
   A* = 30.81 sits ~1.8% above the CMB value 30.26, i.e. GU absorbs the known
   Planck-vs-DESI-DR2 amplitude tension into A and then wins slightly on shape.
3. **The +21.58 at the disciplined point is real and must be co-reported.** At the
   CMB-fixed amplitude with canonical f0 = 0.125, GU is strongly disfavored
   (dAIC = +21.58); note even LCDM is a poor absolute fit there (p = 0.0038, the known
   ~1% Planck-DESI amplitude tension), so +21.58 is GU's increment on top of a shared
   tension.
4. **The free-f0 -16.40 is an envelope, not a result.** Adopting f0 ~ 0.05 would be
   tuning to the BAO data, and it contradicts the CPL-tuned f0 = 0.125. The
   internal-inconsistency guard is now a hard test assertion: the BAO-preferred f0 and
   the CPL-preferred f0 differ by a factor >= 2. No single f0 satisfies both observables.
   This strain is a finding, not a nuisance, and any writeup must carry it.
5. **The "~4.6 sigma" and "~3.2 sigma" figures are different animals.** 3.2 sigma is a
   Mahalanobis distance of GU's CPL projection from the DESY5 contour center; 4.6 sigma
   is sqrt(21.58) read as a 1-dof-equivalent delta-chi^2; DESI's own 2.8-4.2 sigma is the
   w0waCDM-vs-LCDM preference. The wave45 test prints an explicit do-not-conflate note.

## Persona 3 -- dark-energy theorist: what GU actually predicts, and the gates

What the theta sector predicts, at its honest grade:

- **Shape, not amplitude.** The prediction is a two-component dark energy: a constant
  DeWitt-Lambda (w = -1) plus an oscillating-damped Klein-Gordon theta mode with
  **M^2 = 8 H0^2** (equivalently M_KK = 2 sqrt(2) H0), the ground eigenvalue
  lambda_{N,1} = (9/2)^2 - (7/2)^2 of the normal Laplacian on the GL(4,R)/O(3,1) fiber
  with the BC_1 (7,1) restricted-root system, at R_s = c/H0. Since M_KK exceeds the
  Breitenlohner-Freedman-type bound 3H0/2, the mode oscillates and damps; the resulting
  w(z) is **non-monotone and intrinsically non-CPL** (shallow peak near z ~ 0.23), which
  is exactly why the CPL projection and the raw likelihood can disagree.
- **What is NOT predicted:** the amplitude f0 (equivalently B_i). H42 preregistered this:
  f0 is GU's sole data-facing fit, not source-derivable today. Canonical f0 = 0.125 was
  itself tuned to the DESI CPL point. Hence "the GU prediction" at the distance level is
  only as sharp as an unfixed one-parameter family.
- **The OQ2 gate sits under M^2 = 8.** The eigenvalue is reconstruction-grade
  (rc3-delta-n-spectrum-gl4r, rc3-root-multiplicity-bc1; the A_3-vs-BC_1 root-system
  question and the CAS Iwasawa check F6 are open). The FALSIFICATION side does not hinge
  on it (H43/H44 scanned the entire admissible band M^2 in [1,25] and the miss is
  everywhere >= 3.2 sigma). The POSITIVE side does: any statement of the form "GU's
  specific shape fits the DR2 distances" inherits reconstruction grade through M^2 = 8
  and cannot be promoted past it until OQ2 closes. No promotion past reconstruction
  grade is made here, and none is possible by this wave's construction.

## Persona 4 -- hostile referee: the p-hacking attack, faced directly

The attack: "You fit a model, got excluded at 3.2 sigma, then went shopping for a
comparison in which it survives, and now you headline 'viable as a distance model'.
That is garden-of-forking-paths behavior."

The honest reply, which the artifacts already support and this wave hardens into test
assertions:

1. **The falsification is the headline and stays the headline.** H43/H44's CPL-locus
   falsification is robust (every admissible M^2, 1-component ansatz, IC variation,
   self-consistent backreaction; global closest 3.20 sigma) and H46 explicitly does NOT
   overturn it. The wave45 test asserts the headline discipline textually (check C1) so
   it cannot silently drift.
2. **H46 was not comparison-shopping; it was the pre-registered honest limit.** H43 and
   H44 each named, at the moment of the kill, the same single untested freedom: the CPL
   Mahalanobis is a lossy projection of a non-CPL w(z), and the raw-distance level is
   amplitude-degenerate (DARK-ENERGY-03, recorded 2026-06-30, BEFORE the falsification
   chain ran). Testing the named limit is follow-through, not forking.
3. **The order of results is falsification first, viability second.** The sequence is
   kill (H43), harden the kill (H44), then check the one named residual freedom (H46).
   A p-hacker's sequence is the reverse.
4. **The viability claim is scoped to the point of fragility, in its own verdict.** H46's
   verdict string is MARGINAL (degeneracy-fragile), not VIABLE: excluded at the
   disciplined point, competitive only along the amplitude/f0 degeneracy directions,
   and the two degeneracy escapes are mutually inconsistent (f0 = 0.125 vs ~0.05).
5. **What would still worry me as a referee** (kept, not rebutted): the shape win
   (dAIC = -3.17) is small, obtained after freeing an amplitude GU's own calibration
   fixes, and the theta_star re-solve of GU's amplitude (H46 honest limit 2) has not
   been executed. Until that is computed, "competitive on shape" is conditional on a
   fixed-Om argument for the amplitude fairness. This is blocker B1 below.

**Publishable point, phrased referee-proof:** DESI's headline (w0,wa) CPL compression
excludes GU's theta-sector w(z) at ~3.2 sigma robustly; the same model's raw H(z) is not
independently excluded by the actual DR2 BAO likelihood, and matches or slightly beats
LCDM in shape once the distance amplitude is marginalized. The interesting object is the
gap between a CPL-proxy verdict and a raw-likelihood verdict for intrinsically non-CPL
models, with GU as the worked example. Stated this way, the CPL kill is load-bearing and
the distance-level statement is a scoped methodological finding, not a rescue.

## Persona 5 -- honesty auditor: reconciliation with canon and corrections

- **Canon verdict OPEN: consistent, stays OPEN.** `canon/theta-field-flrw-dark-energy-eos.md`
  carries verdict OPEN with corrections DARK-ENERGY-01/02/03. Nothing in this wave
  changes a verdict label. The wave45 test asserts `verdict: OPEN` is still present.
- **One stale-prose finding (flagged, then corrected, per the runbook).** The canon
  file's DARK-ENERGY-03 rationale says the model is "neither a clean confirmation nor a
  clean falsification vs DESI". Written 2026-06-30, that was correct. After waves 20/25
  (2026-07-12) it is stale AS UNSCOPED PROSE: the CPL-projection comparison IS now
  falsified at exploration grade (robust ~3.2 sigma), while the raw-distance comparison
  remains degenerate/MARGINAL. A future agent reading only canon would under-read the
  state of the sector. Per the claim-status consistency runbook this is exactly the
  "historical prose that could be read as the current claim" trigger. Correction applied
  in this wave: a DARK-ENERGY-04 annotation on the canon file scoping the 03 language
  (CPL-projection comparison: falsified at exploration grade per H43/H44; raw-distance
  comparison: MARGINAL per H46; digits verified per this wave), with matching rows in
  `RESEARCH-STATUS.md` and `CANON.md`. Verdict label unchanged (OPEN). No promotion.
- **Corrections history coherent.** DARK-ENERGY-01 (divergence-free downgrade), 02
  (process-milestone re-elevation reversed), 03 (sign red-flag retracted as a
  local-derivative artifact + hardcoded d ln rho/dz = 3 bug) form a consistent chain;
  H43/H44/H46/H46B all build on the post-03 state. The w0 = -0.826 "match" language in
  canon is already correctly labeled a fit.
- **No other contradictions found.** The H46 exploration's data-quality note (cov-file
  sigma vs paper rounded error, LRG3+ELG1 0.162 vs 0.152) is confirmed by this wave's
  extraction, including its explanation.

---

## Synthesis and verdict

**Digit gate: CLEARED.** Every DESI DR2 number in the repo's dark-energy chain matches
the primary source: 13/13 likelihood means exact, 169/169 covariance entries exact,
Table 4 rounding consistent (one sub-0.001 quirk in the paper's own rounding), Planck
prior digits exact, CPL contour digits exact, and the one unpublished quantity (rho) is
a declared, scanned assumption. The publication hold based on unverified digits can be
lifted; the numbers themselves are publication-grade.

**The honest likelihood comparison, in one paragraph.** At the disciplined point
(canonical f0 = 0.125, CMB-fixed amplitude) GU is excluded on the raw DR2 BAO likelihood
(dAIC = +21.58 vs LCDM). Freed-amplitude shape comparison: GU mildly better
(dAIC = -3.17, below the decisive line; both fits acceptable). Free-f0 envelope:
dAIC = -16.40, envelope only, and internally inconsistent with the CPL-tuned f0. The
correct public sentence is: "falsified as a CPL fit; not independently excluded, and
competitive in shape, as a distance model; the two rescues of the distance level are
mutually inconsistent in f0."

**Paper-candidate ready? NOT YET.** The distinction CPL-proxy-vs-raw-likelihood is a
genuine, now digit-verified, publishable point. Two named blockers before scaffolding
`papers/candidates/`:

- **B1 (physics, decisive):** execute the theta_star re-solve of GU's own CMB-calibrated
  amplitude (H46 honest limit 2): match the CMB acoustic scale with GU's own D_M(z*)
  including the z > 30 tail, instead of the fixed-Om Planck-amplitude argument. Expected
  shift < 1%, but the freed-amplitude shape claim (the paper's positive leg) currently
  rests on the fairness argument this computation would replace. A referee will ask for
  it; it is cheap relative to its load.
- **B2 (framing, structural):** the paper must be built with the CPL falsification as
  the primary result and the distance-level viability as the scoped secondary finding,
  with the f0 internal inconsistency stated in the abstract, not the discussion. If the
  draft cannot be structured that way, it should not exist.

When B1 is computed (either outcome) the candidate can be scaffolded; its natural slug
is `de-cpl-proxy-vs-raw-bao-likelihood`.

## Honest limits

1. The Table 4 extraction is from the arXiv v2 HTML render by direct text extraction;
   the likelihood files, not the rounded table, are what enter every chi^2 in the repo,
   and those are verified byte-for-byte.
2. This wave adds no new physics: the theta_star re-solve (B1) remains undone.
3. The AIC accounting treats the analytically marginalized amplitude as one fitted
   parameter for each model; a full Bayesian evidence with a declared amplitude prior
   would be the stronger version (expected to agree in direction at these dchi^2 sizes).
4. M^2 = 8 H0^2 remains reconstruction-grade (OQ2 open); the positive shape statement
   inherits that grade and is not promoted past it here.

## RE-RANK signal

**MARGINAL, unchanged, now referee-grade.** The DE sector's headline (CPL falsification
stands; distance level MARGINAL, degeneracy-fragile) is unchanged; what changed is its
grade: the digits are primary-source-verified, the statistics carry an explicit metric,
and the framing guards are executable test assertions. Next single object for the
sector: the theta_star amplitude re-solve (B1).

---

*Filed 2026-07-13. Wave 45 (H46B). Reproduced:
`python -u tests/wave45/H46B_referee_grade_desi_verification.py` (exit 0, 33/33).
Personas run inline (observational cosmologist, statistician, dark-energy theorist,
hostile referee, honesty auditor). Primary sources fetched read-only with retrieval
dates recorded; no external action taken.*
