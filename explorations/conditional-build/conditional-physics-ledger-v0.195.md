---
artifact_type: conditional_physics_ledger_release
created: 2026-08-12
ledger_version: "0.195"
run_id: RUN-20260812-043842-gu-trace-hq-connection-internal-chain
---

# Conditional physics ledger v0.195

Ledger v0.195 — 82/82 mapped; 32 SAME · 19 DIFFERS · 26 NEEDS · 5
OVER-DETERMINED. Headline counts and booked residue do not move. Split-spin
compatibility of the trace-owned Hermitian form is now exact.

For fixed trace q, `D H_q=0` keeps exactly
`Spin(1,3)xSpin(6,3)`, dimension `42`.  The defect has exact rank nine and
reconstructs every normal connection component that moves q.  This supplies a
valid compatible split-spin connection without adding datum or using P1.

The internal-chain shortcut fails.  Freezing q replaces full Pati-Salam
`Spin(6)xSpin(4)` by `Spin(6)xSpin(3)`.  Although the residual algebra can
contain `su(3)+su(2)+u(1)`, its naive fermion restriction makes both
Pati-Salam halves diagonal-`SU(2)` doublets.  Exact intersection with the
independent `(4,1,2)` `v_PSB` stabilizer has dimension `9`, not the Standard
Model's `12`; trace q cannot be reused as that breaking vector.

The source-typed route therefore remains the moving/full-`U(64,64)` (or still
unselected two-half) connection plus the explicit full-Pati-Salam/`U(3,2)`
intersection.  Its distinct `varpi` cell must then be tested as the observed
scalar doublet.  The rank-nine `6+3` connection defect is not a Higgs doublet.
Physical half asymmetry, BV cohomology, domains, index and count remain
downstream.

Residue stays at 84 booked continuous real parameters, at least 19
function-valued slots and nine discrete forks, with five scoped quotients.
Six rows migrate in distance/evidence only. P1/P2/P3 remain unchanged.

Machine-readable ledger:
`lab/process/conditional-physics-ledger-v0.195.json`.
