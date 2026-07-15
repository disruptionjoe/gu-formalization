---
artifact_type: exploration
status: exploration (FALSIFICATION wave, NON-NAIVE; five personas inline, one worker, no sub-agents; deterministic test with positive controls first)
created: 2026-07-14
wave: W220
label: W220
hypothesis: "FALSIFICATION attack on GU's dark-energy leg vs the DESI DR2 DATA, NON-NAIVE mode: assume GU is correct and grant every unbuilt piece resolving as GU hopes, then find where GU is NEVERTHELESS wrong against data. The critical move is to SEPARATE the DERIVED CHARACTER (falsifiable) from the FITTED shape/epoch (W160 proved the crossing epoch is provably FREE, so the specific z of crossing cannot falsify). Pin the derived character precisely -- sign-changing / phantom-crossing, clock-coupled, O(1)~H^2 -- then confront the DESI DR2 w0-wa constraints (arXiv:2503.14738)."
title: "W220 -- FALSIFY the derived dark-energy CHARACTER against DESI DR2. VERDICT: SURVIVES-WITH-TENSION. The four-axis derived character (A1 dynamical / A2 sign-changing phantom-crossing / A3 clock-coupled z=O(1) / A4 amplitude O(1) under the F1 ceiling) is NOT excluded by DESI DR2 -- it is CORROBORATED: the character-negating LCDM null is disfavored at 2.8-4.2 sigma, DESI's OWN best fit is a phantom crossing at z=0.405 in GU's phantom->quintessence direction with rho_DE non-monotonic, and the amplitude ratio wa/(w0+1)=-3.468 stays (barely, margin +0.032) above the canon F1 kill-line -3.5. The pre-declared FAILURE CONDITION does not fire on any of its four clauses. The 3.47 sigma (closest over f0) / 4.19 sigma (canonical f0=0.125) miss of GU's specific CPL locus, and W129's dchi^2>=+33.5 distance-model exclusion, attach to the FITTED shape (provably free per W160) and are therefore a STANDING MONITOR, not a falsification. Sharpest live tripwire: DR3/Euclid pushing the ratio past -3.5 would fire FC-d and falsify axis A4."
grade: "computation + statistics (tests/W220_falsify_dark_energy_vs_desi.py, deterministic seed 20260714, exit 0, 15/15; positive controls FIRST reproduce H43's (w0,wa)=(-0.7677,-0.2733), joint 4.19 sigma, closest-over-f0 3.47 sigma, DESI's own w=-1 crossing at z=0.4052, and the W160 stationary free-epoch uniformity). Exploration grade; canon verdict on theta-field-flrw-dark-energy-eos.md stays OPEN and UNCHANGED; no canon/verdict/status flip; no promotion; f0/B_i remain fits; M^2=8 stays reconstruction-grade."
depends_on:
  - canon/theta-field-flrw-dark-energy-eos.md
  - explorations/W160-debit3-forced-binary-2026-07-14.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/W144-desi-fitted-issuance-function-2026-07-14.md
  - tests/wave20/H43_de_shape_falsifier.py
  - tests/wave45/H46B_referee_grade_desi_verification.py
scripts:
  - tests/W220_falsify_dark_energy_vs_desi.py
---

# W220 -- FALSIFY the derived dark-energy CHARACTER against DESI DR2

Test: `tests/W220_falsify_dark_energy_vs_desi.py` (15/15, exit 0). Deterministic (seed
20260714). No network. Positive controls run first and reproduce the load-bearing numbers
from H43 (`tests/wave20`), H46B (`tests/wave45`), and W160.

Five personas ran inline in one worker, sequentially (no sub-agents): (1) cosmology /
dark-energy specialist, (2) DESI-data / w0-wa-contour specialist, (3) FLRW / theta-field-EOS
specialist, (4) prediction-vs-fit separator (enforces the W160 free-epoch caveat), (5)
ruthless skeptic.

## 0. Method and the pre-declared failure condition

NON-NAIVE falsification. ASSUME GU is correct and GRANT every unbuilt piece resolving as GU
hopes (the source-action bottleneck, the matter->connection bridge, f0/B_i). "Unbuilt /
undetermined" is a GAP, not a falsification. Only a WRONG DEFINITE prediction counts.

The load-bearing separation (W160): the frontier fluctuation two-point function is STATIONARY
(its correlation depends only on the log-count separation, not the absolute epoch), so pinning
the crossing at a specific z requires a non-stationary rank-1 bump that provably breaks the
everpresent amplitude law. Deriving the amplitude and deriving the epoch are MUTUALLY
EXCLUSIVE. Therefore the crossing EPOCH and the specific (w0, wa) / f0 / B_i are FITTED
boundary data and CANNOT falsify GU. Only the DERIVED CHARACTER can.

