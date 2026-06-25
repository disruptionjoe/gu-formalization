---
title: "Hourly 20260625 1702 Cycle 2 IG Finite Transcript Admission Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-1702"
cycle: 2
lane: 2
doc_type: ig_finite_transcript_admission_matrix
artifact_id: "IG_FINITE_TRANSCRIPT_ADMISSION_MATRIX_1702_C2_L2_V1"
verdict: "BLOCKED_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE_MISSING"
owned_path: "explorations/hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md"
companion_audit: "tests/hourly_20260625_1702_cycle2_ig_finite_transcript_admission_matrix_audit.py"
---

# Hourly 20260625 1702 Cycle 2 IG Finite Transcript Admission Matrix

## 1. Verdict

Verdict: **blocked**.

The cycle 1 blocker is now converted into a finite-data admission matrix for:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

No row is admissible as the requested raw or formal transcript. The repo has a
typed Shiab contraction in the `Cl(9,5)` setting and two chirality exclusions in
the D7 screen, but it does not have the full finite D7 product data needed to
close `FC-IRR`, `FC-MULT`, or `FC-HW`.

Admission decision:

```text
accepted_transcript: false
accepted_receipt_count: 0
proof_restart_allowed: false
target_import_used: false
K_IG_family_identity_verified: false
```

This is not a no-go against the IG route. It is a strict finite-data admission
block. Chirality, target generation count, desired uniqueness, or downstream GU
success are not proof data for this matrix.

## 2. Sources read and directly derived facts

From `RESEARCH-POSTURE.md`:

- compatibility is not derivation;
- target data must not be hidden inside reconstruction;
- a failed proof object must be treated as an exact blocker or a constructive
  next object, not as a promoted claim.

From `process/runbooks/five-lane-frontier-run.md` and
`process/runbooks/three-cycle-fifteen-hole-run.md`:

- frontier lanes must give a decision-grade artifact;
- verdicts must distinguish blocked, conditional, no-go, host, and import;
- each blocked lane must name the first exact missing proof object.

From cycle 1
`explorations/hourly-20260625-1702-cycle1-ig-raw-formal-d7-branching-transcript.md`
and its audit:

- no raw CAS transcript was admitted;
- no formal D7 branching proof was admitted;
- local D7 CAS tooling was not available in that lane;
- the first obstruction was the absence of a full `B` product D7 branching table;
- `FC-IRR`, `FC-MULT`, and `FC-HW` all remained blocked;
- proof restart, target import, and claim promotion were all rejected.

From `canon/shiab-existence-cl95.md`:

- the current canon uses signature `(9,5)`;
- `Cl(9,5) ~= M(64,H)` and the spinor module is `S = H^64`;
- the Shiab/Clifford contraction exists as
  `Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S`;
- this canon does not establish generation count, uniqueness of the equivariant
  map, or a `K_IG` selector theorem.

Direct D7 facts inherited from the cycle 1 artifact:

- convention: `omega_1` is vector, `omega_2` is two-form/adjoint,
  `omega_6` is positive half-spin, and `omega_7` is negative half-spin;
- product A is `V(omega_1) tensor V(omega_7)`;
- product B is `V(omega_2) tensor V(omega_6)`;
- chirality excludes `V(omega_7)` from product B;
- chirality excludes `V(omega_1 + omega_7)` from product B;
- these exclusions do not supply product B's full summand list, multiplicities,
  dimensions, or the multiplicity of `V(omega_6)`.

## 3. Strongest positive construction attempt

The strongest positive construction attempt is:

```text
ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1
```

It combines:

- the real `Cl(9,5)` Shiab contraction;
- the fixed D7 convention;
- the candidate gamma-trace branch
  `c: V(omega_1) tensor V(omega_7) -> V(omega_6)`;
- the two chirality exclusions from product B.

This is useful because it identifies the exact finite products to compute. It is
not enough to admit the transcript because it does not give:

- product A's full decomposition;
- product A summand multiplicities and dimensions;
- the kernel/cokernel branch of `c`;
- irreducibility or full decomposition of `ker(c)`;
- the highest weight of `ker(c)`;
- product B's full decomposition;
- product B summand multiplicities and dimensions;
- the multiplicity of `V(omega_6)` in product B;
- full rival exclusions beyond the two chirality-screened rows.

## 4. First exact obstruction/missing field set

The first exact obstruction is:

```text
ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6
```

This is the first blocker because `FC-MULT` cannot be decided until product B
has every summand, every multiplicity, every dimension, a total dimension check,
and the multiplicity of `V(omega_6)`. The absence of two wrong-chirality rivals
does not prove that the desired `V(omega_6)` copy is unique, and it does not
exclude all same-chirality or non-listed rivals.

Minimal missing field set:

```text
raw_or_formal_source_identity:
  raw CAS tool/version/invocation/commands/output, or formal proof identity

product_A:
  full summand list
  multiplicities
  dimensions
  total dimension check
  kernel/cokernel branch for c
  irreducibility or full decomposition of ker(c)
  highest weight or corrected weight of ker(c)

product_B:
  full summand list
  multiplicities
  dimensions
  total dimension check
  multiplicity of V(omega_6)
  full rival presence/absence checks

verdicts:
  FC-IRR
  FC-MULT
  FC-HW
  rival exclusions
```

## 5. Constructive next object

Create:

```text
RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1
```

The object can be either:

- a raw D7 CAS receipt with tool name, version, invocation, commands, and raw
  output; or
- a formal D7 branching proof that supplies the same finite fields.

The next object must compute or prove both products:

```text
A = V(omega_1) tensor V(omega_7)
B = V(omega_2) tensor V(omega_6)
```

and must issue explicit `FC-IRR`, `FC-MULT`, and `FC-HW` verdicts without using
chirality alone, target generation count, or desired uniqueness as proof data.

## 6. Consequence for IG/GU claims

For IG:

```text
Shiab existence: present
D7 convention: present
two chirality exclusions: present
accepted finite transcript: false
FC-IRR: blocked
FC-MULT: blocked
FC-HW: blocked
K_IG family identity: false
full rival-row exclusion: false
proof restart: false
```

For GU:

- no major GU claim is promoted;
- no `K_IG` selector theorem is closed;
- the route remains conditional on a finite D7 transcript/proof object;
- if later product B gives multiplicity greater than one for `V(omega_6)`, the
  uniqueness branch fails unless a separate source-natural discriminator is
  supplied.

## 7. Next computation/proof step

Run or prove the two finite D7 decompositions:

```text
decompose V([1,0,0,0,0,0,0]) tensor V([0,0,0,0,0,0,1])
decompose V([0,1,0,0,0,0,0]) tensor V([0,0,0,0,0,1,0])
```

The first acceptance-critical output is the full product B table:

```text
B = V(omega_2) tensor V(omega_6)
```

