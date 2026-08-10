# process_gates

Governance / consistency / prose-discipline audits, relocated here from `tests/` in the
2026-06-30 de-theater pass so that `tests/` is reserved for files that build a mathematical
object and compute a number/rank/dim/index.

These files assert **documentation and status discipline** (posture wording, claim-DAG
consistency, allowed/forbidden provenance inputs, "no overclaim" checks, Lean-surface presence,
etc.) - they do **not** perform mathematics. A green run here means the prose/governance
contracts hold; it says nothing about whether a GU claim is mathematically checked. For that,
see `tests/` (real computations) and `tests/chase/` (verified verdict scripts).

Current correction gate:

- `p3_normal_tangential_support_audit.py` enforces ledger v0.148's exact
  actual-base pullback obstruction, normal-versus-horizontal form-slot fence,
  internal-gauge kill, re-scoped abstract `S4` theorem, unchanged accounting
  and tangential-support-or-soldering successor before action restriction.

- `p3_spin_bundle_diagonal_audit.py` enforces ledger v0.147's exact P3/chiral-
  spin bundle class match, topology-versus-connection fence, five-dimensional
  arbitrary ASD moduli, zero homogeneous invariant deformations, unchanged
  accounting and connection-preserving support-pullback successor.

- `p3_selfdual_source_reduction_audit.py` enforces ledger v0.146's exact
  split-versus-factor distinction, two rank-three `su(2)` components,
  current-action self-dual revival kill, unbuilt P3/source diagonal and
  restricted-action Euler/BV/domain successor.

- `p3_native_characteristic_pairing_audit.py` enforces ledger v0.145's exact
  zero native quadratic pairings, direct P3 horn kill, nonzero-but-unowned
  self-dual reduction control, unchanged accounting and action/BV reduction
  successor.

- `p3_characteristic_amplitude_selector_audit.py` enforces ledger v0.144's
  conditional characteristic-class magnitude selector, the current
  auxiliary-P3/source-connection Layer-0 fence, fixed-versus-free pairing
  distinction, remaining sign, unchanged accounting and parentwise
  source/P3-diagonal successor.

- `global_projector_amplitude_layer0_audit.py` enforces ledger v0.143's
  separation of conditional constant-shift screening from nonzero VEV
  amplitude selection, unchanged accounting, and amplitude-dependent global
  compatibility/domain successor.

- `zero_fermion_vev_selector_exhaustion_audit.py` enforces ledger v0.142's
  prior-art correction, exact rank-two source family, one amplitude, local
  ten-component trace cancellation, pointwise-Hessian Layer-0 fence,
  classical symplectic/BFV no-selector scope, unchanged accounting and global
  normalization/domain successor.

- `zero_fermion_coupled_hessian_current_order_audit.py` enforces ledger
  v0.141's exact zero current/mixed-Hessian ranks, live fermion block, cubic
  `dD/db` vertex, unchanged rank-one trace and accounting, hostile
  symplectic/analytic fences, and split bosonic/nonzero-fermion successor.

- `degree_duality_pair_graph_gate_audit.py` enforces ledger v0.140's exact
  bare-q RS leakage, Pin-completed W/mirror exchange, rank-384 closure,
  source-sign joined-rank-256 upper obstruction, unchanged accounting and
  sign-cluster stopping rule.

- `southeast_zero_graph_gate_audit.py` enforces ledger v0.139's exact unique
  rank-64 upper graph, zero induced W/mirror action, rank-64 action-tied
  lower-left obstruction, source-faithful sign/duality fence, unchanged
  accounting and replacement-Shiab/adapter successor.

- `four_field_zero_order_port_audit.py` enforces ledger v0.138's exact
  parent-specific rank-64-in-rank-128 port theorem, unique projective ratios,
  source-full coefficient conflict, hostile graph/BV/domain fence, unchanged
  accounting and graph-Riccati/lower-left successor.

- `action_owned_leakage_composition_audit.py` enforces ledger v0.137's exact
  composition: every named parent retains a certified leak witness, the
  nonzero-branch pointwise action Hessian has no radical on their grades, the
  field-tangent escape closes, and four-field/BV/domain/adapter scope remains
  (`21/21`).

- `zero_order_w_mirror_parent_leakage_audit.py` enforces ledger v0.136's
  exact q-repaired zero-order cross/outside-pair leakage ranks, W/mirror
  symmetry, moving-Spin/two-half/source-full parent distinction, hostile
  analytic/symplectic scope fence, unchanged accounting and action-orbit/BV
  successor.

- `induced_fermion_principal_discriminator_audit.py` enforces ledger v0.135's
  exact K77 principal symbol anchors, W/mirror `224/96` equality, natural-sector
  half-kernel rule, planted random controls, lower-order parent-ablation fence,
  hostile symplectic/analytic review, unchanged accounting and draft-9.16
  zero-order successor.

- `nonzero_branch_parent_hessian_audit.py` enforces ledger v0.134's complete
  `229,376`-direction pointwise Hessian census, zero radical on both parent
  decompositions, two-half/full-U/moving-Spin Layer-0 fences, hostile and
  symplectic review, unchanged accounting, and the induced K77 Dirac/RS
  successor.

- `bosonic_parent_action_ownership_audit.py` enforces ledger v0.133's
  zero-branch full-norm result, the distinct `B`-adjoint and Weyl reductions,
  the hostile scope fence, unchanged accounting, and the dependency order
  nonzero-branch normal Hessian then induced K77 Dirac/RS operator.

- `action_owned_reduction_carrier_typing_audit.py` enforces ledger v0.132's
  connection-versus-fermion Layer-0 separation, local-linearized consistency
  scope, two-step Build queue, unchanged accounting and hostile-review fence.

- `exploration_absorption_priority_canon_audit.py` enforces ledger v0.131's
  six distance-only carrier-scope migrations, conditional fixed-`W` banners,
  unchanged accounting, action-owned carrier-discrimination priority, neutral-
  state anti-inflation fence and current functional-contract pointer.

- `selected_k77_moving_parent_bundle_observation_reduction_audit.py` enforces
  ledger v0.130's exact moving-projector rank/cocycle/Euler descent, global
  totals `113,893/229,477`, `8,192+8,192` block/coset typing, observation-value
  counts `32,613/65,637`, no observation parent selection, action-ownership
  fence, unchanged accounting and hostile-review scope.

- `selected_k77_grade5_unitary_parent_euler_closure_audit.py` enforces ledger
  v0.129's exact grade graph, failure of grade `1+2+5` closure, complete-grade
  Spin total `113,893`, unitary-covariant total `229,477`, non-collapse of the
  two-half/full-U symmetry and pairing fork, unchanged accounting, and all
  hostile scope fences.

- `selected_k77_complete_euler_jet_tangent_closure_audit.py` enforces ledger
  v0.128's observed `594 -> 810` and full-Y14 `594 -> 1250` first-jet closure,
  total tangents `1,131/1,571`, correctly typed unsymmetrized Euler owner and
  scalar covector, conditional conormal restriction, unchanged accounting and
  grade-five/two-half/full-unitary parent fences.

- `selected_k77_observation_stabilizer_subbundle_audit.py` enforces ledger
  v0.127's dependency-hashed rank-594 bank, all-51-generator stabilizer
  invariance, natural `160+180+60+184+10` decomposition, `594 -> 727` ambient
  scope plant, conditional observation reduction, unchanged accounting and
  unitary-parent fence.

- `selected_k77_minimal_hessian_tangent_closure_audit.py` enforces ledger
  v0.126's `89 -> 174 -> 464 -> 594` object/scope separation, total tangent
  `915`, full-`X^4` and both-branch closure, no full-`1,571` promotion, no
  invented Noether/BV quotient, unchanged accounting and unitary-parent fence.

- `selected_k77_moving_metric_first_action_hessian_audit.py` enforces ledger
  v0.125's local-principal selected-Spin `9/9/4` metric ranks, inherited
  `91/6/88` epsilon ranks, co-moving/stationary scope, no unitary-parent port,
  no quotient or 1,571 promotion, unchanged accounting and hostile fences.

- `k77_exact_bank_api_audit.py` enforces ledger v0.124's canonical exact bank,
  29 current dependency hashes, nonrecursive consumer, selected-Spin/unitary-
  parent fences, unchanged accounting, three hostile charges and efficient
  mandatory-eight plus object-triggered specialist routing.

- `selected_k77_moving_epsilon_first_action_completion_audit.py` enforces
  ledger v0.123's exact zero lower-Cartan and moving-Phi/Shiab corrections,
  surviving `91/6/88` epsilon ranks, selected-Spin 321 closure kill, broader-
  parent and quotient fences, unchanged accounting, and mandatory durable
  exact-bank successor, now discharged by ledger v0.124.

- `selected_k77_fixed_operator_metric_epsilon_leakage_audit.py` enforces
  ledger v0.122's all-causal/both-branch fixed-operator rank pattern, the
  horizontal/off-slice split, total-moving-source fence, unchanged accounting
  and mandatory source, symplectic and analytic review.

- `selected_k77_first_action_tangent_closure_audit.py` enforces ledger
  v0.121's complete rank-196/inertia-`97,99` grade-one self blocks, zero
  horizontal/off-slice grade-two cross, narrowed minimum-321 disposition,
  grade-label indexing trap, parent/action/domain fences and unchanged
  accounting.

- `selected_k77_lower_order_source_block_reconciliation_audit.py` enforces
  ledger v0.120's exact raw-residual/lower-epsilon Layer-0 typing, branch ranks
  `91/91`, positive conjugate coefficients, v0.95 fixed-`varpi` metric port,
  parent/action/domain fences, unchanged accounting and two hostile repairs.

- `selected_k77_two_branch_action_block_port_audit.py` enforces ledger
  v0.119's exact rank-91 first-action cross and rank-1470 residual zero-jet
  `varpi` ports to both branches, common selected causal principal ranks
  `110/110/16`, distinct lower-order amplitudes, incomplete-Frechet and
  expanded-parent fences, unchanged accounting and mandatory source,
  symplectic, Krein and microlocal boundaries.

- `selected_k77_common_graded_trace_boundary_triple_audit.py` enforces ledger
  v0.116's strong graded `H7/H-7` plus `H8/H-8` trace carrier, relative
  cotangent-lift symplectic/polarization descent, and the distinction between
  a boundary trace skeleton and the still-unowned bulk `Dmax/Dmin`, Green,
  Krein and coupled BV--BFV structures.
- `selected_k77_relative_edge_bitorsor_topology_audit.py` enforces ledger
  v0.115's distinction between active gauge motion and passive patching, the
  one-sided trivial-bundle obstruction, the relative `A0` bitorsor
  nonemptiness theorem, preserved dressing/trace/kernel/BFV results and all
  analytic, physical and action-parent fences.
- `selected_k77_branch_bfv_no_selector_audit.py` enforces ledger v0.114's
  exact nonzero-branch symplectomorphism, amplitude-blind vertical
  polarization, stratum-wise classical minimal-edge BFV charge/CME, global
  topology/domain/quantum fences and unchanged accounting.

