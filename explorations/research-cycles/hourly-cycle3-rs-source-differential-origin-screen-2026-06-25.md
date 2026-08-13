---
title: "Hourly Cycle 3 RS Source Differential Origin Screen"
date: "2026-06-25"
cycle: "3-of-3"
run: "3-1-5-4"
status: exploration
doc_type: frontier_run_artifact
verdict: "BLOCKED_RAW_PRINCIPAL_SYMBOL_ONLY__SOURCE_DERIVED_D_RS_MINUS_1_NOT_SUPPLIED"
owned_path: "explorations/hourly-cycle3-rs-source-differential-origin-screen-2026-06-25.md"
audit:
  - "tests/hourly_cycle3_rs_source_differential_origin_screen_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle2-rs-quotient-transport-builder-2026-06-25.md"
  - "explorations/hourly-cycle1-effect-typed-witness-rs-quotient-2026-06-25.md"
  - "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
  - "explorations/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/hourly-cycle2-actual-dgu-operator-certificate-schema-2026-06-25.md"
  - "explorations/af4-tau-rs-gauge-fixing-2026-06-23.md"
  - "explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md"
  - "tests/rs_clifford_projector_model.py"
---

# Hourly Cycle 3 RS Source Differential Origin Screen

## 1. Verdict

**Verdict: blocked; current repo sources provide raw principal-symbol gauge
directions and reconstruction-grade gauge language, but not an
action-derived or source-theorem-derived right-H-linear RS gauge/BRST
differential.**

The strongest positive attempt starts from the raw pointwise principal map:

```text
epsilon |-> xi tensor epsilon
```

and from the reconstruction-grade statement:

```text
psi_a^RS ~ psi_a^RS + nabla_a epsilon.
```

Those are the right shape for the principal symbol of a candidate
`d_RS,-1`. They do not yet constitute the required source object:

```text
d_RS,-1 : Ghost_RS,H^src -> Field_RS,H^src.
```

The first exact obstruction is source provenance plus finality. No current
source read here derives this map from a primary GU action, a source
Euler-Lagrange/Noether theorem, or a source-closed actual `D_GU` operator; and
no current source proves that the resulting global map is right-H-linear,
connection-compatible, has image equal to the physical RS gauge equivalence
direction, and extends to a BRST complex or gauge-fixed elliptic object.

Current decision:

```text
d_RS,-1 source-origin screen = FAILS_SOURCE_DERIVATION_GATE
raw principal gauge symbol = AVAILABLE_AS_CONTEXT
reconstruction-grade gauge prose = AVAILABLE_AS_CANDIDATE_SHAPE
source-derived H-linear differential = NOT_SUPPLIED
physical Pi_RS^phys = NOT_DEFINED
rank and generation claims = QUARANTINED
```

This is not a negative theorem against GU. It is a source-origin screen: the
repo has a plausible local symbol and a plausible formal gauge transformation,
but not the proof object that lets the RS quotient/BRST builder advance.

## 2. What Was Derived Directly From Repo Sources

The research posture requires constructive obstruction handling and forbids
turning compatibility into derivation. The five-lane runbook requires a
decision-grade artifact with exact missing proof objects and rank-claim
quarantine.

The Cycle 1 and Cycle 2 RS quotient artifacts establish the required witness
shape:

```text
d_RS,-1 : Ghost_RS,H^src -> Field_RS,H^src
```

with four effect layers:

```text
source -> projection -> finality -> loss
```

The Cycle 2 quotient transport builder makes this a first-stage validation
gate. Projection, finality, and loss are not meaningful until the source
witness for `d_RS,-1` exists.

The physical quotient/BRST complex gate supplies the raw finite-dimensional
context:

```text
R^+ = ker(G_+)
R^- = ker(G_-)
g_xi : epsilon |-> P_+(xi tensor epsilon)
sigma_raw(xi) = P_- (c(xi) tensor 1_F) P_+
```

and identifies the raw principal gauge image as context only. It does not say
whether that image is quotient, ghost, gauge-fixed, physical, boundary-sensitive,
or absent from the source theory.

The executable RS Clifford/projector model directly computes raw complex
matrices. It verifies gamma-trace projectors and computes the pointwise
principal gauge map:

```text
gauge_symbol(xi, spinor_rank, internal_rank)
```

whose docstring is:

