---
title: "Deflation false-negative audit (active/exploration tier)"
status: process
doc_type: audit
created: 2026-07-03
scope: "OBJ-DEFLATE meta-audit, active/exploration tier. Sample recent OPEN-downgrades / verdict-deflations / KILLs and test whether any live lead was buried when the evidence only supported 'narrowed', not 'dead'. Report only — no status flips, no re-opens."
method: "Read the concentrated deflation registers (objection-triage-register, triage-pass-2026-06-30) plus the CORRECTION stream in DERIVATION-PROGRESS, then read the source exploration files behind the load-bearing kills to judge each against the evidence actually presented."
---

# Deflation false-negative audit — 2026-07-03

Extends the canon-tier audit (2026-07-03, which found the repo tends to OVER-deflate) to the
active/exploration tier. Question: did any recent KILL / downgrade bury a lead the evidence only
NARROWED?

## 1. Sampled deflation decisions

| # | Claim / lead | Where | Kill / deflation rationale | Verdict | Decisive re-test (if RE-OPEN) |
|---|---|---|---|---|---|
| 1 | Time-as-finality crosswalk (OBJ-TAF) is a dead lane | `lab/roadmap/objection-triage-register.md`; `triage-pass-...-2026-06-30.md` | 55 files, only computed nulls; "every object reduces to Čech / rate-independent restatement / record-audit"; verifier-flipped PARK→KILL | **RE-OPEN-CANDIDATE (narrow)** | The KILL is right for the observer-finality / issuance-rate crosswalk (genuinely rate-independent, `rate-independence-negative-finding`). But the lane BUNDLES a GU-native live residual — the shiab-selector 3-dim question (`observer-selector-leftover-space-2026-06-26.md`, coords channel-mix / chiral-block-tie / scale on GU's OWN 4-real-dim shiab family). Re-test: run `tests/shiab_family_basis.py` + a forgetful-channel-style check asking whether ANY crosswalk-proposed selector imposes a real constraint on the 3 free coords, NO TaF/TI import. Its "forgetful leg" already failed; if the other legs also impose nothing, the kill is confirmed for the residual too. |
| 2 | Sorkin causal-set chirality route (PERSONA-H) | `triage-pass-...-2026-06-30.md`; `explorations/sorkin-causal-set/...axis-note.md` | One-paragraph closure: spatial reflection is an order-preserving Lorentzian isometry ⇒ mirror sprinklings are order-isomorphic ⇒ no isomorphism-invariant can be chirality-sensitive. Flipped PURSUE→PARK | **CORRECTLY-KILLED** (argument is sound; hits the note's own failure-mode 1; PARK is if anything lenient — the argument would justify KILL) | — |
| 3 | Seiberg-Witten source action can make a chiral generation count (MOVE-5) | `canon/source-action-seiberg-witten-RESULTS.md`; CORRECTION 5-01 | Net chiral index of the moment-map image is EXACTLY 0, Ψ-independent across 400 samples, 3 agreeing measures, forced by a verified-unitary chirality-swap; verdict stays OPEN | **CORRECTLY-KILLED** (for the assumed SW template only; guardrail explicitly does NOT touch GU's own source action) | — but flag: the triage cluster-A gloss ("covers the entire Krein class INCLUDING the true one") over-generalizes past the file's own guardrail. Watch, don't re-open. |
| 4 | 3 generations via `ind_H(D_RS)=8` / `rank_H=4` | DERIVATION-PROGRESS CORRECTIONs FC4-HOLONOMY-01, GEN-03, GEN-04, CANON-2 | rank 4 obtained by dividing target index 8 by Â(K3)=2 → circular; downgraded CONDITIONALLY_RESOLVED→OPEN | **CORRECTLY-KILLED** (the overclaim only; lead preserved as OPEN and named the strongest publishable object). Not a false negative. | — |
| 5 | theta-field dark energy is a clean falsification vs DESI (`w_a>0`) | `canon/theta-field-flrw-dark-energy-eos.md`; CORRECTION DARK-ENERGY-02 then -03 | -02 demoted to OPEN reading `w_a>0` as a standing falsification red-flag; -03 (2026-06-30) RETRACTED that as a local-derivative / fit-window artifact (global CPL fit gives `w_a=-0.25`, DESI sign) | **CORRECTLY-KILLED, self-caught** | — DARK-ENERGY-02 was itself a transient OVER-deflation (read narrowing as falsification); the loop corrected it in days. Calibration signal, not an open false-negative. |
| 6 | Schwarzschild Willmore residual falsifies solar-system (`O(M/r^3)`) | `canon/schwarzschild-weak-field-rfail.md`; CORRECTION RFAIL-02 then RFAIL-03 | -02 raised an `O(M/r^3)` falsifying red-flag (down to OPEN); -03 (2026-06-30) showed the linear-in-M residual is IDENTICALLY ZERO — BOTH order estimates were artifacts | **CORRECTLY-KILLED, self-caught** | — Same shape as #5: a transient false-falsification, self-corrected. Verdict stayed OPEN throughout. |
| 7 | Freed-Hopkins observer pairing is a closed GENUINE_OBSTRUCTION | `canon/no-go-class-relative-map.md`; CORRECTIONs FH-01, XOBS-IC4-01 | Obstruction rested on a same-session CONDITIONALLY_SUPPORTED IC4 input; downgraded GENUINE_OBSTRUCTION → CONDITIONALLY_RESOLVED / lane-narrowed | **CORRECTLY handled** (this DEFLATES an obstruction claim, i.e. keeps a lead alive; explicit reopen trigger recorded) | — anti-over-deflation, not a false negative |
| 8 | Y14 spin structure is unconditional | `canon/w2-y14-spin-structure.md`; CORRECTION W2-01 | Unconditional claim FALSE; Y14 spin iff X4 spin; X4-spin precondition STANDS | **CORRECTLY-KILLED** (the overclaim; conditional lead preserved) | — |
| 9 | Stochastic parity-breaking substrate (PERSONA-M) | `triage-pass-...-2026-06-30.md` | "analogy only, zero derived parity" — but explicitly NOT killed because a cheap GFF even-d Bochner closure exists | **CORRECTLY handled** (declined to KILL where a cheap closure survives) | — anti-over-deflation discipline working |
| 10 | BvN wall / C_MPR adjunction (OBJ-CMPR) | register; `triage-pass` | Denies an adjunction whose codomain `C_GW` is never defined → not a proposition; demoted, upgrade parked | **CORRECTLY-KILLED** (ill-posed as stated); define-or-demote path preserved | — |
| 11 | Automated loop is converging (OBJ-CONVERGE) | register; `triage-pass` | Rising issue counts, same-day no-op churn → thrashing; KILLed as a research lane (spawns an ops action) | **CORRECTLY-KILLED** (process lane, not a math lead) | — |
| 12 | Located-not-forced Thm-1 enumeration / antilinear leg | DERIVATION-PROGRESS ENTRY WC-ENUM-COMPLETENESS, WC-ANTILINEAR-BOUND (2026-07-02) | Adversarial kill attempts run; "failure condition did NOT fire"; leads UPGRADED, not killed | **Not a deflation — leads SURVIVED** | — included as a control: the loop does let leads live when the kill attempt fails |

## 2. Count

- **RE-OPEN candidates: 1** (item 1, narrow — the GU-native shiab-selector residual bundled inside the OBJ-TAF KILL).
- **1 watch/UNSURE** (item 3 — MOVE-5 framing over-generalizes past its own guardrail, but the killed object is correctly killed; do not re-open).
- Everything else sampled was **correctly killed** (mostly overclaims / red-flags, lead preserved at OPEN) or **correctly kept alive**.

## 3. Calibration read

The active-tier deflation discipline is **well-calibrated, trending slightly LENIENT — not too aggressive at
the individual-claim level.** Evidence:

1. **Downgrades preserve leads.** The dominant move is CONDITIONALLY_RESOLVED / GENUINE_OBSTRUCTION →
   **OPEN**, not KILL (items 4, 7, 8). The strongest lead (generation count) was downgraded and
   simultaneously named the strongest publishable object — the opposite of burial.
2. **The loop self-catches its own over-deflations.** Its real over-deflation failure mode is planting a
   transient FALSE FALSIFICATION red-flag that reads "narrowed" as "dead" (DARK-ENERGY-02, RFAIL-02) — and
   it reliably RETRACTED both within days (DARK-ENERGY-03, RFAIL-03), verdict held at OPEN throughout. This
   is exactly the OVER-deflation the canon-tier audit flagged, but at the active tier it is transient and
   self-correcting, not sticky.
3. **It declines to KILL when a cheap closure survives** (PERSONA-M) and **PARKs rather than KILLs even
   when it has a proof** (Sorkin). That is leniency, not over-aggression.
4. **Where it KILLs, the target is usually a process lane** (OBJ-CONVERGE) **or a genuinely exhausted null
   lane** (OBJ-TAF crosswalk content) **or an ill-posed proposition** (OBJ-CMPR).

**The one residual false-negative risk is at the LANE-AGGREGATION level, not the individual verdict.** A
coarse lane-wide KILL (OBJ-TAF) can sweep a GU-native live sub-lead (the shiab-selector 3-dim residual,
which has its own computable anchor `tests/shiab_family_basis.py` and shares only vocabulary with the null
crosswalk) into a kill it does not individually deserve. The register even fenced this off explicitly ("do
NOT re-open on a source-action trigger the lane doesn't own") — good discipline against import, but the
same fence is what buries a GU-owned residual. Recommendation for Joe (not actioned here): before closing
any multi-file lane by aggregate KILL, run a one-line "does this lane contain a GU-NATIVE computable
sub-question distinct from the null?" check. For OBJ-TAF that sub-question is item 1's re-test.

Net: no evidence of systematic over-killing of live leads at the claim level; the machinery OBJ-DEFLATE
worried about is, if anything, slightly too gentle. The single actionable false-negative is a bundling
artifact, re-testable without any target import.
