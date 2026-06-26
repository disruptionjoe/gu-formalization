---
title: "Hourly 20260626 1102 Cycle 3 KIG Source-Selection Boundary Certificate"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 3
lane: 3
doc_type: "frontier_run_lane_artifact"
artifact_id: "KIGSourceSelectionBoundaryCertificate_1102_C3_L3_V1"
verdict: "certificate_defined_applied_no_source_selected_branch3_candidate"
owned_path: "explorations/hourly-20260626-1102-cycle3-kig-source-selection-boundary-certificate.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 3 KIG Source-Selection Boundary Certificate

## 1. Verdict

Verdict: **closed certificate / applied rejection**.

This artifact defines:

```text
KIGSourceSelectionBoundaryCertificate_V1
```

as the compact boundary certificate a future K_IG source-row candidate must
satisfy to move from:

```text
reconstruction-only Branch 3 host
```

to:

```text
source-selected Branch 3 admission.
```

The certificate is defined and applied to the current repo state. No candidate
passes.

Current decision state:

```text
certificate_defined: true
certificate_applied: true
source_selection_candidate_present: false
source_selected_branch3_admitted: false
rival_parent_classes_closed: false
source_row_passing_firewall_allowed: false
trace_eliminator_retry_allowed: false
exact_gr_restart_allowed: false
theta_restart_allowed: false
target_import_used: false
claim_status_change: false
```

The strongest admissible object remains:

```text
K_IG^rec(U; A) = D_A U
P_IG^rec in Omega^2(Y, ad P)
S_parent,rec = int_Y <P_IG^rec, D_A U> - ...
```

as a reconstruction-only exterior parent-action template. It is not
source-selected and cannot be used to restart trace exclusion, exact GR, or
theta/FLRW work.

## 2. What Was Derived Directly From Repo Sources

The posture and runbook set the governing logic: constructive obstruction work
is allowed, but compatibility, target success, and action cleanliness are not
derivations. Frontier rows must state exact obstructions, rollback conditions,
and no claim-status drift unless a claim really changes.

The predecessor K_IG chain gives these direct facts:

| repo source | direct fact used |
|---|---|
| `RESEARCH-POSTURE.md` | Construct missing objects aggressively, but do not treat compatibility, target utility, or hidden target data as proof. |
| `process/runbooks/five-lane-frontier-run.md` | A lane must produce a decision-grade artifact with a verdict, exact obstruction, constructive next object, terrain, forbidden shortcut, invariant, kill condition, and witness shape. |
| `hourly-20260626-1102-cycle1-kig-parent-variation-acquisition-extraction-row.md` | The acquired local 2021 author draft supplies one-form IG/gauge-potential geometry, augmented torsion, Shiab/action/deformation rows, but no pre-codomain parent degree row for `ParentVariationSlot_IG = Omega^2(Y, ad P)`. |
| `hourly-20260626-1102-cycle2-kig-reconstruction-only-parent-action-boundary.md` | The repo may host an exterior Branch 3 parent action only as reconstruction-only. No pre-codomain source row means no source-selected Branch 3 and no source-row-passing rival-parent firewall. |
| `hourly-20260626-1003-cycle3-kig-primary-source-locator-row.md` | No repo-local primary/source-equivalent row locates a Branch 3 parent variation slot with `degree(P_IG)=2` before selected codomain or `K_IG = D_A U`. |
| `hourly-20260626-1003-cycle2-kig-parent-variation-source-locator-receipt.md` | `KIGParentVariationSourceLocatorReceipt_V1` did not close: no acceptable source locator emitted the exterior parent slot before codomain/operator selection. |
| `hourly-20260626-1003-cycle1-kig-source-row-rival-parent-firewall-test.md` | `SourceRowPassingKIGRivalParentFirewall_V1` is blocked because `source_locator_present`, `parent_slot_pre_codomain_present`, and `exterior_degree_rule_present` are false. |
| `hourly-20260626-0904-cycle3-kig-rival-parent-firewall.md` | A future row must include source locator, parent slot before codomain/operator selection, degree 2 or equivalent exterior slot statement, noncircularity, rival treatment, target-replacement guard, and rollback. |
| `hourly-20260626-0803-cycle3-kig-parent-degree-selector.md` | The independent selector `degree(P_IG)=2 before selected_codomain` is not admitted; the degree-2 parent is conditional on `K_IG = D_A U` or exterior codomain. |
| `hourly-20260626-0803-cycle1-kig-positive-exterior-degree-rule.md` | Positive exterior degree is not source-forced; `CODERIVATIVE_TRACE` remains the first live rival. |

