---
doc_type: manuscript_dgu01_operator_source_identity_gate
run: hourly-20260625-0301
cycle: 2
lane: 3
owned_path: "explorations/hourly-20260625-0301-cycle2-manuscript-dgu01-operator-source-identity.md"
companion_audit: "tests/hourly_20260625_0301_cycle2_manuscript_dgu01_operator_source_identity_audit.py"
source_pdf: "Geometric_UnityDraftApril1st2021.pdf"
artifact_id: "ManuscriptDGU01OperatorSourceCandidate_V1"
target_object: "D_GU^epsilon 0/1 typed target"
---

# Manuscript DGU01 Operator Source Identity Gate

## 1. Verdict

Verdict: **blocked**.

`ManuscriptDGU01OperatorSourceCandidate_V1` resolves the Cycle 1 DGU/VZ
obstruction as far as the local 2021 manuscript allows. The manuscript emits a
real source-native action/operator/Euler-Lagrange cluster on PDF pages 41-48
and a related first-order / second-order equation summary on PDF pages 55-58.
That cluster is decision-grade positive evidence for a GU bosonic/fermionic
operator program, but it does not identify, define, or prove equality with the
later `D_GU^epsilon` 0/1 typed target.

Receipt decision:

```text
accepted_receipt_count: 0
candidate_status: quarantined_positive_source_locator
identity_gate_passed: false
principal_symbol_computation_allowed: false
proof_restart_allowed: false
```

No principal symbol is computed or claimed here. The local manuscript does not
source-establish identity between any emitted `omega`, `T_omega`, `B_omega`,
Shiab, `/D_omega`, `Upsilon`, or `delta_omega` object and the later
`D_GU^epsilon` 0/1 operator.

## 2. What Was Derived Directly From Repo Sources

Direct controls from repo sources:

| source | direct constraint |
|---|---|
| `RESEARCH-POSTURE.md` | Do constructive GU reconstruction, but do not treat compatibility or target success as derivation. |
| `process/runbooks/five-lane-frontier-run.md` | Produce a verdict artifact; do not let hosted-by become selected-by or compatible-with become derived-from. |
| Cycle 1 DGU/VZ artifact | The first missing object is `operator_source_primary_action_or_EL for D_GU^epsilon 0/1`; accepted receipt count was zero. |
| Cycle 1 transition ledger | This lane's next object is `ManuscriptDGU01OperatorSourceCandidate_V1`. |
| Target-import guard | VZ, dark-energy, DESI, FLRW, or downstream success evidence cannot select a source operator. |

Direct local manuscript extraction from `Geometric_UnityDraftApril1st2021.pdf`
focused on PDF pages 41-48 and 55-58:

| normalized source object | manuscript locators | source-side role | identity result for `D_GU^epsilon` 0/1 |
|---|---:|---|---|
| `omega = (epsilon, varpi)` | pp. 44, 48, 57 | GU connection/gauge variable; `omega` packages the gauge element `epsilon` and connection form `varpi`. | Quarantined positive context; not a typed 0/1 operator. |
| `T_omega` | pp. 44-45, 56-58 | Shifted/displaced torsion, e.g. `varpi - epsilon^{-1} d_0 epsilon` or relative to the gauge-transformed Levi-Civita spin connection. | Rejected as operator identity; it is a field/input term, not the target operator. |
| `B_omega` | pp. 44, 57 | Gauge-rotated Levi-Civita spin connection; the manuscript writes `B_omega = nabla_0 + epsilon^{-1} d_0 epsilon` and later `nabla^{B_omega} = nabla^g . epsilon`. | Quarantined as connection data; no source equality to `D_GU^epsilon` 0/1. |
| `Shiab_omega` / `circledot_omega` | pp. 41-44, 56-57 | Gauge-covariant contraction/projection-like operator on ad-valued curvature forms; kills Weyl curvature while preserving gauge covariance. | Quarantined positive operator family; no source-selected actual DGU 0/1 identity. |
| `/D_omega` | pp. 46-47 | Fermionic Dirac-like block matrix acting on `(zeta, nu)` spinorial fields with `rho(epsilon)` factors. | Rejected for DGU 0/1 identity; source does not identify it with the target rolled-up operator. |
| `Upsilon_omega` | pp. 44-47, 55 | Euler-Lagrange object: `dI_1` gives `(Upsilon_omega, Xi_omega)`, `Upsilon_omega = 0`, and combined `Upsilon^B + Upsilon^F = 0`. | Quarantined positive EL locator; not a source-emitted `D_GU^epsilon` 0/1 action/operator/EL certificate. |
| `delta_omega` | pp. 47-48, 55 | Proposed square-root/cochain operator with `delta_omega_2 o delta_omega_1 = Upsilon_omega`; deformation complex operators are then specified for the bosonic piece. | Quarantined deformation-complex route; no family identity to the DGU 0/1 target. |

