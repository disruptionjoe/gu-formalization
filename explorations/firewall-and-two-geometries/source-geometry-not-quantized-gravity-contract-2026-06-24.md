---
title: "Source Geometry, Not Quantized Gravity Contract"
date: "2026-06-24"
status: exploration/interface_contract
doc_type: source_geometry_reduction_contract
verdict: "SOURCE_GEOMETRY_REFRAME_ACCEPTED_AS_CONTRACT_NOT_PROOF"
owned_path: "explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
audit_script: "tests/source_geometry_contract_audit.py"
depends_on:
  - "explorations/persona-and-dialectic/all-persona-wall-break-steelman-hegelian-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
  - "README.md"
  - "docs/OVERVIEW.md"
  - "CANON.md"
  - "RESEARCH-STATUS.md"
  - "NEXT-STEPS.md"
  - "explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/dark-energy-cosmology/flrw-theta-xi-branch-reduction-2026-06-24.md"
  - "explorations/generation-sector/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"
  - "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md"
---

# Source Geometry, Not Quantized Gravity Contract

## 1. Verdict

The steelman is accepted as a research contract:

```text
GU should not be framed first as "quantize the 4D GR metric."
GU should be framed first as a source-geometry and reduction program.
```

That reframing is useful because it puts the primary mathematical burden in the right place:
define the deeper source object, then derive observer-facing shadows. The shadows must recover
or falsify:

```text
GR, QFT, matter/SM finite control, measurement records, and known physics.
```

The reframing is not a proof and not a permission slip. It does not excuse exact GR recovery,
QFT consistency, Standard Model data, anomaly checks, measurement-state derivation, or
falsifiable predictions. It only changes the order of explanation:

```text
source geometry first;
metric quantization, if present, second as an observer-shadow or effective quantization.
```

Current decision:

```text
No future GU claim may be promoted merely because it is "not quantized GR."
Any positive claim must carry a source-to-shadow reduction certificate.
```

## 2. Steelman Problem Statement In Plain English And Formal Terms

Plain English:

GU is most defensible if its basic object is not a quantum operator-valued 4D metric. The
basic object should be a higher/source geometry whose reductions make 4D observers see a
metric, fields, matter multiplets, quantum states, and measurement records. The problem is
therefore not:

```text
start with g_mu_nu and quantize it.
```

The problem is:

```text
write the source object and prove that its allowed observer reductions recover the known
metric, quantum, matter, and measurement shadows without target insertion.
```

Formal contract:

```text
G_src =
  (Y, g_Y, P, S, A, D_src, S_src,
   IG_data, section_space, boundary_data,
   observer_access, provenance_rules)

R_GU =
  (R_GR, R_QFT, R_SM, R_MEAS, R_RECORD)
```

where:

```text
R_GR(G_src, s)       -> (X, g = s^* g_Y, 4D EL equations, GR limits)
R_QFT(G_src, s)      -> (local algebras or Hilbert space, state, dynamics, EFT/QFT checks)
R_SM(G_src, s)       -> (finite-control matter/gauge/Higgs/anomaly shadow)
R_MEAS(G_src, O)     -> (rho_AB or state family, admissible observables, probabilities)
R_RECORD(G_src, O)   -> (bounded observer records and claim/proof finality)
```

The source object may contain a 14D metric bundle, `Sp(64)` carrier data, quaternionic spinors,
IG variables, typed operators, actions, boundary data, and section maps. But the name
"source geometry" is not enough. A claim counts only when the relevant source object and
reduction map are explicit enough to audit.

This turns "quantum gravity" into a downstream certificate:

```text
quantum gravity certificate =
  show how the source geometry produces the quantum/EFT shadow seen by 4D observers,
  including gravitons or metric fluctuations if those are part of the effective theory.
```

## 3. What Changes Compared With Conventional Quantum-Gravity Framing

The starting variable changes.

Conventional framing often begins with a classical 4D metric and asks for a quantization:

```text
g_mu_nu on X^4  ->  quantized metric / graviton / path integral over metrics.
```

The source-geometry framing begins with a richer object:

```text
G_src on or over Y^14  ->  observer reductions  ->  g_mu_nu, QFT, matter, records.
```

The proof object changes. A positive GU claim must no longer say only that a shadow is
compatible with known physics. It must exhibit:

```text
source object + reduction map + provenance trace + recovery checks.
```

The role of no-go theorems changes, but only class-relatively. A no-go theorem may apply
to a shadow category rather than the source category, but GU must then prove the exact
forgetful/reduction operation and the invariant it preserves or forgets. "Different category"
is not a result by itself.

The role of metric quantization changes. It becomes one possible effective shadow:

```text
metric quantization is allowed as R_QFT or R_GR-linearized output,
not as the primary definition of GU.
```

The role of phenomenology changes. A phenomenological target such as negative `xi_eff`,
three generations, or CHSH violation can guide a search, but cannot be used as an input.
The target value must appear at the end of the reduction, not inside the source object or
selector.

The role of compact controls changes. K3, finite Connes controls, Bell fixtures, and
Pati-Salam ansatz states remain valuable controls. They are not physical GU evidence until
the source-to-control transport map is proved.

## 4. What Does Not Change: Obligations GU Still Owes

The source-geometry framing does not weaken the physics bill. It itemizes it.

GR obligations remain:

- derive the 4D metric shadow `g = s^* g_Y`;
- write the full vacuum Euler-Lagrange tuple, including section, connection, IG, spinor,
  boundary, and cross terms;
- recover exact Schwarzschild and Kerr, not only weak-field bookkeeping;
- explain cosmological reductions with canonical normalization, including `Z_theta`,
  `C_Rtheta`, and `xi_eff` if theta dark energy is claimed.

QFT obligations remain:

- provide a quantum or operator-algebraic shadow with states, observables, locality,
  positivity/unitarity, spin-statistics, anomaly control, and EFT limits;
- show how metric fluctuations or gravitons appear if the observer-facing theory contains
  them;
- prove that lower-order or hidden source terms do not create acausal, nonunitary, or
  anomalous shadow dynamics.

Matter/SM obligations remain:

- recover the finite-control package, not merely host it;
- separate `derive`, `select`, `host`, `import`, `compatible`, and `ansatz`;
- derive or honestly import `A_F`, `G_SM`, the central quotient, hypercharge, Higgs
  scalar, anomaly shadow, and generation count;
- reject any selector that passes equally well for `n != 3` when claiming three generations.

Measurement obligations remain:

- derive the relevant finite state, such as `rho_AB`, from source zero modes, a two-point
  function, vacuum data, or an explicit reduction channel;
- derive admissible local observables and their commutation/locality rules;
- keep Bell/CHSH controls as controls until GU supplies the state and measurement postulate.

Governance obligations remain:

- every live claim keeps dependencies, forbidden inputs, proof grade, finality status,
  citation language, and rollback condition;
- clean falsification or demotion is a successful outcome;
- downstream claims inherit the weakest load-bearing certificate, not the strongest prose
  nearby.

## 5. Required Reduction Certificate Stack

Every future source-geometry claim must carry the following certificate stack. A missing
layer blocks promotion.

| layer | certificate question | required content | common failure |
|---|---|---|---|
| Source object | What is the deeper object? | typed fields, symmetries, variation space, action/operator, boundary/domain data, branch key | source geometry by name only |
| Reduction map | How does the observer shadow arise? | domain, codomain, map/functor/projection, loss ledger, normalization, covariance | analogy or forgetful prose without a map |
| Provenance | Where did each datum enter? | derive/select/host/import/ansatz/control tags, dependency DAG, forbidden target inputs | target value inserted upstream |
| Known-physics recovery | Which standard checks are passed? | GR, black holes, FLRW, SM matter, anomaly, low-energy limits, experimental bounds as applicable | compatibility treated as recovery |
| Quantum/QFT recovery | What is the quantum shadow? | state space or local algebras, states, observables, locality, positivity/unitarity, EFT/renormalization status | QFT recovery by slogan |
| Falsification/rollback | What demotes the claim? | binary failure conditions, rollback target, citation downgrade, downstream dependency updates | no way to lose |

The stack is cumulative. A strong source object with no QFT shadow is not a QFT claim. A
strong compact control with no reduction map is not physical source-geometry evidence. A
working phenomenological fit with no provenance is not a derivation.

Minimum machine-checkable fields for a claim certificate:

```text
claim_id
source_object
reduction_map
provenance_trace
known_physics_recovery
quantum_qft_recovery
forbidden_shortcuts
rollback_condition
allowed_citation
```

## 6. Claim Certificate Table

| claim class | current allowed statement | source object required | reduction required | proof/recovery certificate | forbidden shortcut | rollback condition |
|---|---|---|---|---|---|---|
| Source-geometry claim | GU may be framed as a source-geometry/reduction program. | `G_src` with typed fields, action/operator, IG variation, boundary data, and source symmetries. | At least one explicit `R_GU` component with domain/codomain. | Interface contract plus source-to-shadow map, not only ontology. | "source geometry" named without equations or maps. | If no stable `G_src` can supply any reduction, demote to metaphor/interface-only. |
| GR shadow claim | GR recovery is open except bounded weak-field results and conditional branches. | Source action/operator plus section map and variation space. | `R_GR: G_src -> (X,g,E_g)` with full EL tuple. | Exact Schwarzschild/Kerr and FLRW coefficient checks. | weak field as exact GR; hidden matter relabeling; free beta with nonzero theta. | Any exact black-hole failure in the full tuple demotes GR recovery for that branch. |
| QFT shadow claim | QFT recovery is required and currently not supplied as a full source-to-QFT certificate. | Source operator/action with quantizable degrees, symplectic/inner-product data, and gauge constraints. | `R_QFT` to local algebras, Hilbert space, path integral, or EFT data. | locality, positivity/unitarity, anomalies, spin-statistics, renormalization/EFT and causal propagation. | qft_recovery_by_slogan; assuming metric quantization is enough. | Nonunitarity, anomaly, acausality, or missing state/observable map demotes the QFT claim. |
| SM/matter claim | GU derives useful Pati-Salam representation data and hosts Higgs quantum numbers; full SM finite control is not derived. | Source carrier, selector/shadow functor, finite-control target-free input data. | `R_SM` selecting or reducing to finite algebra, gauge group, matter, Higgs, anomalies. | no imported `A_F`, `G_SM`, `n=3`, hypercharge, or Higgs potential unless tagged as import. | host as selector; compact or finite control as physical derivation. | Replacement test for `n != 3`, imported finite CC data, or extra anomalous modes demote the claim. |
| Measurement claim | CHSH and observer-finality controls are useful; GU-derived physical forcing is open. | Source zero modes/two-point function/vacuum and observer split. | `R_MEAS` to density matrix or state family and admissible observables. | trace-one positive state, local commutativity, physical measurement postulate, computed probabilities. | ansatz state as measurement; observer-finality as physics escape. | If derived states are separable or all admissible settings have `CHSH <= 2`, demote the physical-forcing claim. |

## 7. Forbidden Shortcuts And Rollback Conditions

Forbidden shortcut vocabulary:

| shortcut | forbidden move | rollback |
|---|---|---|
| `metric_quantization_as_primary_start` | treating "quantize the GR metric" as the definition of GU | reclassify as an ordinary quantum-gravity branch, not source geometry |
| `source_geometry_by_name_only` | naming a deeper geometry without typed source fields and maps | demote to metaphor/interface placeholder |
| `phenomenological_term_without_source` | inserting `xi`, `Lambda`, masses, potentials, or cross terms because a target needs them | demote to phenomenological control |
| `ansatz_state_as_measurement` | copying Bell, product, thermal, or generic vacuum states into the GU slot | demote to ansatz/control |
| `compact_control_as_physical_index` | using K3 or other compact arithmetic as noncompact GU index evidence without a bridge | demote to compact control only |
| `host_as_selector` | treating ambient containment or Type II_1 embedding as SM selection | demote to host/import |
| `compatibility_as_recovery` | saying no contradiction equals derivation | demote to compatibility only |
| `observer_finality_as_physics_escape` | using record/finality language to bypass state, action, or no-go obligations | demote to governance/formal layer |
| `weak_field_as_exact_GR` | promoting `O(M/r)` compatibility to exact Schwarzschild/Kerr recovery | demote to weak-field scope |
| `free_beta_nonzero_theta` | varying beta freely while claiming nonzero theta from only `|theta|^2` | reject branch for nonzero theta |
| `qft_recovery_by_slogan` | asserting QFT emergence without states, observables, locality, positivity, and anomalies | block QFT shadow claim |