No source extraction was retried here. No trace/coderivative exclusion was
retried here. This lane only defines and applies the boundary certificate from
the repo's existing negative and reconstruction-only rows.

## 3. Boundary Certificate Fields and Verifier Predicate

Certificate name:

```text
KIGSourceSelectionBoundaryCertificate_V1
```

Purpose:

```text
Decide whether a future source-row candidate upgrades Branch 3 from
reconstruction-only host status to source-selected admission.
```

### Required Public Fields

| field | required content |
|---|---|
| `candidate_id` | Stable identifier for the candidate source row. |
| `source_kind` | `official_primary`, `author_draft`, `lawful_local_transcript`, `rendered_visual_frame`, or explicitly justified source-equivalent repo artifact. |
| `source_id` | Stable source handle, local path, transcript identifier, manuscript identifier, or accepted repo artifact. |
| `custody` | Hash for byte sources, local path, transcript capture metadata, or enough provenance for re-check. |
| `exact_locator` | Page/equation/timestamp/frame/section/line locator precise enough to independently inspect. |
| `source_text_or_formula` | Faithful text/formula extraction or transcription sufficient to verify the emitted object. |
| `emitted_object` | `ParentVariationSlot_IG = Omega^2(Y, ad P)` or exact source-equivalent Branch 3 parent momentum / parent variation slot. |
| `degree_statement` | `degree(P_IG)=2`, `P_IG in Omega^2(Y, ad P)`, or a source-equivalent exterior 2-form parent slot. |
| `order_log` | Proof that the parent slot and degree are emitted before `selected_codomain`, before `K_IG = D_A U`, and before exact-GR/theta/trace utility. |
| `operator_relation` | States whether the row selects `K_IG`, selects only parent degree, or only makes the firewall evaluable. |
| `rival_parent_ledger` | Explicit status of all live rival parent classes listed below. |
| `target_replacement_guard` | Exact-GR, theta/FLRW, Lambda/DESI, residual, chirality, generation, and coefficient labels can be replaced by neutral labels without changing the emitted row. |
| `anti_smuggling_guard` | No target performance, action elegance, or reconstruction convenience is used to select source row, degree, operator, or rival elimination. |
| `rollback_conditions` | Exact conditions under which the candidate loses source-selected status. |

### Live Rival Parent Classes

The candidate must close or source-irrelevantize all of:

| rival class | schematic form | why it remains live before the certificate |
|---|---|---|
| `ZERO_FORM_PARENT` | parent paired with a 0-form output | not excluded until the parent slot is source-fixed to exterior 2-forms. |
| `CODERIVATIVE_TRACE` | `D_A^* U` or `trace_g(nabla_A U)` | first blocking rival; 0-form/trace-sector route is not source-excluded. |
| `SYMMETRIC_DERIVATIVE` | `Sym(nabla_A U)`, possibly trace-free | symmetric-tensor parent slot remains possible if metric/connection data are admitted. |
| `PROJECTED_DERIVATIVE` | `Pi_{s,epsilon}(nabla_A U)` or projected `D_A U` | source projectors/loss policies are named but not final. |
| `LOWER_ORDER_DRESSED_EXTERIOR` | `D_A U + L_{s,epsilon}(U)` | same exterior degree can survive with lower-order source-natural dressing. |

### Acceptance Predicate

The verifier accepts a candidate iff all conditions hold:

```text
accept(candidate) iff
  stable_source(candidate)
  and exact_locator_recheckable(candidate)
  and emits_branch3_parent_slot(candidate)
  and emits_degree_2(candidate)
  and pre_codomain_order(candidate)
  and noncircular_from_D_A_U(candidate)
  and closes_rival_parent_classes(candidate)
  and target_replacement_invariant(candidate)
  and anti_smuggling_guard_passes(candidate)
  and rollback_conditions_declared(candidate).
```

