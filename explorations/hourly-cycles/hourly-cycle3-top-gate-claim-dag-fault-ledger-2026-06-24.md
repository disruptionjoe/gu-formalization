---
title: "Hourly Cycle 3 Top-Gate Claim DAG / Fault-Finality Ledger"
date: "2026-06-24"
status: exploration/governance
doc_type: top_gate_claim_dag_fault_finality_ledger
verdict: "COARSE_DAG_EXISTS_BUT_CYCLE3_TOP_GATE_DAG_REMAINS_REQUIRED_GOVERNANCE_ARTIFACT"
owned_path: "explorations/hourly-cycle3-top-gate-claim-dag-fault-ledger-2026-06-24.md"
companion_audit:
  - "tests/hourly_cycle3_top_gate_claim_dag_fault_ledger_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/persona-review-distributed-systems-2026-06-24.md"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
  - "NEXT-STEPS.md"
  - "explorations/hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md"
  - "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md"
  - "explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md"
  - "explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md"
  - "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md"
  - "explorations/hourly-cycle2-fixed-data-phi-obs-sector-ledger-2026-06-24.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
  - "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
  - "explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md"
  - "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md"
---

# Hourly Cycle 3 Top-Gate Claim DAG / Fault-Finality Ledger

## 1. Verdict

The repo has a usable coarse live DAG in
`explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`, but it is not yet the
usable Cycle 3 top-gate DAG after the hourly Cycle 1 and Cycle 2 refinements. It names the
right governance layer, but several top gates have since been pushed down to sharper first
missing objects:

| top gate | Cycle 1/2 refined blocker |
|---|---|
| theta / IG action | `K_IG_selector` and source-forced field degrees |
| RS generation | source-defined gauge/BRST differential `d_RS,-1` |
| `Phi_obs` / Type II1 selector | `FIXED_DATA_X_CERTIFICATE` and target-free `Phi_obs` image |
| QFT / CHSH | `P_fin^b` plus 16 local `gu-derived:` mode records |
| VZ | `ActualDGU01OperatorCertificate` |
| meta process | top-gate machine-readable registry with fault/finality rules |

Decision:

```text
repo_has_coarse_live_DAG: yes
repo_has_cycle3_top_gate_DAG_after_cycles_1_2_before_this_file: no
this_file_supplies_cycle3_top_gate_DAG_v0: yes
mathematical_claim_upgrades_made_here: none
governance_status: required_artifact_now_available_as_exploration_v0
```

This artifact is a governance object. It is not evidence for GU, does not close any physics
or mathematics gate, and does not promote any exploration to canon. Its purpose is to make
the current partial order auditable: every downstream status is bounded by its weakest
load-bearing missing proof object.

## 2. DAG node schema

Every top-gate node in this ledger must carry the following fields.

| field | meaning |
|---|---|
| `node_id` | Stable top-gate identifier used by audits and future maintenance. |
| `claim_surface` | The claim family whose status this node bounds. |
| `owner_files` | Current files that own the live decision or most precise blocker. |
| `accepted_inputs` | Inputs allowed to support the node without rollback. |
| `forbidden_inputs` | Inputs that count as invalid messages, target leakage, control import, or stale upgrade. |
| `dependencies` | Upstream objects that must exist before the top claim can close. |
| `supersessions_demotions` | Earlier claims or weaker blockers replaced by Cycle 1/2 results. |
| `closure_condition` | Exact condition for promotion or closure. |
| `current_status` | Present top-gate status. |
| `current_proof_grade` | Best current proof grade, deliberately not inflated. |
| `invalid_message_fault_model` | Adversarial/fault model for this node. |
| `finality_rule` | What may be cited now and what is not final. |
| `first_missing_object` | First exact proof object or source datum now blocking the gate. |
| `claim_upgrade_allowed` | Must be `false` in this artifact; upgrades require future proof objects. |

Node status vocabulary:

```text
underdefined
blocked
negative_filter_current_classes
conditional_template
governance_required
```

Proof-grade vocabulary:

```text
raw_control
contract_only
conditional_template
formal_negative_filter
executable_control
governance
open_none
```

Finality vocabulary:

```text
not_final
conditional_negative_finality
typed_template_finality_only
control_finality_only
governance_finality
```

Global downgrade rule:

```text
No downstream node may inherit a stronger status than the weakest load-bearing dependency.
No control, ansatz, host, target-fitted value, or visible-cardinality toy may be cited as a
derived GU result.
```

## 3. Top-gate node table

### Compact registry

| node_id | top gate | current_status | current_proof_grade | first_missing_object | finality_rule |
|---|---|---|---|---|---|
| `THETA_IG_ACTION` | theta / IG action and FLRW coefficient route | `underdefined` | `conditional_template` | `K_IG_selector` | `not_final` for dark energy; Branch 3 template only |
| `RS_GENERATION` | RS physical rank and generation count | `underdefined` | `raw_control` plus `contract_only` | `d_RS,-1` | `not_final` for rank 4, rank 8, and generations |
| `PHI_OBS_TYPEII1` | `Phi_obs` / Type II1 fixed-data selector | `negative_filter_current_classes` | `formal_negative_filter` plus `contract_only` | `FIXED_DATA_X_CERTIFICATE` | negative filter only; no positive selector finality |
| `QFT_CHSH` | source-mode quotient, positive seed, covariance, CHSH | `blocked` | `executable_control` only | `SourceProjectorPFinBWithLocalModeRecords` | controls only; physical forcing not final |
| `VZ_ACTUAL_OPERATOR` | VZ actual operator, FC-VZ-1, FC-VZ-4 | `underdefined` | `conditional_template` | `ActualDGU01OperatorCertificate` | typed-spine finality only |
| `META_PROOF_PROCESS` | proof-grade process and top-gate governance | `governance_required` | `governance` | top-gate registry maintenance rule | governance finality only |

### THETA_IG_ACTION

- Claim surface: nonzero theta, source-forced IG dynamics, FLRW scalar coefficient packet,
  and any dark-energy `xi_eff` comparison.
