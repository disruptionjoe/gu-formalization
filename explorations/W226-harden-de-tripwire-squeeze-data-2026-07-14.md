---
artifact_type: exploration
status: exploration (FALSIFICATION monitor-hardening, NON-NAIVE; five personas inline, one worker, no sub-agents; deterministic test with positive controls first + a live-fire control)
created: 2026-07-14
wave: W226
label: W226
hypothesis: "HARDEN GU's dark-energy AMPLITUDE tripwire (canon failure mode F1) and SQUEEZE it against the strongest CURRENT combined data, NON-NAIVE. W220 left a live killer: the DESI DR2 ratio wa/(w0+1) = -3.468 sits +0.032 from the F1 kill-line -3.5. Two questions: (a) does the encoded tripwire check the RIGHT quantity and robustly auto-fire on updated (w0,wa) digits? (b) does a stronger CURRENT combination (DESI DR2 + CMB + SNe compilations) already cross -3.5? Separate the derived CHARACTER (amplitude axis A4, falsifiable) from the fitted shape/epoch (W160-provably FREE)."
title: "W226 -- HARDEN the DE amplitude tripwire + SQUEEZE current data. VERDICT: SURVIVES-WITH-TENSION at updated 2-sigma margin +1.11. The W220 tripwire had TWO fragilities, both fixed: (1) it tested the CENTRAL ratio, contradicting canon F1's explicit 'at 2-sigma', which would SPURIOUSLY FIRE (false GU-falsification) on the DESI+CMB+Pantheon+ row whose central ratio is already -3.83 (past -3.5) while its 2-sigma edge is only -2.20; (2) it hardcoded one BASE row (DESY5) instead of scanning all admissible combinations, and the ratio's pole at w0=-1 makes central-value tests unstable exactly where future data move. The hardened FC-d (tests/W226_de_tripwire.py) scans EVERY current combination, propagates the full rho=-0.8 correlation, and fires iff ANY 2-sigma least-negative edge < -3.5 (canon-F1 exact). SQUEEZE result: current central ratios span -3.02..-3.83 (Pantheon+ already past the line at central), but NO current combination excludes ratio>-3.5 at 2-sigma; the tightest 2-sigma edge is -2.39 (DESY5), a live falsification margin of +1.11. W220's '+0.032 margin' was a DESY5-central artifact and is superseded. Resolving release: DESI DR3 (full 5-yr, ~2027) / Euclid DR1 cosmology (~mid-2027)."
grade: "computation + statistics (tests/W226_de_tripwire.py, deterministic seed 20260714, exit 0, 11/11; positive controls FIRST reproduce the DESY5 central ratio -3.468/+0.032, the canon F1 line, the Pantheon+ central-vs-2-sigma-edge fragility, and a LIVE-FIRE control that fires FC-d on a tight synthetic DR3-like row -- the monitor is not vacuous). Exploration grade; canon verdict on theta-field-flrw-dark-energy-eos.md stays OPEN and UNCHANGED; no canon/verdict/status flip; no promotion; f0/B_i remain fits; the amplitude axis A4 is the only falsifiable content, the (w0,wa) point / shape / epoch remain W160-provably FREE."
depends_on:
  - canon/theta-field-flrw-dark-energy-eos.md
  - explorations/W220-falsify-dark-energy-vs-desi-2026-07-14.md
  - explorations/W160-debit3-forced-binary-2026-07-14.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - tests/W220_falsify_dark_energy_vs_desi.py
scripts:
  - tests/W226_de_tripwire.py
---

# W226 -- HARDEN the DE amplitude tripwire + SQUEEZE current data

Test: `tests/W226_de_tripwire.py` (11/11, exit 0). Deterministic (seed 20260714). No
network. Positive controls run first and include a LIVE-FIRE control that proves the
hardened tripwire actually fires (exit-1 path) on a tight synthetic DR3-like row.

Five personas ran inline in one worker, sequentially (no sub-agents): (1) dark-energy /
cosmology specialist, (2) DESI / data-combination specialist, (3) forecasting /
survey-timeline specialist, (4) prediction-vs-fit separator (enforces the W160 free-epoch
caveat), (5) ruthless skeptic.

## 0. What was inherited and the pre-declared failure condition

W220 found GU's DE character SURVIVES-WITH-TENSION and left the amplitude axis A4 as the
sharpest live killer: canon failure mode **F1** (`theta-field-flrw-dark-energy-eos.md`
line 196, verbatim): *"DESI DR2 or Euclid measures w_a/(w_0+1) < -3.5 at 2-sigma. This
requires B_i > 3 M_Pl, unphysical in GU."* W220 reported the DESI+CMB+DESY5 central ratio
-3.468 as sitting +0.032 above the -3.5 line.