Rollback rule:

```text
If any certificate layer fails, demote the claim to the highest layer actually certified.
```

Examples:

```text
source object only                         -> source-object proposal
source object + GR map, no QFT             -> classical shadow only
compact index arithmetic, no bridge        -> compact control only
Pati-Salam labels, no selector             -> representation host/relative branch
Bell state, no GU state channel            -> ansatz/control
phenomenological xi, no source coefficient -> target mechanism, not GU derivation
```

## 8. Branch Robustness

| branch | role | allowed use | cannot claim | robustness decision |
|---|---|---|---|---|
| source geometry primary | intended steelman branch | primary program if `G_src` and `R_GU` are explicit | proof of GU before reductions close | `PRIMARY_PROGRAM_OPEN` |
| metric quantization | downstream or comparison branch | effective QFT/linearized metric shadow after `R_QFT` or `R_GR` supplies it | primary GU definition or automatic recovery | `SECONDARY_SHADOW_ONLY` |
| phenomenological insertion | target-search branch | controls, parameter scans, target windows such as `xi_eff < -0.319` | derivation or source coefficient | `CONTROL_OR_TARGET_ONLY` |
| ansatz-only | fixture branch | executable controls, candidate states, sanity checks | physical forcing, measurement derivation, observer evidence | `CONTROL_ONLY` |
| compact-control-only | finite/compact arithmetic branch | K3, finite Connes, compact characteristic-class or Bell-control comparison | noncompact physical index or SM/measurement derivation | `CONTROL_ONLY_NOT_PHYSICAL` |

This robustness table deliberately preserves useful work. It does not discard metric
quantization, phenomenological scans, ansatz states, or compact controls. It prevents them
from occupying the wrong proof slot.

The strongest branch is source geometry primary, but it is also the most expensive branch:
it owes all reductions. A weaker branch can be valuable as a control only if its citation
language remains weaker.

## 9. Next Meaningful Proof/Computation Step

The next useful step is a source-to-shadow proof packet, not a new slogan.

Minimal packet:

```text
SOURCE_OBJECT_V0 =
  G_src instantiated from the primary GU interface:
  fields, variations, gauge group, D_src, S_src, IG branch, section map,
  boundary/domain data, and observer access.

REDUCTION_PACKET_V0 =
  R_GR and R_QFT written for the same branch.
```

The packet should answer two binary questions first:

```text
1. Does the same source object produce a computable full GR EL tuple?
2. Does the same source object produce a QFT shadow with states and admissible observables?
```

Concrete sequence:

1. Choose one IG/action branch, preferably Branch 2A only if a natural
   `Phi(epsilon,beta,s)=0` with `D_A Phi=0` is actually derived; otherwise choose Branch 3
   and use total-current language.
2. Lock the operator provenance: prove whether the primary `D_src` contains the first-order
   `Phi_2(d_A psi)` block needed by the VZ typed-spine result.
3. Run `R_GR` on exact Schwarzschild before Kerr, using the full EL tuple.
4. Run `R_QFT` on the same branch: identify the state space or local algebra, positive
   states, admissible observables, locality/causality, and anomaly obligations.
5. Only after those two reductions are explicit should the project attempt SM finite
   selection, Y14/K3 physical index promotion, or CHSH physical forcing from that branch.

If the packet cannot be written without importing target physics, the honest result is not
failure. It is a branch demotion:

```text
source_geometry_primary -> interface-only or control-only for the affected claim.
```

## Machine-Readable Contract

