---
title: "Hourly 20260625 0803 Cycle 2 RS UCSD Typed Operator Source-Origin Classifier"
date: "2026-06-25"
run_id: "hourly-20260625-0803"
cycle: 2
lane: 4
doc_type: rs_ucsd_typed_operator_source_origin_classifier
artifact_id: "UCSDTypedRSMinusOneOperatorSourceOriginClassifier_V1"
verdict: "CONDITIONAL_SOURCE_ORIGIN_HOST_UNDERDEFINED_ZERO_ACCEPTED_RS_OPERATOR"
owned_path: "explorations/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md"
companion_audit: "tests/hourly_20260625_0803_cycle2_rs_ucsd_typed_operator_source_origin_classifier_audit.py"
---

# Hourly 20260625 0803 Cycle 2 RS UCSD Typed Operator Source-Origin Classifier

## 1. Verdict

Verdict: **conditional source-origin host, underdefined as a typed pure-RS
operator**.

The UCSD April 2025 transcript can be classified as a **source-origin surface**
for the rolled-up de Rham/Dirac/Rarita-Schwinger operator idea. It is not yet a
source-origin **operator rule** for `d_RS,-1`.

The distinction is load-bearing:

```text
source-origin surface status: hosted candidate
operator-rule status: underdefined
family identity status: not runnable
proof restart status: forbidden
accepted RS receipt count: 0
accepted RS proof restart count: 0
generation-count promotion: forbidden
```

`UCSDTypedRSMinusOneOperator_V1` therefore exists only as a **conditional object
specification**. It does not exist as an accepted repo receipt. It would become
an accepted candidate only if the UCSD source surface supplies a typed pure-RS
domain, codomain, degree/slot, operator formula, and RS projection or quotient
that passes family identity.

## 2. Specific GU Claim Or Bridge Under Test

Claim under test:

```text
UCSDTypedRSMinusOneOperator_V1:
Can the UCSD rolled-up de Rham/Dirac/Rarita-Schwinger passages be typed as a
source-origin operator/action/differential rule for the RS minus-one slot,
separately from aggregate family identity and separately from proof restart?
```

This bridge tests source-origin status only. It does not test whether the RS
operator is correct physics, whether Velo-Zwanziger is evaded, whether the K3
generation count follows, or whether equation `10.10` can be rehabilitated.

The required GU object remains:

```text
source.action_or_operator for d_RS,-1
```

## 3. Sources Read First

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md`
- `explorations/hourly-20260625-0711-cycle1-rs-manual-image-formula-diagram-audit.md`
- `explorations/hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md`
- `literature/weinstein-ucsd-2025-04-transcript.md`
- `canon/no-go-class-relative-map.md`

Directly relevant UCSD transcript ranges:

- `[00:32:07]-[00:35:30]`: `Y^14`, pullback from the metric bundle, de Rham
  sequence tensored with spinors, and the middle-map problem.
- `[00:35:30]-[00:37:41]`: rolled-up Dirac/de Rham/Rarita-Schwinger gadget and
  the symbol from spinor-valued two-forms back to spinor-valued one-forms.
- `[00:39:18]-[00:40:27]`: product-rule-like Rarita-Schwinger representation
  identity and spin-three-halves family discussion.
- `[00:41:45]-[00:42:29]`: Velo-Zwanziger question and class-assumption caveat.

## 4. Typed-Operator Source-Origin Classifier

| field | UCSD hosted content | classifier value | decision |
|---|---|---|---|
| `source_surface` | UCSD April 2025 transcript ranges around `[00:32:07]-[00:37:41]` | primary-source transcript surface | hosted |
| `operator_name` | "rolled up Dirac, de Rham, Rarita-Schwinger gadget"; "ship in a bottle operator" | source-named aggregate operator family, not formal name | hosted underdefined |
| `domain` | ordinary derivative from spinor-valued one-forms to spinor-valued two-forms | `Omega^1(E)`, where `E` is not source-typed enough for pure RS | underdefined |
| `codomain` | symbol maps spinor-valued two-forms back into spinor-valued one-forms | `Omega^1(E)` after `Omega^2(E) -> Omega^1(E)` symbol | underdefined |
| `degree_or_slot` | middle-map problem `Omega^1 -> Omega^(d-1)` and roll-up `Omega^2 -> Omega^1` | form-degree data present; minus-one complex slot absent | missing for `d_RS,-1` |
| `rule_kind` | exterior derivative plus symbol/projection-like operator | differential-symbol composite candidate | hosted, not accepted |
| `RS_only_purity` | transcript says Dirac/de Rham/Rarita-Schwinger aggregate and later gives RS representation language | aggregate, not pure RS operator rule | fail for purity |
| `relation_to_equation_10_10` | alternate source surface after equation `10.10` failed locally | independent hosted candidate; does not repair `10.10` | separate scoped fail preserved |
| `family_identity` | RS representation discussion exists later, but no typed quotient from aggregate spinor forms to pure RS slot | not runnable | blocked |

Typed status:

```text
hosted_source_origin_surface: true
hosted_operator_idea: true
typed_source_origin_operator_rule: false
pure_RS_rule: false
minus_one_slot_identified: false
family_identity_runnable: false
```

The UCSD source-origin classification is therefore **surface-positive** and
**operator-negative/underdefined**.

## 5. Strongest Positive Typing Attempt

The strongest positive typing attempt is the following operator packet:

```text
E = source-intended spinor bundle over Y^14