- Owner files: `explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md`,
  `explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md`,
  `explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`, and
  `explorations/gu-minimal-action-spec-2026-06-24.md`.
- Accepted inputs: source-locked GU action or parent action; source-selected `K_IG`, `Q_IG`,
  `Z_U`, `V_src`, `S_cross_src`, field degrees, and boundary data; full EL tuple; derived
  total current `theta_eff`; FLRW scalar-mode survival; same-branch `Z_theta`,
  `C_Rtheta`, and `xi_eff = C_Rtheta / Z_theta`; empty target-input log.
- Forbidden inputs: DESI/Rubin windows upstream; `xi_eff < -0.319` or `xi_eff ~= -0.6` used
  as selector input; bare `Lambda`; bare `R theta^2`; `K_IG = D_A U` chosen only because it
  is natural; Branch 3 template promoted without source selector; free `beta` plus only
  `|theta|^2` while claiming nonzero theta.
- Dependencies: `K_IG_selector`; field-degree selector; source-forced `S_IG_dyn` or parent
  action; total-current Noether/projection proof; `SourceForcedThetaFLRWCoefficientPacket`.
- Supersessions/demotions: Cycle 2 supersedes the broader Cycle 1 packet block by placing
  the first block at `K_IG_selector`; the free-beta bare-theta branch remains a negative
  conditional result because it kills nonzero theta.
- Closure condition: source geometry selects a complete IG dynamics packet before targets,
  the locked action emits scalar mode, `Z_theta > 0`, `C_Rtheta`, and `xi_eff`, and
  replacement-target checks do not change the packet.
- Current proof grade: `conditional_template`.
- Invalid-message/fault model: target fitting, auxiliary-field collapse, hidden variation
  constraints, missing total-current terms, and source templates laundered as source
  selection.
- Finality rule: not final for dark energy or `xi_eff`; cite only that Branch 3 is a
  coherent template and that the source selector is missing.
- First missing object: `K_IG_selector`.
- Claim upgrade allowed here: no.

### RS_GENERATION

- Claim surface: physical RS effective rank, RS index, total generation count, and
  Candidate A/B comparison.
- Owner files: `explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md`,
  `explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md`,
  `explorations/generation-count-rs-symbol-index-contract-2026-06-24.md`, and
  `tests/rs_clifford_projector_model.py`.
- Accepted inputs: source-selected right-H physical RS domain; gamma-trace maps; source
  gauge/BRST differential; ghost/antighost or gauge-fixing data; symbol exactness or
  ellipticity; H-linear trace/index certificate; source-selected `F/ch2`; same-operator
  `K3/Y14` or APS bridge.
- Forbidden inputs: `ind_H(D_RS)=8`; total `ind_H(D_GU)=24`; three generations; four
  generations; `rank_H(E_RS^eff)=8/2`; raw `96_C` promoted to physical H-rank; halving
  complex rank without H-linear trace; BRST-style subtraction without source ghost data.
- Dependencies: `d_RS,-1`; `Pi_RS^phys`; `E_RS^eff`; H-linear trace; source-selected
  background; same-operator bridge.
- Supersessions/demotions: Cycle 2 pushes the broad "effective rank certificate missing"
  obstruction down to the source-defined gauge/BRST differential; raw projector rank remains
  raw-only.
- Closure condition: complete source-derived quotient/BRST or gauge-fixed elliptic complex
  computes an H-linear index/rank with no target inputs. Rank 4 would conditionally support
  Candidate A; rank 8 would conditionally support Candidate B; any other value forces
  reformulation.
- Current proof grade: `raw_control` plus `contract_only`.
- Invalid-message/fault model: target division, raw algebra masquerading as analytic index,
  missing quotient, complex-only trace conversion, compact K3 control treated as GU theorem.
- Finality rule: not final for rank 4, rank 8, three generations, or four generations.
- First missing object: `d_RS,-1`.
- Claim upgrade allowed here: no.

### PHI_OBS_TYPEII1

- Claim surface: exact finite Connes-channel `Phi_obs`, replacement observer shadow,
  Type II1 selector, SM gauge/one-generation/three-generation finite-control targets.
- Owner files: `explorations/hourly-cycle2-fixed-data-phi-obs-sector-ledger-2026-06-24.md`,
  `explorations/hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md`,
  `explorations/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md`, and
  `canon/type-ii1-spectral-sm-checklist.md`.
- Accepted inputs: fixed data
  `(N subset M, tau, A, H, D, J, gamma, Phi_obs)` selected independently of targets;
  sector idempotents; Markov traces; fusion/equivalence classes; spectral compatibility;
  actual observer-mode anomaly shadow; `n=2`, `n=4`, and `n` replacement obstructions.
- Forbidden inputs: `A_F`; finite CC tuple; `G_SM`; central `Z_6`; `K_SM`; `n=3`; `C3`;
  index 3; D4 arms; three projections; `dim H_F=96`; ordinary anomaly-free SM shadow;
  physical Higgs data; equal trace alone.
- Dependencies: `FIXED_DATA_X_CERTIFICATE`; target-free `Phi_obs` image; `N_NEQ_3`
  replacement obstruction; sectorwise spectral compatibility; actual observer-mode anomaly
  shadow.
- Supersessions/demotions: Cycle 2 demotes C3/D4 from candidate selector to negative
  control; Cycle 1 keeps finite Connes control as observer-facing certificate, not primary
  substrate axiom.
- Closure condition: fixed Type II1 data compute `T_A`, `T_G`, `T_1`, and `T_3` or a
  declared replacement shadow without target inputs, and nearest replacements fail by a
  named spectral, index, standard-invariant, anomaly, or Connes-channel obstruction.
- Current proof grade: `formal_negative_filter` for cardinality/current candidate failures,
  `contract_only` for positive `Phi_obs`.
- Invalid-message/fault model: host mistaken for selector, visible cardinality transported
  through Type II1 language, SM finite data attached externally, anomaly-safe copies used
  as selector.
