---
title: "PP3 prediction package v0.4: three-branch conditional dark-energy shape test"
status: active_research
doc_type: prediction_package
package_id: PP3
version: "0.4"
package_status: FROZEN_CONDITIONAL_THREE_BRANCH_CURVE_FAMILY
frozen_at: "2026-07-22T17:38:45-05:00"
supersedes: explorations/prediction-package-pp3-de-curve-family-v0.3-2026-07-22.md
owner_item: PRED-CANDIDATE-PACKETS
lane_id: "2"
directed_by: "Joe direct chat, 2026-07-22 (prepare, adversarially check, commit, and push everything required before publication approval)"
extends:
  - lab/process/prediction-package-standing-rule.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/de-amplitude-audit-2026-07-20.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/pp3-v0.4-release-hardening-decision-record-2026-07-22.md
runnable:
  - tests/channel-swings/pp3_curve_family_locus_v04.py
receipts:
  - explorations/receipts/pp3-v0.4/pp3-v0.4-locus.csv
  - explorations/receipts/pp3-v0.4/pp3-v0.4-observables.csv
  - explorations/receipts/pp3-v0.4/pp3-v0.4-summary.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# PP3 v0.4: three-branch conditional dark-energy shape test

## Frozen claim

Conditional on the chain below, the tested construction maps the unresolved
program-native mass assignments M²/H0²∈{3,7,8} into three standard-physics
canonical-scalar FLRW curves. The registered prediction is their union,

\[
\Gamma=\Gamma_3\cup\Gamma_7\cup\Gamma_8,
\qquad \Gamma_m(f_0)=(w_0,w_a,w_b,H,D_M/r_d,D_H/r_d),
\]

not one global one-parameter line. Each branch is one-parameter in the fitted
split fraction f0. M² is unresolved and may not be selected after
confrontation. Compatibility with the union is not confirmation of GU.

This packet is exploration tier, CONDITIONAL, and construction-scoped. It
does not promote a canon verdict, claim that GU predicts the dark-energy
amplitude, or claim that a healthy covariant accelerating realization exists.

## Object provenance

- **Program-native assumptions:** the theta-sector identification; the three
  candidate M² assignments; the conditional orientation/sign linkage.
- **Standard-physics truncation:** one real canonical scalar with Zθ>0 plus a
  positive cosmological-constant-like component; flat FLRW; slow-roll initial
  conditions; standard Friedmann/Klein–Gordon evolution.
- **Imported confrontation/calibration:** Planck θ★, r★, r_d, physical matter
  and radiation densities; DESI DR2 BAO for the calibration-reference
  segments; standard CMB/BAO/SN likelihood machinery.
- **Fitted, not predicted:** f0 and the absolute dark-energy scale.

## Frozen projection and emitter

The descriptive CPL image is computed independently of a survey covariance:
x=1-a; z∈[0,2.33]; 512 samples uniform in x; linear least-squares
w(x)=w0+wa x. The curvature coefficient wb is the leading quadratic
coefficient of the residual from that linear fit, so it cannot redefine the
CPL slope. R=wa/(w0+1) and S2=wb/(w0+1). At f0=0 the ratios are reported only
as branchwise limits.

The deterministic emitter is
`tests/channel-swings/pp3_curve_family_locus_v04.py`. It writes the complete
machine-readable locus, H and distance observables, and JSON receipt. Doubling
the solver resolution changes w0 and wa by <5×10⁻⁴, R and S2 by <5×10⁻³, and
distance ratios by <10⁻⁴ relative; the actual maxima are in the JSON receipt.

### Current-calibration reference segments

DESI DR2 plus the frozen own-θ★ calibration supplies branch-dependent
reference limits, not theory limits:

| M² | f0 limit | endpoint w0+1 | endpoint wa | R range on segment | S2 range on segment |
|---:|---:|---:|---:|---:|---:|
| 3 | 0.2076 | 0.08228 | -0.11199 | [-1.3611,-1.3043] | [-0.0428,-0.0130] |
| 7 | 0.0389 | 0.05818 | -0.06187 | [-1.0635,-0.9728] | [-0.1930,-0.1592] |
| 8 | 0.0274 | 0.05169 | -0.04954 | [-0.9584,-0.8573] | [-0.2392,-0.2046] |

The correlations are the prediction. Rectangular global slope/curvature
envelopes are descriptive at best and are not scoring rules.

### Extended shape-registration domain

To keep a current-data ceiling from masquerading as the end of a theoretical
curve, the emitter also registers stress-tested extensions through f0=0.125,
the pre-existing DESI-signal-matching reference for each branch, and 10%
beyond the largest such endpoint: f0≤1.7908, 0.2508, and 0.1914 for M²=3,7,8.
The extension is a declared v0.4 scoring domain, not a theory-derived bound.
Outcomes beyond it are unregistered rather than silently extrapolated.

## Eligible scoring release

A release may score PP3 v0.4 only if it is public after this freeze, provides
machine-readable joint posterior chains or an official joint contour, permits
the fixed PP3 convention to be reproduced or the three native branches to be
refitted, and identifies the likelihood/calibration used. One-dimensional
marginals and quoted central values are exposure accounting only.

