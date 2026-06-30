---
title: "Marble/Wood Source-Geometry Reframing Contract"
date: "2026-06-24"
status: exploration/interface_contract
doc_type: marble_wood_source_geometry_reframing_contract
verdict: "conditional"
owned_path: "explorations/cycle-gates-and-audits/marble-wood-source-geometry-reframing-2026-06-24.md"
audit_script: "tests/marble_wood_reframing_audit.py"
depends_on:
  - "lab/process/runbooks/five-lane-frontier-run.md"
  - "explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
  - "explorations/firewall-and-two-geometries/quantum-gravity-reframing-no-go-map-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
  - "CANON.md"
  - "RESEARCH-STATUS.md"
  - "NEXT-STEPS.md"
---

# Marble/Wood Source-Geometry Reframing Contract

## 1. Verdict

**Verdict: conditional.**

The marble/wood framing is accepted as a decision-grade reframing contract, not as a
physics proof:

```text
MARBLE_WOOD_REFRAME:
  conditional / contract-open
  sharpens the next burden
  does not close GR-SHADOW, QFT-SHADOW, MATTER-SHADOW, MEASUREMENT, or ANOMALY
```

Answer to the key question:

```text
Yes, this framing changes the next proof burden.
```

It changes the burden away from either of these weaker assignments:

```text
fix the wood by appending better matter terms;
quantize the marble by making the 4D metric the primary quantum field.
```

The sharper GU burden is:

```text
derive the observer-facing marble and the observer-facing wood
as two shadows of the same source geometry,
with a shared source object, shared branch, shared provenance ledger,
and separate recovery checks for both shadows.
```

This is a steelman because it keeps open the heterodox possibility that the familiar
geometric marble is itself premature. The 4D metric may be a downstream observer-facing
object rather than the primitive object. But that possibility has a cost: GU must derive
both sides of the observer equation from the deeper source, rather than treating one side
as fundamental and the other as phenomenological input.

Late nuance accepted:

```text
G_mu_nu is the principled marble candidate.
T_mu_nu is the wood candidate.
Lambda g_mu_nu is a geometric-side patch, not automatically marble.
```

That matters because a bare `Lambda` can look geometric while still being a fitted
constant. In this contract it gets its own burden: any cosmological-constant or
dark-energy replacement must be source-derived, dynamic or branch-fixed with provenance,
and tested against target-fitting. It may not be smuggled in as "marble" merely because it
sits on the left side of Einstein's equation.

Allowed:

- Cite the marble/wood asymmetry as a reason to require a same-source source-to-shadow
  theorem.
- Treat metric quantization as a possible downstream shadow, not the primary definition
  of GU.
- Treat matter/QFT/SM data as owed observer shadows, not as optional decoration.
- Ask whether the metric marble and matter wood are both projections of `G_src`.
- Treat `Lambda g_mu_nu` as a separate patch/dark-energy slot that needs source
  provenance before it can be promoted.

Forbidden:

- Treat the reframing as quantum-gravity recovery.
- Treat "not quantizing the 4D metric" as a QFT or measurement certificate.
- Treat the existing metric shadow, Pati-Salam branch, Higgs slot, K3 arithmetic, Bell
  controls, or weak-field Schwarzschild result as the dual-shadow theorem.
- Move unexplained source residuals to matter and call that derived wood.
- Keep the metric marble primitive while claiming source geometry has explained both
  sides.
- Treat a bare `Lambda`, fitted `xi_eff`, or dark-energy target window as derived merely
  because it helps the cosmological equation.

Currently open:

```text
same-source dual-shadow theorem: not supplied
GR/marble shadow: specified_open, true certificate not supplied
Lambda/dark-energy patch: open, no source-derived replacement certificate supplied
QFT/wood shadow: schema_defined_blocked before state-space and state extraction
SM/matter finite control: partial/open, no source-geometry selector yet
measurement: controls only, no GU-derived state and admissible observables yet
anomaly shadow: relative/open until the observer-facing mode list is derived
```

What would count as progress:

```text
one branch-fixed G_src
  -> R_marble certificate
  -> R_wood certificate
  -> shared conservation/provenance identity
  -> rollback conditions for both shadows
```

## 2. Plain-English Translation

