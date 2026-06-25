---
title: "Hourly 20260625 1602 Cycle 2 IG Raw Formal D7 Branching Transcript Admission"
date: "2026-06-25"
run_id: "hourly-20260625-1602"
cycle: 2
lane: 2
doc_type: ig_raw_formal_d7_branching_transcript_admission
artifact_id: "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_ADMISSION_1602_C2_L2_V1"
verdict: "BLOCKED_NO_ADMISSIBLE_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT"
owned_path: "explorations/hourly-20260625-1602-cycle2-ig-raw-formal-d7-branching-transcript-admission.md"
companion_audit: "tests/hourly_20260625_1602_cycle2_ig_raw_formal_d7_branching_transcript_admission_audit.py"
---

# Hourly 20260625 1602 Cycle 2 IG Raw Formal D7 Branching Transcript Admission

## 1. Verdict

Verdict: **blocked**.

The current repo does not supply an admissible raw CAS transcript or formal D7
branching proof for:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

The repo does supply narrow positive evidence: the Shiab/Clifford contraction is
typed in the `Cl(9,5)` setting, and chirality excludes `V(omega_7)` and
`V(omega_1 + omega_7)` from `V(omega_2) tensor V(omega_6)`. Those positives are
not enough to admit the transcript because they do not close `FC-IRR`,
`FC-MULT`, or `FC-HW`.

Admission decision:

```text
accepted_receipt_count: 0
accepted_selector_count: 0
raw_CAS_transcript_admitted: false
formal_D7_branching_proof_admitted: false
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
target_import_used: false
proof_restart_allowed: false
```