**GU's derived DE character, pinned to four falsifiable axes** (canon
`theta-field-flrw-dark-energy-eos.md` + W144/W154/W158/W160):

- **A1 DYNAMICAL.** w is not identically -1; the everpresent Lambda fluctuates with amplitude
  ~ 1/sqrt(N) ~ (l_p/R_H)^2 ~ H^2, an O(1) fraction of rho_crit.
- **A2 SIGN-CHANGING.** The issuance Q = d rho_V / d ln a changes sign +->- (issuance then
  withdrawal): rho_DE rises then falls (interior maximum), i.e. w crosses -1 with direction
  PHANTOM-past -> QUINTESSENCE-now. The sign is FORCED by the q=5 Krein-indefinite grading
  (W158), not fitted.
- **A3 CLOCK-COUPLED.** The fluctuation correlation length is ~ one e-fold ~ one Hubble time
  (W160), so the crossing, IF present, sits at z = O(1).
- **A4 AMPLITUDE O(1).** |1+w| is O(1)-scale and bounded above: canon failure condition F1
  forbids wa/(w0+1) < -3.5 (that would require B_i > 3 M_Pl, structurally unphysical in GU).

**PRE-DECLARED FAILURE CONDITION.** GU is FALSIFIED on the dark-energy leg IF the DESI data
CONTRADICT the derived character beyond ~3-5 sigma -- specifically if any of these fire:
- FC-a: data FAVOR w == -1 (pure Lambda); the character-negating LCDM null is preferred -> kills A1/A2.
- FC-b: data force a MONOTONIC rho_DE (no interior maximum, no phantom crossing) -> kills A2.
- FC-c: data force the crossing at z NOT O(1) (z >> 1 or z << 1) -> kills A3.
- FC-d: data force wa/(w0+1) < -3.5 at 2 sigma (B_i > 3 M_Pl) -> kills A4.
If NONE fire, the character SURVIVES and the specific-shape miss is a MONITOR on the free shape.

## 1. Persona 1 -- cosmology / dark-energy specialist: what character DESI actually prefers

DESI DR2 (arXiv:2503.14738, Sec. VII, w0waCDM; H3/H46B-verified digits): DESI+CMB+DESY5 gives
w0 = -0.752 +/- 0.057, wa = -0.86 (+0.23 / -0.20), correlation rho(w0,wa) = -0.8. The
preference for dynamical DE (w0waCDM) OVER LCDM is 3.1 sigma (DESI+CMB alone) and 2.8-4.2
sigma with SNe (Pantheon+ 2.8, Union3 3.8, DESY5 4.2).

The physically important fact: DESI does not merely allow dynamical DE, it prefers a SPECIFIC
CHARACTER. With w0 > -1 and wa < 0, the best-fit w(a) = w0 + wa(1-a) crosses w = -1 at
a* = 1 + (1+w0)/wa = 0.7116, i.e. **z = 0.405** -- phantom (w < -1) for z > 0.405,
quintessence (w > -1) for z < 0.405. The CPL dark-energy density rho_DE(a) is consequently
NON-MONOTONIC with an interior MAXIMUM at z = 0.405 (verified in the test, PC2/PC2b). That is
exactly a SIGN-CHANGING issuance Q = d rho_V/d ln a, +->-, in the PHANTOM-past -> QUINTESSENCE-now
direction. DESI's own preferred model IS GU's derived character, axis for axis.

## 2. Persona 2 -- DESI-data / w0-wa-contour specialist: the four-axis confrontation

Running each derived axis against the DR2 contour (test block CHARACTER CONFRONTATION):

- **A1 DYNAMICAL.** The character-negating null (pure Lambda, w = -1) is DISFAVORED by DESI at
  2.8-4.2 sigma across SNe compilations. FC-a does not fire; the data point AWAY from the
  character-killing region.
- **A2 SIGN-CHANGING.** DESI best fit: w0 = -0.752 (> -1) AND wa = -0.86 (< 0) -> a phantom
  crossing exists at z = 0.405 in (0, 2), rho_DE non-monotonic, direction phantom->quintessence.
  FC-b does not fire.
- **A3 CLOCK-COUPLED.** The DESI crossing epoch z = 0.405 is O(1) (in [0, 2], ~ one Hubble
  time back), consistent with GU's ~one-e-fold correlation length. FC-c does not fire.