Expanded predicates:

```text
stable_source(candidate):
  source_kind, source_id, custody, and locator are stable enough for an
  independent reader to re-check the row.

exact_locator_recheckable(candidate):
  locator points to the exact text/formula/frame/table row that emits the
  parent slot, not merely to a broad source surface.

emits_branch3_parent_slot(candidate):
  source_text_or_formula emits a Branch 3 parent variation / parent momentum
  slot, not merely torsion, curvature, Shiab input, deformation-complex
  codomain, or a downstream reconstruction template.

emits_degree_2(candidate):
  source_text_or_formula states or source-equivalently forces
  degree(P_IG)=2 or P_IG in Omega^2(Y, ad P).

pre_codomain_order(candidate):
  the parent slot and degree are emitted before selected_codomain,
  before K_IG = D_A U, before trace exclusion, before exact-GR, and before
  theta/FLRW utility.

noncircular_from_D_A_U(candidate):
  degree(P_IG)=2 is not inferred from D_A U being a 2-form, from the exterior
  codomain already being selected, from parent-action cleanliness, or from
  reconstruction convenience.

closes_rival_parent_classes(candidate):
  ZERO_FORM_PARENT, CODERIVATIVE_TRACE, SYMMETRIC_DERIVATIVE,
  PROJECTED_DERIVATIVE, and LOWER_ORDER_DRESSED_EXTERIOR are each
  source-excluded or made irrelevant by the same candidate row.

target_replacement_invariant(candidate):
  replacing exact-GR, theta/FLRW, Lambda/DESI, residual, chirality,
  generation, and coefficient labels by neutral labels leaves the source row,
  parent slot, degree, and rival treatment unchanged.

anti_smuggling_guard_passes(candidate):
  no target behavior, coefficient match, Standard Model/chirality success,
  generation count, exact-GR success, theta/FLRW behavior, or aesthetic
  action preference is used upstream.

rollback_conditions_declared(candidate):
  candidate declares exact revocation conditions for source instability,
  ambiguous locator, circular degree inference, surviving rivals, or target
  import.
```

### Admission Consequence

If accepted:

```text
source_selection_candidate_present: true
source_selected_branch3_admitted: true only for the row's stated scope
source_row_passing_firewall_allowed: true
trace_eliminator_retry_allowed: true only after rival ledger says the trace
  class is source-excluded or evaluable by degree mismatch
exact_gr_restart_allowed: still requires the full source-selected action
  packet, currents, coefficients, boundary data, and reduction data
theta_restart_allowed: still requires the full source-selected action packet,
  coefficient/current data, and FLRW reduction data
```

If rejected:

```text
Branch 3 remains reconstruction-only.
K_IG^rec = D_A U may remain as a candidate template.
No source-selected K_IG claim is admitted.
No trace/exact-GR/theta restart is allowed from this gate.
```

## 4. Strongest Positive Construction Attempt

The strongest positive construction allowed by current repo sources is:

```text
Data:
  Y = current GU source-space baseline
  P -> Y
  A in Conn(P)
  U in Omega^1(Y, ad P)
  P_IG^rec in Omega^2(Y, ad P)
  Q_IG^rec an Ad-invariant pairing, template-level
  Z_U^rec a reconstruction coefficient

Candidate operator:
  K_IG^rec(U; A) = D_A U in Omega^2(Y, ad P)

Parent action template:
  S_parent,rec[A,U,P_IG^rec]
    =
      int_Y <P_IG^rec, D_A U>_{Q_IG^rec}
      - (1/(2 Z_U^rec)) int_Y <P_IG^rec, P_IG^rec>_{Q_IG^rec}
      + S_src,rec
      + S_boundary,rec.
```

This is positive because it is typed, local, gauge-covariant, first-order at
the parent level, and matches the source-adjacent one-form geometry found in
the local GU draft and repo action-spine artifacts.

It does not pass the source-selection boundary because its degree order is:

```text
choose K_IG^rec = D_A U
  -> D_A U is an exterior 2-form
  -> matching parent P_IG^rec is in Omega^2(Y, ad P).
```

