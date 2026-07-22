---
title: "PP3 v0.3 — STAGED disclosure-and-currency supersession (awaiting Joe's re-freeze; NOT frozen, NOT posted)"
status: STAGED_UNFROZEN_AWAITING_JOE_REFREEZE
doc_type: prediction-package-supersession
created: 2026-07-22
supersedes: explorations/prediction-package-pp3-de-curve-family-2026-07-20.md  # v0.2, FROZEN 2026-07-20T06:48:12-05:00
freeze_commits_v0.2: [a833d98 (v0.1 freeze), 2da1c73 (v0.2 additive S2)]
repo_head_at_gather: e620ff0
reason: >-
  uncontestability-audit-pp3-packet-2026-07-21 (S1): the frozen v0.2 SOURCE packet's DESI-DR2 disclosure
  lags its own VERIFICATION.md / W113 — it states the DR2 exclusion of f0=0.125 as a plain data fact,
  when it is calibration-scoped (viable under amplitude marginalization). Bounded reconciliation only.
scope: >-
  WORDING / DISCLOSURE / BASIS-CURRENCY ONLY. Every frozen locus / band / segment / curvature / kill
  NUMBER is PRESERVED. Two number-ADJACENT items are FLAGGED for Joe, NOT changed.
governance: STAGED for Joe's re-freeze. Not frozen, not posted. Only Joe approves the superseding freeze.
---

# PP3 v0.3 — staged supersession (for Joe's re-freeze)

**Do not treat as frozen or postable.** This stages the exact wording changes to (i) reconcile the frozen
v0.2 disclosure with VERIFICATION.md / W113 and (ii) bring the basis current. **Zero frozen physics
numbers change.** Number-invariance verified: the emitter `tests/channel-swings/pp3_curve_family_locus.py`
was re-run — exit 0, headline `7 [E] + 1 [F] = 8`, frozen locus table reproduced cell-for-cell.

## A. Frozen numbers — PRESERVED (number-invariance evidence)
One-parameter thawing DE locus through `(w0,wa)=(-1,0)`, parameter = split fraction `f0`; non-phantom
`w0+1>0`, `w(z)≥-1` pointwise. **All values below unchanged from v0.2** (emitter-reproduced today):

| f0 | w0+1 | wa | wa/(w0+1) | max dev w+1 |
|---|---|---|---|---|
| 0.005 | 0.01082 | -0.01080 | -0.998 | 0.0094 |
| 0.010 | 0.02121 | -0.02150 | -1.013 | 0.0183 |
| 0.015 | 0.03122 | -0.03208 | -1.028 | 0.0267 |
| 0.020 | 0.04086 | -0.04253 | -1.041 | 0.0348 |
| 0.027 | 0.05380 | -0.05691 | -1.058 | 0.0456 |
| 0.125 | 0.18943 | -0.22702 | -1.199 | 0.1567 |

Band spots (f0=0.020): M²=3 → (0.01013, -0.01343, R=-1.325); M²=7 → (0.03292, -0.03643, R=-1.107).
Slope invariant `wa/(w0+1) ∈ [-1.33, -1.00]`. Segment bound `w0+1 ≤ 0.054` (image of `f0 ≤ 0.027`).
Curvature invariant `S2 = wb/(w0+1)`: mean -0.170 at M²=8, envelope `[-0.19,-0.02]`, sign-definite negative.
Kills K1 (phantom, ≥3σ), K2 (slope outside `[-1.80,-0.65]`, ≥3σ, 35% tol), K3 (`w0+1>0.06`), K4 (web) —
**all thresholds unchanged.** Grade: exploration tier, R0_COND, CONDITIONAL.

## B. Disclosure reconciliation (the P0 fix — wording only)
**B1 — the DESI DR2 disclosure sentence** (Known-inputs disclosure, first bullet). Replace:
> "The DESI DR2 vector is CONSUMED … (it produced the f0 ≤ 0.027 ceiling and the +5.7σ exclusion of
> f0 = 0.125)…"
with:
> "The DESI DR2 BAO vector (arXiv:2503.14738) is CONSUMED in this packet's construction. Under the
> packet's OWN-θ\* (CMB-anchored) distance calibration — condition-chain link 4 — it produced the
> `f0 ≤ 0.027` ceiling (image `w0+1 ≤ 0.054`) and the +5.7σ overshoot of the canonical `f0 = 0.125`
> amplitude. This ceiling is CALIBRATION-SCOPED, not a calibration-independent property of DR2: under
> amplitude marginalization the same DR2 BAO likelihood is consistent with f0 up to ~0.15 — canonical
> `f0 = 0.125` included, inside the Δχ²≤1 band (W113) — and the theta-sector shape slightly out-fits
> ΛCDM. The sole residual exclusion lives in one direction, the amplitude-calibration direction (as
> VERIFICATION.md records). Nothing derived from DR2 is claimed as prediction."

**B2 — table-row relabel:** `0.125 (excluded ref)` → `0.125 (canonical ref; off-segment under own
calibration — viable under amplitude marginalization on current DR2, see disclosure)`. **Row values
unchanged.**

**B3 — K3 justification qualifier** (number 0.06 unchanged): replace K3's "the frozen ceiling from data
already in hand" with "the frozen ceiling **under the packet's OWN-calibration (CMB-anchored) closure
(condition link 4; not a calibration-independent DR2 fact)** — a larger detected amplitude read in that
same convention contradicts the family's own likelihood structure: kill, not stretch." K1/K2/K4 stand.

**B4 — two one-phrase touch-ups:** frozen-prediction item 2 → "…the frozen **own-calibration** current-
data ceiling." (Emitter-header caption: see FLAG B.)

