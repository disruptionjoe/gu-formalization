---
title: "Hourly 20260625 0703 Cycle 1 IG Rival Selector Eliminator Recheck"
date: "2026-06-25"
run_id: "hourly-20260625-0703"
cycle: 1
lane: 5
doc_type: ig_rival_selector_eliminator_recheck
artifact_id: "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1"
verdict: "UNDERDEFINED_HOSTED_SHIAB_CANDIDATE_NOT_SELECTED"
owned_path: "explorations/hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md"
companion_audit: "tests/hourly_20260625_0703_cycle1_ig_rival_selector_eliminator_recheck_audit.py"
---

# Hourly 20260625 0703 Cycle 1 IG Rival Selector Eliminator Recheck

## 1. Verdict

Verdict: **underdefined**.

The current repo sources support a strong hosted Shiab candidate, but they do
not execute `ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1`.
The missing object is not a minor citation gap. It is the rule that would have
to eliminate source-natural rival selector/codomain classes and identify the
hosted Shiab row with `SourceForcedCodomainSelectorForK_IG`.

Decision state:

```text
artifact_id: ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1
accepted_receipt_count: 0
selector_identity_passed: false
surviving_rival_count: 6
proof_restart_allowed: false
hosted_shiab_status: hosted_candidate_not_selected
first_obstruction: missing source-emitted representation-theory/Bianchi/projection rival-eliminator object
```

This artifact does not demote Shiab existence. It prevents a different
overclaim: the hosted Shiab candidate cannot be treated as the selected/final
IG codomain until a source-side eliminator defeats the rivals.

## 2. Specific GU Claim/Bridge Under Test

Claim under test:

```text
Author-manuscript representation/Bianchi/Summary material eliminates rival
source-natural selectors/codomains and identifies the hosted Shiab candidate
with SourceForcedCodomainSelectorForK_IG.
```

Bridge being tested:

```text
Manuscript Sections 5/8/9/Summary
  -> representation-theory/Bianchi/projection selector
  -> rival-class elimination
  -> family identity to SourceForcedCodomainSelectorForK_IG
  -> IG proof-restart eligibility
```

The bridge does not close from the available repo sources.

## 3. Owned Output Path And Sources Read First

Owned output path:

```text
explorations/hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md
```

Owned audit path:

```text
tests/hourly_20260625_0703_cycle1_ig_rival_selector_eliminator_recheck_audit.py
```

Sources read first:

| source | decision relevance |
| --- | --- |
| `RESEARCH-POSTURE.md` | Requires constructive pursuit but forbids compatibility-as-derivation and target-data import. |
| `process/runbooks/five-lane-frontier-run.md` | Requires decision-grade lane output, exact obstruction, and no "hosted by" to "selected by" promotion. |
| `explorations/hourly-20260625-0601-cycle3-next-frontier-object-dependency-dag.md` | Names this object as the next IG frontier and forbids proof restart until accepted receipts exist. |
| `explorations/hourly-20260625-0601-cycle2-ig-selector-rival-eliminator-matrix.md` | Supplies the prior rival matrix and the missing `ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1`. |
| `explorations/hourly-20260625-0601-cycle1-author-manuscript-ig-selector-identity-packet.md` | Supplies manuscript locators and the failed identity packet for `SourceForcedCodomainSelectorForK_IG`. |
| `explorations/hourly-cycle3-k-ig-codomain-finality-certificate-2026-06-25.md` | Establishes that `K_IG = D_A U` is admissible but not final; codomain finality and rival elimination remain open. |
| `canon/shiab-existence-cl95.md` | Canonically supports real Shiab existence in the Cl(9,5) setting while leaving uniqueness of equivariant maps open. |

## 4. Strongest Positive Construction Attempt

The strongest positive route is the manuscript-hosted Shiab normalization:

```text
Section 5.3-5.4:
  inhomogeneous gauge/action and augmented torsion context

Section 8:
  Shiab family, invariant-subspace, and operator-choice surface

Section 9.1:
  typed displayed Shiab candidate
  Omega^2(Y, ad) -> Omega^{d-1}(Y, ad)

Summary:
  projection-removal and Einstein/Ricci comparison context
```

Under a favorable reading, Section 8 is the intended location of the missing
representation-theory/highest-weight/Bianchi computation, Section 9 displays
the best typed candidate, and the Summary shows that projection loss mattered
to the author.

That gives a real positive construction:

```text
The author manuscript hosts a source-located, typed Shiab/codomain candidate
that is plausible enough to test against the K_IG selector schema.
```

