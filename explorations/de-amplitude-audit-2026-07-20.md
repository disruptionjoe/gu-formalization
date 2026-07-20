---
title: "DE amplitude audit: the theta_star re-solve with the full high-z tail, the blind H46B likelihood adjudication, and the honest amplitude statement"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (big-swing orchestration: Lane 2 DE amplitude audit)"
axiom: lab/process/boundary-adapter-standing-axiom.md
inputs:
  - lab/process/research-portfolio.json (DE-AMP-DIAGNOSTIC spec, authoritative)
  - explorations/wave46/H46C-theta-star-gu-cmb-calibration-2026-07-13.md
  - explorations/wave45/H46B-referee-grade-desi-verification-2026-07-13.md
  - explorations/de-amp-diagnostic-closure-audit-2026-07-15.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/channel-swing-CH-COSMO-2026-07-19.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md (Element 2, the B.5 scale slot)
  - explorations/pred-norm-rank-2026-07-15.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable: tests/channel-swings/de_amplitude_audit_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# DE amplitude audit (2026-07-20)

Lane 2's one READY item, executed per the repository's own portfolio spec.
Receipt: `tests/channel-swings/de_amplitude_audit_probe.py`, deterministic,
numpy + stdlib physics (repo modules imported only to verify seed-data
identity), run 2026-07-20, **exit 0**, headline:

```
HEADLINE: 14 [E] + 4 [F] = 18   (setup [T] = 7 excluded)   ALL PASS
```

## 0. What this audit is (spec vs brief, divergence named)