### Marble

In Einstein's complaint, the marble is the elegant geometric side: the metric geometry and
curvature language that make GR look mathematically unified. More precisely, the
principled marble candidate is the Einstein-curvature structure `G_mu_nu[g]`, not every
term that happens to sit on the left-hand side. In repo-local GU terms, marble means the
observer-facing metric/geometric shadow:

```text
R_marble(G_src, branch, s)
  -> (X, g = s^* g_Y, projected 4D metric equations, GR limits)
```

The marble is not automatically fundamental. The allowed heterodox hypothesis is:

```text
the 4D metric geometry may be a shadow of source geometry,
not the source object itself.
```

That hypothesis is open, not proved. It becomes meaningful only when the repo has a true
`GR-SHADOW` certificate: a branch-fixed `S_GU`, full EL tuple, section projection,
conservation theorem, exact Schwarzschild/Kerr witnesses, and macroscopic/weak-field
limits from the same branch.

### Lambda Patch

`Lambda g_mu_nu` is a special case. It sits on the geometric side of the usual equation,
but this contract does not count a bare cosmological constant as principled marble. It is
a geometric-looking patch until the source branch supplies its provenance.

Repo-local name:

```text
R_Lambda(G_src, branch, s)
  -> Lambda_eff or dynamic dark-energy/source term
```

Current status:

```text
open / patch-slot / not derived
```

Allowed use:

- keep `Lambda_eff`, theta cosmology, `xi_eff`, DESI/Rubin-style target windows, and
  dark-energy phenomenology as controls or targets;
- ask whether source geometry generates a dynamic contribution that replaces a bare
  constant;
- require the same anti-smuggling discipline used for matter terms.

Forbidden use:

- call a bare `Lambda` source-derived because it is written beside `G_mu_nu`;
- fit `xi_eff` or a dark-energy equation of state to data and cite that as GU derivation;
- move uncancelled source residuals into `Lambda_eff` after the target metric is known.

The first proof object for this slot is:

```text
LambdaPatchProvenanceCertificate(branch)
```

It must show whether the cosmological term is zero, imported, phenomenological, or
generated from the branch-fixed source action/operator with coefficients fixed before the
cosmology target is tested.

### Wood

The wood is the less elegant matter/stress-energy side: fields, matter, gauge data,
equations of state, phenomenological sources, and observer-facing QFT structure. In
repo-local GU terms, wood is not just `T_mu_nu` as a symbol. It includes:

```text
R_wood(G_src, branch, s, O)
  -> QFT state space or local algebra
  -> positive states or density matrices
  -> admissible observables and probabilities
  -> matter/gauge/Higgs finite-control shadow
  -> anomaly-safe observer-facing mode list
  -> measurement/readout channel
  -> T_mu_nu^shadow when an observer metric equation is claimed
```

The wood cannot be repaired by inserting a better phenomenological right-hand side. A
source-geometry program must show how the observer-facing matter/QFT/stress shadow is
extracted from the same branch that produces the metric shadow.

### Source-Geometry Shadow

A source-geometry shadow is an observer-facing object obtained by an explicit reduction
map from a deeper source object:

```text
G_src =
  (Y, g_Y, P, S, A, D_GU, S_GU,
   IG_data, section_space, boundary_data,
   observer_access, provenance_rules)

R_dual =
  (R_marble, R_Lambda, R_wood, R_measurement, R_record)
```

The word "shadow" is not a license for vagueness. A shadow claim needs:

```text
domain,
codomain,
map or functor,
normalization,
loss ledger,
provenance tags,
recovery checks,
rollback condition.
```

The important same-source condition is:

```text
R_marble and R_wood must consume the same branch-fixed G_src.
```

If the metric is derived from one branch and the matter/QFT packet is imported from
another source, the marble/wood asymmetry has not been resolved. It has only been
relabeled.

## 3. What Changes Relative To Prior Contracts

The prior source-geometry contract already says:

```text
GU should not be framed first as quantized 4D GR.
GU should be framed first as source geometry plus observer reductions.
```

The quantum-gravity reframing no-go map already says:

```text
not quantizing the metric is a valid primary-framing exit,
but QFT recovery and exact GR recovery are still owed.
```

