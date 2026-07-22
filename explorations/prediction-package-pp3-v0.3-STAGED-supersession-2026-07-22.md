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
v0.2 disclosure with VERIFICATION.md / W113, (ii) bring the basis current, and (iii) resolve the two
number-adjacent flags per the Science Council (grounded in GU's Purpose/Passion/Practice; Joe-approved
direction). **Zero frozen physics numbers change.** Cross-modal reproduction (independent, 2026-07-22):
emitter `pp3_curve_family_locus.py` exit 0, headline `7 [E] + 1 [F] = 8`, frozen locus table reproduced
cell-for-cell; `W113_world_contact.py` amplitude legs reproduced; `de_amplitude_audit_probe.py` amplitude
ledger + σ/dAIC reproduced (numbers in §E). Decision trail: see §H.

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

## E. Flag resolutions (Science Council verdict, Joe-approved direction; numbers verified 2026-07-22)

**FLAG A — resolved by disambiguation, not selection: the conditional, fiducial-anchored amplitude
ledger.** The confusion was a floating referent — there are TWO distinct data-preferred amplitudes, and
three distinct "%", cross-wired across PP3 / VERIFICATION.md / W113 / manuscript. Canonical ledger (each
number carries value + baseline + source-test; independently reproduced today):

| Quantity | Value | Referent | Source-test |
|---|---|---|---|
| `A_Planck` (CMB baseline) | 30.2577 | — (import) | f0→0 limit → 30.2577 |
| `A_GU` (own-θ\* pinned prediction) | 31.9715 | **+5.66% vs Planck** | `de_amplitude_audit_probe.py` |
| BAO-preferred (own-θ\* confrontation) | `A*` = 31.4709 (σ_A=0.0872) | A_GU overshoots by **+5.74σ**, dAIC **+35.79** → amplitude leg disfavored/closed | `de_amplitude_audit_probe.py` |
| Amplitude-marginalized (shape viability) | `A*` = 30.8059 | **+1.81% vs Planck**, inside Δχ²≤1 (f0∈[0.040,0.150], canonical f0=0.125 included); pinning A→Planck costs +41.3 χ² | `W113_world_contact.py` |

- **Reporting rule:** lead with the **σ-tension (own-θ\* confrontation, +5.74σ) and dAIC (+35.79)**; demote
  every bare "%" to a parenthetical carrying its baseline. **State the σ-tension as CONDITIONAL on the
  own-θ\* pinning (condition-chain link 4)** — it is the residual of a *pinned* prediction against
  *marginalized* data, not a calibration-independent fact. The two `A*` (31.4709 confrontation vs 30.8059
  marginalized) are DISTINCT references and must never be collapsed.
- **Why this fits GU's charter:** Flag A is the program's own **forced-vs-imported distinction** turned on
  its own numbers — what the own-θ\* convention *imports* (a calibration knob) vs what the data *force*
  (the marginalized preference). Reporting them with one referent would commit, on the load-bearing
  falsifiable, the exact conflation the program exists to expose.

**FLAG B — resolved: correct to the emitter.** Emitter headline `6 [E] + 1 [F] = 7` (stale in frozen v0.2,
two places) → **`7 [E] + 1 [F] = 8`** (current emitter verified today; locus table reproduced exactly). Plus
a standing *regenerate-don't-transcribe* guard so the quoted receipt is regenerated from the emitter and
cannot drift again.

## F. Amendment ledger (progressive — manipulability-reducing, before→after + certification)
Every touched stated value, logged as a dated amendment (v0.2 stays sealed on disk; v0.3 is a new file):

| # | Item | Before (v0.2) | After (v0.3) | Kind |
|---|---|---|---|---|
| 1 | DESI DR2 disclosure sentence | "+5.7σ exclusion of f0=0.125" as a plain data fact | calibration-scoped (own-θ\*); viable under amplitude marginalization | wording |
| 2 | Table row f0=0.125 | "excluded ref" | "canonical ref; off-segment under own calibration; viable under amp-marg" | wording |
| 3 | K3 justification | "ceiling from data already in hand" | "ceiling under own-calibration closure (link 4)" | wording |
| 4 | Frozen-prediction item 2 | "current-data ceiling" | "own-calibration current-data ceiling" | wording |
| 5 | Emitter receipt headline | `6 [E]+1 [F]=7` | `7 [E]+1 [F]=8` | **stated value (Flag B)** |
| 6 | Amplitude story | one "%" cross-wired | 4-quantity ledger (§E) | **precision/attribution (Flag A)** |

- **Reason (causal, so it reads as honesty-tightening not outcome-motivation):** the amplitude referents
  were cross-wired (two distinct `A*`, three distinct "%"); the receipt count drifted post-freeze when the
  emitter gained a check. Both corrections REDUCE manipulability.
- **Certification:** **no locus / band / segment / curvature / kill (K1–K4) number changed.** Independently
  reproduced 2026-07-22 (emitter exit 0 + table cell-for-cell; W113 legs; DE-audit ledger + σ/dAIC). The
  bet is untouched; the corrections tighten the prose and bookkeeping around it.

## G. Excluded from this freeze (future work — do NOT inject into v0.3)
The amplitude residual `A_GU − A*` (the +5.66%-vs-Planck / +5.74σ-vs-BAO-preferred gap) is a candidate
**future Lane-2 native prediction** (DR3-testable) — the "confusion" points at a real, nameable quantity.
Recorded as a seed here per the byproduct-feeds-North-Star discipline; it is **not** part of v0.3's frozen
content and must not enter until separately built and pre-declared.

## H. Decision provenance (audit trail)
`explorations/pp3-v0.3-reporting-decision-record-2026-07-22.md` — the full trail: the two flags, the
10-persona pass, the Science Council (registered; grounded in GU Purpose/Passion/Practice), the explicit
aggregation verdict, and the cross-modal reproduction that fixed the ledger. Plus the returned gathers and
the source-hash / freeze lineage above.

## Freeze-readiness (yours to act on)
Flags resolved, basis current, numbers independently reproduced, amendment discipline logged — **v0.3 is
freeze-READY for your re-freeze.** One non-blocking follow-on: propagate the §E canonical ledger to
`VERIFICATION.md` and the manuscript so all four docs tell one amplitude story (PP3's own content is
internally correct without it). Nothing is frozen or posted until you re-freeze.

## Boundary
STAGED, unfrozen, unposted. Only Joe approves the superseding freeze. Return channel per the
supersession-prep note: `mailboxes/drafting-factory/`.
