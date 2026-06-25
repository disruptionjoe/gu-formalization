---
title: "Hourly 20260625 1802 Cycle 1 IG Raw Formal D7 Branching Transcript"
date: "2026-06-25"
run_id: "hourly-20260625-1802"
cycle: 1
lane: 2
doc_type: ig_raw_formal_d7_branching_transcript
artifact_id: "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_1802_C1_L2_V1"
verdict: "BLOCKED_NO_ADMISSIBLE_RAW_OR_FORMAL_D7_TRANSCRIPT"
owned_path: "explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md"
companion_audit: "tests/hourly_20260625_1802_cycle1_ig_raw_formal_d7_branching_transcript_audit.py"
---

# Hourly 20260625 1802 Cycle 1 IG Raw Formal D7 Branching Transcript

## 1. Verdict

Verdict: **blocked**.

This lane attempted to admit a raw CAS transcript or formal D7 branching proof
for the Shiab Hom-space gate:

```text
IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE
```

No admissible transcript or proof is present in the read sources or available
local tool surface. The 1702 finite-data gate remains the controlling blocker:
product B still lacks a full summand/multiplicity/dimension table for
`V(omega_2) tensor V(omega_6)`, and product A still lacks the kernel/cokernel
and highest-weight packet for
`c: V(omega_1) tensor V(omega_7) -> V(omega_6)`.

Admission decision:

```text
transcript_admitted: false
accepted_receipt_count: 0
product_b_full_table_admitted: false
product_a_kernel_packet_admitted: false
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
proof_restart_allowed: false
no_target_import: true
```

This is not a no-go against the IG route. It is a strict receipt/proof-object
block. Shiab existence and chirality exclusions remain narrow positives, but
they do not supply the full finite D7 transcript.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md` and the frontier runbooks:

- compatibility is not derivation;
- hosted existence is not source-natural selector identity;
- target generation count, desired uniqueness, and downstream GU success cannot
  be used as representation-theory evidence;
- a blocked lane must name the first exact missing proof/source object and the
  constructive object that would remove it.

From `canon/shiab-existence-cl95.md`:

- the current canon works in signature `(9,5)`;
- `Cl(9,5) ~= M(64,H)` and `S = H^64`;
- the real Clifford contraction exists as
  `Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S`;
- this proves existence of at least one natural real-linear equivariant map, but
  explicitly does not prove injectivity, uniqueness, generation count, or the
  full Hom-space dimension.

From the 1702 cycle 1 and cycle 2 IG artifacts:

- D7 conventions are fixed:
  `omega_1 = vector`, `omega_2 = two-form/adjoint`,
  `omega_6 = positive half-spin`, `omega_7 = negative half-spin`;
- product A is `V(omega_1) tensor V(omega_7)`;
- product B is `V(omega_2) tensor V(omega_6)`;
- two product B rival rows are excluded by chirality:
  `V(omega_7)` and `V(omega_1 + omega_7)`;
- those two exclusions are not the full product B table and do not decide
  `FC-MULT`;
- no raw CAS transcript or formal D7 branching proof was admitted at 1702.

From `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`:

- the strongest old construction is a reconstruction-grade chirality and
  gamma-trace skeleton;
- it gives expected LiE commands rather than raw output;
- it explicitly keeps OQ-CG-2 open and says a LiE/Sage computation should list
  all summands of `V(omega_2) tensor V(omega_6)`;
- its own correction leaves `FC-IRR`, `FC-MULT`, and `FC-HW` open.

Local tool probe for this lane found Python only. `sage`, `SageMath`, `LiE`,
`lie`, `gap`, `sympy`, `sage`, and `sageall` were not available, so this lane did
not generate a new accepted CAS receipt.

## 3. The strongest positive construction attempt

The strongest positive construction remains:

```text
ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1
```

It gives a real positive skeleton:

- the Shiab contraction exists in the `Cl(9,5)` canon;
- the D7 convention and two tensor products are fixed;
- the gamma-trace map identifies a candidate product A branch;
- chirality excludes `V(omega_7)` and `V(omega_1 + omega_7)` from product B.

This construction is not admissible as the requested transcript because it lacks
the finite rows that a transcript receipt must contain. In particular, it does
not list every product B summand, multiplicity, dimension, or total dimension
check, and it does not prove the product A kernel decomposition or highest
weight.

## 4. First exact obstruction or missing proof/source object

The first exact obstruction is:

```text
ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6
```

This blocks `FC-MULT` first. Without the complete product B table, the route
cannot decide whether `V(omega_6)` occurs with multiplicity exactly one in
`V(omega_2) tensor V(omega_6)`. Chirality excludes two named wrong-chirality
rows, but it does not rule out all same-chirality summands, extra copies, or
missing dimension mass.

The second missing packet is:

```text
ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6
```

This blocks `FC-IRR` and `FC-HW`: the repo has the candidate map
`c: V(omega_1) tensor V(omega_7) -> V(omega_6)`, but does not admit a formal or
raw-transcript proof of the kernel branch, cokernel branch, irreducibility, or
highest weight.

## 5. The constructive next object that would remove or test the obstruction

Create:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

A valid receipt must contain either raw CAS provenance or a formal proof source:

```text
source/provenance:
  root system D7 and omega convention
  raw CAS tool name, version, invocation, commands, and raw output
  OR formal D7 branching proof with equivalent finite data

