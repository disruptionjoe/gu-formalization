---
artifact_type: exploration
status: exploration
created: 2026-07-14
wave: W129
title: "W129 -- the OQ2 M^2-band sweep of the H46C dark-energy exclusion. The H46C theta_star-calibrated raw-BAO comparison is rerun across the full admissible OQ2 band (ground eigenvalues 3, 7, 8 plus a bracketing scan over M^2 in [1, 25] including the excited states and the 20.25 continuum threshold), the 1-component ansatz, and the z_start IC variants, with the Gaussian omega_m h^2 prior replaced by a profiled scan at three band points. VERDICT: HOLDS-BAND-WIDE at the pre-stated escape criterion -- at every band point the DESI-CPL-matched amplitude is excluded at dchi^2 >= +33.5 (profiled: >= +14.9 at the softest point) -- WITH a quantified honest softening: the H46C bound f0 < ~0.027 is the M^2 = 8 number, and across the admissible set the 3-sigma-equivalent bound runs from 0.027 (BC_1) through 0.039 (A_1) to 0.208 (S^3, M^2 = 3), where the reference point f0 = 0.125 is only mildly disfavored (dAIC +5.25; +2.0 with omega_m h^2 profiled). Everything the bound allows anywhere on the band is an LCDM mimic (|w0 + 1| < 0.1), so the surviving region cannot be the DESI dark-energy signal. The single-band-point (OQ2) gate on the exclusion is retired; SNe integration remains the named residual."
grade: "computation + statistics (tests/W129_oq2_m2_band_sweep.py, deterministic, exit 0, 13/13; positive controls reproduce H46C's M^2 = 8 row to 4 digits and the LCDM baseline chi^2 = 30.68 exactly). Exploration grade; canon verdict OPEN unchanged; DARK-ENERGY-06 scope correction applied per the claim-status consistency runbook; M^2 = 8 stays reconstruction-grade (OQ2 as 'which eigenvalue is THE GU value' remains open, but no longer gates the exclusion)."
depends_on:
  - tests/W129_oq2_m2_band_sweep.py
  - tests/wave46/H46C_theta_star_cmb_calibration.py
  - tests/wave29/H46_de_raw_bao_likelihood.py
  - tests/wave25/H44_de_backreacted_background.py
  - tests/wave20/H43_de_shape_falsifier.py
  - explorations/wave46/H46C-theta-star-gu-cmb-calibration-2026-07-13.md
  - canon/theta-field-flrw-dark-energy-eos.md
scripts:
  - tests/W129_oq2_m2_band_sweep.py
---

# W129 -- the OQ2 M^2-band sweep of the H46C dark-energy exclusion

## Object

H46C (Wave 46) delivered the falsification-hardened dark-energy verdict at ONE band
point: with GU's own theta_star CMB calibration, the canonical (M^2 = 8 H0^2,
f0 = 0.125) theta-sector distance model is excluded on the DESI DR2 raw BAO likelihood
at dAIC = +35.78 vs LCDM, with a 3-sigma-equivalent amplitude bound f0 < ~0.027. Its
stated honest limits: the M^2-band calibration scan was unexecuted (only the
reconstruction-grade M^2 = 8 shape ran), single pipeline, no SNe, Gaussian omega_m h^2
prior approximation. The 2026-07-14 landscape assessment ranked closing this gate as
problem #2 (H67): the cheapest headline-flipping computation, and the flagship
referee's vulnerability 3.

This wave executes the sweep. Five personas run inline, then synthesis.

Reproduction: `python -u tests/W129_oq2_m2_band_sweep.py` (deterministic, exit 0,
13/13 PASS; runtime a few minutes).

**Headline: the exclusion is NOT an artifact of the M^2 = 8 choice -- no admissible
(M^2, ansatz) point escapes at any amplitude that carries the DESI CPL signal -- but
the single-number bound f0 < ~0.027 IS an M^2 = 8 artifact: at the S^3 variant
(M^2 = 3) it relaxes by a factor ~7.6 to f0 < 0.208, and the correct band-wide
statement is signal-level, not amplitude-level.**

---

## Persona 1 -- cosmologist: the calibration across the band

