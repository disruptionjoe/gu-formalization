---
title: "Hourly 20260625 1503 Cycle 2 IG D7 Proof Object Admission"
date: "2026-06-25"
run_id: "hourly-20260625-1503"
cycle: 2
lane: 2
doc_type: ig_d7_proof_object_admission
artifact_id: "IG_D7_FORMAL_OR_CAS_PROOF_OBJECT_ADMISSION_1503_C2_L2_V1"
verdict: "BLOCKED_FORMAL_PROOF_NOT_ADMITTED"
owned_path: "explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md"
companion_audit: "tests/hourly_20260625_1503_cycle2_ig_d7_proof_object_admission_audit.py"
---

# Hourly 20260625 1503 Cycle 2 IG D7 Proof Object Admission

## 1. Verdict

Verdict: **blocked**.

No formal hand proof object can be admitted from the current repo sources for the
exact D7 gates needed by the IG selector route. The repo contains an accepted
narrow positive result: the Cl(9,5) Shiab/Clifford contraction exists and the
chirality-parity screen excludes `V(omega_7)` and `V(omega_1+omega_7)` from
`V(omega_2) tensor V(omega_6)`. It does not contain a complete finite D7 proof
object with full summand lists, multiplicities, and dimension checks.

Decision state:

```text
formal_proof_admitted: false
raw_transcript_required: true
FC-IRR: blocked_formal_proof_missing
FC-MULT: blocked_formal_proof_missing
FC-HW: blocked_formal_proof_missing
full_summand_lists_present: false
dimension_checks_present: false
accepted_selector_count: 0
target_import_used: false
proof_restart_allowed: false
```

