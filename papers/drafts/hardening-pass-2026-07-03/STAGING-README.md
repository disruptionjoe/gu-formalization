---
title: "Bucket-A paper-hardening pass (2026-07-03) — STAGED DRAFTS, not canon"
status: draft
doc_type: staging_index
created: 2026-07-03
---

# located-not-forced hardening pass — 2026-07-03 (staged drafts)

A big-swing pass at hardening the `located-not-forced` paper while it is out for external review.
Produced by a scope -> produce -> **adversarial verify** -> synthesize workflow; every item was
adversarially re-checked and every certificate re-run independently by the main loop (all exit 0),
including a reproduced Lean compile (4.32.0-rc1) and a three-method rank confirmation.

**These are DRAFTS. Nothing here is promoted.** No canon file, `CANON.md`, `RESEARCH-STATUS.md`,
`NEXT-STEPS.md`, or the paper was edited. The generation-count verdict stays **OPEN**; nothing derives
three (A2a even returns the "wrong" number, 416, which is itself anti-target-import evidence). Internal
tier. Promotion to canon or into the paper pauses for Joe.

## Items

| item | artifact | grade | verifier | key residual |
|---|---|---|---|---|
| **A1** Lean-formalize the theorem legs | `Lean/GUFormalization/LocatedNotForcedLegs.lean` is the sole authoritative certificate; this folder retains the historical inventory, the mathlib-free arithmetic check, and `A1-arithmetic-certificate.py` | Complete for the finite kernel (2026-07-22 baseline) | holds | the former unverified duplicate was retired; physical premises remain outside Lean |
| **A2a** OQ-RK1 `ind_H` rank certificate | `../../tests/hardening-pass/oqrk1_indh_rank.py` (+ `verify/`), `A2a-oqrk1-indh-rank-RESULTS-DRAFT.md` | Partial / honest-negative | holds | composite rank returns 832 (C) / 416 (H) **without target import**; the physical-projector / BRST / K-theory legs stay BLOCKED_NEEDS_SPEC; OBJ-GEN stays OPEN |
| **A2b** Distler-Garibaldi scope-exit note | `A2b-distler-garibaldi-scope-exit-note.md`, `certs/dg_scope_exit_structural_cert.py` (dim Sp(64)=8256, rank 64; E8 dim 248 rank 8; obstructions True) | Partial-success (strong) | holds | §4 functor non-existence disclosed as residual; also fixes a real arXiv miscitation (0905.2483 -> 0905.2658) |
| **A2c** Nguyen §3.1 shiab-dissolution note | `A2c-nguyen-3-1-shiab-dissolution-note.md` | Success (honest scope) | holds | dissolves only the UNIVERSAL form, contingent on the (9,5) reconstruction; claims EXISTENCE ONLY (no uniqueness/selector/rank) |
| **A3** enum-completeness route-(a) classification | `A3-enum-completeness-route-a-classification-attempt.md`, `../../tests/hardening-pass/enum_route_a_classification.py` | Partial (proof-grade dims; residuals R1/R2/R3) | holds | reproduces the census, not a generation count; three named residuals R1/R2/R3 keep route (a) OPEN |

## Certificates (all re-run by the main loop, exit 0)

- `A1-arithmetic-certificate.py` (17 checks), `A1-arith-core-check.lean` (Lean compile exit 0)
- `../../tests/hardening-pass/oqrk1_indh_rank.py` + `verify/oqrk1_indh_rank_indep_check.py`,
  `verify/adv_recheck.py`, `verify/adv_recheck_832.py`, `verify/indep_hom_klimyk_direct.py`
- `certs/dg_scope_exit_structural_cert.py`
- `../../tests/hardening-pass/enum_route_a_classification.py`

(One redundant adversarial-verifier throwaway, `verify/indep_hom_peel.py`, was removed — it hung on a
Weyl-product loop and duplicated the Klimyk route that already confirms dim Hom = 2.)

## No target import

Across all five items the tokens 3 / 4 / 8 / 24 / chi(K3) appear only as disclaimed factorizations,
quarantined (non-load-bearing) section numbers, or residual-family arithmetic — never divided-by or
normalized-to. A2a returning 416 (not a target) is the strongest single piece of anti-import evidence.

## Suggested next moves (for Joe / future runs)

- A1: stand up a `.lake`/mathlib compile to verify the skeleton legs (would cross internal -> external tier
  on the theorem-grade core — the paper's caveat (e) gap).
- A2b / A2c: these are referee-defense notes ready to fold into the paper's response-to-referees or an
  appendix once Joe decides; the DG arXiv-citation fix should propagate to the paper's bibliography.
- A3: attack residuals R1/R2/R3 to push route (a) from partial toward a full classification proof.
- A2a: the physical-projector / gauge-fixed leg is BLOCKED_NEEDS_SPEC (routes into the source-action
  bottleneck); do not force it.
