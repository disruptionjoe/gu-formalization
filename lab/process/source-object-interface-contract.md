---
title: "Source-Object Interface Contract"
status: frozen_spec_no_instance
doc_type: construction_space_contract
created: "2026-07-19"
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
probe: P5-SOURCE-OBJECT-SPEC
source_owner: possibility-to-capability
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Source-Object Interface Contract

P5 freezes the constraint-side shape of the source object requested from
possibility-to-capability. It does not claim that such an object exists. It
only states what a returned source-owned packet must provide before GU can use
it to validate conditional construction-space grades or reopen recovery work.

## Boundary

The source object is a typed import until an actual packet returns. GU may use
this contract for `R0_COND` or `R1_COND` interior exploration, but integration
validation requires a concrete instance with provenance, assumptions,
normalizations, and non-retuning conditions fixed before target comparison.

No claim status, canon verdict, public posture, publication state, or external
action moves here. No external action is authorized.

## Construction Fork

This contract keeps the geometer-versus-physics fork explicit:

- GR uses the GU-native source/residual-bookkeeping question, not an imported
  Einstein stress tensor.
- QM uses the GU-native Krein/BRST physical-sector question, not positive
  Hilbert space by assumption.
- COSMO uses a GU physical scalar channel, not standard SVT variables as
  evidence.
- SM uses source-owned selector evidence, not a Pati-Salam or Spin(10) host as
  a complete Standard Model selector.

## Required Shared Source Object

A returned packet must bind one shared source object across the four legs. If
the packet supplies separate per-sector repairs, the construction-space result
is at best sector-specific hosting and cannot support native unification.

The packet must supply:

- identity and provenance independent of the GU consequence it enables;
- branch assumptions, normalizations, and allowed operations;
- a loss ledger for any reduction or shadow map;
- typed imports and import counts for every granted object;
- explicit failure conditions and rollback language;
- evidence that all target-facing choices were frozen before target use.

## Four-Leg Interface

### GR Leg

The GR leg must provide a vacuum-supported source or residual-bookkeeping
mechanism that can cancel or evade the trace-free `Q^TF(B)` obstruction at
order `M^2`, while preserving the prior linear cheap-read clears. The packet
must name the ambient/H-class first variation or equivalent source tensor, fix
its coefficient before Schwarzschild/Kerr target use, and show why it is not a
target-shaped stress import or standard Einstein dynamics in disguise.

### QM Leg

The QM leg must supply the six certificate families from P4: a physical quotient
or field complex, state space or local algebra, observable admissibility,
probability rule with positivity and normalization, locality/causal
compatibility, and state-preserving dynamics. It must also state how negative
Krein-norm states are removed or graded out of the physical sector after the
constraints are discharged.

### COSMO Leg

The cosmology leg must supply a physical scalar channel with a gauge-invariant
projector, an observable map to expansion or perturbation quantities, and a
closed SVT quadratic truncation with non-scalar residues discharged. A standard
SVT variable may be comparator language, but it is not GU evidence unless the
source object supplies the projector and map.

### SM Leg

The Standard Model leg must supply a source-owned target-free selector or
equivalent finite algebra/gauge quotient/observer-shadow packet that handles
chirality, three generations, absolute hypercharge normalization, a physical
Higgs sector, a complete surviving spectrum, and extra or mirror mode
decoupling. Host evidence is useful only as typed support; it is not the
selector.

## Consistency And Failure Reading

The first P6-era test is internal consistency: can one frozen source object
satisfy all four legs without hidden target imports or mutually inconsistent
normalizations? If the leg demands are mutually inconsistent for the
predeclared source-object families, that is a falsification-shaped result for
the predeclared construction class under the P0 endings. It is not a global GU
verdict.

## Handoff

This contract should be routed to the possibility-to-capability mailbox as a
`source_object_interface_contract` proposal. The current child run cannot write
that cross-owner mailbox, so the parent should route the payload from the run
receipt or final result.

## Addendum (2026-07-19 evening): constraints recovered from the 2026-06-27 assembly

Archaeology (`explorations/assembly-archaeology-recovered-parameters-2026-07-19.md`)
recovered spec-sheet constraints the four-leg form must also satisfy:

- the packet's action-level structure must FORCE `delta_2 . d_RS,-1 = 0` via
  a Noether identity (not supply the differential as bare data);
- a NON-EQUIVARIANT compensator (sigma_c outside the Spin(9,5) family) is
  required — every equivariant attempt provably cannot close;
- the physical sector must be realized cohomologically (clean decoupling is
  Velo-Zwanziger-acausal; the ghost is causality-required);
- generations require either an a-priori rank pin or a NON-QUATERNIONIC
  structure (quaternionic-parity no-go: GU-native carriers have even index);
- the three global objects stand: families pushforward over GL(4,R)/O(3,1);
  the global boundary holonomy/spectral section of the non-compact Y14 end
  (lineage of DEP-NATIVE-SOURCE-DATUM); a BV-to-boundary-Dirac map;
- any compensator structure must reproduce the exact C2 scale law
  C2(2xi)/C2(xi) = 2.