d_A:
  Omega^1(Y^14; E) -> Omega^2(Y^14; E)

B:
  Omega^2(Y^14; E) -> Omega^1(Y^14; E)

candidate rolled operator:
  D_roll = B o d_A:
  Omega^1(Y^14; E) -> Omega^1(Y^14; E)
```

This is the best source-faithful attempt because the transcript says the
ordinary derivative takes one-forms to two-forms, then a special symbol knocks
two-forms back to one-forms, producing the rolled-up complex. It is a genuine
candidate source-origin shape for an operator.

A second, less complete route uses the transcript's middle-map problem:

```text
M:
  Omega^1(Y^14; E) -> Omega^(d-1)(Y^14; E)
```

That route is source-hosted because the transcript explicitly names the problem
of getting from `Omega^1` to `Omega^(d-1)` with a differential. It is weaker
because the transcript names it as the issue to solve, not as a displayed
formula.

The best possible conditional receipt would have to refine the packet to:

```text
P_RS o B o d_A o I_-1:
  RS_minus_one_source_space -> RS_field_or_equation_space
```

where `I_-1` injects or identifies the minus-one RS source slot and `P_RS`
projects or quotients the aggregate spinor-valued form data to the pure
Rarita-Schwinger family.

No such `I_-1` or `P_RS` is present in the transcript as read.

## 6. First Exact Obstruction Or Missing Object

The first exact obstruction is:

```text
The transcript hosts a rolled-up aggregate spinor-valued de Rham/Dirac/RS
operator shape, but does not supply the pure-RS source/target typing and
projection or quotient needed to turn that shape into source.action_or_operator
for d_RS,-1.
```

Exact missing object:

```text
UCSDTypedRSMinusOneOperator_V1
```

Required fields still missing or underdefined:

| required field | current status |
|---|---|
| `source_surface` | hosted by transcript, but exact slide/frame/crop not acquired |
| `operator_name` | informal aggregate names only |
| `domain` | spinor-valued form domain hosted; pure RS minus-one domain missing |
| `codomain` | spinor-valued one-form codomain hosted; pure RS target missing |
| `degree_or_slot` | form-degree movement hosted; `d_RS,-1` slot missing |
| `rule_kind` | differential-symbol composite hosted; action/operator receipt not formalized |
| `RS_only_purity` | fails: aggregate Dirac/de Rham/Rarita-Schwinger language |
| `relation_to_equation_10_10` | independent of equation `10.10`, which remains scoped fail |
| `family_identity` | not runnable without `P_RS`, quotient, or source family certificate |

This is a typing obstruction, not a global no-go. It says the current source
surface does not yet emit the object the repo needs.

## 7. Impact If Closed

If `UCSDTypedRSMinusOneOperator_V1` were supplied, the repo could promote a
narrow source-origin candidate:

```text
PrimarySourceReceiptInstanceCandidate_V1:
  source = UCSD-April-2025 transcript/slide/frame
  family = RS
  required_object = source.action_or_operator for d_RS,-1
  status = candidate_receipt_pending_family_identity