- `selected_k77_branch_boundary_amplitude_classification_audit.py` enforces
  ledger v0.113's exact residual-adjoint zero versus primitive-epsilon
  rank-14-per-endpoint charge split, Galois-related amplitudes, five boundary
  horns, global BFV/parent/tangent fences and unchanged accounting.

- `selected_k77_full_parent_branch_stationarity_audit.py` enforces ledger
  v0.112's complete pointwise real `u(64,64)` source-connection tangent,
  exact `8,192+8,192` two-half/half-exchanging split, both branch survivals,
  full homogeneous-epsilon bulk identity, live endpoint momentum and strict
  parent-selection/global-functional-tangent fences.

- `selected_k77_source_tangent_branch_stationarity_audit.py` enforces ledger
  v0.111's exact source-coordinate pullback, both local branch survivals,
  independent-`B` endpoint retyping, 1,571 completeness fence, distinct action
  parents and amplitude/Hessian/BV/domain successor.

- `selected_k77_nonconstant_atlas_xi_prolongation_audit.py` enforces ledger
  v0.110's exact nonconstant affine descent, source-confirmed Xi redundancy,
  two ansatz-selected algebraic witnesses, native-moving-geometry fences and
  fail-closed current pointers.

- `selected_k77_source_euler_two_to_one_audit.py` enforces ledger v0.109's
  source-field Layer-0 correction, exact one-amplitude invariant family,
  v0.108 representative/retraction split, local connection-jet/Bianchi/
  constant-descent grade, and global prolongation/amplitude fences.

- `selected_k77_curvature_vev_trace_audit.py` enforces ledger v0.108's
  same-carrier Layer-0 correction, exact zero-freedom scalar curvature-jet
  branch and metric-trace cancellation, while keeping the global connection,
  full derivative Euler, differential Bianchi, observation and physics fences
  open and preserving all three action parents.

- `selected_k77_direct_metric_euler_audit.py` enforces ledger v0.107's exact
  rank-one direct metric trace, nine-dimensional traceless kernel,
  fixed-field/fixed-source/co-moving lift-independence, residual-square
  noncancellation, dynamic-VEV successor, three action parents and mandatory
  symplectic/analytic/source fences.

- `selected_k77_common_first_action_epsilon_hessian_audit.py` enforces ledger
  v0.106's old-background trace-covector correction, exact nontrivial common
  connection branch, direct-metric-Euler fence, rank-91 moving-epsilon cross,
  grade-one receiver requirement, 125/321/1,571 tangent gate, action-parent
  separation and mandatory symplectic/analytic/source controls.

- `selected_k77_primitive_epsilon_common_bank_audit.py` enforces ledger
  v0.105's primitive-epsilon 91-column typing, exact 125-field raw/Gram strata
  `110/110/110` and `110/110/16`, inertias, null isotropic excess 94,
  first-action `34` versus `125` mismatch, unbooked trace quotients, mandatory
  symplectic/analytic fences and the three distinct action parents.

- `selected_k77_stationary_gram_boundary_strata_audit.py` enforces ledger
  v0.104's rectangular-residual versus square-Gram typing, exact causal Gram
  ranks `22/22/14`, inertias, unbooked doubled trace quotients `44/44/28`,
  `H7 x H-7` regularity-only fence, missing edge-carrier soldering/full action/
  maximal-domain/odd-BFV gates and the three distinct action parents.

- `selected_k77_sobolev_edge_current_algebra_audit.py` enforces ledger
  v0.103's weak `H7 x H7` versus strong `H7 x H-7` distinction, `H8`
  gauge/edge threshold, conditional nonempty-torsor edge quotient, classical
  charged current algebra, no-selection polarization and full odd-BFV/domain/
  topology/action-parent fences.

- `selected_k77_full_tau_a0_moment_map_audit.py` enforces ledger v0.102's
  full derivative-bearing nonzero-`A0` tilted quotient, conditional
  Spin-native action trace, raw charged moment map, exact edge characteristic
  kernel and moving-reference algebraic patch law while preserving functional
  BFV, charged-boundary, common-domain and expanded-action-parent fences.

- `selected_k77_boundary_disposition_selector_audit.py` enforces ledger
  v0.101's source/action boundary-selection negative result, conditional
  full-boundary-gauge plus nonzero-momentum edge selector, charged-symmetry
  comparator, inventory and fail-closed current pointers.

- `selected_k77_action_noether_preboundary_audit.py` enforces ledger v0.100's
  nonvacuous moving pairing/density cancellation, local matched-q
  selected-action Euler-Noether identity, action-owned `E_B-E_T` endpoint
  momentum, compact-support presymplectic basicness, live unrestricted
  boundary moment map and global BFV/domain/action-parent fences.

- `selected_k77_common_physical_equation_dual_green_audit.py` enforces ledger
  v0.99's 34-field covector-valued common equation dual, nonzero local Green
  concomitant, zero matched-q physical pullback in every causal class, firing
  missing-term controls, source/symplectic/analytic fences, distinct action
  parents and selected-action Euler/Noether successor.

- `selected_k77_source_native_diffeomorphism_ward_closure_audit.py` enforces
  ledger v0.98's matched-q metric--Cartan--moving-Shiab `J R=0`, physical
  rank-four versus raw rank-three longitudinal split, rejection of frozen-q0
  and missing-term plants, grade-one-gamma nonrequirement, source and
  symplectic/analytic fences, and common-`K_loc`/action-Euler successor.

- `selected_k77_common_metric_dupsilon_coefficient_bank_audit.py` enforces
  ledger v0.97's four rank-nine common metric banks, combined rank-twenty and
  all-causal transverse rank-six result, exact metric/varpi torsion graph,
  rejection of the identity-defined Ward metric owner, measured rank-four
  physical defect, source/symplectic/analytic fences and the complete
  primitive-epsilon/diffeomorphism successor.

- `selected_k77_common_field_formal_adjoint_green_audit.py` enforces ledger
  v0.96's actual four-direction source-varpi coefficient bank, exact
  covector-valued `K_loc` formal adjoint and Green current, fail-closed missing
  common-coordinate `D_g`/full primitive `D_epsilon` inventory, field-Riesz
  fence, mandatory symplectic/analytic review, and distinct selected/
  two-`U(32,32)`/full-`U(64,64)` action parents.

- `selected_k77_fixed_varpi_normal_frechet_closure_audit.py` enforces ledger
  v0.95's exact fixed-varpi `delta T`, three-term `delta F_A=0` cancellation,
  rank-20 metric-derived Levi-Civita image, all-causal transverse rank-six
  closure, raw-residual observation fence, mandatory symplectic/analytic
  review, frozen accounting and common-field formal-adjoint/Green successor.

- `selected_k77_transverse_comoving_coefficient_closure_audit.py` enforces
  ledger v0.94's exact ten-direction and three-transverse-six comoving
  Hodge/Clifford/Phi/Shiab coefficient closure, live rank-six source-response
  fence, mandatory symplectic/analytic review, frozen accounting and the
  component-normal field/connection/observation successor.

- `selected_k77_operative_pairing_symmetry_closure_audit.py` enforces the
  v0.93 exact Spin/block/full carrier closures `2107/16382/16383`, invariant
  pairing dimensions `3/3/1` (or `2` with a separately typed exchange), the
  two-`C^(32,32)` versus full-`U(64,64)` Layer-0 split, mandatory symplectic
  and analytic fences, `84..86` conditional residue range, and lower-order
  `D_g Upsilon` successor.

- `selected_k77_residual_pairing_invariance_audit.py` enforces the v0.92
  local-pairing theorem, full-`U(64,64)` comparator versus Weyl-block fork,
  mandatory symplectic and analytic fences, frozen headline/residue/datum
  accounting, and lower-order transverse/adjoint/Green successor.

- `selected_k77_action_frechet_ward_object_separation_audit.py` enforces the
  v0.91 distinction between first-action Euler bank and residual Jacobian,
  four Ward versus six transverse directions, conditional MW selector,
  mandatory symplectic/hostile review and frozen headline/residue/datum fence.

- `signature_generic_cartan_ward_compose_audit.py` enforces the v0.90
  Cartan/primitive-epsilon composition, branch-native K77/K95 Hodge split,
  mandatory specialist review, frozen headline meter and actual-action
  Frechet successor gate.

- `signature_rationale_build_branch_retype_audit.py` enforces the v0.89
  distinction between author-asserted K77 and geometry-derived K95, the
  unchanged scientific meter, and the branch-aware successor gate.

- `selected_k77_full_reduction_quotient_reconciliation_scope_audit.py` audits
  the v0.59 source-owned labelled-reduction quotient, persistent horizontal-
  plane forgetful failure, closed invariant-replacement horn, mandatory
  symplectic fence and frozen ledger/datum/lane/posture boundary.

- `selected_k77_source_graph_basicness_scope_audit.py` audits the predecessor v0.58
  full-frame covariance versus quotient-basicness split, source
  epsilon/soldering uncertainty, unbookable surplus, mandatory symplectic
  review and frozen ledger/datum/lane/posture boundary.

- `selected_k77_cartan_spencer_signature_correction_scope_audit.py` audits the
  v0.57 `(9,5)` to settled K77 `(7,7)` coefficient repair, old-value
  supersession, surviving pointwise theorem, mandatory symplectic review and
  frozen ledger/datum/lane/posture boundary.

- `selected_source_varpi_cartan_composition_scope_audit.py` audits the v0.56
  fixed-epsilon source tangent, exact pointwise four-column Cartan lift,
  global-integrability fence, mandatory symplectic review and frozen
  datum/lane/posture boundary.

- `selected_nonzero_background_cartan_spencer_owner_scope_audit.py` audits
  the v0.55 unrestricted Cartan/Spencer owner, Levi-Civita subclass fence,
  mandatory symplectic review and frozen datum/lane/posture boundary.

- `selected_invariant_constituent_operator_naturality_scope_audit.py` audits
  the v0.54 branch-tangent naturality result, independent-field-jet fence,
  mandatory symplectic review and frozen datum/lane/posture boundary.
