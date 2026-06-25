---
title: "QFT Shadow Extraction Certificate"
date: "2026-06-24"
status: exploration/certificate
doc_type: qft_shadow_extraction_certificate
verdict: "QFT_SHADOW_SCHEMA_DEFINED; CURRENT_REPO_BLOCKED_BEFORE_STATE_SPACE_AND_STATE_EXTRACTION"
owned_path: "explorations/qft-shadow-extraction-certificate-2026-06-24.md"
companion_audit:
  - "tests/qft_shadow_extraction_certificate_audit.py"
depends_on:
  - "explorations/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/gu-measurement-channel-chsh-gate-2026-06-24.md"
  - "explorations/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md"
  - "explorations/observer-finality-physical-forcing-gate-2026-06-24.md"
  - "explorations/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/finite-control-provenance-audit-2026-06-24.md"
  - "tests/h3_pati_salam_gu_measurement_gate.py"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# QFT Shadow Extraction Certificate

## 1. Verdict

`QFT-SHADOW` is not closed in the current repo.

The repo has enough typed geometry and control machinery to define the certificate that
would be needed:

```text
source GU geometry
  -> Hilbert/Fock or algebraic state space
  -> states or density matrices
  -> admissible observables
  -> Born probabilities
  -> locality/causality and unitary dynamics
  -> spin-statistics and anomaly compatibility
```

But the repo does not yet supply the proof objects that make this chain real. In
particular, it does not derive a QFT state space from the primary GU source data, does not
derive a vacuum/two-point/density state, does not derive GU-admissible measurement
observables, and does not prove the full observer-facing anomaly and spin-statistics
shadow.

The correct current decision is:

```text
certificate schema: defined
current QFT shadow extraction: blocked/specification-open
first hard blocker: QFTStateSpaceExtractionCertificate
second hard blocker: QFTStateExtractionCertificate
OBS-CHSH dependency: still parked because rho_AB and admissible observables are absent
VZ contribution: conditional causal principal-symbol support only
ANOMALY contribution: relative ordinary SM shadow only; full GU shadow open
```

This is different from quantizing the GR metric. The proposed GU route does not have to
start by promoting the 4D metric `g_mu_nu` to a quantum operator or summing over metrics.
It may instead treat the source geometry, operator, section map, and reduction functor as
primary, then recover quantum theory as an observer-facing shadow. However, avoiding
metric quantization does not avoid quantum mechanics or QFT. Empirical physics is stated
in terms of states, observables, amplitudes/probabilities, local commutation, unitary
time evolution, spin-statistics, and anomaly cancellation. A GU theory that cannot
recover those objects has not recovered the observed quantum world.

## 2. Certificate Schema

The certificate is a typed extraction chain. Each stage must name its input, output,
proof obligation, and failure mode.