```text
Pointwise principal gauge map epsilon -> xi tensor epsilon.
```

It also reports that the raw symbol does not automatically kill the projected
gauge image. This is useful source-derived computational evidence for the local
symbol shape. It is not a source theorem for a global differential.

The typed operator/action spine supplies a host for a candidate derivation. It
defines a proposed `D_roll` and an action spine with `D_DD`, `S_theta`, and open
IG variation status. It explicitly labels the spine as a canonical proposal, not
proof-grade closure, and states that the RS index still lacks a gauge-fixing or
ghost/subtraction complex and ellipticity certificate.

The actual `D_GU` operator certificate schema sharpens this further. It says the
source-closed actual 0/1 operator is still missing at:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

Therefore the repo does not yet have an actual source operator from which the RS
gauge symmetry can be read as a Noether, BRST, or operator-complex differential.

The strongest tempting positive source is `af4-tau-rs-gauge-fixing`, which states:

```text
psi_a^RS ~ psi_a^RS + nabla_a epsilon
```

and says the map is H-linear because the covariant derivative is built from an
`Sp(64)` connection. This is a useful candidate shape, but the same file is a
reconstruction-grade gauge-fixing/counting argument. It does not cite or derive
the transformation from the current GU action, does not build
`Ghost_RS,H^src`, does not prove that `Field_RS,H^src` is the source-selected
physical RS field module, does not supply a BRST continuation, and does not
prove symbol exactness or ellipticity.

Therefore the direct source-derived facts are:

```text
raw gamma-trace projectors exist over C
raw principal gauge symbol epsilon -> xi tensor epsilon exists in code
reconstruction-grade nabla_epsilon gauge language exists
typed carrier/action spine can host a future derivation
actual source-closed D_GU operator certificate is missing
action/source theorem deriving d_RS,-1 is missing
right-H-linear final RS quotient/BRST object is missing
rank and generation readouts are not promoted
```

## 3. Strongest Positive Construction Attempt

The strongest positive construction tries to promote the raw symbol and AF4
gauge language into a source-origin candidate, with every non-source step marked.

Candidate source differential:

```text
Ghost_RS,H^src = source-selected spinor ghost module
Field_RS,H^src = source-selected gamma-trace-constrained RS field module
d_RS,-1(epsilon) = Pi_gamma-free(nabla^A epsilon)
principal_symbol(d_RS,-1)(xi)(epsilon) = P_+(xi tensor epsilon)
```

This has the right local form because the raw Clifford/projector model already
implements the principal map `epsilon -> xi tensor epsilon`, and the physical
quotient/BRST artifact already identifies:

```text
g_xi : S_4^+ tensor F -> R^+
```

as the natural candidate degree-minus-one symbol.

The strongest source route would be a Noether/BRST certificate:

```text
RS_SOURCE_ORIGIN_CERTIFICATE:
  source_action_or_operator:
    primary GU action, actual D_GU, or Euler-Lagrange source theorem

  source_symmetry:
    infinitesimal parameter epsilon in Ghost_RS,H^src
    field variation delta psi_RS = d_RS,-1 epsilon
    invariance or Noether identity for the source RS action/operator

  H_linearity:
    Ghost_RS,H^src and Field_RS,H^src are right-H modules
    connection used in d_RS,-1 preserves the right-H structure
    gamma-trace projection commutes with right-H multiplication

  projection:
    image(d_RS,-1) is exactly the physical RS gauge equivalence direction
    Pi_raw is related to, but not identified with, Pi_RS^phys without proof

  finality:
    d_RS,-1 extends to C_RS^-1 -> C_RS^0 -> C_RS^1
    or to an equivalent gauge-fixed elliptic block
    symbol exactness or ellipticity holds for every xi != 0

  loss:
    ghosts, antighosts, gauge fixing, gamma trace, H conversion, background,
    and boundary terms are recorded before any rank/index readout
```

If this certificate were supplied, the Cycle 2 quotient transport builder would
have a valid source witness and could proceed to projection/finality/loss
validation. That is the strongest positive route available.

