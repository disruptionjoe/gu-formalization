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

- `absorbed_readme_surface_map_audit.py`
- `antilinear_bound_readme_inventory_audit.py`
- `anchored_leads_readme_inventory_audit.py`
- `anomaly_readme_inventory_audit.py`
- `big_swing_readme_inventory_audit.py`
- `boundary_eta_readme_inventory_audit.py`
- `calm_gw_boundary_readme_inventory_audit.py`
- `canon_readme_surface_map_audit.py`
- `carrier_bit_decision_readme_inventory_audit.py`
- `certificate_shape_audit.py`
- `changed_public_path_hygiene_audit.py`
- `contributing_guidance_audit.py`
- `carrier_mass_readme_inventory_audit.py`
- `chase_readme_inventory_audit.py`
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
- `de_amp_diagnostic_closure_audit.py`
- `dgu_guarded_symbol_certificate_audit.py`
- `docs_readme_surface_map_audit.py`
- `enum_completeness_readme_inventory_audit.py`
- `escape_corners_readme_inventory_audit.py`
- `explorations_top_level_file_boundary_audit.py`
- `explorations_readme_surface_map_audit.py`
- `finite_control_provenance_audit.py`
- `forcing_slot_readme_inventory_audit.py`
- `flrw_theta_xi_branch_gate.py`
- `fork_depth_audit.py`
- `function_space_ext_readme_inventory_audit.py`
- `generation_sector_readme_inventory_audit.py`
- `github_readme_surface_map_audit.py`
- `gu_independent_readme_inventory_audit.py`
- `gr_shadow_recovery_certificate_audit.py`
- `gu_action_branch_gate.py`
- `hardening_pass_readme_inventory_audit.py`
- `hessian_z3_readme_inventory_audit.py`
- `internal_paths_readme_inventory_audit.py`
- `internal_ops_gitignore_audit.py`
- `issue_template_validation_audit.py`
- `k77_post_b2_next_eight_wave_scaffold_audit.py`
- `k77_wave2_action_ward_scope_audit.py`
- `k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit.py`
- `k77_wave2_actual_y14_receiver_ordering_scope_audit.py`
- `k77_wave2_actual_draft916_blockwise_scope_audit.py`
- `k77_wave2_common_two_layer_action_scope_audit.py`
- `k77_wave2_dirac_derham_superig_rebase_scope_audit.py`
- `k77_wave2_euler_shell_two_connection_scope_audit.py`
- `k77_wave2_global_draft916_krein_preboundary_scope_audit.py`
- `k77_wave2_mixed_primalizer_comparison_scope_audit.py`
- `k77_wave2_two_connection_action_owner_scope_audit.py`
- `k77_wave2_q_receiver_trace_adjoint_ward_scope_audit.py`
- `k77_wave2_source_sign_shiab_duality_scope_audit.py`
- `k77_wave2_trace_q_coefficient_zero_order_reality_scope_audit.py`
- `k77_wave2_up_back_over_target_scope_audit.py`
- `k77_wave2_stabilized_mixed_cross_map_scope_audit.py`
- `lab_active_research_readme_surface_map_audit.py`
- `lab_automation_readme_surface_map_audit.py`
- `lab_deep_research_readme_surface_map_audit.py`
- `lab_process_readme_surface_map_audit.py`
- `lab_process_runbooks_readme_inventory_audit.py`
- `lab_readme_surface_map_audit.py`
- `lab_sources_readme_surface_map_audit.py`
- `lab_specifications_readme_surface_map_audit.py`
- `lane_state_freshness_audit.py`
- `lean_certificate_surface_audit.py`
- `literal_derivation_audit.py`
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
- `next_steps_frontdoor_guard_audit.py`
- `pati_salam_readme_inventory_audit.py`
- `papers_candidates_readme_inventory_audit.py`
- `papers_readme_lifecycle_map_audit.py`
- `post_batch2_wave1a_supersession_dependency_audit.py`
- `primary_gu_interface_contract_audit.py`
- `process_gate_readme_inventory_audit.py`
- `protected_surface_diff_audit.py`
- `pull_request_template_validation_audit.py`
- `public_path_hygiene_audit.py`
- `queue_review_freshness_audit.py`
- `readme_entrypoint_map_audit.py`
- `qft_shadow_extraction_certificate_audit.py`
- `quantum_gravity_reframing_audit.py`
- `reproduce_harness_scope_audit.py`
- `reproduction_docs_consistency_audit.py`
- `recovery_certification_matrix_audit.py`
- `recovery_contract_action_fingerprint_audit.py`
- `recovery_contract_manifest_audit.py`
- `research_portfolio_contract_audit.py`
- `research_posture_audit.py`
- `resolver_wave_a_scope_audit.py`
- `resolver_wave_b_scope_audit.py`
- `resolver_wave_c_scope_audit.py`
- `resolver_wave_d_scope_audit.py`
- `resolver_wave_e_scope_audit.py`
- `resolver_wave_f_scope_audit.py`
- `resolver_wave_g_scope_audit.py`
- `resolver_wave_h_scope_audit.py`
- `resolver_wave_i_scope_audit.py`
- `resolver_wave_k77a_scope_audit.py`
- `resolver_wave_k77b_scope_audit.py`
- `resolver_wave_k77b2_scope_audit.py`
- `resolver_wave_k77b3_scope_audit.py`
- `resolver_wave_k_scope_audit.py`
- `roadmap_current_routing_links_audit.py`
- `rs_function_space_readme_inventory_audit.py`
- `scripts_readme_surface_map_audit.py`
- `sequential_source_to_index_goals_audit.py`
- `sm_boundary_readme_inventory_audit.py`
- `sm_finite_control_ledger_audit.py`
- `source_action_readme_inventory_audit.py`
- `source_geometry_contract_audit.py`
- `spec_consistency_readme_inventory_audit.py`
- `stress_energy_shadow_emergence_audit.py`
- `symbolic_proofs_readme_inventory_audit.py`
- `tests_manifest_count_audit.py`
- `tests_root_readme_inventory_audit.py`
- `threads_readme_inventory_audit.py`
- `three_cycle_fifteen_hole_runbook_audit.py`
- `three_generation_route_alternatives_audit.py`
- `topological_generation_count_families_k3_chi_gate_audit.py`
- `unified_marble_wood_closure_audit.py`
- `wave_disposition_schema_audit.py`
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

## Lab README surface-map gate

