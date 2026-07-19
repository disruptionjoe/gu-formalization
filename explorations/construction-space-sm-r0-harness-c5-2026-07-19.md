---
title: "Construction-space SM R0 harness for C5"
status: exploration
doc_type: construction_space_probe
created: 2026-07-19
run_id: RUN-20260719-534-repository-work-cycle-cai-hourly
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
probe: P2-SM-R0-HARNESS-C5
test: tests/recovery-contract/construction_space_sm_r0_c5_harness.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Construction-space SM R0 harness for C5

Operational result: `P2 harness complete`.

This probe built the reusable Rung 0 Standard Model constraint checker requested
by council round 2 for `C5-NATIVE-QUOTIENT-SELECTOR`.

It does not change claim status, canon verdicts, public posture, paper state, or
the Standard Model recovery verdict. It only installs a repeatable current-record
screen for future C5 candidates and records the current C5 seed result.

## Harness Contract

The harness checks a candidate quotient/algebra/shadow packet against the frozen
SM R0 list:

- gauge anomaly cancellation for the surviving spectrum;
- chirality production;
- three generations without per-generation adjustable structure;
- absolute hypercharge normalization;
- physical Higgs sector;
- complete surviving spectrum;
- extra or mirror mode decoupling at accessible energies;
- source-owned target-free selector status.

The harness is deliberately stricter than a Pati-Salam host check. Host evidence,
relative hypercharge arithmetic, or anomaly cancellation after granting the
ordinary chiral shadow is useful evidence, but not enough for SM R0.

## Machine Check

`tests/recovery-contract/construction_space_sm_r0_c5_harness.py` uses exact
rational arithmetic for anomaly checks and candidate metadata for the
source-owned selector, generation, Higgs, spectrum, and decoupling constraints.

Positive controls:

- a complete source-owned three-generation packet passes;
- a wrong-hypercharge packet fails;
- an anomaly-free vectorlike host still fails because chirality, native
  generation selection, Higgs, spectrum, and decoupling are load-bearing.

## Current C5 Seed Result

The current C5 seed is the Pati-Salam / Spin(10) host with the W222 relative
hypercharge/anomaly arithmetic.

It has real positive evidence:

- one-generation ordinary anomaly cancellation;
- relative hypercharge arithmetic once the Pati-Salam-to-SM branch and chiral
  shadow are granted.

It fails SM R0 under current evidence because it still lacks:

- a source-owned target-free finite algebra or gauge-quotient selector;
- native three-generation selection;
- absolute hypercharge normalization before branch import;
- physical Higgs sector;
- complete surviving-spectrum theorem;
- extra or mirror mode decoupling.

The construction-space map records the current seeded C5 SM track as
`R0_FAIL`. A future source-owned selector packet can be run through the same
harness without changing the constraint list.

## Boundary

This is a reusable harness plus a current-evidence seed failure, not a global
Standard Model no-go. The exact resurrection burden remains the same: provide a
source-owned finite algebra, gauge quotient, observer shadow, chirality
mechanism, Higgs projection, spectrum theorem, or decoupling certificate before
target comparison.

Paper seed proposal: none.
