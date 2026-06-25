---
doc_type: manuscript_dgu_vz_operator_receipt_candidates
run: hourly-20260625-0301
cycle: 1
lane: 4
owned_path: "explorations/hourly-20260625-0301-cycle1-manuscript-dgu-vz-operator-receipt-candidates.md"
companion_audit: "tests/hourly_20260625_0301_cycle1_manuscript_dgu_vz_operator_receipt_candidates_audit.py"
source_pdf: "Geometric_UnityDraftApril1st2021.pdf"
target_object: "operator_source_primary_action_or_EL for D_GU^epsilon 0/1"
---

# 2021 Manuscript DGU/VZ Operator Receipt Candidate Search

## 1. Verdict

Verdict: **blocked**.

The 2021 manuscript contains real source-adjacent action, operator,
Euler-Lagrange, and deformation-complex material. The strongest passages are
the Shiab/action/Euler-Lagrange cluster on PDF pages 41-48 and the first-order
/ second-order equation summary on PDF pages 55-58. They do not emit the
specific target object needed by the DGU/VZ receipt gate:

```text
operator_source_primary_action_or_EL for D_GU^epsilon 0/1
```

In particular, the local text search found no literal `D_GU`, no `D_GU^epsilon`,
and no `principal symbol` passage in the PDF extraction. The manuscript gives a
GU action scaffold, a Shiab contraction operator family, a `/D_omega` fermionic
operator display, and deformation operators `delta_omega_1, delta_omega_2`, but
it remains schematic or adjacent for the later `D_GU^epsilon` 0/1 operator
certificate.

Receipt decision:

```text
candidate_acceptance_status: none accepted
accepted_receipt_count: 0
first_missing_object: operator_source_primary_action_or_EL for D_GU^epsilon 0/1
proof_restart_allowed: false
target_import_flags: false
```

## 2. What Was Derived Directly From Repo Sources

The direct source inputs were the research posture, the five-lane runbook, the
prior DGU source-receipt artifacts, the target-import guard, and local text
extraction from `Geometric_UnityDraftApril1st2021.pdf`.

From the prior repo artifacts:

| Source | Directly inherited constraint |
| --- | --- |
| `hourly-20260625-0103-cycle1-dgu-01-operator-source-receipt.md` | The first missing DGU/VZ receipt field is `operator_source_primary_action_or_EL`; typed-spine and reconstruction algebra do not count as primary source receipts. |
| `hourly-20260625-0103-cycle2-dgu-primary-source-locator.md` | UCSD/transcript hints and local reconstructions are primary hints or reconstruction targets, not an actual `D_GU^epsilon` 0/1 source operator receipt. |
| `hourly-20260625-0203-cycle2-repo-local-primary-gu-source-receipt-map.md` | DGU/VZ requires an `operator_source_primary_action_or_EL for D_GU^epsilon 0/1`; accepted receipt count was zero before this manuscript pass. |
| `hourly-20260625-0203-cycle3-target-import-guard-receipt-audit.md` | VZ success, dark-energy recovery, DESI, FLRW, or other target-facing evidence cannot select a source operator. |

From the 2021 manuscript search:

| Query family | PDF page locators | Directly derived result |
| --- | --- | --- |
| `D_GU`, `D_GU^epsilon` | none found in extracted text | The manuscript extraction does not name the target operator. |
| `principal symbol` | none found in extracted text | The manuscript extraction does not emit `sigma_1(D_GU^epsilon)`. |
| `Shiab`, `operator`, `Bianchi` | pp. 41-44, 56-57, 65 | The manuscript gives a family of Shiab contraction operators and says Bianchi identity considerations were intended to choose an operator, while also saying the original calculation/notes are not located. |
| `action`, `Euler`, `Lagrange`, `first order`, `second order` | pp. 43-45, 55-58, 64-65 | The manuscript gives bosonic actions and Euler-Lagrange forms, plus a first-order / second-order GU equation schema. |
| `fermionic`, `Dirac`, `/D_omega` | pp. 46-48, 60-62 | The manuscript gives a fermionic operator display and a deformation-complex context, but not the target `D_GU^epsilon` 0/1 receipt. |
| `inhomogeneous gauge group`, `epsilon`, `theta`, `pi`, `alpha` | pp. 32-40, 43-48, 56-57 | The manuscript supplies representation and variable context for `G = H semidirect N`, `omega = (epsilon, varpi)`, and variations, but not a source-emitted DGU/VZ operator certificate. |