`lab_readme_surface_map_audit.py` checks that `lab/README.md` names every live top-level lab
surface, uses relative links that resolve from the lab README location, and preserves the
front-door boundary between working lab material and reviewed `canon/` / `papers/` outputs.
This is a navigation/process guard only; it does not validate research claims.

## Lab automation README surface-map gate

`lab_automation_readme_surface_map_audit.py` checks that `lab/automation/README.md` names
the live direct automation entries and preserves the boundary that automation prompts, logs,
evidence, and helpers are operational provenance rather than load-bearing research. This is a
navigation/process guard only; it does not inspect run payloads or validate research claims.

## Lab deep-research README surface-map gate

`lab_deep_research_readme_surface_map_audit.py` checks that
`lab/deep-research/README.md` names every direct external deep-research brief,
points adjacent hostile-referee prompt readers to the live paper surfaces, and
preserves the boundary that web-enabled model reports are source/provenance and
adversarial-hardening context rather than claim-status, canon-verdict,
proof-status, paper-status, or public-posture movement. This is a
navigation/process guard only; it does not parse deep-research payloads or
validate research claims.

## Lab active-research README surface-map gate

`lab_active_research_readme_surface_map_audit.py` checks that
`lab/active-research/README.md` keeps its declared Current Threads table wired to live
local surfaces and preserves the active-research / not-yet-canon boundary. This is a
navigation/process guard only; it does not validate theorem packets or move research status.

## Lab process README surface-map gate

`lab_process_readme_surface_map_audit.py` checks that `lab/process/README.md` names
the live direct process directories and direct process files, while preserving the boundary
that process navigation does not move claim status, canon verdicts, proof status, research
verdicts, or public posture. This is a navigation/process guard only; it does not inspect
process payloads or validate research claims.

## Lab process runbooks README inventory gate

`lab_process_runbooks_readme_inventory_audit.py` checks that
`lab/process/runbooks/README.md` names every live direct runbook, uses relative links that
resolve from the runbooks README location, and preserves the boundary between process
navigation and claim-status, canon-verdict, public-posture, proof-status, or research-verdict
movement. This is a navigation/process guard only; it does not run Lean or validate research
claims.

## Lab sources README surface-map gate

`lab_sources_readme_surface_map_audit.py` checks that `lab/sources/README.md`
only lists source files that resolve locally, allows only the named pre-existing
unlisted source files, and preserves the boundary that media/source records are
provenance rather than mathematical evidence until tied to a transcript,
timestamp, or archived text fragment. This is a navigation/process guard only;
it does not mine sources, edit claim ledgers, validate research claims, or
change source/canon status.

## Lab specifications README surface-map gate

`lab_specifications_readme_surface_map_audit.py` checks that `lab/specifications/README.md`
names the live direct specification directories, points readers to each local README, and
preserves the role of specifications as comparable, falsifiable research-object machinery.
This is a navigation/process guard only; it does not validate candidate specifications or
change research status.

## Docs README surface-map gate

`docs_readme_surface_map_audit.py` checks that `docs/README.md` names every live second-tier docs
file, uses relative links that resolve from the docs README location, and preserves the boundary
between explanatory docs and the owner status/canon/publication surfaces. This is a navigation/process
guard only; it does not validate research claims.

## Explorations README surface-map gate

`explorations_readme_surface_map_audit.py` checks that `explorations/README.md` links every live
top-level exploration directory exactly once, uses relative links that resolve from the explorations
README location, and preserves the boundary between exploration-lab records and reviewed
canon/publication surfaces. This is a navigation/process guard only; it does not validate research claims.

## Explorations top-level file boundary gate

`explorations_top_level_file_boundary_audit.py` freezes the reviewed exception set for loose
top-level `explorations/*.md` notes, including the current source-action method sweep, substrate-choice
thesis, transcript carrier-B evidence note, and Godelian initial-conditions boundary-axiom stub. This is
a placement and boundary-label guard only; it does not move exploration notes, edit canon pointers,
validate research claims, or change verdicts.

## Absorbed README surface-map gate

`absorbed_readme_surface_map_audit.py` checks that `absorbed/README.md` links every live top-level
absorbed directory exactly once, uses relative links that resolve from the absorbed README location,
and preserves the boundary between absorbed context and operative repo truth. This is a navigation/process
guard only; it does not validate source-action claims or change research status.

## Canon README surface-map gate

`canon_readme_surface_map_audit.py` checks that `canon/README.md` keeps its
owner pointers wired to live repo surfaces and preserves the boundary that
`CANON.md` owns authoritative grades and index state. This is a navigation/process
guard only; it does not validate canon claims or change canon verdicts.

## Papers README lifecycle-map gate

`papers_readme_lifecycle_map_audit.py` checks that `papers/README.md` names the live
publication-stage directories, names every current staged candidate directory exactly once,
keeps the empty-published marker aligned with `papers/published/`, uses relative links that
resolve from the papers README location, and preserves the Joe-confirmed candidate/published
boundaries. This is a navigation/process guard only; it does not publish, submit, move paper
artifacts, validate research claims, or change public posture.

## Papers candidates README inventory gate

`papers_candidates_readme_inventory_audit.py` checks that `papers/candidates/README.md`
names every live staged-candidate directory exactly once, resolves local candidate and staging-note links
from the candidate README location, preserves the candidate / not-yet-public / no-publication-action
boundaries, and explicitly marks candidate folders that still lack `STAGING-NOTES.md` as cleanup debt. This
is a navigation/process guard only; it does not publish, submit, move paper artifacts, validate research
claims, or change public posture.

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

## Tests root README inventory gate

`tests_root_readme_inventory_audit.py` checks that the loose direct-root `tests/*.py`
sector table in `tests/README.md` covers every tracked root certificate script exactly
once and that row counts match the tracked root scripts. This protects the public
reproduction map without running certificates or changing verdicts.

## Threads README inventory gate

`threads_readme_inventory_audit.py` checks that `tests/threads/README.md`
names every direct thread audit script, resolves local companion-note links, and
preserves the exploration / no-claim-status / no-verdict-change / no-public-posture
boundary around the fast-moving A/B/C/D/E thread surface. This is a map and
posture guard only; it does not run the thread scripts or change verdicts.

## Reproduction harness scope gate

`reproduce_harness_scope_audit.py` imports `scripts/reproduce_all.py` without running
the certificate suite, then checks that quick mode discovers exactly the live `tests/`
Python certificates, full mode adds only the declared paper certificate roots, skip
directories remain excluded, tracked-only mode matches Git-tracked certificates,
`process_gates/` remains outside the computational certificate sweep, and list mode
prints repository-relative slash paths.

