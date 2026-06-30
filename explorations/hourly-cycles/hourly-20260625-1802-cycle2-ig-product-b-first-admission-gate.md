---
title: "Hourly 20260625 1802 Cycle 2 IG Product B First Admission Gate"
date: "2026-06-25"
run_id: "hourly-20260625-1802"
cycle: 2
lane: 2
doc_type: ig_product_b_first_admission_gate
artifact_id: "IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1"
verdict: "BLOCKED_PRODUCT_B_FIRST_REQUIRED_NO_BYPASS"
owned_path: "explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md"
companion_audit: "tests/hourly_20260625_1802_cycle2_ig_product_b_first_admission_gate_audit.py"
---

# Hourly 20260625 1802 Cycle 2 IG Product B First Admission Gate

## 1. Verdict

Verdict: **blocked**.

The IG selector/family identity work cannot bypass the missing Product B full
D7 summand/multiplicity/dimension table. The dependency gate is:

```text
Product B full table first,
then Product A kernel/cokernel/highest-weight packet,
then FC-IRR / FC-MULT / FC-HW,
then any K_IG selector or family-identity proof restart.
```

No bypass is valid from Product A partials, chirality exclusions, desired
multiplicity, or target generation count. Those data can guide the next
computation, but they cannot be admitted as a replacement for the finite D7
receipt.

Admission decision:

```text
product_b_first_required: true
bypass_allowed: false
transcript_admitted: false
accepted_receipt_count: 0
target_generation_count_used: false
proof_restart_allowed: false
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
```

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md`:

- target data must not be hidden inside a reconstruction;
- compatibility is not derivation;
- a blocked route must name the exact proof object that would remove the
  obstruction.

From the five-lane and three-cycle runbooks:

- this lane must make a decision-grade gate call, not a summary;
- blocked, conditional, no-go, host, and import verdicts must not be conflated;
- exact rollback and falsification conditions are part of the artifact.

From `canon/shiab-existence-cl95.md`:

- the current canon admits a real `Cl(9,5)` Shiab/Clifford contraction;
- that canon explicitly does not prove uniqueness, injectivity, selector
  identity, anomaly cancellation, or generation count;
- kernel/rank and equivariant-map multiplicity are open representation-theory
  questions.

From
`explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md`
and its audit:

- no raw CAS transcript or formal D7 proof was admitted;
- accepted receipt count was zero;
- Product B lacks a full table for
  `V(omega_2) tensor V(omega_6)`;
- Product A lacks the kernel/cokernel/highest-weight packet for
  `c: V(omega_1) tensor V(omega_7) -> V(omega_6)`;
- `FC-IRR`, `FC-MULT`, and `FC-HW` remain blocked;
- proof restart is forbidden until an admissible transcript exists.

From
`explorations/hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md`:

- the first obstruction was already identified as the missing Product B full
  summand/multiplicity/dimension table;
- chirality exclusions for two wrong-chirality rows are narrow positives only;
- target generation count and desired uniqueness are not proof data.

## 3. Strongest positive construction attempt

The strongest positive construction is the conditional skeleton:

```text
Cl(9,5) Shiab contraction
+ fixed D7 convention
+ gamma-trace candidate on Product A
+ two Product B chirality exclusions
```

It supplies useful orientation:

- Product A is `V(omega_1) tensor V(omega_7)`;
- Product B is `V(omega_2) tensor V(omega_6)`;
- the candidate Product A map is
  `c: V(omega_1) tensor V(omega_7) -> V(omega_6)`;
- Product B cannot contain the two named wrong-chirality rivals
  `V(omega_7)` and `V(omega_1 + omega_7)`.

This is the best available positive construction because it identifies the
finite products and the relevant Hom-space screen. It still does not admit the
IG selector/family identity. It does not list all Product B summands, their
multiplicities, their dimensions, or a dimension sum. It also does not prove
the Product A kernel, cokernel, irreducibility, or highest weight.

## 4. First exact obstruction/missing proof object

The first exact obstruction is:

```text
ProductBFullSummandMultiplicityDimensionTableFor_V_omega2_tensor_V_omega6
```

This object is first because `FC-MULT` asks a Product B question before Product
A can rescue anything:

```text
Does V(omega_6) occur in V(omega_2) tensor V(omega_6),
and if so, with what multiplicity among the full set of Product B summands?
```

The following attempted bypasses fail:

```text
Product A partials:
  fail, because a candidate map A -> V(omega_6) does not determine the
  multiplicity of V(omega_6) inside B.

