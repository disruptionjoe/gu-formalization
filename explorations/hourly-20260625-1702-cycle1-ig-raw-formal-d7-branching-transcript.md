---
title: "Hourly 20260625 1702 Cycle 1 IG Raw Formal D7 Branching Transcript"
date: "2026-06-25"
run_id: "hourly-20260625-1702"
cycle: 1
lane: 2
doc_type: ig_raw_formal_d7_branching_transcript
artifact_id: "RawOrFormalD7BranchingTranscriptForShiabHomSpace_1702_C1_L2_V1"
verdict: "BLOCKED_NO_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_CONSTRUCTED"
owned_path: "explorations/hourly-20260625-1702-cycle1-ig-raw-formal-d7-branching-transcript.md"
companion_audit: "tests/hourly_20260625_1702_cycle1_ig_raw_formal_d7_branching_transcript_audit.py"
---

# Hourly 20260625 1702 Cycle 1 IG Raw Formal D7 Branching Transcript

## 1. Verdict

Verdict: **blocked**.

I attempted to construct or admit:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

from the current repo sources and local tool surface. The repo does not contain
an admissible raw CAS transcript or formal D7 branching proof with the finite
data needed to evaluate multiplicity, irreducibility, highest weight,
kernel/cokernel branch, product A/B summands, dimensions, and rival selector
exclusions.

Decision state:

```text
accepted_receipt_count: 0
raw_CAS_transcript_present: false
formal_D7_branching_proof_present: false
local_D7_CAS_tool_available: false
finite_D7_data_complete: false
proof_restart_allowed: false
target_import_used: false
claim_promotion_allowed: false
```

