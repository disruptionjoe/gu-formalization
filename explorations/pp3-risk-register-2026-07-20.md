---
title: "PP3 risk register: where the official DR2-era w0waCDM central values sit relative to the frozen band — zero-weight exposure accounting, nothing in PP3 moves"
status: active_research
doc_type: exploration
package_ref: PP3
owner_item: PRED-CANDIDATE-PACKETS
lane_id: "2"
directed_by: "Joe direct chat, 2026-07-20 (fan-out: PP3 risk register)"
extends:
  - explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
  - lab/process/prediction-package-standing-rule.md
runnable:
  - tests/channel-swings/pp3_risk_register_calc.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# PP3 risk register (2026-07-20)

> **ZERO-WEIGHT BANNER.** Every published number in this note is
> PRE-FREEZE known data: the DESI DR2 BAO paper (arXiv:2503.14738) is
> dated March 2025, PP3 froze on 2026-07-20 and consumed the DR2 vector
> in its own construction, and PP3's known-inputs disclosure already
> names the evolving-DE quadrant as known. **Nothing here carries
> confirmation or kill weight for PP3. No kill fires, no branch
> resolves, no threshold is scored.** This note edits nothing in the
> frozen packet (versioning rule: the packet is never edited beyond a
> superseded-by header) and changes no claim status, canon verdict, or
> public posture. It is exposure accounting: it records where the
> official published central values sit relative to the frozen band, so
> that when a FUTURE release lands, the register already says plainly
> what "the DR2-era central values held" would mean.

## 1. Purpose