The pipeline is H46C's, verbatim where possible: the H44 backreacted background
solver, the official DESI DR2 13-point likelihood (mean + full covariance) from H46,
the same Planck anchors (100 theta_star = 1.04110 +/- 0.00031, r_star = 144.43 Mpc,
z_star = 1089.92, r_drag = 147.09 Mpc, omega_m h^2 = 0.1430 +/- 0.0011, all
primary-source-verified in Waves 45/46), the same brentq solve of
theta_star(h; model) = theta_star(Planck), the same A1-A5 approximations, the same A3
ratio correction dividing out the shared pipeline systematic. The only new code
parameterizes H46C's `dm_integral` / `theta100_of` / `calibrate_h` over
(M^2, z_start, omega_m h^2) in place of the module constants.

Correctness gates, all green before any band point runs:

- PC0: the LCDM theta_star calibration recovers h = 0.67280 (0.12% pipeline offset,
  divided out by A3), identical to H46C's PC2.
- PC1: the LCDM baseline chi^2 = 30.678 reproduces the H46/H46C value 30.68.
- PC2: the parameterized machinery at (M^2 = 8, f0 = 0.125) reproduces H46C's row to
  four digits: h_cal = 0.63749, A_cal = 31.9714, dAIC = +35.780 (published 0.63746,
  31.97, +35.78).
- PC3: f0 -> 0 calibrates to the LCDM point at M^2 = 3 and 20.25 alike (the family is
  continuous across the band; the calibration lever is the theta density, not M^2
  itself).

Physics of the band direction: larger M^2 means the field unfreezes earlier
(z_osc grows with M), so more matter-like <w> = 0 theta density accumulates in the
past, the D_M(z_star) deformation grows, and the weak theta_star lever arm
(dln theta_star / dln h ~ 0.19) amplifies it into a larger calibrated-H0 undershoot.
Hence the monotone worsening up the band: h_cal falls from 0.663 (M^2 = 3) to 0.572
(threshold 20.25), and dAIC climbs from +5.3 to +314 at the reference f0 = 0.125.
Below M^2 ~ 2.25 (the de Sitter BF bound (3/2)^2) the field never oscillates, w stays
near -1, and the model degenerates toward LCDM regardless of f0 -- which is why the
low edge of the bracketing scan is harmless to LCDM and useless to GU.

## Persona 2 -- statistician: consistent comparison, worst case and best case

The comparison is fixed across the band: dAIC = chi^2_GU(own theta_star calibration)
minus chi^2_LCDM(own theta_star calibration = the Planck point, 30.68), k = (0, 0) on
both sides, no CMB chi^2 term double-counted. The band scan is NOT a fit: the OQ2
spread is theoretical uncertainty, so the verdict quotes the worst case (the band
point most favorable to GU) alongside the rest, and no best band point is allowed to
masquerade as the model.

Escape criterion, pre-stated in the test header before the scan ran: an ESCAPE is an
admissible point with dAIC < +4 (the weakest conventional Burnham-Anderson level at
which a point could be argued not meaningfully disfavored; H46C's own verdict level
was dchi^2 > 9) at an amplitude that carries the DESI CPL signal. Anything admissible
below +9 is additionally reported as a softening.

One subtlety the single-point H46C table could not see: f0 = 0.125 is the CPL-TUNED
amplitude at M^2 = 8 only. At other M^2 the amplitude that would actually mimic the
DESI signal differs (the w0 response coefficient C in w0 ~ -1 + C f0 falls with M^2).
So the escape test proper is evaluated at f0_CPL(M^2), the amplitude at which the
calibrated backreacted w0(f0) reaches the DESI CPL level w0 = -0.752, interpolated
from the per-f0 calibration scan at each band point.

Worst case and best case over the admissible set {3, 7, 8}, at the reference
f0 = 0.125: dAIC in [+5.25, +35.78] (worst case for the exclusion: S^3, M^2 = 3).
At the DESI-CPL-matched amplitude: dchi^2 in [+33.46, +47.18] -- no admissible point
comes anywhere near the +4 escape level, or even the +9 level, where it matters.

## Persona 3 -- DE theorist: what is actually admissible

Per the repo's OQ2 analysis (tests/wave20 `admissible_M2()`, source-first and
DESI-blind), the admissible set is the GROUND eigenvalue of each named root-system
assignment for the normal Laplacian on the GL(4,R)/O(3,1) fiber,
lambda = rho^2 - nu^2 in units H0^2:

- BC_1 (m1, m2) = (7, 1), rho = 9/2: ground M^2 = 8. The CANONICAL assignment.
- A_1 m = 8 (no long root), rho = 4: ground M^2 = 7. The "no long root" alternative.
- S^3 no-Z2 (full-sphere compact dual), l = 1: M^2 = l(l+2) = 3. The Z_2/covering
  ambiguity variant.