product A:
  expression: V(omega_1) tensor V(omega_7)
  full summand list
  multiplicities for every summand
  dimensions for every summand
  total dimension check = 14 * 64 = 896
  map c: A -> V(omega_6)
  kernel branch and cokernel branch
  irreducibility of ker(c), or full kernel decomposition
  highest weight of ker(c), or corrected weight with recomputation

product B:
  expression: V(omega_2) tensor V(omega_6)
  full summand list
  multiplicities for every summand
  dimensions for every summand
  total dimension check = 91 * 64 = 5824
  multiplicity of V(omega_6)
  presence/absence of V(omega_7)
  presence/absence of V(omega_1 + omega_7)
  full rival-row presence/absence checks

verdicts:
  FC-IRR
  FC-MULT
  FC-HW
  rival selector exclusion status
  explicit no-target-import statement
```

The acceptance-critical computation is product B:

```text
decompose V([0,1,0,0,0,0,0]) tensor V([0,0,0,0,0,1,0])
```

Product A must also be supplied before a proof restart:

```text
decompose V([1,0,0,0,0,0,0]) tensor V([0,0,0,0,0,0,1])
```

## 6. What this means for IG selector/family identity and proof restart

For the IG selector route:

```text
Shiab existence: admitted narrow positive
D7 convention: admitted narrow positive
two chirality exclusions: admitted narrow positive
raw/formal D7 transcript: absent
product B full table: absent
product A kernel packet: absent
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
K_IG family identity: not verified
proof restart: forbidden
```

The `K_IG` selector/family identity cannot be promoted or replayed from the
current materials. If product B later returns multiplicity greater than one for
`V(omega_6)`, the current uniqueness branch fails unless a separate
source-natural discriminator is supplied. If product B returns multiplicity one
with a complete dimension check, the next sequential task is still product A's
kernel/cokernel/highest-weight packet.

## 7. Next meaningful proof or computation step

Run a D7-capable representation computation in LiE, SageMath, GAP with an
appropriate package, Magma, or write a formal D7 proof that produces the same
finite data. The first machine-checkable output should be the full product B
table with dimensions summing to `5824`, followed by the product A packet with
dimensions summing to `896`.

Do not start `K_IG` family identity, rival-row elimination, or GU proof replay
until `transcript_admitted` is true.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_1802_C1_L2_V1",
  "artifact_id": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_1802_C1_L2_V1",
  "artifact_path": "explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md",
  "owned_path": "explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md",
  "companion_audit": "tests/hourly_20260625_1802_cycle1_ig_raw_formal_d7_branching_transcript_audit.py",
  "decision_target": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
  "run_id": "hourly-20260625-1802",
  "cycle": 1,
  "lane": 2,
  "verdict": "BLOCKED_NO_ADMISSIBLE_RAW_OR_FORMAL_D7_TRANSCRIPT",
  "verdict_class": "blocked",
  "transcript_admitted": false,
  "accepted_transcript": false,
  "accepted_receipt_count": 0,
  "accepted_selector_count": 0,
  "raw_CAS_transcript_present": false,
  "raw_CAS_transcript_admitted": false,
  "formal_D7_branching_proof_present": false,
  "formal_D7_branching_proof_admitted": false,
  "product_b_full_table_admitted": false,
  "product_a_kernel_packet_admitted": false,
  "proof_restart_allowed": false,
  "no_target_import": true,
  "target_import_used": false,
  "target_physics_used": false,
  "desired_generation_count_used": false,
  "desired_uniqueness_used": false,
  "claim_promotion_allowed": false,
  "major_GU_claim_promoted": false,
  "selector_theorem_closed": false,
  "K_IG_family_identity_verified": false,
  "full_rival_row_elimination_completed": false,
  "local_tool_probe": {
    "python": "present",
    "sage": "not_found",
    "SageMath": "not_found",
    "LiE": "not_found",
    "lie": "not_found",
    "gap": "not_found",
    "sympy": "not_found",
    "sageall": "not_found"
  },
  "directly_derived_repo_results": [
    "Cl_9_5_Shiab_contraction_exists",
    "Shiab_existence_does_not_establish_uniqueness_or_generation_count",
    "D7_weight_convention_specified",
    "product_A_is_V_omega1_tensor_V_omega7",
    "product_B_is_V_omega2_tensor_V_omega6",
    "chirality_excludes_V_omega7_from_product_B",
    "chirality_excludes_V_omega1_plus_omega7_from_product_B",
    "older_SC1_OQ1A_material_is_reconstruction_grade_or_expected_output_not_raw_transcript",
    "1702_cycle2_identified_product_B_full_table_as_first_obstruction"
  ],
  "strongest_positive_construction_attempt": "ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1",
  "accepted_narrow_positives": [
    "Cl_9_5_Shiab_contraction_exists",
    "D7_weight_convention_specified",
    "chirality_excludes_V_omega7_from_product_B",
    "chirality_excludes_V_omega1_plus_omega7_from_product_B"
  ],
  "first_obstruction": "ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6",
  "first_missing_proof_source_object": "FullBProductD7SummandMultiplicityDimensionTranscriptForShiabHomSpace_V1",
  "second_missing_proof_source_object": "ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6",
  "constructive_next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "next_meaningful_step": "Produce_raw_LiE_Sage_GAP_Magma_output_or_formal_D7_branching_proof_for_product_B_then_product_A_with_full_summands_multiplicities_dimensions_dimension_checks_kernel_cokernel_highest_weight_and_FC_verdicts.",
  "fc_irr": "blocked",
  "fc_mult": "blocked",
  "fc_hw": "blocked",
  "FC_IRR_status": "blocked",
  "FC_MULT_status": "blocked",
  "FC_HW_status": "blocked",
  "FC_IRR_verdict": "blocked_missing_product_A_kernel_irreducibility_or_full_decomposition",
  "FC_MULT_verdict": "blocked_missing_product_B_full_summand_multiplicity_dimension_table_and_multiplicity_of_V_omega6",
  "FC_HW_verdict": "blocked_missing_product_A_kernel_highest_weight_or_corrected_weight",
  "all_FC_gates_closed": false,
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
  "finite_rows_missing": [
    "raw_CAS_tool_version_invocation_commands_output_or_formal_proof_identity",
    "product_B_full_summand_list",
    "product_B_multiplicities",
    "product_B_dimensions",
    "product_B_total_dimension_check",
    "product_B_multiplicity_of_V_omega6",
    "product_B_full_rival_presence_absence_checks",
    "product_A_full_summand_list",
    "product_A_multiplicities",
    "product_A_dimensions",
    "product_A_total_dimension_check",
    "product_A_kernel_branch",
    "product_A_cokernel_branch",
    "product_A_kernel_irreducibility_or_full_decomposition",
    "product_A_kernel_highest_weight_or_corrected_weight",
    "FC_IRR_verdict_receipt",
    "FC_MULT_verdict_receipt",
    "FC_HW_verdict_receipt"
  ],
  "valid_transcript_receipt_must_contain": [
    "root_system_D7_and_omega_convention",
    "raw_CAS_tool_name_version_invocation_commands_raw_output_or_formal_D7_proof",
    "product_A_full_summands_multiplicities_dimensions_total_dimension_check",
    "product_A_kernel_cokernel_branch_for_c_to_V_omega6",
    "product_A_ker_c_irreducibility_or_full_decomposition",
    "product_A_ker_c_highest_weight_or_corrected_weight",
    "product_B_full_summands_multiplicities_dimensions_total_dimension_check",
    "product_B_multiplicity_of_V_omega6",
    "product_B_presence_absence_of_V_omega7_and_V_omega1_plus_omega7",
    "full_rival_row_presence_absence_checks",
    "FC_IRR_FC_MULT_FC_HW_verdicts",
    "explicit_no_target_import_statement"
  ],
  "proof_restart_rule": "proof_restart_allowed_must_be_false_unless_transcript_admitted_is_true"
}
```
