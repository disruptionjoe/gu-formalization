---
title: "Objection Triage Register (3-Pass Analysis)"
status: active_research
doc_type: roadmap
created: 2026-06-24
updated_at: "2026-06-30"
---

# Objection Triage Register (3-Pass Analysis)

## Purpose

This register is the durable home for every objection, weakness, and "is-this-pathway-worth-it"
question surfaced by the 2026-06-24 three-pass repo assessment (neutral synthesis, then a heterodox
reading, then an orthodox reading). Its job is **capture**, so nothing is lost.

Two layers, on purpose:

- **This register** holds the *viability* question for each lane: should we enter it at all, and
  what is the smallest falsifiable first artifact? Each item carries a `viability` field
  (`UNTRIAGED | PURSUE | PARK | KILL`).
- **`NEXT-STEPS.md`** holds the *compute task* once a lane is greenlit, so the
  `gu-research-loop` workflow can pick it up. Each item below has a matching OPEN row in
  `NEXT-STEPS.md` under "Objection Triage Register (3-Pass Analysis, 2026-06-24)".

These are not mirrors. The register decides whether to pursue; `NEXT-STEPS.md` tracks the bounded
work once we do.

## How to use

1. A one-time triage pass assigns each `UNTRIAGED` item a `viability` verdict plus a
   `decisive_first_test`. The triage applies the repo's own `verdict-inflation` and
   `UNDISMISSED-CANDIDATE` lenses so "worth pursuing" cannot itself be inflated.
2. `PURSUE` → its `NEXT-STEPS.md` row stays OPEN and becomes loop-eligible.
3. `PARK` → record an explicit wake trigger so it cannot silently resurface or be lost.
4. `KILL` → archive with the killing reason recorded.

No item exits this register without a recorded disposition.

## Status legend

- `viability`: `UNTRIAGED` (default until the triage pass runs) | `PURSUE` | `PARK` | `KILL`
- Items are ordered: cross-cutting load-bearing first, then per-lane (neutral), orthodox,
  heterodox, meta.

---

## Triage results (2026-06-30)

The one-time triage pass ran on 2026-06-30 (full method + 0-5 scores in
`lab/roadmap/triage-pass-underexplored-movable-objections-2026-06-30.md`). Every item now carries a
`viability` disposition below.

| id | viability | disposition |
|---|---|---|
| OBJ-GEN | PARK | Strongest publishable object (2-primary / prime-sieve firewall) but the decisive gate OQ-RK1 is blocked on the unbuilt source-derived RS index operator. |
| OBJ-CMPR | PARK | Only the demotion is earned; the define-or-demote upgrade is source-action-gated. |
| OBJ-TAF | KILL | 55 files, only computed nulls; every object reduces to Čech / rate-independent restatement. Closed with the null finding as the kill artifact. |
| OBJ-HETSUB | PARK | Rollup of the heterodox-substrate lanes; no substrate derives SM chirality; specialist-gated, no falsifiable first artifact. |
| OBJ-FHOBS | PARK | K3 moduli topology done; GU verdict gated on the unverified IC4 reduction. Wake = IC4/K3 topology fixed. |
| OBJ-VZ | PARK | Symbol-level, source-conditional; cheapest next step is one canonical typed D_GU definition. |
| OBJ-FALSIFY | PARK | Census complete and honestly negative; no independent artifact runnable now. |
| OBJ-DESI | PARK | Duplicate physics object of MOVE-2; resolved 2026-06-30 (w_a<0 under global CPL fit, ΛCDM-degenerate; red-flag retracted, see CORRECTION DARK-ENERGY-03). |
| OBJ-DG | PARK | Correct and cheap but ground-clearing only; discount the crown-jewel framing; wake on a positive result to attach. |
| OBJ-NGUYEN | PURSUE | Real rep-theory kernel; a cheap one-pass fetch of the absent Nguyen PDF de-risks the lane; scrub retracted "dissolves / FULLY CLOSED" wording. |
| OBJ-CONNES | PARK | Reframed to load-bearing only for observer-facing SM-shadow claims; only an un-executed canon wording patch remains. |
| OBJ-DEFLATE | PARK | KILL-adjacent; a spot-check shows recent downgrades warranted; run reactively only. |
| OBJ-CONVERGE | KILL | Loop demonstrably thrashing (rising issue counts; runaway no-op). Closed as a research lane — but the finding must spawn a separate loop-redesign/halt **ops** action, not silently vanish. |