The certificate requires the reverse order:

```text
source row
  -> selected Branch 3 parent variation slot is exterior 2-form valued
  -> degree(P_IG)=2
  before selected_codomain
  before K_IG = D_A U
  before downstream target utility.
```

Therefore the strongest current construction is a witness for
reconstruction-only host status, not a witness for source-selected Branch 3.

## 5. First Exact Obstruction or Missing Object

First exact obstruction:

```text
PreCodomainParentMomentumDegreeSourceRow_V1.absent
```

Equivalent missing object:

```text
No current repo-local primary/source-equivalent row emits:

  ParentVariationSlot_IG = Omega^2(Y, ad P)
  degree(P_IG)=2

before:

  selected_codomain = Omega^2(Y, ad P)
  K_IG = D_A U
  exterior operator/codomain selection
  trace/coderivative exclusion
  exact-GR utility
  theta/FLRW utility.
```

This missing object appears before the firewall, before trace elimination,
before exact-GR restart, and before theta restart.

Current candidate application:

| candidate class in current repo | passes certificate? | first failed predicate |
|---|---:|---|
| reconstruction-only exterior parent action `K_IG^rec = D_A U` | no | `noncircular_from_D_A_U` fails; degree is downstream of operator/codomain choice. |
| acquired 2021 draft one-form/action/deformation rows | no | `emits_branch3_parent_slot` fails; rows emit one-form geometry and action/deformation data, not `P_IG` parent degree. |
| primary source locator row from cycle 1003/c3 | no | `stable_source` and `exact_locator_recheckable` for the target object fail because no locator row was found. |
| parent variation source locator receipt from cycle 1003/c2 | no | `emits_degree_2` and `pre_codomain_order` fail; no acceptable locator emitted degree 2 before codomain/operator selection. |
| rival-parent firewall from cycle 0904/c3 | no candidate to accept | firewall fields are defined, but `SourceRowPassingKIGRivalParentFirewall_V1` remains missing. |
| positive exterior degree rule / parent degree selector rows | no | selected parent momentum degree is not source-forced independently of selected codomain. |

No current source-selection candidate is present. No candidate passes.

## 6. Constructive Next Object

Build:

```text
PreCodomainParentMomentumDegreeSourceRow_V1
```

This is narrower than a full physics restart and earlier than trace exclusion.
It should be a source row, not a reconstruction template.

Minimum object:

| field | required content |
|---|---|
| `source_kind` | Primary/source-equivalent GU action, manuscript, transcript/frame, or accepted source artifact. |
| `source_id` | Stable identifier and custody metadata. |
| `exact_locator` | Page/equation/timestamp/frame/table locator. |
| `source_text_or_formula` | Faithful row that can be independently re-checked. |
| `emitted_object` | Branch 3 parent variation or parent momentum slot. |
| `degree_statement` | `degree(P_IG)=2`, `P_IG in Omega^2(Y, ad P)`, or exact exterior-slot equivalent. |
| `order_log` | Statement appears before selected codomain, before `K_IG = D_A U`, and before target claims. |
| `notation_bridge` | Explains whether the source notation is `P_IG`, parent momentum, first-order auxiliary, variation slot, or another exact equivalent. |
| `rival_parent_effect` | Handles `ZERO_FORM_PARENT`, `CODERIVATIVE_TRACE`, `SYMMETRIC_DERIVATIVE`, `PROJECTED_DERIVATIVE`, and `LOWER_ORDER_DRESSED_EXTERIOR`. |
| `target_replacement_guard` | Row survives replacing downstream target labels by neutral labels. |
| `rollback_condition` | Revokes the row if degree 2 is inferred from `D_A U`, selected codomain, formal template convenience, or target behavior. |

Sequential use:

```text
PreCodomainParentMomentumDegreeSourceRow_V1
  -> KIGSourceSelectionBoundaryCertificate_V1
  -> SourceRowPassingKIGRivalParentFirewall_V1
  -> TraceContractionExclusionLemmaForK_IG_V1, only if allowed
  -> exact-GR/theta restarts, only after the full source-selected action packet.
```

Do not parallelize a trace, exact-GR, or theta restart against this step. Those
lanes depend on this row passing first.