Chirality exclusions:
  fail, because excluding V(omega_7) and V(omega_1 + omega_7) does not list
  all same-chirality Product B summands or prove the multiplicity of V(omega_6).

Desired multiplicity:
  fail, because uniqueness cannot be an input to the multiplicity computation.

Target generation count:
  fail, because generation count is downstream target data and is not finite
  D7 branching evidence.
```

The second missing object is:

```text
ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6
```

It is not enough by itself. It becomes the next gate only after Product B's full
table is admitted.

## 5. Constructive next object

The next object must be one of these admissible receipts:

```text
ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

The minimum Product B receipt must contain:

```text
root system: D7
omega convention:
  omega_1 = vector
  omega_2 = two-form/adjoint
  omega_6 = positive half-spin
  omega_7 = negative half-spin
expression:
  V(omega_2) tensor V(omega_6)
required rows:
  every summand
  every multiplicity
  every summand dimension
  total dimension check = 91 * 64 = 5824
  multiplicity of V(omega_6)
  presence/absence of all named rival rows
provenance:
  raw CAS tool/version/invocation/commands/output
  OR formal D7 proof supplying the same finite data
```

After that, but not before, the next object is the Product A packet:

```text
ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6
```

with `V(omega_1) tensor V(omega_7)`, full summands, multiplicities, dimensions,
dimension sum `14 * 64 = 896`, kernel/cokernel branch for `c`, kernel
irreducibility or full decomposition, and highest weight or corrected weight.

## 6. Consequence for IG selector/family identity and proof restart

The IG selector/family identity remains unverified. The current repo admits
only narrow prerequisites:

```text
Shiab existence: present
D7 convention: present
two chirality exclusions: present
Product B full table: absent
Product A kernel packet: absent
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
K_IG selector/family identity: not verified
proof restart: forbidden
```

The proof restart rule is:

```text
No K_IG selector/family identity proof replay is allowed unless
transcript_admitted is true and accepted_receipt_count is at least 1.
```

Rollback and falsification conditions:

- If a later Product B receipt has dimension sum different from `5824`, reject
  that receipt or correct the D7 convention before using it.
- If Product B has no `V(omega_6)` row, the current selector branch fails.
- If Product B has multiplicity greater than one for `V(omega_6)`, the
  uniqueness branch fails unless a separate source-natural discriminator is
  supplied.
- If Product B is clean but Product A lacks the required kernel/cokernel and
  highest-weight packet, the route remains blocked at Product A.
- If any route uses target generation count, desired multiplicity, or downstream
  family identity as representation-theory evidence, mark it as target import
  and reject the proof restart.

## 7. Next proof/source step

Produce the Product B finite transcript first:

```text
decompose V([0,1,0,0,0,0,0]) tensor V([0,0,0,0,0,1,0])
```

The acceptable source is raw output from a D7-capable tool such as LiE,
SageMath, GAP with an appropriate package, Magma, or a formal D7 branching
proof that supplies the same finite data. Only after Product B is admitted
should the run spend proof-restart effort on:

```text
decompose V([1,0,0,0,0,0,0]) tensor V([0,0,0,0,0,0,1])
```