**KILLs actioned:** OBJ-TAF and OBJ-CONVERGE. OBJ-CONVERGE's thrashing finding is flagged for a
loop-redesign/halt ops action (it is not merely a closed research lane).

---

## OBJ-GEN — Three-generation count is OPEN and fitted, not derived

- **Lane:** generation count / `ind_H(D_RS)=8`
- **Origin:** all three passes converge here (the shared load-bearing weak point)
- **Objection:** The headline physics number (3 SM generations via `ind_H(D_GU)=24`) is currently
  *fitted, not derived*. All three analytic routes failed (scalar Flensted-Jensen/BC1 used the
  wrong involution; rank-3 A3 Harish-Chandra gives an empty discrete series because SL(4,R) has
  none; tau-twisted fails on four independent criteria). The surviving APS/K3 route is circular: it
  gets `rank_H(S_RS^+)=4` by dividing the target index 8 by Â(K3)=2.
- **Current repo status:** OPEN (correctly downgraded from "CONDITIONALLY 3" under the
  UNDISMISSED-CANDIDATE rule). See DERIVATION-PROGRESS.md CORRECTIONS FC4-HOLONOMY-01 / GEN-04.
- **Decisive gate:** OQ-RK1 — CAS matrix computation of `rank(Π_RS · E₊ · Π_RS)` in M(64,ℍ) that
  returns 4 or 8 **without** dividing by the target index.
- **Decisive first test:** run OQ-RK1 as a direct Clifford-algebra rank computation; a 4 confirms 3
  generations, an 8 implies 4 generations (Candidate B, still live).
- **Kill / falsification condition:** OQ-RK1 returns a value inconsistent with both 3 and 4
  generations, or proves the rank is not well-defined independent of the physical-DOF input.
- **Recommended destination:** NEXT-STEPS (highest priority — moves every other verdict)
- **viability:** PARK (2026-06-30 triage — decisive gate OQ-RK1 blocked on the unbuilt source action)

## OBJ-CMPR — BvN wall is a naming exercise

- **Lane:** C_MPR / 9-tuple / BvN wall
- **Origin:** neutral
- **Objection:** The BvN wall denies an adjunction whose codomain category `C_GW` is never defined,
  and whose functors L, R are never written — a non-existence claim about an undefined object is not
  a proposition. The 9-tuple is a record schema, not shown to be a complete invariant.
- **Current repo status:** exploration; object/morphism reduct `C_SR` verified as a genuine
  category, but the wall itself remains an open (and currently ill-posed) obligation.
- **Decisive first test:** give `C_GW` an object-level definition (objects + anomaly-free morphisms
  + functors L, R). If it cannot be written down, demote the wall permanently.
- **Kill / falsification condition:** no well-typed `C_GW` exists, or any candidate collapses to the
  commutative subcategory where BvN-1936 already holds trivially.
- **Recommended destination:** NEXT-STEPS (define-or-demote)
- **viability:** PARK (2026-06-30 triage — only the demotion is earned; upgrade is source-action-gated)

## OBJ-TAF — Observer-finality crosswalk has no transport into a GU theorem