PP3 froze a one-parameter thawing locus: any future-detected deviation
from LCDM lies at slope wa/(w0+1) in [-1.33, -1.00], amplitude
w0+1 <= 0.054, non-phantom, with second invariant S2 ~= -0.17 at
canonical M^2 = 8. The packet's own council record flagged the live
risk ("current hint central values may prefer steeper slopes; that is
content, not a flaw"). This note quantifies that flag with the official
numbers, fetched today, cited exactly — not recalled from memory.

## 2. The fetched numbers (official, cited)

Source: arXiv:2503.14738v2, "DESI DR2 Results II: Measurements of
Baryon Acoustic Oscillations and Cosmological Constraints", Section
VII, equations (25)-(28); significance-of-preference column from
Table 6 of the same paper (Delta chi^2_MAP converted to sigma).
Fetched 2026-07-20 from the arXiv HTML (v2) and extracted verbatim from
the equation source.

| combo | w0 | wa | preference over LCDM |
|---|---|---|---|
| DESI+CMB (eq. 25) | -0.42 +/- 0.21 | -1.75 +/- 0.58 | 3.1 sigma |
| DESI+CMB+Pantheon+ (eq. 26) | -0.838 +/- 0.055 | -0.62 +0.22 -0.19 | 2.8 sigma |
| DESI+CMB+Union3 (eq. 27) | -0.667 +/- 0.088 | -1.09 +0.31 -0.27 | 3.8 sigma |
| DESI+CMB+DESY5 (eq. 28) | -0.752 +/- 0.057 | -0.86 +0.23 -0.20 | 4.2 sigma |

Also recorded from the paper: DESI BAO alone gives only a mild, prior-cut
preference (w0 = -0.48 +0.35 -0.17, wa < -1.34 at 68%, eq. 23; 1.7 sigma
per Table 6) — the strength of the published preference is driven by the
combinations, not by BAO alone. The paper quotes NO numeric w0-wa
correlation coefficient in Section VII; it describes the degeneracy
directions qualitatively only.

## 3. Computed exposure (emitter: `tests/channel-swings/pp3_risk_register_calc.py`)

Slope r = wa/(w0+1); sigma_r by first-order propagation of the quoted
marginal errors (asymmetric wa errors symmetrized), correlation ignored
(none published — see Limitations). "d(band)" = sigma distance of the
central slope below the frozen band edge -1.33; "d(K2)" = distance below
the widened kill edge -1.80. "dA(seg)" = sigma distance of the central
amplitude above the segment ceiling 0.054 in the w0 marginal; "dA(K3)"
= same vs the K3 threshold 0.06. "z_x" = redshift where the central CPL
curve crosses w = -1 (the phantom crossing implied by the central fit).

| combo | w0+1 | slope r | sigma_r | d(band) | d(K2) | dA(seg) | dA(K3) | z_x |
|---|---|---|---|---|---|---|---|---|
| DESI+CMB | 0.580 | -3.02 | 1.48 | 1.14 | 0.82 | 2.50 | 2.48 | 0.50 |
| DESI+CMB+Pantheon+ | 0.162 | -3.83 | 1.81 | 1.38 | 1.12 | 1.96 | 1.85 | 0.35 |
| DESI+CMB+Union3 | 0.333 | -3.27 | 1.23 | 1.58 | 1.20 | 3.17 | 3.10 | 0.44 |
| DESI+CMB+DESY5 | 0.248 | -3.47 | 1.18 | 1.82 | 1.42 | 3.40 | 3.30 | 0.41 |

Emitter receipt: `5 [T] + 6 [E] = 11` checks pass, exit 0; the [T]
checks recompute the arithmetic independently (identity r*(w0+1) = wa,
numerical-partial propagation vs analytic, alternative sigma form,
K2-band reconstruction from the packet's 35% rule, crossing-redshift
residual).

## 4. Assessment against the frozen band

**The honest headline: all four official central values sit OUTSIDE the
frozen PP3 band on both axes.**

- **Slope.** Central slopes run -3.0 to -3.8 — steeper not only than
  the frozen band [-1.33, -1.00] but than the K2-widened band edge
  -1.80. Tension is ~1.1-1.8 sigma vs the band edge (per combo, naive
  propagation), ~0.8-1.4 sigma vs the K2 edge. None of this reaches the
  predeclared 3-sigma kill bar even at face value, and it carries zero
  weight regardless — but the DIRECTION is uniform across all four
  combos: the published fits prefer a much steeper thawing line than
  the theta-sector family can produce.
- **Amplitude.** Central w0+1 runs 0.16 to 0.58 vs the frozen segment
  ceiling 0.054 — outside by ~1.9-3.4 sigma in the w0 marginal. The
  two strongest-preference combos (Union3, DESY5) sit ~3.1-3.3 sigma
  above the K3 threshold at face value. This is the sharper of the two
  exposures.
- **Phantom crossing (K1-relevant).** Every central CPL curve crosses
  w = -1 at z ~ 0.35-0.50. PP3's family is non-phantom pointwise. A
  future release confirming pointwise w(z) < -1 at >= 3 sigma fires K1
  (shared with PP1), independent of the slope question.
- **S2 (curvature).** The published fits are pure CPL; they carry no
  curvature information. The second invariant is unresolved by
  anything in this register.

Structural note, so the register is not misread as a contradiction
inside PP3: the f0 <= 0.027 ceiling (image: w0+1 <= 0.054) was derived
by fitting the one-parameter GU family to the same DR2 vector — a
WITHIN-family constraint. The free two-parameter fits above prefer a
point OFF the family. Both facts coexist consistently; together they
say the DR2-era data, taken at central value, pull off-locus, and the
family's own best fit against that data is small-amplitude. That is
exactly the risk PP3 accepted at freeze.

**What "central values hold" would mean.** If a future, packet-eligible
release reproduces these central values with shrunken contours, K3
(amplitude) fires first, K2 (slope) close behind, and K1 fires via the
pointwise phantom crossing. Branch D would then resolve AGAINST the
theta-sector family as GU's DE realization, and the packet reverts per
its named kills. Conversely, the published preference is combination-
driven (BAO alone: 1.7 sigma) and the SNe compilations disagree among
themselves at the ~2x level in amplitude — central values migrating
toward (w0, wa) = (-1, 0) with a small residual deviation is exactly
the corridor in which PP3's Branch D becomes live. The register's job
is to make both outcomes score cleanly, in public, later.

## 5. Limitations (named, all of them cutting in known directions)

1. **Correlation ignored.** arXiv:2503.14738 quotes no numeric w0-wa
   correlation coefficient in Section VII, so the slope propagation
   uses marginal errors only. The w0-wa contours are known to be
   strongly anti-correlated; since both partials of r = wa/(w0+1) are
   positive at every central point (wa < 0), a negative covariance term
   would SHRINK sigma_r — the quoted ~1.1-1.8 sigma slope tensions are
   therefore likely UNDERSTATED. No correlation value is invented; the
   proper statement awaits a 2-D distance-to-locus against released
   chains.
2. **CPL-convention mismatch.** The published (w0, wa) are posterior
   summaries of a free w0waCDM fit over the full data range under the
   DESI priors; PP3's locus table is the least-squares CPL image of the
   GU w(a) over z in [0, 2.33] at own-theta_star calibration. Same
   plane, different projections — and PP3's own convention pin (exact
   z = 0 vs CPL-fit intercept, C_exact vs C_CPL) shows convention shifts
   of tens of percent are possible. The comparison here is indicative,
   not a like-for-like confrontation.