## Scripts README surface-map gate

`scripts_readme_surface_map_audit.py` checks that `scripts/README.md` names the live
repository tooling files, uses relative links that resolve from the scripts README location,
and preserves the boundary between contributor tooling and research-status movement. This is
a navigation/process guard only; it does not run the certificate suite or validate research
claims.

## Reproduction docs consistency gate

`reproduction_docs_consistency_audit.py` checks that `REPRODUCE.md`, `tests/README.md`,
and `scripts/reproduce_all.py` consistently describe the public reproduction model:
certificates remain directly runnable, and `scripts/reproduce_all.py` is the central
one-step runner. This is a documentation guard, not a mathematical certificate.

## RS function-space README inventory gate

`rs_function_space_readme_inventory_audit.py` checks that `tests/rs-function-space/README.md`
names every direct and nested RS function-space Python certificate and preserves the
open-crux / no-target-import boundary around the family-index and boundary-eta checks.
This is a map and posture guard only; it does not run the RS function-space scripts or
change verdicts.

## Anchored-leads README inventory gate

`anchored_leads_readme_inventory_audit.py` checks that
`tests/anchored-leads/README.md` names every direct anchored-lead candidate
screen and preserves the candidate-screen / located-not-forced /
source-action-gated boundary. This is a map and posture guard only; it does
not run the anchored-lead scripts or change verdicts.

## Big-swing README inventory gate

`big_swing_readme_inventory_audit.py` checks that `tests/big-swing/README.md`
names every direct big-swing Python or Lean certificate and preserves the
exploration / not-a-verdict-change / source-action-gated boundary. This is a
map and posture guard only; it does not run the big-swing scripts or change
verdicts.

## Anomaly README inventory gate

`anomaly_readme_inventory_audit.py` checks that `tests/anomaly/README.md`
names every direct anomaly Python validator and preserves the frontstage /
not-an-anomaly-cancellation-verdict / no-claim-status-movement boundary around
the Dai-Freed anomaly gate. This is a map and posture guard only; it does not
run the anomaly script or change verdicts.

## Antilinear-bound README inventory gate

`antilinear_bound_readme_inventory_audit.py` checks that
`tests/antilinear-bound/README.md` names every direct and nested antilinear-bound Python
certificate and preserves the null-eigenspace / Krein-admissibility / not-a-GU-derivation
boundary around the antilinear class. This is a map and posture guard only; it does not
run the antilinear-bound scripts or change verdicts.

## Boundary-eta README inventory gate

`boundary_eta_readme_inventory_audit.py` checks that `tests/boundary-eta/README.md`
names every direct and nested boundary-eta Python certificate and preserves the 2-primary /
tangential-order-3 / not-a-verdict-change boundary around the +96 selector fork. This is a
map and posture guard only; it does not run the boundary-eta scripts or change verdicts.

## CALM/GW boundary README inventory gate

`calm_gw_boundary_readme_inventory_audit.py` checks that
`tests/calm-gw-boundary/README.md` names every tracked direct CALM/GW Python
validator and preserves the finite certificate-shape / not-an-actual-GW-proof /
no-status-movement boundary around the Jordan-component monotonicity gate. This
is a map and posture guard only; it does not run the CALM/GW script or change
verdicts.

## SM-boundary README inventory gate

`sm_boundary_readme_inventory_audit.py` checks that `tests/sm-boundary/README.md`
names every direct and nested tracked SM-boundary Python certificate and preserves the
local-anomaly / 2-primary / no-mod-3-selector / no-claim-status-movement boundary around
the SM-shaped anomaly-inflow toy. This is a map and posture guard only; it does not run
the SM-boundary scripts or change verdicts.

## Source-action README inventory gate

`source_action_readme_inventory_audit.py` checks that `tests/source-action/README.md`
names every tracked direct source-action Python certificate and preserves the frozen /
source-action-wall / not-a-verdict-change boundary around the Seiberg-Witten and
moment-map source-action family. This is a map and posture guard only; it does not run
the source-action scripts or change verdicts.

## Spec-consistency README inventory gate

`spec_consistency_readme_inventory_audit.py` checks that
`tests/spec-consistency/README.md` names every tracked direct spec-consistency Python
certificate and preserves the consolidation / not-new-physics / no-verdict-change
boundary around source-action requirements consistency checks. This is a map and posture
guard only; it does not run the spec-consistency script or change verdicts.

## Function-space extension README inventory gate

`function_space_ext_readme_inventory_audit.py` checks that
`tests/function-space-ext/README.md` names every direct and nested function-space
extension Python certificate and preserves the conditional-theorem /
residuals-remain-open / not-a-verdict-change boundary around the function-space
extension family. This is a map and posture guard only; it does not run the
function-space extension scripts or change verdicts.

## Hardening-pass README inventory gate

`hardening_pass_readme_inventory_audit.py` checks that
`tests/hardening-pass/README.md` names every direct and nested hardening-pass
Python certificate and preserves the draft-support / OQ-RK1 honest-negative /
route-(a) residuals-open / no-target-import boundary around the
located-not-forced hardening pass. This is a map and posture guard only; it
does not run the hardening-pass scripts or change verdicts.

## Pati-Salam README inventory gate

`pati_salam_readme_inventory_audit.py` checks that `tests/pati-salam/README.md`
names every tracked direct Pati-Salam harness script and preserves the
active-research / reproduction-harness / no-physical-generation-count /
no-status-movement boundary around the owner-script harness. This is a map and
posture guard only; it does not run the Pati-Salam harness or change verdicts.

## Protected surface diff gate

`protected_surface_diff_audit.py` checks the current local Git diff plus untracked files for
paths that scheduled Progress runs should not touch without explicit review: canon/status/posture
surfaces, protected licenses, papers, Lean proof surfaces, active-research packets, absorbed
source-action material, and the claim-status ledger/runbook. This is a governance guard for
staging discipline, not a mathematical certificate and not a verdict on the changed content.

## Queue review freshness gate

`queue_review_freshness_audit.py` fails when wave dispositions have piled up since the last
filed queue review. Both existing review mechanisms examine *waves*; nothing examined the
*queue*, and the program's seven-wave `(9,5)` loss was a queue defect — every wave D-J passed
its own hostile review while the whole stack rested on an undetermined Layer-0 real-form fork
that Wave K then flipped. The gate discovers one disposition of record per resolver wave under
`explorations/` and `explorations/cycle-gates-and-audits/` (discovery and ordering rules are
stated in the script docstring), finds the queue review under `lab/process/queue-reviews/`
whose `covers_through:` reaches furthest along that order, and goes RED at
`MAX_UNREVIEWED_DISPOSITIONS = 5`. A queue review must also declare
`doc_type: queue-review`, name a real disposition id, and visibly answer the four queue
questions: undetermined-fork stacking, high-fan-out items worked late, redundant probes
attacking one object with different selectors, and conditional-match T-grade movement. This is
a process-discipline gate only; a green run says the queue has been examined recently and says
nothing about whether any wave is mathematically correct.