- `selected_second_layer_residual_constituent_operator_correction_scope_audit.py`
  audits the v0.53 retraction, selected nonzero constituent, source return,
  mandatory symplectic review and frozen datum/lane/posture boundary.

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
- `conditional_physics_ledger_v04_scope_audit.py`
- `conditional_physics_ledger_v05_scope_audit.py`
- `conditional_physics_ledger_v06_scope_audit.py`
- `conditional_physics_ledger_v07_scope_audit.py`
- `conditional_physics_ledger_v08_scope_audit.py`
- `conditional_physics_ledger_v09_scope_audit.py`
- `conditional_physics_ledger_v010_scope_audit.py`
- `conditional_physics_ledger_v011_scope_audit.py`
- `conditional_physics_ledger_v012_scope_audit.py`
- `conditional_physics_ledger_v013_scope_audit.py`
- `conditional_physics_ledger_v014_scope_audit.py`
- `conditional_physics_ledger_v015_scope_audit.py`
- `conditional_physics_ledger_v016_scope_audit.py`
- `conditional_physics_ledger_v017_scope_audit.py`
- `conditional_physics_ledger_v018_scope_audit.py`
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
- `eric_lane_decisive_source_collision_audit.py`
- `escape_corners_readme_inventory_audit.py`
- `explorations_top_level_file_boundary_audit.py`
- `explorations_readme_surface_map_audit.py`
- `finite_control_provenance_audit.py`
- `functional_channel_operating_contract_scope_audit.py`
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
- `k77_wave2_action_polarization_common_observation_domain_scope_audit.py`
- `k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit.py`
- `k77_wave2_full_source_action_defect_localization_scope_audit.py`
- `k77_wave2_actual_y14_receiver_ordering_scope_audit.py`
- `k77_wave2_actual_draft916_blockwise_scope_audit.py`
- `k77_wave2_common_two_layer_action_scope_audit.py`
- `k77_wave2_dirac_derham_superig_rebase_scope_audit.py`
- `k77_wave2_euler_shell_two_connection_scope_audit.py`
- `k77_wave2_global_draft916_krein_preboundary_scope_audit.py`
- `k77_wave2_mixed_primalizer_comparison_scope_audit.py`
- `k77_wave2_moving_shiab_epsilon_ward_green_domain_scope_audit.py`
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
- `moving_gimmel_hodge_frame_owner_scope_audit.py`
- `next_steps_frontdoor_guard_audit.py`
- `pati_salam_readme_inventory_audit.py`
- `papers_candidates_readme_inventory_audit.py`
- `papers_readme_lifecycle_map_audit.py`
- `path_dependency_audit.py`
- `post_batch2_wave1a_supersession_dependency_audit.py`
- `primary_gu_interface_contract_audit.py`
- `process_gate_readme_inventory_audit.py`
- `protected_surface_diff_audit.py`
- `pull_request_template_validation_audit.py`
- `public_path_hygiene_audit.py`
- `queue_review_freshness_audit.py`
- `register_writeback_audit.py`
- `selected_cubic_augmented_torsion_d3_owner_scope_audit.py`
- `selected_cubic_gauge_rotated_lc_ward_owner_scope_audit.py`
- `selected_cubic_intrinsic_homogeneous_ward_closure_scope_audit.py`
- `selected_cubic_reduced_numerator_scope_audit.py`
- `selected_cubic_two_connection_principal_ward_descent_scope_audit.py`
- `selected_action_curvature_graph_six_versus_four_scope_audit.py`
- `selected_action_offgraph_dbt_principal_symbol_scope_audit.py`
- `selected_action_second_soldering_observation_jets_scope_audit.py`
- `selected_action_stationary_spin_lc_hessian_scope_audit.py`
- `selected_action_coupled_diffeomorphism_ward_retype_scope_audit.py`
- `selected_action_source_variable_hessian_scope_audit.py`
- `selected_action_ward_completion_identifiability_scope_audit.py`
- `selected_nonzero_background_cartan_spencer_owner_scope_audit.py`
- `selected_source_varpi_cartan_composition_scope_audit.py`
- `selected_k77_cartan_spencer_signature_correction_scope_audit.py`
- `selected_k77_fixed_varpi_normal_frechet_closure_audit.py`
- `selected_k77_operative_pairing_symmetry_closure_audit.py`
- `selected_k77_transverse_comoving_coefficient_closure_audit.py`
- `selected_k77_action_boundary_coefficient_bank_scope_audit.py`
- `selected_k77_full_u6464_action_bank_scope_audit.py`
- `selected_k77_contact_presymplectic_gauge_basicness_scope_audit.py`
- `selected_k77_minimal_edge_mode_reduction_scope_audit.py`
- `selected_k77_full_reduction_quotient_reconciliation_scope_audit.py`
- `selected_k77_source_graph_basicness_scope_audit.py`
- `selected_second_layer_actual_source_lift_rank_mismatch_scope_audit.py`
- `selected_second_layer_full_cl2_residual_pullback_scope_audit.py`
- `selected_second_layer_i2b_gauss_owner_map_scope_audit.py`
- `selected_second_layer_tt_euler_preboundary_helicity_scope_audit.py`
- `spectral_conditioning_disclosure_audit.py`

- `pw2fr2b2b2g_full_a4_multiindex_green_distinct_i2b_c4_scope_audit.py`
- `pw2fr2b2b2h_mixed_shiab_second_jet_scope_audit.py`
- `pw2fr2b2b2h2_i2b_second_residual_primalizer_pairing_scope_audit.py`
- `pw2fr2b2b2h3_source_epsilon_curvature_orbit_graph_scope_audit.py`
- `pw2fr2b2b2h4_source_active_real_form_scope_exit_scope_audit.py`
- `pw2fr2b2b2i_separate_conditional_active_c4_banks_scope_audit.py`
- `pw2fr2b2b2i1_s3_geometric_transport_scope_audit.py`
- `pw2fr2b2b2i2_affine_first_size3_full_evaluator_scope_audit.py`
- `pw2fr2b2b2i2_resumable_first_size6_scope_audit.py`
- `pw2fr2b2b2i2_resumable_second_size6_scope_audit.py`
- `pw2fr2b2b2i2_resumable_third_size6_scope_audit.py`
- `pw2fr2b2b2i2_s3_fixed_orbit_full_evaluator_scope_audit.py`
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
- `global_projector_amplitude_layer0_audit.py`
- `zero_fermion_vev_selector_exhaustion_audit.py`
- `p3_characteristic_amplitude_selector_audit.py`
- `p3_native_characteristic_pairing_audit.py`

## Eric-lane decisive source-collision gate

`eric_lane_decisive_source_collision_audit.py` checks that decisive
author-guided campaign results record a local primary-source collision as
`SOURCE-CONFIRMS`, `SOURCE-CORRECTS`, or `SOURCE-SILENT`, including the
retroactive ECW3C ultrahyperbolic scope repair. It is a provenance/process
guard only; source speech is not mathematical verification.

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

`trace_q_higgs_chirality_admission_scope_audit.py` fail-closes the pre-wave
trace-`q` / Higgs / chirality admission result. It preserves the distinction
between the canonical K77 trace receiver, Weinstein's ad-valued displaced
connection, and the conditional `sigma_epsilon`-derived moving chimeric vector;
requires the K-null/balanced finite-screen result, the mandatory symplectic
boundary, unchanged ledger rows and unused P1/P2/P3; and forbids promoting the
literal K77-to-K95 port to a global chiral no-go.

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

## K77 Wave 2 full source-action defect-localization scope gate

`k77_wave2_full_source_action_defect_localization_scope_audit.py` requires the
scalar-coefficient/induced-density localization rather than literal top-form
pullback, its orientation-free patch descent, the exact first-order Euler
monopole plus graph-mixed normal dipole, and the moving support plus density
shape equation. It requires gauge/diffeomorphism localization functoriality
only given a complete even owner ledger and keeps the minimal BV theorem at
closed-algebra, boundary-free grade. It enforces the hostile-review fence
between a source-shaped normal-jet witness and the actual moving K77 Shiab
symbol, and leaves the bulk/defect normalization, primitive BV ledger, common
domain, physics, Wave 3 and P1/P2/P3 open.

## K77 Wave 2 I1B conormal-symbol / weld / domain scope gate

`k77_wave2_i1b_conormal_symbol_weld_domain_scope_audit.py` requires the
selector-independent fixed-`epsilon` I1B symbols, their exact `B:T=2:1`
principal ratio, graph-conormal mixing, and the fixed-section `85/91`
annihilator count per paired adjoint coefficient block. It preserves the
preferred K77 Shiab as unselected, types the all-section zero theorem with its
arbitrary-`T`/nondegenerate-pairing/all-splitting hypotheses, and refuses to
promote a generic matrix fixture. It requires the source-guided no-duplicate
weld, the invariant normal-density debt rather than an unconditional
`length^10` claim, and the smooth plus fixed-section `H9/H10` trace-regular
variation class. The dependent epsilon owner chain, moving-section Sobolev
composition, closed Green/BFV domain, physics, Wave 3 and P1/P2/P3 stay open.

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
## K77 Wave 2 moving-Shiab / epsilon-Ward / Green-domain scope gate

`k77_wave2_moving_shiab_epsilon_ward_green_domain_scope_audit.py` requires
exhaustive enumeration of the eight source-permitted product channels, all-85
mixed-normal support, and the distinct selected-slice and full-grade-one rank
vectors. It requires exact moving-Phi dual-number agreement, the primitive
`D_B^!(E_B-E_T)+(D_epsilon Shiab)^!K_S` chain, the complete homogeneous even
Ward owner fixture, and the compact-core `H10 -> H9` Green graph. It forbids
turning epsilon orbit transport into a selector, bundling metric/Hodge/density
or section motion into the primitive epsilon row, or promoting compact-core
Dirichlet closure to a global physical domain. P1/P2/P3, physics, Wave 3 and
the `TG-1 AND TG-2 AND TG-3` conjunction remain unchanged.

## K77 Wave 2 action-polarization / common-observation-domain scope gate

`k77_wave2_action_polarization_common_observation_domain_scope_audit.py`
requires the complete `91 x 14` grade-one channel block, eight pairwise
nonproportional restrictions, span rank five, and three exact restricted
Clifford/Hodge relations while forbidding promotion to a full-adjoint rank
theorem. It requires all eight frozen action polarizations to satisfy the
Euler/Helmholtz check with selection rank zero, and it keeps the printed
endpoint distinct. It accepts only a conditional bounded-geometry
`H10 -> H9` associated-bundle observation scale, types the codimension-ten
section as an interior trace rather than a Green boundary, and leaves closed
`L2`/Krein/hyperbolic/BFV domains open. The independent Sage free-product
rank-eight result is fenced from the represented K77 rank-five block.
P1/P2/P3, physics, Wave 3 and `TG-1 AND TG-2 AND TG-3` remain unchanged.

## K77 Wave 2 full-adjoint Shiab / Bianchi / two-connection target scope gate

`k77_wave2_full_adjoint_shiab_bianchi_two_connection_target_scope_audit.py`
requires the structural `S_(f,i,o)=A_f+B_(i,o)` proof, exact full displayed
map span five, three universal relations and eight projective classes. It
requires the free-DGA quadratic-eddy path average and first-moment Bianchi
syzygy, plus the independent two-connection reconstruction
`F_B+(1/2)DeltaF-(1/6)T^2`. It retains the nonzero mixed `-T wedge F_B`
defect and requires selection rank zero to be scoped to the pre-Shiab target.
The moving `Phi(epsilon)` chain map, typed fermion-to-boson Euler comparison,
preferred Shiab, physical domain, Wave 3, physics and P1/P2/P3 remain open.

## K77 Wave 2 principal-Bianchi product-selector scope gate

`k77_wave2_principal_bianchi_product_selector_scope_audit.py` requires exact
rank-91 algebraic-Riemann differential-Bianchi jet carriers for positive,
negative and null covectors, four Bianchi-passing displayed rows, defect rank
one, and `comm/symi/symi` as the unique nonzero Riemann survivor. It requires
the exact `-2` ambient-Einstein response, zero Weyl response, moving-epsilon
transport without added selection, and the commuting two-connection
curvature comparison square. It forbids attribution to Weinstein's missing
sheet, full source-natural Shiab uniqueness, an eddy-completed chain or full
Euler functor, observed gravity, domain, physics, P1/P2/P3 or Wave-3 promotion.