| stage | certificate field | required output | closure condition | current status |
|---|---|---|---|---|
| 1 | `SourceGeometryCertificate` | fixed GU branch: `I_GU`, `D_GU`, `S_GU`, section/vacuum/boundary data, gauge constraints | source data are branch-closed and variation space is fixed | partial: interface typed, primary action/operator still open |
| 2 | `PhysicalFieldComplexCertificate` | gauge-fixed physical field complex or local field algebra generators | constraints, ghosts/gauge quotients, and domains are explicit | missing for full QFT shadow |
| 3 | `QFTStateSpaceExtractionCertificate` | Hilbert space, Fock space, or net of local `*`-algebras `A(O)` with representation data | positive inner product or algebraic positivity; CCR/CAR/domain rules; no unremoved negative-norm sector | missing |
| 4 | `QFTStateExtractionCertificate` | vacuum/local algebra state `omega`, density matrix `rho`, two-point function, covariance, or finite reduction `rho_AB` | state is positive, normalized, source-derived, and not a copied control/ansatz | missing |
| 5 | `ObservableAdmissibilityCertificate` | self-adjoint operators, PVM/POVM effects, or local algebra elements with finite reductions | observable rule is GU-derived, local, and has physical readout meaning | missing |
| 6 | `BornProbabilityCertificate` | `p(E)=omega(E)` or `p_i=Tr(rho E_i)` with normalization and positivity | probabilities are derived from stage 4 and 5, not assigned by hand | missing |
| 7 | `LocalityCausalityCertificate` | microcausality/NAC, causal propagation cone, no superluminal characteristics | local algebras commute at spacelike separation and dynamics respects the physical cone | conditional only through VZ/formal controls |
| 8 | `UnitarityCertificate` | unitary time evolution, `*`-automorphism group, or unitary S-matrix on physical states | Hamiltonian/generator is self-adjoint or algebraic dynamics is norm/state preserving | missing |
| 9 | `SpinStatisticsCertificate` | spin-statistics assignment for observer-facing modes | spin representation, positivity, locality, and CAR/CCR statistics are jointly proved | missing |
| 10 | `AnomalyShadowCertificate` | anomaly cancellation or anomaly inflow/cobordism compatibility for every observer-facing mode | no extra surviving anomalous modes; ordinary SM cancellation cannot be assumed before the shadow is fixed | open/relative |

Two output formats are allowed:

1. **Hilbert/Fock route.** GU data produce a one-particle Hilbert space, CCR/CAR
   algebra, Fock representation, vacuum or thermal/quasifree state, observables, and
   probabilities.
2. **Algebraic QFT route.** GU data produce a net `O -> A(O)`, a positive state `omega`,
   GNS representation `(H_omega, pi_omega, Omega_omega)`, local observables, and
   probabilities.

The algebraic route is acceptable and may be better for curved/source-geometry settings.
But it still owes states, observables, probabilities, locality, spin-statistics, anomaly
compatibility, and unitarity or state-preserving dynamics.

## 3. What Current Repo Supplies

The current repo supplies useful ingredients, but they stop before a QFT shadow is
extracted.

| repo object | supplied evidence | QFT-shadow use | limitation |
|---|---|---|---|
| `I_GU` interface contract | typed carrier fields, section map, action/operator slots, reduction components | names the source geometry inputs for stage 1 | primary action/operator and branch source law remain underdefined |
| typed operator spine `D_lambda` | first-order `Phi_d = Phi_2 o d_A` block with `lambda_d != 0` in the proposal | can feed physical field complex and causal principal-symbol checks | conditional on the typed spine being the actual primary `D_GU` |
| VZ 14D Schur gate | determinant-free non-null kernel proof for typed-spine principal symbol | conditional support for causal propagation, not a quantum state | no Hilbert/Fock/algebraic state, no Born rule, no unitarity proof |
| observer/formal layer | signed-readout and H3/CHSH controls | executable falsification surface for finite measurement claims | formal/protocol only until GU supplies state and observables |
| Pati-Salam CHSH fixture | finite proxy, Bell/product controls, ansatz rejection gate | excellent downstream test once `rho_AB` exists | current violating states are controls or ansatz, not GU outputs |
| Pati-Salam representation branch | `(4,2,1)+(4bar,1,2)` and relative SM charge packet | candidate finite labels for observer-facing fermion modes | labels are not a Hilbert state, density matrix, or measurement rule |
| SM/Higgs finite-control ledger | Pati-Salam packet derived/hosted; Higgs quantum-number slots hosted; ordinary SM anomaly cancellation relative to exact SM shadow | anomaly and finite-control checklist for stage 10 | no target-free selector for `A_F`, `G_SM/Z_6`, physical Higgs, or full anomaly shadow |
| live claim DAG | current status discipline and forbidden-input model | prevents overpromotion of controls/hosts/ansatz states | governance only; not evidence for QFT recovery |

Therefore the repo currently supports this statement and no stronger one:

```text
GU has a typed source-interface proposal, conditional causal-symbol evidence, finite
observer controls, and relative SM/anomaly host data. It has not yet extracted the
observer-facing QFT state space, states, observables, probabilities, or full anomaly-safe
local quantum theory.
```

## 4. Missing Proof Objects

### State Extraction

The first missing proof object is `QFTStateSpaceExtractionCertificate`.

Minimum contents:

```text
source_branch:
  operator, action branch, section, gauge constraints, boundary/vacuum data
field_complex_or_algebra:
  physical fields after gauge quotient, domains, adjoints, grading, CAR/CCR choice
state_space:
  Hilbert/Fock space or algebraic net and GNS representation
positivity:
  positive finite inner product or positive algebraic state
finite_reduction:
  map to finite observer spaces when a finite experiment is claimed
```

The second missing proof object is `QFTStateExtractionCertificate`.

Minimum contents:

```text
source_kind:
  zero_mode_projector, ker(D_GU) basis, two_point_function, covariance,
  vacuum_local_algebra_state, modular_state, thermal_state, or scattering state
source_provenance:
  gu-derived:<operator/section/vacuum/reference>
output_state:
  omega or rho, and for CHSH rho_AB
checks:
  positivity, normalization, Hermiticity where finite, trace one where density-matrix,
  not equal to a forbidden control or ansatz by construction
```

Representation branching alone cannot fill either certificate. It fixes labels and
dimensions. It does not determine amplitudes, phases, Schmidt spectrum, correlations,
vacuum choice, or density matrices.

### Observable Admissibility

The missing `ObservableAdmissibilityCertificate` must specify:

```text
observable_rule:
  how source geometry or local algebra selects physical readouts
operators:
  self-adjoint local operators, projectors, effects, or finite +/-1 observables
provenance:
  gu-admissible:<measurement-postulate-reference>
checks:
  spectrum/effects valid, locality valid, same-party noncommutation physically justified,
  no future-setting dependence, no postselection hidden in the extraction
```

The current CHSH Pauli settings are controls. They are not yet GU-admissible physical
measurements.

### Spin-Statistics And Anomalies

The missing `SpinStatisticsCertificate` must prove that observer-facing modes have the
correct exchange statistics from the recovered local quantum theory, not merely from a
spin-label convention. It needs the spin representation, positivity, locality, and
CAR/CCR choice in the same branch.

The missing `AnomalyShadowCertificate` must prove one of:

```text
exact ordinary SM observer shadow, with no extra modes;
or complete cancellation/inflow/cobordism compatibility for every extra surviving mode.
```

The repo only has relative ordinary SM anomaly cancellation after the Pati-Salam-to-SM
shadow is already chosen. That is a valid check on a computed ordinary shadow. It is not
a proof that GU has produced exactly that shadow.

### Unitarity And Locality

The missing `UnitarityCertificate` must show state-preserving dynamics:

```text
Hilbert route:
  self-adjoint Hamiltonian/generator, unitary evolution, unitary S-matrix if scattering
algebraic route:
  *-automorphism dynamics preserving the positive state class
gauge route:
  physical inner product after constraints/ghosts has no negative-norm survivors
```

The missing `LocalityCausalityCertificate` must connect the VZ/formal locality controls
to the actual QFT shadow:

```text
microcausality:
  [A(O1), B(O2)] = 0 for spacelike separated regions, with graded version for fermions
causal propagation:
  physical wavefront/characteristic cone agrees with the GU observer cone
NAC/CHSH:
  Alice/Bob local commutativity holds for the live state and live observables
```

The typed VZ gate is relevant here, but it is not enough. VZ controls a principal-symbol
causality obstruction for a conditional operator. It does not produce a positive state,
probabilities, spin-statistics, anomaly cancellation, or unitary dynamics.

## 5. Relation To VZ And CHSH Gates

`VZ-14D` is a causal-symbol gate, not a QFT recovery theorem. Its contribution to this
certificate is narrow and valuable:

```text
If the primary operator really contains the typed-spine Phi_d block with lambda_d != 0,
then the 14D non-null spin-3/2 Schur symbol has no kernel in the checked sector.
```

That helps the future `LocalityCausalityCertificate`. It does not close state-space
extraction, observables, Born probabilities, spin-statistics, anomalies, or unitarity.
If the primary operator later lacks `Phi_d` or has `lambda_d = 0`, this causal support is
rolled back.

`OBS-CHSH` is a finite measurement gate. It asks for exactly the kind of downstream QFT
shadow this certificate requires:

```text
GU source data -> finite Alice/Bob spaces -> rho_AB -> admissible +/-1 observables
-> CHSH value
```

The current fixture is behaving correctly. It accepts controls as controls, rejects
ansatz states as GU evidence, and parks the live gate because `rho_AB` and
`gu-admissible` observables are missing. A closed QFT shadow certificate would supply
those missing inputs. It might produce a violation, or it might produce a negative result.
Both are scientifically meaningful.

## 6. Claim Certificate Table

| claim | current certificate | supplied evidence | missing proof object | forbidden promotion | rollback condition |
|---|---|---|---|---|---|
| `QFT-SHADOW` | `schema_defined_blocked` | typed GU interface, conditional operator spine, finite controls, relative SM/anomaly host data | `QFTStateSpaceExtractionCertificate`, `QFTStateExtractionCertificate`, `ObservableAdmissibilityCertificate`, `BornProbabilityCertificate`, `UnitarityCertificate`, `SpinStatisticsCertificate`, `AnomalyShadowCertificate` | saying "not quantum gravity" means no quantum recovery is needed; treating representation labels as quantum states; importing a Hilbert space/state by notation | no positive state space, no normalized state, no admissible observables, nonunitary dynamics, or anomalous observer modes |
| `OBS-CHSH` | `executable_controls_pending` | Pati-Salam finite proxy, Bell/product controls, ansatz-state audits, provenance rejection gate | GU-derived `rho_AB`, finite reduction map, GU-admissible observables, NAC for live state/settings | copying Bell state into GU slot; relabeling Pati-Salam ansatz as derived; using Pauli settings without measurement postulate | derived state is separable, all admissible settings give `CHSH <= 2`, or violation only comes from controls/ansatz |
| `VZ-14D` | `conditional_reconstruction` | typed-spine Schur principal-symbol proof for `lambda_d != 0` | primary `D_GU` provenance and downstream 4D/subprincipal/gauge dynamics | using zero-order `Phi_F` as first-order `Phi_d`; treating VZ as full QFT recovery | primary operator lacks `Phi_d`, has `lambda_d = 0`, coefficient changes without rederivation, or 4D/subprincipal gate fails |
| `ANOMALY` | `relative_ordinary_sm_shadow_open_full_gu_shadow` | ordinary one-generation SM anomaly cancellation after relative Pati-Salam-to-SM branch | target-free finite-control/shadow selector; complete anomaly calculation for all observer-facing modes | assuming ordinary SM shadow; deleting extra modes by fiat; using anomaly cancellation to select the packet | any extra observer-facing anomalous mode survives, or the shadow is not exactly ordinary anomaly-free SM content |

## 7. Branch/Source Robustness Table

| source lane | what it can robustly supply now | what it cannot supply now | QFT-shadow decision |
|---|---|---|---|
| typed operator spine | conditional principal-symbol data and candidate field operator | primary source closure, state space, vacuum, observables, unitarity | useful input, not a QFT shadow |
| full action/IG branch | branch taxonomy and known free-beta obstruction | fixed physical action, full EL tuple, source law, vacuum sector | blocked before QFT dynamics |
| zero-mode/projector lane | possible future finite state source; current RS/projector controls elsewhere in repo | physical gauge-fixed zero-mode basis and positive finite Gram matrix | promising but currently missing |
| two-point/quasifree lane | best next source for algebraic/Fock state extraction | actual GU two-point function, Hadamard/positivity, finite covariance | best next computation |
| Pati-Salam finite proxy | finite labels and executable CHSH harness | GU-derived density matrix and measurement postulate | downstream test only |
| Type II_1/Connes host lane | conditional hosting and negative selector discipline | target-free `A_F`, `G_SM/Z_6`, exact shadow, full anomaly proof | host/open, not selector |
| ordinary SM anomaly formulas | verification after exact ordinary shadow is produced | selection of the shadow or deletion of extra modes | relative check only |
| conventional metric quantization | not used by the GU premise | cannot be cited as the missing GU extraction unless adopted as a new branch | outside this certificate |