## 7. Meaning for K_IG/Trace/Exact-GR/Theta Claims

Allowed current statement:

```text
The repo hosts a coherent reconstruction-only exterior Branch 3 parent action
with K_IG^rec = D_A U and P_IG^rec in Omega^2(Y, ad P), provided it is
quarantined from source-selected claims.
```

Forbidden current statements:

```text
GU source rows select K_IG = D_A U.
GU source rows select degree(P_IG)=2 before codomain/operator choice.
GU source rows select source-selected Branch 3.
The exterior parent action passes SourceRowPassingKIGRivalParentFirewall_V1.
CODERIVATIVE_TRACE is eliminated.
SYMMETRIC_DERIVATIVE is eliminated.
PROJECTED_DERIVATIVE is eliminated.
LOWER_ORDER_DRESSED_EXTERIOR is eliminated.
Exact-GR restart is allowed from this gate.
Theta/FLRW restart is allowed from this gate.
The reconstruction-only action changes claim status.
```

Meaning by claim family:

| claim family | current meaning |
|---|---|
| `K_IG` | `D_A U` remains strongest exterior reconstruction candidate; not source-selected. |
| trace/coderivative | retry barred; `CODERIVATIVE_TRACE` remains live until a source-side exterior parent degree is fixed before targets. |
| exact-GR | restart barred; a template action is not a source-selected action packet, current, boundary, or reduction theorem. |
| theta/FLRW | restart barred; no source-selected Branch 3 coefficient/current packet exists. |
| claim status | no promotion, demotion, or status-file workflow is triggered by this certificate. |

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain:

```text
primary: provenance-verifier
secondary: source-selection boundary certificate
secondary: smooth-variational parent-action typing
secondary: rival-parent class closure
barred downstream: trace elimination, exact-GR, theta/FLRW
```

Forbidden shortcut:

```text
Do not promote K_IG^rec = D_A U to K_IG^src because it is natural,
gauge-covariant, first-order, action-friendly, cleaner than trace,
compatible with one-form source geometry, useful for exact GR, useful for
theta/FLRW, or aligned with downstream coefficient behavior.
```

Invariant:

```text
source-selection boundary invariant:

  after exact-GR, theta/FLRW, Lambda/DESI, residual, chirality, generation,
  and coefficient labels are replaced by neutral labels, the certificate must
  still distinguish:

    reconstruction-only exterior template: allowed
    source-selected Branch 3: absent unless a source row passes
    rival-parent firewall: barred unless all certificate predicates pass
    trace/exact-GR/theta restart: barred unless their upstream gates pass
```

Kill condition for this current rejection:

```text
A stable primary/source-equivalent row is found whose exact source text or
formula emits the Branch 3 parent variation / parent momentum slot as exterior
2-form valued, with degree(P_IG)=2 before selected_codomain and before
K_IG = D_A U, and whose same row closes or source-irrelevantizes all live rival
parent classes without target import.
```

Rollback conditions for any future accepted candidate:

```text
R1. Roll back if the source locator is unstable, broad, ambiguous, or cannot be
    independently re-checked.

R2. Roll back if the emitted object is torsion, curvature, Shiab input,
    deformation-complex codomain, or reconstruction template rather than a
    Branch 3 parent variation / parent momentum slot.

R3. Roll back if degree(P_IG)=2 is inferred from K_IG = D_A U, selected
    codomain, exterior-template convenience, action cleanliness, or target
    behavior.

R4. Roll back if ZERO_FORM_PARENT or CODERIVATIVE_TRACE remains source-possible
    before source selection.

R5. Roll back if SYMMETRIC_DERIVATIVE remains source-possible before source
    selection.

R6. Roll back if PROJECTED_DERIVATIVE remains source-possible before source
    selection.

R7. Roll back if LOWER_ORDER_DRESSED_EXTERIOR remains source-possible and the
    row does not fix or forbid the lower-order dressing.

R8. Roll back if exact-GR, theta/FLRW, Lambda/DESI, residual, chirality,
    generation count, or coefficient matching is used to select the row,
    degree, operator, or rival elimination.

R9. Roll back if a reconstruction-only symbol is cited downstream without the
    `^rec` quarantine marker or is silently reused as `^src`.
```