The current repo does not instantiate the certificate. The construction above
uses the raw principal symbol and a reconstruction-grade gauge phrase as a
candidate, not as a derived source theorem.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
RS_SOURCE_ORIGIN_CERTIFICATE.source_action_or_operator = MISSING
```

Equivalently:

```text
No current source proves that d_RS,-1 is generated by a GU action, a source
Noether theorem, or a source-closed actual D_GU operator.
```

This obstruction is first because all later gates depend on it. Without source
origin, the candidate map cannot be typed as the physical gauge equivalence
relation. Without that relation, `Pi_RS^phys` is undefined. Without `Pi_RS^phys`
or an equivalent BRST/gauge-fixed object, there is no final H-linear RS
Fredholm/index object.

The obstruction is not the lack of a plausible formula. The plausible formula is
available:

```text
d_candidate(epsilon) = Pi_gamma-free(nabla^A epsilon)
sigma(d_candidate)(xi)(epsilon) = P_+(xi tensor epsilon)
```

The obstruction is the missing proof that this formula is the source-derived
RS gauge/BRST differential for the current GU branch.

The exact missing subobjects are:

```text
source_action_or_operator:
  missing actual GU RS action/operator/EL source whose symmetry is d_RS,-1

source_Noether_or_BRST_identity:
  missing proof that delta psi_RS = nabla epsilon is a source symmetry

module_definition:
  missing Ghost_RS,H^src and Field_RS,H^src as source-selected right-H modules

connection_compatibility:
  asserted in reconstruction prose, not proved from the source connection data

image_identification:
  missing proof that im(d_RS,-1) is exactly the physical RS gauge direction

complex_finality:
  missing C_RS^-1 -> C_RS^0 -> C_RS^1 or gauge-fixed elliptic block

symbol_finality:
  missing exactness or ellipticity for all nonzero covectors

loss_ledger:
  missing ghost/antighost/gauge/H/background/APS accounting for this source map
```

The AF4 gauge-fixing note cannot close this obstruction by itself. It contains a
candidate transformation and H-linearity assertion, but it is not a source-origin
certificate and it mixes fiber-count, index-count, and representation-filter
claims that later artifacts have quarantined behind the quotient/BRST builder.

## 5. Constructive Next Object

The constructive next object is:

```text
RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1
```

Minimum fields:

```text
certificate_id: RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1
source_action_or_operator:
  primary_source_reference_or_repo_source_object
  actual_operator_formula_or_action_variation
  status: DERIVED | COMPARISON | MISSING

ghost_module:
  name: Ghost_RS,H^src
  bundle_or_section_space
  right_H_action
  connection

field_module:
  name: Field_RS,H^src
  gamma_trace_constraint
  right_H_action
  connection

differential:
  formula
  source_derivation
  principal_symbol_relation_to_epsilon_xi_tensor_epsilon
  right_H_linearity_proof
  connection_compatibility_proof

source_symmetry:
  Noether_identity_or_BRST_operator
  proof_that_im_d_is_physical_gauge_direction

finality:
  BRST_complex_or_gauge_fixed_block
  symbol_exactness_or_ellipticity_for_all_xi_nonzero
  H_linear_Fredholm_or_trace_object

loss:
  gamma_trace_loss
  gauge_image_loss
  ghost_antighost_subtraction
  complex_to_H_conversion
  background_F_ch2_dependence
  APS_eta_h_spectral_flow_if_used

target_quarantine:
  no physical rank, H-index, or generation target appears as input