## K77 Wave 2 eddy / augmented-torsion Euler prolongation scope gate

`k77_wave2_eddy_augmented_torsion_euler_prolongation_scope_audit.py`
requires the source-collided quadratic-eddy path average, exact replay of the
K77-B3 printed-endpoint obstruction, and the action's actual
Fréchet/formal-adjoint Euler formula. It requires complete rank-182 grade-one
generic-adjoint carriers on all three covector orbits and rank-13 symbols to
be owned by the **printed rival**, alongside rank-91 Riemann closure. It
forbids transferring `Xi_print` to the action Euler, reviving the printed
endpoint, or assigning the raw northeast block without a typed owner,
homotopy, quotient or rival disposition. No Noether/BV, domain, observation,
physics, P1/P2/P3 or Wave-3 promotion is allowed.

## K77 Wave 2 action degree-14 / northeast scope gate

`k77_wave2_action_owned_degree14_northeast_scope_audit.py` requires the
selected degree-two Shiab's complete tested-carrier rank `1197`, its exact
`Cl1/Cl5` split `196/1001`, and all `63,336` formal-adjoint entry identities.
It requires raw northeast rank `8281`, exact rank-91 retention on positive,
negative and null Riemann banks, and the minimal degree-three collapse to
`comm/symi = 0/1` with zero traceless-Ricci response. It types action-owned
degree 14 as the full even Noether totalization and forbids substituting
`D_B E_act`, source `Xi`, or `J_D+J_F`. It also forbids promoting the finite
formal adjoint to a closed positive Krein domain or extending the minimal
candidate kill to all source-natural Shiabs. P1/P2/P3, physics, Wave 3 and the
third-lane conjunction remain unchanged.

## Pre-contract 0B trace-reversal robustness scope gate

`precontract_wave_0b_trace_reversal_robustness_scope_audit.py` preserves the
Layer-0 separation between the vertical Frobenius fibre metric, the ambient
fourteen-dimensional Einstein contraction and the observed four-dimensional
Einstein equation. It retains the exact ambient displayed-ansatz kill and the
incompatible `26` versus `6` naive-restriction responses, while leaving a
non-scalar observed receiver, physical GR and P1/P2/P3 open.

## Conditional physics ledger v0.1 scope gate

`conditional_physics_ledger_v01_scope_audit.py` freezes 86 enumerated source
rows into 78 canonical targets plus eight aliases, requires the extensible
verdict/reason taxonomy, distance and revival fields, recomputes the residue
and ensures all six over-determined rows remain independently owned. The
`78/78` meter means frozen-map coverage, not construction completion.

## Pre-contract 0C typed identity and theorem-scope gate

`precontract_wave_0c_typed_identity_theorem_scope_audit.py` preserves the
narrow T3/spinor-Shiab projective identity without equating the whole SA-C2
cure or Eric's degree-thirteen adjoint Shiab. It retains the exact
Riemann-restricted trace-reversal adapter, leaves the full action domain open,
and fences the scale-blindness theorem to genuinely invariant suppliers.

## Pre-contract 0B/0A/0C campaign reconciliation gate

`precontract_waves_0abc_campaign_scope_audit.py` checks execution order,
cross-wave ledger dispositions, the automatic meter and residue, immediate
Compose-plus-Source ordering, the full-domain observed-receiver next gate and
all no-promotion fences. It explicitly refuses to ratify the future operating
contract or change P1/P2/P3, canon, public posture or observed physics.

## Selected-Shiab observed Einstein receiver scope gate

`full_domain_shiab_observed_einstein_receiver_scope_audit.py` requires the
rank-ten image of the observed Einstein map on the Bianchi-selected
displayed-family candidate's complete Riemann kernel
kernel. It kills only post-Shiab factorization, retains the pre-Shiab Gauss
map at local first-variation grade, and leaves source-action ownership, global
descent, domain, physics, P1/P2/P3, canon and public posture open.

## Conditional physics ledger v0.2 scope gate

`conditional_physics_ledger_v02_scope_audit.py` preserves v0.1 as immutable,
requires exactly the scoped `LT-GR1b` migration, keeps `LT-GR1` unchanged, and
preserves the frozen 78-row denominator and verdict counts.

## Conditional physics ledger v0.3 scope gate

`conditional_physics_ledger_v03_scope_audit.py` preserves v0.2 byte-for-byte,
requires the append-only five-way `LT-GR2` split, recomputes the 82 active
targets, and wires the official interview source, Layer-0 flatness fence,
released directive and next curvature/VEV Euler gate. It rejects a source-only
field equality as an action-parameter or magnitude result.

## Conditional physics ledger v0.4 scope gate

`conditional_physics_ledger_v04_scope_audit.py` preserves v0.3, recomputes the
unchanged 82-row denominator and verdict counts, requires the exact ambient
curvature/`T` ranks `105/196` and 91-row split, keeps native BV quotient rank
undefined, and enforces the noncircular transition from the killed
contraction-first receiver to the complete pre-Shiab moving Gauss/`II` action
owner. It also requires the current action's vacuum-shift result to remain
tracking rather than screening.

## Conditional physics ledger v0.5 scope gate

`conditional_physics_ledger_v05_scope_audit.py` preserves v0.4 byte-for-byte,
recomputes the unchanged 82-row denominator and verdict counts, requires
`LT-GR2c` to remain `NEEDS/MISSING_CONSTRUCTION`, and wires the scoped
current-`I1B` `T=0` ownership kill to the conditional fixed-slot non-null
even-BV quotient rank 16. It rejects promotion past the missing global
`sigma_epsilon` soldering map, nonlinear bulk/defect weld and null/Green
domain, and requires `SOURCE-SILENT` plus unchanged P1/P2/P3.

## Conditional physics ledger v0.6 scope gate

`conditional_physics_ledger_v06_scope_audit.py` preserves v0.5 byte-for-byte,
recomputes the unchanged 82-row denominator and verdict/residue counts, and
requires only `LT-GR2c` to move. It wires the exact K77 rank-ten receiver,
adjoint isometric right inverse/projector and same-stratum orthogonal action
weld while refusing promotion past global full-reduction existence,
bulk/defect support normalization, nonlinear BV or the null/Green domain.

## Conditional physics ledger v0.7 scope gate

`conditional_physics_ledger_v07_scope_audit.py` preserves v0.6 byte-for-byte,
recomputes the unchanged 82-row denominator and verdict counts, and requires
only `LT-GR2c` to move. It wires the admitted spin-X/source-`P_H`/source-
`epsilon` global full labelled K77 Clifford frame and the source-guided
bulk-plus-independent-`X` support horn while refusing to book `lambda_def`
until its normalization alias is adjudicated. Nonlinear BV, null/Green domain,
physical cosmology and P1/P2/P3 remain open/unchanged.

## Conditional physics ledger v0.8 scope gate

`conditional_physics_ledger_v08_scope_audit.py` preserves v0.7 byte-for-byte,
recomputes the unchanged 82-row denominator and verdict counts, and requires
only `LT-GR2c` to move. It wires the formal minimal homogeneous-gauge CME,
exact null `10 -> 6 -> 2` constraint/gauge quotient, conditional flat-defect
Green complex and 84-real prequotient count while requiring the curved/global
`Y14` domain, observation, positivity, vacuum and cosmology to remain open.

## Conditional physics ledger v0.9 scope gate

`conditional_physics_ledger_v09_scope_audit.py` preserves v0.8 byte-for-byte,
recomputes the unchanged 82-row denominator, verdict and residue counts, and
requires exactly four row-distance migrations. It wires the determinant-one
complete first-jet section observation, inverse-transpose equation dual,
finite-jet global-shell fence, sharp standard K77 ambient-Cauchy obstruction
and conditional observed curvature/distortion equation. It keeps constrained
domain construction, the physical up-and-back stress map, nonzero vacuum,
positive cohomology and P1/P2/P3 open/unchanged.

## Conditional physics ledger v0.10 scope gate

`conditional_physics_ledger_v010_scope_audit.py` preserves v0.9
byte-for-byte, recomputes the unchanged 82-row denominator, verdict and
residue counts, and requires exactly five row migrations. It wires the
zero-parameter radial reconstruction of action-owned Hilbert stress, the
retained observed `10 -> 6 -> 2` quotient, the adverse double-pole propagator
diagnosis and the scope correction that reopens the existing full nonlinear
`T`-cubic vacuum. It forbids promotion to a released source totalization,
connection-current equality, Einstein recovery, screening, cosmology or a
P1/P2/P3 change.

## Conditional physics ledger v0.11 scope gate

`conditional_physics_ledger_v011_scope_audit.py` preserves v0.10
byte-for-byte, recomputes the unchanged 82-row denominator, verdict and
residue counts, and requires exactly seven row migrations. It corrects the
mistyped one-pole-total target, wires the conditional full-`|II|^2` response
with one simple massless Einstein pole plus one distinct massive GU partner,
and records the exact finite cyclic nonlinear saddle branches. It requires P2,
the selected moving-K77 Fréchet-adjoint vacuum, source totalization/current
identity and physical Krein/Green domain to remain open.

## Conditional physics ledger v0.12 scope gate

`conditional_physics_ledger_v012_scope_audit.py` preserves v0.11
byte-for-byte, recomputes the unchanged 82-row denominator, requires exactly
seven row migrations and verifies the verdict move to `33/19/24/6`. It wires
the rank-100 canonical Gauss restriction of the written connection norm, the
rank-ten trace-first negative control, the selected nonzero K77 algebraic
branch `-kappa_1/312` and the one-fork residue reduction to nine. It keeps the
physical stability, selected-branch totalization/current chain, common
Krein/Green domain, massive-partner classification and external `P2_datum`
open.

## Conditional physics ledger v0.13 scope gate

`conditional_physics_ledger_v013_scope_audit.py` preserves v0.12 byte-for-
byte, recomputes the unchanged 82-row denominator, verdict and residue counts,
and requires exactly seven row migrations. It separates the radial Clifford-
one Hessian from the trace/traceless gravitational Gauss Hessians, wires the
common observed defect Krein/Green domain, records the exact opposite pole
residues and types the one-action direct-plus-soldered current chain. It keeps
the full metric/coframe soldering derivative, positive physical BV cohomology,
ambient `Y14` domain and two-field curvature/VEV cosmology open.

## Conditional physics ledger v0.14 scope gate

`conditional_physics_ledger_v014_scope_audit.py` preserves v0.13 byte-for-
byte, recomputes the unchanged 82-row denominator, verdict and global residue
counts, and requires exactly eight row migrations. It wires the rank-ten
gauge-rotated Levi-Civita metric derivative modulo gauge, the lower bound of
two surviving massive even-BV TT classes, the canonical finite tree-level
positive Krein majorant, and the local curvature/VEV two-to-one horn with
exact shift susceptibility `2/a`. It explicitly keeps full nonlinear ambient
soldering, odd super-IG cohomology, loop/UV positivity, ambient/global/nonlocal
cosmology and action-owned `w(z)` open. The third scoped quotient is ranked
without booking a global residue reduction.