```json
{
  "artifact": "SOURCE_GEOMETRY_NOT_QUANTIZED_GRAVITY_CONTRACT",
  "version": "2026-06-24",
  "verdict": "SOURCE_GEOMETRY_REFRAME_ACCEPTED_AS_CONTRACT_NOT_PROOF",
  "current_decision": "REQUIRE_SOURCE_TO_SHADOW_CERTIFICATES_BEFORE_PROMOTION",
  "required_stack_order": [
    "source_object",
    "reduction_map",
    "provenance",
    "known_physics_recovery",
    "quantum_qft_recovery",
    "falsification_rollback"
  ],
  "certificate_stack": {
    "source_object": {
      "required_fields": [
        "typed_fields",
        "symmetries",
        "variation_space",
        "action_or_operator",
        "boundary_domain_data",
        "branch_key"
      ],
      "failure": "source_geometry_by_name_only"
    },
    "reduction_map": {
      "required_fields": [
        "domain",
        "codomain",
        "map_or_functor",
        "normalization",
        "loss_ledger",
        "covariance"
      ],
      "failure": "compatibility_as_recovery"
    },
    "provenance": {
      "required_fields": [
        "derive_select_host_import_ansatz_control_tags",
        "dependency_dag",
        "forbidden_target_inputs",
        "citation_language"
      ],
      "failure": "phenomenological_term_without_source"
    },
    "known_physics_recovery": {
      "required_fields": [
        "gr_recovery",
        "black_hole_or_cosmology_gate",
        "sm_matter_gate",
        "anomaly_gate",
        "low_energy_limits"
      ],
      "failure": "weak_field_as_exact_GR"
    },
    "quantum_qft_recovery": {
      "required_fields": [
        "state_space_or_local_algebra",
        "positive_states",
        "admissible_observables",
        "locality_causality",
        "unitarity_or_reflection_positivity",
        "eft_or_renormalization_status"
      ],
      "failure": "qft_recovery_by_slogan"
    },
    "falsification_rollback": {
      "required_fields": [
        "binary_failure_conditions",
        "rollback_target",
        "downstream_dependency_update",
        "allowed_citation_after_failure"
      ],
      "failure": "no_way_to_lose"
    }
  },
  "claim_keys": [
    "SOURCE_GEOMETRY",
    "GR_SHADOW",
    "QFT_SHADOW",
    "SM_MATTER",
    "MEASUREMENT"
  ],
  "claims": [
    {
      "id": "SOURCE_GEOMETRY",
      "status": "contract_open",
      "proof_grade": "interface_contract",
      "finality": "not_final",
      "required_certificates": [
        "source_object",
        "reduction_map",
        "provenance",
        "known_physics_recovery",
        "quantum_qft_recovery",
        "falsification_rollback"
      ],
      "allowed_current_citation": "GU is being framed as a source-geometry/reduction program, not as a proof of physics.",
      "forbidden_shortcuts": [
        "source_geometry_by_name_only",
        "compatibility_as_recovery"
      ],
      "rollback_condition": "no_stable_source_object_or_reduction_map_can_be_written"
    },
    {
      "id": "GR_SHADOW",
      "status": "open",
      "proof_grade": "specification",
      "finality": "not_final",
      "required_certificates": [
        "source_object",
        "reduction_map",
        "provenance",
        "known_physics_recovery",
        "quantum_qft_recovery",
        "falsification_rollback"
      ],
      "allowed_current_citation": "Exact GR recovery remains open; weak-field and branch-local controls keep their bounded scope.",
      "forbidden_shortcuts": [
        "weak_field_as_exact_GR",
        "free_beta_nonzero_theta",
        "phenomenological_term_without_source"
      ],
      "rollback_condition": "full_EL_tuple_fails_Schwarzschild_or_Kerr"
    },
    {
      "id": "QFT_SHADOW",
      "status": "open",
      "proof_grade": "missing_reduction_certificate",
      "finality": "not_final",
      "required_certificates": [
        "source_object",
        "reduction_map",
        "provenance",
        "known_physics_recovery",
        "quantum_qft_recovery",
        "falsification_rollback"
      ],
      "allowed_current_citation": "QFT recovery is an owed shadow certificate, not currently closed.",
      "forbidden_shortcuts": [
        "metric_quantization_as_primary_start",
        "qft_recovery_by_slogan"
      ],
      "rollback_condition": "nonunitarity_anomaly_acausality_or_missing_state_observable_map"
    },
    {
      "id": "SM_MATTER",
      "status": "partial_host_selector_open",
      "proof_grade": "reconstruction_negative_filter",
      "finality": "not_final",
      "required_certificates": [
        "source_object",
        "reduction_map",
        "provenance",
        "known_physics_recovery",
        "quantum_qft_recovery",
        "falsification_rollback"
      ],
      "allowed_current_citation": "GU derives useful Pati-Salam representation data and hosts Higgs quantum numbers; full SM finite control is not derived.",
      "forbidden_shortcuts": [
        "host_as_selector",
        "compact_control_as_physical_index",
        "phenomenological_term_without_source"
      ],
      "rollback_condition": "selector_imports_target_data_or_replacement_test_passes_for_n_not_3"
    },
    {
      "id": "MEASUREMENT",
      "status": "controls_only",
      "proof_grade": "executable_control",
      "finality": "not_final",
      "required_certificates": [
        "source_object",
        "reduction_map",
        "provenance",
        "known_physics_recovery",
        "quantum_qft_recovery",
        "falsification_rollback"
      ],
      "allowed_current_citation": "Observer-finality and CHSH controls are useful, but GU-derived measurement forcing is open.",
      "forbidden_shortcuts": [
        "ansatz_state_as_measurement",
        "observer_finality_as_physics_escape",
        "compatibility_as_recovery"
      ],
      "rollback_condition": "derived_state_separable_or_all_admissible_measurements_CHSH_le_2"
    }
  ],
  "forbidden_shortcut_vocabulary": [
    "metric_quantization_as_primary_start",
    "source_geometry_by_name_only",
    "phenomenological_term_without_source",
    "ansatz_state_as_measurement",
    "compact_control_as_physical_index",
    "host_as_selector",
    "compatibility_as_recovery",
    "observer_finality_as_physics_escape",
    "weak_field_as_exact_GR",
    "free_beta_nonzero_theta",
    "qft_recovery_by_slogan"
  ],
  "changed_obligations": [
    "primary_input_is_source_geometry_not_metric_quantization",
    "metric_quantization_is_downstream_shadow",
    "proof_object_is_source_to_shadow_reduction",
    "compact_controls_require_transport_certificate",
    "phenomenology_is_target_not_input"
  ],
  "unchanged_obligations": [
    "exact_GR_recovery",
    "QFT_recovery",
    "SM_finite_control",
    "anomaly_control",
    "measurement_state_and_observables",
    "falsification_and_rollback"
  ],
  "branch_robustness": [
    {
      "id": "source_geometry_primary",
      "decision": "PRIMARY_PROGRAM_OPEN",
      "allowed_use": "primary branch only with explicit G_src and R_GU certificates",
      "forbidden_claim": "proof_of_GU_before_reductions_close"
    },
    {
      "id": "metric_quantization",
      "decision": "SECONDARY_SHADOW_ONLY",
      "allowed_use": "effective QFT or linearized metric shadow after reduction",
      "forbidden_claim": "primary_definition_of_GU"
    },
    {
      "id": "phenomenological_insertion",
      "decision": "CONTROL_OR_TARGET_ONLY",
      "allowed_use": "target window or parameter scan",
      "forbidden_claim": "source_derived_coefficient"
    },
    {
      "id": "ansatz_only",
      "decision": "CONTROL_ONLY",
      "allowed_use": "executable fixture or candidate sanity check",
      "forbidden_claim": "physical_forcing_or_measurement_derivation"
    },
    {
      "id": "compact_control_only",
      "decision": "CONTROL_ONLY_NOT_PHYSICAL",
      "allowed_use": "compact arithmetic or finite-control comparison",
      "forbidden_claim": "noncompact_physical_index_or_SM_derivation_without_bridge"
    }
  ],
  "rollback_conditions": [
    "no_stable_source_object_or_reduction_map_can_be_written",
    "full_EL_tuple_fails_Schwarzschild_or_Kerr",
    "nonunitarity_anomaly_acausality_or_missing_state_observable_map",
    "selector_imports_target_data_or_replacement_test_passes_for_n_not_3",
    "derived_state_separable_or_all_admissible_measurements_CHSH_le_2"
  ],
  "next_step": "source_object_v0_plus_gr_qft_reduction_packet"
}
```

## Sources Read

- `explorations/persona-and-dialectic/all-persona-wall-break-steelman-hegelian-2026-06-24.md`
- `explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`
- `README.md`
- `docs/OVERVIEW.md`
- `CANON.md`
- `RESEARCH-STATUS.md`
- `NEXT-STEPS.md`
- `explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/dark-energy-cosmology/flrw-theta-xi-branch-reduction-2026-06-24.md`
- `explorations/generation-sector/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md`
- `explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md`
