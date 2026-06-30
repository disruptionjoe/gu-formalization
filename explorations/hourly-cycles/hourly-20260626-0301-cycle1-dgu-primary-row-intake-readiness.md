---
title: "Hourly 20260626 0301 Cycle 1 DGU Primary Row Intake Readiness"
date: "2026-06-25"
run_id: "hourly-20260626-0301"
cycle: 1
lane: "DGU"
doc_type: "frontier_gate"
artifact_id: "DGUPrimaryRowIntakeReadiness_0301_C1_DGU_V1"
verdict: "blocked_primary_row_instance_not_intake_ready"
owned_path: "explorations/hourly-20260626-0301-cycle1-dgu-primary-row-intake-readiness.md"
---

# Hourly 20260626 0301 Cycle 1 DGU Primary Row Intake Readiness

## 1. Verdict

Verdict: **blocked**.

The DGU route is not intake-ready for
`PrimarySourceDGU01SectorRuleRowInstance_V1`. The latest closeout fixes the
order:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1
  -> DGU01SameOperatorWitness_V1
  -> symbol certificate
  -> VZ replay
  -> proof restart candidate
```

That order cannot be advanced from typed `D_roll`. Typed `D_roll` is still a
comparison screen only. It may tell us what a candidate source row should be
compared against after a primary row is admitted; it may not supply the source
row, the row payload, the extraction method, or the actual operator handle.

Decision state:

```text
target_import_used: false
typed_d_roll_available_as_screen: true
typed_d_roll_allowed_as_source_row: false
primary_row_instance_found: false
primary_row_payload_found: false
row_extraction_method_found: false
actual_operator_handle_found: false
intake_ready_for_same_operator_witness: false
intake_ready_for_symbol_certificate: false
intake_ready_for_vz_replay: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `process/runbooks/five-lane-frontier-run.md` | Applied the frontier-run standard: produce a decision artifact, name the exact obstruction, and avoid claim inflation. |
| `RESEARCH-POSTURE.md` | Preserved the rule that compatibility, hosted vocabulary, or target success cannot become derivation. |
| `explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md` | Applied source-object before reduction/proof discipline and the source-to-shadow certificate stack. |
| `explorations/hourly-20260626-0202-three-cycle-fifteen-hole-synthesis.md` | Consumed the latest cross-route synthesis naming `PrimarySourceDGU01SectorRuleRowInstance_V1` as the next DGU frontier object. |
| `explorations/hourly-20260626-0202-cycle3-dgu-symbol-vz-closeout.md` | Consumed the latest DGU closeout and its blocked/no-restart order. |
| `explorations/hourly-20260626-0202-cycle1-dgu-primary-row-discriminator-gate.md` | Consumed the primary-row discriminator schema and the missing row payload. |
| `explorations/hourly-20260626-0202-cycle2-dgu-row-to-same-operator-firewall.md` | Consumed the same-operator firewall and the rule that typed `D_roll` sits only on the comparison side. |

Targeted identifier searches also checked prior DGU schema/protocol artifacts
for field names. They did not supply a new row instance.

## 3. Specific GU Claim Or Bridge Under Test

The claim under test is not "VZ works for typed `D_roll`." The tested bridge is:

```text
a primary source row emits the actual D_GU^epsilon 0/1 sector rule
well enough to instantiate PrimarySourceDGU01SectorRuleRowInstance_V1,
then compare that actual operator against typed D_roll,
then decide whether symbol and VZ replay work are admissible.
```

This is an intake gate for a source row. It is not a proof of the same-operator
witness, symbol certificate, hyperbolicity, VZ evasion, causality, or physical
recovery.

## 4. Strongest Positive Construction Attempt

The strongest admissible construction is a row-intake packet with these fields:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1:
  source_scope_id
  source_id
  exact_locator
  source_row_payload
  payload_integrity_or_capture_note
  extraction_method_to_D_GU_epsilon_0_1_sector_rule
  extracted_sector_rule
  actual_operator_handle
  actual_operator_formula_or_action_EL_reference
  domain
  codomain
  epsilon_0_1_meaning
  coefficients_and_normalization
  Q_projector_relation
  principal_symbol_or_sufficient_first_order_data
  family_or_branch_identity
  typed_D_roll_comparison_policy
  target_import_screen
  rollback_condition