The separation that governs everything (W160): the frontier fluctuation two-point function
is STATIONARY, so the crossing epoch and the specific `(w0, wa)` point / `f0` / `B_i` are
FITTED boundary data and cannot falsify GU. Only the DERIVED CHARACTER can. Axis A4 -- the
statement that `|1+w|` is O(1) but the amplitude is BOUNDED ABOVE by the F1 ceiling -- is
the falsifiable amplitude content. The ratio `wa/(w0+1)` is the observational proxy for the
`B_i` amplitude, and F1 is the ceiling.

**PRE-DECLARED FAILURE CONDITION (stated, then tested).** GU is FALSIFIED on the DE
amplitude axis A4 IFF a CURRENT admissible dataset EXCLUDES `wa/(w0+1) > -3.5` at 2-sigma
(its 2-sigma least-negative edge falls below -3.5), forcing `B_i > 3 M_Pl`; OR excludes the
derived character beyond ~5 sigma. SURVIVES-WITH-TENSION iff every current admissible
2-sigma edge stays above -3.5 -- report the updated margin and the resolving release. Only
the CHARACTER (A4 ceiling) counts; the fitted shape/epoch (W160-free) does NOT.

## 1. Persona 1 -- dark-energy / cosmology specialist: what quantity F1 actually tests

F1 names a specific measurable: `wa/(w0+1)` compared to -3.5, **at 2-sigma**. The phrase
"at 2-sigma" is load-bearing and was dropped in W220's encoding. A measurement establishes
`ratio < -3.5` "at 2-sigma" only if the *least-negative* (2-sigma, toward-zero) edge of the
measured ratio is still below -3.5 -- i.e. the data EXCLUDE `ratio > -3.5` at 95.4%. A
central value past -3.5 is NOT that condition; it is roughly a 1-sigma statement at best.

Physical note: `wa/(w0+1)` has a POLE at `w0 = -1`. For a phantom-crossing model (`w0 > -1`,
`wa < 0`) the ratio is finite, but as data push `w0 -> -1` the ratio diverges while carrying
almost no likelihood weight. Any central-value test is therefore unstable exactly in the
direction improved data will move. The correct statistic is the correlated 2-sigma edge.

## 2. Persona 2 -- DESI / data-combination specialist: the SQUEEZE (part b)

The strongest CURRENT combined constraints are DESI DR2 BAO + CMB (Planck/ACT) + a SNe
compilation. All four DESI DR2 w0waCDM rows (arXiv:2503.14738 Sec. VII; H3/H46B/W220-verified
digits, `rho(w0,wa) = -0.8`), with the central ratio, the central margin to -3.5, and the
2-sigma least-negative edge (correlated MC, seed 20260714):

| combination | pref (vs LCDM) | central ratio | central margin | 2-sigma least-neg edge | edge margin |
|---|---|---|---|---|---|
| DESI+CMB | 3.1 sigma | -3.017 | +0.483 | -1.75 | +1.75 |
| DESI+CMB+Pantheon+ | 2.8 sigma | **-3.827** | **-0.327** | -2.20 | +1.30 |
| DESI+CMB+Union3 | 3.8 sigma | -3.273 | +0.227 | -2.21 | +1.30 |
| DESI+CMB+DESY5 | 4.2 sigma | -3.468 | +0.032 | **-2.39** | **+1.11** |

The finding: the CENTRAL ratio of the most stringent current admissible combination,
**DESI+CMB+Pantheon+, is already -3.83 -- PAST the -3.5 kill-line** (central margin -0.33).
W220's headline "+0.032 margin" was an artifact of picking the DESY5 row; it does not
describe the current dataset as a whole. Pantheon+ has the SNe pulling `w0` closest to -1
(`w0 = -0.838`), which shrinks the denominator and inflates the ratio -- the pole effect
from Section 1, made concrete.

BUT at the level F1 actually requires (2-sigma), **no current combination excludes
`ratio > -3.5`.** Every 2-sigma least-negative edge sits at -1.75 .. -2.39, and for the
worst central case (Pantheon+) `P(ratio < -3.5)` is only 0.66 -- about 1 sigma, not the 2
sigma F1 demands. The tightest 2-sigma edge is DESY5's -2.39, a **live falsification margin
of +1.11**. FC-d does not fire on any current admissible combination.

## 3. Persona 3 -- forecasting / survey-timeline specialist: the resolving release (part c)