Resolved payload-typing questions: the transmitted Z/2 orientation is
quaternionic-commuting in the `(9,5)` H-class and cannot discharge generations.
`P-RANK-FOLD` additionally shows that the finite subgroup-chain datum acts on
the internal Spin(10) factor and cannot carry the mirror selector or collapse
the extra `SU(2)-` doublet. The native value `3 = dim Lambda^2_+` survives, but
the packet must supply a distinct generation-physicalization selector rather
than an arbitrary integer. B.5 remains source-owned and unconstructed.

## Machine-Readable Contract

```json
{
  "artifact": "SOURCE_OBJECT_INTERFACE_CONTRACT",
  "probe": "P5-SOURCE-OBJECT-SPEC",
  "status": "FROZEN_SPEC_NO_INSTANCE",
  "source_owner": "possibility-to-capability",
  "gu_owner": "gu-formalization",
  "contract_ref": "lab/process/source-object-interface-contract.md",
  "evidence_inputs": [
    "lab/process/construction-space-exploration-protocol.md",
    "lab/process/construction-space-preregistered-endings-2026-07-19.md",
    "explorations/construction-space-gr-r0-lemma-c9-c3-2026-07-19.md",
    "explorations/construction-space-sm-r0-harness-c5-2026-07-19.md",
    "explorations/construction-space-retro-verify-p3-2026-07-19.md",
    "explorations/construction-space-qm-checklist-p4-2026-07-19.md",
    "lab/process/construction-space-map.json"
  ],
  "source_requirements": {
    "identity": [
      "frozen_before_target_use",
      "source_owned_not_gu_constructed_from_consequence",
      "provenance_independent_of_gu_result",
      "branch_assumptions_explicit",
      "normalizations_explicit",
      "non_retuning_conditions_explicit"
    ],
    "sharedness": [
      "one_source_object_across_GR_QM_COSMO_SM",
      "shared_normalizations_or_explicit_loss_ledger",
      "typed_import_count_for_every_granted_object"
    ]
  },
  "legs": [
    {
      "id": "GR",
      "must_supply": [
        "vacuum_supported_source_or_residual_bookkeeping",
        "trace_free_QTF_slot_cancellation_or_evasion_at_order_M2",
        "ambient_H_class_first_variation_or_equivalent_source_tensor",
        "coefficient_frozen_before_schwarzschild_kerr_target_use",
        "linear_cheap_read_clears_preserved"
      ],
      "forbidden_shortcuts": [
        "target_shaped_stress_import",
        "standard_einstein_dynamics_as_evidence",
        "zero_or_metric_proportional_tensor_called_trace_free_cancellation"
      ]
    },
    {
      "id": "QM",
      "must_supply": [
        "physical_quotient_or_field_complex",
        "state_space_or_local_algebra",
        "observable_admissibility",
        "probability_rule_with_positivity_and_normalization",
        "locality_or_causal_compatibility",
        "state_preserving_dynamics",
        "negative_norm_physical_state_discharge"
      ],
      "forbidden_shortcuts": [
        "positive_hilbert_space_by_assumption",
        "krein_form_named_as_physical_state_space",
        "brst_complex_without_source_defined_differential"
      ]
    },
    {
      "id": "COSMO",
      "must_supply": [
        "physical_scalar_projector",
        "gauge_invariant_observable_map",
        "closed_SVT_quadratic_truncation",
        "non_scalar_residue_discharge",
        "source_object_to_scalar_channel_binding"
      ],
      "forbidden_shortcuts": [
        "standard_SVT_variable_as_GU_evidence",
        "target_fitted_background_choice",
        "scalar_name_without_projector"
      ]
    },
    {
      "id": "SM",
      "must_supply": [
        "source_owned_target_free_selector",
        "chirality_production",
        "three_generations_without_per_generation_adjustable_structure",
        "absolute_hypercharge_normalization",
        "physical_higgs_sector",
        "complete_surviving_spectrum",
        "extra_or_mirror_mode_decoupling"
      ],
      "forbidden_shortcuts": [
        "host_group_as_selector",
        "relative_hypercharge_arithmetic_as_absolute_normalization",
        "target_spectrum_import"
      ]
    }
  ],
  "mutual_consistency_tests": [
    "no_leg_requires_source_tensor_zero_while_another_requires_nonzero",
    "no_QM_positivity_interface_contradicts_the_declared_Krein_discharge",
    "no_COSMO_scalar_projector_depends_on_target_fitted_background",
    "no_SM_selector_imports_the_target_spectrum_after_comparison",
    "all_shared_normalizations_are_frozen_or_loss_ledgered"
  ],
  "integration_rule": "GU may grade cells R0_COND or R1_COND using this contract as a typed import. A concrete p2c instance is required before integration validation.",
  "failure_reading": "Mutual inconsistency across the legs is a falsification-shaped result for the predeclared construction class only, not a global GU verdict.",
  "handoffs": {
    "p2c_mailbox": "source_object_interface_contract",
    "parent_route_required": true
  }
}
```