This is not a no-go against the IG/Shiab Hom-space route. It is a strict
admission block: the current repo has chirality exclusions, locator/schema
records, and reconstruction-grade prior arguments, but not the exact proof
object requested by the 1602 dependency DAG.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md` and the frontier runbooks:

- compatibility is not derivation;
- hosted existence is not source-natural selection;
- target physics, desired generation count, or desired uniqueness cannot be used
  as representation-theory evidence;
- a blocked lane must name the first exact missing proof/source object and the
  constructive next object.

From `canon/shiab-existence-cl95.md`:

- the current canon treats `Y^14` in signature `(9,5)`;
- `Cl(9,5) ~= M(64,H)` and `S = H^64`;
- the Shiab/Clifford contraction exists as
  `Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S`;
- Shiab existence explicitly does not prove generation count or uniqueness of
  the equivariant map.

From the 1503 and 1602 IG artifacts:

- the D7 convention is fixed:
  `omega_1 = vector`, `omega_2 = two-form/adjoint`,
  `omega_6 = positive half-spin`, `omega_7 = negative half-spin`;
- chirality excludes `V(omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- chirality excludes `V(omega_1 + omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- prior LiE/Sage references are pseudocode or expected-output sketches, not raw
  output;
- the open finite gates are still `FC-IRR`, `FC-MULT`, and `FC-HW`.

From `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`:

- the strongest old reconstruction note gives a plausible decomposition shape;
- it labels the multiplicity-one and kernel/highest-weight claims as
  reconstruction grade;
- it explicitly names `OQ-CG-2` as requiring LiE/Sage numerical verification;
- it states that a full LiE/Sage computation would enumerate the full
  `V(omega_2) tensor V(omega_6)` decomposition with multiplicities.

Local tool check for this lane found only Python on path; `sage`, `LiE`, `lie`,
and `gap` were not found. Therefore this lane did not generate a new raw D7
transcript.

## 3. The strongest positive result

The strongest positive result is:

```text
ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1
```

It supports the route in the following narrow sense:

- the Shiab contraction exists and is typed over the current `Cl(9,5)` canon;
- the finite D7 products to test are exactly identified;
- the gamma-trace map gives a candidate branch
  `c: V(omega_1) tensor V(omega_7) -> V(omega_6)`;
- chirality excludes two named rival rows from product B:
  `V(omega_7)` and `V(omega_1 + omega_7)`.

This is meaningful positive evidence, but it is not the requested transcript.
It does not list all product B summands, does not prove the multiplicity of
`V(omega_6)` in product B, does not prove the irreducibility or full
decomposition of `ker(c)`, and does not admit the highest weight of `ker(c)`.

## 4. First exact obstruction or missing proof/source object

The first exact obstruction is:

```text
No admitted full B-product D7 branching table:
B = V(omega_2) tensor V(omega_6)
with every summand, multiplicity, dimension, total dimension check, and the
multiplicity of V(omega_6).
```

This blocks `FC-MULT` first. Without the full B table, the lane cannot decide
whether `V(omega_6)` occurs uniquely in the codomain-side product or whether
additional copies or unlisted summands change the Hom-space dimension.

The same missing transcript also leaves the related gates blocked:

- `FC-IRR`: no admitted proof that `ker(c)` in
  `V(omega_1) tensor V(omega_7) -> V(omega_6)` is irreducible, and no accepted
  full kernel decomposition if it is reducible;
- `FC-HW`: no admitted highest-weight proof that `ker(c)` has highest weight
  `omega_1 + omega_7`, and no corrected weight with recomputed intersections;
- rival selector exclusion: chirality excludes two rivals, but full rival-row
  exclusion requires the admitted A/B decompositions and multiplicities.

The first missing proof/source object is therefore:

```text
FullBProductD7SummandMultiplicityDimensionTranscriptForShiabHomSpace_V1
```

as a required component of:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

## 5. Constructive next object that would remove or test the obstruction

Create:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

Minimum accepted fields:

```text
root_and_convention:
  root_system: D7
  omega_1: vector
  omega_2: two-form_adjoint
  omega_6: positive_half_spin
  omega_7: negative_half_spin

proof_source:
  raw CAS transcript with tool name, version, invocation, commands, raw output;
  or formal D7 branching/highest-weight proof with equivalent finite data.

product_A:
  A = V(omega_1) tensor V(omega_7)
  full summand list
  multiplicities for every summand
  dimensions for every summand
  total dimension check
  kernel/cokernel branch for c: A -> V(omega_6)
  irreducibility of ker(c), or full kernel decomposition
  highest weight of ker(c), or corrected weight and recomputation

product_B:
  B = V(omega_2) tensor V(omega_6)
  full summand list
  multiplicities for every summand
  dimensions for every summand
  total dimension check
  multiplicity of V(omega_6)
  presence/absence of V(omega_7)
  presence/absence of V(omega_1 + omega_7)

verdicts:
  FC-IRR
  FC-MULT
  FC-HW
  rival selector exclusion status
  no target physics or desired generation count used
```

The most direct computation remains:

```text
decompose V([1,0,0,0,0,0,0]) tensor V([0,0,0,0,0,0,1])
decompose V([0,1,0,0,0,0,0]) tensor V([0,0,0,0,0,1,0])
```

## 6. What this means for the IG/GU claim

For IG:

```text
Shiab existence: present
chirality exclusions: present
raw/formal D7 transcript: absent
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
K_IG family identity: not verified
full rival-row elimination: not complete
accepted_selector_count: 0
proof_restart_allowed: false
```

For GU, the claim status remains a **conditional route with a finite D7 proof
object blocker**. The repo may cite the Shiab existence canon and the chirality
screen as narrow positives. It may not promote a `K_IG` selector theorem,
uniqueness theorem, generation result, or major GU claim from those positives.

## 7. Next meaningful proof or computation step

Install or locate a D7-capable representation tool, or write a formal proof that
supplies the same data. The immediate high-value computation is the full
product B table, because it tests the first obstruction:

```text
B = V(omega_2) tensor V(omega_6)
```

If `V(omega_6)` has multiplicity greater than one in B, the current
uniqueness-based selector branch fails unless a separate source-natural
discriminator is supplied. If the multiplicity is exactly one and the full B
table passes dimension checks, the next sequential step is to close product A
kernel irreducibility/highest weight and then run the `K_IG` family identity and
rival-row eliminator.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_1702_C1_L2_V1",
  "artifact_id": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_1702_C1_L2_V1",
  "decision_target": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "run_id": "hourly-20260625-1702",
  "cycle": 1,
  "lane": 2,
  "verdict": "BLOCKED_NO_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_CONSTRUCTED",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1702-cycle1-ig-raw-formal-d7-branching-transcript.md",
  "companion_audit": "tests/hourly_20260625_1702_cycle1_ig_raw_formal_d7_branching_transcript_audit.py",
  "accepted_receipt_count": 0,
  "accepted_selector_count": 0,
  "accepted_selectors": [],
  "proof_restart_allowed": false,
  "target_import_used": false,
  "target_physics_used": false,
  "desired_generation_count_used": false,
  "claim_promotion_allowed": false,
  "major_GU_claim_promoted": false,
  "selector_theorem_closed": false,
  "K_IG_family_identity_verified": false,
  "full_rival_row_elimination_completed": false,
  "raw_CAS_transcript_present": false,
  "raw_CAS_transcript_admitted": false,
  "formal_D7_branching_proof_present": false,
  "formal_D7_branching_proof_admitted": false,
  "local_D7_CAS_tool_available": false,
  "local_D7_CAS_tools_checked": {
    "sage": "not_found",
    "LiE": "not_found",
    "lie": "not_found",
    "gap": "not_found",
    "python": "present"
  },
  "finite_data_fields": {
    "root_system_D7_convention": "present_from_repo_sources",
    "omega_1_vector": "present_from_repo_sources",
    "omega_2_two_form_adjoint": "present_from_repo_sources",
    "omega_6_positive_half_spin": "present_from_repo_sources",
    "omega_7_negative_half_spin": "present_from_repo_sources",
    "product_A_full_summand_list": "missing_admitted_transcript",
    "product_A_multiplicities": "missing_admitted_transcript",
    "product_A_dimensions": "missing_admitted_transcript",
    "product_A_total_dimension_check": "missing_admitted_transcript",
    "kernel_branch_for_c_A_to_V_omega6": "missing_admitted_transcript",
    "cokernel_branch_for_c_A_to_V_omega6": "missing_admitted_transcript",
    "ker_c_irreducibility_or_full_decomposition": "missing_admitted_transcript",
    "ker_c_highest_weight_or_corrected_weight": "missing_admitted_transcript",
    "product_B_full_summand_list": "missing_admitted_transcript",
    "product_B_multiplicities": "missing_admitted_transcript",
    "product_B_dimensions": "missing_admitted_transcript",
    "product_B_total_dimension_check": "missing_admitted_transcript",
    "multiplicity_of_V_omega6_in_B": "missing_admitted_transcript",
    "presence_absence_of_V_omega7_in_B": "present_chirality_exclusion_only",
    "presence_absence_of_V_omega1_plus_omega7_in_B": "present_chirality_exclusion_only",
    "rival_selector_exclusions_full": "missing_admitted_transcript",
    "FC_IRR_verdict": "blocked",
    "FC_MULT_verdict": "blocked",
    "FC_HW_verdict": "blocked"
  },
  "transcript_or_proof_source_booleans": {
    "raw_CAS_tool_name_present": false,
    "raw_CAS_version_present": false,
    "raw_CAS_invocation_present": false,
    "raw_CAS_commands_present": false,
    "raw_CAS_output_present": false,
    "formal_branching_proof_present": false,
    "formal_highest_weight_proof_present": false,
    "formal_dimension_checks_present": false,
    "repo_sources_only_used_for_admission": true
  },
  "directly_derived_repo_results": [
    "Cl_9_5_Shiab_contraction_exists",
    "Shiab_contraction_typed_Omega2_tensor_S_to_Omega1_tensor_S",
    "Shiab_existence_does_not_establish_generation_count_or_uniqueness",
    "D7_weight_convention_specified",
    "chirality_excludes_V_omega7_from_V_omega2_tensor_V_omega6",
    "chirality_excludes_V_omega1_plus_omega7_from_V_omega2_tensor_V_omega6",
    "prior_SC1_OQ1A_multiplicity_and_kernel_claims_are_reconstruction_grade",
    "prior_LiE_Sage_material_is_pseudocode_or_expected_output_not_raw_transcript"
  ],
  "accepted_narrow_positives": [
    "Cl_9_5_Shiab_contraction_exists",
    "D7_weight_convention_specified",
    "chirality_excludes_V_omega7_from_B",
    "chirality_excludes_V_omega1_plus_omega7_from_B"
  ],
  "strongest_positive_result": "ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1",
  "first_obstruction": "No_admitted_full_B_product_D7_branching_table_for_B_equals_V_omega2_tensor_V_omega6_with_every_summand_multiplicity_dimension_total_dimension_check_and_multiplicity_of_V_omega6",
  "first_missing_proof_source_object": "FullBProductD7SummandMultiplicityDimensionTranscriptForShiabHomSpace_V1",
  "next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "constructive_next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "next_meaningful_step": "Produce_raw_LiE_Sage_GAP_output_or_formal_D7_branching_proof_for_A_equals_V_omega1_tensor_V_omega7_and_B_equals_V_omega2_tensor_V_omega6_with_full_summand_lists_multiplicities_dimensions_kernel_cokernel_branch_highest_weight_FC_gate_verdicts_and_rival_selector_exclusions.",
  "FC_IRR_status": "blocked_missing_irreducibility_proof_or_full_kernel_decomposition_for_ker_c",
  "FC_MULT_status": "blocked_missing_full_B_summand_multiplicity_dimension_table_and_multiplicity_of_V_omega6",
  "FC_HW_status": "blocked_missing_highest_weight_proof_or_raw_transcript_for_ker_c",
  "all_FC_gates_closed": false,
  "product_A": {
    "expression": "V(omega_1) tensor V(omega_7)",
    "full_summand_list_admitted": false,
    "multiplicities_admitted": false,
    "dimensions_admitted": false,
    "kernel_branch_admitted": false,
    "cokernel_branch_admitted": false,
    "ker_c_irreducibility_admitted": false,
    "ker_c_highest_weight_admitted": false
  },
  "product_B": {
    "expression": "V(omega_2) tensor V(omega_6)",
    "full_summand_list_admitted": false,
    "multiplicities_admitted": false,
    "dimensions_admitted": false,
    "multiplicity_of_V_omega6_admitted": false,
    "V_omega7_absence_chirality_excluded": true,
    "V_omega1_plus_omega7_absence_chirality_excluded": true
  },
  "rival_selector_exclusions": {
    "chirality_excludes_two_named_rivals": true,
    "full_rival_selector_exclusion_admitted": false,
    "reason": "full_A_B_decompositions_and_multiplicities_absent"
  },
  "promotion_firewall": {
    "shiab_existence_not_selector_theorem": true,
    "chirality_exclusion_not_full_branching_transcript": true,
    "chirality_only_rejected_as_admission_basis": true,
    "pseudocode_not_raw_CAS_receipt": true,
    "reconstruction_grade_not_formal_proof": true,
    "target_physics_not_used": true,
    "desired_generation_count_not_used": true,
    "proof_restart_blocked": true,
    "GU_claim_not_promoted": true
  },
  "what_this_means_for_IG_GU": "IG_remains_a_conditional_route_with_a_finite_D7_proof_transcript_blocker; GU_claims_are_not_promoted_and_selector_restart_is_not_allowed."
}
```