The route is not refuted. It remains blocked until either a raw finite
LiE/Sage/formal transcript exists, or a hand proof supplies the same finite data
at proof grade.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md` and the runbooks:

- compatibility cannot be promoted to derivation;
- a hosted object cannot be promoted to a selected source-natural object;
- target physics cannot choose the selector;
- a blocked lane must name the exact missing proof object and a constructive next
  object.

From `canon/shiab-existence-cl95.md` and
`explorations/sc1-shiab-domain-codomain-2026-06-23.md`:

- `Y^14` is treated in the `(9,5)` signature setting;
- `Cl(9,5) ~= M(64,H)` and `S = H^64`;
- the Shiab/Clifford contraction has the typed form
  `Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S`;
- existence, equivariance, and right-H-linearity of the contraction do not settle
  uniqueness of equivariant maps.

From `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md` and the
`SC1-OQ1A-VERDICT-OVERSTATED` correction in `DERIVATION-PROGRESS.md`:

- the D7 convention in use is
  `omega_1 = vector`, `omega_2 = two-form / adjoint`,
  `omega_6 = positive half-spin`, and `omega_7 = negative half-spin`;
- the chirality screen excludes `V(omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- the same screen excludes `V(omega_1+omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- irreducibility of `ker(c)` in
  `V(omega_1) tensor V(omega_7) -> V(omega_6)` remains reconstruction grade;
- the highest-weight identification `ker(c) = V(omega_1+omega_7)` remains
  reconstruction grade;
- the multiplicity-one claim for `V(omega_6)` inside
  `V(omega_2) tensor V(omega_6)` remains reconstruction grade;
- a LiE/Sage computation or formal D7 branching/highest-weight proof is required
  for upgrade.

From the cycle-1 transcript lane and the prior audit gate:

- no raw LiE/Sage transcript was found locally;
- the first exact missing object is still
  `VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1`;
- `K_IG` family identity, selector restart, and full rival-row elimination remain
  downstream.

Narrow direct result admitted here:

```text
Directly admitted: Cl(9,5) Shiab existence/equivariance/H-linearity and the
chirality exclusions for V(omega_7) and V(omega_1+omega_7) from
V(omega_2) tensor V(omega_6).

Not admitted: irreducibility of ker(c), highest weight of ker(c), multiplicity
one of V(omega_6), complete D7 decompositions, or selector uniqueness.
```

## 3. The strongest positive construction attempt

The strongest positive construction is the following conditional hand-proof
skeleton.

Let `D7 = so(14,C)` with fundamental weights as above. Let

```text
A = V(omega_1) tensor V(omega_7)
B = V(omega_2) tensor V(omega_6)
c: A -> V(omega_6)
```

where `c` is the gamma-trace / Clifford multiplication map. The desired common
summand analysis would be:

```text
A = V(omega_6) oplus V(omega_1+omega_7)
B = V(omega_6) oplus W_1 oplus ... oplus W_r
```

with:

- `V(omega_6)` appearing exactly once in both `A` and `B`;
- `V(omega_1+omega_7)` absent from `B`;
- every `W_i` explicitly listed, with multiplicity and dimension;
- no `W_i` is isomorphic to `V(omega_6)` or `V(omega_1+omega_7)`.

The exact theorem statements that would be admissible are:

```text
FC-IRR theorem:
  In D7, the kernel of the equivariant gamma-trace map
    c: V(omega_1) tensor V(omega_7) -> V(omega_6)
  is irreducible and the decomposition is
    V(omega_1) tensor V(omega_7)
      = V(omega_6) oplus V(omega_1+omega_7),
  with both summands multiplicity one and dimensions summing to 14 * dim V(omega_7).

FC-MULT theorem:
  In D7, the decomposition of
    V(omega_2) tensor V(omega_6)
  contains V(omega_6) with multiplicity exactly one, and the proof supplies the
  full summand list with multiplicity and dimension checks for every summand.

FC-HW theorem:
  The highest weight of ker(c) is omega_1 + omega_7, and this assignment is proved
  by a highest-weight argument or by a finite branching/character computation;
  if the weight differs, the common-summand intersection is recomputed from the
  corrected weight.
```

The strongest positive route therefore has a clear shape. It is not presently an
admissible proof object because the repo sources stop before the required finite
decomposition data.

## 4. The first exact obstruction or missing proof object

The first exact obstruction is still:

```text
VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1
```

The obstruction is not merely the absence of CAS. A hand proof is acceptable in
principle, but it must be a finite proof object with the same content a CAS
transcript would provide.

Minimum proof obligations:

```text
PO-ROOT:
  State the D7 Dynkin convention and identify omega_1, omega_2, omega_6, omega_7.

PO-FC-IRR:
  Prove the full decomposition of V(omega_1) tensor V(omega_7), not only the
  existence of the gamma-trace map.

PO-FC-MULT:
  Prove the full decomposition of V(omega_2) tensor V(omega_6), or at minimum
  prove multiplicity one for V(omega_6) while also listing every other summand
  and excluding accidental overlap with the codomain product.

PO-FC-HW:
  Prove the highest weight of ker(c), not infer it from expected dimension alone.

PO-DIM:
  Supply dimension checks for every reported summand and for both tensor product
  totals.

PO-NO-IMPORT:
  Do not use target generation count, desired selector uniqueness, or physics
  success as evidence for the D7 decomposition.
```

The current hand route fails at `PO-FC-IRR`, `PO-FC-MULT`, `PO-FC-HW`, and
`PO-DIM`. It supplies exact chirality exclusions, but not full finite
representation data.

## 5. The constructive next object that would remove or test the obstruction

Create either:

```text
FormalD7BranchingProofForShiabHomSpace_V1
```

or:

```text
LiEOrSageD7MultiplicityAuditForShiabHomSpace_V1
```

Admission rubric for either object:

```text
required_inputs:
  root_system: D7
  dynkin_convention:
    omega_1: vector
    omega_2: two-form_adjoint
    omega_6: positive_half_spin
    omega_7: negative_half_spin
  products:
    - V(omega_1) tensor V(omega_7)
    - V(omega_2) tensor V(omega_6)

required_outputs:
  - full_summand_list_for_V_omega1_tensor_V_omega7
  - full_summand_list_for_V_omega2_tensor_V_omega6
  - multiplicities_for_all_summands
  - dimensions_for_all_summands
  - tensor_product_total_dimension_checks
  - proof_or_transcript_for_ker_c_irreducibility
  - proof_or_transcript_for_ker_c_highest_weight
  - explicit_presence_or_absence_of_V_omega6
  - explicit_presence_or_absence_of_V_omega7
  - explicit_presence_or_absence_of_V_omega1_plus_omega7
  - gate_verdicts_for_FC_IRR_FC_MULT_FC_HW

rejection_conditions:
  - only chirality exclusions are supplied
  - only expected decompositions are stated
  - only dimensions of selected summands are checked
  - the full B product is abbreviated as "other summands"
  - the proof relies on target physics or desired uniqueness
  - the proof repeats a reconstruction-grade argument without closing its named gap
```

## 6. What this means for `K_IG`, selector restart, and rival elimination

`K_IG` remains blocked upstream of the D7 packet.

```text
D7 finite proof object admitted: false
D7 raw transcript accepted: false
K_IG family identity verified: false
full rival-row elimination completed: false
accepted_selector_count: 0
proof_restart_allowed: false
```

The selector restart is not allowed because zero selectors have been accepted.
The `K_IG` family identity cannot be treated as proved by the existence of the
Shiab map, and the rival matrix cannot be eliminated by chirality-only exclusions
inside one representation-theory subproblem.

If the D7 packet is later admitted, it would only close the first finite gate. A
separate downstream theorem would still have to identify the admitted source map
with the `K_IG` selector and eliminate the representation-natural rivals without
target import.

## 7. Next meaningful proof/computation step

The next meaningful step is to produce the finite D7 packet, preferably with a
raw transcript and independently checkable dimensions.

If working without CAS, the next proof step is not another prose uniqueness
argument. It is a complete D7 branching proof of the two tensor products above,
including all summands and their dimensions. If that hand proof cannot be given
compactly, the route should wait for a raw LiE/Sage transcript.

The immediate test remains `FC-MULT`: if `V(omega_6)` occurs with multiplicity
greater than one in `V(omega_2) tensor V(omega_6)`, the current
uniqueness-based selector route fails unless a stronger source-natural Bianchi
rule distinguishes the extra copy.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "IG_D7_FORMAL_OR_CAS_PROOF_OBJECT_ADMISSION_1503_C2_L2_V1",
  "artifact_id": "IG_D7_FORMAL_OR_CAS_PROOF_OBJECT_ADMISSION_1503_C2_L2_V1",
  "run_id": "hourly-20260625-1503",
  "cycle": 2,
  "lane": 2,
  "verdict": "BLOCKED_FORMAL_PROOF_NOT_ADMITTED",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md",
  "companion_audit": "tests/hourly_20260625_1503_cycle2_ig_d7_proof_object_admission_audit.py",
  "decision_target": "IG_D7_FORMAL_OR_CAS_PROOF_OBJECT_ADMISSION",
  "formal_proof_admitted": false,
  "raw_transcript_required": true,
  "formal_hand_proof_allowed_in_principle": true,
  "formal_hand_proof_present": false,
  "raw_CAS_transcript_present": false,
  "full_summand_lists_present": false,
  "dimension_checks_present": false,
  "target_import_used": false,
  "target_physics_used": false,
  "accepted_selector_count": 0,
  "accepted_selectors": [],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "K_IG_family_identity_verified": false,
  "full_rival_row_elimination_completed": false,
  "first_exact_obstruction": "VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1",
  "constructive_next_object": "FormalD7BranchingProofForShiabHomSpace_V1_or_LiEOrSageD7MultiplicityAuditForShiabHomSpace_V1",
  "directly_derived_repo_results": [
    "Cl_9_5_Shiab_contraction_exists",
    "Shiab_contraction_is_typed_Omega2_tensor_S_to_Omega1_tensor_S",
    "Shiab_existence_does_not_establish_uniqueness",
    "chirality_excludes_V_omega7_from_V_omega2_tensor_V_omega6",
    "chirality_excludes_V_omega1_plus_omega7_from_V_omega2_tensor_V_omega6"
  ],
  "strongest_positive_construction_attempt": "ConditionalD7HandProofSkeletonWithGammaTraceAndChiralityExclusions",
  "FC_IRR_status": "blocked_missing_formal_irreducibility_proof_and_full_decomposition_of_V_omega1_tensor_V_omega7",
  "FC_MULT_status": "blocked_missing_full_summand_list_and_multiplicity_proof_for_V_omega6_in_V_omega2_tensor_V_omega6",
  "FC_HW_status": "blocked_missing_highest_weight_proof_for_ker_c",
  "FC_IRR_theorem_statement": "ker_c_of_V_omega1_tensor_V_omega7_to_V_omega6_is_irreducible_and_V_omega1_tensor_V_omega7_equals_V_omega6_oplus_V_omega1_plus_omega7_with_multiplicity_one",
  "FC_MULT_theorem_statement": "V_omega6_occurs_with_multiplicity_exactly_one_in_V_omega2_tensor_V_omega6_and_all_other_summands_are_listed_with_multiplicities_and_dimensions",
  "FC_HW_theorem_statement": "highest_weight_of_ker_c_is_omega1_plus_omega7_or_corrected_weight_is_reported_and_common_summands_are_recomputed",
  "required_proof_obligations": [
    "PO_ROOT_D7_Dynkin_convention",
    "PO_FC_IRR_full_decomposition_of_V_omega1_tensor_V_omega7",
    "PO_FC_MULT_full_decomposition_of_V_omega2_tensor_V_omega6",
    "PO_FC_HW_highest_weight_of_ker_c",
    "PO_DIM_dimension_checks_for_every_reported_summand",
    "PO_NO_IMPORT_no_target_physics_or_desired_uniqueness"
  ],
  "missing_finite_representation_data": [
    "full_decomposition_of_V_omega1_tensor_V_omega7",
    "irreducibility_of_kernel_of_c",
    "highest_weight_of_kernel_of_c",
    "full_decomposition_of_V_omega2_tensor_V_omega6",
    "multiplicity_of_V_omega6_in_V_omega2_tensor_V_omega6",
    "dimension_checks_for_all_reported_summands"
  ],
  "accepted_narrow_results": [
    "Shiab_existence_equivariance_H_linearity",
    "chirality_exclusion_of_V_omega7",
    "chirality_exclusion_of_V_omega1_plus_omega7"
  ],
  "rejected_admission_bases": [
    "reconstruction_grade_kernel_irreducibility",
    "reconstruction_grade_highest_weight_assignment",
    "chirality_only_argument_without_full_summand_list",
    "expected_decomposition_without_raw_output_or_formal_branching_proof",
    "dimension_check_for_selected_summands_only",
    "target_physics_or_desired_selector_uniqueness"
  ],
  "admission_rubric_required_outputs": [
    "full_summand_list_for_V_omega1_tensor_V_omega7",
    "full_summand_list_for_V_omega2_tensor_V_omega6",
    "multiplicities_for_all_summands",
    "dimensions_for_all_summands",
    "tensor_product_total_dimension_checks",
    "proof_or_transcript_for_ker_c_irreducibility",
    "proof_or_transcript_for_ker_c_highest_weight",
    "explicit_presence_or_absence_of_V_omega6",
    "explicit_presence_or_absence_of_V_omega7",
    "explicit_presence_or_absence_of_V_omega1_plus_omega7",
    "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW"
  ],
  "proof_restart_allowed_if_and_only_if": "formal_proof_admitted_or_raw_CAS_transcript_present_and_all_FC_gates_closed_and_K_IG_family_identity_verified_and_full_rival_row_elimination_completed_and_target_import_used_false",
  "next_meaningful_step": "Produce_a_complete_D7_branching_proof_or_raw_LiE_Sage_transcript_for_the_two_required_tensor_products_with_full_summand_lists_multiplicities_and_dimension_checks."
}
```