DESI DR2 is the 3-year dataset (public March 2025). DESI completed its planned 5-year survey
in spring 2026 and continues observing into 2028. The measurement that resolves this leg:

- **DESI DR3 / final (full 5-year BAO + full-shape), ~2027.** Roughly doubles the DR2
  statistical power on `(w0, wa)`. This is the primary resolver -- it tightens the `(w0, wa)`
  contour and drives the 2-sigma edge of the ratio toward -3.5. If DR3 keeps the central
  `(w0, wa)` near the DR2 phantom-crossing values while halving the errors, the 2-sigma edge
  moves from ~-2.4 toward -3.5 and FC-d could fire.
- **Euclid DR1 cosmology, ~mid-2027.** DR1-Foundation (imaging/spectra, no cosmology)
  releases Nov 2026; the full DR1 with LE3 cosmology products (weak lensing + galaxy
  clustering, percent-level `w0-wa`) follows ~mid-2027. An independent `(w0, wa)` constraint
  that either corroborates the phantom-crossing character or tightens the amplitude.

So the leg is resolved within ~12-24 months of this filing by DESI DR3 (~2027) and Euclid
DR1 cosmology (~mid-2027). The hardened tripwire is written to re-run against those digits
by adding one dict row.

## 4. Persona 4 -- prediction-vs-fit separator: what is falsifiable here

The amplitude CEILING (axis A4) is derived: F1 is a structural statement that `B_i` cannot
exceed ~3 `M_Pl` in GU, mapped onto `wa/(w0+1) < -3.5`. That ceiling is the falsifiable
content and the tripwire tests exactly it. What is NOT falsifiable, per W160: the specific
`(w0, wa)` point, the crossing epoch, and the `f0`/`B_i` VALUE inside the ceiling -- these
are fitted boundary data (the two-point function is stationary; deriving amplitude and epoch
are mutually exclusive). The 3.47-4.19 sigma shape miss from W220 and the W129
`dchi^2 >= +33.5` distance-model exclusion attach to that free shape and remain a MONITOR,
not a falsification. This wave changes none of that; it only sharpens the A4 ceiling test.

Crucially, the Pantheon+ central-crossing is a fact about the `(w0, wa)` POINT (free), read
through the ratio; it becomes a FALSIFICATION only if it holds at 2-sigma (the ceiling being
excluded), which it does not. The separation is what keeps the honest verdict from
overreacting to the -3.83 central number.

## 5. Persona 5 -- ruthless skeptic: is the hardening a cover for a near-miss?

The skeptic's charge: "you found a current dataset already past -3.5 at central value, then
redefined the test to 2-sigma so it doesn't count -- that is moving the goalposts to save
GU." Three responses, one concession:

- The 2-sigma level is CANON, not a W226 invention: F1 says "at 2-sigma" verbatim, written
  before this data. W220's central-only encoding was the deviation from canon; W226 restores
  the pre-registered threshold. The honest error ran the OTHER way -- W220's test would have
  spuriously FIRED (declared GU falsified) had its BASE been repointed to Pantheon+.
- The hardening is tested to fire: the LIVE-FIRE positive control (`PC-LIVE`) feeds a tight
  synthetic DR3-like row (`ratio ~ -4.3`, small errors) whose 2-sigma edge is -3.74, and
  FC-d fires. The tripwire is live, not vacuous.
- The squeeze made the tension WORSE, not better, and it is reported: the most stringent
  current admissible combination is already past the line at central value. GU is not
  comfortable here; it is one good DESI DR3 tightening (errors halved at the same central)
  from FC-d firing.
- Concession (recorded): the `wa/(w0+1)` proxy is pole-fragile and the "amplitude axis" is,
  as W220 conceded, a weak/generic prediction. Its survival is a weak confirmation. The
  sharp content remains the shape, which misses at 3.47-4.19 sigma (W220 monitor). The A4
  ceiling survives current data at 2-sigma; that is the whole of the claim.

## 6. VERDICT

**SURVIVES-WITH-TENSION at updated 2-sigma margin +1.11.**

- **Amplitude axis A4 (falsifiable ceiling) -- SURVIVES.** No current admissible combination
  (DESI DR2 + CMB + Pantheon+/Union3/DESY5) excludes `wa/(w0+1) > -3.5` at 2-sigma. The
  tightest current 2-sigma least-negative edge is -2.39 (DESY5), giving a live falsification
  margin of **+1.11**. The pre-declared FAILURE CONDITION does not fire.