## Process gate README inventory gate

`process_gate_readme_inventory_audit.py` compares the live `process_gates/*.py` files with the
local script names documented in this README. It keeps the public process map synchronized with
the executable gate surface without running the gates themselves or evaluating their scientific
content.

## Pull-request template validation gate

`pull_request_template_validation_audit.py` checks that `.github/PULL_REQUEST_TEMPLATE.md`
continues to name the claim-grading discipline, the claim-status consistency workflow, targeted
reproduction harness usage, and relevant process-gate checks. This is contributor-intake hygiene;
it does not run the certificate suite or evaluate any research claim.

## Contributing guidance gate

`contributing_guidance_audit.py` checks that `CONTRIBUTING.md` still names the claim-grading
discipline, claim-status consistency workflow, repository placement map, and licensing
boundaries, and that those referenced repo paths exist. This is contributor-process hygiene;
it does not edit contributor policy or evaluate any research claim.

## Issue-template validation gate

`issue_template_validation_audit.py` checks that `.github/ISSUE_TEMPLATE/*.yml`
keeps source-path references on the live `lab/sources/` surface and preserves the
bounded-problem, six-axis specification, reference-routing, and media-provenance
guardrails for public issue intake. This is contributor-intake hygiene; it does not
run the certificate suite or evaluate any research claim.

## GitHub README surface-map gate

`github_readme_surface_map_audit.py` checks that `.github/README.md` names the live pull
request template, issue templates, and lightweight workflow file, uses local links that
resolve from `.github/`, and preserves the boundary between contributor intake and research
status movement. This is contributor-ops hygiene; it does not run the certificate suite or
evaluate any research claim.

## README entrypoint map gate

`readme_entrypoint_map_audit.py` checks that the public root README's Start Here
pointers remain complete and that the Repository Layers section has exactly one
bullet for each top-level public surface, with `lab/` and `Lean/` routed through
the non-root surface paragraph. This is a navigation/process guard only; it does
not validate research claims.

## NEXT-STEPS front-door guard

`next_steps_frontdoor_guard_audit.py` checks that `NEXT-STEPS.md` remains a
roadmap, preserves the Firewall-Boundary attack-not-defend front door, routes
older-status promotion through the claim-status workflow, and keeps the
research-posture contributor pointer. This is roadmap/process hygiene only; it
does not parse formula-like links, edit roadmap content, or validate research
claims.

## DE-AMP diagnostic closure gate

`de_amp_diagnostic_closure_audit.py` checks that the H46B source-input certificate,
H46C amplitude re-solve, W129 OQ2 band sweep, and DE-AMP closure note remain wired as
diagnostic evidence rather than prediction evidence. This is provenance and closure
hygiene only; it does not rerun the cosmology certificates, edit the portfolio, or
change any verdict, claim status, canon surface, or public posture.

## Recovery contract manifest gate

`recovery_contract_manifest_audit.py` checks that the first RECOVERY-CONTRACT construction
manifest remains process-grade only, keeps sector combination underdefined, preserves the
W203/W229/W230/W236 source-action boundaries, refuses to consume the corrected
finality-polarity adapter as an independent return, and avoids local home-path leaks. This
is an overclaim-boundary guard only; it does not validate GU physics or change claim status.

## Recovery contract action fingerprint gate

`recovery_contract_action_fingerprint_audit.py` checks that the RECOVERY-CONTRACT action
fingerprint remains process-grade only, names the W203/W229/W230/W236 branch-local source-action
family, preserves the W154 / c_kin = 0 posit boundary, separates forced/free/imported quantities,
limits allowed reductions to branch-local use, and avoids local home-path leaks. This is an
overclaim-boundary guard only; it does not validate GU physics or change claim status.

## Decider README inventory gate

`decider_readme_inventory_audit.py` checks that `tests/decider/README.md` names every direct
`tests/decider/*.py` certificate and preserves the explicit not-forced / gated boundary for the
single-decider family. This is a map and posture guard only; it does not run the decider scripts
or change verdicts.

## Generation-sector README inventory gate

`generation_sector_readme_inventory_audit.py` checks that `tests/generation-sector/README.md`
names every direct `tests/generation-sector/*.py` certificate and preserves the frozen,
paper-cited, not-verdict-changing boundary for the generation-sector family. This is a map and
posture guard only; it does not run the generation-sector scripts or change verdicts.

## GU-independent README inventory gate

`gu_independent_readme_inventory_audit.py` checks that
`tests/gu-independent/README.md` names every tracked direct GU-independent Python
certificate and preserves the structural no-go / external-index /
no-claim-status-movement boundary. This is a map and posture guard only; it does
not run the GU-independent scripts or change verdicts.

## Enum-completeness README inventory gate

`enum_completeness_readme_inventory_audit.py` checks that
`tests/enum-completeness/README.md` names every direct and nested enum-completeness Python
certificate and preserves the delimited-class / no-canon-promotion /
not-a-physics-derivation boundary around the publication-gating enumeration family. This
is a map and posture guard only; it does not run the enum-completeness scripts or change
verdicts.

## Forcing-slot README inventory gate

`forcing_slot_readme_inventory_audit.py` checks that
`tests/forcing-slot/README.md` names every direct forcing-slot Python
certificate and preserves the toy-model / stabilized-source /
not-a-GU-derivation / not-a-verdict-change boundary around the forcing-slot
screen. This is a map and posture guard only; it does not run the forcing-slot
scripts or change verdicts.

## Carrier-mass README inventory gate

`carrier_mass_readme_inventory_audit.py` checks that `tests/carrier-mass/README.md`
names every direct carrier-mass Python certificate plus the local JSON output, and preserves
the vectorlike zero-not-three / action-gated boundary for the carrier-mass family. This is a
map and posture guard only; it does not run the carrier-mass scripts or change verdicts.

## Carrier-bit decision README inventory gate

`carrier_bit_decision_readme_inventory_audit.py` checks that
`tests/carrier-bit-decision/README.md` names every direct carrier-bit Python
certificate and Markdown analysis, and preserves the bit-narrowed-but-open /
SG4 / no-status-movement boundary for the carrier-bit campaign. This is a map
and posture guard only; it does not run the carrier-bit scripts or change
verdicts.