```

Decision statuses:

```text
ACCEPT_SOURCE_DERIVED_D_RS_MINUS_1
FAIL_SOURCE_ACTION_OR_OPERATOR_MISSING
FAIL_ONLY_RAW_PRINCIPAL_SYMBOL
FAIL_ONLY_RECONSTRUCTION_GAUGE_PROSE
FAIL_RIGHT_H_LINEarity
FAIL_CONNECTION_COMPATIBILITY
FAIL_IMAGE_NOT_PHYSICAL_GAUGE_DIRECTION
FAIL_NO_BRST_OR_GAUGE_FIXED_FINALITY
FAIL_NONEXACT_OR_NONELLIPTIC_SYMBOL
FAIL_LOSS_LEDGER
INVALID_TARGET_INPUT
```

The next worker should fill this certificate before any further RS rank or
generation arithmetic is attempted.

## 6. Impact On GU Claim

The impact is a precise deferral, not a demotion of the working hypothesis.

If the GU RS branch is correct, the source theory should contain the missing
object:

```text
d_RS,-1 : Ghost_RS,H^src -> Field_RS,H^src
```

as an action-derived or source-theorem-derived gauge/BRST differential whose
principal symbol matches the raw map already computed. The current repo has the
local candidate shape but not the source derivation.

Current GU claim status:

```text
RS physical quotient/BRST object = NOT_DEFINED
source-derived d_RS,-1 = NOT_SUPPLIED
raw gauge principal symbol = CONTEXT_ONLY
typed/action host = PROPOSAL_ONLY
AF4 gauge-fixing count = NOT_A_SOURCE_ORIGIN_CERTIFICATE
rank readout = QUARANTINED
generation readout = NOT_DERIVED
```

Any downstream artifact that identifies `Pi_raw` with `Pi_RS^phys`, treats the
raw projected gauge image as a physical loss, or uses target rank/index/generation
values before this certificate is filled should be rolled back.

## 7. Next Meaningful Proof/Computation Step

Do a source-origin derivation search, not another raw projector computation:

1. Extract the actual GU action/operator/Euler-Lagrange object for the RS
   sector, or explicitly mark it absent.
2. Derive the infinitesimal source symmetry and Noether identity, if present.
3. Define `Ghost_RS,H^src` and `Field_RS,H^src` on the same source-selected
   right-H carrier.
4. Prove that `d_RS,-1(epsilon)` globalizes and has principal symbol
   `epsilon -> xi tensor epsilon`.
5. Prove right-H linearity and connection compatibility from the source
   connection, not from informal analogy.
6. Prove that `im(d_RS,-1)` is exactly the physical RS gauge direction.
7. Complete the BRST complex or gauge-fixed block and prove symbol
   exactness/ellipticity for every nonzero covector.
8. Only after those pass, hand the certificate to the quotient transport builder.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE3_RS_SOURCE_DIFFERENTIAL_ORIGIN_SCREEN",
  "version": "2026-06-25",
  "verdict": "BLOCKED_RAW_PRINCIPAL_SYMBOL_ONLY__SOURCE_DERIVED_D_RS_MINUS_1_NOT_SUPPLIED",
  "verdict_class": "blocked",
  "decision_for_current_sources": "FAIL_SOURCE_DERIVATION_GATE",
  "screened_object": {
    "id": "d_RS,-1",
    "required_map": "Ghost_RS,H^src -> Field_RS,H^src",
    "required_origin": "action_or_source_theorem_derived_H_linear_RS_gauge_BRST_differential",
    "current_status": "NOT_SUPPLIED"
  },
  "source_derived_context": {
    "raw_gamma_trace_projectors_available": true,
    "raw_principal_gauge_symbol_available": true,
    "raw_principal_gauge_symbol": "epsilon -> xi tensor epsilon",
    "reconstruction_grade_nabla_epsilon_gauge_language_available": true,
    "typed_operator_action_spine_available_as_host": true,
    "actual_D_GU_source_closed_operator_certificate_available": false,
    "action_or_source_theorem_derived_d_RS_minus_1_available": false,
    "BRST_complex_or_gauge_fixed_finality_available": false,
    "Pi_RS_phys_defined": false
  },
  "strongest_positive_construction_attempt": {
    "candidate_formula": "d_candidate(epsilon)=Pi_gamma_free(nabla^A epsilon)",
    "candidate_principal_symbol": "P_plus(xi tensor epsilon)",
    "uses_repo_raw_symbol": true,
    "uses_AF4_reconstruction_gauge_phrase": true,
    "status": "CANDIDATE_SHAPE_ONLY_NOT_SOURCE_DERIVED",
    "would_pass_if": [
      "primary_GU_action_operator_or_EL_derives_the_symmetry",
      "Ghost_RS_H_src_and_Field_RS_H_src_are_defined_on_one_source_carrier",
      "right_H_linearity_is_proved_from_source_connection",
      "connection_compatibility_is_proved",
      "image_is_exactly_physical_RS_gauge_direction",
      "BRST_complex_or_gauge_fixed_elliptic_block_is_supplied",
      "symbol_exactness_or_ellipticity_holds_for_all_nonzero_covectors",
      "loss_ledger_is_complete_and_target_free"
    ]
  },
  "first_exact_obstruction": {
    "field": "RS_SOURCE_ORIGIN_CERTIFICATE.source_action_or_operator",
    "status": "MISSING",
    "description": "No current repo source derives d_RS,-1 from a primary GU action, source Noether theorem, BRST theorem, or source-closed actual D_GU operator.",
    "why_first": "Projection, finality, loss, and physical quotient semantics are typed relative to the source differential.",
    "not_enough": [
      "raw principal symbol epsilon -> xi tensor epsilon",
      "reconstruction-grade psi_a ~ psi_a + nabla_a epsilon statement",
      "typed operator/action host proposal",
      "fiber-count or representation-count gauge-fixing prose"
    ]
  },
  "constructive_next_object": {
    "id": "RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1",
    "required_sections": [
      "source_action_or_operator",
      "ghost_module",
      "field_module",
      "differential",
      "source_symmetry",
      "projection_semantics",
      "finality",
      "loss",
      "target_quarantine"
    ],
    "decision_statuses": [
      "ACCEPT_SOURCE_DERIVED_D_RS_MINUS_1",
      "FAIL_SOURCE_ACTION_OR_OPERATOR_MISSING",
      "FAIL_ONLY_RAW_PRINCIPAL_SYMBOL",
      "FAIL_ONLY_RECONSTRUCTION_GAUGE_PROSE",
      "FAIL_RIGHT_H_LINEarity",
      "FAIL_CONNECTION_COMPATIBILITY",
      "FAIL_IMAGE_NOT_PHYSICAL_GAUGE_DIRECTION",
      "FAIL_NO_BRST_OR_GAUGE_FIXED_FINALITY",
      "FAIL_NONEXACT_OR_NONELLIPTIC_SYMBOL",
      "FAIL_LOSS_LEDGER",
      "INVALID_TARGET_INPUT"
    ]
  },
  "effect_layers": {
    "source": {
      "status": "MISSING_SOURCE_DERIVATION",
      "raw_symbol_available": true,
      "source_theorem_available": false
    },
    "projection": {
      "status": "BLOCKED_BY_SOURCE",
      "Pi_RS_phys_defined": false,
      "may_identify_Pi_raw_with_Pi_RS_phys": false
    },
    "finality": {
      "status": "BLOCKED_BY_SOURCE",
      "BRST_complex_available": false,
      "gauge_fixed_elliptic_block_available": false,
      "symbol_exact_or_elliptic_all_nonzero_xi": false
    },
    "loss": {
      "status": "BLOCKED_BY_SOURCE",
      "complete_loss_ledger_available": false
    }
  },
  "rank_quarantine": {
    "status": "ACTIVE",
    "promote_physical_rank_now": false,
    "promote_H_index_now": false,
    "promote_rank_3_now": false,
    "promote_rank_4_now": false,
    "promote_rank_8_now": false,
    "promote_generation_count_now": false,
    "forbidden_inputs": [
      "physical_rank_target",
      "H_index_target",
      "rank_3",
      "rank_4",
      "rank_8",
      "three_generations",
      "four_generations",
      "normalization_chosen_after_target_comparison",
      "raw_projector_rank_as_physical_rank",
      "raw_projected_gauge_image_as_physical_loss"
    ]
  },
  "rollback_conditions": [
    "claims_source_derived_d_RS_minus_1_from_raw_principal_symbol_only",
    "claims_source_derived_d_RS_minus_1_from_AF4_gauge_prose_only",
    "identifies_Pi_raw_with_Pi_RS_phys_without_source_origin_certificate",
    "uses_projected_raw_gauge_image_as_physical_loss_without_BRST_finality",
    "claims_physical_rank_before_RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1_accepts",
    "claims_H_index_before_final_H_linear_Fredholm_object_exists",
    "claims_rank_3_or_rank_4_or_rank_8_before_source_finality",
    "claims_generation_count_before_source_finality",
    "imports_target_normalization_or_generation_value_as_construction_input"
  ],
  "impact_on_GU_claim": {
    "GU_RS_branch_falsified": false,
    "current_branch_status": "SOURCE_ORIGIN_BLOCKED",
    "what_must_exist_if_branch_correct": "action_or_source_theorem_derived_H_linear_d_RS_minus_1_whose_symbol_matches_epsilon_to_xi_tensor_epsilon",
    "next_gate": "fill_RS_D_MINUS_1_SOURCE_ORIGIN_CERTIFICATE_V1_then_rerun_quotient_transport_builder"
  }
}
```