- Finality rule: conditional negative finality for current instantiated selector classes;
  not final for positive `Phi_obs`, SM gauge, Higgs, or generation selection.
- First missing object: `FIXED_DATA_X_CERTIFICATE`.
- Claim upgrade allowed here: no.

### QFT_CHSH

- Claim surface: finite source-mode quotient data, positive one-particle seed, quasifree
  covariance/state, Alice/Bob finite state, and CHSH physical forcing.
- Owner files: `explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md`,
  `explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md`,
  `explorations/observer-finality-pati-salam-chsh-fixture-2026-06-24.md`, and
  `explorations/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md`.
- Accepted inputs: `P_fin^b`; exactly 16 local `gu-derived:` source-mode records in
  `K_b = (4,2,1) direct_sum (4bar,1,2)`; source raw representatives; local support or
  local algebra inclusion; exact `H_raw`; removed-direction representatives
  `EOM_b/Gauge_b/Constraint_b/Ghost_b/Null_b`; exact `Q_b`; `H_phys = Q_b^* H_raw Q_b`;
  positivity/rank certificate; later source covariance and GU-admissible observables.
- Forbidden inputs: identity Gram as GU derivation; Bell state; Pauli controls; free vacuum;
  Hadamard/Fock state; target-fitted covariance or CHSH state; Stinespring/CPTP source
  without GU derivation; direct-sum carrier silently used as tensor product; Pati-Salam
  labels as physical Gram.
- Dependencies: `SourceProjectorPFinBWithLocalModeRecords`; `SourceRawGramRuleAndMatrix`;
  `FinitePhysicalQuotientRepresentatives`; positive finite seed; covariance gate; derived
  `rho_AB`; GU-admissible observables; locality/NAC data.
- Supersessions/demotions: Cycle 2 pushes the Cycle 1 finite Gram block down to missing
  `P_fin^b` and local mode records; CHSH fixtures remain executable controls, not GU state.
- Closure condition: clean source-mode quotient packet computes positive nonzero `H_phys`
  first; only later may source covariance, `rho_AB`, and admissible observables support a
  CHSH computation.
- Current proof grade: `executable_control` only.
- Invalid-message/fault model: control mistaken for derived state, nonlocal basis hiding
  correlations, imported identity pairing, gauge/constraint leakage, and direct sum/tensor
  import.
- Finality rule: control finality only; physical CHSH and QFT recovery are not final.
- First missing object: `SourceProjectorPFinBWithLocalModeRecords`.
- Claim upgrade allowed here: no.

### VZ_ACTUAL_OPERATOR

- Claim surface: actual GU RS 0/1 operator, FC-VZ-1 E-block invertibility, spin-3/2 Schur
  route, FC-VZ-4 subprincipal/extrinsic-curvature characteristics, and no-go map wording.
- Owner files: `explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md`,
  `explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md`,
  `explorations/vz-proof-grade-closure-attempt-2026-06-24.md`, and
  `canon/no-go-class-relative-map.md`.
- Accepted inputs: source-closed `D_GU^epsilon` 0/1-sector certificate; rolled-up
  domain/codomain; `sigma_1(D_GU^epsilon)`; coefficients `a`, `b`, `lambda_d`; separated
  `Phi_2`, `Phi_d`, `F_xi`, `Phi_F`; Q projectors; all real mixed non-null covectors;
  actual section-pulled `sigma_0_inv(S_Rs_4D_full)` including `II_s^H`, `Z_A`, Poisson
  corrections, and `K_mu_nu`.
- Forbidden inputs: displayed typed-spine matrix treated as actual operator; `Phi_F` used
  as source of `F_xi`; hidden first-order terms placed in `Z_A`; pure-covector-only audit;
  trace and embedded conventions mixed; "verified" VZ language before FC-VZ-1 and FC-VZ-4.
- Dependencies: `ActualDGU01OperatorCertificate`; `E_actual` all-covector kernel audit;
  actual R-sector Schur symbol; `ActualDGUSectionSubprincipalCertificate`; coupled
  RS/constraint characteristic matrix.
- Supersessions/demotions: Cycle 2 supersedes typed-spine arithmetic as the live blocker:
  the typed spine remains conditional evidence but not actual-operator closure. The no-go map
  wording remains capped at conditional 14D and 4D principal-symbol only.
- Closure condition: actual operator certificate closes FC-VZ-1 for every real non-null
  mixed covector, then the same operator's section-pulled subprincipal/constraint matrix has
  no non-null spacelike characteristics.
- Current proof grade: `conditional_template`.
- Invalid-message/fault model: candidate operator laundered as source-closed operator,
  order-convention confusion, same-session closure inflation, lower-order terms becoming
  effective order one after pullback, constraint subsystem changing the cone.
- Finality rule: typed-template finality only; full VZ evasion and actual-operator status
  are not final.
- First missing object: `ActualDGU01OperatorCertificate`.
- Claim upgrade allowed here: no.

### META_PROOF_PROCESS

- Claim surface: status discipline, proof-grade vocabulary, no-smuggling guardrails, and
  live top-gate dependency management.
- Owner files: `RESEARCH-POSTURE.md`,
  `process/runbooks/five-lane-frontier-run.md`,
  `explorations/persona-review-distributed-systems-2026-06-24.md`, and
  `explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`.
- Accepted inputs: explicit assumptions; source files; machine-readable gate registries;
  independent proof/computation artifacts; audits that check no upgrades; correction logs.
- Forbidden inputs: consensus as mathematical proof; stale canon drift; same-session
  upgrade laundering; "compatible with" becoming "derived from"; process discipline treated
  as physics evidence.
- Dependencies: all top gates above, plus update discipline when any node changes.
- Supersessions/demotions: this file supersedes the earlier coarse live DAG only for the
  six Cycle 3 top-gate statuses after cycles 1 and 2; it does not replace the repo-wide
  ledger.