```

The minimum fields before `DGU01SameOperatorWitness_V1` can even be evaluated
are:

| field | why it is required before same-operator work |
|---|---|
| `source_scope_id` | Declares the source domain being admitted or rejected. |
| `source_id` | Names the primary source, not a reconstruction artifact. |
| `exact_locator` | Makes the row auditable at a page, timestamp, equation, frame, or byte range. |
| `source_row_payload` | Supplies the actual source-emitted content; this is the first content-bearing blocker. |
| `extraction_method_to_D_GU_epsilon_0_1_sector_rule` | Prevents reading typed `D_roll` back into the source row. |
| `extracted_sector_rule` | States what source row actually says about the 0/1 sector. |
| `actual_operator_handle` | Gives `DGU01SameOperatorWitness_V1.primary_row_operator_handle` a left-hand side. |
| `epsilon_0_1_meaning` | Locks conventions before any comparison can be meaningful. |
| `coefficients_and_normalization` | Prevents post-comparison rescaling or target fitting. |
| `typed_D_roll_comparison_policy` | Allows typed `D_roll` only as a right-side screen. |
| `target_import_screen` | Records that the row was not manufactured from VZ or typed-spine targets. |

The minimum additional fields before a symbol certificate can be evaluated are:

| field | why it is required before symbol work |
|---|---|
| `domain` | Specifies the actual 0/1 input bundle or space. |
| `codomain` | Specifies the actual 0/1 output bundle or space. |
| `Q_projector_relation` | Fixes the relevant `Q_in`, `Q_out`, inclusion, and projection data. |
| `principal_symbol_or_sufficient_first_order_data` | Supplies `sigma_1(D_GU^epsilon)` or enough actual first-order data to compute it. |
| `actual_operator_formula_or_action_EL_reference` | Ties the symbol to the same actual operator handle, not to typed `D_roll` by substitution. |

The minimum additional fields before VZ replay can be evaluated are:

| field or certificate | why it is required before VZ replay |
|---|---|
| accepted `DGU01SameOperatorWitness_V1` | Shows whether the actual row operator is the typed `D_roll` operator or a different branch. |
| accepted source-clean symbol certificate | Prevents replaying typed-spine symbol algebra as if it were source-emitted. |
| fixed nonzero coefficient conditions | Keeps `a`, `b`, `lambda_d`, or their actual replacements from being fitted after the target is known. |
| lower-order and extra first-order term ledger | Shows that omitted source terms do not invalidate the VZ hypotheses. |
| VZ hypothesis checklist for the accepted operator | Separates conditional typed-spine algebra from an admissible proof replay. |

## 5. First Exact Obstruction Or Missing Object

The first exact missing object remains:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload
```

The first downstream missing field is:

```text
DGU01SameOperatorWitness_V1.primary_row_operator_handle
```

The latter cannot be populated independently. It must be extracted from the
accepted primary row through the row-local extraction method. Supplying typed
`D_roll` in this slot would be a target import, not row intake.

## 6. What Would Change If The Hole Closed

If a valid `PrimarySourceDGU01SectorRuleRowInstance_V1` were supplied, the DGU
route would move from blocked intake to a conditional comparison gate:

```text
accepted primary source row
  -> evaluate DGU01SameOperatorWitness_V1
```

If the same-operator witness then showed that the row-extracted actual operator
is typed `D_roll` under locked conventions, the existing typed-spine algebra
would become a candidate screen for symbol-certificate work. It would still not
automatically close VZ replay; the symbol certificate and VZ hypotheses would
need source-clean evaluation for the same accepted operator.

If the actual row operator differed from typed `D_roll`, the result would still
be useful. It would demote typed `D_roll` VZ replay for this branch and force a
new actual-operator symbol computation rather than a proof restart.

## 7. What Would Falsify Or Demote The Route

The route is falsified or demoted at this gate if any of these occurs:

