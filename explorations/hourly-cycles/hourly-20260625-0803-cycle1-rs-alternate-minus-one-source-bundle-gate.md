---
title: "Hourly 20260625 0803 Cycle 1 RS Alternate Minus-One Source Bundle Gate"
date: "2026-06-25"
run_id: "hourly-20260625-0803"
cycle: 1
lane: 4
doc_type: rs_alternate_minus_one_source_bundle_gate
artifact_id: "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1"
verdict: "UCSD_HOSTED_CANDIDATE_UNDERDEFINED_ZERO_ACCEPTED_RS_RECEIPTS"
owned_path: "explorations/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md"
companion_audit: "tests/hourly_20260625_0803_cycle1_rs_alternate_minus_one_source_bundle_gate_audit.py"
---

# Hourly 20260625 0803 Cycle 1 RS Alternate Minus-One Source Bundle Gate

## 1. Verdict

Verdict: **underdefined hosted candidate, not closed**.

The UCSD April 2025 transcript gives a stronger alternate primary-source
surface than equation `10.10` for the RS route. It explicitly hosts the rolled
up de Rham/Dirac/Rarita-Schwinger construction, names the hard middle map
problem from `Omega^1` to `Omega^(d-1)`, and describes a symbol taking
spinor-valued two-forms back to spinor-valued one-forms. That is a real
candidate surface.

It still does not supply an accepted RS-only minus-one receipt. The transcript
does not type a source space, target space, differential/operator/action, or
candidate map as `source.action_or_operator for d_RS,-1`; it also does not
identify the quotient from spinors to pure Rarita-Schwinger fields or prove a
family identity against the repo's RS required object.

Decision state:

```text
equation_10_10_status: scoped_fail_only
ucsd_candidate_status: hosted_underdefined_candidate
accepted_rs_receipt_count: 0
accepted_rs_proof_restart_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
global_rs_no_go: false
```

## 2. Specific GU Claim Or Bridge Under Test

Bridge under test:

```text
AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1:
Does the UCSD transcript supply an alternate primary-source RS-only minus-one
rule, differential/operator/action, source and target spaces, or a map from
Omega^1 to Omega^(d-1), or from spinor-valued two-forms back to one-forms,
that can serve as source.action_or_operator for d_RS,-1?
```

The bridge is narrower than the full generation-count claim. It asks only
whether the source layer now emits the missing RS differential/action receipt
needed before any RS family identity, K3 index, symbol, or generation-count
restart.

## 3. Owned Output Path And Sources Read First

Owned output path:

- `explorations/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md`

Owned audit path:

- `tests/hourly_20260625_0803_cycle1_rs_alternate_minus_one_source_bundle_gate_audit.py`

Sources read first:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260625-0711-three-cycle-fifteen-hole-synthesis.md`
- `explorations/hourly-20260625-0711-cycle1-rs-manual-image-formula-diagram-audit.md`
- `explorations/hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md`
- `literature/weinstein-ucsd-2025-04-transcript.md`
- `tests/rs_clifford_projector_model.py`

## 4. What Was Derived Directly From Repo Sources

Prior repo state:

- Equation `10.10` is already exhausted only as a scoped manuscript image/cell
  failure. It is mixed `/S plus ad`/`ad`/`/S`, not a typed RS minus-one cell.
- The exact local missing object from equation `10.10` is
  `ImageTypedRSMinusOneRuleCell_V1`.
- The 0711 synthesis forbids RS proof restart unless an accepted receipt and
  family identity check exist.
- The finite Clifford projector model computes raw gamma-trace/projector ranks
  only. It is not a K-theory index, not a GU source receipt, and not a typed
  source differential.

UCSD transcript facts, normalized without promoting them:

- The transcript hosts the `Y^14`/bundle-of-metrics setting and says the quantum
  work is moved upstairs while `X^4` remains the classical slice.
- It says GU creates a "de Rham Dirac Einstein complex" and starts from an
  ordinary de Rham sequence tensored with spinors.
- It identifies the hard problem: getting from `Omega^1` to `Omega^(d-1)` with
  a differential.
- It says connection information is mined from the inhomogeneous gauge group
  for a minimally coupled exterior derivative.
- It says rolling the complex creates a Dirac/de Rham/Rarita-Schwinger gadget.
- It describes a symbol that takes spinor-valued two-forms back into
  spinor-valued one-forms, after the ordinary derivative takes one-forms to
  two-forms.
- It later gives a representation-theoretic product-rule-like description for
  the Rarita-Schwinger three-halves representation.

These are source-hosted ingredients for a candidate. They are not yet the
typed RS-only receipt object.

## 5. Strongest Positive Construction Attempt

The strongest construction the UCSD source suggests is:

```text
Let E be the relevant spinor bundle upstairs on Y.
Start with a spinor-valued de Rham column
  Omega^0(E) -> Omega^1(E) -> Omega^2(E) -> ... .