Let C₀.₉₉₇₃(D) be the release's 99.73% joint region in the declared
confrontation space. Let T(Γ) denote a branch tube widened only by the frozen
numerical/projection error receipt, never by an arbitrary percentage.

## Decision rule

**Branch D (detected deviation).** Branch D activates only if the same eligible
joint posterior excludes ΛCDM at 99.73%. PP3 v0.4 predicts

\[
C_{0.9973}(D)\cap[T(\Gamma_3)\cup T(\Gamma_7)\cup T(\Gamma_8)]\ne\varnothing.
\]

An intersection is compatibility, not unique attribution or confirmation.

**Branch N (null).** If no deviation is detected, the registered family remains
unfalsified but earns no confirmation. Its nonzero shape remains untested and
the f0→0 corner is observationally indistinguishable from ΛCDM.

## Predeclared failures

- **K1 — inherited sign-chain failure.** Either (a) a robust CPL-proxy phantom
  result at ≥2σ or (b) pointwise w(z)<-1 over a subwindow of z≤2 at ≥3σ kills
  the PP1 conditional sign conjunction inherited here. It does not kill GU in
  general.
- **K2 — registered family-shape failure.** In Branch D, K2 fires when the
  99.73% joint region is disjoint from the union of all three extended branch
  tubes, profiling over M² and f0. This kills this canonical-scalar FLRW theta
  shape realization. The old 35%-widened ratio cut is retired.
- **K3 — own-calibration closure failure.** K3 fires when the joint region
  intersects an extended branch tube but is disjoint from the union of all
  three current-calibration segment tubes. It kills the conjunction of shape,
  own-θ★ calibration, and frozen DR2 compatibility segment, not the family
  shape alone. If both unions are disjoint, K2 is the substantive failure.
- **K4 — source-linkage consistency failure.** If a future source action
  determines f0 without confrontation tuning and its branch misses the
  measured point, the claimed source linkage fails. This is structural, not a
  fourth numeric threshold.

Residual direction is diagnostic evidence; it does not uniquely identify
which chain link failed.

## Minimum condition chain

1. The cosmological dark-energy sector is the GU theta magnitude sector plus
   a positive cosmological-constant-like component.
2. The pullback is one real canonical scalar mode with Zθ>0, not spin-2;
   scalar-block mixing is discharged; nonminimal, higher-derivative, and
   nonlocal terms do not change the tested quadratic evolution.
3. A causal, stable, accelerating covariant realization exists whose FLRW
   reduction is this truncation. This remains open; failure blocks the shape.
4. Flat Friedmann closure, positive total DE density, exact-budget radiation,
   slow-roll-attractor initial conditions, and the frozen projection apply.
5. M²/H0² belongs to the unresolved data-blind set {3,7,8}; no branch is
   selected after confrontation.
6. f0≥0 remains fitted. A future source action must determine it without
   post-hoc tuning; v0.4 does not claim GU computes f0 or the absolute scale.
7. Own-θ★ is the declared calibration fork for K3; K1 inherits PP1's exact
   sign chain; scoring obeys the eligibility rule above.

## Existing evidence and prospective posture

DESI DR2 predates v0.4 and was consumed in defining the calibration-scoped
reference segments. It earns no prospective confirmation credit and is never
rescored as a post-freeze pass or kill. It remains scientifically relevant
adverse evidence. At exploration grade, the three-branch CPL projection misses
the DR2 region globally by about 3.2σ. In native BAO-distance space the theta
shape remains viable when amplitude is marginalized, but that fit has no
realization under the packet's own CMB calibration; own-θ★ closure produces
the recorded calibration tension. v0.4 prospectively registers whether an
independent post-DR2 joint posterior reproduces, strengthens, or reverses it.

Amplitude ledger: A_Planck=30.2577; own-θ★ A_GU=31.9715 (+5.66% relative to
Planck); under that pinning A_GU overshoots the BAO-preferred A*=31.4709
(σ_A=0.0872) by +5.74σ with ΔAIC=+35.79. With amplitude marginalized, the
best-fit A*=30.8059 (+1.81% relative to Planck), and f0=0.125 lies inside the
Δχ²≤1 interval [0.040,0.150]. These are distinct comparisons.

## Boundary and supersession discipline

This packet narrows exactly what can be killed: the tested theta identification
and standard-physics realization, not all GU, generic thawing, or every possible
dark-energy construction. A source derivation may distinguish among the three
assumed mass assignments only within this truncation.

v0.4 materially supersedes v0.3 because the branch domains, projection,
curvature grid, and K2/K3 rules changed after adversarial audit. v0.3 remains
sealed except for its superseded-by header. Any future numeric or scoring-rule
change requires another superseding version with reasons.

## Receipt

Emitter headline at freeze: `4 [E] + 1 [V]; setup [T]=1; ALL PASS`.
Resolution maxima: Δw0=2.91×10⁻⁶, Δwa=7.23×10⁻⁶, ΔR=2.76×10⁻⁵,
ΔS2=5.75×10⁻⁶, relative Δ(D_M/r_d)=1.83×10⁻⁵, and relative
Δ(D_H/r_d)=1.86×10⁻⁵. No likelihood is evaluated by the emitter.
