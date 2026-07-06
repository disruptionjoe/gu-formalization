# process_gates

Governance / consistency / prose-discipline audits, relocated here from `tests/` in the
2026-06-30 de-theater pass so that `tests/` is reserved for files that build a mathematical
object and compute a number/rank/dim/index.

These files assert **documentation and status discipline** (posture wording, claim-DAG
consistency, allowed/forbidden provenance inputs, "no overclaim" checks, Lean-surface presence,
etc.) - they do **not** perform mathematics. A green run here means the prose/governance
contracts hold; it says nothing about whether a GU claim is mathematically checked. For that,
see `tests/` (real computations) and `tests/chase/` (verified verdict scripts).

## Why top-level (same depth as `tests/`)

Each gate computes the repo root as `Path(__file__).resolve().parents[1]`, which assumes the
file sits one level under the repo root. `process_gates/` is at the same depth as `tests/`, so
that path logic is preserved unchanged and no gate needed editing to move here.

## Live process gate inventory

This filename inventory is intentionally mechanical: it lets `process_gate_readme_inventory_audit.py`
detect when a new gate exists without a public process-map entry. Detailed meaning stays in the
selected notes below and in each script header.

- `changed_public_path_hygiene_audit.py`
- `constraint_first_ig_tangent_gate.py`
- `cycle1_branch3_dynamical_ig_current_audit.py`
- `cycle1_qft_positive_two_point_certificate_audit.py`
- `cycle1_source_selected_pati_salam_stabilizer_audit.py`
- `cycle1_vz_subprincipal_eblock_proof_gate_audit.py`
- `cycle2_qft_physical_field_positive_pairing_seed_audit.py`
- `cycle2_source_critical_rank_one_psb_selection_audit.py`
- `cycle2_source_forced_s_ig_dyn_action_audit.py`
- `cycle2_vz_actual_operator_e_block_audit.py`
- `cycle3_cgw_bvn_wall_define_or_demote_audit.py`
- `cycle3_connes_control_load_bearing_audit.py`
- `cycle3_dark_energy_predictive_sign_coupling_audit.py`
- `cycle3_single_surviving_prediction_census_audit.py`
- `cycle3_taf_transport_or_close_audit.py`
- `decider_readme_inventory_audit.py`
- `dgu_guarded_symbol_certificate_audit.py`
- `finite_control_provenance_audit.py`
- `flrw_theta_xi_branch_gate.py`
- `gr_shadow_recovery_certificate_audit.py`
- `gu_action_branch_gate.py`
- `internal_ops_gitignore_audit.py`
- `lean_certificate_surface_audit.py`
- `live_claim_dag_audit.py`
- `marble_wood_open_avenues_audit.py`
- `marble_wood_reframing_audit.py`
- `matter_gauge_source_selector_audit.py`
- `metric_marble_prematurity_audit.py`
- `mission_a_generation_count_analytic_machinery_audit.py`
- `mission_a_lambda_dark_energy_provenance_audit.py`
- `mission_a_matter_gauge_selector_audit.py`
- `mission_a_metric_shadow_extraction_audit.py`
- `mission_a_qft_state_space_extraction_audit.py`
- `primary_gu_interface_contract_audit.py`
- `process_gate_readme_inventory_audit.py`
- `protected_surface_diff_audit.py`
- `public_path_hygiene_audit.py`
- `qft_shadow_extraction_certificate_audit.py`
- `quantum_gravity_reframing_audit.py`
- `reproduce_harness_scope_audit.py`
- `reproduction_docs_consistency_audit.py`
- `research_posture_audit.py`
- `roadmap_current_routing_links_audit.py`
- `sequential_source_to_index_goals_audit.py`
- `sm_finite_control_ledger_audit.py`
- `source_geometry_contract_audit.py`
- `stress_energy_shadow_emergence_audit.py`
- `tests_manifest_count_audit.py`
- `three_cycle_fifteen_hole_runbook_audit.py`
- `three_generation_route_alternatives_audit.py`
- `topological_generation_count_families_k3_chi_gate_audit.py`
- `unified_marble_wood_closure_audit.py`
- `y14_k3_bridge_gate.py`
- `y14_k3_bridge_loss_audit.py`
- `y14_k3_end_data_topography_gate_audit.py`

## Current routing link gate

