# VERIFICATION -- Open-System Bistability of Total Unitarity (draft)

Each load-bearing claim maps to the repo test that machine-checks it, with the exit status recorded on the
run of 2026-07-14 (Python + numpy). Reproduce from the repo root with `python -u tests/<file>`.

| # | Claim (draft section) | Grade | Test | Recorded result |
|---|---|---|---|---|
| T1 | Physical-subspace unitarity defect A^dag A = P+ + B^dag B, sign-definite (Sec 3, Thm 1) | THEOREM | `tests/W132_graded_optical_theorem_physical_subspace.py` | 18/18, exit 0 |
| T2 | Like-signed regime: reduced physical-sheet pole (argument principle 1 vs 0) WITH real total spectrum and positive total metric, total unitary to 1e-15 (Sec 3, Thm 2) | THEOREM (finite model) | `tests/W183_external_input_open_system.py` | 27/27, exit 0 |
| T3 | Opposite-signed regime: total exceptional point g_c = 0.392, no positive total metric, complex pair above g_c (Sec 3, Thm 3) | THEOREM (finite model) | `tests/W183_external_input_open_system.py` | 27/27, exit 0 |
| T4 | Bistable fixed point: non-vacuity (kappa* = 1.059), both fixed points stable, operative bootstrap (positive total metric min eig 0.448, total unitary to 6e-14) (Sec 3, Thm 4) | TOY-MODEL | `tests/W186_source_content_reservoir_krein_type.py` | 36/36, exit 0 |
| T5 | Selection reduces to coupling ratio vs O(1) (Sec 3, Thm 5) | TOY / STRUCTURAL | `tests/W186_source_content_reservoir_krein_type.py` (Block D) | 36/36, exit 0 |
| P6 | Fade dynamical selection through a finite-N non-unitary window (Sec 3, Prop 6) | PLAUSIBLE-ONLY | `tests/W186_source_content_reservoir_krein_type.py` (Block E) | 36/36, exit 0 |
| S1 | Perturbative C-operator exists through Q2 off resonance; obstructs on a measure-zero commensurate lattice (support) | PROVEN-in-QM | `tests/W169_c_operator_perturbative_construction.py` | 23/23, exit 0 |
| S2 | Interacting C-operator all-orders QFT: existence CONDITIONAL-ON-SUB-THRESHOLD (PT-unbroken) (support) | STRUCTURAL | `tests/W179_c_operator_allorders_qft.py` | exit 0 |
| S3 | Interacting-C essential spectrum via analytic Fredholm (support) | STRUCTURAL | `tests/W175_analytic_fredholm_essential_spectrum.py` | exit 0 (slow, ~3 min) |
| S4 | No-local-positive-metric hardening (support) | THEOREM (free theory) | `tests/W121_path2_target3_hypothesis_hardening.py` | exit 0 |

## Coverage honesty

- The reframe theorems (T1, T2, T3) and the non-vacuity of the operative fixed point (T4a) are machine-
  checked as exact / argument-principle statements in a finite model.
- **T4-T5 and P6 are checked ONLY within the finite Friedrichs / Fano-Anderson toy.** No test exercises a
  real Stelle-class or GU dressed reservoir. Closing that gap is item 1 of the hardening ledger (the
  generic-capture lemma or a real dressed computation) and is the gate to any candidate promotion.
- All positive controls in the underlying tests run FIRST (W183 PC1-PC3; W186 PC1-PC2), and each load-
  bearing claim carries a matched negative control (positive-definite metric shows no sign flip and no
  bistability; residue-flip removes the W132 violation), per the W138 kill-battery discipline.

*Recorded 2026-07-14 by TEAM CLASS-PAPER (W188). Drafts only; no promotion; external action Joe-gated.*
</content>