## Functional-channel operating-contract scope gate

`functional_channel_operating_contract_scope_audit.py` requires the ratified
Build/Compose/Source/Verify contract to remain wired through `AGENTS.md`,
`LANES.yaml` and the operating model while purpose Lanes 1/2/3/A remain
unchanged. It enforces information-preserving ledger fields, source return
codes, independent adverse-row adjudication, condition-based dispatch,
two-sided hostile review and the current `GU-COSMO-DYNAMIC-01` K77 rank-ten
receiver, formal homogeneous-gauge CME, null physical quotient, exact
first-jet section-germ observation, action-owned Hilbert stress, canonical
full-II norm selection, massless-plus-massive simple-pole response and
selected nonzero K77 algebraic stationary branch. It now also enforces ledger
v0.13, the distinct `100/117` and `124/117` Gauss Hessians, the common defect
Krein/Green domain, exact opposite residues, the direct-plus-soldered current
chain, then the v0.14 metric-soldering/even-BV/local-curvature results and the
v0.15 first-interaction and global-zero-mode update, followed by the v0.16
fixed-background field-mixing spectral `C` and exact exceptional-locus
classification. The latest return is `SOURCE-SILENT` for this C construction;
the predecessor source correction still holds that algebraic super-IG descent
is not a default odd action. It now also enforces v0.17's zero vacuum cubic
Hessian, three-species odd-channel shells, numerator-before-pole fence and
symplectic descent veto. It keeps the full nonlinear/Fock `C`, selected
on-shell numerator, physical-sheet test, full cubic bank, common domain,
domain/measure functional, algebraic global descent, action-owned `w(z)` and
external `P2_datum` open. It
also forbids treating Einstein recovery as recovery of a constant or dynamical
cosmological sector and records that this reset changes no scheduler, trigger,
activation grant, canon, external datum or public posture.
## Cross-theory mechanism-donor scope gate

`cross_theory_mechanism_donor_crosswalk_scope_audit.py` enforces that the donor
assessment remains a bounded Compose checkpoint, selects exactly the two
method ports `NCG-CONTROL` and `STRING-LINF` under the two-port cap, moves no
ledger row or external datum, preserves Curt separation/no-third-lane, and
wires the five-wave construction front door. It also requires the operating
contract to forbid wrong-type-as-gap, finite-NCG-object import, free higher-
gauge levels and premature FRG.

## Conditional physics ledger v0.15 scope gate

`conditional_physics_ledger_v015_scope_audit.py` preserves v0.14 byte-for-
byte, recomputes the unchanged 82-row denominator, verdict and global residue
counts, and requires exactly six row migrations. It wires the exact failure of
every multiplicative scalar-sign extension of the free spectral involution on
the first owned cubic, the full finite-local constant-mode no-screening/
solvability dichotomy, and the conditional normalized global projector. It
ranks a fourth scoped zero-mode quotient without global residue reduction and
requires the domain/measure functional, interacting `C`, algebraic super-IG
global descent, FLRW `w(z)` and P2 identification to remain open.

## Conditional physics ledger v0.16 scope gate

`conditional_physics_ledger_v016_scope_audit.py` preserves v0.15 byte-for-
byte, recomputes the unchanged 82-row denominator, verdict and global residue
counts, and requires exactly four row migrations. It wires the exact positive
spectral fundamental symmetry of the first action-owned fixed-background TT
Hessian, the rank-four/zero-freedom first correction, and the generic Jordan,
complex-spectrum, disconnected-real and scalar-nonselection loci. It keeps
stationary-vacuum selection, the full nonlinear action, scalar fluctuations,
the full cubic bank, common BV/Green/Fock domain and UV positivity open, and
does not consume P1/P2/P3.

## Conditional physics ledger v0.17 scope gate

`conditional_physics_ledger_v017_scope_audit.py` preserves v0.16 byte-for-
byte, recomputes the unchanged 82-row denominator, verdict and global residue
counts, and requires exactly four row migrations. It wires the exact zero of
the complete cubic Hessian at the zero-field point, the fixed-theta reduction
to the predecessor TT block, and the real odd-channel continuum shells for
both scalar parities. It requires the selected on-shell momentum numerator,
Q1, physical sheet, common BV/Green/Fock domain and native `Y14` state-space
identification to remain open, and does not consume P1/P2/P3.

## Selected-cubic reduced-numerator and ledger v0.18 scope gates

`selected_cubic_reduced_numerator_scope_audit.py` enforces the compact-core
`q0-q0` bulk zero, the unselected mixed completion fork, `SOURCE-SILENT`, the
symplectic bulk/preboundary distinction and the Q1/native-`Y14` nonpromotion
fences. `conditional_physics_ledger_v018_scope_audit.py` preserves the 82-row
denominator, `33/19/24/6` verdict counts, residue and four quotient count,
requires exactly four append-only migrations, and corrects `LT-SM8` from
`PROVEN_UNSUPPLYABLE` to `MISSING_CONSTRUCTION` without consuming P1/P2/P3.

## Trace-omega Higgs/chirality Compose and ledger v0.19 scope gate

`trace_omega_higgs_chirality_compose_scope_audit.py` enforces the mandatory
post-`SOURCE-CORRECTS` migration of exactly `RA-D2`, `RA-G2`, `RA-E3` and
`RA-E5` to the typed no-new-datum
`T_omega -> res^V -> sigma_epsilon -> h_omega -> gamma(h_omega)` chain. It
preserves all verdicts/reason kinds, the `RA-D2` genuine-falsification
disposition, residue, four quotient count, P1/P2/P3, Curt separation and the
full-moving selected-cubic Build at rank one. The companion v0.19 channel
probe checks predecessor equivalence for every untouched row and all four
append-only migration edges.

## Selected augmented-torsion D3 owner and ledger v0.20 scope gate

`selected_cubic_augmented_torsion_d3_owner_scope_audit.py` enforces the exact
intrinsic trace/traceless D3 coefficients, the zero `theta_rad-q0-qm` and
nonzero `theta_rad-qm-qm` classes, the stationary pullback jet-order theorem,
the mandatory symplectic nonpromotion and the K95-to-K77 real-form fence. It
requires exactly three append-only distance migrations, leaves `LT-GR3` and
all verdict/reason kinds unchanged, preserves residue and four scoped
quotients, and consumes no P1/P2/P3.

## Selected gauge-rotated LC / Ward owner and ledger v0.21 scope gate

`selected_cubic_gauge_rotated_lc_ward_owner_scope_audit.py` enforces the exact
`(14/3)(p.q)(h0:hm)` shell kernel, zero complete LC--Gauss block, stationary
radial second-jet elimination and the rank-five connection-gauge obstruction.
It requires the mandatory symplectic nonpromotion, five append-only
distance-only migrations, unchanged `LT-GR3`, verdicts, reason kinds, residue,
four scoped quotients and unused P1/P2/P3.

## Selected two-connection principal Ward descent and ledger v0.22 scope gate

`selected_cubic_two_connection_principal_ward_descent_scope_audit.py` enforces
the complete `24+24 -> 24` difference-map rank/kernel theorem, unique
normalized `(1,-1)` coefficients, isolated rank-five versus diagonal rank-zero
gauge blocks, and preservation of the nonzero mixed TT kernel. It requires the
mandatory symplectic fence between principal descent and the full
Ward/BV/preboundary quotient, exactly five append-only distance migrations,
unchanged `LT-GR3`, verdicts, reason kinds, residue and four scoped quotients,
and unused P1/P2/P3.

## Selected intrinsic homogeneous Ward closure and ledger v0.23 scope gate

`selected_cubic_intrinsic_homogeneous_ward_closure_scope_audit.py` enforces
the exact 91-generator moving-Shiab covariance and intrinsic cubic/quadratic
Ward closure, the four frozen-Shiab and wrong-sign defects, nonvacuity and the
independent Sage structural control. It requires the mandatory symplectic
fence between pointwise homogeneous invariance and primitive epsilon Green,
full direct/moving geometry and preboundary/BFV reduction; exactly five
distance-only migrations; unchanged `LT-GR3`, verdicts, reason kinds, revival
triggers, residue and four scoped quotients; and unused P1/P2/P3.

## Two-layer selected-cubic owner retype and ledger v0.24 scope gate

`two_layer_action_selected_cubic_owner_retype_scope_audit.py` enforces the
Layer-0 split among first-order `I1B`, residual `Upsilon_B`, second-layer
`I2B`, and observer `||II||^2`; generic cubic independence and the accidental
one-dimensional plant; one-way solution redundancy; exactly one LT-GR3
distance migration; the split non-conflicting queue; mandatory symplectic
preboundary fence; unchanged verdicts, residue and four scoped quotients; and
unused P1/P2/P3.

## Selected first-order epsilon/preboundary Compose and ledger v0.25 gate

`selected_first_order_epsilon_preboundary_compose_scope_audit.py` enforces the
selected row's inclusion in the prior eight-product epsilon domain, exact
principal/homogeneous/primitive owner composition, compact Dirichlet zero
flux, live unrestricted flux, repository-not-source product attribution,
mandatory symplectic/BFV fence, exactly five distance-only migrations,
unchanged verdicts/residue/quotients and unused P1/P2/P3.

## Moving gimmel/Hodge/frame owner and ledger v0.26 gate

`moving_gimmel_hodge_frame_owner_scope_audit.py` enforces the exact
trace-reversed `Sym2` inertia `(6,4)`, total gimmel inertia `(7,7)`, local TT
density derivative zero, live fixed-frame Hodge response, exact co-moving
frame compensator and Hodge/coframe owner fusion. It requires the mandatory
symplectic fence against action/BV/BFV cancellation, exactly five distance-only
migrations, unchanged verdicts/residue/quotients and unused P1/P2/P3.

## Selected-action co-moving-frame naturality and ledger v0.27 gate

`selected_action_comoving_frame_naturality_scope_audit.py` enforces exact
degree-one/two Hodge naturality, tautological Phi transport, low-grade
Clifford scalar-pairing naturality and zero pure-frame derivative of a nonzero
selected intrinsic action. It requires the mandatory symplectic fence between
frame naturality and physical Euler/presymplectic/BV/BFV stationarity, exactly
five distance-only migrations, unchanged verdicts/residue/quotients and unused
P1/P2/P3.

## Selected-action physical soldering/observation and ledger v0.28 gate

`selected_action_physical_soldering_observation_compose_scope_audit.py`
enforces the exact rank-ten Levi-Civita soldering symbol, complete first-jet
observation/equation dual, nonzero metric Euler receiver, moving-section term
and unrestricted preboundary potential. It requires the symplectic fence
between a preboundary owner and BFV reduction, exactly five distance-only
migrations, unchanged verdicts/residue/quotients and unused P1/P2/P3.

## Selected-action second soldering/observation jets and ledger v0.29 gate