| condition | result |
|---|---|
| The row payload is absent after a declared and complete source-scope search. | Produce a scoped negative primary-row receipt, not a global DGU no-go. |
| The payload is present but the extraction method imports typed `D_roll`, VZ targets, or desired coefficients. | Fail row intake for target import. |
| The row emits only adjacent bosonic, family, or transcript-neighborhood language with no actual 0/1 sector rule. | Keep the evidence adjacent-only; no same-operator witness. |
| The actual operator handle cannot be separated from comparison artifacts. | Keep `DGU01SameOperatorWitness_V1` unevaluable. |
| Domain, codomain, epsilon convention, or normalization can be changed after comparison. | Demote the route for convention instability. |
| The accepted actual operator differs from typed `D_roll`. | Demote typed `D_roll` VZ replay for this branch; compute the actual symbol separately. |
| The symbol data cannot be tied to the same actual operator handle. | Block symbol certificate and VZ replay. |

## 8. Next Meaningful Computation/Proof/Check

The next useful step is not VZ replay. It is a primary-row intake build or a
narrow negative receipt:

```text
Build PrimarySourceDGU01SectorRuleRowInstance_V1 for a named source scope.
```

The check should:

1. Declare `source_scope_id`, source surfaces, and query/notation variants.
2. Capture the exact row payload with a locator and integrity note.
3. Extract the source-emitted `D_GU^epsilon` 0/1 sector rule without using
   typed `D_roll` as an input.
4. Assign the actual operator handle, domain, codomain, epsilon convention,
   coefficients, Q/projector relation, and first-order or symbol data.
5. Run the target-import screen.
6. Only then evaluate `DGU01SameOperatorWitness_V1`.

If no row is found, the output should list exact inspected windows and absence
claims. It should not restart the VZ proof and should not claim a global DGU
failure.

## 9. Claim-Status Consistency Result

No claim status changes. No source row, same-operator witness, symbol
certificate, VZ replay, physical recovery replay, or proof restart is admitted.
The claim-status consistency workflow is not triggered by this artifact because
the result preserves the existing blocked/no-restart state.

## 10. JSON Summary

```json
{
  "artifact_id": "DGUPrimaryRowIntakeReadiness_0301_C1_DGU_V1",
  "run_id": "hourly-20260626-0301",
  "cycle": 1,
  "lane": "DGU",
  "artifact_path": "explorations/hourly-20260626-0301-cycle1-dgu-primary-row-intake-readiness.md",
  "verdict_class": "blocked_primary_row_instance_not_intake_ready",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "proof_restart_allowed": false,
  "typed_d_roll_available_as_screen": true,
  "typed_d_roll_allowed_as_source_row": false,
  "primary_row_instance_found": false,
  "primary_row_payload_found": false,
  "row_extraction_method_found": false,
  "actual_operator_handle_found": false,
  "intake_ready_for_same_operator_witness": false,
  "intake_ready_for_symbol_certificate": false,
  "intake_ready_for_vz_replay": false,
  "first_missing_field": "PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload",
  "first_missing_downstream_field": "DGU01SameOperatorWitness_V1.primary_row_operator_handle",
  "required_fields_before_same_operator_witness": [
    "source_scope_id",
    "source_id",
    "exact_locator",
    "source_row_payload",
    "extraction_method_to_D_GU_epsilon_0_1_sector_rule",
    "extracted_sector_rule",
    "actual_operator_handle",
    "epsilon_0_1_meaning",
    "coefficients_and_normalization",
    "typed_D_roll_comparison_policy",
    "target_import_screen"
  ],
  "required_fields_before_symbol_certificate": [
    "domain",
    "codomain",
    "Q_projector_relation",
    "principal_symbol_or_sufficient_first_order_data",
    "actual_operator_formula_or_action_EL_reference"
  ],
  "required_fields_before_vz_replay": [
    "accepted_DGU01SameOperatorWitness_V1",
    "accepted_source_clean_symbol_certificate",
    "fixed_nonzero_coefficient_conditions",
    "lower_order_and_extra_first_order_term_ledger",
    "VZ_hypothesis_checklist_for_accepted_operator"
  ],
  "constructive_next_object": "PrimarySourceDGU01SectorRuleRowInstance_V1",
  "next_meaningful_step": "Build a primary-row intake packet for a named source scope, or produce a scoped negative primary-row receipt with exact inspected windows."
}
```