including every summand, multiplicity, dimension, total dimension check,
multiplicity of `V(omega_6)`, and full rival-row presence/absence checks.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "IG_FINITE_TRANSCRIPT_ADMISSION_MATRIX_1702_C2_L2_V1",
  "artifact_id": "IG_FINITE_TRANSCRIPT_ADMISSION_MATRIX_1702_C2_L2_V1",
  "decision_target": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "run_id": "hourly-20260625-1702",
  "cycle": 2,
  "lane": 2,
  "verdict": "BLOCKED_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE_MISSING",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md",
  "companion_audit": "tests/hourly_20260625_1702_cycle2_ig_finite_transcript_admission_matrix_audit.py",
  "accepted_transcript": false,
  "accepted_receipt_count": 0,
  "accepted_selector_count": 0,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "target_physics_used": false,
  "desired_generation_count_used": false,
  "desired_uniqueness_used": false,
  "chirality_alone_used_as_selector": false,
  "claim_promotion_allowed": false,
  "major_GU_claim_promoted": false,
  "selector_theorem_closed": false,
  "K_IG_family_identity_verified": false,
  "family_identity_verified": false,
  "full_rival_row_elimination_completed": false,
  "raw_CAS_transcript_admitted": false,
  "formal_D7_branching_proof_admitted": false,
  "first_obstruction": "ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6",
  "first_missing_field_set": [
    "product_B_full_summand_list",
    "product_B_multiplicities",
    "product_B_dimensions",
    "product_B_total_dimension_check",
    "multiplicity_of_V_omega6_in_B",
    "full_rival_presence_absence_checks"
  ],
  "next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "constructive_next_object": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
  "strongest_positive_construction_attempt": "ConditionalD7ShiabHomSpaceChiralityAndGammaTraceSkeleton_V1",
  "accepted_narrow_positives": [
    "Cl_9_5_Shiab_contraction_exists",
    "D7_weight_convention_specified",
    "chirality_excludes_V_omega7_from_product_B",
    "chirality_excludes_V_omega1_plus_omega7_from_product_B"
  ],
  "FC_IRR_verdict": "blocked_missing_product_A_kernel_irreducibility_or_full_decomposition",
  "FC_MULT_verdict": "blocked_missing_product_B_full_summand_multiplicity_dimension_table_and_multiplicity_of_V_omega6",
  "FC_HW_verdict": "blocked_missing_product_A_kernel_highest_weight_or_corrected_weight",
  "finite_field_rows": [
    {
      "field": "raw_or_formal_source_identity",
      "required": true,
      "source_identity": "raw_CAS_receipt_or_formal_D7_proof",
      "current_value": null,
      "status": "missing",
      "admission_effect": "blocks_transcript",
      "notes": "Cycle_1_admitted_no_raw_CAS_transcript_and_no_formal_D7_branching_proof."
    },
    {
      "field": "D7_convention",
      "required": true,
      "source_identity": "cycle_1_repo_sources",
      "current_value": {
        "root_system": "D7",
        "omega_1": "vector",
        "omega_2": "two_form_adjoint",
        "omega_6": "positive_half_spin",
        "omega_7": "negative_half_spin"
      },
      "status": "present",
      "admission_effect": "necessary_not_sufficient",
      "notes": "Convention is fixed but supplies no product decomposition."
    },
    {
      "field": "product_A_decomposition",
      "required": true,
      "source_identity": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
      "expression": "V(omega_1) tensor V(omega_7)",
      "full_summands": null,
      "multiplicities": null,
      "dimensions": null,
      "total_dimension_check": null,
      "status": "missing",
      "admission_effect": "blocks_FC_IRR_and_FC_HW",
      "notes": "A is identified but no admitted full finite table is present."
    },
    {
      "field": "product_A_kernel_cokernel_branch",
      "required": true,
      "source_identity": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
      "map": "c: V(omega_1) tensor V(omega_7) -> V(omega_6)",
      "kernel_branch": null,
      "cokernel_branch": null,
      "highest_weight": null,
      "irreducibility": null,
      "status": "missing",
      "admission_effect": "blocks_FC_IRR_and_FC_HW",
      "notes": "Gamma-trace skeleton names the map but does not prove kernel irreducibility or highest weight."
    },
    {
      "field": "product_B_full_summands",
      "required": true,
      "source_identity": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
      "expression": "V(omega_2) tensor V(omega_6)",
      "full_summands": null,
      "multiplicities": null,
      "dimensions": null,
      "total_dimension_check": null,
      "multiplicity_of_V_omega6": null,
      "status": "missing",
      "admission_effect": "first_obstruction_blocks_FC_MULT",
      "notes": "This is the first exact obstruction because the Hom-space multiplicity cannot be decided."
    },
    {
      "field": "product_B_chirality_excluded_rivals",
      "required": true,
      "source_identity": "cycle_1_chirality_screen",
      "expression": "V(omega_2) tensor V(omega_6)",
      "V_omega7_absent_by_chirality": true,
      "V_omega1_plus_omega7_absent_by_chirality": true,
      "full_rival_exclusions": false,
      "status": "partial",
      "admission_effect": "narrow_positive_only",
      "notes": "Chirality excludes two rows but is not promoted to a selector or full transcript."
    },
    {
      "field": "FC_IRR_verdict",
      "required": true,
      "source_identity": "finite_D7_transcript_or_formal_proof",
      "current_value": "blocked",
      "status": "blocked",
      "admission_effect": "blocks_selector_theorem",
      "notes": "Missing irreducibility proof or full kernel decomposition for ker(c)."
    },
    {
      "field": "FC_MULT_verdict",
      "required": true,
      "source_identity": "finite_D7_transcript_or_formal_proof",
      "current_value": "blocked",
      "status": "blocked",
      "admission_effect": "first_gate_block",
      "notes": "Missing product B full summands, multiplicities, dimensions, total check, and V(omega_6) multiplicity."
    },
    {
      "field": "FC_HW_verdict",
      "required": true,
      "source_identity": "finite_D7_transcript_or_formal_proof",
      "current_value": "blocked",
      "status": "blocked",
      "admission_effect": "blocks_selector_theorem",
      "notes": "Missing highest-weight proof or corrected recomputation for ker(c)."
    }
  ],
  "rival_exclusions": {
    "chirality_excludes_two_named_rivals": true,
    "chirality_promoted_to_selector": false,
    "full_rival_selector_exclusion_admitted": false,
    "reason": "full_A_B_decompositions_multiplicities_dimensions_and_same_chirality_rival_checks_absent"
  },
  "promotion_firewall": {
    "shiab_existence_not_selector_theorem": true,
    "chirality_exclusion_not_full_branching_transcript": true,
    "chirality_only_rejected_as_admission_basis": true,
    "target_generation_count_not_used": true,
    "desired_uniqueness_not_used": true,
    "target_import_not_used": true,
    "proof_restart_blocked": true,
    "GU_claim_not_promoted": true
  },
  "consequence_for_IG_GU": "IG_remains_conditional_on_RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1;_GU_claims_and_K_IG_selector_are_not_promoted.",
  "next_computation_or_proof_step": "Produce_raw_CAS_output_or_formal_D7_branching_proof_for_A_and_B_with_full_summands_multiplicities_dimensions_kernel_cokernel_highest_weight_irreducibility_rival_exclusions_and_FC_verdicts."
}
```