This marble/wood contract sharpens those statements in five ways.

| change | decision consequence |
|---|---|
| The proof target becomes dual, not single-shadow. | A GR shadow alone is insufficient, and a QFT/matter shadow alone is insufficient. The next promoted claim needs both sides from one source branch or an explicit narrower scope. |
| "Fix the wood" is demoted as a primary route. | Adding stress-energy terms, finite Connes data, SM targets, Higgs potentials, or state ansatzes can be controls only unless source provenance is supplied. |
| "Quantize the marble" is demoted as the primary GU route. | Metric quantization may appear downstream as an effective shadow, but it cannot be the defining GU move without changing branches. |
| The metric marble itself is put under audit. | The 4D metric is allowed to be observer-facing output, not primitive input. Therefore exact GR recovery must be proved as a shadow rather than assumed as the elegant side. |
| `Lambda g_mu_nu` is split away from principled marble. | A cosmological-constant or dark-energy term must be zero, imported, phenomenological, or source-derived by certificate; it cannot ride along as automatic geometry. |

This reframing changes the next proof burden to:

```text
DualShadowDerivationPacketV0:
  same G_src
  same branch
  R_marble
  R_wood
  shared provenance and conservation identity
  no target insertion
```

It also changes citation discipline:

```text
"source geometry instead of quantized GR"
```

is too weak by itself. The stronger contract language is:

```text
"source geometry must derive both the metric/geometric and matter/QFT observer shadows."
```

## 4. What Does Not Change

The marble/wood reframing does not reduce the physics bill. It makes the bill harder to
hide.

| obligation | unchanged repo-local status |
|---|---|
| GR / marble recovery | `GR-SHADOW` is specified/open. A true certificate is not supplied. Exact Schwarzschild/Kerr remain unpassed in the full source EL tuple. |
| Exact-solution tests | Weak-field Schwarzschild remains bounded. Schwarzschild and Kerr require branch-fixed witness fields and full `E_s,E_A,E_IG,E_Psi` closure. |
| QFT / wood recovery | `QFT-SHADOW` is schema-defined but blocked before state-space and state extraction. States, observables, probabilities, locality, unitarity/positivity, spin-statistics, and anomalies remain owed. |
| SM finite control | Source geometry derives a Pati-Salam representation branch and hosts Higgs quantum-number slots, but no full SM gauge quotient, finite algebra, Higgs dynamics, anomaly-safe observer shadow, or generation count is derived. |
| Measurement | Bell/CHSH and observer-finality fixtures remain controls until GU derives `rho_AB`, admissible observables, and a measurement/readout channel. |
| Anomaly | Ordinary SM anomaly cancellation is only relative to an exact ordinary SM shadow. Full GU anomaly safety requires every observer-facing mode to be listed and checked. |
| Provenance governance | `derive`, `select`, `host`, `import`, `ansatz`, and `control` remain separate. Compatibility is not recovery. Hosting is not selection. |

In particular, the contract does not allow any of the following moves:

```text
weak-field marble -> exact marble
Pati-Salam labels -> full wood
Bell controls -> measurement derivation
K3 compact control -> physical generation count
ambient Higgs slot -> physical Higgs scalar
source-geometry slogan -> QFT recovery
```

## 5. Claim Certificate Table

