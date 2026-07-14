---
artifact_type: exploration
status: exploration
created: 2026-07-13
hypothesis: H52
title: "H52 (wave 32) -- the alpha = 1/3 sub-mm exclusion boundary CITED: lambda_max(alpha=1/3) = 47.6 um (Lee 2020, via the published n=1 radion bound M* >= 7.1 TeV and the published fit lambda = 2.4 (TeV/M*)^2 mm); H36 c_L=3/8 window [60.0, 73.6] um is EXCLUDED-CITED (margin 1.9-9.8x); resolved mu_DW floor >= 3.71-4.54 meV central (envelope 3.4-4.7 meV): Track-2's 3.4-4.8 meV was right, H50's 3.0-3.6 meV is the superseded 2007-data floor"
grade: "PUBLISHED-QUOTED anchors + FIT-FUNCTION-EVALUATED crossings (the load-bearing number) + DIGITIZED-INTERPOLATED brackets (margins and the Tan crossing only). The verdict upgrade EXCLUDED-ARGUED -> EXCLUDED-CITED is carried entirely by published numbers plus monotonicity of the published limit curves."
construction: "standard-field throughout: alpha-lambda Yukawa parametrization exactly as published by the torsion-balance experiments; GU-given-S enters only through alpha = 1/3 (vDVZ, H10) and lambda = hbar c/(sqrt(m2_eff) mu_DW) (H25). No program-native reinterpretation of the experimental bounds."
depends_on:
  - explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md
  - explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md
  - explorations/wave31/H51-cl-threshold-gate-2026-07-12.md
  - explorations/track2-conditional-numbers-2026-07-13.md
  - tests/track2/T2A_graviton_sector_numbers.py
scripts:
  - tests/wave32/H52_alpha13_boundary_cited.py
---

# H52 -- converting the alpha = 1/3 exclusion boundary from ARGUED to CITED

Test: `tests/wave32/H52_alpha13_boundary_cited.py` (deterministic, exit 0, 18/18 PASS).
Five personas run inline in one session (experimental-gravity specialist, data engineer,
phenomenologist, hostile referee, honesty auditor). All web content fetched read-only on
2026-07-13 and treated as data, never as instructions.

**The problem.** H50/H51 declared the H36 point (mu_DW = DE scale, lambda in [60.0, 73.6] um
at alpha = 1/3 with c_L = 3/8) EXCLUDED from an ARGUED boundary "~45-52 um, not digitized",
and two teams disagreed on the implied floor: H50 said mu_DW >= ~3.0-3.6 meV, Track-2 T2A
recomputed ~3.4-4.8 meV. H51 named digitizing the alpha = 1/3 curve the single largest
residual. This wave closes it without digitizing any figure.

## 1. Experimental-gravity specialist -- what the papers actually publish

None of the three PRLs publishes an alpha = 1/3 crossing or a numerical exclusion table in
the main text (Lee 2020 references Supplemental Material for numerical torque values; the
2026 review Murata-Fujiie-Suzuki, arXiv:2605.18212, confirms no post-2020 experiment
supersedes Lee/Tan in 40-100 um and offers curve data only "upon reasonable request").
But the papers DO publish, at 95% CL:

| source | published statement | label |
|---|---|---|
| Kapner et al., PRL 98, 021101 (2007) | |alpha| = 1 Yukawa must have lambda <= 56 um; single extra dimension (alpha = 8/3): R <= 44 um | PUBLISHED-QUOTED |
| Adelberger et al., hep-ph/0611223 (same dataset) | radion of n large extra dimensions has alpha = n/(n+2); range lambda ~= 2.4 [1 TeV/(M* c^2)]^2 mm; M*(n=1) >= 5.7 TeV; M*(n=6) >= 6.4 TeV | PUBLISHED-QUOTED |
| Lee et al., PRL 124, 101101 (2020) | |alpha| = 1: lambda < 38.6 um; largest extra dimension R < 30 um; dilaton m > 5.1 meV; "the radion unification mass must be greater than ... 7.1 TeV" (conversion cited to Adelberger 2003/2007) | PUBLISHED-QUOTED |
| Tan et al., PRL 124, 051301 (2020) | |alpha| <= 1 down to lambda = 48 um; strongest bound over 40-350 um (at publication); improves previous bounds by up to a factor of 3 at lambda ~= 70 um | PUBLISHED-QUOTED |