## Escape-corners README inventory gate

`escape_corners_readme_inventory_audit.py` checks that
`tests/escape-corners/README.md` names every tracked direct escape-corners
Python certificate, Markdown analysis, and checked-in run log, and preserves
the SG4 / no-status-movement boundary for the escape-corners campaign. This is
a map and posture guard only; it does not run the escape-corners scripts or
change verdicts.

## Hessian/Z3 README inventory gate

`hessian_z3_readme_inventory_audit.py` checks that `tests/hessian-z3/README.md`
names every direct Hessian/Z3 Python certificate and preserves the proxy,
action-gated, not-forced boundary for the carrier-occupancy family. This is a
map and posture guard only; it does not run the Hessian/Z3 scripts or change
verdicts.

## Internal-paths README inventory gate

`internal_paths_readme_inventory_audit.py` checks that
`tests/internal-paths/README.md` names every tracked internal-path Python
certificate and preserves the target-free / source-action-gated /
not-forced boundary around the OQ-RK1, Y14 bundle, signed-readout, and
Sp-family anomaly checks. This is a map and posture guard only; it does
not run the internal-path scripts or change verdicts.

## Symbolic-proofs README inventory gate

`symbolic_proofs_readme_inventory_audit.py` checks that
`tests/symbolic-proofs/README.md` names every tracked symbolic-proof Python
certificate and preserves the symbolic / not-a-verdict-change /
no-formalization boundary around the core theorem identity checks. This is a
map and posture guard only; it does not run the symbolic-proof script or
change verdicts.

## Chase README inventory gate

`chase_readme_inventory_audit.py` checks that `tests/chase/README.md`
names every nested MOVE-1..MOVE-5 chase Python script and preserves the
terminal-verdict / independent-reverification / not-GU-derivation boundary.
This is a map and posture guard only; it does not run the chase scripts or
change verdicts.

## Relocated surface path hygiene

Repository process, automation, and active-research owner surfaces now live under `lab/`.
Process gates should point at current `lab/process/`, `lab/automation/`, and
`lab/active-research/` paths when checking live owner surfaces. Historical exploration
artifacts may still quote older path strings as provenance. Do not rewrite those mechanically
unless the selected gate depends on them as current executable inputs.

Remaining content failures are governance debt to fix or retire separately; they are not
introduced by the path repair.
## Resolver Wave B scope gate

`resolver_wave_b_scope_audit.py` checks that the internal `P_hinge` projector
never becomes the external P3 count datum, the finite-kinematic fences survive,
the route disposition is `REBASE`, and P1/P2/P3 remain unchanged and unused.
It does not validate the representation calculations or move a scientific bar.

## Resolver Wave C scope gate

`resolver_wave_c_scope_audit.py` keeps the bare `16x144` tensor separate from
the conditional complex-linear dualized Hom factor, records the internal real
252 rather than two real 126s, rejects the raw Lambda5-to-Sp-connection
shortcut, requires the admissible placement and dim-13 receiving geometry to
remain open, and prevents order-three torsion from becoming integer P3. It does
not validate the character calculations or build a mass.

## Resolver Wave D scope gate

`resolver_wave_d_scope_audit.py` preserves the distinction between a native
grade-six connection coefficient, its real-252 effective kernel, the total
ordered K/C/P0/Y bilinear, and the separate one-form-output comparator with
its desired 144 component and paired 16-dimensional companions. It requires
moving full-Sp descent, source selection, VEV, mass, and P1/P2/P3 to
remain open and does not reproduce the mathematical certificates.

## Resolver Wave E scope gate

`resolver_wave_e_scope_audit.py` preserves the native full-14 `9I` result
against the vertical `5I` comparator, requires the source-to-active port to
remain open, and keeps the source-silent unweighted reconstruction separate
from the one-simple-blade half-weight candidate. It fences the displayed
source kappa term and affine comparator from the joined and total
Shiab/fermion/bridge Euler residuals. It also requires representation-wide
half-weight, full `G2/Y/P0`, actual `Y14` Zorro descent, VEV, mass, quotient,
domain, no-leakage, and P1/P2/P3 to remain open.

## Resolver Wave F scope gate

`resolver_wave_f_scope_audit.py` preserves the distinction between the fixed
`1/9` projector on an already grade-six exterior carrier, the missing `q6`
and actual source `U_(Theta,epsilon)`, and the separate downstream full-20
placement. It records the full real exterior Hom-space as four-dimensional
and `[a:b]` as only its star-even subansatz. It requires public native-`Sp`
reduction, actual tilted `epsilon_src` split descent, `Theta_Z` overlap/Riesz,
transverse Euler closure, complete Shiab/fermion selection, VEV, mass,
quotient, domain, no-leakage, and P1/P2/P3 to remain open. It also prevents
the isolated `AUXILIARY_CAN_FORCE` comparator from becoming source ownership
or coupled nonpropagation, and prevents an arbitrary vectorlike `chi=0`
object from becoming a canonical KO/index basepoint.

## Resolver Wave G scope gate

`resolver_wave_g_scope_audit.py` preserves the distinction between the exact
fixed-reduction native `q6`, the local rank-252 composite, the moving
conjugated projector family, and the still-missing public source port. It
requires the five-intertwiner Sage census and grade-ten near-miss to remain
visible; records that a frozen projector is not full-`Sp` equivariant; and
keeps the chosen-`A0=0` tilted first-jet fixture and `GL(2)` frame surrogate
separate from a combined `Psrc(T_omega)` and actual `Theta_Z`/Zorro
nonconstant overlap descent. It also keeps the global density/Krein adjoint,
source variation domain, total active/transverse Euler, Ward/Green data,
domain, no-leakage, and P1/P2/P3 open.

## Resolver Wave H scope gate

`resolver_wave_h_scope_audit.py` preserves the Layer-0 real-form fork between
the public U-type source presentation and native right-`H` Sp geometry. It
requires `J_red` to remain a chosen, source-silent local reduction field; the
Reynolds map to be restricted to the explicitly typed real public `u(K)`
carrier; public covariance to move the codomain to `sp(K,J_h)`; and the map
to remain non-homomorphic. It keeps the rank-252 `Psrc(T_omega)` and projector
first jet local/fixed-coindex, and prevents the auxiliary quadratic from
becoming the displayed source action or an Euler covector. Actual
`Met(X)`/`Theta_Z` descent, source-action variation, total Euler tangency,
global density/Krein adjoints, Ward/Green/domain, observation no-leakage, and
P1/P2/P3 coupling remain open. It does not reproduce the Clifford, matrix,
Sage, source, or symbolic first-jet certificates.