- Closure condition: every future upgrade or demotion changes the node status, dependency
  edge, forbidden-input list, and finality rule in one pass, and no audit detects a stronger
  downstream status than its dependency allows.
- Current proof grade: `governance`.
- Invalid-message/fault model: stale graph, missing edge, vague node semantics, and graph
  bureaucracy that stops affecting decisions.
- Finality rule: governance finality only; useful for status transitions, not evidence for
  physics or mathematics.
- First missing object: canon-facing top-gate maintenance rule and audit adoption.
- Claim upgrade allowed here: no.

## 4. Dependency/supersession edges

### Dependency edges

| from | to | edge_type | meaning |
|---|---|---|---|
| `META_PROOF_PROCESS` | `THETA_IG_ACTION` | `governance_guard` | theta/IG status must obey no-target-fitting and source-lock rules. |
| `META_PROOF_PROCESS` | `RS_GENERATION` | `governance_guard` | generation count cannot inherit raw-rank or target-division upgrades. |
| `META_PROOF_PROCESS` | `PHI_OBS_TYPEII1` | `governance_guard` | selector claims must reject target data and replacement-passing toys. |
| `META_PROOF_PROCESS` | `QFT_CHSH` | `governance_guard` | controls/ansatz states cannot become GU-derived CHSH evidence. |
| `META_PROOF_PROCESS` | `VZ_ACTUAL_OPERATOR` | `governance_guard` | typed-spine candidates cannot become actual-operator closure by wording. |
| `PHI_OBS_TYPEII1` | `QFT_CHSH` | `observer_shadow_dependency` | QFT/CHSH finite sectors need an observer-facing source-mode map, not only labels. |
| `THETA_IG_ACTION` | `QFT_CHSH` | `future_measurement_action_dependency` | any physical measurement/postulate loop must be source-locked before CHSH promotion. |
| `VZ_ACTUAL_OPERATOR` | `RS_GENERATION` | `operator_provenance_analogy` | both require actual source operator/quotient objects before raw algebra can promote. |

The last two edges are governance/dependency-pressure edges, not mathematical implications.
They prevent inconsistent upgrade posture across adjacent gates.

### Supersession and demotion edges

| superseded or demoted item | by node | edge_type | reason |
|---|---|---|---|
| coarse `THETA-XI` live-ledger blocker | `THETA_IG_ACTION` | `refined_obstruction` | Cycle 2 locates the first source block at `K_IG_selector`. |
| broad RS effective-rank certificate block | `RS_GENERATION` | `refined_obstruction` | Cycle 2 locates the first physical quotient block at `d_RS,-1`. |
| C3/D4 visible-three selector attempt | `PHI_OBS_TYPEII1` | `demotion` | `n=2`, `n=4`, and `n` replacements work; current class is negative control. |
| finite quotient-Gram packet block | `QFT_CHSH` | `refined_obstruction` | Cycle 2 locates the first finite packet block at `P_fin^b` plus local modes. |
| displayed VZ typed-spine inverse as closure | `VZ_ACTUAL_OPERATOR` | `demotion` | actual `D_GU^epsilon` certificate is missing; typed spine is conditional only. |
| process-only DAG sufficiency | `META_PROOF_PROCESS` | `refined_governance` | Cycle 1/2 blockers require a top-gate registry with fault/finality fields. |

## 5. Fault/finality model

Fault classes:

| fault id | invalid message class | affected nodes | guard |
|---|---|---|---|
| `F_TARGET` | target value used upstream | `THETA_IG_ACTION`, `RS_GENERATION`, `PHI_OBS_TYPEII1` | require empty target-input log and replacement-target checks. |
| `F_RAW` | raw/control object promoted to physical proof | `RS_GENERATION`, `QFT_CHSH`, `VZ_ACTUAL_OPERATOR` | raw objects are controls until source quotient/operator data exist. |
| `F_HOST` | host/embedding mistaken for selector | `PHI_OBS_TYPEII1` | selected target rows must be target-free and beat `n=2,4`. |
| `F_CONTROL` | executable control or ansatz used as GU result | `QFT_CHSH` | Bell/Pauli/identity/free-vacuum controls are import/control only. |
| `F_TYPED_SPINE` | typed candidate treated as actual source object | `VZ_ACTUAL_OPERATOR`, `THETA_IG_ACTION` | require source-closed operator/action certificate. |
| `F_STALE` | older wording survives refined blocker | all nodes | update node status, edge, and finality rule together. |
| `F_CONSENSUS` | governance confused with proof | `META_PROOF_PROCESS` | DAG has governance finality only. |

Finality rules:

| node | finality state | what can be cited now | what cannot be cited |
|---|---|---|---|
| `THETA_IG_ACTION` | `not_final` | Branch 3 is a coherent template; source selector missing. | GU predicts dark energy, `Lambda`, `Z_theta`, `C_Rtheta`, or `xi_eff`. |
| `RS_GENERATION` | `not_final` | raw projector algebra and quotient/BRST contract. | rank 4, rank 8, three generations, or four generations derived. |
| `PHI_OBS_TYPEII1` | `conditional_negative_finality` | current instantiated selectors fail as selectors; host remains conditional. | positive finite Connes channel, replacement shadow, SM gauge, or generations selected. |
| `QFT_CHSH` | `control_finality_only` | CHSH fixtures and ansatz states are useful controls. | GU-derived `H_phys`, covariance, `rho_AB`, observables, or CHSH violation. |
| `VZ_ACTUAL_OPERATOR` | `typed_template_finality_only` | typed spine is a coherent conditional route. | actual GU RS operator, FC-VZ-1, FC-VZ-4, or full VZ evasion closed. |
| `META_PROOF_PROCESS` | `governance_finality` | this DAG can block status laundering. | process finality as mathematics or physics evidence. |

Global finality rule:

```text
A top-gate claim is final only when its closure condition is met by an owned future proof,
computation, or source certificate. A governance node may block an upgrade immediately, but
it may not upgrade a mathematical or physical claim.
```

## 6. First exact obstruction or missing proof object