`selected_action_second_soldering_observation_jets_scope_audit.py` enforces
the exact nonzero symmetric-frame spin Levi-Civita second jet, the distinction
from Christoffel `D2`, zero pure-section and nonzero section--field observation
Hessians, the spatial second-section total-derivative owner, and the nonlinear
formal-adjoint Euler/preboundary owner. It keeps direct selected-action
coefficient expansion, BV, global domain and BFV open and preserves all ledger
counts plus unused P1/P2/P3.

## Selected-action stationary spin-LC Hessian and ledger v0.30 gate

`selected_action_stationary_spin_lc_hessian_scope_audit.py` enforces the
Layer-0 separation between the rank-ten coordinate Christoffel map and the
rank-nine action spin-Levi-Civita map, its longitudinal kernel, the exact
stationary selected metric-Hessian causal ranks/inertias, the vanishing
stationary second-lift chain term and the nonzero rank-three diffeomorphism
cross residual. It keeps direct curvature/full-II/defect/observation Ward
totalization, BV, global domain and BFV open and preserves all ledger counts
plus unused P1/P2/P3.

## Selected-action Ward-completion identifiability and ledger v0.31 gate

`selected_action_ward_completion_identifiability_scope_audit.py` enforces the
exact rank-34 symmetric Ward system, its 21-dimensional quotient-form
ambiguity, the non-natural diagnostic-completion fence, the separately
invariant-block and observation-transport controls, and the correction to a
same-`I1B` direct metric/coframe owner. It keeps action-derived completion,
BV, global domain and BFV open and preserves ledger counts plus unused
P1/P2/P3.

## Selected-action coupled diffeomorphism Ward retype and ledger v0.32 gate

`selected_action_coupled_diffeomorphism_ward_retype_scope_audit.py` preserves
the v0.31 metric-only theorem at its scoped grade while enforcing the
rank-four one-form Lie symbol, coupled rank-98/affine-198 target, diagnostic-
completion fence and actual same-`I1B` block-Hessian burden. It forbids
booking the affine freedom as residue or promoting BV/BFV or physics.

## Selected-action source-variable Hessian and ledger v0.33 gate

`selected_action_source_variable_hessian_scope_audit.py` enforces the Layer-0
correction from a frozen-slot one-form surrogate to source variables
`(g,varpi)` with `T=varpi-B_LC(g)`, the exact rank-24 zero-jet Hessian, its
four gauge plus six nongauge null directions and both Ward block equations.
It keeps the full first-order derivative/curvature/density/observation
six-versus-four test, BV, global domain and BFV open and forbids booking
zero-jet nullity as residue or a quotient.

## Selected-action curvature graph six-versus-four and ledger v0.34 gate

`selected_action_curvature_graph_six_versus_four_scope_audit.py` enforces the
exact selected Riemann response, trace ratio twelve, stationary graph gain
`-1/26`, rank-30 gauge-only nonnull kernel and rank-28 null kernel with gauge
four plus two tensor characteristics. It preserves the ambient-curvature
no-go on its larger carrier, keeps off-graph `d_B T`, observation, common
domain, BV and BFV open, and forbids booking characteristics as residue or a
new quotient.

## Selected-action off-graph dBT principal symbol and ledger v0.35 gate

`selected_action_offgraph_dbt_principal_symbol_scope_audit.py` enforces the
formal-adjoint distinction between raw density and Euler symbol, records the
exact adjacent-grade `Cl1`--horizontal-`Cl2` ranks `12/12/11`, rejects the
current 34-variable truncation as action-invariant, preserves the graph
curvature theorem and requires the mandatory symplectic hostile review.

## Selected-action grade-one Schur, observation and ledger v0.36 gate

`selected_action_grade1_dbt_schur_observation_scope_audit.py` enforces the
complete rank-196 indefinite grade-one Hessian, the corrected
curvature-plus-`d_B T` source cross, exact Ward identity and Schur ranks. It
requires the paired observation receiver to preserve the cross, retracts the
generic graph-only `LT-GR1` match, and records the exact positive N2 two-mode
causal candidate without calling it a graviton, selecting `kappa_1`, reducing
residue or promoting a fifth quotient. Symplectic/Green/common-domain/BV/BFV
typing remains mandatory.

## Selected-action N2 little-group, Green flux and ledger v0.37 gate

`selected_action_n2_null_little_group_green_scope_audit.py` enforces the exact
gauge-four-plus-two N2 kernel, its helicity-one rather than helicity-two
compact null-rotation module and its rank-two gauge-descending local principal
Green flux. It requires N2 to be retired only as the completed first-layer
spin-two carrier, preserves the graph-only scoped theorem, and promotes the
distinct second-layer I2B/observer-full-II owner map without changing verdict
counts, residue, quotients, P1/P2/P3, canon or public posture.

## Selected second-layer I2B/Gauss owner map and ledger v0.38 gate

`selected_second_layer_i2b_gauss_owner_map_scope_audit.py` enforces the exact
rank-100 Gauss insertion and projected trace-reversed form inside the complete
rank-1,274 `Cl2` residual carrier. It also requires the explicit `2/39`
orthogonal leakage witness, the `I2B_GAUSS_WRONG_TYPE` disposition,
`SOURCE-SILENT`, mandatory variational/symplectic refusal of a physical phase-
space promotion, and the complete 1,274-by-100 residual target as successor.
It forbids verdict, residue, quotient, P1/P2/P3, canon and public-posture
movement.

## Selected second-layer full-Cl2 pullback and ledger v0.39 gate

`selected_second_layer_full_cl2_residual_pullback_scope_audit.py` requires the
exact rank-100, 640-entry sparse target; full-II and trace-square coefficients;
`(54,46)` inertia; stationary-only co-moving scope; mandatory symplectic
review; and total-residual other-grade support as successor. It forbids
helicity, Euler/preboundary, domain/BV/BFV, residue, quotient, datum, canon and
public-posture promotion.

## Selected second-layer TT Euler, preboundary, helicity and ledger v0.40 gate

`selected_second_layer_tt_euler_preboundary_helicity_scope_audit.py` requires
the exact fourth-order TT polynomial and mass ratio, massless helicity-two
module, massive axial-weight-two TT plane, nonzero action preboundary current
and opposite local pole Green signs. It keeps the massive full `SO(3)` type and complete scalar/vector/
constraint quotient, coupled nonzero-fermion Hessian, common global domain,
odd BV/BFV, positivity and Einstein recovery open. It also requires the
symplectic hostile lens and forbids residue, fifth-quotient, datum, canon or
public-posture promotion.

## Selected second-layer off-TT scalar/Ward owner and ledger v0.42 gate

`selected_second_layer_offtt_scalar_ward_owner_scope_audit.py` requires exact
TT reproduction, rank-four metric-only Ward failure, rejection of the
restricted scalar candidate and the Layer-0 separation of observer/full-II
from the selected residual action owner. It requires all six hostile lenses,
including symplectic geometry, and routes the next Build to full co-moving
`D Upsilon` before scalar, massless-constraint, domain or BV/BFV claims.

## Selected second-layer massive SO3 closure and ledger v0.41 gate

`selected_second_layer_massive_so3_closure_scope_audit.py` requires the exact
five-dimensional spin-two orbit closure and Casimir, the distinct one-state
spin-zero complement, the two-dimensional commutant and the explicit
TT-to-scalar non-identifiability witness. It routes the next Build to the
native full-`B`, background-subtracted off-TT section variation before the
massless constraint complex. It requires all six hostile lenses, including
symplectic geometry, and forbids physical-state, scalar-coefficient, domain,
BV/BFV, residue, fifth-quotient, datum, canon and public-posture inflation.

## Selected second-layer D Upsilon gauge-orbit weld and ledger v0.43 gate

`selected_second_layer_dupsilon_gauge_orbit_weld_scope_audit.py` enforces the
exact rank-four metric Ward load and source-native connection diffeomorphism
orbit, the rank-four forced residual response, and uniqueness of the diagnostic
weld only on that orbit. It keeps the actual selected-`Upsilon` derivative,
twelve transverse connection directions, scalar/constraint quotient,
domain/BV/BFV, residue, fifth quotient, datum, canon and public posture open.
It also requires differential-geometric, representation, variational,
symplectic, Krein/operator, source-critical and archaeology hostile lenses.

## Selected second-layer actual source-lift rank mismatch and ledger v0.44 gate

`selected_second_layer_actual_source_lift_rank_mismatch_scope_audit.py`
enforces the source correction from the rank-four covector-slot proxy to the
rank-three independent connection lift, its time kernel and the mandatory
section/observation successor. It forbids inflating the connection-only route
kill to a full-action, scalar, domain, BV/BFV, datum, quotient or posture result.

## Selected second-layer observation-owner retype and ledger v0.45 gate

`selected_second_layer_observation_owner_retype_scope_audit.py` enforces the
metric/graph-section identity, rejects an independent observation action
column, preserves the source-normal-jet chain-rule route, and routes the next
Build to source-native `j1 Upsilon` before the conditional full-`II` owner-map
comparison. It requires the symplectic lens and forbids scalar, domain, BV/BFV,
datum, quotient or posture inflation.

## Selected second-layer normal-jet carrier compatibility and ledger v0.46 gate

`selected_second_layer_normal_jet_carrier_compatibility_scope_audit.py`
rejects the false residual-Gram factorization, retains the raw rank-four orbit,
and requires all four needed columns to lie in the source-native mixed-normal
carrier. It keeps the actual prolonged source jet, background-subtraction
owner, scalar/domain/BV/BFV, external datum, fifth quotient, canon and public
posture open, with the symplectic lens mandatory.

## Selected second-layer Shiab inverse/Bianchi completion and ledger v0.47 gate

`selected_second_layer_shiab_inverse_bianchi_completion_scope_audit.py`
requires the exact full selected-Shiab isomorphism, unique preimages and four
rank-fourteen principal-Bianchi failures. It rejects only the standalone split
connection-jet identification, routes the next Build to total source-native
Gauss-Codazzi-Ricci completion and keeps scalar/domain/BV/BFV, external datum,
fifth quotient, canon and public posture open, with symplectic review
mandatory.

## Selected second-layer non-null Koszul/GCR split and ledger v0.48 gate

`selected_second_layer_nonnull_koszul_gcr_split_scope_audit.py` requires the
canonical non-null connection support/rank, the separately typed transverse
completion burden, exact selected-Shiab recombination, an open null screen,
mandatory symplectic review and no datum/quotient/posture promotion.

## Selected second-layer GCR Clifford-grade owner retype and ledger v0.49 gate

`selected_second_layer_gcr_exterior_degree_owner_retype_scope_audit.py`
requires the exhaustive 8,281-column `Cl2` grade classification, the exact
rank-1,274 `Cl1 -> Cl2` selected-Shiab isomorphism, preservation of the
`28+117=145` odd packet and exact exclusion of the single-`q` contraction
adapter. It rejects direct Levi-Civita/Gauss--Codazzi--Ricci ownership, routes
the next Build to a source-native odd augmented-torsion/translation-curvature
packet or richer moving epsilon/soldering map, keeps null continuation and
total Bianchi/raw-`Upsilon` naturality open, requires symplectic review and
forbids residue, fifth-quotient, datum, canon or public-posture promotion.