- **Tension (monitor, central-value) -- WORSE than W220 reported.** The most stringent
  current admissible combination, DESI+CMB+Pantheon+, is already at central ratio **-3.827,
  past the -3.5 line** (central margin -0.33), at ~1 sigma (`P(ratio<-3.5)=0.66`). W220's
  "+0.032 margin" was a DESY5-central artifact and is superseded: the correct current figures
  are the 2-sigma margin +1.11 (firing test) and the worst central margin -0.33 (monitor).
- **Tripwire hardened.** FC-d now (i) tests the canon quantity (2-sigma least-negative edge,
  not central), fixing a bug that would have spuriously falsified GU on the Pantheon+ row;
  (ii) scans EVERY admissible combination, not one BASE; (iii) is pole-robust via full
  `rho=-0.8` correlated propagation; (iv) auto-extends -- add a DR3/Euclid row and it is
  covered. Verified live-firing.
- **Resolving release.** DESI DR3 / final (full 5-year, ~2027) and Euclid DR1 cosmology
  (~mid-2027) roughly double the `(w0, wa)` power and will push the 2-sigma edge toward -3.5.
  Re-run `tests/W226_de_tripwire.py` against those digits.

## 7. Optional (part d) -- an additional currently-checkable DE observable

Beyond `w0-wa`, GU's derived character (A2 sign-changing, A3 clock-coupled, A4 O(1)~H^2)
implies two further currently-checkable signatures. Neither falsifies now; both are logged as
candidate future tripwires, and both are amplitude/shape-contaminated (W160-free) EXCEPT for
their character-level content:

- **Growth-rate / structure (`f sigma8`).** A non-monotonic `rho_DE` with quintessence-now
  (`w0 > -1`) predicts a specific SIGN of the late-time growth deviation vs LCDM (mild growth
  enhancement as DE was more phantom-like in the recent past). DESI DR2 full-shape RSD +
  weak-lensing (`S8`) can check the SIGN, but the AMPLITUDE is `f0`-contaminated (free), so
  only the direction is character-level. Current `f sigma8` / `S8` data are consistent with
  the mild-deviation direction and do not exclude it -- not a current falsification.
- **Feature WIDTH (clock coupling, A3).** A3 predicts the DE transition has correlation
  width ~ one e-fold (`Delta ln a ~ 1`, one Hubble time). This is a CHARACTER prediction
  independent of epoch/amplitude: a reconstructed `w(z)` feature much NARROWER than one
  e-fold would falsify A3. DESI DR2 non-parametric `w(z)` reconstructions show an O(1)-e-fold
  feature, consistent with A3 -- no current falsification, but a sharp future tripwire once
  DR3/Euclid reconstruct the feature width.

These are recorded as analysis only (no fabricated reconstruction digits encoded); the hard,
tested tripwire remains the A4 amplitude ceiling.

## 8. What this does NOT do (honest limits)

- Exploration grade throughout. No canon / verdict / status movement: the verdict on
  `theta-field-flrw-dark-energy-eos.md` stays OPEN and unchanged; no promotion; `f0`/`B_i`
  remain fits; only the A4 ceiling is treated as falsifiable content.
- Single BAO dataset family (DESI DR2). SNe enter only through the published w0waCDM
  compilations, not an independent GU likelihood. The `rho(w0,wa) = -0.8` correlation is the
  declared DESI value; the MC edge uses a Gaussian approximation to the (mildly asymmetric)
  posterior -- adequate for a 2-sigma-edge tripwire, not a full-likelihood recomputation.
- The `wa/(w0+1)` proxy is pole-fragile near `w0=-1` (documented; the tripwire guards it by
  the correlated 2-sigma-edge statistic and an explicit `P(w0<-1) < 2.3%` check).
- Part (d)'s growth / feature-width observables are logged as analysis, not encoded tests.

*Filed 2026-07-14 by the W226 FALSIFICATION monitor-hardening wave (NON-NAIVE). Five personas
inline in one worker (dark-energy/cosmology specialist, DESI/data-combination specialist,
forecasting/survey-timeline specialist, prediction-vs-fit separator, ruthless skeptic); no
sub-agents. Reproducible: `python -u tests/W226_de_tripwire.py` (11/11, exit 0; positive
controls first, live-fire control included). Exploration grade; canon OPEN unchanged; VERDICT:
SURVIVES-WITH-TENSION at updated 2-sigma margin +1.11. Tripwire hardened to canon-F1 (2-sigma)
and auto-scanning; resolving release DESI DR3 (~2027) / Euclid DR1 cosmology (~mid-2027).*