NOT admissible as sector masses, swept anyway as bracketing: the excited tower states
(12, 14, 15, 18, 20 -- the sector mass is the lowest normal mode; an excited state
could only matter if the ground mode were projected out, which nothing in the repo's
construction does) and the BC_1 continuum threshold rho^2 = 20.25 (the upper anchor:
above it the fiber spectrum is continuous, and it is not an eigenvalue). The
continuous scan [1, 25] covers all of these and everything between, matching the
H43/H44 CPL-level bracket.

The exclusion claim therefore attaches to {3, 7, 8}; the bracketing rows show it is
not knife-edged anywhere in [1, 25] either. What would make M^2 = 3 the preferred
value: adopting the full-sphere compact dual WITHOUT the Z_2 quotient in the
fiber-spectrum reconstruction. The repo's canonical reconstruction (rc3-delta-n
spectrum) takes BC_1; nothing in this wave moves that, and OQ2 (which assignment is
THE GU value) stays open. What this wave changes is the CONSEQUENCE of that openness:
before, the exclusion was hostage to it; now every admissible resolution of OQ2 lands
on an excluded point at signal level.

## Persona 4 -- numerical engineer: the tables

Full band sweep (two-component ansatz, z_start = 30; dAIC at the reference
f0 = 0.125; f0_9 = the 3-sigma-equivalent amplitude bound; f0_CPL = the
DESI-signal-matched amplitude and the escape test dchi^2 there):

| band point | class | M^2 | h_cal | dAIC@0.125 | w0@0.125 | f0_9 | w0@f0_9 | f0_CPL | dchi^2@CPL |
|---|---|---|---|---|---|---|---|---|---|
| BC_1 ground [CANONICAL] | admissible | 8.00 | 0.63749 | +35.78 | -0.805 | 0.0274 | -0.943 | 0.174 | +47.18 |
| A_1 ground (no long root) | admissible | 7.00 | 0.64346 | +26.36 | -0.838 | 0.0389 | -0.937 | 0.228 | +43.73 |
| S^3 no-Z2 l=1 | admissible | 3.00 | 0.66341 | +5.25 | -0.945 | 0.2076 | -0.917 | 1.628 | +33.46 |
| BC_1 excited nu=5/2 | bracketing | 14.00 | 0.60012 | +139.68 | -0.597 | 0.0058 | -0.965 | 0.057 | +79.33 |
| BC_1 excited nu=3/2 | bracketing | 18.00 | 0.58013 | +247.42 | -0.482 | >2.0* | - | 0.041 | +113.16 |
| BC_1 excited nu=1/2 | bracketing | 20.00 | 0.57312 | +306.34 | -0.445 | >2.0* | - | 0.041 | +135.54 |
| A_1 excited | bracketing | 12.00 | 0.61222 | +95.95 | -0.666 | 0.0095 | -0.956 | 0.075 | +65.14 |
| S^3 l=2 | bracketing | 15.00 | 0.59451 | +164.48 | -0.564 | 0.0051 | -0.967 | 0.051 | +88.11 |
| continuum threshold | bracketing | 20.25 | 0.57241 | +313.69 | -0.442 | >2.0* | - | 0.041 | +138.75 |
| scan | scan | 1.00 | 0.67063 | +0.99 | -0.984 | >2.0 | - | none | - |
| scan | scan | 2.00 | 0.66725 | +2.78 | -0.965 | 0.4403 | -0.910 | none | - |
| scan | scan | 4.00 | 0.65910 | +8.57 | -0.922 | 0.1297 | -0.919 | 0.740 | +35.57 |
| scan | scan | 5.00 | 0.65433 | +13.01 | -0.896 | 0.0783 | -0.929 | 0.454 | +38.06 |
| scan | scan | 6.00 | 0.64910 | +18.84 | -0.868 | 0.0561 | -0.932 | 0.317 | +41.23 |
| scan | scan | 9.00 | 0.63129 | +47.32 | -0.772 | 0.0214 | -0.945 | 0.140 | +51.79 |
| scan | scan | 10.00 | 0.62493 | +61.17 | -0.737 | 0.0157 | -0.950 | 0.112 | +56.06 |
| scan | scan | 16.00 | 0.58927 | +190.91 | -0.534 | >2.0* | - | 0.046 | +95.71 |
| scan | scan | 22.00 | 0.56867 | +363.86 | -0.428 | >2.0* | - | 0.045 | +165.59 |
| scan | scan | 25.00 | 0.56790 | +435.44 | -0.453 | >2.0* | - | 0.057 | +213.59 |

