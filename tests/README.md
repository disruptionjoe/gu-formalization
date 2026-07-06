# tests/

Computational checks for the program's claims. Each file is a standalone audit/gate script (run it directly
with `python`). For a one-step sweep, use `scripts/reproduce_all.py` as the central runner. This manifest is
the map: which directory/group supports which claim.

## Reproducing the lead paper ("Located, Not Forced")

The three files the paper cites for its load-bearing computations live in **`generation-sector/`**:

- `generation-sector/ghost_parity_krein.py` — the carrier's Krein signature is exactly `(+96, -96)` (vectorlike).
- `generation-sector/net_chiral_index_invariant.py` — on the `(96,96)` cross-chirality carrier the net chiral
  index `chi = 0` for every physical subspace, invariant under any linear Krein isometry (Theorem 2).
- `generation-sector/t1a_kinematic_chirality_kill.py` — the kinematic chirality-forcing route is killed.

These three paths are **frozen** (the paper cites them); do not move or rename them.

## Organized subdirectories

| Directory | What it covers |
|---|---|
| `generation-sector/` (27) | the generation-count core: Krein signature, net chiral index, chirality kills (paper-cited; frozen) |
| `source-action/` (11) | the twisted Rarita-Schwinger / source-action gate work (frozen alongside the paper) |
| `gu-independent/` (11) | the GU-independent class-level structural no-go |
| `hessian-z3/` (9) | Hessian / Z3 carrier-occupancy checks |
| `forcing-slot/` (8) | the forcing-slot toy stabilized-source test |
| `carrier-mass/` (7) | the carrier Dirac-mass capstone |
| `anchored-leads/` (7) | the anchored-leads screen, including an independent Jones-index finite-type recheck |
| `decider/` (4) | the single-decider ("only honest computable integer is one") |
| `boundary-eta/` (2) | the boundary eta-invariant / tangential fork, with nested independent denominator checks |
| `anomaly/` (1) | frontstage anomaly gate validators, currently the Sp(1) 2-primary Dai-Freed AHSS gate |
| `calm-gw-boundary/` (1) | finite CALM/GW boundary gate for Jordan-component axial-charge monotonicity versus scalar/rounded readout failures |
| `pati-salam/` (1) | reproduction harness for the active-research Pati-Salam chain verification scripts |
| `enum-completeness/` (2) | enumeration-completeness certificate for the located-not-forced publication gate |
| `antilinear-bound/` (3) | antilinear-bound certificate for the located-not-forced publication gate |
| `function-space-ext/` (9) | WC-FUNCTION-SPACE-EXT probes plus the signed-readout UII certificate-shape validator: finite Galerkin, conditional section theorem + independent check, APS eta boundary control, and UII gap gate |
| `rs-function-space/` (4) | RS function-space family-index scaffolds: K3 pushforward, boundary eta, and family/characteristic-class generation-arena probes |
| `hourly-cycles/` (archived off-tree) | **archived** hourly-automation output; not load-bearing |

## Loose audit scripts at `tests/` root, by sector

These ~94 scripts are referenced as provenance from `canon/*-RESULTS.md`, so they are indexed here in place
(not moved) to keep those reproduction pointers valid. Grouped by subject:

- **RS / BV-BRST sector** — `rs_*.py` (20): the Rarita-Schwinger bicomplex, ghost / Koszul-Tate / BRST
  structure, `c2` curvature, Clifford projector, symbol-index. (e.g. `rs_bicomplex_*`, `rs_ghost_*`,
  `rs_k3_symbol_index_formula_audit.py`).
- **shiab selector / codifferential** — `shiab_*.py` (10): selector complex, gamma-trace, quaternionic
  H-linearity, seesaw, `Sp(64)`, codiff obstruction (e.g. `shiab_selector_*`, `shiab_vs_codiff_cl95.py`).
- **Cycle audits** — `cycle1_*`, `cycle2_*`, `cycle3_*.py` (15): per-cycle gate/certificate audits
  (IG current, RS rank, QFT two-point, Pati-Salam stabilizer, VZ e-block, dark-energy sign, prediction census).
- **Mission-A extraction audits** — `mission_a_*.py` (5): generation-count machinery, dark-energy provenance,
  matter-gauge selector, metric/QFT shadow extraction.
- **Generation count & K3** — `gen_*`, `y14_k3_*`, `three_generation_*`, `three_cycle_*`,
  `topological_generation_count_*`, `sp64_octic_trace_i16.py`, `ahat_genus_y14_i16.py`, `c2_holonomy_*` (~12).
- **Bell / QFT / measurement** — `h3_*`, `qft_shadow_extraction_*`, `quantum_gravity_reframing_*` (~6):
  Pati-Salam CHSH state/correlator, measurement gate, Cech-sheaf fixture.
- **Velo-Zwanziger** — `vz_*.py` (2): typed-symbol gate, subprincipal `FC-VZ-4`.
- **GR / cosmology / dark energy** — `gr_shadow_recovery_*`, `gu_action_branch_*`, `flrw_theta_xi_*`,
  `theta_flrw_desi_sign.py`, `willmore_el_schwarzschild_order.py`, `stress_energy_shadow_emergence_*` (~6).
- **Marble-wood reframing** — `marble_wood_*`, `unified_marble_wood_*`, `metric_marble_prematurity_*` (~4).
- **Source / selector / control** — `source_geometry_*`, `matter_gauge_source_selector_*`,
  `sequential_source_to_index_goals_*`, `finite_control_*`, `sm_finite_control_ledger_*`,
  `dgu_guarded_symbol_*`, `constraint_first_ig_tangent_*`, `primary_gu_interface_*`, `oq_rk1_*` (~10).
- **Meta / posture audits** — moved to `process_gates/` in the de-theater pass; examples include
  `live_claim_dag_audit.py`, `lean_certificate_surface_audit.py`, `research_posture_audit.py`, and
  `temporal_issuance_source_action_steelmen_checker.py`. They are governance gates, not mathematical
  certificate tests.