| claim | current status | allowed citation language | forbidden shortcuts | rollback conditions |
|---|---|---|---|---|
| `MW-FRAMING` | `conditional_contract` | "Einstein's marble/wood asymmetry sharpens GU's proof burden: both metric geometry and matter/QFT structure must be recovered as observer-facing shadows from the same source geometry." | `reframe_as_physics_proof`; `compatibility_as_recovery`; `source_geometry_by_name_only` | Roll back to `interface_metaphor_only` if no same-source reduction target can be specified. |
| `MARBLE-PREMATURITY-HYPOTHESIS` | `heterodox_open` | "GU may investigate whether the 4D metric marble is downstream rather than primitive." | `metric_shadow_assumed_fundamental`; `metric_quantization_as_primary_start`; `weak_field_as_exact_GR` | Roll back if the only working branch imports a fundamental 4D Einstein-Hilbert sector as the physical metric theory. |
| `MARBLE-GR-SHADOW` | `specified_open` | "GR as a marble shadow is specified but not certified; exact GR recovery remains open." | `weak_field_as_exact_GR`; `hidden_matter_relabeling`; `branch_engineered_cross_terms`; `kerr_by_spherical_analogy` | Roll back any marble-shadow promotion if Schwarzschild or Kerr fails the full branch-fixed source EL tuple, or if the pass requires target-fitted residual terms. |
| `LAMBDA-PATCH-DARK-ENERGY` | `open_patch_slot` | "`Lambda g_mu_nu` is a geometric-side patch slot; GU may seek a source-derived dynamic replacement, but no such certificate is currently supplied." | `bare_Lambda_as_marble`; `dark_energy_fit_as_derivation`; `Lambda_residual_absorber`; `fitted_xi_eff_as_source` | Roll back to phenomenological control/import if `Lambda_eff`, `xi_eff`, or a dark-energy term is inserted, fitted after data, or not generated from branch-fixed `S_GU/D_GU`. |
| `WOOD-QFT-MATTER-SHADOW` | `blocked_open` | "Matter/QFT wood recovery is owed as a shadow certificate; current data provide controls, representation branches, and hosts, not a full observer-facing QFT/matter derivation." | `qft_recovery_by_slogan`; `representation_labels_as_quantum_state`; `host_as_selector`; `phenomenological_term_without_source`; `ordinary_sm_anomaly_as_full_shadow` | Roll back if no positive state space, normalized source-derived state, admissible observables, anomaly-safe mode list, or target-free matter/gauge selector is supplied. |
| `SAME-SOURCE-DUAL-SHADOW` | `required_next_burden` | "The next proof object should derive both marble and wood from one branch-fixed `G_src`, or explicitly demote the claim scope." | `separate_branch_splicing`; `wood_imported_after_marble`; `marble_assumed_after_wood`; `loss_ledger_omitted` | Roll back to separate GR/QFT open certificates if `R_marble` and `R_wood` do not share the same source object, branch, normalizations, and provenance ledger. |
| `MEASUREMENT-RECORD-SHADOW` | `controls_only` | "Observer-finality and CHSH fixtures are useful audit surfaces; physical measurement remains open." | `ansatz_state_as_measurement`; `observer_finality_as_physics_escape`; `pauli_controls_as_gu_measurements` | Roll back if the only violation or probability assignment comes from copied control states, imported observables, or a measurement postulate not derived from GU data. |

### Progress Criteria

| progress object | minimum content | decision it could change |
|---|---|---|
| `SourceBranchClosureCertificate` | one fixed `I_GU` branch with `D_GU`, `S_GU`, variation space, source law, boundary/domain data, and observer access | could move `MW-FRAMING` from contract-open to proof-target-ready |
| `R_marble` witness | `g=s^*g_Y`, full source EL projection, conservation theorem, exact Schwarzschild first, Kerr second, weak/macroscopic limit | could promote or fail `MARBLE-GR-SHADOW` for that branch |
| `R_wood` witness | physical field complex or local algebra, positive state, admissible observables, matter/gauge selector, anomaly audit, `T_mu_nu^shadow` if a metric equation is claimed | could promote or fail `WOOD-QFT-MATTER-SHADOW` for that branch |
| shared provenance ledger | every datum tagged derive/select/host/import/ansatz/control, with no target values upstream | could test whether the dual-shadow claim is same-source or spliced |
| rollback matrix | binary failure conditions for marble, wood, measurement, anomaly, and exact solutions | could make the claim falsifiable rather than rhetorical |

### Forbidden Shortcuts

```text
reframe_as_physics_proof
metric_quantization_as_primary_start
source_geometry_by_name_only
compatibility_as_recovery
weak_field_as_exact_GR
hidden_matter_relabeling
branch_engineered_cross_terms
qft_recovery_by_slogan
representation_labels_as_quantum_state
host_as_selector
phenomenological_term_without_source
ordinary_sm_anomaly_as_full_shadow
ansatz_state_as_measurement
observer_finality_as_physics_escape
separate_branch_splicing
wood_imported_after_marble
marble_assumed_after_wood
loss_ledger_omitted
```

### Rollback Rule

```text
If either shadow fails, demote the dual claim to the strongest separately certified layer.
```