and the Product A kernel/cokernel/highest-weight packet.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1",
  "artifact_id": "IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1",
  "artifact_path": "explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md",
  "owned_path": "explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md",
  "companion_audit": "tests/hourly_20260625_1802_cycle2_ig_product_b_first_admission_gate_audit.py",
  "decision_target": "IG_PRODUCT_B_FIRST_ADMISSION_GATE",
  "run_id": "hourly-20260625-1802",
  "cycle": 2,
  "lane": 2,
  "verdict": "BLOCKED_PRODUCT_B_FIRST_REQUIRED_NO_BYPASS",
  "verdict_class": "blocked",
  "product_b_first_required": true,
  "bypass_allowed": false,
  "transcript_admitted": false,
  "accepted_transcript": false,
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "target_generation_count_used": false,
  "target_import_used": false,
  "target_physics_used": false,
  "desired_multiplicity_used": false,
  "desired_uniqueness_used": false,
  "product_a_partials_bypass_allowed": false,
  "chirality_exclusions_bypass_allowed": false,
  "desired_multiplicity_bypass_allowed": false,
  "target_generation_count_bypass_allowed": false,
  "product_b_full_table_admitted": false,
  "product_a_kernel_packet_admitted": false,
  "FC_IRR_status": "blocked",
  "FC_MULT_status": "blocked",
  "FC_HW_status": "blocked",
  "fc_irr": "blocked",
  "fc_mult": "blocked",
  "fc_hw": "blocked",
  "all_FC_gates_closed": false,
  "K_IG_family_identity_verified": false,
  "selector_theorem_closed": false,
  "claim_promotion_allowed": false,
  "major_GU_claim_promoted": false,
  "dependency_gate_order": [
    "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1",
    "ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6",
    "FC_IRR_FC_MULT_FC_HW_verdicts",
    "K_IG_selector_family_identity_proof_restart"
  ],
  "strongest_positive_construction_attempt": "ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1",
  "accepted_narrow_positives": [
    "Cl_9_5_Shiab_contraction_exists",
    "D7_weight_convention_specified",
    "chirality_excludes_V_omega7_from_product_B",
    "chirality_excludes_V_omega1_plus_omega7_from_product_B"
  ],
  "bypass_tests": [
    {
      "route": "Product_A_partials",
      "allowed": false,
      "reason": "Product_A_map_or_kernel_information_does_not_determine_multiplicity_of_V_omega6_inside_Product_B"
    },
    {
      "route": "chirality_exclusions",
      "allowed": false,
      "reason": "Two_wrong_chirality_exclusions_do_not_supply_full_Product_B_summands_multiplicities_dimensions_or_same_chirality_rival_checks"
    },
    {
      "route": "desired_multiplicity",
      "allowed": false,
      "reason": "Desired_uniqueness_cannot_be_used_as_input_to_the_D7_multiplicity_computation"
    },
    {
      "route": "target_generation_count",
      "allowed": false,
      "reason": "Generation_count_is_downstream_target_data_not_finite_D7_branching_evidence"
    }
  ],
  "first_obstruction": "ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6",
  "first_missing_proof_object": "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1",
  "second_missing_proof_object": "ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6",
  "next_object": "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1_or_RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "constructive_next_object": "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1_or_RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "product_B": {
    "expression": "V(omega_2) tensor V(omega_6)",
    "expected_total_dimension": 5824,
    "full_summand_list_admitted": false,
    "multiplicities_admitted": false,
    "dimensions_admitted": false,
    "total_dimension_check_admitted": false,
    "multiplicity_of_V_omega6_admitted": false,
    "V_omega7_absence_chirality_excluded": true,
    "V_omega1_plus_omega7_absence_chirality_excluded": true,
    "full_rival_presence_absence_admitted": false
  },
  "product_A": {
    "expression": "V(omega_1) tensor V(omega_7)",
    "expected_total_dimension": 896,
    "full_summand_list_admitted": false,
    "multiplicities_admitted": false,
    "dimensions_admitted": false,
    "total_dimension_check_admitted": false,
    "kernel_branch_admitted": false,
    "cokernel_branch_admitted": false,
    "ker_c_irreducibility_admitted": false,
    "ker_c_highest_weight_admitted": false
  },
  "valid_product_b_receipt_must_contain": [
    "root_system_D7_and_omega_convention",
    "raw_CAS_tool_name_version_invocation_commands_raw_output_or_formal_D7_proof",
    "product_B_full_summand_list",
    "product_B_multiplicities",
    "product_B_dimensions",
    "product_B_total_dimension_check_5824",
    "product_B_multiplicity_of_V_omega6",
    "full_named_rival_presence_absence_checks",
    "explicit_no_target_import_statement"
  ],
  "rollback_or_falsification_conditions": [
    "reject_or_correct_receipt_if_product_B_dimension_sum_is_not_5824",
    "current_selector_branch_fails_if_product_B_has_no_V_omega6_row",
    "uniqueness_branch_fails_if_product_B_multiplicity_of_V_omega6_is_greater_than_one_without_source_natural_discriminator",
    "route_remains_blocked_if_product_A_packet_is_missing_after_product_B_is_admitted",
    "reject_proof_restart_if_target_generation_count_or_desired_multiplicity_is_used_as_representation_theory_evidence"
  ],
  "proof_restart_rule": "proof_restart_allowed_must_be_false_unless_transcript_admitted_is_true_and_accepted_receipt_count_is_at_least_1",
  "next_proof_source_step": "Produce_Product_B_full_D7_table_or_raw_formal_D7_transcript_receipt_before_Product_A_packet_and_before_any_FC_or_K_IG_restart."
}
```