- **Lane:** time-as-finality / observer-finality crosswalk
- **Origin:** neutral
- **Objection:** The lane is fenced as a test layer only ("should not be cited as GU canon or as a
  way to evade no-go theorems"). The FR-series confirmed the issuance rate is GU-irrelevant
  (rate-independence negative finding). It keeps producing structural-parallels and nulls.
- **Current repo status:** exploration, explicitly cautioned in RESEARCH-STATUS.md.
- **Decisive first test:** identify one concrete transport from a crosswalk object into a GU theorem
  (not a structural parallel). If none exists, close the lane with a stated reason.
- **Kill / falsification condition:** every crosswalk object reduces to standard Cech cohomology or
  a rate-independent restatement with no GU-side consequence.
- **Recommended destination:** NEXT-STEPS (transport-or-close)
- **viability:** KILL (2026-06-30 triage — closed; 55 files, only computed nulls; null finding is the kill artifact)

## OBJ-HETSUB — Heterodox substrate lanes lack an SM-chirality bridge

- **Lane:** Wolfram/rulial, stochastic parity-breaking, CA irreducibility, decidability
- **Origin:** neutral (lowest in the 15-persona ranking: K=41, M=48, N=44)
- **Objection:** None of the four lanes has a bridge to actual SM chirality; parity-breaking gets
  inserted rather than derived, so the lanes "likely collapse."
- **Current repo status:** exploration; low priority.
- **Decisive first test:** for each of the four sub-lanes, name one falsifiable chirality hook
  (what SM-chirality invariant lives in the substrate and what its smooth shadow loses). Park any
  sub-lane that cannot produce one.
- **Kill / falsification condition:** the parity-breaking / chirality is shown to be hand-inserted
  in every toy model of the lane.
- **Recommended destination:** NEXT-STEPS (hook-or-park, four sub-lanes)
- **viability:** PARK (2026-06-30 triage — specialist-gated; no falsifiable first artifact)

## OBJ-FHOBS — Freed-Hopkins observer-pairing narrowed to one conditional survivor

- **Lane:** observer-pairing anomaly enrichment (Freed-Hopkins Option B)
- **Origin:** neutral / heterodox (the "most profound but fragile extension")
- **Objection:** The non-forgettable-observer search returned a structural no-go (every
  bordism-invariant observer datum either descends through the forgetful functor or is ordinary
  tangential/background data). The lane survives only through `X_obs^sol`, whose closure FH-01
  explicitly refused as same-session verdict inflation on an all-conditional chain.
- **Current repo status:** CONDITIONALLY_RESOLVED / lane-narrowed; NOT a closed obstruction.
- **Decisive first test:** compute the topology of `X_obs^sol = M_RF(K3)` and decide whether its
  KSp⁰ class is non-extendable beyond gauge-field backgrounds.
- **Kill / falsification condition:** `X_obs^sol` is contractible or its class relabels as ordinary
  Sp(64)-gauge background (the relabeling case of the prior no-go).
- **Recommended destination:** NEXT-STEPS (compute-or-park, wake trigger = IC4/K3 topology fixed)
- **viability:** PARK (2026-06-30 triage — gated on the unverified IC4 reduction; wake = IC4/K3 topology fixed)

## OBJ-VZ — Velo-Zwanziger evasion holds only at principal-symbol order

- **Lane:** Velo-Zwanziger fifth-theorem entry
- **Origin:** orthodox
- **Objection:** The evasion holds only at principal-symbol order; the subprincipal order may
  overturn it (FC-VZ-4), and the 14D leg is gated on *unverified* E-block invertibility (FC-VZ-1).
  This is the order-by-order optimism that historically fails for spin-3/2-coupled-to-gauge.
- **Current repo status:** CONDITIONALLY_RESOLVED (4D principal-symbol) / CONDITIONALLY_EVADED (14D).
- **Decisive first test:** do the subprincipal/extrinsic-curvature characteristic computation
  (close FC-VZ-4) and supply a direct Clifford-algebra proof of E-block invertibility (close
  FC-VZ-1).
- **Kill / falsification condition:** the extrinsic curvature `II_s = s*(θ)` sources spacelike
  characteristics at subprincipal order, or E(ξ) is non-invertible on the relevant cone.
- **Recommended destination:** NEXT-STEPS (subprincipal + E-block)
- **viability:** PARK (2026-06-30 triage — source-conditional; cheapest step is one canonical typed D_GU definition)

## OBJ-FALSIFY — The substrate-shadow thesis needs one concrete surviving SM prediction

- **Lane:** central thesis falsifiability
- **Origin:** orthodox
- **Objection:** The "no-goes are shadows of richer substrate invariants" thesis is unfalsifiable
  until *one* concrete, checkable SM consequence survives without an internal-artifact crutch.
- **Current repo status:** thesis is canon-as-posture; no single surviving empirical prediction yet.
- **Decisive first test:** enumerate the candidate single-prediction tests across the repo
  (generation count, dark-energy EOS, anomaly content) and rank by nearness-to-decidable.
- **Kill / falsification condition:** every candidate prediction is either reconstruction-grade,
  IC-sensitive, or assumes its own conclusion.
- **Recommended destination:** NEXT-STEPS (prediction census)
- **viability:** PARK (2026-06-30 triage — census complete and honestly negative; no artifact runnable now)

## OBJ-DESI — Dark-energy w_a sign reversed and IC-sensitive

- **Lane:** theta-field FLRW dark energy EOS
- **Origin:** orthodox (the nearest empirical hook, currently pointing the wrong way)
- **Objection:** Corrected FLRW Klein-Gordon integration reversed the sign to `w_a > 0` (opposite to
  DESI's `w_a = -0.75`), and the sign is initial-condition-sensitive (OQ3-A).
- **Current repo status:** canon, CONDITIONALLY_RESOLVED, with the sign correction logged.
- **Decisive first test:** resolve OQ3-A — derive the physical initial conditions (slow-roll from
  z ≫ z_osc) and determine whether the sign is a genuine prediction or an IC artifact.
- **Kill / falsification condition:** the predicted `w_a` sign is robustly positive under physical
  ICs, contradicting DESI; or `w_a` is not sign-stable, making it non-predictive.
- **Recommended destination:** NEXT-STEPS (OQ3-A IC derivation + OQ5 phi_0 scan)
- **viability:** PARK (2026-06-30 triage — duplicate of MOVE-2; resolved w_a<0/ΛCDM-degenerate, see CORRECTION DARK-ENERGY-03)

## OBJ-DG — Distler-Garibaldi scope-exit (crown jewel to harden)

- **Lane:** Distler-Garibaldi stress case
- **Origin:** heterodox (crown jewel — protect from erosion)
- **Objection (inverted — a strength to defend):** GU was never in Distler-Garibaldi's class (GU
  violates DG-A1/A2/A6/A7; the single-E8-adjoint functor does not exist from GU's construction), so
  the most-cited refutation of GU is a scope error, not a refutation. This needs to be made
  bulletproof and packaged as a standalone result before it can erode.
- **Current repo status:** RESOLVED as scope-exit (no residual on the scope-exit claim); the
  separate generation-count number stays OPEN and is NOT part of this verdict.
- **Decisive first test:** write the standalone exposition "the DG refutation is a category error"
  with the four violated assumptions made explicit and referee-checkable.
- **Kill / falsification condition:** a functor `F_DG: GU_data → DG_E8` is constructed (would
  reopen the scope-exit).
- **Recommended destination:** NEXT-STEPS (harden + paper surface)
- **viability:** PARK (2026-06-30 triage — correct but ground-clearing only; discount the crown-jewel framing)

## OBJ-NGUYEN — shiab dissolves Nguyen §3.1 (crown jewel to harden)

- **Lane:** shiab existence Cl(9,5) vs the Nguyen critique
- **Origin:** heterodox (crown jewel — protect from erosion)
- **Objection (inverted — a strength to defend):** The explicit Cl(9,5)≅M(64,ℍ) shiab construction
  dissolves Nguyen's §3.1 complexification objection. This is one of the strongest closed positive
  results and should be packaged as standalone.
- **Current repo status:** canon, RESOLVED.
- **Decisive first test:** standalone write-up of the construction + the §3.1 dissolution, audited
  against the Nguyen synthesis, ready for external readers.
- **Kill / falsification condition:** a gap is found in the H-linearity or Spin(9,5)-equivariance of
  the Clifford contraction.
- **Recommended destination:** NEXT-STEPS (harden + paper surface)
- **viability:** PURSUE (2026-06-30 triage — cheap one-pass fetch of the absent Nguyen PDF de-risks the lane; scrub retracted wording)

## OBJ-CONNES — Is the finite Connes control case over-elevated?

- **Lane:** Type II1 / spectral SM posture
- **Origin:** heterodox structural critique
- **Objection:** The finite Connes-Chamseddine control case is elevated to a *canon requirement*
  (Canon claim 3), and the J²=−1 (quaternionic) vs +1 (modular) gap is treated as GU's defect to
  patch — when a heterodox reading says GU's quaternionic structure is the point and Connes'
  framework is the limited shadow. Auditing the richer object against the poorer one's rules.
- **Current repo status:** canon posture; treated as load-bearing.
- **Decisive first test:** decide whether "preserve the finite Connes control case" is genuinely
  load-bearing for GU's claims, or an imported constraint that can be relaxed/reframed.
- **Kill / falsification condition:** dropping the Connes-control requirement breaks a result that
  currently depends on it (confirms it is load-bearing, closes the objection).
- **Recommended destination:** NEXT-STEPS (canon-posture audit)
- **viability:** PARK (2026-06-30 triage — load-bearing only for observer-facing SM-shadow claims; canon wording patch pending)

## OBJ-DEFLATE — Is verdict-deflation over-killing live leads?

- **Lane:** research-loop methodology
- **Origin:** heterodox structural critique
- **Objection:** The UNDISMISSED-CANDIDATE / verdict-inflation machinery keeps knocking live leads
  back to OPEN on technicalities; this may be manufacturing false modesty and burning leads (a
  false-negative risk, the mirror of the verdict-inflation risk it guards against).
- **Current repo status:** the deflation machinery is active and (by design) aggressive.
- **Decisive first test:** false-negative audit — sample recent OPEN downgrades and check whether
  any was too aggressive relative to the actual proof state.
- **Kill / falsification condition:** the audit finds every downgrade was warranted (closes the
  objection); or finds systematic over-deflation (opens a calibration fix).
- **Recommended destination:** NEXT-STEPS (loop calibration audit)
- **viability:** PARK (2026-06-30 triage — KILL-adjacent; spot-check shows recent downgrades warranted; run reactively only)

## OBJ-CONVERGE — Is the automated loop converging or thrashing?

- **Lane:** research-loop methodology (meta)
- **Origin:** meta
- **Objection:** Heavy reliance on automated parallel-agent passes plus aggressive self-correction
  may be generating churn (file proliferation, repeated downgrades). Is the loop converging on
  resolved results or thrashing?
- **Current repo status:** loop running daily; `lab/process/loop-adversarial-log.md` accumulates run
  summaries.
- **Decisive first test:** define and compute a convergence read over the adversarial log (net
  RESOLVED gain per run, downgrade/upgrade churn ratio, repeat-item rate).
- **Kill / falsification condition:** the metric shows steady net progress (closes the objection) or
  shows thrashing (opens a loop-redesign task).
- **Recommended destination:** NEXT-STEPS (convergence metric)
- **viability:** KILL (2026-06-30 triage — loop demonstrably thrashing; closed as a research lane; spawns a separate loop-redesign/halt ops action)

---

## Provenance

Source: 2026-06-24 three-pass repo assessment (neutral synthesis → heterodox reading → orthodox
reading) conducted in conversation with Joe. The strongest pathway out at assessment time was the
signed-readout boundary theorem (only finished self-contained theorem); the three viewpoints
disagreed on strongest/weakest by design, and all three converged on OBJ-GEN as the load-bearing
weak point.