Use the ordinary minimally coupled exterior derivative
  d_A: Omega^1(E) -> Omega^2(E).
Apply a source-intended "ship in a bottle" symbol/projection
  B: Omega^2(E) -> Omega^1(E)
to form a rolled-up middle operator
  B d_A: Omega^1(E) -> Omega^1(E).
Then combine this with the rolled-up de Rham/Dirac complex to obtain the
Dirac/de Rham/Rarita-Schwinger shape that could host the RS sector.
```

A second, weaker positive route uses the transcript's middle-map phrase:

```text
Construct M: Omega^1(E) -> Omega^(d-1)(E)
as the missing differential-like map, then use Hodge/contraction/roll-up data
to pair it back with one-form spinor data and isolate an RS summand.
```

This is positive because the transcript points at exactly the class of maps the
repo was missing after equation `10.10`: a way to route one-form spinor data
through higher-degree spinor-valued forms and back into one-form data.

It is not accepted because `E`, `B`, `M`, the RS quotient/projection, and the
minus-one source slot are not source-typed.

## 6. First Exact Obstruction Or Missing Object

The first exact missing object is:

```text
UCSDTypedRSMinusOneOperator_V1
```

Minimum required fields:

| field | required status |
|---|---|
| `source_surface` | UCSD transcript timestamp/range or source slide/frame |
| `family` | pure `RS`, not aggregate spinor or de Rham/Dirac/Rarita-Schwinger |
| `required_object` | `source.action_or_operator for d_RS,-1` |
| `source_space` | source-emitted RS minus-one/gauge/ghost/parameter space |
| `target_space` | source-emitted pure RS field/equation/constraint space |
| `degree_or_slot` | `-1` or a source-equivalent complex slot |
| `operator_formula` | explicit action/operator/differential/gauge/Noether/BRST formula |
| `middle_map` | typed map `Omega^1 -> Omega^(d-1)` or typed `Omega^2 -> Omega^1` symbol |
| `rs_projection_or_quotient` | source-defined projection from spinor-valued forms to pure RS |
| `family_identity_status` | passed against the repo RS required object |

Current first decisive obstruction:

```text
The UCSD transcript hosts the rolled-up map idea but never names or types the
operator/projection that isolates a pure RS d_RS,-1 source-to-target rule.
```

## 7. Impact If Closed

If `UCSDTypedRSMinusOneOperator_V1` were supplied, the repo would have its first
alternate-primary-source candidate for the RS missing receipt after equation
`10.10` failed locally.

The immediate promotion would still be narrow:

```text
PrimarySourceReceiptInstanceCandidate_V1:
  source = UCSD-April-2025-transcript-or-slide
  family = RS
  required_object = source.action_or_operator for d_RS,-1
  status = candidate_receipt_pending_family_identity
```

Only then would it be meaningful to run:

- RS family identity against the source-typed operator.
- Source-origin and target-import guards.
- Gauge/quotient/BRST finality checks.
- RS symbol/index or K3 generation-count restart readiness.

Closing this gate would not itself prove `rank_H(S_RS^+)`,
`ind_H(D_RS)`, or the generation count.

## 8. Falsification/Demotion Condition

The UCSD alternate source route is demoted if the source slides/video/transcript
around the rolled-up de Rham/Dirac/Rarita-Schwinger passage do not supply:

```text
a source-typed RS-only operator/action/differential with source space,
target space, degree/slot, RS projection or quotient, and family identity.
```

Demotion would be local to the UCSD-hosted candidate unless a separate global
negative bundle covers all primary source surfaces. The equation `10.10`
manuscript result remains a scoped failure and is not evidence that the UCSD
candidate fails globally.

Rollback condition:

```text
A UCSD slide/frame, corrected transcript segment, lecture note, or official
source artifact supplies UCSDTypedRSMinusOneOperator_V1 and the RS family
identity check passes.
```

## 9. Next Meaningful Computation Or Proof/Source Step

Next source step:

```text
Acquire the exact UCSD slide/frame range for the transcript passages around
the de Rham/Dirac/Rarita-Schwinger roll-up and transcribe the displayed complex,
middle map, and "ship in a bottle" symbol.
```

Next proof computation after source acquisition:

```text
Build a typed candidate operator packet with:
  B: Omega^2(E) -> Omega^1(E),
  M: Omega^1(E) -> Omega^(d-1)(E), if displayed,
  P_RS: Omega^1(E) -> RS(E) or equivalent,
  and the resulting candidate d_RS,-1 source and target spaces.