```

The immediate impact would be:

- equation `10.10` would remain a scoped fail, not repaired retroactively;
- the UCSD route would become the active alternate source-origin route;
- RS family identity could become runnable;
- proof restart would still wait on family identity and quotient/gauge checks;
- generation-count work would remain unpromoted until downstream analytic and
  source-origin gates close.

Closing this gate would be important because it would replace a negative image
cell route with a source-hosted typed operator route. It would not itself prove
the three-generation count.

## 8. Falsification/Demotion Condition

The UCSD typed-operator route is demoted if the exact UCSD slides/video frames
around the relevant transcript ranges fail to supply all of:

```text
source-typed pure RS domain;
source-typed pure RS codomain;
minus-one or source-equivalent complex slot;
operator/action/differential formula;
projection, quotient, or family certificate separating RS from aggregate
Dirac/de Rham/spinor-valued form data.
```

Demotion state would be:

```text
UCSD hosted aggregate operator idea remains;
UCSDTypedRSMinusOneOperator_V1 absent;
accepted RS receipt count remains 0;
proof restart remains forbidden;
generation-count promotion remains forbidden.
```

Rollback condition:

```text
A UCSD slide/frame/official note/corrected transcript supplies the missing
typed pure-RS operator packet and family identity passes.
```

## 9. Next Meaningful Proof/Source Step

Next source step:

```text
Acquire the exact UCSD slide/frame sequence for [00:32:07]-[00:37:41] and
transcribe the displayed complex, middle map, symbol, and any labels on the
rolled-up operator.
```

Next proof step after source acquisition:

```text
Construct a candidate packet with fields:
  source_surface
  operator_name
  domain
  codomain
  degree_or_slot
  rule_kind
  RS_only_purity
  relation_to_equation_10_10
  family_identity