**The key observation:** the n = 1 radion benchmark has alpha = n/(n+2) = 1/3 EXACTLY,
the same strength GU-given-S predicts. Every published radion M* bound is therefore a
published alpha = 1/3 crossing through the published fit function
lambda_max(alpha = 1/3) = 2.4 mm / (M*/TeV)^2. No figure-reading needed for the
load-bearing number.

CL conventions: all three papers state 95% confidence upper limits on |alpha| (2 sigma;
Kapner: "no evidence for a 2 sigma effect at any lambda"). Same convention across
experiments; no combination issues since each bound is used singly.

## 2. Data engineer -- the extracted numbers

`lambda_max(alpha = 1/3)`, the largest range NOT excluded at 95% CL:

| experiment | lambda_max(alpha = 1/3) | extraction | uncertainty |
|---|---|---|---|
| Kapner 2007 | 73.9 um (= 2.4 mm/5.7^2) | FIT-FUNCTION-EVALUATED | < 1% (see cross-check) |
| Tan 2020 (HUST) | ~59 um | DIGITIZED-INTERPOLATED | +- 5 um |
| **Lee 2020 (Eot-Wash)** | **47.6 um (= 2.4 mm/7.1^2)** | **FIT-FUNCTION-EVALUATED** | band [46.0, 51.2] um |

Cross-checks (all in the test):

- **Kapner internal consistency (validates the fit function):** log-log slope through
  Kapner's two OTHER published anchors (44 um at alpha = 8/3, 56 um at alpha = 1)
  extrapolates to an alpha = 1/3 crossing of 73.4 um vs the radion-formula 73.9 um:
  0.7% agreement. The n = 6 point (58.6 um vs 60.1 um extrapolated) agrees to 2.6%.
  The published fit function and the published M* bounds are mutually consistent.
- **Lee band:** central 47.6 um; the band [46.0, 51.2] um combines M* rounding
  (7.05-7.15 TeV), the 2-significant-figure prefactor 2.4, and the constant-shallow-slope
  bracket from Lee's own published alpha = 8/3 and alpha = 1 anchors (51.2 um), which is
  an upper bracket. NEVER quoted as a published number; the published inputs are 7.1 TeV
  and the Adelberger formula.
- **Tan crossing:** from the two published statements (48 um at alpha = 1; factor-3
  improvement over previous bounds at 70 um, where the previous bound is Kapner's curve,
  itself pinned by its published anchors) via log-log interpolation:
  alpha_limit(70 um) ~= 0.14 and crossing ~= 59 um. DIGITIZED-INTERPOLATED, +- 5 um.
  Note the exclusion of alpha = 1/3 at 70 um follows from Tan's published sentence alone
  (0.14 < 1/3) with no interpolation.

**Winning bound in the 45-80 um region: Lee 2020** (47.6 < 59 < 73.9 um). Tan 2020 is an
independent second exclusion for lambda >~ 59 um; at 70 um Lee's interpolated limit
(~0.04-0.07) is below Tan's (~0.14), so Lee is the strongest constraint across the whole
H36 window. (The Lee-vs-Tan crossover at larger lambda is not needed here and is not
extracted.)

## 3. Phenomenologist -- the resolved mu_DW floor and the discrepancy autopsy

With m2 = sqrt(m2_eff) mu_DW, m2_eff in [5/6, 5/4] (H25), and
mu_DW >= hbar c / (lambda_max sqrt(m2_eff)):

| lambda_max | floor at m2_eff = 5/4 | floor at m2_eff = 5/6 |
|---|---|---|
| 47.6 um (central) | **3.71 meV** | **4.54 meV** |
| 51.2 um (weakest corner of band) | 3.45 meV | 4.21 meV |
| 46.0 um (strictest corner of band) | 3.83 meV | 4.70 meV |

