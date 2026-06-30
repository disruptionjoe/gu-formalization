---
title: "Hourly 20260625 1302 Cycle 1 IG Selector Theorem"
date: "2026-06-25"
run_id: "hourly-20260625-1302"
cycle: 1
lane: 2
doc_type: ig_selector_theorem_attempt
artifact_id: "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
verdict: "CONDITIONAL_NOT_CLOSED"
owned_path: "explorations/hourly-20260625-1302-cycle1-ig-selector-theorem.md"
companion_audit: "tests/hourly_20260625_1302_cycle1_ig_selector_theorem_audit.py"
---

# Hourly 20260625 1302 Cycle 1 IG Selector Theorem

## 1. Verdict

Verdict: **conditional**.

The current repo sources do not prove
`SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1`. They do supply a
strong conditional route: the Cl(9,5) Shiab/Clifford contraction exists, the
UCSD source motivates a curvature-to-one-form middle map governed by Bianchi
structure, and the SC1/OQ1 line conditionally narrows the relevant
Spin(9,5)-equivariant Shiab hom-space. But the line does not close at source
grade because the multiplicity and highest-weight facts needed for uniqueness
are explicitly correction-gated, and even a closed uniqueness theorem would
still have to be identified with the `K_IG` codomain selector and tested against
all representation-natural rivals.

Decision state:

```text
artifact: SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1
run_id: hourly-20260625-1302
verdict_class: conditional
theorem_closed: false
source_natural_eliminations: 2
accepted_selector_count: 0
proof_restart_allowed: false
PTUJ_formula_packet_assumed: false
```