This is not a no-go against the IG route. It is an admission gate saying the
finite D7 proof/transcript object is still absent.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md` and the frontier runbooks:

- compatibility is not derivation;
- a hosted map is not a selected source-natural map;
- target physics, generation count, or desired uniqueness cannot choose the
  selector;
- a blocked lane must name the first exact missing proof object and a constructive
  next object.

From `explorations/hourly-20260625-1602-cycle1-ig-d7-proof-transcript-object.md`:

- no formal D7 branching proof object or raw CAS transcript was present at cycle
  1;
- the relevant missing object was named as
  `VerifiedMultiplicityIrreducibilityAndHighestWeightD7PacketForShiabHomSpace_V1`;
- the constructive next object was exactly
  `RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1`;
- the accepted receipt count and selector count remained zero.

From `tests/hourly_20260625_1602_cycle1_ig_d7_proof_transcript_object_audit.py`:

- the prior artifact's machine-readable contract required no accepted receipt,
  no target import, no proof restart, explicit missing multiplicity,
  irreducibility, highest-weight, and dimension data, and a named next object.

From `explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md`:

- a hand proof is allowed in principle, but it must supply the same finite data
  as a CAS transcript;
- chirality-only and reconstruction-grade arguments are rejected as admission
  bases;
- full summand lists, multiplicities, highest-weight data, irreducibility data,
  and dimension checks are required.

From repo search in this lane:

- the active D7 references still point back to `sc1-oq1a-d7-clebsch-gordan-cas`
  and the 1302/1503/1602 IG audit artifacts;
- the visible LiE/Sage material is pseudocode or a required future computation,
  not raw command output;
- no file was found that upgrades the current D7 packet to an admitted raw or
  formal transcript.

## 3. Strongest positive current candidate

The strongest positive current candidate is:

```text
ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1
```

It contains the following admissible narrow positives:

- `Cl(9,5)` Shiab/Clifford contraction exists and is typed as
  `Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S`;
- the D7 convention is fixed with `omega_1` vector, `omega_2` two-form/adjoint,
  `omega_6` positive half-spin, and `omega_7` negative half-spin;
- chirality excludes `V(omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- chirality excludes `V(omega_1 + omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- the expected finite computation is small and exactly stated.

Why it is not admitted:

- it does not give the full summand list for
  `V(omega_1) tensor V(omega_7)`;
- it does not prove irreducibility of `ker(c)` or give a full kernel
  decomposition;
- it does not give the full summand list for
  `V(omega_2) tensor V(omega_6)`;
- it does not prove the multiplicity of `V(omega_6)` in the second product;
- it does not provide dimensions for every reported summand;
- it does not close `FC-IRR`, `FC-MULT`, or `FC-HW`.

## 4. Required transcript/proof fields for FC-IRR, FC-MULT, FC-HW

An admitted `RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1` must contain
all of the following finite-data fields.

```text
root_and_convention:
  root_system: D7
  omega_1: vector
  omega_2: two-form_adjoint
  omega_6: positive_half_spin
  omega_7: negative_half_spin

provenance:
  either raw CAS tool name, version, invocation, commands, and raw output;
  or a formal D7 branching/highest-weight proof with the same finite data.

product_A:
  A = V(omega_1) tensor V(omega_7)
  full summand list
  multiplicities for all summands
  dimensions for all summands
  total dimension check
  multiplicity of V(omega_6)
  kernel decomposition for c: A -> V(omega_6)

product_B:
  B = V(omega_2) tensor V(omega_6)
  full summand list
  multiplicities for all summands
  dimensions for all summands
  total dimension check
  multiplicity of V(omega_6)
  presence or absence of V(omega_7)
  presence or absence of V(omega_1 + omega_7)

FC-IRR:
  prove ker(c) is irreducible, or report its full reducible decomposition and
  recompute the common-summand intersection.

FC-MULT:
  prove the multiplicity of V(omega_6) in B and show that every other B summand
  is accounted for.

FC-HW:
  prove the highest weight of ker(c), expected but not admitted as
  omega_1 + omega_7, or report the corrected weight and recompute the gate.

firewall:
  no target generation count, desired selector uniqueness, or downstream physics
  success is used as evidence.
```

## 5. Candidate decision matrix

| Candidate | Positive evidence | Missing admission fields | Decision |
| --- | --- | --- | --- |
| `Cl(9,5)` Shiab existence | typed contraction exists | no D7 full summand lists, no multiplicities, no irreducibility, no highest weight | rejected as full transcript basis |
| Chirality exclusions | excludes `V(omega_7)` and `V(omega_1 + omega_7)` from `B` | no multiplicity of `V(omega_6)`, no full `A`, no full `B`, no dimensions | rejected as chirality-only admission basis |
| SC1/OQ1A pseudocode | names LiE/Sage commands and expected audit target | no raw output, no version, no complete transcript | rejected as raw CAS receipt |
| 1503 formal admission skeleton | states proof obligations exactly | does not itself prove the obligations | rejected as formal proof receipt |
| 1602 cycle 1 transcript object | names next object and required fields | records absence of the object | rejected as admission receipt |

Current accepted receipt count: `0`.

## 6. First exact obstruction

The first exact obstruction is:

```text
No candidate supplies the full summand list with multiplicities and dimensions
for B = V(omega_2) tensor V(omega_6).
```

This obstruction hits `FC-MULT` first. Because `FC-MULT` is missing, the route
cannot prove that the shared `V(omega_6)` copy is unique inside the codomain
product. Even if chirality excludes two rival summands, the Hom-space dimension
cannot be admitted until every summand of `B` is listed and the multiplicity of
`V(omega_6)` is proved.

The same missing packet also blocks:

- `FC-IRR`, because `ker(c)` in
  `V(omega_1) tensor V(omega_7) -> V(omega_6)` is not proved irreducible or
  fully decomposed;
- `FC-HW`, because the highest weight of `ker(c)` is not admitted by a formal
  highest-weight proof or raw transcript.

## 7. Impact on K_IG selector, proof restart, and GU claim

For `K_IG`:

```text
D7 transcript admitted: false
K_IG family identity verified: false
full rival-row elimination completed: false
selector theorem closed: false
accepted_selector_count: 0
proof_restart_allowed: false
```

The selector proof may not restart from the current evidence. Chirality and Shiab
existence remain useful inputs, but they are not a selector theorem.

For the GU claim:

- no major GU claim is promoted by this lane;
- the IG route remains a conditional route with a finite proof/transcript blocker;
- the result strengthens the promotion firewall by separating chirality/narrow
  positives from full selector-theorem admission;
- failure of a later transcript is still informative: if `V(omega_6)` appears
  with multiplicity greater than one in `B`, the present uniqueness branch must
  fail or add a stronger source-natural discriminator.

## 8. Next meaningful proof/computation step

Create the next object:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

The most direct computation is:

```text
decompose V([1,0,0,0,0,0,0]) tensor V([0,0,0,0,0,0,1])
decompose V([0,1,0,0,0,0,0]) tensor V([0,0,0,0,0,1,0])
```

The output must include tool/version/provenance, raw commands or formal proof
steps, full summand lists, multiplicities, dimensions, total dimension checks,
and explicit verdicts for `FC-IRR`, `FC-MULT`, and `FC-HW`.

## 9. Machine-readable JSON summary

```json
{
  "artifact": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_ADMISSION_1602_C2_L2_V1",
  "artifact_id": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_ADMISSION_1602_C2_L2_V1",
  "run_id": "hourly-20260625-1602",
  "cycle": 2,
  "lane": 2,
  "verdict": "BLOCKED_NO_ADMISSIBLE_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1602-cycle2-ig-raw-formal-d7-branching-transcript-admission.md",
  "companion_audit": "tests/hourly_20260625_1602_cycle2_ig_raw_formal_d7_branching_transcript_admission_audit.py",
  "decision_target": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "accepted_receipt_count": 0,
  "accepted_selector_count": 0,
  "raw_CAS_transcript_admitted": false,
  "formal_D7_branching_proof_admitted": false,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "target_physics_used": false,
  "claim_promotion_allowed": false,
  "selector_theorem_closed": false,
  "K_IG_family_identity_verified": false,
  "full_rival_row_elimination_completed": false,
  "all_FC_gates_closed": false,
  "strongest_positive_current_candidate": "ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1",
  "accepted_narrow_positives": [
    "Cl_9_5_Shiab_contraction_exists",
    "D7_weight_convention_specified",
    "chirality_excludes_V_omega7_from_V_omega2_tensor_V_omega6",
    "chirality_excludes_V_omega1_plus_omega7_from_V_omega2_tensor_V_omega6"
  ],
  "required_fields": [
    "root_system_D7_convention",
    "raw_CAS_or_formal_proof_provenance",
    "A_full_summand_list_for_V_omega1_tensor_V_omega7",
    "A_multiplicities_for_all_summands",
    "A_dimensions_for_all_summands",
    "A_total_dimension_check",
    "B_full_summand_list_for_V_omega2_tensor_V_omega6",
    "B_multiplicities_for_all_summands",
    "B_dimensions_for_all_summands",
    "B_total_dimension_check",
    "multiplicity_of_V_omega6_in_A",
    "multiplicity_of_V_omega6_in_B",
    "irreducibility_of_ker_c_or_full_kernel_decomposition",
    "highest_weight_of_ker_c_or_corrected_weight",
    "presence_absence_of_V_omega7_in_B",
    "presence_absence_of_V_omega1_plus_omega7_in_B",
    "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW",
    "no_target_physics_or_desired_uniqueness_used"
  ],
  "missing_fields": [
    "raw_CAS_tool_version_invocation_and_output",
    "formal_D7_branching_proof",
    "A_full_summand_list_for_V_omega1_tensor_V_omega7",
    "A_multiplicities_for_all_summands",
    "A_dimensions_for_all_summands",
    "A_total_dimension_check",
    "B_full_summand_list_for_V_omega2_tensor_V_omega6",
    "B_multiplicities_for_all_summands",
    "B_dimensions_for_all_summands",
    "B_total_dimension_check",
    "multiplicity_of_V_omega6_in_B",
    "irreducibility_of_ker_c_or_full_kernel_decomposition",
    "highest_weight_of_ker_c_or_corrected_weight",
    "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW"
  ],
  "FC_IRR_status": "blocked_missing_irreducibility_proof_or_full_kernel_decomposition",
  "FC_MULT_status": "blocked_missing_full_summand_list_multiplicities_dimensions_for_B_and_multiplicity_of_V_omega6",
  "FC_HW_status": "blocked_missing_highest_weight_proof_or_raw_transcript_for_ker_c",
  "candidate_rows": [
    {
      "candidate": "Cl_9_5_Shiab_existence",
      "positive_evidence": "typed_Shiab_Clifford_contraction_exists",
      "decision": "rejected_as_full_transcript_basis",
      "reason": "no_D7_full_summand_lists_multiplicities_irreducibility_highest_weight_or_dimensions"
    },
    {
      "candidate": "chirality_exclusions",
      "positive_evidence": "excludes_V_omega7_and_V_omega1_plus_omega7_from_B",
      "decision": "rejected_as_chirality_only_admission_basis",
      "reason": "does_not_prove_multiplicity_of_V_omega6_or_full_A_B_decompositions"
    },
    {
      "candidate": "SC1_OQ1A_LiE_Sage_pseudocode",
      "positive_evidence": "names_relevant_commands_and_expected_computation",
      "decision": "rejected_as_raw_CAS_receipt",
      "reason": "pseudocode_not_raw_output_no_version_no_complete_transcript"
    },
    {
      "candidate": "1503_formal_admission_skeleton",
      "positive_evidence": "states_required_proof_obligations",
      "decision": "rejected_as_formal_proof_receipt",
      "reason": "obligations_are_not_proved"
    },
    {
      "candidate": "1602_cycle1_transcript_object",
      "positive_evidence": "names_required_next_object_and_fields",
      "decision": "rejected_as_admission_receipt",
      "reason": "records_absence_of_raw_or_formal_transcript"
    }
  ],
  "chirality_only_rejected_as_admission_basis": true,
  "first_obstruction": "No_candidate_supplies_the_full_summand_list_with_multiplicities_and_dimensions_for_B_equals_V_omega2_tensor_V_omega6",
  "next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "next_meaningful_step": "Produce_raw_LiE_Sage_CAS_output_or_a_formal_D7_branching_proof_for_the_two_required_tensor_products_with_full_summand_lists_multiplicities_dimensions_irreducibility_highest_weight_and_FC_gate_verdicts.",
  "promotion_firewall": {
    "shiab_existence_not_selector_theorem": true,
    "chirality_exclusion_not_full_branching_transcript": true,
    "chirality_only_rejected_as_admission_basis": true,
    "pseudocode_not_raw_CAS_receipt": true,
    "formal_obligation_list_not_formal_proof": true,
    "target_physics_not_used": true,
    "proof_restart_blocked": true,
    "GU_claim_not_promoted": true
  }
}
```