- **A4 AMPLITUDE.** DESI central ratio wa/(w0+1) = -0.86/0.248 = **-3.468**, which is NOT below
  the F1 kill-line -3.5 (margin +0.032). FC-d does not fire. (The naive marginal 2-sigma
  most-negative excursion is more negative, but rho = -0.8 anti-correlates w0 and wa so that
  the joint 2-sigma contour does not reach -3.5 at the central-consistent point; the honest,
  reportable statistic is the central ratio, sitting just inside the ceiling.)

No FC clause fires. The derived character is NOT excluded by DESI DR2 in any anti-GU direction.

## 3. Persona 3 -- FLRW / theta-field-EOS specialist: which route supplies the character

Two internal GU routes bear on the character, and they must not be conflated:

- **Route A (canonical scalar; canon Results 1-4, H43).** The theta zero-mode as a canonical
  scalar gives w_DE = (-1 + f wB)/(1+f) with f >= 0 and wB in [-1, 1], hence w_DE >= -1 ALWAYS.
  It CANNOT truly cross -1; its CPL FIT lands at (w0, wa) = (-0.768, -0.273) -- right sign on
  both, but wa far too small in magnitude -- and misses the DESI ellipse (Section 4). Route A's
  character is quintessence-like, NOT phantom-crossing.
- **Route B (everpresent-Lambda + q=5 Krein-indefinite; W144/W154/W158/W160).** The indefinite
  Krein metric (negative-norm directions) permits a genuine SIGN-CHANGING issuance -- rho_V
  rising (effective phantom) then falling -- with the SIGN forced by the q = 5 grading. This is
  the phantom-crossing character the prompt names as "the derived DE character," and the one
  that matches DESI.

The falsification target is Route B's character (the sign-changing / clock-coupled / O(1)~H^2
statement). GRANTING GU's hopes, that character is what confronts DESI, and it survives. Route
A's inability to cross -1 is a fact about the canonical-scalar realization's SHAPE, folded into
the standing tension (Section 4), not a separate character kill -- because the amplitude/shape
in Route A is precisely the fitted, W160-free part.

## 4. Persona 4 -- prediction-vs-fit separator: what is prediction, what is fit

This is the wave's crux and the reason the verdict is SURVIVES-WITH-TENSION rather than either
a clean survive or a kill.

**PREDICTION (derived, falsifiable, tested above):** A1 dynamical, A2 sign-change DIRECTION
(phantom->quintessence), A3 crossing at z = O(1), A4 amplitude O(1) under the F1 ceiling. All
four are consistent with -- indeed corroborated by -- DESI DR2. The failure condition does not
fire.

**FIT (provably free per W160, CANNOT falsify):** the specific crossing epoch (DESI's z = 0.405
is a fitted boundary datum -- W160 proved the phase is free), the specific (w0, wa) point, and
the amplitude f0 / B_i. GU's canonical-scalar CPL locus misses the DESI ellipse at **3.47 sigma**
(closest over f0) / **4.19 sigma** (canonical f0 = 0.125, reproduced in PC3b/PC3c), and W129
showed the CMB-calibrated theta distance model is excluded at dchi^2 >= +33.5 at DESI-signal
amplitudes band-wide. Under the strict method, a miss of a FREE quantity is not a WRONG DEFINITE
prediction -- it is a monitor. The 3.47-4.19 sigma tension is real and reported honestly; it is
not a falsification of the character.

The honest crux, stated plainly: the SURVIVES verdict is CONDITIONAL on the W160 free-epoch
obstruction holding (the epoch/shape is fitted, not predicted) and on taking Route B's
sign-changing character as "the" derived character. Reject the W160 escape -- insist the
canonical-scalar FLRW-KG route make a definite shape prediction -- and the leg is
FALSIFIED-ON-SHAPE at 3.47-4.19 sigma (Route A never crosses -1 and its locus tracks across the
DESI degeneracy). W160 is itself exploration-grade. So the load-bearing assumption is named, not
hidden.

## 5. Persona 5 -- ruthless skeptic: is the surviving character even falsifiable?

The strongest attack is not that DESI kills the character but that the character is too GENERIC
to be a real prediction: "sign-changing DE at z = O(1) with O(1) amplitude" is almost exactly
the CPL-with-wa<0 family DESI reports, and W144 literally FITS the DESI issuance function -- so
is this retrofit dressed as prediction?

Two honest responses, and one concession:
- The character IS falsifiable in principle: a null result (Planck-consistent LCDM, w = -1, no
  evolution, monotone rho_DE) WOULD have killed A1/A2, and pre-DR2 that was the default
  expectation. The character-negating region is exactly what DESI now disfavors at 2.8-4.2
  sigma. So the prediction took a real risk and the data landed on the GU side.
