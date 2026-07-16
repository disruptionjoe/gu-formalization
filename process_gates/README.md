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
- `lab_active_research_readme_surface_map_audit.py`
- `lab_automation_readme_surface_map_audit.py`
- `lab_deep_research_readme_surface_map_audit.py`
- `lab_process_readme_surface_map_audit.py`
- `lab_process_runbooks_readme_inventory_audit.py`
- `lab_readme_surface_map_audit.py`
- `lab_sources_readme_surface_map_audit.py`
- `lab_specifications_readme_surface_map_audit.py`
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
- `next_steps_frontdoor_guard_audit.py`
- `pati_salam_readme_inventory_audit.py`
- `papers_candidates_readme_inventory_audit.py`
- `papers_readme_lifecycle_map_audit.py`
- `primary_gu_interface_contract_audit.py`
- `process_gate_readme_inventory_audit.py`
- `protected_surface_diff_audit.py`
- `pull_request_template_validation_audit.py`
- `public_path_hygiene_audit.py`
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