## 3. The Strongest Positive Result

The strongest positive result is that the manuscript does contain a primary
source-adjacent GU action/operator/Euler-Lagrange scaffold:

| Candidate id | Locator | Short paraphrase | Acceptance status |
| --- | --- | --- | --- |
| `MS2021-SHIAB-FAMILY` | PDF pp. 41-42 | Introduces the Ship-in-a-Bottle idea and a Shiab contraction operator family using gauge-conjugated invariant forms. | `rejected_schematic_operator_family` |
| `MS2021-BOSONIC-ACTION-EL` | PDF pp. 43-45 | Defines a first-order bosonic action `I_B1`, a Shiab operator, and Euler-Lagrange forms `Upsilon_omega`, `Xi_omega`; records a GU equation of the form `Upsilon_omega = 0`. | `rejected_adjacent_action_EL_not_D_GU_epsilon_0_1` |
| `MS2021-FERMIONIC-DIRACLIKE` | PDF pp. 46-47 | Displays a fermionic Dirac-like operator `/D_omega` and combines bosonic/fermionic variations into `Upsilon_omega`. | `rejected_adjacent_fermionic_operator_not_receipt` |
| `MS2021-DEFORMATION-COMPLEX` | PDF pp. 47-48 | Posits a deformation complex with `delta_omega_1` and `delta_omega_2` coming from linearized equations of motion. | `rejected_deformation_complex_not_source_operator` |
| `MS2021-EQUATION-SUMMARY` | PDF pp. 55-58, 64-65 | States that first-order reduced Euler-Lagrange equations imply a related second-order theory and summarizes the GU Dirac-square-root picture. | `rejected_claim_schema_not_operator_receipt` |

This is stronger than metadata or secondary reconstruction because it is in the
manuscript itself and includes action and Euler-Lagrange formulas. It still does
not accept as the required source object, because the passage does not identify
the later `D_GU^epsilon` 0/1 operator, its rolled-up domain/codomain, its
principal symbol, or the coefficient packet needed by the DGU/VZ gate.

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction remains:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

The manuscript obstruction is sharper than a generic absence. On PDF p. 42,
the author says the Shiab operators were previously chosen by representation
theory and Bianchi identity considerations, but the author has been unable to
locate the old notes and hopes either to find or reconstruct the argument. That
prevents this manuscript from serving as an accepted operator-choice receipt.

The p. 43 footnote repeats the same obstruction for the specific settled Shiab
operator: it says the operator cannot yet be located and, even if found, would
be in a different language. Therefore the manuscript emits an operator family
and candidate action machinery, not an actual source-selected operator instance
for `D_GU^epsilon` 0/1.

Missing proof objects:

| Missing object | Why it is still missing |
| --- | --- |
| `D_GU^epsilon` 0/1 operator formula | No literal `D_GU` or `D_GU^epsilon` occurrence was found in the PDF extraction; the displayed operators are Shiab, `/D_omega`, and `delta_omega` objects. |
| `operator_source_primary_action_or_EL` | The manuscript gives source-adjacent action/EL formulas but does not connect them to the actual later DGU 0/1 receipt object. |
| `sigma_1(D_GU^epsilon)` | No `principal symbol` passage was found; no source-derived principal symbol for the target operator is emitted. |
| coefficient / lower-order packet | The manuscript uses `epsilon`, `varpi`, `theta`, `alpha`, `kappa`, curvature, torsion, and Shiab terms, but does not supply the target DGU/VZ coefficient packet for the 0/1 block. |
| family identity gate | No passage proves identity between the manuscript's schematic GU operator/action material and the later typed `D_GU^epsilon` 0/1 operator used by DGU/VZ analyses. |

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The constructive next object is:

```text
ManuscriptDGU01OperatorSourceCandidate_V1
```

It would need to quote or transcribe one primary passage that performs all of
the following source-side tasks:

1. names or defines the actual first-order GU operator corresponding to
   `D_GU^epsilon` on the rolled-up 0/1 sector;
2. fixes the domain, codomain, grading, and projection conventions;
3. derives the operator from the manuscript action or Euler-Lagrange system, or
   explicitly defines it as the source operator;
4. computes or emits the principal symbol `sigma_1(D_GU^epsilon)`;
5. lists lower-order terms and coefficient dependencies before any VZ or
   cosmology comparison;
6. passes the target-import guard with no VZ, dark-energy, DESI, or FLRW
   evidence used to select the operator.

If no such manuscript passage exists, the next test is a negative-receipt
certificate for the 2021 manuscript:

```text
Manuscript2021NoDGU01OperatorReceipt_V1
```

That certificate should cite the positive page cluster and the p. 42 / p. 43
operator-choice obstruction, then explicitly block proof restart.

## 6. What This Means For The Relevant GU Claim

For the DGU/VZ claim, the 2021 manuscript improves source proximity but does
not close the source receipt.

Allowed claim:

```text
The 2021 manuscript contains primary source-adjacent GU action, Shiab operator,
Euler-Lagrange, and deformation-complex material that should be mined before
declaring the DGU/VZ operator source absent.
```

Forbidden claims:

```text
DGU/VZ actual D_GU^epsilon 0/1 is identified.
VZ evasion is established.
Dark-energy recovery is established.
FLRW proof status is improved.
Principal symbol sigma_1(D_GU^epsilon) is emitted.
Proof restart is allowed.
```

The relevant GU claim remains blocked at source intake. The manuscript can
guide the search for the actual operator, but it cannot be promoted into a
receipt for the actual DGU/VZ operator without an additional family-identity
and source-emission gate.

## 7. Next Meaningful Proof Or Computation Step

The next meaningful step is a focused source extraction, not a VZ computation:

```text
pages 41-48 and 55-58
  -> extract all action/operator/EL displays into normalized notation
  -> identify whether any displayed first-order operator is identical to the
     later D_GU^epsilon 0/1 typed-spine candidate
  -> compute the principal symbol only after identity is established
  -> keep proof restart blocked unless source acceptance and identity gate pass
```

Recommended sequence:

1. Build a display-equation index for PDF pp. 41-48 and 55-58.
2. Normalize `omega = (epsilon, varpi)`, `T_omega`, `B_omega`,
   `Shiab_omega`, `/D_omega`, `Upsilon_omega`, and `delta_omega`.
3. Compare those objects against the typed `D_roll` / `D_GU^epsilon` 0/1
   candidate only as a family-identity test.