## 9. Certificate/Witness Shape

Certificate:

```text
KIGSourceSelectionBoundaryCertificate_V1
```

Public inputs:

```text
RESEARCH-POSTURE.md
process/runbooks/five-lane-frontier-run.md
K_IG predecessor artifacts through hourly-20260626-1102/cycle2
candidate source row
candidate rival parent ledger
target labels replaced by neutral labels
```

Witness shape for acceptance:

```text
source_witness:
  source_kind
  source_id
  custody
  exact_locator
  source_text_or_formula
  emitted_object = Branch 3 parent variation / parent momentum slot
  degree_statement = degree(P_IG)=2 or P_IG in Omega^2(Y, ad P)
  order_log before selected_codomain and before K_IG = D_A U

rival_witness:
  ZERO_FORM_PARENT status
  CODERIVATIVE_TRACE status
  SYMMETRIC_DERIVATIVE status
  PROJECTED_DERIVATIVE status
  LOWER_ORDER_DRESSED_EXTERIOR status
  source-exclusion or source-irrelevance proof for each

boundary_witness:
  target_replacement_guard
  anti_smuggling_guard
  rollback_conditions
```

Verifier predicate:

```text
KIGSourceSelectionBoundaryCertificate_V1.accepts(candidate)
  iff accept(candidate) from Section 3 evaluates true.
```

Semantic lift if accepted:

```text
The candidate may move from reconstruction-only comparator to source-selected
Branch 3 row for its exact stated scope. It does not automatically prove exact
GR, theta/FLRW, coefficient recovery, or all downstream physics.
```

Current verifier result:

```text
reject all present candidates:
  no source-selection candidate is present in the current repo state;
  the only exterior Branch 3 object is reconstruction-only.
```

Anti-smuggling guard:

```text
No use of exact-GR success, theta/FLRW behavior, Lambda/DESI behavior,
xi_eff, residual placement, Standard Model/chirality success, generation count,
coefficient matching, or clean action aesthetics may select the source row,
degree, operator, or rival elimination.
```

## 10. JSON Summary