There is no single mathematical proof object shared by all six top gates. The first
obstruction is node-local and must not be compressed into a synthesis slogan.

| node | first exact obstruction | why it is first |
|---|---|---|
| `THETA_IG_ACTION` | `K_IG_selector` | downstream `Q_IG`, `Z_U`, `V_src`, `S_cross_src`, boundary data, current, and FLRW coefficients depend on selected field degrees and operator. |
| `RS_GENERATION` | `d_RS,-1` | without a source-defined gauge/BRST differential, `Pi_RS^phys` is not defined and raw `Pi_raw` cannot become physical. |
| `PHI_OBS_TYPEII1` | `FIXED_DATA_X_CERTIFICATE` | without fixed target-free data, `Phi_obs` cannot compute `T_A`, `T_G`, `T_1`, or `T_3`. |
| `QFT_CHSH` | `SourceProjectorPFinBWithLocalModeRecords` | the repo names `K_b` but not which local source modes occupy it. |
| `VZ_ACTUAL_OPERATOR` | `ActualDGU01OperatorCertificate` | displayed typed-spine blocks are not actual GU operator provenance. |
| `META_PROOF_PROCESS` | top-gate registry maintenance rule | without registry/audit adoption, stale upgrades can bypass refined blockers. |

The first exact cross-gate governance obstruction before this file was the absence of a
machine-readable top-gate registry incorporating the Cycle 1/2 refined blockers. This file
supplies that registry at exploration grade; it does not close the node-local mathematical
obstructions above.

## 7. Impact for next frontier ordering

The next frontier should not open another broad synthesis lane before the first source
objects are attempted. The ordering implied by the DAG is:

1. `VZ_ACTUAL_OPERATOR`: extract `ActualDGU01OperatorCertificate`. VZ has strong typed
   algebra, so actual-operator provenance is the shortest path to a clean upgrade or
   rollback.
2. `RS_GENERATION`: build `RS_PHYSICAL_QUOTIENT_BRST_COMPLEX_BUILDER` around `d_RS,-1`.
   Generation count is load-bearing and cannot move by more raw ranks.
3. `THETA_IG_ACTION`: run `K_IGSourceSelectionTest_V0` before any new cosmology comparison.
   C01 is high value, but target quarantine makes source selector first.
4. `PHI_OBS_TYPEII1`: run a fixed-data candidate inventory and reject visible-three or
   imported finite-CC candidates before spending effort on sector traces.
5. `QFT_CHSH`: request the exact `P_fin^b` local mode packet; until then, further Bell
   fixtures are controls only.
6. `META_PROOF_PROCESS`: maintain this graph whenever any top gate changes, and require
   audits for no-upgrade and forbidden-input checks.