The portfolio entry `DE-AMP-DIAGNOSTIC` ("Audit the CMB-calibrated dark-energy
amplitude", track: diagnostic, READY) is the authority. Its `next_swing`:
*re-solve theta_star with GU's own full D_M(z_star), including the
high-redshift tail, then return a blind official-H46B likelihood
adjudication.* Its kill condition: *if the corrected canonical amplitude
remains strongly disfavored, close the positive raw-BAO amplitude leg; if it
moves, report the shift without calling it a new prediction.* Its forbidden
shortcut: *this is data hygiene and compatibility testing, not a decisive or
distinctive GU prediction; only H46B-verified likelihood inputs may seed the
calculation.*

The orchestration brief sketched a broader structural audit (which ratios are
forced, where the one absolute scale can enter, packageability). The two are
not the same object; per instruction the SPEC is executed as the core
(Sections 2-4) and the structural amplitude question is answered on top of it
(Sections 5-6), clearly separated. Divergence noted; nothing in the spec was
displaced by the sketch.

Relation to the 2026-07-15 closure audit
(`explorations/de-amp-diagnostic-closure-audit-2026-07-15.md`): that audit
recommended CLOSED for the bounded H46B-locality question, while the steward
kept the portfolio item READY with the full-tail re-solve as the remaining
swing. This run executes exactly that remaining swing, adds the M^2-band
calibration scan H46C named as its own cheap unexecuted hardening step, and
completes the one full normalization-and-likelihood audit after which the
spec's `switch_condition` says the item closes.

## 1. Construction forks, named (GEOMETER-VS-PHYSICS-OBJECTS discipline)

| Load-bearing object | Construction used | Why |
|---|---|---|
| DE background | PROGRAM-NATIVE: two-component DeWitt-Lambda (w = -1) + theta magnitude mode, linear KG | The frozen H44 model spec; the only GU-side DE construction the repo owns |
| Mode mass M^2 | PROGRAM-NATIVE: root-system band {3, 7, 8} H0^2 (S^3/A_1/BC_1 ground eigenvalues), reconstruction grade, OQ2 open | Never a tuned mass parameter; the band is scanned, not selected by data |
| Scale structure | PROGRAM-NATIVE ratio-only (H24 / PRED-NORM-RANK): geometry fixes dimensionless ratios only; NO absolute amplitude is GU-derivable at current grade | Settled fork (mu_DW row of the objects table); exhibited computationally in probe checks E10/E11 |
| Amplitude A = (c/H0)/r_d | STANDARD-PHYSICS import: Planck theta_star calibration + r_drag | The diagnostic asks whether the CMB-calibrated amplitude leg survives official likelihood inputs; using the standard apparatus does not make it a GU derivation |
| Likelihood | STANDARD-PHYSICS: official DESI DR2 13-dim BAO Gaussian likelihood, H46B-verified digits | Confrontation apparatus only; probe check F1 executes the blindness |
| The absolute-scale SLOT | PROGRAM-NATIVE-shaped slot, IMPORTED value: the B.5 global datum (P5 dossier Element 2, spectral-section cut scale) | The one place the frozen material allows an absolute scale to enter; the value (2.24 meV) is a pure empirical import, declared the dossier's weakest element |
| f0, B_i | FITS, not GU quantities (H42 preregistration; canon corrections DE-02..06) | Listing them as construction parameters would repeat the DE-04-era mistake |

A no-go read below is therefore branch-local to this construction set: it
falsifies the theta-sector family as a CMB-consistently-calibrated distance
model, never "GU" and never the source-action spine.

## 2. What was recomputed from scratch (nothing trusted from cache)

Per the standing rule from the DE history (the sign was once computed from a
hard-coded `d ln rho/dz = 3` against the real ~4.2; DARK-ENERGY-03), every
load-bearing number was recomputed by an independent implementation: fresh
RK4 + fixed-point background solver, fresh bisection calibration, fresh
likelihood assembly. The H44/H46/H46C modules were imported ONLY to verify
that the probe's embedded DESI/Planck arrays are bitwise identical to the
H46B-verified inputs ([T] checks).

| Quantity | This audit (fresh) | Prior value | Source of prior |
|---|---|---|---|
| d ln rho_B/dz at z = 0 | **+4.202** | 4.229 (archaeology) / 4.307 (bb-p1) / 3 (BUG, retired) | DARK-ENERGY-03; bb_p1 probe |
| Canon Result-2 coefficient C | **1.392-1.401** | 1.39 (canon) / 1.438 (bb-p1, LCDM bg) | canon Result 2 |
| Row 1 chi2 (GU/LCDM, Planck A) | **52.26 / 30.68** | 52.26 / 30.68 | H46/H46B |
| GU own calibration h_GU | **0.63749** (H0 = 63.75) | 0.6375 | H46C |
| A_GU (own theta_star calibration) | **31.9715** (+5.66% vs Planck) | 31.97 | H46C |
| Overshoot vs BAO-preferred A* | **+5.74 sigma_A** | +5.7 sigma_A | H46C |
| Row 2 dAIC (canonical f0, M^2 = 8) | **+35.79** | +35.78 | H46C |
| 3-sigma-equivalent split bound | **f0 < 0.027** | ~0.027 | H46C/W129 |
| M^2 = 3 canonical-f0 dchi2 | **+5.23** (mild) | +5.25 | W129 / DE-06 |
| rho_DE^(1/4), Planck point | **2.239 meV**; 1.13e-123 M_Pl^4 | 2.24 meV; ~1e-123 | COSMO-A1 bracket |

The 4.202 / 4.229 / 4.307 spread across three independent implementations is
a few-percent background/IC-convention sensitivity (backreacted vs pure-LCDM
background, slow-roll IC detail); all three sit far from the historical
hard-coded 3, and none of them is load-bearing for any sign or verdict (the
probe never uses this quantity to build w(z) — it is recomputed purely as the
bug-class guard).

## 3. The re-solve: full D_M(z_star) including the high-redshift tail

The spec's named upgrade over the fairness-argument era is executed in two
tail treatments:

- **R-A** (the H46C treatment): additive radiation keeping E(0) = 1 exactly;
  frozen theta density above z_start = 30.
- **R-B** (exact-budget, new): radiation as a genuine component Or a^-4 in
  BOTH H^2 and the KG friction, flat closure OL = 1 - Om - Or, so the high-z
  tail is the full component sum with no additive bookkeeping.

Result: the ratio-corrected calibrated amplitude differs between treatments
by **3.3e-5 relative** — the H46C verdict carries no tail systematic. The
"corrected canonical amplitude" therefore MOVES by less than 0.004%: per the
spec's kill condition this shift is reported and is not called a prediction.
The frozen-theta tail fraction at z_start is 3.4e-5 of matter, so fixing
r_star, z_star, r_drag at Planck values (the standard late-time-model move)
remains legitimate; the A2 neutrino approximation stays shared between both
pipelines and is divided out by the ratio correction.

## 4. The blind H46B likelihood adjudication

Blindness is executed, not asserted: the calibration functions contain no
DESI quantity (check F1 perturbs the DESI mean vector by 10% and the
calibrated h moves by exactly zero), and the COSMO-A1 meV bracket constant is
not even defined in the probe until every calibration output is frozen.

Adjudication (canonical f0 = 0.125, M^2 = 8, own theta_star calibration):
**chi2_GU = 66.47 vs chi2_LCDM = 30.68, dAIC = +35.79** — decisively
disfavored; the calibrated amplitude overshoots the BAO-preferred amplitude
for GU's own shape by +5.74 sigma_A. Per-f0 calibration scan: chi2(f0) is
monotone increasing; the BAO + theta_star preferred value is the LCDM limit
f0 -> 0 with 3-sigma-equivalent bound **f0 < 0.027**; the amplitude is an
upper limit, not a detection.

New hardening (the band scan H46C named but did not run): the calibration
re-solved at every admissible band point. Direction is band-generic
(h_cal < h_LCDM at M^2 = 3, 7, 8) and the exclusion is ordered:
dchi2 = +5.2 (M^2 = 3, mild — the DE-06 honest softening reproduced) /
+26.3 (M^2 = 7) / +35.8 (M^2 = 8). This independently confirms W129's
band-wide reading with a fresh implementation.

**Kill-condition adjudication (the spec's own words): the corrected
canonical amplitude REMAINS strongly disfavored. The positive raw-BAO
amplitude leg is CLOSED** (at exploration grade, M^2-band scoped, BAO +
theta_star only). What survives is exactly what DE-05/06 recorded: an
undetected component with f0 < 0.027 (canonical; band-softest ~0.21 at
M^2 = 3) riding on a DeWitt-Lambda LCDM mimic.

**PP1 first live read** (the flag CH-COSMO Section 3 left for this audit):
there is no detected deviation — the chi2 minimum sits at the f0 -> 0 edge,
one-sided bound only. The DE background is ORIENTATION-SILENT; PP1 stays
untriggered, and no sign-consistency datum for the transmitted Z/2 is
available from current data. Recorded as a non-firing outcome, exactly as
PP1-6 anticipated.

## 5. The honest amplitude statement (the structural question)

What the frozen material does and does not determine about the dark-energy
AMPLITUDE, as opposed to the sign:

**Forced (ratios and structure, at their recorded grades).**
- The two-component form: Lambda_eff at w = -1 exactly, plus an oscillating
  mode with time-averaged w = 0 (Result 1, algebraically exact).
- The mapping w_0 + 1 = C f0 with C = 1.39-1.40 recomputed (reconstruction
  grade), and the pointwise quintessence-side statement conditional on the
  PP1 chain.
- The admissible mass band M^2 in {3, 7, 8} H0^2 (reconstruction grade,
  OQ2 open) and z_osc ~ 1.85.
- The ratio-only scale structure itself: probe E10 exhibits that the absolute
  mode amplitude is unobservable in the shape (KG linearity — only the
  dimensionless f0 enters), and E11 exhibits that at f0 -> 0 the calibrated
  amplitude reduces EXACTLY to the imported Planck point: every GU-native
  contribution to the amplitude is a dimensionless calibration ratio.

**Free (and where the one absolute scale can enter).**
- GU fixes NO absolute dark-energy amplitude at any current grade.
  PRED-NORM-RANK stands: rank-3 rescaling freedom, four invariant quotient
  families, no native absolute normalization. This audit adds the
  computational exhibit (E10/E11) to that rank result.
- The single construction slot where an absolute scale is allowed to live is
  the B.5 global datum (P5 dossier Element 2): the spectral-section cut
  scale, a native-shaped SLOT whose VALUE is a pure empirical import — the
  declared weakest element of that dossier, typed ASSUMED. Nothing in this
  audit moves that typing; the 1e-123 question is relocated there, not
  answered.

**The honest amplitude statement, in one sentence.** The dark-energy
amplitude in GU is a PURE IMPORT (the COSMO-A1 empirical point,
rho_DE^(1/4) ~ 2.24 meV, confrontation data only) plus one GU-facing
DERIVED-FROM-IMPORTS consistency number — the model's own CMB-calibration
ratio (+5.66%) — which the official likelihood then DISFAVORS at the
canonical split; the surviving amplitude freedom is a one-sided split bound
f0 < 0.027 (canonical), and no amplitude prediction exists.

**Bracket confrontation (flagged, consumed nowhere upstream).** GU's own
calibrated total sits at 2.149 meV — inside the two-sided 10% COSMO-A1
bracket. The bracket does not discriminate at its resolution; the raw
likelihood (row 2) does. This is the two-layer structure CH-COSMO recorded:
total pinned two-sided, split bounded one-sided.

## 6. Packageability (standing rule applied — and not fired)

Against the admission criteria of
`lab/process/prediction-package-standing-rule.md`:

1. **The total amplitude** is not a derivable observable — it is an import
   into the B.5 slot. Fails criterion 1. Packaging it would also be a
   retrodiction (criterion 4).
2. **The f0 ceiling** (f0 < 0.027) is a DATA-derived bound, not a GU
   derivation; it is already carried as the COSMO-A1 ledger row and its
   dynamical companion is the already-frozen DE-F1 tripwire. Nothing new to
   freeze.
3. **The sign** is already PREDICTION PACKET 1 (frozen 2026-07-19); this
   audit's contribution to PP1 is the recorded non-firing live read
   (orientation-silent), not a new packet.

**No packageable prediction emerged; the prediction-package interrupt does
not fire; no PP3 candidate file is created.** This is the honest outcome the
spec's forbidden_shortcut anticipates: the audit is data hygiene, not a
prediction generator.

## 7. Five-lens council pass (inline, one worker)

**Cosmologist.** The full-tail re-solve is the right closure of the H46C
chain: the one legitimate worry left in that pipeline was bookkeeping in the
z > 30 tail, and R-B removes it at the component level (radiation in both
H^2 and the friction). The 3e-5 tail shift settles it; with SNe still
unintegrated the only remaining data-side hardening is a second BAO dataset,
and both are monitor events, not audit gaps. The band scan closes H46C's own
named residual. Nothing in the data-facing chain is now argued rather than
computed.

**Spectral geometer.** The audit keeps the geometry honest: M^2 enters only
as the root-system band, and the two genuinely geometric statements — the
ratio-only scale structure and the B.5 cut-scale slot — are kept strictly
separated from the fit quantities f0, B_i. The right reading of E11 is that
the calibration functor is the identity on the geometry's scale content:
GU contributes a shape deformation (a ratio), the data contribute the point.
The 1e-123 question lives entirely in the B.5 slot and this audit correctly
refuses to pretend otherwise.

**Effective-field-theorist.** The two-component model is a consistent IR
truncation and its one free amplitude is now boxed: every CMB-consistent
realization is an LCDM mimic (|w0 + 1| < 0.04 canonical). The EFT-side
caution stands: Z_theta, xi_eff, and the scalar-block mixing are still never
emitted (CH-COSMO items 3-5), so even the surviving mimic band is
conditional on an action that does not yet exist. That conditionality is
correctly carried by the channel card, not this audit.

**Data-confrontation skeptic.** The two prior DE sign numbers came from a
bug, so I checked the recomputation discipline first: the 4.2-class
coefficient and C = 1.39 are recomputed fresh, the probe's blindness is
EXECUTED (F1 perturbs the data and the calibration provably cannot see it),
and the meV bracket is defined after the calibration outputs freeze. The
reproduction of W129's M^2 = 3 number (+5.23 vs +5.25) by an independent
implementation is the strongest single credibility datum in this run. One
residual: the ratio correction divides out shared systematics against an
LCDM control — if both pipelines shared a physics error (not a numerics
error), the ratio would hide it; the PC1/PC2 controls bound but do not
eliminate that class.

**Buildability engineer.** The probe is self-contained (numpy + stdlib
physics; repo imports only for seed verification), deterministic, ~90 s,
exit-code-gated, and every prior-value comparison is a tolerance-tagged
assertion rather than prose. The item is now mechanically closable: the
spec's switch_condition ("close after one complete normalization and
likelihood audit") is satisfied by this run plus receipt. Recommendation to
the daily steward (Lane A, not executed here): reconcile DE-AMP-DIAGNOSTIC
to its closed/monitor disposition, with reopen triggers = new official BAO
release (monitor), SNe integration, or a source-side derivation of f0.

## 8. Consistency with existing gates and explorations

- `process_gates/de_amp_diagnostic_closure_audit.py`: untouched and
  unbroken (it audits the 2026-07-15 evidence chain; this run adds new files
  only). No contradiction: this run agrees the bounded diagnostic is
  complete and executes the one remaining spec swing.
- H46C / W129 / DE-05 / DE-06: independently REPRODUCED, not contradicted
  (table in Section 2; band numbers in Section 4).
- `process_gates/mission_a_lambda_dark_energy_provenance_audit.py` and
  `process_gates/cycle3_dark_energy_predictive_sign_coupling_audit.py`:
  structural audits of historical June explorations; nothing here edits
  those artifacts. Substantively, this audit is consistent with their core
  demands (no fitted xi_eff, no bare-Lambda promotion, anti-fitting
  discipline, no "GU predicts dark energy" claim). The cycle3 artifact's
  historical "w_a > 0" language was already corrected by DARK-ENERGY-03 and
  is not relied on here.
- PP1 (`explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md`):
  consistent; this run supplies its first live read (untriggered,
  orientation-silent) without touching the packet.
- The one deliberate difference from prior work: bb-p1's cross-check values
  (C = 1.438, d ln rho = 4.307) were computed on a pure-LCDM background;
  this audit's backreacted-background values (C = 1.39-1.40, 4.202) sit
  closer to the canon and archaeology numbers. Recorded as a convention
  spread, not a discrepancy — none of these quantities is load-bearing for
  any verdict.

## 9. Honest limits

1. SNe remain unintegrated (named residual since H46C; adding SNe at
   H0_GU = 63.75 can only worsen GU, so the closure direction is safe).
2. Single BAO dataset (DESI DR2); a second dataset is robustness, not a gap
   in this audit's bounded question.
3. The A2 neutrino-as-matter approximation is shared and ratio-corrected;
   residual second order.
4. M^2 = 8 canonical stays reconstruction-grade (OQ2 as "which eigenvalue"
   open, no longer gating, per DE-06).
5. Everything here is exploration tier. Verdict on
   `canon/theta-field-flrw-dark-energy-eos.md` stays OPEN; no claim status,
   canon, register, scorecard, or public posture moves in this run.

## 10. Boundary

New files only (`explorations/de-amplitude-audit-2026-07-20.md`,
`tests/channel-swings/de_amplitude_audit_probe.py`); no existing file
edited; nothing committed by this run; nothing external. The steward
closure recommendation in Section 7 is a proposal for Lane A, not an
executed portfolio change. Did this create a packageable prediction? No —
adjudicated against the standing rule in Section 6.