The two source-natural eliminations counted here are narrow: parity/chirality
exclusions of `Delta^-` and `V(omega_1+omega_7)` from
`Lambda^2 tensor Delta^+`. They are not rival-row eliminations for the full
0803 IG matrix.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md` and the five-lane runbook:

- compatibility, hosting, and target success data cannot be promoted into a
  derivation;
- proof restart is forbidden without an accepted source object, family identity,
  rival elimination, and non-import screen.

From `canon/shiab-existence-cl95.md` and `DERIVATION-PROGRESS.md`:

- the current canon signature is `(9,5)`;
- `Cl(9,5) ~= M(64,H)` and the spinor module is `S = H^64`;
- a real-linear, Spin(9,5)-equivariant, nonzero Shiab/Clifford contraction
  exists:

```text
Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S
```

- the canon file explicitly does not establish uniqueness of equivariant maps;
- the generation count and downstream physics remain separate open problems.

From `literature/weinstein-ucsd-2025-04-transcript.md`:

- the Bianchi identity motivates the desired automatic divergence-free behavior;
- Einstein's contraction is presented as a curvature-to-gauge-potential-like
  map;
- GU is described as needing a middle map from `omega_1` to
  `omega_{d-1}` in the rolled-up complex.

From `explorations/sc1-oq1-shiab-uniqueness-2026-06-23.md` and
`explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md`:

- the natural proof target is the hom-space
  `Hom_{Spin(9,5),H}(Lambda^2 tensor S, Lambda^1 tensor S)`;
- the Clebsch-Gordan attempt verifies the parity/chirality exclusions for
  `V(omega_7)` and `V(omega_1+omega_7)`;
- the same attempt leaves `FC-IRR`, `FC-MULT`, and `FC-HW` open, and
  `DERIVATION-PROGRESS.md` records the verdict correction from resolved to
  conditionally resolved.

From the 0803 rival-eliminator matrix:

- ten candidate/rival rows are already in scope;
- zero full row eliminations were accepted there;
- `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` is the first
  exact missing object.

## 3. Strongest positive result

The strongest positive result is:

```text
ConditionalShiabHomSpaceNarrowingForK_IGSelectorRoute_V1
```

It says the source side has more than a generic candidate. The canon supplies an
actual Cl(9,5) Shiab map. The UCSD source supplies the right qualitative role:
a middle operator turning curvature-type input into one-form/gauge-potential
type output with Bianchi-controlled conservation behavior. The SC1/OQ1A
calculation supplies exact chirality exclusions and a conditional path to
one-dimensionality for the chiral hom-space.

That is enough to make the selector route mathematically meaningful. It is not
enough to accept the selector theorem.

The positive result stops at:

```text
shiab_exists: true
middle_map_motivated: true
chirality_exclusions_verified: true
hom_space_uniqueness_verified: false
K_IG_family_identity_verified: false
full_rival_matrix_eliminated: false
```

## 4. First exact obstruction or missing proof object

The first exact obstruction is:

```text
VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1
```

This is narrower than the whole missing theorem. The selector theorem cannot
even start as a closed source-natural proof until this packet closes:

- `FC-IRR`: irreducibility of `ker(c)` in
  `Lambda^1 tensor Delta^- -> Delta^+`;
- `FC-MULT`: multiplicity one for `V(omega_6)` inside
  `V(omega_2) tensor V(omega_6)`;
- `FC-HW`: highest-weight assignment for `ker(c)`;
- the real-form/parity step relating the chiral halves and fixing whether the
  full Spin(9,5)/O(9,5) map is unique up to scalar;
- the Bianchi condition as an actual algebraic or differential selection rule,
  not merely a motivation.

After that packet, a second obstruction remains: family identity to
`SourceForcedCodomainSelectorForK_IG` plus row-by-row elimination of the 0803
representation-natural rival matrix. Current sources do not provide that
identity.

## 5. Constructive next object

The next object should be:

```text
LiEOrSageD7MultiplicityAuditForShiabHomSpace_V1
```

Required contents:

1. Compute the D7 decompositions:
   `V(omega_1) tensor V(omega_7)` and
   `V(omega_2) tensor V(omega_6)`.
2. Return multiplicities for `V(omega_6)`, `V(omega_7)`, and
   `V(omega_1+omega_7)`.
3. Prove or reject irreducibility of `ker(c)`.
4. Record exact command, tool version, root convention, Dynkin-label convention,
   and output transcript.
5. State whether the result upgrades SC1/OQ1A from conditional to verified.
6. Only if verified, add a second-stage theorem translating the resulting
   source map into `K_IG` selector fields and applying the 0803 rival matrix.

This object removes the first obstruction or turns it into a scoped fail.

## 6. Meaning for IG proof restart and surface identity work

IG proof restart is **not allowed** from the current state.

Surface identity work should also stay downstream. Manuscript, Oxford,
PTUJ/Keating, and UCSD surfaces can locate candidate formulas or motivate the
operator class, but the selector theorem must not assume a PTUJ formula packet
or use target physics to pick the answer. A surface can become a receipt only
after the source-natural selector rule exists and the formula is shown to be the
same family member, or a controlled non-identical member, under that rule.

Practical routing:

- do not restart `K_IG` proofs;
- do not promote the 0803 matrix rows as eliminated;
- do not treat the Cl(9,5) existence theorem as selection;
- do run the multiplicity/highest-weight audit before another broad source
  identity pass.

## 7. Next meaningful proof or computation step

Run a D7 representation computation for the SC1/OQ1A gates. The immediate test
is whether `FC-MULT` fires. If multiplicity is greater than one, the route
demotes from conditional to fail for uniqueness-based selection unless a new
Bianchi source rule distinguishes the extra maps. If multiplicity is one and
`ker(c)` is irreducible with the stated highest weight, then the next step is a
separate `K_IG` family-identity theorem and the full 0803 rival-row eliminator.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
  "artifact_id": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
  "run_id": "hourly-20260625-1302",
  "cycle": 1,
  "lane": 2,
  "verdict": "CONDITIONAL_NOT_CLOSED",
  "verdict_class": "conditional",
  "owned_path": "explorations/hourly-20260625-1302-cycle1-ig-selector-theorem.md",
  "companion_audit": "tests/hourly_20260625_1302_cycle1_ig_selector_theorem_audit.py",
  "starting_matrix": "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1",
  "required_selector_theorem": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
  "theorem_closed": false,
  "rival_rows_examined": [
    "displayed_or_canon_shiab_clifford_contraction",
    "exterior_covariant_derivative",
    "einstein_ricci_contraction_analog",
    "hodge_star_or_dimension_shift_analog",
    "symmetric_product_or_derivative",
    "projection_dependent_shiab_variant",
    "lower_order_dressed_variant",
    "oxford_visual_formula_variant",
    "ptuj_missing_sheet_variant",
    "ucsd_middle_map_variant"
  ],
  "rival_row_eliminations": [],
  "rival_row_elimination_count": 0,
  "source_natural_eliminations": [
    {
      "id": "chirality_excludes_Delta_minus_from_Lambda2_tensor_Delta_plus",
      "scope": "SC1_OQ1A_internal_representation_summand",
      "eliminates_full_0803_rival_row": false,
      "source_basis": "Clifford_even_chirality_parity"
    },
    {
      "id": "chirality_excludes_V_omega1_plus_omega7_from_Lambda2_tensor_Delta_plus",
      "scope": "SC1_OQ1A_internal_representation_summand",
      "eliminates_full_0803_rival_row": false,
      "source_basis": "Clifford_even_chirality_parity"
    }
  ],
  "source_natural_elimination_count": 2,
  "source_natural_eliminations_are_full_rival_rows": false,
  "accepted_selector_count": 0,
  "accepted_selectors": [],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "PTUJ_formula_packet_assumed": false,
  "target_physics_used": false,
  "strongest_positive_result": "ConditionalShiabHomSpaceNarrowingForK_IGSelectorRoute_V1",
  "positive_result_fields": {
    "shiab_exists": true,
    "middle_map_motivated": true,
    "chirality_exclusions_verified": true,
    "hom_space_uniqueness_verified": false,
    "K_IG_family_identity_verified": false,
    "full_rival_matrix_eliminated": false
  },
  "first_exact_obstruction": {
    "id": "VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1",
    "status": "missing",
    "blocks": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
    "open_failure_conditions": [
      "FC_IRR_ker_c_irreducibility",
      "FC_MULT_multiplicity_one_for_V_omega6",
      "FC_HW_highest_weight_of_ker_c",
      "real_form_parity_full_map_uniqueness",
      "Bianchi_selection_rule_not_merely_motivation"
    ]
  },
  "constructive_next_object": "LiEOrSageD7MultiplicityAuditForShiabHomSpace_V1",
  "proof_restart_rule": {
    "allowed_if": "accepted_selector_count_gt_0_and_full_rival_rows_eliminated_and_K_IG_family_identity_verified_and_target_physics_used_false_and_PTUJ_formula_packet_not_assumed",
    "current_conditions_met": false
  },
  "forbidden_promotions": [
    "compatibility_to_derivation",
    "hosting_to_selection",
    "shiab_existence_to_K_IG_selector",
    "PTUJ_locator_to_formula_packet",
    "target_physics_to_source_selector",
    "conditional_hom_space_to_full_rival_elimination"
  ],
  "next_meaningful_step": "Run_LiE_or_Sage_D7_multiplicity_audit_for_SC1_OQ1A_then_only_if_verified_attempt_K_IG_family_identity_and_full_0803_rival_eliminator."
}
```