This ordering favors gates where a single source object can decide a live branch. It also
keeps the observer/QFT lanes from consuming target-like data before the source-mode and
`Phi_obs` objects exist.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "HOURLY_CYCLE3_TOP_GATE_CLAIM_DAG_FAULT_LEDGER",
  "version": "2026-06-24",
  "verdict": "COARSE_DAG_EXISTS_BUT_CYCLE3_TOP_GATE_DAG_REMAINS_REQUIRED_GOVERNANCE_ARTIFACT",
  "usable_dag_decision": {
    "repo_has_coarse_live_DAG": true,
    "repo_has_cycle3_top_gate_DAG_after_cycles_1_2_before_this_file": false,
    "this_artifact_supplies_cycle3_top_gate_DAG_v0": true,
    "mathematical_claim_upgrades_made_here": false,
    "governance_status": "required_artifact_now_available_as_exploration_v0"
  },
  "top_gates": [
    "THETA_IG_ACTION",
    "RS_GENERATION",
    "PHI_OBS_TYPEII1",
    "QFT_CHSH",
    "VZ_ACTUAL_OPERATOR",
    "META_PROOF_PROCESS"
  ],
  "nodes": [
    {
      "id": "THETA_IG_ACTION",
      "claim_surface": "theta_IG_action_FLRW_coefficient_route",
      "owner_files": [
        "explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md",
        "explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md",
        "explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md",
        "explorations/gu-minimal-action-spec-2026-06-24.md"
      ],
      "accepted_inputs": [
        "source_locked_action_or_parent_action",
        "source_selected_K_IG_Q_IG_Z_U_V_src_S_cross_src_field_degrees_boundary_data",
        "full_EL_tuple",
        "derived_total_current_theta_eff",
        "FLRW_scalar_mode_survival",
        "same_branch_Z_theta_C_Rtheta_xi_eff",
        "empty_target_input_log"
      ],
      "forbidden_inputs": [
        "DESI_Rubin_windows_upstream",
        "xi_eff_threshold_or_target_used_upstream",
        "bare_Lambda",
        "bare_Rtheta2",
        "K_IG_chosen_by_naturalness_only",
        "Branch_3_template_promoted_without_selector",
        "free_beta_bare_theta_norm_with_nonzero_theta_claim"
      ],
      "dependencies": [
        "K_IG_selector",
        "field_degree_selector",
        "source_forced_S_IG_dyn_or_parent_action",
        "total_current_conservation_proof",
        "SourceForcedThetaFLRWCoefficientPacket"
      ],
      "supersessions_demotions": [
        "Cycle_2_refines_Cycle_1_packet_block_to_K_IG_selector",
        "free_beta_bare_theta_branch_remains_negative_conditional_result"
      ],
      "closure_condition": "source_geometry_selects_complete_IG_dynamics_packet_before_targets_and_locked_action_emits_scalar_mode_Z_theta_positive_C_Rtheta_and_xi_eff_with_replacement_target_checks_passed",
      "current_status": "underdefined",
      "current_proof_grade": "conditional_template",
      "invalid_message_fault_model": [
        "target_fitting",
        "auxiliary_field_collapse",
        "hidden_variation_constraint",
        "missing_total_current_terms",
        "template_laundered_as_source_selection"
      ],
      "finality_rule": "not_final_for_dark_energy_or_xi_eff; cite_Branch_3_template_only",
      "first_missing_object": "K_IG_selector",
      "claim_upgrade_allowed": false
    },
    {
      "id": "RS_GENERATION",
      "claim_surface": "RS_physical_rank_index_and_generation_count",
      "owner_files": [
        "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md",
        "explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md",
        "explorations/generation-count-rs-symbol-index-contract-2026-06-24.md",
        "tests/rs_clifford_projector_model.py"
      ],
      "accepted_inputs": [
        "source_selected_right_H_RS_domain",
        "gamma_trace_maps",
        "source_gauge_BRST_differential",
        "ghost_antighost_or_gauge_fixing_data",
        "symbol_exactness_or_ellipticity",
        "H_linear_trace_or_index_certificate",
        "source_selected_F_ch2",
        "same_operator_K3_Y14_or_APS_bridge"
      ],
      "forbidden_inputs": [
        "ind_H_D_RS_equals_8",
        "ind_H_D_GU_equals_24",
        "three_generations",
        "four_generations",
        "rank_H_E_RS_eff_equals_8_divided_by_2",
        "raw_96_C_promoted_to_physical_H_rank",
        "complex_rank_halving_without_H_trace",
        "BRST_subtraction_without_source_ghost_data"
      ],
      "dependencies": [
        "d_RS,-1",
        "Pi_RS_phys",
        "E_RS_eff",
        "H_linear_trace",
        "source_selected_background",
        "same_operator_bridge"
      ],
      "supersessions_demotions": [
        "Cycle_2_refines_effective_rank_block_to_d_RS_minus_1",
        "raw_projector_rank_remains_raw_only"
      ],
      "closure_condition": "complete_source_derived_quotient_BRST_or_gauge_fixed_elliptic_complex_computes_H_linear_index_or_rank_with_no_target_inputs",
      "current_status": "underdefined",
      "current_proof_grade": "raw_control_plus_contract_only",
      "invalid_message_fault_model": [
        "target_division",
        "raw_algebra_as_analytic_index",
        "missing_quotient",
        "complex_only_trace_conversion",
        "K3_control_as_GU_theorem"
      ],
      "finality_rule": "not_final_for_rank_4_rank_8_three_generations_or_four_generations",
      "first_missing_object": "d_RS,-1",
      "claim_upgrade_allowed": false
    },
    {
      "id": "PHI_OBS_TYPEII1",
      "claim_surface": "Phi_obs_Type_II1_fixed_data_selector_and_finite_control_targets",
      "owner_files": [
        "explorations/hourly-cycle2-fixed-data-phi-obs-sector-ledger-2026-06-24.md",
        "explorations/hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md",
        "explorations/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md",
        "canon/type-ii1-spectral-sm-checklist.md"
      ],
      "accepted_inputs": [
        "fixed_data_X_N_subset_M_tau_A_H_D_J_gamma_Phi_obs",
        "sector_idempotents",
        "Markov_traces",
        "fusion_equivalence",
        "spectral_compatibility",
        "actual_observer_mode_anomaly_shadow",
        "n2_n4_n_replacement_obstructions"
      ],
      "forbidden_inputs": [
        "A_F",
        "finite_CC_tuple",
        "G_SM",
        "central_Z6",
        "K_SM",
        "n_equals_3",
        "C3",
        "index_3",
        "D4_arms",
        "three_projections",
        "dim_H_F_96",
        "ordinary_anomaly_free_SM_shadow",
        "physical_Higgs_data",
        "equal_trace_alone"
      ],
      "dependencies": [
        "FIXED_DATA_X_CERTIFICATE",
        "PHI_OBS_IMAGE_WITHOUT_TARGET_INPUT",
        "N_NEQ_3_REPLACEMENT_OBSTRUCTION",
        "SECTORWISE_SPECTRAL_COMPATIBILITY_PROOF",
        "ACTUAL_OBSERVER_MODE_ANOMALY_SHADOW"
      ],
      "supersessions_demotions": [
        "C3_D4_demoted_to_negative_control",
        "finite_Connes_control_kept_as_observer_certificate_not_substrate_axiom"
      ],
      "closure_condition": "fixed_Type_II1_data_compute_T_A_T_G_T_1_T_3_or_declared_replacement_shadow_without_target_inputs_and_nearest_replacements_fail_by_named_obstruction",
      "current_status": "negative_filter_current_classes",
      "current_proof_grade": "formal_negative_filter_plus_contract_only",
      "invalid_message_fault_model": [
        "host_as_selector",
        "visible_cardinality_transport",
        "external_SM_data_attachment",
        "copywise_anomaly_as_selector"
      ],
      "finality_rule": "conditional_negative_finality_for_current_classes; no_positive_selector_finality",
      "first_missing_object": "FIXED_DATA_X_CERTIFICATE",
      "claim_upgrade_allowed": false
    },
    {
      "id": "QFT_CHSH",
      "claim_surface": "source_mode_quotient_positive_seed_covariance_CHSH",
      "owner_files": [
        "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md",
        "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md",
        "explorations/observer-finality-pati-salam-chsh-fixture-2026-06-24.md",
        "explorations/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md"
      ],
      "accepted_inputs": [
        "P_fin_b",
        "exactly_16_local_gu_derived_mode_records",
        "source_raw_representatives",
        "local_support_or_local_algebra_inclusion",
        "exact_H_raw",
        "EOM_Gauge_Constraint_Ghost_Null_representatives",
        "exact_Q_b",
        "H_phys_equals_Q_star_H_raw_Q",
        "positivity_rank_certificate",
        "later_source_covariance_and_GU_observables"
      ],
      "forbidden_inputs": [
        "identity_Gram_as_GU_derivation",
        "Bell_state",
        "Pauli_controls",
        "free_vacuum",
        "Hadamard_or_Fock_state",
        "target_fitted_covariance_or_CHSH_state",
        "Stinespring_or_CPTP_without_GU_derivation",
        "direct_sum_as_tensor_product",
        "Pati_Salam_labels_as_physical_Gram"
      ],
      "dependencies": [
        "SourceProjectorPFinBWithLocalModeRecords",
        "SourceRawGramRuleAndMatrix",
        "FinitePhysicalQuotientRepresentatives",
        "PositiveFiniteOneParticleSeed",
        "source_covariance_gate",
        "derived_rho_AB",
        "GU_admissible_observables",
        "locality_NAC_data"
      ],
      "supersessions_demotions": [
        "Cycle_2_refines_finite_Gram_block_to_P_fin_b_local_modes",
        "CHSH_fixtures_remain_executable_controls_not_GU_state"
      ],
      "closure_condition": "clean_source_mode_quotient_packet_computes_positive_nonzero_H_phys_then_later_source_covariance_rho_AB_and_admissible_observables_support_CHSH",
      "current_status": "blocked",
      "current_proof_grade": "executable_control",
      "invalid_message_fault_model": [
        "control_as_derived_state",
        "nonlocal_basis_hiding_correlation",
        "imported_identity_pairing",
        "gauge_constraint_leakage",
        "direct_sum_tensor_import"
      ],
      "finality_rule": "control_finality_only; physical_CHSH_and_QFT_recovery_not_final",
      "first_missing_object": "SourceProjectorPFinBWithLocalModeRecords",
      "claim_upgrade_allowed": false
    },
    {
      "id": "VZ_ACTUAL_OPERATOR",
      "claim_surface": "actual_GU_RS_operator_FC_VZ_1_FC_VZ_4",
      "owner_files": [
        "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md",
        "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md",
        "explorations/vz-proof-grade-closure-attempt-2026-06-24.md",
        "canon/no-go-class-relative-map.md"
      ],
      "accepted_inputs": [
        "source_closed_D_GU_epsilon_0_1_certificate",
        "rolled_up_domain_codomain",
        "sigma_1_D_GU_epsilon",
        "coefficients_a_b_lambda_d",
        "separated_Phi_2_Phi_d_F_xi_Phi_F",
        "Q_projectors",
        "all_real_mixed_non_null_covectors",
        "actual_section_pulled_sigma_0_inv_S_Rs_4D_full_with_II_s_H_Z_A_Poisson_K_mu_nu"
      ],
      "forbidden_inputs": [
        "typed_spine_matrix_as_actual_operator",
        "Phi_F_as_source_of_F_xi",
        "hidden_first_order_terms_in_Z_A",
        "pure_covector_only_audit",
        "mixed_trace_and_embedded_conventions",
        "verified_VZ_language_before_FC_VZ_1_and_FC_VZ_4"
      ],
      "dependencies": [
        "ActualDGU01OperatorCertificate",
        "E_actual_all_covector_kernel_audit",
        "actual_R_sector_Schur_symbol",
        "ActualDGUSectionSubprincipalCertificate",
        "coupled_RS_constraint_characteristic_matrix"
      ],
      "supersessions_demotions": [
        "typed_spine_arithmetic_remains_conditional_not_actual_operator_closure",
        "no_go_map_wording_capped_at_conditional_14D_and_4D_principal_symbol"
      ],
      "closure_condition": "actual_operator_certificate_closes_FC_VZ_1_for_every_real_non_null_mixed_covector_and_same_operator_section_pulled_subprincipal_constraint_matrix_has_no_non_null_spacelike_characteristics",
      "current_status": "underdefined",
      "current_proof_grade": "conditional_template",
      "invalid_message_fault_model": [
        "candidate_operator_as_source_closed_operator",
        "order_convention_confusion",
        "same_session_closure_inflation",
        "lower_order_terms_effective_order_one_after_pullback",
        "constraint_subsystem_changes_cone"
      ],
      "finality_rule": "typed_template_finality_only; actual_operator_and_full_VZ_evasion_not_final",
      "first_missing_object": "ActualDGU01OperatorCertificate",
      "claim_upgrade_allowed": false
    },
    {
      "id": "META_PROOF_PROCESS",
      "claim_surface": "proof_grade_process_and_top_gate_governance",
      "owner_files": [
        "RESEARCH-POSTURE.md",
        "process/runbooks/five-lane-frontier-run.md",
        "explorations/persona-review-distributed-systems-2026-06-24.md",
        "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
      ],
      "accepted_inputs": [
        "explicit_assumptions",
        "source_files",
        "machine_readable_gate_registries",
        "independent_proof_or_computation_artifacts",
        "audits_that_check_no_upgrades",
        "correction_logs"
      ],
      "forbidden_inputs": [
        "consensus_as_mathematical_proof",
        "stale_canon_drift",
        "same_session_upgrade_laundering",
        "compatibility_as_derivation",
        "process_discipline_as_physics_evidence"
      ],
      "dependencies": [
        "THETA_IG_ACTION",
        "RS_GENERATION",
        "PHI_OBS_TYPEII1",
        "QFT_CHSH",
        "VZ_ACTUAL_OPERATOR"
      ],
      "supersessions_demotions": [
        "this_file_refines_coarse_live_DAG_for_Cycle_3_top_gate_statuses_only",
        "does_not_replace_repo_wide_ledger"
      ],
      "closure_condition": "every_future_upgrade_or_demotion_updates_node_status_dependency_edge_forbidden_inputs_and_finality_rule_in_one_pass_and_audits_detect_no_stronger_downstream_status_than_dependencies_allow",
      "current_status": "governance_required",
      "current_proof_grade": "governance",
      "invalid_message_fault_model": [
        "stale_graph",
        "missing_edge",
        "vague_node_semantics",
        "bureaucracy_without_decision_effect"
      ],
      "finality_rule": "governance_finality_only; not_math_or_physics_evidence",
      "first_missing_object": "canon_facing_top_gate_maintenance_rule_and_audit_adoption",
      "claim_upgrade_allowed": false
    }
  ],
  "dependency_edges": [
    {
      "from": "META_PROOF_PROCESS",
      "to": "THETA_IG_ACTION",
      "edge_type": "governance_guard"
    },
    {
      "from": "META_PROOF_PROCESS",
      "to": "RS_GENERATION",
      "edge_type": "governance_guard"
    },
    {
      "from": "META_PROOF_PROCESS",
      "to": "PHI_OBS_TYPEII1",
      "edge_type": "governance_guard"
    },
    {
      "from": "META_PROOF_PROCESS",
      "to": "QFT_CHSH",
      "edge_type": "governance_guard"
    },
    {
      "from": "META_PROOF_PROCESS",
      "to": "VZ_ACTUAL_OPERATOR",
      "edge_type": "governance_guard"
    },
    {
      "from": "PHI_OBS_TYPEII1",
      "to": "QFT_CHSH",
      "edge_type": "observer_shadow_dependency"
    },
    {
      "from": "THETA_IG_ACTION",
      "to": "QFT_CHSH",
      "edge_type": "future_measurement_action_dependency"
    },
    {
      "from": "VZ_ACTUAL_OPERATOR",
      "to": "RS_GENERATION",
      "edge_type": "operator_provenance_analogy"
    }
  ],
  "supersession_edges": [
    {
      "superseded": "coarse_THETA_XI_live_ledger_blocker",
      "by": "THETA_IG_ACTION",
      "edge_type": "refined_obstruction",
      "reason": "Cycle_2_places_first_source_block_at_K_IG_selector"
    },
    {
      "superseded": "broad_RS_effective_rank_certificate_block",
      "by": "RS_GENERATION",
      "edge_type": "refined_obstruction",
      "reason": "Cycle_2_places_first_physical_quotient_block_at_d_RS_minus_1"
    },
    {
      "superseded": "C3_D4_visible_three_selector_attempt",
      "by": "PHI_OBS_TYPEII1",
      "edge_type": "demotion",
      "reason": "n2_n4_and_n_replacements_work_current_class_is_negative_control"
    },
    {
      "superseded": "finite_quotient_Gram_packet_block",
      "by": "QFT_CHSH",
      "edge_type": "refined_obstruction",
      "reason": "Cycle_2_places_first_finite_packet_block_at_P_fin_b_plus_local_modes"
    },
    {
      "superseded": "displayed_VZ_typed_spine_inverse_as_closure",
      "by": "VZ_ACTUAL_OPERATOR",
      "edge_type": "demotion",
      "reason": "ActualDGU01OperatorCertificate_missing_typed_spine_conditional_only"
    },
    {
      "superseded": "process_only_DAG_sufficiency",
      "by": "META_PROOF_PROCESS",
      "edge_type": "refined_governance",
      "reason": "Cycle_1_2_blockers_require_top_gate_registry_with_fault_finality_fields"
    }
  ],
  "fault_classes": {
    "F_TARGET": {
      "affected_nodes": [
        "THETA_IG_ACTION",
        "RS_GENERATION",
        "PHI_OBS_TYPEII1"
      ],
      "guard": "empty_target_input_log_and_replacement_tests"
    },
    "F_RAW": {
      "affected_nodes": [
        "RS_GENERATION",
        "QFT_CHSH",
        "VZ_ACTUAL_OPERATOR"
      ],
      "guard": "raw_objects_are_controls_until_source_data_exist"
    },
    "F_HOST": {
      "affected_nodes": [
        "PHI_OBS_TYPEII1"
      ],
      "guard": "target_free_selected_rows_and_n2_n4_obstructions"
    },
    "F_CONTROL": {
      "affected_nodes": [
        "QFT_CHSH"
      ],
      "guard": "controls_are_import_control_only"
    },
    "F_TYPED_SPINE": {
      "affected_nodes": [
        "VZ_ACTUAL_OPERATOR",
        "THETA_IG_ACTION"
      ],
      "guard": "require_source_closed_operator_or_action_certificate"
    },
    "F_STALE": {
      "affected_nodes": [
        "THETA_IG_ACTION",
        "RS_GENERATION",
        "PHI_OBS_TYPEII1",
        "QFT_CHSH",
        "VZ_ACTUAL_OPERATOR",
        "META_PROOF_PROCESS"
      ],
      "guard": "update_node_status_edge_and_finality_together"
    },
    "F_CONSENSUS": {
      "affected_nodes": [
        "META_PROOF_PROCESS"
      ],
      "guard": "governance_finality_only"
    }
  },
  "global_finality_rule": "A_top_gate_claim_is_final_only_when_its_closure_condition_is_met_by_future_proof_computation_or_source_certificate; governance_may_block_but_not_upgrade_claims",
  "no_claim_upgrades": {
    "all_nodes_claim_upgrade_allowed": false,
    "forbidden_positive_claims": [
      "GU_derives_dark_energy",
      "GU_derives_Lambda",
      "rank_4_promoted",
      "rank_8_promoted",
      "three_generations_derived",
      "Phi_obs_positive_selector_constructed",
      "Type_II1_selects_SM_or_three_generations",
      "H_phys_computed_from_current_sources",
      "rho_AB_GU_derived",
      "CHSH_violation_GU_derived",
      "Actual_GU_RS_operator_identified",
      "FC_VZ_1_closed",
      "FC_VZ_4_closed",
      "full_VZ_evasion_closed"
    ]
  },
  "first_exact_obstructions": {
    "THETA_IG_ACTION": "K_IG_selector",
    "RS_GENERATION": "d_RS,-1",
    "PHI_OBS_TYPEII1": "FIXED_DATA_X_CERTIFICATE",
    "QFT_CHSH": "SourceProjectorPFinBWithLocalModeRecords",
    "VZ_ACTUAL_OPERATOR": "ActualDGU01OperatorCertificate",
    "META_PROOF_PROCESS": "canon_facing_top_gate_maintenance_rule_and_audit_adoption"
  },
  "next_frontier_ordering": [
    "VZ_ACTUAL_OPERATOR",
    "RS_GENERATION",
    "THETA_IG_ACTION",
    "PHI_OBS_TYPEII1",
    "QFT_CHSH",
    "META_PROOF_PROCESS"
  ]
}
```
