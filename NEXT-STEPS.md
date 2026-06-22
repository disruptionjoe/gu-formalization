---
title: "Next Steps For Contributors"
status: active_research
doc_type: roadmap
updated_at: "2026-06-01"
---

# Next Steps For Contributors

This repo should not ask contributors to solve Geometric Unity. The useful unit is a bounded test with a clear failure condition.

## Best First Tasks

| order | task | output | best for |
|---:|---|---|---|
| 1 | Build or improve the no-go assumption/evasion matrix. | A precise assumption/exits table. | mathematicians, physicists, careful generalists |
| 2 | Fill one six-axis candidate specification. | One complete substrate/observer/pairing/causal/emergence/loop spec. | anyone proposing a path |
| 3 | Strengthen the finite Connes control checklist. | A clearer Type II1 extension requirement. | NCG/operator-algebra contributors |
| 4 | Work on the signed-readout theorem core. | Definitions, theorem statement, proof, or counterexample. | TCS, math, lattice-QFT readers |
| 5 | Run the observer-finality record-graph test. | A diagram and definitions separating evidence, causality, finality, and readout. | distributed systems, foundations, TCS contributors |
| 6 | Claim-mine a transcript-rich GU media source. | Timestamped rows in the source ledger. | source researchers, science communicators |

## Highest-Upside Paths

| path | status | publish potential | next action |
|---|---|---:|---|
| Class-relative no-go map | canon | 5 | sharpen assumptions and known exits |
| Six-axis specification protocol | canon | 5 | add more filled examples |
| Type II1 spectral SM checklist | canon / active research | 5 | specialist review of KO-dim and principal-graph issues |
| Signed-readout boundary theorem | active research | 5 | prove monotonicity criterion and PN/Jordan factorization |
| Observer-finality record-graph test | exploration | 4 | test whether finality semantics clarify signed-readout without smuggling global time |
| Observer-pairing anomaly enrichment | exploration | 3 | build a toy enriched-bordism example |
| C_MPR / 9-tuple / BvN wall | exploration | 3 | state object, morphism, and proof obligations before claiming theorem status |

## Nguyen Critique: Priority Research Items

These three tasks are the direct operational outputs of the full assessment in
`explorations/nguyen-gu-critique/`. They are ranked by how much they constrain
everything downstream.

| order | task | output | blocker if skipped |
|---:|---|---|---|
| N1 | **Signature audit** — redo §3.1's complexification argument in split-signature (7,7) with Majorana–Weyl spinors (real dim 64), not Euclidean (14,0). | Clear verdict: does the unannotated-⊗ℂ gap survive in GU's actual signature? | Without this, we don't know which horn of the §3.1↔§3.2 pincer is live. |
| N2 | **Shiab from Spin(7,7)-invariant data** — define the shiab operator from Sp(14) or Spin(7,7)-invariant subspaces and compute its anomaly content. | A construction (or proven obstruction). This is the one place new mathematics is required. | This is the pincer. No other task resolves it. |
| N3 | **Discharge or record H3** — the Čech-H¹ ↔ holonomy dictionary in `time-as-finality` (`tests/T63`) is conditional on H3; run the `cech_sheaf_fixture` in `temporal-issuance` (E015 route). | H3 discharged, or H3 recorded as the named open blocker. | Current holonomy results are conditional; their status is unresolved. |

**Constraint on all three:** No output from N1–N3 should be framed as a Nguyen
refutation in published form. These repos specify escape routes; they do not prove
them. Framing: "these are the constructions GU would need; we are attempting them."

---

## What To Avoid

- Do not claim this repo proves GU.
- Do not claim computation or observer language evades Witten without a construction.
- Do not treat C_MPR, the 9-tuple, PCP-blindness, or the BvN-style wall as settled.
- Do not use media claims as technical evidence without independent formalization.
- Do not make broad synthesis essays when a small falsifiable test is possible.
- Do not use observer-finality language as a no-go theorem escape hatch; state the record protocol and failure mode.