**B5 — side-by-side to include:** *Own-θ\* calibration:* f0≤0.027 ceiling, canonical f0=0.125 overshoots
+5.7σ, dAIC=+35.79. *Amplitude-marginalized:* canonical f0=0.125 viable inside Δχ²≤1, basin ~[0.04,0.15],
shape out-fits ΛCDM ~3.3 χ² (~1.3 AIC), profile min f0≈0.10.

## C. Basis-currency additions (post-freeze; NO number change; honest grades)
1. **σ = w₁(L_time) typing** (GU, 2026-07-21): the inherited external sign bit is now typed as the first
   Stiefel–Whitney class of the arrow-of-time line bundle over `F ≃ RP³` (Z/2 = spin cover S³→RP³).
   *Nuance (do not over-propagate):* the "σ = circle-orientation" reading is a class-relative LOCAL
   no-go, not a global impossibility — that reading stays OPEN.
2. **DU source-is-observer strengthening — CONDITIONAL-THEOREM grade.** The DE sign cannot *dynamically*
   flip because any orientation internal to the record dynamics is derivable/disclosed and cannot be the
   becoming-involution; the true σ is the external, underivable, fixpoint-free one the interior can't
   mint (a fully source-internal mint is a Kleene quine). Cite AT this grade: external-by-necessity
   *under the first-person-underivability standard*, Lean-proved on the involution leg only, the literal
   monotonicity bridge refuted; grounds sign externality only, σ's value and the amplitude untouched.
3. **TI/TaF structural support (toy-grade):** the Krein/orientation co-flip identity — `sgn(w0+1)` is the
   single global readout of one external orientation bit — with provenance rule SRC-COH-1 (one Krein
   form per action slot; a relative-sign flip is a hidden external import, not a dynamical process, so a
   dynamical crossing is forbidden); E139 (the de Sitter DE sector is fixed-source disclosure, W4 fails);
   arrow-as-theorem + T19 (the arrow-reversal involution is refuted). All toy-grade/conditional.
4. **Roll-health antecedent disclosure** (aligns PP3 with its own register's CPRED-04 gate): the healthy
   dynamical roll assumed by the *thawing-shape* legs is OPEN in the program's covariant cosmology — the
   strongest local realization is superluminal except at constant-Λ (DU COV-02), scale-free causal-memory
   completions track rather than accelerate (DU CMF-01), and a healthy accelerating roll (COV-03) is
   unbuilt. **Neither failure crosses the phantom divide (all land at w ≥ −1), so both are CONSISTENT
   with — even corroborate — the non-phantom prediction.** This gates the *shape*, not the *sign*; the
   sign leg is roll-health-independent.
5. **Honest qualifiers:** the C.3 support is toy-grade/conditional (bar-b OPEN, not a TI physical
   candidate); the arrow↔DE-sign welding is tight only under zero-import operations — separating them
   costs "one extra Z/2," itself an external import (NOT a dynamical-crossing route); the cross-repo
   GU=TaF=TI orientation identity is leg-deep, not mechanism-deep (conjectural bridge, not proven); the
   finality→*physical*-arrow grounding is conditional (physical source gates OPEN).
6. **Units-guard:** any Λ/rate sentence must compare rate²-to-rate² (Λ vs `λ_max²`/`Γ_min²`), never Λ vs
   a raw rate.

## D. Semantic diff summary
Wording / disclosure / basis-currency ONLY. **Zero frozen physics numbers changed.** The prediction is
unchanged; its honesty envelope is TIGHTENED (accurate DESI framing) and its basis STRENGTHENED
(source-is-observer + co-flip) and honestly GATED (roll-health). Number-invariance: emitter exit 0,
table reproduced. Source hashes: v0.2 = a833d98 + 2da1c73; HEAD e620ff0.

## E. TWO number-adjacent FLAGS — for Joe's re-freeze decision (surfaced, NOT changed)
**FLAG A — amplitude-percentage attribution (substantive precision).** Three amplitudes circulate:
Planck `A_CMB=30.258`; amplitude-marginalized data-preferred `A*=30.806 = +1.81% above Planck` (W113);
GU own-θ\* `A_GU=31.9715 = +5.66% above Planck` (DE amplitude audit). VERIFICATION.md attributes the
"+1.81%" (data-preferred-vs-Planck), while the manuscript attaches "+1.8%" to the own-θ\* calibration —
but the own-calibration figure is +5.66%. **These describe different quantities and the docs don't phrase
the referent identically.** NOT a frozen PP3 number; a numeric-attribution choice for you to settle so
PP3 / VERIFICATION.md / W113 / manuscript state one amplitude story. Either framing leaves every frozen
locus/kill number untouched.

**FLAG B — stale receipt count (housekeeping).** The frozen v0.2 quotes the emitter headline as
`6 [E] + 1 [F] = 7` in two places; the current emitter and the v0.2 changelog both give `7 [E] + 1 [F]
= 8` (locus table reproduces exactly). Correcting it makes the packet self-consistent with its own
emitter — but it changes a *stated value*, so it's your call, not a silent fix.

## Re-freeze decision (yours)
Options: (1) approve v0.3 as staged (B disclosure fix + C basis-currency; all numbers preserved) →
re-freeze; (2) same, plus a ruling on FLAG A (which amplitude attribution is canonical) and FLAG B
(correct the receipt count); (3) discuss any item. Nothing is frozen or posted until you decide.

## Boundary
STAGED, unfrozen, unposted. Only Joe approves the superseding freeze. Return channel per the
supersession-prep note: `mailboxes/drafting-factory/`.
