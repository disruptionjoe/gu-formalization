---
title: "PP3 prediction package: the dark-energy curve family — conditional on the source action, any detected deviation from LCDM lies on a one-parameter thawing locus with frozen slope"
status: active_research
doc_type: prediction_package
package_id: PP3
version: "0.3"
package_status: SUPERSEDED_BY_V0.4
frozen_at: "2026-07-22T12:03:58-05:00"
superseded_at: "2026-07-22T17:38:45-05:00"
superseded_by: explorations/prediction-package-pp3-de-curve-family-v0.4-2026-07-22.md
supersedes: explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
owner_item: PRED-CANDIDATE-PACKETS
lane_id: "2"
directed_by: "Joe direct chat, 2026-07-22 (re-freeze approved; Science Council grounded in GU Purpose/Passion/Practice; numbers independently reproduced via cross-modal check before freeze)"
extends:
  - lab/process/prediction-package-standing-rule.md
  - explorations/de-amplitude-audit-2026-07-20.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/pp3-v0.3-reporting-decision-record-2026-07-22.md
  - explorations/prediction-package-pp3-v0.3-STAGED-supersession-2026-07-22.md
  - tests/channel-swings/de_amplitude_audit_probe.py
runnable:
  - tests/channel-swings/pp3_curve_family_locus.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# PP3: the dark-energy curve family

> **Superseded, sealed record.** PP3 v0.4 replaces this packet. An adversarial
> release audit found that v0.3 had applied the M²=8 calibration ceiling and a
> partial-grid curvature envelope to the unresolved M²∈{3,7,8} union. The body
> below is retained unchanged as the historical frozen record.