It does not give the needed stronger construction:

```text
The author manuscript source-forces exactly one K_IG codomain/selector and
eliminates all source-natural rivals.
```

The canon Shiab result strengthens existence, not selector identity. It states
that the Clifford contraction Shiab exists over the real Cl(9,5) setting, but it
also records that uniqueness of equivariant maps is open. That open uniqueness
question aligns with, rather than closes, the rival-selector obstruction.

## 5. Explicit Rival-Class Table

| rival class | source-natural candidate shape | positive source surface | eliminator required | eliminator found? | status |
| --- | --- | --- | --- | ---: | --- |
| exterior derivative | `D_A U`-style exterior/covariant derivative with 2-form codomain | `K_IG = D_A U` is the strongest typed exterior witness in the finality certificate; Shiab input starts at `Omega^2` | source rule proving exterior 2-form codomain and exterior principal symbol are selected | no | survives as admissible candidate, not final |
| coderivative / trace / scalar contraction | coderivative, trace, divergence, or scalar contraction class | Einstein/Ricci comparison and projection language make contraction-style readings source-natural | rule excluding contraction/trace/zero-form codomains before target comparison | no | survives |
| symmetric derivative | symmetric-gradient, strain-like, or trace-free symmetric derivative | first-order gauge-covariant derivatives are not source-excluded by the current interface | representation/Bianchi rule forcing antisymmetric exterior degree as the only parent-coupled derivative | no | survives |
| projected derivative | derivative followed by projection, quotient, or projection-removal policy | Summary eqs. 12.2-12.7 provide projection-removal context | projector/loss theorem proving no projected first-order class can be the selected source object | no | survives |
| lower-order dressed exterior | exterior principal part plus algebraic, torsion, curvature, or gauge lower-order additions | Section 5 torsion/action material makes source-natural lower-order dressing plausible | lower-order rigidity or normalization policy fixing/forbidding additions | no | survives |
| displayed Shiab codomain | hosted displayed map `Omega^2(Y, ad) -> Omega^{d-1}(Y, ad)` | Section 9.1 gives the strongest typed Shiab candidate; canon supports Shiab existence | family identity witness from displayed Shiab to `SourceForcedCodomainSelectorForK_IG` plus eliminators for the other rows | no | hosted candidate, not selected |

No rival class is eliminated by a source-emitted rule in the current repo
sources. Therefore the hosted Shiab candidate cannot be promoted to the
selected or final codomain.

## 6. First Exact Obstruction Or Missing Proof/Source Object

First obstruction:

```text
ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1 is not present
as a source-emitted object.
```

The missing object must provide all of the following before any proof restart:

```text
candidate family under comparison
representation-theory/highest-weight or equivalent selector
Bianchi identity selection criterion
selected Shiab formula or selected family member
selected K_IG codomain or explicit Shiab-to-K_IG bridge
parent momentum degree
principal-symbol class
projector policy
projection-loss behavior
lower-order freedom policy
eliminators for exterior, coderivative/trace, symmetric, projected, and lower-order dressed classes
family identity to SourceForcedCodomainSelectorForK_IG
```

The obstruction sits upstream of downstream physics. It appears before
`Q_IG`, parent action normalization, boundary variation, theta/FLRW
coefficients, or physical recovery.

## 7. What Would Change If The Hole Closed

If the hole closed with a source-emitted eliminator and identity witness:

- `accepted_receipt_count` could become `1` for this source row.
- `selector_identity_passed` could become `true`.
- `surviving_rival_count` would have to fall to `0` or to a explicitly harmless
  equivalence class.
- `SourceForcedCodomainSelectorForK_IG` would receive a source-side family
  identity candidate.
- IG proof restart could become conditionally allowed, but only after receipt
  review confirms no target import.

Closing this hole would not prove theta/FLRW, dark energy, or downstream
physical recovery. It would only open the next IG selector proof gate.

## 8. What Would Falsify Or Demote The Route

Demote the manuscript-hosted route if any of these are established:

- Section 8 does not actually contain a representation-theory, highest-weight,
  Bianchi, invariant-subspace, or operator-choice surface.
- The displayed Shiab map is only a readout/comparison operator and has no
  source-side identity to the `K_IG` selector.
- The Summary projection-removal equations are only downstream comparison and
  provide no selector-relevant projector policy.
- The Cl(9,5) Shiab existence map is not unique and the source does not select
  among multiple equivariant maps.
- Any source-natural rival remains admissible after all recovered manuscript
  rules are applied.
