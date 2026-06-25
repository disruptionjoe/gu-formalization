---
title: "Hourly 20260625 1602 Cycle 1 IG D7 Proof Transcript Object"
date: "2026-06-25"
run_id: "hourly-20260625-1602"
cycle: 1
lane: 2
doc_type: ig_d7_proof_transcript_object
artifact_id: "IG_D7_PROOF_TRANSCRIPT_OBJECT_1602_C1_L2_V1"
verdict: "BLOCKED_NO_FORMAL_D7_PROOF_OR_RAW_TRANSCRIPT"
owned_path: "explorations/hourly-20260625-1602-cycle1-ig-d7-proof-transcript-object.md"
companion_audit: "tests/hourly_20260625_1602_cycle1_ig_d7_proof_transcript_object_audit.py"
---

# Hourly 20260625 1602 Cycle 1 IG D7 Proof Transcript Object

## 1. Verdict

Verdict: **blocked**.

The repo contains narrow positive IG/Shiab representation-theory facts, but it
does not contain a formal D7 branching proof object, raw LiE/Sage/CAS transcript,
or complete multiplicity and highest-weight transcript sufficient to admit the
Shiab Hom-space selector route. The 1503 blocker therefore remains active.

Decision state:

```text
formal_D7_branching_proof_object_present: false
raw_CAS_transcript_present: false
complete_multiplicity_highest_weight_transcript_present: false
accepted_receipt_count: 0
target_import_used: false
proof_restart_allowed: false
K_IG_selector_theorem_closed: false
```