Examples:

```text
same source object, no R_marble        -> source-object proposal plus wood controls only
R_marble only, no R_wood               -> classical/metric shadow attempt only
R_wood only, metric imported           -> matter/QFT shadow attempt only
Pati-Salam branch, no QFT state        -> representation branch, not wood recovery
weak-field metric only                 -> bounded marble compatibility, not exact recovery
Bell state copied into finite fixture  -> measurement control, not GU measurement
```

## 6. Machine-Readable Contract Block

```json
{
  "artifact": "MARBLE_WOOD_SOURCE_GEOMETRY_REFRAMING_CONTRACT",
  "version": "2026-06-24",
  "verdict": "conditional",
  "decision": "REFRAME_SHARPENS_NEXT_PROOF_BURDEN_NOT_PROOF_OF_RECOVERY",
  "question_answer": "yes_the_framing_sharpens_the_burden_to_same_source_dual_shadow_derivation",
  "source_geometry_claim_grade": "contract_open_not_final",
  "terms": {
    "marble": {
      "plain_english": "observer-facing metric geometry and principled GR-like curvature structure, especially G_mu_nu rather than every left-side term",
      "repo_object": "R_marble(G_src, branch, s) -> (X, g=s^*g_Y, projected_4D_metric_shadow, GR_limits)",
      "current_status": "specified_open_not_certified"
    },
    "lambda_patch": {
      "plain_english": "Lambda g_mu_nu is a geometric-side patch or dark-energy slot until source provenance is supplied",
      "repo_object": "R_Lambda(G_src, branch, s) -> Lambda_eff_or_dynamic_dark_energy_source_term",
      "current_status": "open_not_source_derived",
      "required_certificate": "LambdaPatchProvenanceCertificate"
    },
    "wood": {
      "plain_english": "observer-facing matter, stress-energy, QFT, gauge, measurement, and anomaly data",
      "repo_object": "R_wood(G_src, branch, s, O) -> (QFT_state_space_or_local_algebra, states, observables, matter_gauge_higgs_shadow, anomaly_shadow, T_shadow)",
      "current_status": "blocked_open_partial_controls_and_hosts_only"
    },
    "source_geometry_shadow": {
      "plain_english": "an observer-facing output of an explicit source-to-shadow reduction map",
      "same_source_requirement": "R_marble_and_R_wood_consume_the_same_branch_fixed_G_src"
    }
  },
  "changed_relative_to_prior_contracts": [
    "fix_wood_or_quantize_marble_replaced_by_same_source_derivation",
    "not_quantized_gr_reframe_strengthened_to_dual_shadow_burden",
    "metric_marble_audited_as_possible_shadow_not_primitive",
    "lambda_patch_separated_from_principled_marble",
    "matter_wood_cannot_be_phenomenological_rhs_input",
    "next_proof_object_must_bind_R_marble_and_R_wood_to_one_branch"
  ],
  "unchanged_obligations": [
    "GR_shadow_recovery",
    "QFT_shadow_recovery",
    "SM_finite_control",
    "cosmology_theta_xi_dark_energy_provenance",
    "measurement_state_and_observables",
    "anomaly_shadow",
    "exact_solution_tests",
    "provenance_and_rollback"
  ],
  "claim_certificates": [
    {
      "id": "MW-FRAMING",
      "status": "conditional_contract",
      "proof_grade": "interface_contract",
      "allowed_citation": "Einstein marble/wood asymmetry sharpens GU's proof burden: both metric geometry and matter/QFT structure must be recovered as observer-facing shadows from the same source geometry.",
      "forbidden_shortcuts": [
        "reframe_as_physics_proof",
        "compatibility_as_recovery",
        "source_geometry_by_name_only"
      ],
      "rollback_conditions": [
        "no_same_source_reduction_target_can_be_specified"
      ]
    },
    {
      "id": "MARBLE-PREMATURITY-HYPOTHESIS",
      "status": "heterodox_open",
      "proof_grade": "research_hypothesis",
      "allowed_citation": "GU may investigate whether the 4D metric marble is downstream rather than primitive.",
      "forbidden_shortcuts": [
        "metric_shadow_assumed_fundamental",
        "metric_quantization_as_primary_start",
        "weak_field_as_exact_GR"
      ],
      "rollback_conditions": [
        "only_working_branch_imports_fundamental_4D_metric_sector"
      ]
    },
    {
      "id": "MARBLE-GR-SHADOW",
      "status": "specified_open",
      "proof_grade": "missing_recovery_certificate",
      "allowed_citation": "GR as a marble shadow is specified but not certified; exact GR recovery remains open.",
      "forbidden_shortcuts": [
        "weak_field_as_exact_GR",
        "hidden_matter_relabeling",
        "branch_engineered_cross_terms",
        "kerr_by_spherical_analogy"
      ],
      "rollback_conditions": [
        "Schwarzschild_or_Kerr_fails_full_source_EL_tuple",
        "target_fitted_residual_terms_required"
      ]
    },
    {
      "id": "LAMBDA-PATCH-DARK-ENERGY",
      "status": "open_patch_slot",
      "proof_grade": "missing_source_provenance_certificate",
      "allowed_citation": "Lambda g_mu_nu is a geometric-side patch slot; GU may seek a source-derived dynamic replacement, but no such certificate is currently supplied.",
      "forbidden_shortcuts": [
        "bare_Lambda_as_marble",
        "dark_energy_fit_as_derivation",
        "Lambda_residual_absorber",
        "fitted_xi_eff_as_source"
      ],
      "rollback_conditions": [
        "Lambda_eff_inserted_as_constant",
        "xi_eff_fitted_after_target_data",
        "dark_energy_term_not_generated_from_branch_fixed_S_GU_or_D_GU"
      ]
    },
    {
      "id": "WOOD-QFT-MATTER-SHADOW",
      "status": "blocked_open",
      "proof_grade": "missing_qft_and_selector_certificates",
      "allowed_citation": "Matter/QFT wood recovery is owed as a source-geometry shadow; current data provide controls, representation branches, and hosts.",
      "forbidden_shortcuts": [
        "qft_recovery_by_slogan",
        "representation_labels_as_quantum_state",
        "host_as_selector",
        "phenomenological_term_without_source",
        "ordinary_sm_anomaly_as_full_shadow"
      ],
      "rollback_conditions": [
        "no_positive_state_space",
        "no_normalized_source_derived_state",
        "no_admissible_observables",
        "no_target_free_matter_gauge_selector",
        "uncanceled_observer_facing_anomaly"
      ]
    },
    {
      "id": "SAME-SOURCE-DUAL-SHADOW",
      "status": "required_next_burden",
      "proof_grade": "not_started",
      "allowed_citation": "The next proof object should derive both marble and wood from one branch-fixed G_src, or explicitly demote the claim scope.",
      "forbidden_shortcuts": [
        "separate_branch_splicing",
        "wood_imported_after_marble",
        "marble_assumed_after_wood",
        "loss_ledger_omitted"
      ],
      "rollback_conditions": [
        "R_marble_and_R_wood_use_different_source_objects",
        "R_marble_and_R_wood_use_different_branch_normalizations",
        "shared_provenance_ledger_missing"
      ]
    },
    {
      "id": "MEASUREMENT-RECORD-SHADOW",
      "status": "controls_only",
      "proof_grade": "executable_control_not_physics_derivation",
      "allowed_citation": "Observer-finality and CHSH fixtures are useful audit surfaces; physical measurement remains open.",
      "forbidden_shortcuts": [
        "ansatz_state_as_measurement",
        "observer_finality_as_physics_escape",
        "pauli_controls_as_gu_measurements"
      ],
      "rollback_conditions": [
        "violation_only_from_control_or_ansatz_state",
        "observables_imported_without_GU_measurement_channel"
      ]
    }
  ],
  "forbidden_shortcuts": [
    "reframe_as_physics_proof",
    "metric_quantization_as_primary_start",
    "source_geometry_by_name_only",
    "compatibility_as_recovery",
    "weak_field_as_exact_GR",
    "bare_Lambda_as_marble",
    "dark_energy_fit_as_derivation",
    "Lambda_residual_absorber",
    "fitted_xi_eff_as_source",
    "hidden_matter_relabeling",
    "branch_engineered_cross_terms",
    "qft_recovery_by_slogan",
    "representation_labels_as_quantum_state",
    "host_as_selector",
    "phenomenological_term_without_source",
    "ordinary_sm_anomaly_as_full_shadow",
    "ansatz_state_as_measurement",
    "observer_finality_as_physics_escape",
    "separate_branch_splicing",
    "wood_imported_after_marble",
    "marble_assumed_after_wood",
    "loss_ledger_omitted"
  ],
  "currently_open": [
    "same_source_dual_shadow_theorem",
    "ELProjectedGRShadowTheorem",
    "LambdaPatchProvenanceCertificate",
    "QFTStateSpaceExtractionCertificate",
    "QFTStateExtractionCertificate",
    "ObservableAdmissibilityCertificate",
    "Phi_SG_MG_source_geometry_finite_control_selector",
    "AnomalyShadowCertificate",
    "GU_measurement_channel"
  ],
  "progress_criteria": [
    "one_branch_fixed_G_src",
    "R_marble_full_EL_projection_and_exact_solution_witnesses",
    "Lambda_eff_zero_imported_or_source_derived_with_anti_fitting_test",
    "R_wood_positive_state_observables_matter_selector_and_anomaly_audit",
    "shared_source_conservation_or_provenance_identity",
    "derive_select_host_import_ansatz_control_ledger",
    "binary_rollback_matrix"
  ],
  "next_step": {
    "id": "DualShadowDerivationPacketV0",
    "first_branch_preference": "Branch_2A_if_Phi_is_source_derived_otherwise_Branch_3_total_current",
    "must_emit": [
      "SourceBranchClosureCertificate",
      "R_marble_certificate",
      "R_Lambda_patch_certificate",
      "R_wood_certificate",
      "shared_provenance_ledger",
      "same_source_loss_ledger",
      "rollback_matrix"
    ],
    "first_binary_questions": [
      "does_one_G_src_produce_a_computable_metric_shadow",
      "is_Lambda_eff_zero_imported_or_source_derived_without_target_fitting",
      "does_the_same_G_src_produce_a_positive_QFT_matter_shadow",
      "is_T_shadow_derived_from_R_wood_rather_than_inserted"
    ]
  }
}
```