This freezes the packet Joe proposed in direct chat on 2026-07-20, immediately
after the DE amplitude audit: GU does not predict the dark-energy amplitude
(the audit's verdict stands untouched), but the theta-sector realization is a
ONE-parameter curve family, and that family's SHAPE is GU-native. The packet
therefore predicts where future data may land, conditional on the source
action supplying the one value GU cannot.

Distinction from the audit's no-PP3 adjudication: the audit correctly
declined to package the AMPLITUDE (an import, retrodiction-shaped). This
packet packages the CURVE FAMILY — a different observable with forward
content. Both judgments stand together.

## v0.3 supersession note (2026-07-22 re-freeze)

v0.3 is a disclosure-and-currency supersession of v0.2, approved by Joe in
direct chat after the Science Council (grounded in GU's Purpose/Passion/Practice)
adjudicated two number-adjacent flags. **It changes wording, disclosure, and
basis only — ZERO frozen locus / band / segment / curvature / kill number
changes.** Number-invariance was independently reproduced before this freeze
(emitter `pp3_curve_family_locus.py` exit 0, locus table cell-for-cell; the
amplitude legs re-run via `de_amplitude_audit_probe.py` and
`W113_world_contact.py`). Summary of what changed: the DESI DR2 exclusion is
now stated as CALIBRATION-SCOPED (it was stated as a plain data fact) and an
amplitude ledger keeps the two distinct data-preferred amplitudes from being
cross-wired (Flag A); a stale emitter receipt count is corrected (Flag B); a
sign-leg basis-currency section is added at honest grade. v0.2 is sealed and
carries a superseded-by header. Full audit trail:
`explorations/pp3-v0.3-reporting-decision-record-2026-07-22.md`.

## Predeclared observable and convention

- Native observables: the BAO distance ratios D_M/r_d, D_H/r_d and their
  redshift dependence, as measured by future official BAO releases beyond
  the frozen DESI DR2 vector (arXiv:2503.14738 Table IV), plus SNe when
  integrated.
- Reporting convention for this packet: the CPL plane (w0, wa), with the
  family's image computed by least-squares fit of w(a) = w0 + wa(1 - a)
  over z in [0, 2.33] (the DESI range), at own-theta_star calibration,
  exact-budget radiation treatment. CONVENTION PIN: the exact z = 0 value
  obeys w0_exact + 1 = C_exact f0 with C_exact = 1.33-1.39 (canon Result-2
  convention); the CPL-fit intercept is a distinct, steeper convention
  (C_CPL = 1.99-2.16). The two must never be conflated; the locus table
  below is in the CPL convention.
- Emitter: `tests/channel-swings/pp3_curve_family_locus.py` (exit 0,
  headline `7 [E] + 1 [F] = 8`, deterministic; never touches a likelihood).

## The frozen prediction (two branches, decision rule predeclared)

**Branch D (detection).** If a future release detects a deviation from
LCDM in the DE equation of state, the measured point lies ON the PP3
locus:

1. non-phantom side: w0 + 1 > 0 and w(z) >= -1 pointwise (inherited leg,
   shared with PP1);
2. inside the surviving segment: w0 + 1 <= 0.054 (CPL convention; the
   image of f0 <= 0.027, the frozen own-calibration current-data ceiling);
3. on the frozen slope: wa / (w0 + 1) in [-1.33, -1.00] (the M^2-band and
   segment drift of the shape invariant R; at canonical M^2 = 8,
   R = -1.00 to -1.06 across the segment).

The frozen locus table (M^2 = 8, CPL over z <= 2.33, own calibration):

| f0 | w0+1 | wa | wa/(w0+1) | max deviation of w+1 |
|---|---|---|---|---|
| 0.005 | 0.01082 | -0.01080 | -0.998 | 0.0094 |
| 0.010 | 0.02121 | -0.02150 | -1.013 | 0.0183 |
| 0.015 | 0.03122 | -0.03208 | -1.028 | 0.0267 |
| 0.020 | 0.04086 | -0.04253 | -1.041 | 0.0348 |
| 0.027 | 0.05380 | -0.05691 | -1.058 | 0.0456 |
| 0.125 (canonical ref; off-segment under own calibration — viable under amplitude marginalization, see disclosure) | 0.18943 | -0.22702 | -1.199 | 0.1567 |

Band spots (f0 = 0.020): M^2 = 3: (w0+1, wa) = (0.01013, -0.01343),
R = -1.325; M^2 = 7: (0.03292, -0.03643), R = -1.107.

4. (v0.2) the SECOND shape invariant — curvature confinement: the
   deviation of w(a) from CPL linearity is also one-parameter confined,
   S2 = wb/(w0+1) = -0.159 to -0.181 at canonical M^2 = 8 (mean -0.170;
   wb = leading quadratic coefficient of the residual from the frozen
   linear fit — the v0.1 numbers are untouched). Across the admissible
   band S2 is NOT constant: S2(M^2 = 3) = -0.026, S2(M^2 = 7) = -0.135 —
   so the curvature, unlike the slope, DISCRIMINATES M^2 within the band.
   Frozen consequence: a Branch-D detection precise enough to measure
   curvature reads off the root system (S^3 vs A_1 vs BC_1) — a second
   decimal frozen pre-data, and a future refinement of the condition
   chain rather than a near-term kill. Envelope for the band:
   S2 in [-0.19, -0.02], sign-definite negative.

The qualitative shape claim: a THAWING curve — w pinned at -1 in the deep
past, lifting toward late times, never phantom, with the specific lift
profile of the linear KG theta mode. In one sentence: **if the universe's
dark energy deviates from a cosmological constant, GU's theta-sector says
the deviation is small, thawing, non-phantom, and sits on a line through
(w0, wa) = (-1, 0) of slope -1.0 to -1.3 — one number (the split
fraction) away from fully specified.**

**Branch N (null).** If no deviation is detected, the ceiling shrinks and
the family remains an LCDM mimic. The packet SURVIVES but is confirmed
only in shape, never in value; this is stated now so a future null cannot
be spun as support. A permanent mimic is a permanently unfalsifiable
corner — the packet's value dies asymptotically with the ceiling, and the
honest close-out in that world is "indistinguishable from Lambda."

## Condition chain (enumerated)

1. The theta-sector two-component realization (frozen H44 model spec:
   rho_L + linear KG mode, flat closure, slow-roll attractor IC) IS GU's
   dark-energy sector — the construction-scoped premise.
2. The source action exists and supplies the split fraction f0 (and the
   absolute scale, via the B.5 slot per the P5 dossier Element 2). PP3
   never claims GU computes f0; f0 is the one dial, and the source action
   is its named supplier.
3. M^2 lies in the admissible band {3, 7, 8} (S^3 / A_1 / BC_1; OQ2).
4. Own-theta_star calibration convention (CMB-anchored distance closure).
5. Frozen rows COSMO-A1 (confrontation-only bracket) and the DE-F1
   tripwire; PP1's conditional chain for the sign leg.

If any link fails, the packet reverts per its named kill or degrades to
the construction-scoped statement of the audit.

## Sign-leg basis and the no-dynamical-crossing currency (v0.3)

The non-phantom leg (Branch-D item 1; K1) is inherited from PP1. As of this
re-freeze its basis is stated current, at honest grade; NO frozen number in
this packet changes:

- The DE sign cannot DYNAMICALLY flip: any orientation internal to the record
  dynamics is derivable/disclosed and cannot be the becoming-involution; the
  true external bit sigma is underivable and unmintable from inside (a fully
  source-internal mint is a Kleene quine). Grade: CONDITIONAL-THEOREM under the
  first-person-underivability standard (Lean-proved on the involution leg only;
  the literal monotonicity bridge is refuted). Grounds sign EXTERNALITY only;
  sigma's value and the amplitude are untouched.
- sigma is typed sigma = w_1(L_time), the first Stiefel-Whitney class of the
  arrow-of-time line bundle over F ~ RP^3 (Z/2 = spin cover S^3 -> RP^3;
  post-freeze sharpening 2026-07-21). The "sigma = circle-orientation" reading
  is a class-relative LOCAL no-go, not a global impossibility — that reading
  stays OPEN. Numerically inert for PP3.
- Convergent toy-grade support (TI/TaF): the Krein/orientation co-flip identity
  makes sgn(w0+1) the single global readout of one external orientation bit,
  with provenance rule SRC-COH-1 (a relative-sign flip is a hidden external
  import, not a dynamical process — so a dynamical crossing is forbidden);
  E139 (the de Sitter DE sector is fixed-source disclosure, W4 fails); and the
  arrow-as-theorem + T19 (the arrow-reversal involution is refuted). All
  toy-grade, conditional. Honest qualifiers: the arrow<->DE-sign welding is
  tight only under zero-import operations (separating them costs "one extra
  Z/2," itself an external import, NOT a dynamical-crossing route); the
  cross-repo GU=TaF=TI orientation identity is leg-deep, not mechanism-deep;
  the finality->physical-arrow grounding is conditional.

Roll-health antecedent (honest gate, aligns with CPRED-04): the healthy
dynamical roll assumed by the THAWING-SHAPE legs is OPEN in the program's
covariant cosmology — the strongest local realization is superluminal except at
constant-Lambda (DU COV-02), scale-free causal-memory completions track rather
than accelerate (DU CMF-01), and a healthy accelerating roll (COV-03) is
unbuilt. Neither failure crosses the phantom divide (all land at w >= -1), so
both are CONSISTENT with — even corroborate — the non-phantom prediction. This
gates the SHAPE, not the SIGN; the sign leg is roll-health-independent.

## Competitor baseline

- LCDM: w = -1 exactly. Branch N is indistinguishable from it — stated
  plainly; PP3 beats LCDM only in Branch D.
- Free w0waCDM: two free parameters. PP3 is a ONE-parameter sub-locus of
  that plane; the testable content is the lost dimension (the slope
  confinement), plus the sign and segment bounds.

## Kill thresholds (numeric, predeclared)

- **K1 (phantom kill, shared with PP1):** a detected w0 + 1 < 0 or
  pointwise w(z) < -1 at >= 3 sigma. Kills the sign leg and PP3 with it.
- **K2 (slope kill — the PP3-specific one):** a detected deviation whose
  wa/(w0+1) lies outside [-1.33 x 1.35, -1.00 x 0.65] = [-1.80, -0.65]
  at >= 3 sigma (the frozen band widened by the predeclared 35% tolerance
  of the discriminator in the emitter). Detection ON the non-phantom side
  but OFF the slope kills the theta-sector family as the realization.
- **K3 (segment kill):** a detected w0 + 1 > 0.06 (CPL) jointly with the
  packet's own calibration convention — i.e., a deviation too LARGE for
  the surviving segment. Since f0 <= 0.027 is the frozen ceiling under the
  packet's OWN-calibration (CMB-anchored) closure (condition link 4; not a
  calibration-independent DR2 fact), a larger detected amplitude — read in
  that same convention — contradicts the family's own likelihood structure:
  kill, not stretch.
- **K4 (web kill):** a source-side derivation of f0 (the N4/F7 route)
  that lands off the measured point once Branch D data exists.

## Known-inputs disclosure (the retrodiction guard)

- The DESI DR2 BAO vector (arXiv:2503.14738) is CONSUMED in this packet's
  construction. Under the packet's OWN-theta_star (CMB-anchored) distance
  calibration (condition link 4) it produced the f0 <= 0.027 ceiling (image
  w0+1 <= 0.054) and the +5.7 sigma overshoot of the canonical f0 = 0.125
  amplitude. This ceiling is CALIBRATION-SCOPED, not a calibration-independent
  property of DR2: under amplitude marginalization the same DR2 BAO likelihood
  is consistent with f0 up to ~0.15 — the canonical f0 = 0.125 included, inside
  the delta-chi^2 <= 1 band (W113) — and the theta-sector shape slightly
  out-fits LCDM. The sole residual exclusion lives in one direction, the
  amplitude-calibration direction. Nothing derived from DR2 is claimed as
  prediction.

  Amplitude ledger (the two data-preferred A* are DIFFERENT numbers against
  DIFFERENT references and must never be cross-wired; verified 2026-07-22 by
  `de_amplitude_audit_probe.py` and `W113_world_contact.py`):
  - A_Planck (CMB baseline) = 30.2577 (import; the f0 -> 0 limit).
  - A_GU (own-theta_star pinned prediction) = 31.9715 = +5.66% above Planck.
  - Own-theta_star confrontation (the KILL leg): A_GU overshoots the
    BAO-preferred amplitude A* = 31.4709 (sigma_A = 0.0872) by +5.74 sigma;
    dAIC = +35.79 -> the amplitude leg is decisively disfavored (this is the
    "+5.7 sigma" the packet quotes).
  - Amplitude-marginalized (the VIABILITY leg): letting the amplitude float,
    GU's shape best-fits at canonical f0 = 0.125 with A* = 30.8059 = +1.81%
    above Planck, inside delta-chi^2 <= 1 (f0 in [0.040, 0.150]); pinning A to
    Planck costs +41.3 chi^2.
  Reporting rule: lead with the sigma-tension (own-theta_star, +5.74 sigma) and
  dAIC (+35.79); demote every bare "%" to a baseline-carrying parenthetical.
  The sigma-tension is CONDITIONAL on the own-theta_star pinning (link 4), not a
  calibration-independent fact.
- The published state of the field at freeze time includes evolving-DE
  hints in the same (w0+1 > 0, wa < 0) quadrant as this locus. PP3 claims
  ZERO credit for that quadrant: it was known before the freeze. The
  novel, risky content is the SLOPE CONFINEMENT (item 3) and the segment
  bound (item 2) as future contours shrink — those numbers were computed
  here, from GU-side structure, before any data that can resolve them.
- Confrontation is against FUTURE releases only (post-DR2 BAO, SNe
  integration, joint chains); the packet is scored the first time a
  release can distinguish slope -1.0/-1.3 from its neighborhood.

## Council record (ten lenses, inline, pre-freeze)

Static five — orthodox: conditional predictions are respectable exactly
when the conditional chain is enumerated and the locus is rigid; both
hold; demanded the convention pin (done) and the known-inputs disclosure
(done). Heterodox: the deeper content is inversion — Branch D data
MEASURES f0, turning cosmology into the first instrument that reads the
B.5 slot; keep that framing, it is what makes the packet research rather
than PR. Commercial: cheap now, notarized, bounded downside, fat right
tail; the commit is the asset either way. Wild frontier: the first
confirmed LCDM deviation will be small and structured — having a
pre-registered structured family in the drawer is how a small program
wins that moment; pushed for the slope (the "next decimal"), not just
the sign — adopted as K2. Philosopher: this converts an apparently
degenerating move (amplitude is an import) into a progressive one (novel
risky shape content); severity requires the freeze to PREDATE the
discriminating data — hence freeze today, and the disclosure section
exists so the severity claim survives audit.

Specialist five — observational cosmologist: state the locus in CPL AND
keep the native D_M/D_H machinery runnable (done via the emitter); the
live risk is real — current hint central values may prefer steeper
slopes; that is content, not a flaw. Neural-network expert: (a) this is
a scaling-law epistemology — trust the conditional family, let the next
run falsify it; (b) the locus is a 1-D manifold in observable space, so
future confrontation is cheap (distance-to-manifold), and an off-locus
residual DIRECTION does credit assignment on which chain link broke —
record residual direction at confrontation, not just pass/fail (adopted
into K2/K4 semantics). Mathematical physicist: all absolute-scale routes
factor through one B.5 datum with three independent observable legs (DE
scale, spectral cut, C-strip width ~0.1 mm) — an overdetermined web; PP3
is one leg, and the web is the upgrade path. Statistician: two-branch
decision rule with numeric thresholds predeclared (done); demanded the
explicit statement that Branch N can never count as confirmation (done).
EFT theorist: this is standard practice dressed honestly — chiPT
predicts relations among observables with unknown LECs; f0 and lambda_0
are GU's LECs; PP3 is the relation, and relation-level confirmation is
the only victory claimable.

## Changelog

- **v0.3 (2026-07-22, re-freeze; Joe-approved, Science Council grounded in GU
  Purpose/Passion/Practice):** disclosure-and-currency supersession of v0.2.
  Wording / disclosure / basis only — ZERO frozen locus / band / segment /
  curvature / kill number changed (independently reproduced before freeze:
  emitter exit 0 and locus table cell-for-cell; W113 and de_amplitude_audit
  legs). Changes: (1) the DESI DR2 disclosure restated as CALIBRATION-SCOPED
  (was stated as a plain data fact) + the amplitude ledger added with the two
  distinct data-preferred A* kept distinct (Flag A resolution); (2) table row
  f0 = 0.125 relabeled canonical / off-segment; (3) K3 justification qualified
  to the own-calibration closure; (4) frozen-prediction item 2 -> "own-
  calibration ceiling"; (5) the emitter receipt headline corrected
  `6 [E]+1 [F]=7` -> `7 [E]+1 [F]=8` to match the current emitter (Flag B; the
  v0.2 changelog already carried 7+1=8); (6) sign-leg basis-currency section
  added (source-is-observer at conditional-theorem grade; sigma = w_1(L_time);
  TI/TaF co-flip toy-grade; roll-health antecedent). v0.2 is sealed with a
  superseded-by header. Excluded from this freeze: the amplitude residual as a
  candidate FUTURE Lane-2 native prediction (recorded as a seed, not injected).
  Full trail: `explorations/pp3-v0.3-reporting-decision-record-2026-07-22.md`.
- **v0.2 (2026-07-20, same day as freeze, pre-data):** added the second
  shape invariant S2 (curvature confinement) per the wild-frontier
  council lens ("predict the next decimal"). Additive only: no v0.1
  number, branch, or kill was altered; the emitter's v0.1 checks and
  frozen table are unchanged and re-verified (`7 [E] + 1 [F] = 8`,
  exit 0). S2 is recorded as a future discriminator (it reads M^2),
  not a near-term kill — K1-K4 remain the operative kill set.

## Receipts

- Locus emitter: `tests/channel-swings/pp3_curve_family_locus.py`
  (exit 0, `7 [E] + 1 [F] = 8`; convention pin machine-checked).
- Underlying machinery + verdict: `explorations/de-amplitude-audit-2026-07-20.md`,
  `tests/channel-swings/de_amplitude_audit_probe.py` (exit 0,
  `14 [E] + 4 [F] = 18`): ratio-only structure, tail-robustness, the
  f0 <= 0.027 ceiling, the +5.7 sigma canonical exclusion.
- Sign leg: `explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md`
  (PP1, frozen 2026-07-19).
- Slot analysis: `explorations/blockbuster-p5-instance-dossier-2026-07-19.md`
  Element 2 (the B.5 scale slot); `explorations/source-packet-coflip-holonomy-freeze-2026-07-20.md`
  (the adjacent frozen evidence packet).

## Boundary

Exploration tier under the standing axiom, R0_COND working grade;
CONDITIONAL grade stated per the standing rule; construction-scoped (the
theta-sector family as GU's DE realization). No claim-status, canon,
scorecard, or public-posture movement; nothing external moves (Joe alone
ever takes anything outside). Versioning per the standing rule: this v0.3
supersedes v0.2 (2026-07-20) with reasons recorded in the changelog and the
decision record; v0.2 is sealed and carries a superseded-by header; this file
is never edited beyond a superseded-by header.