4. Accept no source receipt unless the manuscript itself, or another primary GU
   source, emits the actual operator/action/EL object and principal symbol.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "ManuscriptDGU_VZ_OperatorReceiptCandidateSearch_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0301",
  "cycle": 1,
  "lane": 4,
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-0301-cycle1-manuscript-dgu-vz-operator-receipt-candidates.md",
  "companion_audit": "tests/hourly_20260625_0301_cycle1_manuscript_dgu_vz_operator_receipt_candidates_audit.py",
  "source_pdf": "Geometric_UnityDraftApril1st2021.pdf",
  "pdf_page_count_extracted": 69,
  "target_object": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
  "accepted_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "identity_gate_passed": false,
  "target_import_flags": {
    "VZ_used_to_select_operator": false,
    "dark_energy_used_to_select_operator": false,
    "DESI_used_to_select_operator": false,
    "FLRW_used_to_select_operator": false,
    "downstream_target_success_used_as_source_evidence": false
  },
  "searched_terms": [
    "action",
    "operator",
    "Euler",
    "Lagrange",
    "equation",
    "field equation",
    "alpha",
    "theta",
    "pi",
    "epsilon",
    "curvature",
    "divergence",
    "Bianchi",
    "inhomogeneous gauge group",
    "D_GU",
    "D_GU^epsilon",
    "deformation",
    "first order",
    "second order",
    "principal symbol",
    "Shiab",
    "Dirac",
    "D_omega",
    "delta_omega",
    "Upsilon_omega"
  ],
  "searched_term_results": {
    "D_GU": {
      "found": false,
      "pages": []
    },
    "D_GU^epsilon": {
      "found": false,
      "pages": []
    },
    "principal symbol": {
      "found": false,
      "pages": []
    },
    "divergence": {
      "found": false,
      "pages": []
    },
    "Bianchi": {
      "found": true,
      "pages": [42, 43, 57]
    },
    "Shiab": {
      "found": true,
      "pages": [41, 42, 43, 44, 56, 65]
    },
    "Euler_Lagrange": {
      "found": true,
      "pages": [44, 45, 55, 65]
    },
    "inhomogeneous_gauge_group": {
      "found": true,
      "pages": [32, 33, 34, 37, 39, 42, 64]
    },
    "first_order": {
      "found": true,
      "pages": [43, 55]
    },
    "second_order": {
      "found": true,
      "pages": [45, 55, 57, 58, 64, 65]
    }
  },
  "candidate_rows": [
    {
      "candidate_id": "MS2021-NO-DGU-LITERAL",
      "locator": "PDF extracted text, pages 1-69",
      "page_locators": [],
      "candidate_type": "negative_literal_search",
      "short_paraphrase": "No literal D_GU or D_GU^epsilon token was found in the extracted manuscript text.",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "emits_action_or_EL_for_actual_D_GU_epsilon_0_1": false,
      "emits_principal_symbol": false,
      "target_data_seen": [],
      "acceptance_status": "rejected_no_target_operator_token"
    },
    {
      "candidate_id": "MS2021-SHIAB-FAMILY",
      "locator": "Geometric_UnityDraftApril1st2021.pdf pp. 41-42",
      "page_locators": [41, 42],
      "candidate_type": "source_adjacent_operator_family",
      "short_paraphrase": "Introduces Ship-in-a-Bottle and Shiab contraction operators built from gauge-conjugated invariant forms.",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "emits_action_or_EL_for_actual_D_GU_epsilon_0_1": false,
      "emits_principal_symbol": false,
      "target_data_seen": [],
      "acceptance_status": "rejected_schematic_operator_family",
      "obstruction": "The operator choice is described as historically chosen but not currently located or reconstructed."
    },
    {
      "candidate_id": "MS2021-BOSONIC-ACTION-EL",
      "locator": "Geometric_UnityDraftApril1st2021.pdf pp. 43-45",
      "page_locators": [43, 44, 45],
      "candidate_type": "source_adjacent_action_and_EL",
      "short_paraphrase": "Defines a first-order bosonic action, Shiab contraction, Euler-Lagrange forms Upsilon_omega and Xi_omega, and a GU equation Upsilon_omega = 0.",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "emits_action_or_EL_for_actual_D_GU_epsilon_0_1": false,
      "emits_principal_symbol": false,
      "target_data_seen": [],
      "acceptance_status": "rejected_adjacent_action_EL_not_D_GU_epsilon_0_1",
      "obstruction": "The action/EL formulas are not identified with the actual D_GU^epsilon rolled-up 0/1 operator."
    },
    {
      "candidate_id": "MS2021-FERMIONIC-DIRACLIKE",
      "locator": "Geometric_UnityDraftApril1st2021.pdf pp. 46-47",
      "page_locators": [46, 47],
      "candidate_type": "source_adjacent_fermionic_operator",
      "short_paraphrase": "Displays a fermionic Dirac-like /D_omega operator and combines fermionic and bosonic variations.",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "emits_action_or_EL_for_actual_D_GU_epsilon_0_1": false,
      "emits_principal_symbol": false,
      "target_data_seen": [],
      "acceptance_status": "rejected_adjacent_fermionic_operator_not_receipt",
      "obstruction": "No family identity is given between /D_omega and D_GU^epsilon 0/1."
    },
    {
      "candidate_id": "MS2021-DEFORMATION-COMPLEX",
      "locator": "Geometric_UnityDraftApril1st2021.pdf pp. 47-48",
      "page_locators": [47, 48],
      "candidate_type": "source_adjacent_deformation_complex",
      "short_paraphrase": "Posits a cohomological deformation complex with delta_omega operators from linearized equations of motion.",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "emits_action_or_EL_for_actual_D_GU_epsilon_0_1": false,
      "emits_principal_symbol": false,
      "target_data_seen": [],
      "acceptance_status": "rejected_deformation_complex_not_source_operator",
      "obstruction": "The complex is schematic and does not emit the DGU/VZ target operator or symbol."
    },
    {
      "candidate_id": "MS2021-EQUATION-SUMMARY",
      "locator": "Geometric_UnityDraftApril1st2021.pdf pp. 55-58 and 64-65",
      "page_locators": [55, 56, 57, 58, 64, 65],
      "candidate_type": "claim_schema_and_equation_summary",
      "short_paraphrase": "States first-order reduced Euler-Lagrange equations and related second-order equations in a Dirac-square-root schema.",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "emits_action_or_EL_for_actual_D_GU_epsilon_0_1": false,
      "emits_principal_symbol": false,
      "target_data_seen": [],
      "acceptance_status": "rejected_claim_schema_not_operator_receipt",
      "obstruction": "The passage supports the GU program schema but not the specific operator_source_primary_action_or_EL receipt."
    }
  ],
  "strongest_positive_result": {
    "candidate_id": "MS2021-BOSONIC-ACTION-EL",
    "locator": "Geometric_UnityDraftApril1st2021.pdf pp. 43-45",
    "status": "primary_source_adjacent_action_EL_scaffold",
    "accepted_as_receipt": false,
    "reason": "The manuscript emits action and Euler-Lagrange material but not the actual D_GU^epsilon 0/1 source operator or principal symbol."
  },
  "first_exact_obstruction": {
    "field": "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
    "manuscript_locator": "Geometric_UnityDraftApril1st2021.pdf pp. 42-43",
    "description": "The manuscript states that the historical Shiab operator choice/notes cannot currently be located and must be found or reconstructed."
  },
  "constructive_next_object": "ManuscriptDGU01OperatorSourceCandidate_V1",
  "constructive_next_object_allowed_only_if": [
    "source_emits_actual_D_GU_epsilon_0_1_operator",
    "source_emits_or_derives_action_or_EL_for_that_operator",
    "source_emits_or_allows_computation_of_sigma_1_D_GU_epsilon",
    "target_import_flags_all_false",
    "family_identity_gate_passed"
  ],
  "forbidden_promotions": {
    "DGU_actual_operator_identified": false,
    "VZ_evasion_established": false,
    "dark_energy_recovery_established": false,
    "FLRW_proof_status_improved": false,
    "principal_symbol_emitted": false,
    "proof_restart_allowed": false
  },
  "next_meaningful_step": [
    "build_display_equation_index_for_pages_41_48_and_55_58",
    "normalize_omega_T_omega_B_omega_Shiab_D_omega_Upsilon_delta_notation",
    "run_family_identity_test_against_D_GU_epsilon_0_1_candidate",
    "compute_principal_symbol_only_after_identity_gate",
    "keep_proof_restart_blocked_until_receipt_acceptance"
  ]
}
```