## Resolver Wave I scope gate

`resolver_wave_i_scope_audit.py` preserves the local connection-induced
Theta reconstruction/global source-owned Theta boundary, raw `C*` versus
Riesz-raised `C` first-leg law, chosen Wave-H `(9,5)` versus live rival
`(7,7)` branch, and coherent Spin lift versus planted sign inconsistency. It
requires the rank-252 projector to remain an associated
`flat Psrc_raised sharp` family on a pointwise local fixture; keeps the A9F
rank-128 hinge, both tilted-connection assembly, actual source variation,
Euler/Ward/Green/domain, no-leakage, and external-ledger P1/P2/P3 open; and
does not reproduce the symbolic, Clifford, source, or 128-by-128 certificates.

## Resolver Wave J scope gate

`resolver_wave_j_scope_audit.py` preserves the distinction between the
pointwise already-composed scalar-density fixture and the displayed B1
action; the cyclic coefficient comparator and native Euler covector; the
finite Green/`GL(2)` covariance fixtures and native preboundary/Ward objects;
and the `Omega1` source port versus the `Omega2` quadratic coefficient. It
records the exact `R_J([m,m])` coset-curvature obstruction while requiring
both corrected-reduced and full-public/projected-residual port orders,
bosonic and total tangency, native Shiab, monolithic B1, domain, no-leakage,
and P1/P2/P3 coupling to remain open. It does not reproduce the exact
Clifford, matrix, source, transport, or moving-geometry certificates.

## Resolver Wave K scope gate

`resolver_wave_k_scope_audit.py` preserves Curt/Eric's exact source-typed
`(7,7)` arithmetic alongside the distinct conditional-active `(9,5)` branch,
forbids dualization from changing inertia, and keeps the real Clifford forms
separate. It requires the raw displayed Shiab word to remain outside `R_J`
unless public-`u(K)` typed, the active grade projection to remain
repository-derived, the normalized trace to remain `e10`, and the live exact
defect to remain scoped to the repository `q_wedge` comparator. It forbids
promoting that result to a source `[T,T]` obstruction, an owner cancellation
to a Ward theorem, or one port fixture to global descent. It also preserves
the source's fundamental-nonchirality/effective-chirality distinction and
keeps K77 real spinors, atomic particle mapping, the decoupling theorem,
domain, physics, and P1/P2/P3 open.

## Resolver Wave K77-A scope gate

`resolver_wave_k77a_scope_audit.py` preserves the exact real
`Cl(7,7)=M128(R)` carrier, the four complex `2 x 16` observation blocks, the
invariant cross-half pairing, and the one-family representation/charge packet
without importing any right-`H`/quaternionic `(9,5)` structure. It requires
every one of the 37 atomic physics rows to retain its program-mandatory,
SM-shadow, or source-lane obligation separately from moving candidate status,
and enforces the ordered
fixture/map/mechanism/lane/program kill ladder. It keeps Eric/Curt source
descriptions as locators rather than proofs, fences the stale exterior-spinor
construction, fences stale fixed-`c(v)` and `R128 -> C64` claims, preserves
the vertical `KX` channel as classified but unselected, downgrades F/Q/Z to
source arithmetic until actual K77 projectors exist, kills only the
three-block-to-three-generation map, and requires physical
action, VEV, observation, domain, pole/residue, count, dark-sector identity,
and P1/P2/P3 use to remain open.

## Resolver Wave K77-B scope gate

`resolver_wave_k77b_scope_audit.py` preserves the draft-internal normalization
`T wedge T = one-half [T,T]_graded`, distinguishes the literal raw
associative-product Shiab from the source-permitted commutator/`i`-symmetric
family, and retains the exact raw-adjoint-codomain counterexamples. It requires
the six live low-grade channels to remain failed on the same-action endpoint
bank and the two zero-defect channels to remain explicitly vacuous. It keeps
the high-grade invariant copies and full Phi family open, forbids promotion
from a constant algebraic fixture to derivative/Green, Euler/Noether/BV,
domain, observation, or physics, and holds the result at candidate-map rather
than mechanism/lane/program scope. P1/P2/P3 remain unused.

## Resolver Wave K77-B2 scope gate

`resolver_wave_k77b2_scope_audit.py` preserves ambient adjoint curvature
versus the algebraic Riemann submodule, algebraic versus differential versus
historical Bianchi, and ambient versus observed versus Frobenius-fibre trace
reversal. It requires the exact `3185=1+104+3080` decomposition and target
multiplicities `2,2,0`, forbids using Weyl-killing as a uniqueness selector,
and holds the complete K77-B source-inspired factorized repair-family kill to
the joint ambient-Einstein/same-action burden. It preserves the two-coordinate Riemann-
restriction construction at pointwise fixed-frame grade while requiring its
associated-bundle descent, full-domain extension, executable grammar typing,
bounded expression-DAG census, differential Bianchi/Green, moving fields,
observation, physics, and P1/P2/P3 use to remain open. It forbids promotion from displayed
ansatz to bounded grammar, K77 lane, or conditional-program scope.

## Post-K77-B2 eight-wave rendezvous scaffold gate

`k77_post_b2_next_eight_wave_scaffold_audit.py` fail-closes the council's
campaign sequence rather than a mathematical result. It preserves K77 as the
primary source-faithful real `(7,7)` construction and the active `(9,5)`
right-`H` work as a distinct rival implementation/negative-test bank; requires
K77-B3 to be the last isolated selector wave; and checks eight sequential named
gates through a common action, Ward/BV, observation, local-physics, domain,
vacuum, fermion/count, and frozen integrated-acceptance interface. It also
requires the D1 receiving-arrow boundary, early atomic-ledger regrading,
Wave-4 breadth reset, ten specialist lenses, and exact held-out certification
for any ML-assisted search. It makes no scientific, canon, lane, public-
posture, or P1/P2/P3 status change.

## Resolver Wave K77-B3 scope gate

`resolver_wave_k77b3_scope_audit.py` fail-closes the exact distinction between
the full equivariant Hom, its grade-two low/high coordinates, and the two
ambient-Einstein restriction coefficients tested by the cyclic-kernel
witnesses. It records a zero-order linear mechanism kill and forbids promotion
to a K77, `(7,7)`, gravity, source-action, domain, or physics kill. It also
requires the source-normalized one-third quadratic comparison, preserves the
unidentified observed and Frobenius-fibre trace reversals, leaves Green/domain
not reached, keeps P1/P2/P3 unused, and moves the campaign frontier to the
derivative-or-moving-field common action/current/Riesz/Ward rendezvous.