Negative direct derivations:

```text
No literal D_GU or D_GU^epsilon token was found in the checked manuscript
page cluster or inherited full-PDF Cycle 1 search.

No principal-symbol passage was found for the target operator.

No source passage says that Shiab_omega, /D_omega, Upsilon_omega, or
delta_omega is the later D_GU^epsilon 0/1 typed operator.
```

## 3. The Strongest Positive Result

The strongest positive result is not a receipt; it is a clean source-side
operator/action/EL locator:

```text
PDF pp. 43-48 plus pp. 55-57 emit a GU first-order equation architecture:

IB_1 -> dIB_1 = (Upsilon_omega, Xi_omega), Xi = D_omega Upsilon_omega
Upsilon_omega = 0
IB_2 = ||Upsilon_omega||^2 -> D_omega^* Upsilon_omega = 0
Upsilon_omega = (delta_omega)^2 = delta_omega_2 o delta_omega_1
```

The manuscript also emits detailed ingredients around that architecture:
`omega = (epsilon, varpi)`, `T_omega`, `B_omega`, a Shiab contraction operator,
a fermionic `/D_omega`, and deformation operators `delta_omega_1`,
`delta_omega_2`. This is stronger than a metadata hint because it is local
primary manuscript content and includes action and Euler-Lagrange objects.

The positive result remains quarantined because the page cluster does not
perform the required identity step:

```text
source-emitted action/operator/EL object = actual D_GU^epsilon 0/1 typed target
```

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
SourceEstablishedIdentity(
  manuscript_emitted_object,
  D_GU^epsilon_0_1_typed_target
)
```

The obstruction appears before any principal-symbol calculation. On PDF pages
42-43, the manuscript says the historical Shiab operator choice was made using
representation theory and Bianchi identity considerations, but the author could
not locate the old notes and would need either to find or reconstruct the
argument. Therefore the manuscript supplies an operator family and candidate
instantiations, not a source-selected operator instance that can be identified
with `D_GU^epsilon` 0/1.

Missing proof fields:

| required field | manuscript status |
|---|---|
| actual `D_GU^epsilon` 0/1 operator formula | Missing. |
| domain/codomain of the 0/1 typed target | Missing. |
| source statement equating the target with Shiab, `/D_omega`, `Upsilon_omega`, or `delta_omega` | Missing. |
| principal symbol `sigma_1(D_GU^epsilon)` | Missing; computation not allowed before identity. |
| lower-order coefficient packet for the actual target | Missing. |
| accepted source action/operator/EL receipt | Missing. |

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The constructive next object is an identity packet:

```text
DGU01ManuscriptIdentityPacket_V1
```

It would remove or test the obstruction only if it supplies all of:

1. exact source locator for a manuscript-emitted action/operator/EL object;
2. typed target declaration for the later `D_GU^epsilon` 0/1 object;
3. explicit source-side equality, definition, or derivation connecting the two;
4. domain, codomain, grading, chirality, and projection conventions;
5. lower-order term and coefficient packet before any VZ or cosmology test;
6. principal-symbol eligibility, not the principal symbol itself unless the
   identity gate has already passed;
7. target-import flags all false.

If no such packet can be found, the right next artifact is a scoped negative
receipt for the 2021 manuscript page cluster.

## 6. What This Means For The Relevant GU Claim

Allowed claim:

```text
The 2021 manuscript contains a primary source-native GU action/operator/EL
cluster that is a serious locator for reconstructing the actual DGU 0/1 source
operator.
```

Not allowed:

```text
The actual D_GU^epsilon 0/1 operator is identified.
The principal symbol of D_GU^epsilon is emitted or computed.
The VZ analysis can restart.
VZ evasion, dark-energy recovery, DESI agreement, or FLRW proof status is
improved by this artifact.
```

For the relevant GU claim, the manuscript keeps the reconstruction path alive
but blocked. It supports a constructive search for an identity packet; it does
not by itself promote the DGU/VZ operator-source claim.

## 7. Next Meaningful Proof Or Computation Step

The next meaningful step is not a VZ computation. It is a family-identity pass:

1. Build a display-equation index for PDF pages 41-48 and 55-58.
2. For each row, type the emitted source object as field, action, EL object,
   algebraic operator, differential operator, or deformation operator.
3. Compare only source-established types against the later
   `D_GU^epsilon` 0/1 typed target.
4. If identity is source-established, then and only then compute
   `sigma_1(D_GU^epsilon)` and lower-order packets.
5. If identity is still absent, emit a scoped negative receipt and keep proof
   restart blocked.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "ManuscriptDGU01OperatorSourceCandidate_V1",
  "run": "hourly-20260625-0301",
  "cycle": 2,
  "lane": 3,
  "verdict_class": "blocked",
  "source_pdf": "Geometric_UnityDraftApril1st2021.pdf",
  "focused_pdf_pages": [41, 42, 43, 44, 45, 46, 47, 48, 55, 56, 57, 58],
  "target_object": "D_GU^epsilon 0/1 typed target",
  "candidate_status": "quarantined_positive_source_locator",
  "accepted_receipt_count": 0,
  "accepted_receipts": [],
  "identity_gate": {
    "passed": false,
    "required_identity": "SourceEstablishedIdentity(manuscript_emitted_object, D_GU^epsilon_0_1_typed_target)",
    "source_emits_D_GU_epsilon_token": false,
    "source_defines_target_0_1_domain_codomain": false,
    "source_equates_any_normalized_object_to_target": false,
    "first_obstruction": "historical Shiab operator choice not located or reconstructed; no source-selected actual DGU 0/1 operator instance"
  },
  "principal_symbol_guard": {
    "principal_symbol_computation_allowed": false,
    "principal_symbol_claimed": false,
    "reason": "identity gate failed before symbol eligibility"
  },
  "normalized_source_objects": [
    {
      "name": "omega",
      "normalized_form": "omega = (epsilon, varpi) in G = H semidirect N",
      "pdf_pages": [44, 48, 57],
      "source_role": "GU connection/gauge variable",
      "object_kind": "field_packet",
      "identity_status": "quarantined_context_not_operator",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "quarantined"
    },
    {
      "name": "T_omega",
      "normalized_form": "T_omega = varpi - epsilon^{-1} d_0 epsilon, also measured relative to gauge-transformed Levi-Civita spin connection",
      "pdf_pages": [44, 45, 56, 57, 58],
      "source_role": "shifted or displaced torsion term",
      "object_kind": "field_or_input_term",
      "identity_status": "rejected_not_operator",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "rejected"
    },
    {
      "name": "B_omega",
      "normalized_form": "B_omega = nabla_0 + epsilon^{-1} d_0 epsilon; nabla^{B_omega} = nabla^g . epsilon",
      "pdf_pages": [44, 57],
      "source_role": "gauge-rotated Levi-Civita spin connection",
      "object_kind": "connection_data",
      "identity_status": "quarantined_connection_not_target",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "quarantined"
    },
    {
      "name": "Shiab_omega",
      "normalized_form": "circledot_epsilon or circledot_omega maps ad-valued 2-forms to ad-valued (d-1)-forms by gauge-covariant contraction",
      "pdf_pages": [41, 42, 43, 44, 56, 57],
      "source_role": "curvature contraction/projection-like operator family",
      "object_kind": "algebraic_source_operator_family",
      "identity_status": "quarantined_positive_family_missing_source_selector_and_DGU_0_1_identity",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "quarantined"
    },
    {
      "name": "/D_omega",
      "normalized_form": "fermionic Dirac-like block operator acting on (zeta, nu) spinorial fields with rho(epsilon) factors",
      "pdf_pages": [46, 47],
      "source_role": "fermionic first-order operator display",
      "object_kind": "differential_operator",
      "identity_status": "rejected_no_source_identity_to_DGU_0_1_target",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "rejected"
    },
    {
      "name": "Upsilon_omega",
      "normalized_form": "dI_1 gives (Upsilon_omega, Xi_omega), Xi = D_omega Upsilon_omega; reduced first-order equation Upsilon_omega = 0",
      "pdf_pages": [44, 45, 46, 47, 55],
      "source_role": "Euler-Lagrange object and first-order equation",
      "object_kind": "EL_object",
      "identity_status": "quarantined_positive_EL_locator_not_target_identity",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "quarantined"
    },
    {
      "name": "delta_omega",
      "normalized_form": "delta_omega is a proposed square root with delta_omega_2 o delta_omega_1 = Upsilon_omega",
      "pdf_pages": [47, 48, 55],
      "source_role": "deformation-complex operator route",
      "object_kind": "deformation_operator",
      "identity_status": "quarantined_deformation_route_missing_target_identity",
      "identical_to_D_GU_epsilon_0_1": false,
      "explicitly_defines_D_GU_epsilon_0_1": false,
      "acceptance_status": "quarantined"
    }
  ],
  "strongest_positive_result": {
    "status": "source_native_action_operator_EL_cluster",
    "locators": ["PDF pp. 43-48", "PDF pp. 55-57"],
    "accepted_as_DGU_01_receipt": false,
    "reason": "source emits GU action/operator/EL architecture but not identity to later D_GU^epsilon 0/1 typed target"
  },
  "constructive_next_object": "DGU01ManuscriptIdentityPacket_V1",
  "constructive_next_object_requires": [
    "exact_source_locator",
    "typed_D_GU_epsilon_0_1_target_declaration",
    "source_side_equality_definition_or_derivation",
    "domain_codomain_grading_chirality_projection_conventions",
    "lower_order_term_and_coefficient_packet_before_target_tests",
    "principal_symbol_eligibility_after_identity_gate",
    "target_import_flags_all_false"
  ],
  "target_import_flags": {
    "VZ_used_to_select_operator": false,
    "dark_energy_used_to_select_operator": false,
    "DESI_used_to_select_operator": false,
    "FLRW_used_to_select_operator": false,
    "downstream_target_success_used_as_source_evidence": false
  },
  "forbidden_promotions": {
    "DGU_actual_operator_identified": false,
    "principal_symbol_emitted_or_computed": false,
    "VZ_evasion_established": false,
    "dark_energy_recovery_established": false,
    "DESI_agreement_established": false,
    "FLRW_proof_status_improved": false,
    "proof_restart_allowed": false
  },
  "next_meaningful_step": [
    "build_display_equation_index_for_pages_41_48_and_55_58",
    "type_each_source_object_as_field_action_EL_algebraic_operator_differential_operator_or_deformation_operator",
    "compare_only_source_established_types_against_D_GU_epsilon_0_1",
    "compute_principal_symbol_only_after_identity_gate_passes",
    "emit_scoped_negative_receipt_if_identity_remains_absent"
  ]
}
```