`roadmap_current_routing_links_audit.py` checks that local Markdown links in
`lab/roadmap/README.md` are repository-relative and resolve from that file's actual location.
Failures report the roadmap line number and target path. This protects the current routing
table without treating roadmap prose as a research claim.

## Internal ops gitignore gate

`internal_ops_gitignore_audit.py` checks that `steward/runs/` remains ignored and contains no
tracked files. This protects local CapacityOS run records from being published with the public
research repo while leaving those records available for collision checks.

## Public path hygiene gate

`public_path_hygiene_audit.py` checks the root public entry file, neutral contributor/config
files, `process_gates/` sources, and `lab/active-research/` owner surfaces for absolute
home-path leaks before those surfaces are committed in this public repo. Including
active research keeps frontstage public packets from carrying local machine paths; the gate
still treats the content as prose/governance hygiene, not as mathematical validation.
It intentionally does not scan canon, derivation, proof, result-grade, paper, Lean proof,
exploration, or research-status surfaces, so it can run while those areas are dirty or under
governance review.

## Changed public path hygiene gate

`changed_public_path_hygiene_audit.py` checks the current tracked Git diff plus untracked
non-ignored files for generic local home-directory path shapes before scheduled runs stage
or commit public changes. This complements the fixed-surface public path hygiene gate by
covering whatever publishable files the current run actually changed.

## Lean certificate surface gate

`lean_certificate_surface_audit.py` checks the Lean scaffold, current certificate files,
standalone Lean certificate pointers, owner-surface references, CI workflow, and local
Lean check script. It strips Lean comments before scanning for proof placeholders, so
honest explanatory headers can mention `sorry` or `axiom` while proof bodies remain
placeholder-free. This is a process gate; `lake build` and targeted `lake env lean ...`
commands remain the compile checks.

## Tests manifest count gate

`tests_manifest_count_audit.py` checks the live organized-subdirectory counts in
`tests/README.md` against the current direct non-README files in each listed test
directory. Rows marked `archived off-tree` are allowed only when the named directory is
not present. This protects the public reproduction map from drifting as validators are
added or archived without treating manifest counts as mathematical evidence.

## Reproduction harness scope gate

`reproduce_harness_scope_audit.py` imports `scripts/reproduce_all.py` without running
the certificate suite, then checks that quick mode discovers exactly the live `tests/`
Python certificates, full mode adds only the declared paper certificate roots, skip
directories remain excluded, `process_gates/` remains outside the computational
certificate sweep, and list mode prints repository-relative slash paths.

## Reproduction docs consistency gate

`reproduction_docs_consistency_audit.py` checks that `REPRODUCE.md`, `tests/README.md`,
and `scripts/reproduce_all.py` consistently describe the public reproduction model:
certificates remain directly runnable, and `scripts/reproduce_all.py` is the central
one-step runner. This is a documentation guard, not a mathematical certificate.

## Protected surface diff gate

`protected_surface_diff_audit.py` checks the current local Git diff plus untracked files for
paths that scheduled Progress runs should not touch without explicit review: canon/status/posture
surfaces, protected licenses, papers, Lean proof surfaces, active-research packets, absorbed
source-action material, and the claim-status ledger/runbook. This is a governance guard for
staging discipline, not a mathematical certificate and not a verdict on the changed content.

## Process gate README inventory gate

`process_gate_readme_inventory_audit.py` compares the live `process_gates/*.py` files with the
local script names documented in this README. It keeps the public process map synchronized with
the executable gate surface without running the gates themselves or evaluating their scientific
content.

## Decider README inventory gate

`decider_readme_inventory_audit.py` checks that `tests/decider/README.md` names every direct
`tests/decider/*.py` certificate and preserves the explicit not-forced / gated boundary for the
single-decider family. This is a map and posture guard only; it does not run the decider scripts
or change verdicts.

## Relocated surface path hygiene

Repository process, automation, and active-research owner surfaces now live under `lab/`.
Process gates should point at current `lab/process/`, `lab/automation/`, and
`lab/active-research/` paths when checking live owner surfaces. Historical exploration
artifacts may still quote older path strings as provenance. Do not rewrite those mechanically
unless the selected gate depends on them as current executable inputs.

Remaining content failures are governance debt to fix or retire separately; they are not
introduced by the path repair.