- The Shiab-to-`SourceForcedCodomainSelectorForK_IG` bridge requires target
  physics, desired coefficients, or downstream proof success.

Under those outcomes, the manuscript row remains hosted/underdefined or becomes
a scoped fail for this bridge. No global GU no-go follows from this artifact
alone.

## 9. Next Meaningful Computation Or Proof/Source Step

The next meaningful step is a source-window extraction and representation
inventory, not a downstream proof replay:

1. Re-extract Section 8 eqs. 8.1-8.7, Section 9.1 eqs. 9.2-9.6, and Summary
   eqs. 12.2-12.7 from the acquired manuscript object.
2. Build a typed operator inventory: domain, codomain, principal symbol,
   parent momentum degree, projection behavior, lower-order freedom, and
   required geometric data.
3. Compute or cite the representation-theory/Bianchi selection rule for the
   relevant operator family.
4. Test each rival class in the table against only source-emitted eliminators.
5. If all rivals are eliminated and the family identity is source-clean, route
   the row to receipt review. Otherwise keep proof restart forbidden.

Next frontier object:

```text
SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1
```

## 10. JSON Summary

```json
{
  "artifact": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1",
  "run_id": "hourly-20260625-0703",
  "cycle": 1,
  "lane": 5,
  "artifact_id": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1",
  "verdict": "UNDERDEFINED_HOSTED_SHIAB_CANDIDATE_NOT_SELECTED",
  "claim_under_test": "author-manuscript representation/Bianchi/Summary material eliminates rival source-natural selectors/codomains and identifies the hosted Shiab candidate with SourceForcedCodomainSelectorForK_IG",
  "owned_path": "explorations/hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md",
  "rival_classes": [
    {
      "id": "exterior_derivative",
      "candidate_shape": "D_A_U_style_exterior_or_covariant_derivative_with_2_form_codomain",
      "positive_surface": "K_IG_D_A_U_is_strongest_typed_exterior_witness_and_Shiab_input_starts_at_Omega2",
      "eliminator_required": "source_rule_proving_exterior_2_form_codomain_and_exterior_principal_symbol_are_selected",
      "eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "coderivative_trace_scalar",
      "candidate_shape": "coderivative_trace_divergence_or_scalar_contraction_class",
      "positive_surface": "Einstein_Ricci_comparison_and_projection_language_make_contraction_readings_source_natural",
      "eliminator_required": "rule_excluding_contraction_trace_zero_form_codomains_before_target_comparison",
      "eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "symmetric_derivative",
      "candidate_shape": "symmetric_gradient_strain_like_or_trace_free_symmetric_derivative",
      "positive_surface": "first_order_gauge_covariant_derivatives_are_not_source_excluded_by_current_interface",
      "eliminator_required": "representation_Bianchi_rule_forcing_antisymmetric_exterior_degree_as_only_parent_coupled_derivative",
      "eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "projected_derivative",
      "candidate_shape": "derivative_followed_by_projection_quotient_or_projection_removal_policy",
      "positive_surface": "Summary_projection_removal_context",
      "eliminator_required": "projector_loss_theorem_excluding_projected_first_order_classes",
      "eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "lower_order_dressed_exterior",
      "candidate_shape": "exterior_principal_part_plus_algebraic_torsion_curvature_or_gauge_lower_order_additions",
      "positive_surface": "Section_5_torsion_action_material_makes_lower_order_dressing_source_natural",
      "eliminator_required": "lower_order_rigidity_or_normalization_policy",
      "eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "displayed_shiab_codomain",
      "candidate_shape": "Omega^2(Y,ad)->Omega^{d-1}(Y,ad)",
      "positive_surface": "Section_9_1_typed_Shiab_candidate_and_canon_Shiab_existence",
      "eliminator_required": "family_identity_witness_to_SourceForcedCodomainSelectorForK_IG_plus_other_rival_eliminators",
      "eliminator_found": false,
      "status": "hosted_candidate_not_selected"
    }
  ],
  "surviving_rival_count": 6,
  "accepted_receipt_count": 0,
  "selector_identity_passed": false,
  "proof_restart_allowed": false,
  "first_obstruction": "missing source-emitted representation-theory/Bianchi/projection rival-eliminator object selecting the displayed Shiab codomain and eliminating source-natural rival classes for SourceForcedCodomainSelectorForK_IG",
  "missing_source_object": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
  "next_frontier_object": "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1",
  "companion_audit": "tests/hourly_20260625_0703_cycle1_ig_rival_selector_eliminator_recheck_audit.py"
}
```