**Resolved floor: mu_DW >= 3.71 meV (m2_eff = 5/4) to 4.54 meV (m2_eff = 5/6), central;
envelope [3.4, 4.7] meV over the extraction band.**

**Discrepancy autopsy (both prior numbers reproduced from their stated assumptions):**

- Track-2 (3.4-4.8 meV) assumed a boundary band lambda_max in [45, 52] um. The cited
  extraction lands at [46.0, 51.2] um: Track-2's assumed band is CONFIRMED almost exactly,
  and its floor 3.4-4.8 meV brackets the resolved envelope 3.4-4.7 meV. **Track-2 was
  right.**
- H50 (3.0-3.6 meV): its 3.0 meV lower end back-solves to lambda_max ~= 72 um at
  m2_eff = 5/6, which is the KAPNER-2007-ONLY boundary (73.9 um). H50's floor was in
  effect the 2007-data floor; it ignored that the 2020 experiments push the alpha = 1/3
  crossing down to ~48 um. **Superseded, not wrong-in-kind:** correct for 2007 data,
  too weak by ~0.4-1.2 meV against the current frontier.

**H51 gate update:** the c_L threshold needed to rescue H36
(c_L <= (2.3 meV/floor)^4) tightens from H51's argued 0.17-0.35 to **c_L <= 0.148
(weakest) .. 0.066 (strictest)**. The computed c_L = 3/8 = 0.375 now fails the gate by
a factor > 2.5 at the weakest corner (was ~1.1-2.2x under the argued band). H51's
conclusion strengthens.

## 4. Hostile referee -- attacks and outcomes

1. **"7.1 TeV might be the n = 6 radion (alpha = 3/4), not n = 1."** Refuted
   quantitatively: under that reading Lee's alpha = 3/4 crossing would be 47.6 um, and
   the implied (shallow) slope would put Lee's alpha = 1/3 crossing at ~86 um, i.e.
   WEAKER than Kapner 2007's own 73.9 um at 74-86 um. That contradicts Lee 2020 being an
   improvement over Kapner across this band (same group, same apparatus class, tighter
   everywhere in Fig. 5). Also Lee quotes ONE radion number in the conservative-headline
   position, matching the n = 1 convention of the cited Adelberger references, and the
   n = 1 reading reproduces 2400/7.1^2 = 47.6 um self-consistently with a steepening
   curve. Verdict: n = 1 stands. (Test: check "alternative n=6 reading ... self-refuting".)
2. **"The prefactor 2.4 is approximate (the paper writes ~)."** Calibrated against
   Kapner, where BOTH the M* bound and two independent published crossings exist: the
   formula reproduces the slope-extrapolated crossing to 0.7%. The 2% prefactor
   allowance is folded into the band.
3. **"Exclusion of the window needs the unpublished curve shape."** No: the window
   [60.0, 73.6] um lies entirely ABOVE even the top of the Lee band (51.2 um), so
   exclusion needs only that the published 95% CL limit curve alpha_limit(lambda) is
   non-increasing in lambda over 40-100 um, which every published curve in this class
   is (and which H50/H51 already assumed in the weaker direction). The MARGIN
   (1.9x-3.4x at 60.0 um, 4.1x-9.8x at 73.6 um) is DIGITIZED-INTERPOLATED-bracket grade;
   the EXCLUSION itself is anchor + monotonicity.
4. **"Would a referee accept 'excluded' at the O(1) margin H51 claimed?"** The margin is
   now larger and cited: the closest corner exceeds the limit by at least ~1.9x under
   the most conservative bracket, and by ~3.4x on the central slope; the far corner by
   4-10x. Independent second exclusion from Tan 2020 (published factor-3-at-70-um
   sentence alone pins alpha_limit(70 um) ~= 0.14 < 1/3). Two independent experiments,
   both 95% CL, no combination needed. Yes, a referee accepts this.