## AC-G1 propagation, pointer reconciliation and ledger v0.50 gate

`ac_g1_propagation_pointer_baseline_scope_audit.py` enforces the real-Clifford
horn boundary, requires current canon/status wording to scope `Sp(64)` to
conditional `Cl(9,5)`, makes the functional-channel target authoritative while
preserving the old PW2F pointer, and types the 49-failure integration record as
historical inherited debt rather than current-head truth. It forbids anomaly,
datum, quotient, canon-verdict or public-posture inflation.

## Translation-curvature partial owner and ledger v0.51 gate

`selected_second_layer_translation_curvature_principal_owner_scope_audit.py`
requires the exact fixed-`B` `q wedge delta T` image, support `28` ownership,
support `117` exclusion, rank-four owned and transverse families, mandatory
symplectic review and current-ledger/contract wiring. It routes the next Build
to the moving gauge-rotated Levi-Civita/epsilon/soldering response and forbids
Euler, BV/BFV, quotient, datum, canon or posture inflation.

## Transverse-117 residual-zero owner class and ledger v0.52 gate

`selected_second_layer_transverse117_residual_zero_owner_class_scope_audit.py`
requires the universal q-exact connection-curvature symbol, support-117
disjointness, zero-background moving-operator product rule, live nonzero-
background control, source epsilon/soldering Layer-0 fence, mandatory
symplectic review and v0.52 ledger/contract wiring. It routes the next Build
to raw-`Upsilon` normal jet or a source-owned nonzero stationary background
and forbids full-action, Euler, BV/BFV, datum, canon or posture inflation.

## Nonzero-background Cartan/Spencer owner and ledger v0.55 gate

`selected_nonzero_background_cartan_spencer_owner_scope_audit.py` requires the
exact rank-1,274 unrestricted Cartan/Spencer isomorphism, coefficientwise
transverse-117 preimages, the zero Levi-Civita-subclass transverse
intersection, mandatory symplectic review and current-ledger/contract wiring.
It routes the next Build to the actual independent-`varpi`/soldering/
observation normal jet and forbids Euler, quotient, datum, canon or posture
inflation.

## Source-varpi / Cartan composition and ledger v0.56 gate

`selected_source_varpi_cartan_composition_scope_audit.py` requires the
fixed-epsilon source tangent `delta B=0`, `delta T=delta A=alpha`, the exact
pointwise rank-four lifts for all transverse 117, zero coefficient freedom at
fixed background, mandatory symplectic review and current-ledger/contract
wiring. It routes the next Build to a covariant four-column graph morphism,
constraint-surplus count and Spencer/atlas integrability, while forbidding
source-selection, Euler, quotient, datum, canon or posture inflation.

## K77 Cartan/Spencer signature correction and ledger v0.57 gate

`selected_k77_cartan_spencer_signature_correction_scope_audit.py` requires
the executed old inertia `(9,5)` and corrected K77 inertia `(7,7)` to be
measured, all changed-coordinate counts to remain exact, the pointwise
rank/support theorem to survive, old coefficient values to be superseded, and
all graph/atlas/Euler/symplectic promotions to remain fenced.

## K77 source-graph basicness and ledger v0.58 gate

`selected_k77_source_graph_basicness_scope_audit.py` requires exact
full-frame three-patch transport to remain distinct from unframed quotient
basicness, records the horizontal and normal rank-four stabilizer defects,
keeps source gauge `epsilon` distinct from observation soldering, refuses to
book positive quotient surplus, requires the symplectic basicness review, and
freezes verdicts, residue, quotients, datum, canon and posture.

## K77 full-reduction quotient reconciliation and ledger v0.59 gate

`selected_k77_full_reduction_quotient_reconciliation_scope_audit.py` requires
the source-owned labelled Clifford reduction and its central `U(1)` stabilizer
to remain distinct from the horizontal-plane forgetful quotient. It preserves
v0.58's normal defect, requires the exact invariant-target-span obstruction,
counts no orbit-transport surplus, keeps observation Euler/preboundary and
symplectic descent open, and freezes verdicts, residue, quotients, datum, canon
and posture.

## K77 total raw-Upsilon and labelled null screen ledger v0.60 gate

`selected_k77_total_upsilon_null_screen_scope_audit.py` keeps the complete
superconnection Bianchi identity distinct from raw-`Upsilon` naturality and
from the source's `Xi=D Upsilon` redundancy. It requires the exact rank-four
all-grade residual after restoring `kappa_1 T`, the labelled ambient rank-12
`(6,6)` null screen, the separate 4D `10 -> 6 -> 2` physical quotient, the
mandatory symplectic scope fence, zero identity-surplus inflation, and frozen
verdicts, residue, quotients, datum, canon and posture.

## K77 coupled all-grade raw-Upsilon graph ledger v0.61 gate

`selected_k77_coupled_all_grade_upsilon_graph_scope_audit.py` requires the
predeclared 1,470-dimensional source tangent, 4,330-coordinate output support,
rank-1,470/nullity-zero response, four unique conditional lifts, full Bianchi
and paired labelled-frame descent. It keeps the source-silent `-J_2D` target,
2,860-dimensional compatibility cokernel, zero local predictive surplus, and
open Euler/preboundary/symplectic gate separately typed while freezing
verdicts, residue, quotients, datum, canon and posture.

## K77 labelled-null observation-jet Euler/preboundary sufficiency v0.62 gate

`selected_k77_observation_jet_euler_preboundary_scope_audit.py` requires the
labelled-null response rank 1,470/nullity zero, four unique null lifts, one
exact conormal graph derivative, and the live rank-650/nullity-820 source
principal symbol. It keeps the symbol distinct from the invariant Green
current, requires the paired `(Upsilon,Xi)` action/equation dual to remain
open, includes the mandatory symplectic fence, and freezes verdicts, residue,
quotients, P1/P2/P3, canon and posture.

## K77 paired Upsilon/Xi and formal Green-owner v0.63 gate

`selected_k77_paired_upsilon_xi_green_scope_audit.py` requires the graph's
degree-one primalized carrier, the fixed-Hodge degree-thirteen density and the
printed degree-fourteen Xi companion to remain distinct. It requires exact Xi
supports `16,15,11,11`, rank-zero dependence after total-Upsilon closure,
nonzero unrestricted and zero Dirichlet Green flux, and an explicit open flag
for the action-owned K77 Krein pair and antisymmetrized presymplectic current.
It freezes verdicts, residue, quotients, P1/P2/P3, canon and posture.

## K77 action-owned degree-fourteen companion v0.64 gate

`selected_k77_action_owned_degree14_companion_scope_audit.py` requires the
action companion to use both degree-thirteen connection Euler owners and the
moving-Shiab orbit covector. It keeps that generally nonzero primitive epsilon
Euler equation distinct from printed `D Upsilon`, the zero homogeneous Ward
contraction and any antisymmetrized presymplectic/BFV object. It requires the
moving K77 observation insertion to remain open and freezes verdicts, residue,
quotients, P1/P2/P3, canon and posture.

## K77 moving action-Green receiver v0.65 gate

`selected_k77_moving_action_green_receiver_scope_audit.py` requires the
moving target, section, indefinite primalizer and action Euler terms to remain
independently live. It requires exact complete-germ first-variation and Green
transport while preserving ordinary pullback's rank-ten conormal loss. It
keeps the source-native normal Euler jet, antisymmetrized current, BFV quotient
and common domain open and freezes verdicts, residue, quotients, P1/P2/P3,
canon and posture.

## K77 selected-action normal Euler mixed-Hessian v0.66 gate

`selected_k77_source_native_normal_euler_jet_scope_audit.py` requires the
selected action's normal Euler jet to be typed as the mixed action Hessian,
keeps it distinct from the source-printed residual jet, requires all seven
normal-owner classes and zero new free objects, and leaves the coefficientwise
full-K77 bank, antisymmetrized current, basic/common-domain/BFV descent open.
It freezes verdicts, residue, quotients, P1/P2/P3, canon and posture.

## K77 full normal geometry and owner-split correction v0.67 gate

`selected_k77_full_normal_owner_bank_scope_audit.py` requires all ten K77
normal metric directions, the rank-one density bank, and the rank-ten
degree-one/two pairing and Hodge banks. It keeps a vertical coefficient value
distinct from its normal first jet, narrows the seven v0.66 owner buckets to a
chosen trivialization, and preserves only the total mixed Hessian as intrinsic.
It routes next to the Green-potential splitting-change/basicness test, requires
the vertical B/T lift to remain open unless a nonbasic defect survives, and
freezes verdicts, residue, quotients, P1/P2/P3, canon and posture.

## K77 Green-potential point-splitting basicness v0.68 gate

`selected_k77_green_potential_splitting_basicness_scope_audit.py` requires
the complete action-owned Green potential and its field-space exterior
derivative to transport naturally under nonlinear point-frame cotangent
lifts, including a three-splitting cocycle. It requires all ten induced K77
normal/base momentum corrections and a firing partial-potential control. It
retires the vertical B/T lift only for point-trivialization descent, keeps
derivative-dependent contact transformations and physical gauge basicness
open, and freezes verdicts, residue, quotients, P1/P2/P3, canon and posture.

## K77 contact-presymplectic gauge basicness v0.69 gate

`selected_k77_contact_presymplectic_gauge_basicness_scope_audit.py` requires
the actual rank-ten Levi-Civita contact block, diagonal two-connection Ward
closure, fixed-parameter Lie invariance and small/Dirichlet-gauge
horizontality. It separately requires the nonzero unrestricted boundary
moment map in all ten K77 directions, keeps the physical boundary domain or
edge-mode extension and full nonlinear ambient reduction open, and freezes
verdicts, residue, quotients, P1/P2/P3, canon and posture.

## K77 minimal edge-mode reduction v0.70 gate

`selected_k77_minimal_edge_mode_reduction_scope_audit.py` requires the
structural scalar-counterterm failure, unique edge coefficients `(-1,+1)`,
exact all-ten extended dimension/rank/kernel `60/40/20`, and nondegenerate
conditional quotient dimension/rank `40/40`. It books exactly one new scoped
quotient while freezing verdicts and global residue. It keeps the global
labelled `Y14` edge bundle, source-selected physical domain, BFV phase space,
polarization, common domain, P1/P2/P3, canon and posture open.

## K77 tilted edge-bundle type bridge v0.71 gate

`selected_k77_tilted_edge_bundle_type_bridge_scope_audit.py` requires exact
separate tilted affine-one-form and group-valued edge-frame cocycles, the
constant-`xi` zero-form/one-form mismatch, and the null zero-order natural
bridge. It keeps the dressed preboundary form, typed differential/soldering or
domain bridge, global quotient, BFV, common domain, P1/P2/P3, canon and posture open.

## K77 group-edge dressing and Maurer-Cartan bridge v0.72 gate