- The character's content is derived from GU structure, not the DESI number: the O(1)~H^2
  amplitude is the everpresent 1/sqrt(N) law (ported Sorkin), the +->- sign is the q=5 Krein
  pin (W158), the z=O(1) scale is the log-count correlation length (W160). The DESI number
  enters only in the fitted epoch/amplitude, which W160 shows is free anyway.
- Concession (recorded): because the falsifiable character is weak/generic, its SURVIVAL is a
  weak confirmation, not a strong one. The sharp, potentially-killing content is the specific
  shape, and that shape MISSES at 3.47-4.19 sigma. The leg lives on the W160 free-epoch
  separation; if that separation is wrong, the leg is falsified. This is the opposite of
  rooting for GU: the honest read is "survives on a technicality that is itself only
  exploration-grade, with a real 3.5-4 sigma shape tension standing."

**LIVE TRIPWIRE.** The DESI DR2 ratio -3.468 sits 0.032 from the F1 kill-line -3.5. If DR3 or
Euclid push wa more negative or w0 toward -1 so the joint 2-sigma ratio crosses -3.5, FC-d
fires and axis A4 (the amplitude ceiling) is FALSIFIED -- GU would then need B_i > 3 M_Pl. The
W220 test is written so that re-running it against updated (w0, wa) digits flips to exit 1 the
moment any FC clause fires; it is a standing falsification monitor, not a one-shot.

## 6. VERDICT

**SURVIVES-WITH-TENSION.**

- **Character (prediction) -- SURVIVES.** DESI DR2 does not exclude and in fact corroborates
  the sign-changing / clock-coupled / O(1)~H^2 character on all four axes. The character-negating
  LCDM null is disfavored at 2.8-4.2 sigma; DESI's own best fit is a phantom crossing at z=0.405
  in GU's phantom->quintessence direction with non-monotonic rho_DE; the amplitude ratio -3.468
  stays above the F1 kill-line -3.5. The pre-declared FAILURE CONDITION does not fire.
- **Shape/epoch (fit, provably free per W160) -- MISSES, as a MONITOR.** GU's specific CPL
  locus misses at 3.47 sigma (closest over f0) / 4.19 sigma (canonical f0), and W129's
  CMB-calibrated distance model is excluded at dchi^2 >= +33.5 at DESI-signal amplitudes. Per
  W160 this is a miss of a free boundary datum -- a standing monitor, not a falsification.
- **Sigma summary.** Character not excluded (0 sigma against, up to 4.2 sigma FOR via the LCDM
  disfavour); shape tension 3.47-4.19 sigma (monitor); F1 margin +0.032 (live tripwire).

Explicitly: **prediction = the four character axes; fit = the crossing epoch, the (w0,wa)
point, and f0/B_i.** The verdict is conditional on the W160 free-epoch obstruction (named, not
hidden); reject it and the leg is FALSIFIED-ON-SHAPE at 3.47-4.19 sigma.

## 7. What this does NOT do (honest limits)

- Exploration grade throughout; conditional register. Nothing asserts GU, that the DESI wiggle
  is real (the DR3 bet is live), or that dark energy is everpresent-Lambda. The SURVIVES is a
  statement about the reverse-engineered character vs the data, not a claim GU predicts DESI.
- No canon / verdict / status movement. The canon verdict on `theta-field-flrw-dark-energy-eos.md`
  stays OPEN and unchanged; no promotion; f0/B_i remain fits; M^2 = 8 stays reconstruction-grade;
  OQ2 (which eigenvalue) stays open.
- The survival rests on two exploration-grade supports (the W160 free-epoch obstruction; the
  Route-B Krein sign-change as "the" character). Both are named. If either fails, the verdict is
  FALSIFIED-ON-SHAPE at 3.47-4.19 sigma.
- Single BAO dataset (DESI DR2); SNe enter only through the published w0waCDM compilations, not
  an independent GU likelihood; the shape tension uses the (w0,wa)-projection metric (the
  distance-metric degeneracy is the DARK-ENERGY-03/W129 story, cited not re-run).

*Filed 2026-07-14 by the W220 FALSIFICATION wave (NON-NAIVE). Five personas inline in one
worker (cosmology/DE specialist, DESI-contour specialist, FLRW/theta-EOS specialist,
prediction-vs-fit separator, ruthless skeptic); no sub-agents. Reproducible:
`python -u tests/W220_falsify_dark_energy_vs_desi.py` (15/15, exit 0; positive controls first).
Exploration grade; canon OPEN unchanged; VERDICT: SURVIVES-WITH-TENSION. Character not falsified
by DESI DR2; the 3.47-4.19 sigma tension is on the W160-free shape (a monitor); live tripwire:
ratio -3.468 vs F1 kill-line -3.5.*