3. **Calibration convention.** The published combos use the full CMB
   likelihood (and CMB lensing); PP3's segment ceiling is stated at
   own-theta_star calibration (CMB-anchored distance closure). Nearby
   but not identical anchors.
4. **Symmetrized asymmetric errors.** The wa error bars for the SNe
   combos are asymmetric; the propagation uses their mean.
5. **Marginals, not joint.** Sigma distances are read per-axis from 1-D
   marginals; the honest confrontation object is distance-to-manifold
   in the joint posterior (as PP3's council already specified for the
   real scoring, including residual-direction credit assignment).
6. **Model-region mismatch.** The published central fits are phantom-
   crossing curves; PP3's family is non-phantom by construction. At
   central value the two live in different model regions, which is
   part of the exposure, not a correctable artifact.

## 6. What moves the register

- **Future releases that can score the packet:** DESI DR3 / full
  five-year BAO (and full-shape), Euclid spectroscopic BAO, Rubin/LSST
  and ZTF SNe compilations (which may also resolve the current
  Pantheon+/Union3/DESY5 amplitude disagreement and the SN calibration-
  systematics debate), next-generation CMB (SO), and the joint chains
  built from them. Per PP3's disclosure, confrontation is against
  post-DR2 releases only; the packet is scored the first time a release
  distinguishes slope -1.0/-1.3 from its neighborhood.
- **The decision rules are already frozen** — K1 (phantom, >= 3 sigma
  pointwise), K2 (slope outside [-1.80, -0.65] at >= 3 sigma), K3
  (w0+1 > 0.06 in the packet's own calibration convention), K4
  (source-side f0 lands off the measured point). Nothing in this
  register adds, tightens, or loosens them; when the future data land,
  they apply as written.
- **Register maintenance:** re-run this note's emitter against each new
  official release's quoted numbers as a NEW dated register note (this
  file, like the packet, is not edited; supersede by a v2 with reasons).

## Receipts

- Emitter: `tests/channel-swings/pp3_risk_register_calc.py` (exit 0,
  `5 [T] + 6 [E] = 11`; published constants frozen in-file with
  citations; no likelihoods, no GU machinery).
- Frozen packet (untouched): `explorations/prediction-package-pp3-de-curve-family-2026-07-20.md`
  (v0.2, FROZEN_CONDITIONAL_CURVE_FAMILY).
- Source: arXiv:2503.14738v2, Section VII eqs. (23)-(28), Table 6
  (fetched 2026-07-20).

## Boundary

Exploration tier under the standing axiom. Zero confrontation weight by
construction (pre-freeze known data only). No claim-status, canon,
scorecard, or public-posture movement; no edit to any frozen packet;
nothing external moves (Joe alone ever takes anything outside).