## K77 Wave 2 action/current/Riesz/Ward scope gate

`k77_wave2_action_ward_scope_audit.py` requires the primary architecture to
use the written action's actual symmetrized Euler derivative, emit `J_D+J_F`
once without a second current bridge, and keep the Hodge/invariant-pairing map
at indefinite pointwise pseudo-musical grade. It preserves the distinction
between the complete even local-IG Ward contraction and the source
`Xi=D Upsilon` redundancy equation, prevents gauge covariance from selecting
the bridge policy, and records the real mixed rolled bracket as partial
`TG-1` only. `TG-2`, `TG-3`, source-group/Krein compatibility, observation,
domain, vacuum, physics, and P1/P2/P3 remain open; the campaign frontier stays
on the same named Wave-2 gate.

## K77 Wave 2 Dirac--de Rham/super-IG rebase scope gate

`k77_wave2_dirac_derham_superig_rebase_scope_audit.py` fail-closes the
five-object Layer-0 split between ordinary de Rham Dirac, truncated chain,
rolled seesaw operator, displayed draft matrix, and unreleased cyclic
completion. It requires the exact `1920/1920/1024` symbol ranks and 896 null
kernel, retains the bare-middle adjoint failure and conditional nonchiral
cross-pairing, and recognizes the source correction from a mandatory odd
action/Ward to an algebraic super-IG extension. It preserves Curt's three
kinematic pieces without a count inference, keeps full source-group/global
descent and the draft-9.16/Krein/preboundary/domain placement open, and
forbids observation, physics, P1/P2/P3, lane, canon, or public-posture
promotion.

## K77 Wave 2 draft-9.16/primalizer-template scope gate

`k77_wave2_global_draft916_krein_preboundary_scope_audit.py` preserves the
identity-grade page-46 matrix while fail-closing the distinction between the
local source bilinear, a density-dual operator, its Hodge/Krein primalizer,
the primalized formal adjoint, a candidate variational core, and a physical
domain. It requires the `(7,7)` Hodge signs, exact general/finite template
receipts, model labels on overlap/current/Ward fixtures, and the corrected
gamma-trace splitting. It keeps the actual sixteen-block D916 assembly,
`rho(epsilon)` descent, common connection variation, observation, physics,
families, and P1/P2/P3 open, and prevents the campaign from advancing beyond
Wave 2.

## K77 Wave 2 actual-carrier D916 rival scope gate

`k77_wave2_actual_draft916_blockwise_scope_audit.py` requires the exact
section-11.2 ambient half-spinor source receipt and the zero-solution parity
obstruction before permitting the total grading to be called only a
conditional rival.  It requires the corrected inverse-trace weights and
noncompact Spin-equivariance control for the algebraic bracket, preserves the
moving three-patch witness at conditional reduction grade, and refuses to
promote one connection-current direction to the complete shared-core
variation.  It keeps zero-order coefficients, full multi-index adjoint,
full-source-group descent, observation, physics, families, and P1/P2/P3 open;
the campaign remains on Wave 2 with the source-sign/duality/Shiab-parity
reconciliation as its next build.

## K77 Wave 2 source-sign/Shiab/degree-reality reconciliation scope gate

`k77_wave2_source_sign_shiab_duality_scope_audit.py` requires the released
source dispositions, exact `D7` Hom dimensions `(0,2)`, zero barred-row-only
solutions, two full degree-reality sign solutions, no bare half-spinor flip,
and the one vector-supplied flip channel. It requires both exact moving-`q`
repairs, the fixed-`q` failure, surplus `-14`, the material hostile-review
correction, and append-only correction of the predecessor Runtime revision
typo. It keeps `q` source ownership, placement, full adjoint/current/Ward,
full-`H` descent, observation, physics, and P1/P2/P3 use open while holding
Wave 3 closed.

## K77 Wave 2 trace-q ownership / adjoint / Ward scope gate

`k77_wave2_q_receiver_trace_adjoint_ward_scope_audit.py` requires the
source-confirm/source-silent split, exact tautological DeWitt-negative trace
receiver, corrected Clifford-vector type, full form-index/spinor left-right
adjoint exchange, nonzero `dq` and actual even connection-direction currents,
Ward selection rank zero, and the surplus change from `-14` to `-1`. It also
requires the hostile-review repairs separating the coefficient-algebra magic
bracket from the Clifford placement and replacing floating or coefficient-only
fixtures. It keeps zero-order reality, moving Hodge/pairing/density, full-`H`
descent, domain, observation, physics, Wave 3, and P1/P2/P3 use open.

## K77 Wave 2 trace-q coefficient / zero-order reality scope gate

`k77_wave2_trace_q_coefficient_zero_order_reality_scope_audit.py` requires the
full sixteen-cell `q=g/2` assembly, Curt Iceberg placement plus Weinstein's
two-layer correction, native reality selection rank zero, the source-faithful
projective surplus `-1`, and the empty optional Majorana rival on the current
full-index family. It forbids promotion to a commutator/anticommutator result,
keeps the restricted Higgs orbit and barred/unbarred adapter open, and requires
the common two-layer action Euler system before Wave 3 can open.

## K77 Wave 2 common two-layer action / coefficient-selection scope gate

`k77_wave2_common_two_layer_action_scope_audit.py` requires the source-confirmed
two-layer norm-square architecture and unfinished cancellation burden, while
keeping the exact K77 path identification and independent target
source-silent. It checks fixed-coupling selection rank zero on the first-order
locus, literal middle-cancellation rank two, all-covector anticommutator
scalarity, quadratic square span rank three, field-dependent optional-modulus
roots, surplus `-1`, and the full-moving-action scope fence. It keeps the
up/back/over adapter, target, observation, physics, Wave 3, and P1/P2/P3 open.

## K77 Wave 2 up/back/over target scope gate

`k77_wave2_up_back_over_target_scope_audit.py` requires the source-bounded
two-connection square, unique two-minus sign fixture, and universal
Bose--Fermi totalization while preserving the unreleased/caveated source
boundary. It requires full rank two for both direct K77 trace-`q` path signs
and limits that result to a candidate-map kill. Stabilized action-derived
cross maps `U,V`, target matching, observation, physics, Wave 3, and P1/P2/P3
remain open.