Then test whether this packet is pure RS or only aggregate spinor/de Rham data.
```

The existing `tests/rs_clifford_projector_model.py` can be reused only as a
finite-dimensional sanity check after a source-typed RS operator exists. It
cannot supply the receipt by itself.

## 10. Machine-Readable JSON Summary

```json
{
  "artifact": "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0803",
  "cycle": 1,
  "lane": 4,
  "verdict": "UCSD_HOSTED_CANDIDATE_UNDERDEFINED_ZERO_ACCEPTED_RS_RECEIPTS",
  "verdict_class": "underdefined_hosted_candidate",
  "family": "RS",
  "required_object": "source.action_or_operator for d_RS,-1",
  "accepted_rs_receipt_count": 0,
  "accepted_rs_proof_restart_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "global_rs_no_go": false,
  "equation_1010_scoped_failure": {
    "status": "scoped_fail",
    "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
    "source_surface": "Geometric_UnityDraftApril1st2021.pdf#page_49_equation_10.10",
    "missing_object": "ImageTypedRSMinusOneRuleCell_V1",
    "accepted_cell_count": 0,
    "accepted_receipt_count": 0,
    "global_rs_no_go": false,
    "kept_separate_from_ucsd_candidate": true
  },
  "ucsd_hosted_candidate": {
    "status": "hosted_underdefined_candidate",
    "source_id": "UCSD-April-2025-transcript",
    "source_surface": "literature/weinstein-ucsd-2025-04-transcript.md",
    "relevant_passage_lines": [125, 128, 131, 140],
    "positive_source_content": [
      "de_Rham_Dirac_Einstein_complex",
      "ordinary_de_Rham_sequence_tensored_with_spinors",
      "problem_of_getting_from_Omega_1_to_Omega_d_minus_1_with_a_differential",
      "minimally_coupled_exterior_derivative_from_connection_information",
      "rolled_up_Dirac_de_Rham_Rarita_Schwinger_gadget",
      "symbol_from_spinor_valued_two_forms_back_to_spinor_valued_one_forms",
      "representation_product_rule_like_Rarita_Schwinger_three_halves_passage"
    ],
    "candidate_maps_hosted": [
      {
        "id": "middle_map_M",
        "shape": "Omega^1(E) -> Omega^(d-1)(E)",
        "status": "named_as_problem_not_formula"
      },
      {
        "id": "ship_in_bottle_symbol_B",
        "shape": "Omega^2(E) -> Omega^1(E)",
        "status": "described_not_typed_as_RS_minus_one"
      },
      {
        "id": "rolled_operator_B_d_A",
        "shape": "Omega^1(E) -> Omega^1(E)",
        "status": "derived_attempt_not_source_typed"
      }
    ],
    "accepted_as_rs_minus_one_rule": false
  },
  "first_exact_missing_object": {
    "id": "UCSDTypedRSMinusOneOperator_V1",
    "description": "A source-typed pure RS d_RS,-1 operator/action/differential with source space, target space, degree/slot, operator formula, middle map or two-form-to-one-form symbol, RS projection or quotient, and passed family identity.",
    "missing_fields": [
      "source_surface_timestamp_or_slide",
      "pure_RS_family_identity",
      "source_space",
      "target_space",
      "degree_or_slot_minus_one",
      "operator_formula",
      "typed_middle_map_or_symbol",
      "rs_projection_or_quotient",
      "family_identity_status"
    ]
  },
  "strongest_positive_construction_attempt": {
    "operator_chain": "Omega^1(E) --d_A--> Omega^2(E) --B--> Omega^1(E)",
    "alternate_middle_map": "Omega^1(E) --M--> Omega^(d-1)(E)",
    "status": "hosted_but_underdefined",
    "why_not_accepted": [
      "E_not_source_typed",
      "B_not_formula_typed",
      "M_not_formula_typed",
      "no_source_RS_minus_one_slot",
      "no_source_target_pair_for_pure_RS",
      "no_RS_projection_or_quotient",
      "family_identity_not_runnable"
    ]
  },
  "impact_if_closed": {
    "candidate_receipt_would_exist": true,
    "immediate_status_if_closed": "candidate_receipt_pending_family_identity",
    "downstream_allowed_after_family_identity": [
      "RS_family_identity_check",
      "source_origin_guard",
      "gauge_quotient_BRST_finality_check",
      "RS_symbol_or_K3_index_restart_readiness"
    ],
    "generation_count_proved_by_this_gate": false
  },
  "falsification_or_demotion_condition": "UCSD source slides/video/transcript around the roll-up passage fail to supply a source-typed RS-only operator/action/differential with source space, target space, degree/slot, RS projection or quotient, and family identity.",
  "next_meaningful_step": "Acquire exact UCSD slide/frame range and transcribe the displayed complex, middle map, and ship-in-a-bottle symbol before any RS proof restart.",
  "forbidden_promotions": [
    "equation_10_10_failure_as_global_rs_no_go",
    "ucsd_hosted_candidate_as_accepted_receipt",
    "RS_d_RS_minus_1_source_derived",
    "accepted_RS_receipt_without_typed_operator",
    "RS_generation_count_proof_restart_allowed"
  ]
}
```