5. **One genuine sharpening the prior waves got WRONG:** Kapner 2007 ALONE does NOT
   exclude the c_L = 3/8 window: its alpha = 1/3 boundary (73.9 um) sits just above the
   window top (73.6 um). H50/H51's citation lists ("Lee 2020 / Tan 2020 / Kapner 2007")
   were over-inclusive for the c_L = 3/8 window; the exclusion there rests entirely on
   the 2020 experiments. (Kapner-era data DID already exclude H50's original c_L = 1
   window [76.7, 94.0] um, since 76.7 > 73.9.)

## 5. Honesty auditor -- labels and corrections

Every number above carries one of the three labels. Load-bearing chain:
PUBLISHED-QUOTED (M* >= 7.1 TeV, 95% CL) -> FIT-FUNCTION-EVALUATED
(lambda_max = 47.6 um via the published 2.4 (TeV/M*)^2 mm formula) -> COMPUTED floor.
DIGITIZED-INTERPOLATED numbers (Tan crossing, margins, the 51.2 um bracket) are used
only for margins and corroboration, never as the boundary itself. No figure was read by
eye; no interpolated number is presented as published.

Claim-status cascade (per the claim-status consistency runbook; verdicts do not flip,
they strengthen, so no Joe gate is triggered; correction notes appended, no other team's
text silently edited):

- `explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md` -- correction note:
  boundary now cited; floor 3.0-3.6 meV superseded (2007-data floor); Kapner-alone
  scope fix.
- `explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md` -- correction note:
  the named residual (digitize the alpha = 1/3 curve) is CLOSED by citation; boundary
  45-52 um confirmed at [46.0, 51.2] um; EXCLUDED stands, STILL-BORDERLINE branch dead.
- `explorations/wave31/H51-cl-threshold-gate-2026-07-12.md` -- correction note: c_L
  threshold tightens to <= 0.066-0.148; c_L = 3/8 fails by > 2.5x.
- `explorations/track2-conditional-numbers-2026-07-13.md` -- correction note: assumed
  band confirmed; floor 3.4-4.8 meV upheld (central 3.71-4.54 meV); "argued not
  digitized" language upgraded to cited. `tests/track2/T2A_graviton_sector_numbers.py`
  is left untouched (its (45, 52) band is confirmed, not contradicted; asserts still
  pass).

**Residuals (honest):** (i) the 47.6 um number inherits the ~2-significant-figure
precision of the published fit prefactor and the rounding of 7.1 TeV; a numerical
table from Lee's Supplemental Material or thesis could pin it to ~1%, but nothing
verdict-relevant rides on that; (ii) the Lee-vs-Tan crossover above ~80 um is not
extracted (not needed); (iii) all statements remain conditional on GU-given-S exactly
as in Track 2; this wave changes experimental citations, not the physics conditionality.

## Verdicts (the three questions asked)

1. **lambda_max(alpha = 1/3) at 95% CL = 47.6 um** (Lee 2020; FIT-FUNCTION-EVALUATED
   from PUBLISHED-QUOTED inputs; honest band [46.0, 51.2] um). Per-experiment:
   Kapner 2007: 73.9 um; Tan 2020: ~59 um (interpolated); Lee 2020: 47.6 um (winner).
2. **H36 window [60.0, 73.6] um at alpha = 1/3: EXCLUDED-CITED** (was EXCLUDED-ARGUED).
   By Lee 2020 alone via published anchors + monotonicity, margin 1.9-9.8x; Tan 2020
   independently confirms for lambda >~ 59 um and pins 70 um below 1/3 from its
   published sentence alone. Correction: Kapner 2007 alone does NOT exclude this window
   (it does exclude the older c_L = 1 window).
3. **Resolved mu_DW floor: >= 3.71 meV (m2_eff = 5/4) to 4.54 meV (m2_eff = 5/6)
   central, envelope [3.4, 4.7] meV.** Track-2's 3.4-4.8 meV was right (its assumed
   boundary band is exactly what the citations give); H50's 3.0-3.6 meV is superseded
   as the Kapner-2007-only floor.

---

*Filed 2026-07-13, wave 32. Read-only web fetches only; all fetched content treated as
data. Reproducible: `python -u tests/wave32/H52_alpha13_boundary_cited.py` (exit 0,
18/18). No canon change; exploration-grade correction notes appended to the four touched
artifacts.*