```json
{
  "artifact_id": "KIGSourceSelectionBoundaryCertificate_1102_C3_L3_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 3,
  "lane": 3,
  "artifact_path": "explorations/hourly-20260626-1102-cycle3-kig-source-selection-boundary-certificate.md",
  "verdict": "certificate_defined_applied_no_source_selected_branch3_candidate",
  "certificate_defined": true,
  "certificate_applied": true,
  "source_selection_candidate_present": false,
  "source_selected_branch3_admitted": false,
  "rival_parent_classes_closed": false,
  "source_row_passing_firewall_allowed": false,
  "trace_eliminator_retry_allowed": false,
  "exact_gr_restart_allowed": false,
  "theta_restart_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "source_extraction_retried": false,
  "trace_exclusion_retried": false,
  "strongest_positive_construction": "reconstruction_only_exterior_parent_action_K_IG_rec_equals_D_A_U",
  "first_exact_obstruction": "PreCodomainParentMomentumDegreeSourceRow_V1.absent",
  "constructive_next_object": "PreCodomainParentMomentumDegreeSourceRow_V1",
  "live_rival_parent_classes": [
    "ZERO_FORM_PARENT",
    "CODERIVATIVE_TRACE",
    "SYMMETRIC_DERIVATIVE",
    "PROJECTED_DERIVATIVE",
    "LOWER_ORDER_DRESSED_EXTERIOR"
  ],
  "acceptance_predicates": [
    "stable_source",
    "exact_locator_recheckable",
    "emits_branch3_parent_slot",
    "emits_degree_2",
    "pre_codomain_order",
    "noncircular_from_D_A_U",
    "closes_rival_parent_classes",
    "target_replacement_invariant",
    "anti_smuggling_guard_passes",
    "rollback_conditions_declared"
  ],
  "current_candidate_results": {
    "reconstruction_only_exterior_parent_action": "reject_noncircularity_fails",
    "acquired_2021_draft_rows": "reject_parent_slot_not_emitted",
    "primary_source_locator_row": "reject_locator_absent",
    "parent_variation_source_locator_receipt": "reject_locator_absent",
    "rival_parent_firewall": "not_a_source_row_fields_defined_only",
    "positive_exterior_degree_rule": "reject_degree_not_source_forced"
  },
  "rollback_conditions": [
    "unstable_or_ambiguous_source_locator",
    "emitted_object_not_branch3_parent_slot",
    "degree_2_inferred_from_D_A_U_or_selected_codomain",
    "zero_form_or_coderivative_trace_parent_remains_source_possible",
    "symmetric_derivative_parent_remains_source_possible",
    "projected_derivative_parent_remains_source_possible",
    "lower_order_dressed_exterior_parent_remains_unfixed",
    "target_behavior_used_to_select_row_degree_operator_or_rival_elimination",
    "reconstruction_only_template_cited_without_quarantine_marker"
  ],
  "terrain": [
    "provenance-verifier",
    "source-selection-boundary-certificate",
    "smooth-variational-parent-action-typing",
    "rival-parent-class-closure"
  ],
  "forbidden_shortcut": "do_not_promote_K_IG_rec_equals_D_A_U_to_source_selected_from_naturalness_action_cleanliness_or_downstream_utility",
  "invariant": "target_replacement_preserves_reconstruction_only_allowed_source_selected_absent_firewall_barred",
  "kill_condition": "stable_source_row_emits_exterior_branch3_parent_slot_degree_2_before_selected_codomain_and_before_K_IG_equals_D_A_U_and_closes_all_rival_parent_classes",
  "checks_performed": [
    "read_required_posture_and_runbook",
    "read_required_cycle1_acquisition_extraction_negative",
    "read_required_cycle2_reconstruction_only_boundary",
    "read_required_cycle3_primary_source_locator_negative",
    "read_cycle1003_firewall_and_locator_receipt_artifacts",
    "read_cycle0904_rival_parent_firewall",
    "read_cycle0803_positive_exterior_degree_and_parent_degree_selector negatives",
    "checked_git_status_before_edit",
    "confirmed_owned_output_path_absent_before_edit",
    "repo_rg_search_for_current_source_selection_candidates"
  ]
}
```

## Verification

Commands/checks performed for this lane:

```text
Get-Content -Raw RESEARCH-POSTURE.md
Get-Content -Raw process/runbooks/five-lane-frontier-run.md
Get-Content -Raw explorations/hourly-20260626-1102-cycle2-kig-reconstruction-only-parent-action-boundary.md
Get-Content -Raw explorations/hourly-20260626-1102-cycle1-kig-parent-variation-acquisition-extraction-row.md
Get-Content -Raw explorations/hourly-20260626-1003-cycle3-kig-primary-source-locator-row.md
Get-Content -Raw explorations/hourly-20260626-1003-cycle1-kig-source-row-rival-parent-firewall-test.md
Get-Content -Raw explorations/hourly-20260626-1003-cycle2-kig-parent-variation-source-locator-receipt.md
Get-Content -Raw explorations/hourly-20260626-0904-cycle3-kig-rival-parent-firewall.md
Get-Content -Raw explorations/hourly-20260626-0803-cycle3-kig-parent-degree-selector.md
Get-Content -Raw explorations/hourly-20260626-0803-cycle1-kig-positive-exterior-degree-rule.md
git status --short
Test-Path explorations/hourly-20260626-1102-cycle3-kig-source-selection-boundary-certificate.md
rg -n "KIGSourceSelectionBoundaryCertificate|SourceRowPassingKIGRivalParentFirewall|PreCodomainParentMomentumDegreeSourceRow|source_selected_branch3|source-selected Branch 3|ParentVariationSlot_IG|degree\(P_IG\)=2|K_IG\s*=\s*D_A U|CODERIVATIVE_TRACE|SYMMETRIC_DERIVATIVE|PROJECTED_DERIVATIVE|LOWER_ORDER_DRESSED_EXTERIOR" explorations literature sources -g "*.md"
rg --files explorations | rg "kig|KIG|source|parent|firewall|boundary|selector|witness|trace"
```

No source extraction was retried. No trace/coderivative exclusion was retried.
No tests, status/canon files, automation directories, or memory files were
edited.