The robust source for the next step is the two-point/quasifree lane, because it can feed
all downstream gates at once: algebraic state, GNS/Fock representation, finite covariance,
Born probabilities, locality, and CHSH state extraction.

## 8. Forbidden Shortcuts And Rollback Conditions

Forbidden shortcuts:

| shortcut | why forbidden |
|---|---|
| "GU is geometric, therefore quantum recovery is unnecessary" | false target: observed physics still requires quantum states, probabilities, and QFT consistency |
| "We are not quantizing the GR metric, therefore QFT is avoided" | QFT recovery is owed even if metric quantization is not the route |
| representation labels as a Hilbert state | labels do not determine amplitudes, phases, density matrices, or correlations |
| Bell/CHSH control state as GU state | the existing gate correctly rejects controls and ansatz states |
| Pauli controls as GU-admissible observables | noncommuting settings need a measurement postulate and physical readout rule |
| VZ principal-symbol closure as unitarity/locality/QFT proof | VZ is a causal-symbol gate only |
| ordinary SM anomaly cancellation as full GU anomaly proof | extra observer-facing GU/Type II_1 modes may survive |
| importing `A_F`, `G_SM`, `K_SM`, or `n=3` as selector output | finite-control ledgers classify this as target import or cardinality transport |
| writing a formal path integral with no measure/state/reflection positivity | notation alone does not produce a QFT state or probabilities |
| hidden metric quantization rescue | if adopted, it is a new branch and must satisfy its own quantum-gravity assumptions |

Rollback conditions:

```text
QFT-SHADOW rolls back to fail if no positive Hilbert/Fock/algebraic state space can be
constructed from the source branch.

QFT-SHADOW rolls back to fail if the only available states are copied controls, imported
SM finite data, or ansatz density matrices.

OBS-CHSH rolls back to fail for physical forcing if the derived state/settings give no
Bell violation or if the observables are not GU-admissible.

VZ-14D causal support rolls back if the primary operator lacks the Phi_d first-order
block or changes lambda_d without rederivation.

ANOMALY rolls back if any observer-facing extra mode has an uncanceled perturbative,
global, or cobordism anomaly.

UNITARITY rolls back if gauge reduction leaves negative-norm physical states, the
Hamiltonian is not self-adjoint on the physical domain, or the algebraic dynamics does
not preserve the positive state class.
```

## 9. Next Meaningful Proof/Computation Step

Do not add another Bell state and do not add another global prose synthesis. The next
meaningful step is one end-to-end `QFTStateExtractionCertificate`, preferably through the
two-point/quasifree lane.

Minimal proof/computation packet:

1. Fix one source branch:

```text
D_GU, action/variation branch if needed, section, gauge constraints, boundary/vacuum,
and the physical observer cone.
```

2. Construct the physical field algebra or one-particle space:

```text
field complex -> gauge quotient -> positive pairing -> CAR/CCR or local *-algebra net.
```

3. Compute a source-derived two-point function or covariance:

```text
G_LR(x_A,x_B) = omega_GU(psi_L(x_A) psi_R_bar(x_B))
K_AB = finite covariance on V_L tensor V_R
```

and prove positivity/normalization.

4. Reduce to a finite observer state:

```text
rho_AB in End(H_A tensor H_B),
role = "gu_derived",
provenance = "gu-derived:<operator/section/vacuum/reference>".
```

5. Derive admissible observables from the same source:

```text
A, A' in End(H_A), B, B' in End(H_B),
provenance = "gu-admissible:<measurement-postulate-reference>".
```

6. Run the existing gate without weakening it:

```bash
python tests/h3_pati_salam_gu_measurement_gate.py
python tests/h3_pati_salam_gu_measurement_gate.py --require-gu
```

The second command should fail today. It should pass only when real GU-derived state and
observable hooks exist.

7. In parallel, run the anomaly shadow check:

```text
list all observer-facing modes produced by the same shadow functor,
then compute perturbative/global/cobordism anomaly compatibility for all of them.
```

This packet would decide whether GU recovers an observer-facing QFT shadow. It could also
produce a negative result. A negative result is acceptable; an unlicensed Bell state or
imported quantum theory is not.

## Machine-Readable QFT Shadow Certificate

```json
{
  "version": "2026-06-24",
  "verdict": "QFT_SHADOW_SCHEMA_DEFINED_CURRENT_REPO_BLOCKED",
  "status_enum": [
    "supplied",
    "partial",
    "conditional",
    "missing",
    "open",
    "blocked",
    "relative"
  ],
  "stage_order": [
    "SourceGeometryCertificate",
    "PhysicalFieldComplexCertificate",
    "QFTStateSpaceExtractionCertificate",
    "QFTStateExtractionCertificate",
    "ObservableAdmissibilityCertificate",
    "BornProbabilityCertificate",
    "LocalityCausalityCertificate",
    "UnitarityCertificate",
    "SpinStatisticsCertificate",
    "AnomalyShadowCertificate"
  ],
  "stages": [
    {
      "id": "SourceGeometryCertificate",
      "status": "partial",
      "required_fields": ["I_GU", "D_GU", "S_GU", "section", "branch", "boundary_or_vacuum", "gauge_constraints"],
      "missing": ["primary_source_closed_D_GU", "written_branch_closed_S_GU", "fixed_variation_space"]
    },
    {
      "id": "PhysicalFieldComplexCertificate",
      "status": "missing",
      "required_fields": ["physical_fields", "gauge_quotient", "domains", "adjoints", "grading", "CAR_or_CCR_choice"],
      "missing": ["physical_field_complex", "gauge_fixed_domains", "ghost_or_constraint_accounting"]
    },
    {
      "id": "QFTStateSpaceExtractionCertificate",
      "status": "missing",
      "required_fields": ["Hilbert_or_Fock_or_local_algebra_net", "positive_pairing", "representation", "locality_domain"],
      "missing": ["positive_state_space", "local_algebra_net_or_Fock_space", "GNS_or_Fock_representation"]
    },
    {
      "id": "QFTStateExtractionCertificate",
      "status": "missing",
      "required_fields": ["source_kind", "source_provenance", "omega_or_rho", "positivity", "normalization"],
      "missing": ["GU_vacuum_or_two_point_state", "finite_covariance_K_AB", "rho_AB"]
    },
    {
      "id": "ObservableAdmissibilityCertificate",
      "status": "missing",
      "required_fields": ["observable_rule", "self_adjointness", "spectrum_or_effects", "locality", "readout_provenance"],
      "missing": ["GU_measurement_postulate", "gu_admissible_local_observables"]
    },
    {
      "id": "BornProbabilityCertificate",
      "status": "missing",
      "required_fields": ["state", "effect_or_projector", "probability_formula", "normalization"],
      "missing": ["Born_rule_extraction_from_GU_state_and_observables"]
    },
    {
      "id": "LocalityCausalityCertificate",
      "status": "conditional",
      "required_fields": ["microcausality", "NAC", "causal_cone", "wavefront_or_characteristic_control"],
      "missing": ["microcausality_for_live_QFT_shadow", "NAC_for_live_CHSH_state_observables"]
    },
    {
      "id": "UnitarityCertificate",
      "status": "missing",
      "required_fields": ["self_adjoint_generator_or_star_automorphism", "physical_inner_product", "state_preservation"],
      "missing": ["unitary_time_evolution", "positive_physical_inner_product_after_gauge_reduction"]
    },
    {
      "id": "SpinStatisticsCertificate",
      "status": "missing",
      "required_fields": ["spin_representation", "statistics_rule", "positivity", "locality", "CAR_CCR_consistency"],
      "missing": ["spin_statistics_theorem_hypotheses_for_GU_shadow", "CAR_CCR_assignment_from_source"]
    },
    {
      "id": "AnomalyShadowCertificate",
      "status": "open",
      "required_fields": ["observer_shadow_modes", "perturbative_anomalies", "global_anomalies", "cobordism_or_inflow", "extra_mode_policy"],
      "missing": ["target_free_exact_SM_shadow_or_extra_mode_anomaly_cancellation"]
    }
  ],
  "claim_certificates": [
    {
      "id": "QFT-SHADOW",
      "status": "blocked",
      "proof_grade": "specification",
      "missing_objects": [
        "QFTStateSpaceExtractionCertificate",
        "QFTStateExtractionCertificate",
        "ObservableAdmissibilityCertificate",
        "BornProbabilityCertificate",
        "UnitarityCertificate",
        "SpinStatisticsCertificate",
        "AnomalyShadowCertificate"
      ],
      "rollback_conditions": [
        "no_positive_state_space",
        "no_normalized_source_derived_state",
        "no_admissible_observables",
        "nonunitary_dynamics",
        "uncanceled_observer_anomaly"
      ]
    },
    {
      "id": "OBS-CHSH",
      "status": "blocked",
      "proof_grade": "executable_control",
      "missing_objects": ["rho_AB", "GU_measurement_postulate", "gu_admissible_local_observables", "NAC_for_live_state_settings"],
      "rollback_conditions": ["derived_state_separable", "all_admissible_settings_CHSH_le_2", "violation_only_from_ansatz"]
    },
    {
      "id": "VZ-14D",
      "status": "conditional",
      "proof_grade": "conditional_reconstruction",
      "missing_objects": ["primary_source_closed_D_GU", "lambda_d_provenance", "4D_subprincipal_gate"],
      "rollback_conditions": ["primary_D_GU_lacks_Phi_d", "lambda_d_zero", "coefficient_changed_without_rederivation"]
    },
    {
      "id": "ANOMALY",
      "status": "open",
      "proof_grade": "relative_reconstruction",
      "missing_objects": ["target_free_exact_SM_shadow", "extra_mode_anomaly_calculation", "Freed_Hopkins_compatibility_for_surviving_modes"],
      "rollback_conditions": ["extra_observer_mode_anomalous", "ordinary_SM_shadow_assumed_not_derived"]
    }
  ],
  "forbidden_shortcuts": [
    "geometry_means_quantum_recovery_unnecessary",
    "not_quantizing_GR_metric_means_no_QFT_debt",
    "representation_labels_as_quantum_state",
    "Bell_control_as_GU_state",
    "Pauli_controls_as_GU_measurements",
    "VZ_as_full_QFT_recovery",
    "ordinary_SM_anomaly_cancellation_as_full_GU_shadow",
    "import_A_F_G_SM_K_SM_or_n3",
    "formal_path_integral_without_state_or_positivity"
  ],
  "next_step": {
    "id": "compute_GU_two_point_or_covariance_to_finite_rho_AB",
    "preferred_lane": "two_point_quasifree",
    "must_emit": [
      "positive_QFT_state_space",
      "GU_vacuum_or_two_point_state",
      "finite_covariance_K_AB",
      "rho_AB",
      "gu_admissible_local_observables",
      "probabilities",
      "anomaly_shadow_mode_list"
    ]
  }
}
```