*The ">2.0" f0_9 entries at high M^2 are a scan-grid artifact worth naming, not a
loophole: there dchi^2(f0) already exceeds 9 at the smallest scanned amplitude
f0 = 0.005 (dchi^2 = +12.2 at M^2 = 18 and 20, +12.7 at 20.25), so no increasing
straddle of 9 exists WITHIN the scanned range -- the true bound is f0_9 < 0.005,
tighter than every quoted number, not looser. The two genuinely unbounded rows are
M^2 = 1 (below the BF bound: w = -1 forever, an exact LCDM mimic at any f0, so no
bound and also no signal -- f0_CPL = none) and M^2 = 2 (bound 0.44, mimic at the
bound).

Ansatz variants (the wave-20 set):

| variant | M^2 | dAIC | (w0, wa) |
|---|---|---|---|
| 1-component (pure theta, no knob) | 8.00 | +199.04 | (-0.184, -1.227) |
| 1-component | 7.00 | +166.85 | (-0.266, -1.101) |
| 1-component | 3.00 | +53.49 | (-0.641, -0.531) |
| 1-component | 20.25 | +654.20 | (+0.596, -2.434) |
| z_start = 10 (two-comp, M^2 = 8, f0 = 0.125) | 8.00 | +35.83 | f0_9 = 0.0273 |
| z_start = 60 (two-comp, M^2 = 8, f0 = 0.125) | 8.00 | +35.77 | f0_9 = 0.0274 |

The 1-component ansatz dies everywhere (its kinetic-dominated late-time w drags the
distances far off; even its softest point, M^2 = 3, is at +53.5). The z_start IC
variants move the canonical dAIC by less than 0.06 and the f0 bound by 0.0001: the
H46C result is insensitive to the IC redshift, as expected from the frozen attractor.

omega_m h^2 profiled (the H46C A6 Gaussian-prior limit closed; n = the omega_m h^2
shift in Planck sigmas, profiled over n in [-5, +2] for BOTH models; "penalized" =
chi^2 + n^2 under the Planck prior, "flat" = pure profile, no penalty):

| point | penalized dAIC | flat-prior dAIC |
|---|---|---|
| LCDM reference | 0 (min 17.33 at n = -2) | 0 (min 10.45) |
| GU M^2 = 3, f0 = 0.125 | +2.00 (n = -2) | -1.10 (n = -4) |
| GU M^2 = 8, f0 = 0.125 | +16.55 (n = -4) | +3.42 (n = -5, edge) |
| GU M^2 = 20.25, f0 = 0.125 | +223.77 (n = -5, edge) | +205.65 (n = -5, edge) |
| GU M^2 = 3, f0 = 0.2076 (its bound) | +2.89 | - |
| GU M^2 = 3, f0 = 1.628 (its CPL-matched amplitude) | +14.92 | - |

The M^2 = 8 penalized value +16.55 on the coarse integer n-grid matches H46C's +16.03
(half-sigma grid). Exit code 0; 13/13 checks PASS, including the three pre-registered
regression guards (H46C row, LCDM baseline, family continuity).

## Persona 5 -- adversarial skeptic: the escape hunt

The hunt was run to find an escape, not to confirm the exclusion. Findings, in
descending order of how close they come:

1. **S^3, M^2 = 3 -- the real finding of this wave.** At the reference f0 = 0.125:
   dAIC = +5.25, BELOW the 3-sigma-equivalent level; with omega_m h^2 profiled under
   the Planck prior, +2.00 -- statistically ALIVE at that amplitude. The f0 bound
   relaxes to 0.208, a factor 7.6 looser than H46C's headline 0.027. If the sweep had
   stopped at "is f0 = 0.125 excluded at every admissible M^2", the answer would be
   NO and the H46C headline would be reopened. It is not an escape, for one reason
   with two faces: at M^2 = 3 the amplitude f0 = 0.125 produces w0 = -0.945 -- an
   LCDM mimic, not the DESI signal (|w0 + 1| = 0.055 against DESI's 0.25). The
   amplitude at which M^2 = 3 WOULD reach the DESI signal level is f0_CPL = 1.63, and
   there it is excluded at dchi^2 = +33.5 raw, +14.9 with omega_m h^2 profiled. What
   survives at M^2 = 3 is a theta component that does nothing observable: it rides
   inside the LCDM error budget at up to ~21% of the dark-energy density, invisible
   by construction. H43's independent CPL-level result already said the same thing
   from the other side (the S^3 locus misses the DESI contour at 3.25 sigma at every
   f0).
2. **The flat-prior omega_m h^2 direction at M^2 = 8.** Removing the Planck penalty
   entirely and letting omega_m h^2 run to -5 sigma pulls the canonical point down to
   dAIC = +3.4 -- technically under the escape threshold. This is reported and then
   rejected as an escape on stated grounds: it requires omega_m h^2 = 0.1375, a
   5-sigma contradiction of the very CMB measurement the calibration is anchored to
   (one cannot keep theta_star and discard omega_m h^2; they come from the same
   likelihood), the minimum sits at the scan edge, and both models drift the same
   direction (the shared Planck-DESI omega_m tension), with LCDM keeping the lead.
   The defensible statistic is the penalized one: +16.55. What this row honestly
   quantifies is that a nontrivial share of the M^2 = 8 exclusion is carried by
   trusting the Planck omega_m h^2 width -- an SNe-shaped hole, since supernovae
   would independently squeeze exactly this low-omega_m direction. Named as the
   residual.
3. **The low-M^2 edge of the bracket (M^2 = 1, 2).** dAIC = +0.99 and +2.78 at
   f0 = 0.125: unexcluded, and irrelevant twice over -- not admissible (no root
   system in the repo's OQ2 analysis lands there), and below/at the BF bound the
   theta field is a pure w = -1 mimic that never reaches the DESI signal at any
   amplitude (f0_CPL = none).
4. **No interior f0 minimum beats LCDM decisively anywhere** (best case over the
   whole scan: -0.24 at M^2 = 1, f0 = 0.005; every admissible best case is > -0.1).
   The BAO + theta_star preferred amplitude remains the LCDM limit f0 -> 0 at every
   band point: the theta component stays an upper limit, not a detection, band-wide.

## Synthesis

**VERDICT: HOLDS-BAND-WIDE** at the pre-stated escape criterion, with a quantified
M^2-dependent softening that replaces the single-number amplitude bound.

1. **The exclusion of the theta sector as the DESI dark-energy signal is band-wide.**
   At every admissible OQ2 point (M^2 = 3, 7, 8), at every bracketing point of
   [1, 25] where the DESI CPL level w0 = -0.752 is reachable at all, under the
   1-component ansatz and the z_start IC variants, the DESI-CPL-matched amplitude is
   excluded at dchi^2 >= +33.5 under GU's own theta_star calibration; omega_m h^2
   profiling does not reopen the softest point (+14.9). No admissible (M^2, ansatz)
   point escapes. The OQ2 single-band-point gate on H46C (flagship referee
   vulnerability 3, landscape problem #2) is RETIRED.
2. **The honest softening.** The H46C bound f0 < ~0.027 is the M^2 = 8 number, not
   the band number. Across the admissible set the 3-sigma-equivalent bound is
   f0 < 0.027 (BC_1, canonical) / 0.039 (A_1) / 0.208 (S^3). Any DE-05-derived
   statement of the form "excluded for f0 >= ~0.03" must be read at M^2 = 8; the
   band-safe statement is signal-level: **at every admissible M^2, everything the
   BAO + theta_star bound allows is an LCDM mimic (|w0 + 1| < 0.1 at each bound), and
   every amplitude that would reproduce the DESI signal is decisively excluded.**
3. **Direction of the residual risk.** The remaining ways this verdict could move:
   SNe integration (named residual; it would tighten, not loosen, the one soft
   direction found -- the low-omega_m h^2 profile); a second BAO dataset/pipeline
   (the exclusion still rests on the DESI DR2 likelihood alone); an OQ2 resolution
   OUTSIDE the currently admissible set (nothing in the repo proposes one; the
   bracket scan says it would need M^2 < ~2, below every named assignment, and would
   land on a signal-free mimic anyway).

Scope guards: exploration grade; BAO + theta_star only; the excluded object is the
theta-sector DE family as a CMB-consistently-calibrated distance model at DESI-signal
amplitudes across the OQ2 band, not GU as a whole; the canon verdict on
`theta-field-flrw-dark-energy-eos.md` stays OPEN; no promotion; M^2 = 8 stays
reconstruction-grade; f0 and B_i remain fits, not GU predictions. Canon cascade:
CORRECTION DARK-ENERGY-06 applied to the canon file, RESEARCH-STATUS.md, and CANON.md
per the claim-status consistency runbook (this artifact is the owner surface).