`selected_k77_group_edge_dressing_maurer_cartan_bridge_scope_audit.py`
requires the exact universal dressed pair `q=xu^-1`, `pi=p u^T`, rank-eight
pulled-back two-form, four-dimensional characteristic kernel equal to the
right `gl(2)` orbit, and recovered v0.70 minus sign. It requires `u^-1 d u` to
remain a flat/pure-gauge tilted bridge, not arbitrary `varpi`, and keeps the
actual K77 `H` representation/action, nonzero `A0`, global BFV, common domain,
P1/P2/P3, canon and posture open.

## K77 two-endpoint edge dressing v0.73 gate

`selected_k77_two_endpoint_edge_dressing_scope_audit.py` requires the actual
K77 `U(64,64)` group owner, exact source/target cotangent kernel equality, and
the material `p0=p2`, `40/40 -> 20/20` single-holonomy fence. It keeps two
continuum endpoint action owners, primitive epsilon preboundary ownership,
full `tau_A0`, BFV/common domain, P1/P2/P3, canon and posture open.

## K77 epsilon endpoint direct-sum v0.74 gate

`selected_k77_epsilon_endpoint_direct_sum_scope_audit.py` requires the local
epsilon trace map to have rank two and the two-copy K77 dressing to recover the
full `60/40/20 -> 40/40` endpoint quotient. It also requires the hostile
scope repair: `i_n(E_B-E_T)=p_KT` is an open coefficient weld, so the v0.70
boundary coordinates are not yet retyped as existing epsilon traces. The
single-holonomy no-go, full `tau_A0`, global BFV/common domain, P1/P2/P3,
canon and posture remain fenced.

## K77 action/contact Legendre-owner v0.75 gate

`selected_k77_action_contact_legendre_owner_scope_audit.py` preserves the
generic contact/Ward/Green/symplectic theorem, independent endpoint cotangent
variables, direct-sum `40/40` quotient and single-holonomy no-go. It requires
the exact two-`K` nonuniqueness control, cubic selected-action scaling,
nonzero `E_B-E_T` at `T=0`, and rejection of `p=KT` as selected-action
ownership. The actual all-ten oriented action boundary bank, observation
receiver, full `tau_A0`, global BFV/common domain, P1/P2/P3, canon and posture
remain fenced.

## K77 selected-action boundary coefficient-bank v0.76 gate

`selected_k77_action_boundary_coefficient_bank_scope_audit.py` requires the
exact selected `Cl1+Cl2` action bank, ten independent normal rows, lossless
complete observation, nondegenerate indefinite scalar-Clifford images and
opposite local endpoint orientations. It forbids promotion to the full
`U(64,64)` carrier, global physical observation, full Krein domain,
`tau_A0`/BFV, P1/P2/P3, canon or public posture.

## K77 full pointwise u(64,64) action-bank v0.77 gate

`selected_k77_full_u6464_action_bank_scope_audit.py` requires the exact
16,384-real-dimensional pointwise comparator, live-grade fingerprint
`14/59/476`, ranks `14/10`, corrected raw/observed inertia `(4,6,0)`, a
symplectic hostile review and explicit P1/P2/P3 non-use. It forbids promotion
to global adjoint-bundle, physical observation, preferred-Shiab, BFV,
common-domain, canon or public-posture status.

## K77 action-bundle and observation-overlap v0.78 gate

`selected_k77_action_bundle_observation_overlap_scope_audit.py` requires
patchwise recomputation under two noncommuting K77 transitions, exact direct
and sequential action/complete-observation/no-leakage-projector descent, fired
frozen-map and hidden-covector controls, a symplectic hostile review, and
explicit P1/P2/P3 non-use. It forbids promotion to arbitrary-X physical
section integrability, ordinary-pullback faithfulness, preferred Shiab,
global BFV/common domain, canon or public-posture status.

## K77 physical observation-section faithfulness v0.79 gate

`selected_k77_physical_section_faithfulness_scope_audit.py` requires the spin
`S4` counterexample to arbitrary-`X` Lorentz-section existence, exact local
holonomic first/second jets, the universal ordinary-pullback rank `4` plus
conormal rank `10`, and the nonzero selected augmented-torsion Euler witness
in that kernel. It preserves the complete `4+10` receiver while forbidding a
sixth quotient, physical vertical-field interpretation, global BFV/domain,
P1/P2/P3, canon or public-posture promotion.

## K77 metric-section/Bianchi typing v0.80 gate

`selected_k77_metric_section_bianchi_typing_scope_audit.py` requires the
complete field/equation dual to retain all ten graph-conormal directions as
independent metric-section Euler coordinates. It rejects erasing that entire
ten-dimensional sector as “BV,” and separately requires the standard
linearized Einstein comparator complex to be exact at noncharacteristic
covectors and to carry a two-dimensional null helicity-two cohomology. The
actual selected K77 vertical Euler/Ward symbol, global BFV/domain,
P1/P2/P3, canon and public posture remain open.

## K77 coupled Euler-complex scope v0.81 gate

`selected_k77_coupled_euler_complex_scope_audit.py` requires the retained ten
metric equations to remain distinct from a closed vertical-only subsystem. It
requires the exact 34-variable first-layer Ward complex with generic physical
cohomology zero, the exceptional helicity-one typing, the second-layer TT
diagnostic plus rank-four full Ward defect, and the rank-four defect of naive
layer addition. It rejects a 21-dimensional formal Ward fit as construction
and keeps microlocal hyperbolicity, common Green/Krein domain, global BV-BFV,
P1/P2/P3, canon and public posture open.

## K77 stationary two-layer Hessian factorization v0.82 gate

`selected_k77_stationary_two_layer_hessian_factorization_audit.py` requires
the exact stationary `H2=(D Upsilon)^!K*(D Upsilon)` factorization, preserves
independent physical Shiab/Hodge constituent movement, rejects substitution
of the first-action Schur Hessian for the residual Jacobian, and keeps
observation as a dependent receiver. It requires symplectic, Krein and
complex/path-integral fences and leaves the actual common-field `D Upsilon`,
pairing/formal adjoint, Green concomitant, physical kernel, BV-BFV,
P1/P2/P3, canon and public posture open.

## K77 common-field D-Upsilon varpi block v0.83 gate

`selected_k77_common_field_dupsilon_varpi_block_audit.py` requires the exact
24-dimensional source-horizontal `D_varpi Upsilon` block, its 56-coordinate
grade support and rank-three causal diffeomorphism interface. It rejects
promotion of an orbit-only metric completion and import of the older
rank-four metric diagnostic on the fixed-`epsilon` horn, while preserving
source `epsilon` as the unbuilt revival route. It requires the Layer-0
distinction between covariant `D_omega Upsilon` and Frechet
`D_epsilon Upsilon`, plus symplectic, Krein and complex/path-integral fences.

## K77 gamma-soldered epsilon D-Upsilon orbit v0.84 gate

`selected_k77_gamma_soldered_epsilon_dupsilon_orbit_audit.py` requires the
ordinary spin/Levi-Civita Kosmann lift to remain an exact rank-three
negative control with the source-`varpi` longitudinal kernel. It separately
requires the already-owned grade-one `gamma_epsilon` construction to supply
rank four in every causal class, remain nonzero on the missed direction, and
close the four principal `J R=0` columns without a new field, datum,
coefficient or quotient. It preserves source silence on physical soldering,
keeps all six transverse metric columns and lower-order epsilon response open,
and requires symplectic, Krein and complex/path-integral fences.

## K77 metric-transverse augmented-torsion block v0.85 gate

`selected_k77_metric_transverse_augmented_torsion_block_audit.py` requires
the source-owned `delta_gT=-L_qh` principal block, exact Levi-Civita rank nine,
its unique kernel inside the diffeomorphism orbit, and rank-six injectivity on
the transverse metric directions in all causal classes. It also requires the
actual partial metric/varpi/gamma-epsilon Ward packet to remain rank four and
unowned by the still-missing moving Shiab/Hodge/curvature/density/observation
operator. Principal rank, full Frechet closure, pairing/Green, symplectic and
physical claims remain separated.

## K77 principal Ward/gamma-epsilon reconciliation v0.86 gate

`selected_k77_principal_ward_gamma_epsilon_reconciliation_audit.py` requires
source epsilon and conditional gamma-epsilon soldering to remain distinct. It
requires exact direct metric/varpi torsion cancellation, the surviving
source-variable curvature packet to have rank three in all causal classes,
and the gamma extension to remain rank four and nonzero on the sourced kernel.
The moving operator is narrowed, not eliminated. Full Frechet, adjoint/Green,
Krein, symplectic/BFV and physical claims remain open.

## K77 Kosmann/moving-Shiab rank-three closure v0.87 gate

`selected_k77_kosmann_moving_shiab_rank3_audit.py` requires covector-matched
causal response operators, rejection of moving Shiab as a standalone negative
packet, and exact zero-fit closure only for the complete lower-order internal
bivector gauge orbit. It keeps physical diffeomorphism Frechet/Green,
primitive epsilon, Krein, symplectic and BFV descent open.

## K77 physical diffeomorphism split v0.88 gate

`selected_k77_physical_diffeomorphism_split_audit.py` requires the natural
physical rank-four lift, its rank-three Kosmann/skew response and nonzero
symmetric longitudinal complement. It preserves the degree-two Hodge sampled
scope, records the moving observation negative control and source silence on
the exact formula, and rejects promotion from local residual-zero naturality
to full action Frechet, Green, symplectic, BFV, domain or Einstein recovery.

## Hostile-review lens coverage and independent-adjudication gate

`hostile_review_lens_coverage_audit.py` reports the aggregate declared-lens
census without treating a distribution as a failure. Its separate hard gate
names any live over-determined row whose adjudication evidence still points
only to the cluster that found it, enforcing the independent-owner rule.
## K77 bulk-operator admission ledger v0.117

`selected_k77_bulk_operator_admission_audit.py` requires the exact safe
`(2,1,1)` source-action mixed-order grammar while refusing to promote it to an
actual principal-symbol theorem. It keeps predecessor Hessian blocks scoped to
their backgrounds, requires the branch/parent ports plus gauge fixing and bulk
ghosts before `Dmax/Dmin`, and types H7/H8 as a kinematic target. It preserves
all three action parents, P1/P2/P3, canon and public posture.

## K77 branch-Hessian discriminator ledger v0.118

`selected_k77_branch_hessian_discriminator_audit.py` requires the exact
noncritical-coordinate trap, the same-inertia source-`varpi` restrictions for
both distinct actions, and explicit retention of both branches and all three
parents. It rejects Galois transfer as a positivity/Morse theorem and preserves
verdicts, residue, quotients, P1/P2/P3, canon and public posture.

## K77 two-branch action-block port ledger v0.119

`selected_k77_two_branch_action_block_port_audit.py` requires both exact
branches to retain the already-owned rank-91 first-action epsilon/Cl1 cross,
rank-1470 zero-jet low-grade `varpi` map and common selected principal Gram
ranks `110/110/16`. It rejects principal-to-full-Frechet, selected-to-expanded-
parent and finite-rank-to-domain promotion while preserving both actions, all
parent scopes, residue, quotients, P1/P2/P3, canon and public posture.