## 7. Next Meaningful Proof/Computation Step

Build one `DualShadowDerivationPacketV0`, not another broad synthesis.

Minimum packet:

```text
input:
  one branch-fixed G_src
  written D_GU and S_GU or an explicit source-closure failure
  variation space
  section map
  boundary/domain data
  observer-access rule

output:
  R_marble certificate
  R_wood certificate
  shared provenance ledger
  shared loss ledger
  rollback matrix
```

Recommended sequence:

1. Fix the branch. Try Branch 2A only if `Phi(epsilon,beta,s)=0` is source-derived and
   `D_A Phi=0` is proved. Otherwise switch explicitly to Branch 3 and use
   total-current language.
2. For the marble side, attempt `ELProjectedGRShadowTheorem(branch)` for exact
   Schwarzschild before Kerr. Emit every residual rather than moving it into matter.
3. For the wood side, attempt the smallest QFT/matter extraction from the same branch:
   a physical field complex or local algebra, positive state, admissible observables,
   matter/gauge selector status, anomaly mode list, and `T_mu_nu^shadow` if a metric
   equation is claimed.
4. Compare the two outputs through a shared provenance ledger:

   ```text
   every object tagged derive / select / host / import / ansatz / control
   ```

5. Decide the dual claim:

   ```text
   both shadows derived from same source       -> promote branch-local dual-shadow claim
   marble derived, wood missing                -> metric shadow attempt only
   wood derived, marble missing                -> matter/QFT shadow attempt only
   both missing but branch typed               -> source-object proposal
   target input found upstream                 -> demote to control/import
   ```

The first useful computation is therefore not "solve the wood" or "quantize the marble."
It is:

```text
same branch, two reductions, one provenance ledger.
```

## Sources Read

- `lab/process/runbooks/five-lane-frontier-run.md`
- `explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
- `explorations/firewall-and-two-geometries/quantum-gravity-reframing-no-go-map-2026-06-24.md`
- `explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md`
- `explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md`
- `CANON.md`
- `RESEARCH-STATUS.md`
- `NEXT-STEPS.md`