Then test whether a source-defined P_RS or quotient maps the aggregate
spinor-valued one-form data to the pure Rarita-Schwinger family.
```

Do not restart RS index, K3, or generation-count proof work before that packet
exists and passes family identity.

## 10. Machine-Readable JSON Summary

```json
{
  "artifact": "UCSDTypedRSMinusOneOperatorSourceOriginClassifier_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0803",
  "cycle": 2,
  "lane": 4,
  "verdict": "CONDITIONAL_SOURCE_ORIGIN_HOST_UNDERDEFINED_ZERO_ACCEPTED_RS_OPERATOR",
  "verdict_class": "conditional_host_underdefined",
  "family": "RS",
  "required_object": "source.action_or_operator for d_RS,-1",
  "ucsd_typed_operator_exists": "conditional_specification_only",
  "typed_source_origin_operator_rule_exists": false,
  "accepted_rs_receipt_count": 0,
  "accepted_rs_proof_restart_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "generation_count_promotion_allowed": false,
  "equation_1010_status": {
    "status": "scoped_fail",
    "source_surface": "Geometric_UnityDraftApril1st2021.pdf#page_49_equation_10.10",
    "missing_object": "ImageTypedRSMinusOneRuleCell_V1",
    "relation_to_ucsd_candidate": "independent_prior_scoped_failure_not_repaired_by_ucsd_hosting",
    "accepted_cell_count": 0,
    "accepted_receipt_count": 0,
    "global_rs_no_go": false
  },
  "ucsd_hosted_candidate": {
    "status": "hosted_conditional_underdefined",
    "source_id": "UCSD-April-2025-transcript",
    "source_surface": "literature/weinstein-ucsd-2025-04-transcript.md",
    "relevant_transcript_ranges": [
      "00:32:07-00:35:30",
      "00:35:30-00:37:41",
      "00:39:18-00:40:27",
      "00:41:45-00:42:29"
    ],
    "hosted_source_origin_surface": true,
    "hosted_operator_idea": true,
    "accepted_as_rs_minus_one_rule": false,
    "family_identity_runnable": false
  },
  "typed_operator_source_origin_classifier": [
    {
      "field": "source_surface",
      "ucsd_hosted_content": "UCSD April 2025 transcript ranges around rolled-up de_Rham_Dirac_Rarita_Schwinger passage",
      "classifier_value": "primary_source_transcript_surface",
      "decision": "hosted"
    },
    {
      "field": "operator_name",
      "ucsd_hosted_content": "rolled up Dirac/de_Rham/Rarita_Schwinger gadget; ship in a bottle operator",
      "classifier_value": "source_named_aggregate_operator_family_not_formal_name",
      "decision": "hosted_underdefined"
    },
    {
      "field": "domain",
      "ucsd_hosted_content": "ordinary derivative from spinor-valued one-forms to spinor-valued two-forms",
      "classifier_value": "Omega^1(E)_with_E_not_source_typed_as_pure_RS",
      "decision": "underdefined"
    },
    {
      "field": "codomain",
      "ucsd_hosted_content": "symbol maps spinor-valued two-forms back into spinor-valued one-forms",
      "classifier_value": "Omega^1(E)_after_symbol_B_from_Omega^2(E)",
      "decision": "underdefined"
    },
    {
      "field": "degree_or_slot",
      "ucsd_hosted_content": "Omega^1_to_Omega^(d-1)_problem_and_Omega^2_to_Omega^1_rollup",
      "classifier_value": "form_degree_data_present_minus_one_complex_slot_absent",
      "decision": "missing_for_d_RS_minus_1"
    },
    {
      "field": "rule_kind",
      "ucsd_hosted_content": "minimally coupled exterior derivative plus symbol/projection-like operator",
      "classifier_value": "differential_symbol_composite_candidate",
      "decision": "hosted_not_accepted"
    },
    {
      "field": "RS_only_purity",
      "ucsd_hosted_content": "Dirac/de_Rham/Rarita_Schwinger aggregate and later RS representation language",
      "classifier_value": "aggregate_not_pure_RS_operator_rule",
      "decision": "fail_for_purity"
    },
    {
      "field": "relation_to_equation_10_10",
      "ucsd_hosted_content": "alternate source surface after equation 10.10 failed locally",
      "classifier_value": "independent_hosted_candidate",
      "decision": "separate_scoped_fail_preserved"
    },
    {
      "field": "family_identity",
      "ucsd_hosted_content": "RS representation discussion exists but no typed quotient from aggregate spinor forms to pure RS slot",
      "classifier_value": "not_runnable_without_P_RS_or_quotient",
      "decision": "blocked"
    }
  ],
  "strongest_positive_typing_attempt": {
    "operator_chain": "Omega^1(Y^14;E) --d_A--> Omega^2(Y^14;E) --B--> Omega^1(Y^14;E)",
    "alternate_middle_map": "Omega^1(Y^14;E) --M--> Omega^(d-1)(Y^14;E)",
    "conditional_receipt_shape": "P_RS o B o d_A o I_-1: RS_minus_one_source_space -> RS_field_or_equation_space",
    "status": "source_hosted_but_underdefined",
    "why_not_accepted": [
      "I_minus_1_missing",
      "P_RS_or_RS_quotient_missing",
      "pure_RS_domain_missing",
      "pure_RS_codomain_missing",
      "d_RS_minus_1_slot_missing",
      "operator_formula_not_formalized",
      "family_identity_not_runnable"
    ]
  },
  "first_exact_missing_object": {
    "id": "UCSDTypedRSMinusOneOperator_V1",
    "exists": false,
    "conditional_specification_exists": true,
    "description": "A UCSD-source-typed pure RS minus-one operator/action/differential with source surface, operator name, domain, codomain, degree/slot, rule kind, RS-only purity, relation to equation 10.10, and family identity.",
    "missing_fields": [
      "exact_slide_or_frame_source_surface",
      "formal_operator_name",
      "pure_RS_domain",
      "pure_RS_codomain",
      "degree_or_slot_d_RS_minus_1",
      "operator_formula",
      "P_RS_or_RS_quotient",
      "family_identity_status"
    ]
  },
  "impact_if_closed": {
    "candidate_receipt_would_exist": true,
    "immediate_status_if_closed": "candidate_receipt_pending_family_identity",
    "equation_1010_repaired": false,
    "family_identity_would_become_runnable": true,
    "proof_restart_automatically_allowed": false,
    "generation_count_proved_by_this_gate": false
  },
  "falsification_or_demotion_condition": "Exact UCSD slides/video frames around the rolled-up passage fail to supply source-typed pure RS domain, codomain, minus-one or equivalent slot, operator formula, and projection or quotient separating RS from aggregate Dirac/de_Rham/spinor-valued form data.",
  "next_meaningful_step": "Acquire the exact UCSD slide/frame sequence for 00:32:07-00:37:41 and transcribe the displayed complex, middle map, symbol, and rolled-up operator labels.",
  "forbidden_promotions": [
    "equation_10_10_failure_as_global_rs_no_go",
    "ucsd_hosted_candidate_as_accepted_receipt",
    "typed_source_origin_operator_rule_exists",
    "RS_d_RS_minus_1_source_derived",
    "RS_family_identity_passed",
    "RS_generation_count_proof_restart_allowed",
    "generation_count_promotion_allowed"
  ]
}
```