This is not a no-go against the IG route. It is a proof-object admission block:
the route has a precise finite representation-theory object to produce before
selector restart is lawful.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md` and the frontier runbooks:

- compatibility cannot be promoted to derivation;
- a hosted equivariant map cannot be promoted to a selected source-natural map;
- target physics cannot choose the selector;
- blocked lanes must name the first exact missing proof object and the
  constructive next object.

From `canon/shiab-existence-cl95.md`:

- in the current canon, `Y^14` has signature `(9,5)`;
- `Cl(9,5) ~= M(64,H)`, with spinor module `S = H^64`;
- the Shiab/Clifford contraction exists as
  `Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S`;
- Shiab existence explicitly does not establish generation count or uniqueness
  of equivariant maps.

From `explorations/sc1-shiab-domain-codomain-2026-06-23.md`:

- the domain/codomain, Spin(9,5)-equivariance, and right-H-linearity are
  reconstructed and usable as narrow positive inputs;
- the uniqueness/Hom-space question is left open as a D7
  Clebsch-Gordan/multiplicity computation;
- the route needs decomposition of `Lambda^2 tensor Sigma^+` and
  `Lambda^1 tensor Sigma^-`, not another domain/codomain restatement.

From `explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`:

- D7 conventions are stated:
  `omega_1 = vector`, `omega_2 = two-form/adjoint`, `omega_6 = positive half-spin`,
  `omega_7 = negative half-spin`;
- chirality excludes `V(omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- chirality excludes `V(omega_1 + omega_7)` from
  `V(omega_2) tensor V(omega_6)`;
- the file itself records that its verdict was downgraded to
  `CONDITIONALLY_RESOLVED`;
- the remaining failure conditions are `FC-IRR`, `FC-MULT`, and `FC-HW`;
- its LiE/Sage commands are pseudocode and expected outputs, not a raw transcript.

From the 1503 IG lanes:

- `IG_D7_MULTIPLICITY_TRANSCRIPT_1503_C1_L2_V1` found no raw local D7 transcript
  for `FC-IRR`, `FC-MULT`, or `FC-HW`;
- `IG_D7_FORMAL_OR_CAS_PROOF_OBJECT_ADMISSION_1503_C2_L2_V1` found no admissible
  formal hand proof object and named the finite proof obligations;
- both artifacts set `accepted_selector_count = 0`, `target_import_used = false`,
  and `proof_restart_allowed = false`.

The repo-wide transcript surfaces checked for this lane were:

```text
canon/shiab-existence-cl95.md
explorations/sc1-shiab-domain-codomain-2026-06-23.md
explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md
DERIVATION-PROGRESS.md
explorations/hourly-20260625-1503-cycle1-ig-d7-multiplicity-transcript.md
explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md
tests/hourly_20260625_1503_cycle2_ig_d7_proof_object_admission_audit.py
repo rg search for D7/Shiab/K_IG/Hom-space/highest-weight/multiplicity/LiE/Sage/CAS/branching
```

No source checked above supplies the complete finite data required for admission.

## 3. The strongest positive result

The strongest positive construction attempt is:

```text
ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1
```

It consists of four narrow positives:

1. The Shiab map exists and is typed in the `(9,5)` Clifford setting.
2. The D7 labels for the Hom-space problem are specified.
3. Clifford/gamma-trace structure supplies the intended map
   `V(omega_1) tensor V(omega_7) -> V(omega_6)`.
4. Chirality parity excludes `V(omega_7)` and `V(omega_1 + omega_7)` from
   `V(omega_2) tensor V(omega_6)`.

This is a real positive because it pins the finite representation-theory gate and
rules out two possible false common summands. It is still not the full
`K_IG` selector theorem and not even the full finite D7 packet. The missing data are
not cosmetic: multiplicity and irreducibility decide whether the Hom space is
one-dimensional or has additional source-natural rivals.

## 4. The first exact obstruction or missing proof object

The first exact missing object is:

```text
VerifiedMultiplicityIrreducibilityAndHighestWeightD7PacketForShiabHomSpace_V1
```

It is equivalent in role to the 1503 blocker
`VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1`, but the
name here makes the irreducibility obligation explicit.

Minimum missing fields:

```text
root_and_convention:
  D7 with omega_1 vector, omega_2 two-form/adjoint, omega_6 positive half-spin,
  omega_7 negative half-spin.

multiplicity:
  full decomposition of V(omega_2) tensor V(omega_6), with multiplicities for
  every summand, and explicit multiplicity of V(omega_6).

irreducibility:
  proof that ker(c) in
    V(omega_1) tensor V(omega_7) -> V(omega_6)
  is irreducible, or a full reducible decomposition with recomputed intersections.

highest_weight:
  proof that ker(c) has highest weight omega_1 + omega_7, or a corrected highest
  weight and recomputed Hom-space intersection.

dimension_checks:
  dimensions for every reported summand and tensor-product total checks for both
  products.

raw_or_formal_provenance:
  either raw LiE/Sage/CAS output with version/invocation, or a formal D7
  highest-weight/branching proof containing the same finite data.
```

The first obstruction is not "no CAS is installed" in isolation. CAS output would
be sufficient if raw and reproducible, but a hand proof is also acceptable. The
actual obstruction is absence of a proof/transcript object containing the finite
D7 multiplicity, irreducibility, highest-weight, and dimension data.

## 5. The constructive next object that would remove or test the obstruction

Create:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

Acceptance rubric:

```text
inputs:
  root_system: D7
  dynkin_labels:
    omega_1: [1,0,0,0,0,0,0]
    omega_2: [0,1,0,0,0,0,0]
    omega_6: [0,0,0,0,0,1,0]
    omega_7: [0,0,0,0,0,0,1]

required_products:
  A: V(omega_1) tensor V(omega_7)
  B: V(omega_2) tensor V(omega_6)

required_outputs:
  A_full_summand_list_with_multiplicities_and_dimensions
  B_full_summand_list_with_multiplicities_and_dimensions
  ker_c_irreducibility_or_full_kernel_decomposition
  ker_c_highest_weight
  multiplicity_of_V_omega6_in_A
  multiplicity_of_V_omega6_in_B
  presence_absence_of_V_omega7_in_B
  presence_absence_of_V_omega1_plus_omega7_in_B
  tensor_product_total_dimension_checks
  gate_verdicts_for_FC_IRR_FC_MULT_FC_HW
  no_target_physics_or_desired_uniqueness_used
```

This object would either admit the finite D7 gate or falsify the current
uniqueness skeleton. In particular, if `V(omega_6)` has multiplicity greater than
one in `V(omega_2) tensor V(omega_6)`, the current Shiab Hom-space selector route
does not close without an additional source-natural discriminator.

## 6. What this means for the IG/GU claim

For IG:

```text
Shiab existence: present as a narrow positive
D7 chirality exclusions: present as narrow positives
finite D7 proof/transcript packet: absent
K_IG family identity: absent
full rival-row elimination: absent
accepted_selector_count: 0
proof_restart_allowed: false
```

For GU:

- The repo can continue to use the Shiab existence and type as a constructive
  component of the GU reconstruction program.
- The repo cannot claim that `K_IG` selects the source-natural Hom-space route.
- The repo cannot use generation count, target physics, or desired uniqueness as
  evidence for the D7 decomposition.
- No major GU claim is promoted or demoted by this lane; the effect is a tighter
  firewall around the IG selector theorem.

The correct claim status is: **conditional route with a finite proof-object
blocker**.

## 7. Next meaningful proof or computation step

The next meaningful step is to produce the `RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1`
packet. A useful first computation is:

```text
decompose V([1,0,0,0,0,0,0]) tensor V([0,0,0,0,0,0,1])
decompose V([0,1,0,0,0,0,0]) tensor V([0,0,0,0,0,1,0])
```

The output must be raw enough to audit: tool/version/invocation, full summand
lists, multiplicities, dimensions, and explicit gate verdicts for `FC-IRR`,
`FC-MULT`, and `FC-HW`. If that computation is unavailable, write the same object
as a formal D7 branching proof with all summands and dimensions included.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "IG_D7_PROOF_TRANSCRIPT_OBJECT_1602_C1_L2_V1",
  "artifact_id": "IG_D7_PROOF_TRANSCRIPT_OBJECT_1602_C1_L2_V1",
  "run_id": "hourly-20260625-1602",
  "cycle": 1,
  "lane": 2,
  "verdict": "BLOCKED_NO_FORMAL_D7_PROOF_OR_RAW_TRANSCRIPT",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1602-cycle1-ig-d7-proof-transcript-object.md",
  "companion_audit": "tests/hourly_20260625_1602_cycle1_ig_d7_proof_transcript_object_audit.py",
  "decision_target": "IG_D7_PROOF_TRANSCRIPT_OBJECT",
  "accepted_receipt_count": 0,
  "accepted_selector_count": 0,
  "formal_D7_branching_proof_object_present": false,
  "raw_CAS_transcript_present": false,
  "complete_multiplicity_highest_weight_transcript_present": false,
  "formal_hand_proof_admitted": false,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "target_physics_used": false,
  "claim_promotion_allowed": false,
  "K_IG_selector_theorem_closed": false,
  "K_IG_family_identity_verified": false,
  "full_rival_row_elimination_completed": false,
  "transcript_surfaces_checked": [
    "canon/shiab-existence-cl95.md",
    "explorations/sc1-shiab-domain-codomain-2026-06-23.md",
    "explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md",
    "DERIVATION-PROGRESS.md",
    "explorations/hourly-20260625-1503-cycle1-ig-d7-multiplicity-transcript.md",
    "explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md",
    "tests/hourly_20260625_1503_cycle2_ig_d7_proof_object_admission_audit.py",
    "repo_rg_D7_Shiab_K_IG_Hom_space_highest_weight_multiplicity_LiE_Sage_CAS_branching"
  ],
  "accepted_narrow_positives": [
    "Shiab_Cl_9_5_contraction_exists",
    "Shiab_domain_codomain_Omega2_tensor_S_to_Omega1_tensor_S",
    "Spin_9_5_equivariance_and_right_H_linearity",
    "D7_weight_convention_specified",
    "chirality_exclusion_of_V_omega7_from_V_omega2_tensor_V_omega6",
    "chirality_exclusion_of_V_omega1_plus_omega7_from_V_omega2_tensor_V_omega6"
  ],
  "strongest_positive_result": "ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1",
  "first_exact_obstruction": "VerifiedMultiplicityIrreducibilityAndHighestWeightD7PacketForShiabHomSpace_V1",
  "exact_missing_fields": [
    "multiplicity_full_decomposition_of_V_omega2_tensor_V_omega6",
    "multiplicity_of_V_omega6_in_V_omega2_tensor_V_omega6",
    "irreducibility_of_kernel_of_c_in_V_omega1_tensor_V_omega7_to_V_omega6",
    "highest_weight_of_kernel_of_c",
    "full_decomposition_of_V_omega1_tensor_V_omega7",
    "dimension_checks_for_all_reported_summands",
    "raw_or_formal_provenance_for_D7_branching_data",
    "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW"
  ],
  "FC_IRR_status": "blocked_missing_irreducibility_proof_or_full_kernel_decomposition",
  "FC_MULT_status": "blocked_missing_full_multiplicity_transcript_for_V_omega6_in_V_omega2_tensor_V_omega6",
  "FC_HW_status": "blocked_missing_highest_weight_proof_for_kernel_of_c",
  "next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "constructive_next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "next_object_required_outputs": [
    "A_full_summand_list_with_multiplicities_and_dimensions",
    "B_full_summand_list_with_multiplicities_and_dimensions",
    "ker_c_irreducibility_or_full_kernel_decomposition",
    "ker_c_highest_weight",
    "multiplicity_of_V_omega6_in_A",
    "multiplicity_of_V_omega6_in_B",
    "presence_absence_of_V_omega7_in_B",
    "presence_absence_of_V_omega1_plus_omega7_in_B",
    "tensor_product_total_dimension_checks",
    "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW",
    "no_target_physics_or_desired_uniqueness_used"
  ],
  "promotion_firewall": {
    "shiab_existence_not_selector_theorem": true,
    "chirality_exclusion_not_multiplicity_proof": true,
    "pseudocode_not_raw_CAS_transcript": true,
    "reconstruction_grade_not_admitted_proof": true,
    "target_physics_not_used": true,
    "K_IG_not_promoted": true,
    "major_GU_claim_not_promoted": true,
    "proof_restart_blocked": true
  },
  "what_this_means_for_IG_GU": "IG_remains_a_conditional_route_with_a_finite_D7_proof_transcript_blocker; GU_claims_are_not_promoted_and_selector_restart_is_not_allowed.",
  "next_meaningful_step": "Produce_raw_LiE_Sage_CAS_output_or_a_formal_D7_branching_proof_for_the_two_required_tensor_products_with_full_summand_lists_multiplicities_highest_weight_irreducibility_and_dimension_checks."
}
```