## K77 Wave 2 stabilized mixed-cross-map scope gate

`k77_wave2_stabilized_mixed_cross_map_scope_audit.py` requires equation `10.10`
to remain a rectangular deformation-to-Euler complex, the common-action raw
mixed Hessian blocks to retain their density-dual codomains, and the finite and
frozen-K77 reciprocity receipts to pass. It separates coefficient sensitivity
rank two from selection rank zero, requires the primalizer-dependence control,
and forbids direct entrywise matching to the two-connection square without a
typed comparison functor. It keeps full sixteen-cell closure, global
primalizers, observation, physics, Wave 3 and P1/P2/P3 use open.

## K77 Wave 2 mixed-primalizer / two-connection comparison scope gate

`k77_wave2_mixed_primalizer_comparison_scope_audit.py` requires the actual
real-K77 density/Krein four-field inverse, its moving-inverse identity and its
form-frame plus Spin-transition naturality. It requires the source correction
from a bosonic target to an unreleased fermion-cyclic completion/rival, the
typed one-way `0+13 -> 1+14` Hodge roll, and the slot/principal-order mismatch
with D916. It keeps the reverse arrow, cyclic pair, action/Helmholtz owner,
general chain relation, global analytic domain, coefficient selection,
observation and physics open; P1/P2/P3 remain unused and Wave 3 remains closed.

## K77 Wave 2 shifted two-connection / action-shell scope gate

`k77_wave2_two_connection_action_owner_scope_audit.py` requires the internal
shift, both algebraic parity restrictions, the complete square with live
noncommutative mixed defect, the pre-existing `I1B` action/source correction,
the exact path-average `1/2,1/3` transgression controls, and the diagonal-shell
versus action-shell mismatch. It forbids identifying `I1B` with the unreleased
2025 operator, keeps the actual moving K77 Shiab and bosonic Euler primalizer
open, requires zero transgression surplus and trace-`q` surplus `-1`, and keeps
P1/P2/P3 unused and Wave 3 closed.

## K77 Wave 2 Euler-shell dependent-pair scope gate

`k77_wave2_euler_shell_two_connection_scope_audit.py` requires the existing
indefinite K77 density/adjoint pseudo-musical, dimension-one restricted
natural-map class, actual rather than advertised Euler owner, and dependent
pair `A_E=B+sharp_conn(E_T^{B,act})`. It requires the complete square with
both off-shell defects and the bidirectional shell theorem only on a faithful
coefficient module. It enforces source silence, zero surplus,
`free_object_delta=-1`, full-field Ward/domain/observation debt, P1/P2/P3
non-use, and closed Wave 3.

## K77 Wave 2 Euler-lift observation receiver scope gate

`k77_wave2_euler_lift_ward_observation_scope_audit.py` requires the exact
detector `rho_X sharp_X O_E`, separately realized equation-leakage and
representation-blindness false shells, and the repaired restricted converse
only under no-leakage plus faithfulness on the observed connection-difference
image. It preserves source silence for the receiver theorem, finite/model
grades for Ward and preboundary checks, zero selector parameters,
`free_object_delta=0`, the actual `Y14` receiver/BV/common-domain debt,
P1/P2/P3 non-use, and closed Wave 3.

## K77 Wave 2 augmented-torsion four-plus-ten receiver scope gate

`k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit.py` requires
the primary-source collision on augmented torsion and pullback, the existing
pullback-plus-vertical coefficient field map, its exact rank-fourteen inverse
and inverse-transpose Euler receiver, and the degree-thirteen four-plus-ten
bigrading. It checks the nonzero-`kappa` conormal source-action witness while
restricting the kill to automatic horizontality on the displayed full local
translation stratum. It forbids promotion to a localized nonlinear action,
physical Higgs, tilted Ward/BV descent, common Green domain, datum use,
physics movement or Wave 3, and requires the successor gate to own the full
moving defect-action weld.

## Wave disposition schema gate

`wave_disposition_schema_audit.py` requires every wave/cycle disposition artifact to
declare, in frontmatter, what it assumed and what it left open: `fork_assumed:` (the
Layer-0 horn the wave stands on, or `none`), `search_space_dim:` (an integer or stated
expression, or `not_computed` with a `search_space_dim_reason:`), `free_object_delta:`
(new un-owned objects introduced minus retired), and `residue_touched:` (conditional-match
ids each carrying a T0-T4 constrainedness grade, or `none`). These are the 2026-08-04
program-efficiency council's PRE-1/PRE-2/PRE-3 and POST-1/POST-2 questions made mechanical.
The discovery rule is stated in the script docstring and is a three-clause union - placement
plus `-disposition-`/`-rebase-` naming under `explorations/cycle-gates-and-audits/`, a
declared wave `doc_type`, or a declared `route_disposition:` key anywhere under
`explorations/` - and the gate fails if any clause stops matching. Grandfathering is dated:
artifacts whose effective creation date precedes `SCHEMA_CUTOVER` (2026-08-05) are reported
as `legacy` and never fail, the legacy count is printed on every run so the backlog stays
visible, and a legacy artifact that opts into a field must still declare it well-formed.
Effective creation date is the maximum of every date the artifact declares about itself and
its git add date, so backdating a filename does not buy an exemption. This is a disposition-
shape guard only; it reads files as data, executes nothing, and evaluates no research claim.

## Layer-0 fork registry / fork-stack depth gate

`fork_depth_audit.py` checks `lab/process/layer0-fork-registry.yaml` and then counts how deep
the wave queue has stacked on forks that registry still calls open. The registry carries one
row per Layer-0 fork - stable id, the horns, status, fan-out, sources, and for a settled fork
which side won, how, when, and by which artifacts - and the gate requires every cited path to
resolve, refuses half-settled rows, and pins a minimum set of fork ids so a row cannot be
quietly deleted. It also pins the record of the program's one measured queue defect: the
`Cl(7,7) = M128(R)` vs `Cl(9,5) = M64(H)` real-form fork was settled at Wave K after seven
waves had been built on the other horn. The depth counter reads `fork_assumed:` declarations,
resolves each against the registry, and requires an explicit `fork_stack_acknowledged:` with a
stated reason on every disposition past `fork_stack_threshold` (default 3) on a still-open
fork. Proceeding on an undetermined fork is not refused - the acknowledgment is what becomes
mandatory, so the cost lands in the record instead of staying invisible. Working on a
different fork in between does not reset the counter; settling the fork does. This is a queue-
discipline guard only; whether a settlement is mathematically correct is the settling
artifact's business, not this gate's.
