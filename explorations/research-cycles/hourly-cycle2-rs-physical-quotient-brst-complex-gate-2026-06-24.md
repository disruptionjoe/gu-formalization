---
title: "Hourly Cycle 2 RS Physical Quotient/BRST Complex Gate"
date: "2026-06-24"
status: exploration
doc_type: frontier_run_artifact
verdict: "UNDERDEFINED_PHYSICAL_QUOTIENT_BRST_COMPLEX_MISSING"
owned_path: "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
audit:
  - "tests/hourly_cycle2_rs_physical_quotient_brst_complex_gate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md"
  - "explorations/cycle1-generation-rs-rank-direct-gate-2026-06-24.md"
  - "explorations/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md"
  - "explorations/cycle2-physical-rs-projector-effective-operator-certificate-2026-06-24.md"
  - "tests/rs_clifford_projector_model.py"
  - "tests/rs_k3_symbol_index_formula_audit.py"
---

# Hourly Cycle 2 RS Physical Quotient/BRST Complex Gate

## 1. Verdict

**Verdict: underdefined physical quotient/BRST complex missing.**

The Cycle 1 blocker can be pushed down one level. The repo does not merely lack
a numeric physical RS effective rank. It lacks the source-defined physical
quotient or BRST complex that would define the projector:

```text
Pi_RS^phys : M_RS,H^src -> M_RS,H^src
```

The raw complex projector is real and useful:

```text
rank_C(Pi_raw E_+ Pi_raw) = 96
```

but the current sources do not define the physical equivalence relation,
BRST differential, ghost/subtraction terms, gauge-fixing condition, symbol
exactness, ellipticity certificate, H-linear trace, source-selected `F/ch2`,
or same-operator `K3/Y14` bridge needed to turn `Pi_raw` into `Pi_RS^phys`.

Current decision:

```text
Pi_RS^phys = NOT_DEFINED
physical quotient/BRST complex = MISSING
rank_4 = NOT_PROMOTED
rank_8 = NOT_PROMOTED
raw 96_C = RAW_ONLY_NOT_PHYSICAL_EFFECTIVE_RANK
generation count = NOT_DERIVED
```

This is not a proof that the physical rank is neither `4` nor `8`. It is a
typing decision: the physical object whose rank would decide between those
values has not been source-defined.

## 2. Physical Quotient/BRST Complex Signature

A physical quotient/BRST complex sufficient to define `Pi_RS^phys` must supply
the following typed signature on one source-selected right-H module.

```text
RS_PHYS_QUOTIENT_BRST_SIGNATURE =
  source_operator:
    D_GU, D_roll, an action-derived operator, or an explicitly labeled
    comparison operator

  domain:
    M_RS,H^src, including bundle, completion/domain, right-H action,
    connection, compact/K3/Y14/APS choice, and coefficient background

  raw_constraint:
    G_+ : T*K3 tensor S_4^+ tensor F -> S_4^- tensor F
    G_- : T*K3 tensor S_4^- tensor F -> S_4^+ tensor F
    R^+ = ker(G_+), R^- = ker(G_-)

  gauge_or_BRST:
    C^{-1} --d_-1--> C^0 --d_0--> C^1
    with C^0 carrying the gamma-trace-constrained RS field,
    d_-1 the source gauge differential, and d_0 the physical RS operator
    or symbol-level equation map

  ghost_subtraction:
    ghost and antighost bundles, signs, degrees, and virtual-class
    contribution, derived from the same source gauge symmetry

  physical_states:
    image(Pi_RS^phys) = H^0(C^bullet_RS) or an equivalent gauge-fixed
    harmonic representative space

  symbol_gate:
    for every nonzero covector xi, the symbol complex is exact or the
    gauge-fixed symbol is elliptic

  trace_gate:
    Pi_RS^phys and the effective coefficient/K-class are H-linear and
    admit a certified H-linear finite-rank trace or Fredholm index

  background_and_bridge:
    F = s^*S(6,4) or labeled comparison F, ch_2(F)[K3], and a
    same-operator K3/Y14 or APS bridge with correction terms

  target_quarantine:
    rank_4, rank_8, ind_H(D_RS)=8, ind_H(D_GU)=24, and generation counts
    are comparison outputs only, never construction inputs
```

Against this signature, the current repo status is:

| signature field | current status | decision |
|---|---|---|
| domain | no source-selected right-H physical domain | missing |
| gamma-trace constraint | raw complex `G_+`, `G_-`, `P_+`, `P_-` computed | raw-only available |
| gauge map | raw principal sample `epsilon -> xi tensor epsilon` checked | source global gauge map missing |
| gauge fixing | no physical gauge condition supplied | missing |
| BRST differential | no source-derived differential or cohomology supplied | missing |
| ghost/subtraction | comparison arithmetic exists, but no derived ghost complex | missing |
| symbol exactness | no all-`xi` exactness proof for a quotient complex | missing |
| ellipticity | no gauge-fixed elliptic symbol or elliptic complex | missing |
| H-linear trace | no global H-linear trace/index conversion certificate | missing |
| `F/ch2` | `rank_C(F)=16` appears as control data; physical `ch2` not fixed | underdefined |
| `K3/Y14` bridge | compact K3 remains control-only without same-operator bridge | underdefined |

The current sources therefore do not define `Pi_RS^phys`.

## 3. What Raw Projector Code Does And Does Not Establish

`tests/rs_clifford_projector_model.py` establishes a concrete raw complex
`Cl(4,0)` model:

```text
S_4^+ = C^2
S_4^- = C^2
F = C^16
V_+ = C^4 tensor S_4^+ tensor F = C^128
V_- = C^4 tensor S_4^- tensor F = C^128
G_+ : V_+ -> S_4^- tensor F = C^32
G_- : V_- -> S_4^+ tensor F = C^32
```

It verifies:

```text
rank_C(ker G_+) = 96
rank_C(ker G_-) = 96
P_+^2 = P_+
P_-^2 = P_-
G_+ P_+ = 0
G_- P_- = 0
```

The same raw data support the direct composite:

```text
Pi_raw = orthogonal projector onto the full raw gamma-trace kernel
E_+    = raw spinor chirality projector
rank_C(Pi_raw E_+ Pi_raw) = 96
```

The sample nonzero covector calculation also finds the raw projected symbol
full rank on the raw gamma-trace kernels, and it finds a projected principal
gauge image of rank `32_C` that is not killed by the raw symbol.

That establishes:

```text
raw gamma-trace projectors: established over C
raw direct rank 96_C: established
sample raw symbol sanity: established
projected gauge image not silently quotiented: established
```

It does not establish:

```text
physical quotient equivalence relation
source-derived gauge symmetry
BRST differential or ghost complex
symbol exactness for the quotient
ellipticity of a gauge-fixed physical RS complex
Pi_RS^phys as an H-linear projector
E_RS^eff as an H-linear effective coefficient/K-class
H-linear trace or index conversion
source-selected F and ch_2(F)[K3]
same-operator K3/Y14 bridge
rank_4 or rank_8
```

The raw code therefore narrows the obstruction. The problem is not the absence
of elementary gamma-trace matrices. The problem is the absence of the physical
quotient/BRST layer that tells us which raw directions are gauge, ghost,
physical, or trace-visible.

## 4. Strongest Positive Construction Attempt

The strongest positive attempt that can be written from the current sources is
a candidate compact K3 comparison complex. It is not source-derived yet, but it
is the right shape to test.

For each nonzero covector `xi`, use the raw maps:

```text
R^+ = ker(G_+)
R^- = ker(G_-)
P_+ : V_+ -> R^+
P_- : V_- -> R^-
g_xi : S_4^+ tensor F -> R^+
      epsilon |-> P_+(xi tensor epsilon)
sigma_raw(xi) = P_- (c(xi) tensor 1_F) P_+ : R^+ -> R^-
```

The candidate BRST-style symbol skeleton would be:

```text
C^{-1}_xi = S_4^+ tensor F
C^0_xi    = R^+
C^1_xi    = R^-

C^{-1}_xi --g_xi--> C^0_xi --sigma_phys(xi)--> C^1_xi
```

with an added gauge-fixing/antighost block or an equivalent elliptic complex so
that the physical degree-zero object is:

```text
H^0_RS(xi) = ker(sigma_phys(xi)) / im(g_xi)
```

and `Pi_RS^phys` is the H-linear harmonic representative projector for that
cohomology.

This attempt is valuable because it exposes the exact work left to do:

1. prove `g_xi` is the actual source gauge map, not only a raw principal map;
2. define `sigma_phys`, not merely `sigma_raw`;
3. add the ghost/antighost or gauge-fixing terms with signs and degrees;
4. prove symbol exactness or ellipticity for all `xi != 0`;
5. lift the construction to a global right-H module with H-linear connection;
6. compute the K-class/Chern character using the actual source-selected `F`;
7. bridge the same physical complex between K3 control and the `Y14` branch.

The current repo supplies only the raw ingredients in steps 1 and 2 as local
complex matrices. It does not supply the source theorem that identifies this
skeleton with the physical GU RS quotient.

## 5. First Exact Missing Object

The first exact missing object is the source-defined gauge/BRST differential:

```text
d_RS,-1 : Ghost_RS,H^src -> Field_RS,H^src
```

with:

```text
Field_RS,H^src includes the gamma-trace-constrained RS field;
im(d_RS,-1) is exactly the physical gauge equivalence direction;
d_RS,-1 is H-linear and connection-compatible;
d_RS,-1 is paired with a gauge-fixing or BRST continuation;
the resulting symbol complex is exact or elliptic for xi != 0.
```

Without this object, the repo cannot tell whether the projected raw gauge image
of rank `32_C` is to be quotiented, gauge-fixed, left physical, cancelled by
ghosts, or transported with an APS correction. Therefore `Pi_RS^phys` cannot be
identified with `Pi_raw`, and `rank_H(Pi_RS^phys E_RS^eff Pi_RS^phys)` is not
a defined physical quantity.

This is one level lower than the previous broad blocker. The broad blocker was:

```text
No common source-selected right-H module supports Pi_RS^phys and E_RS^eff.
```

The lower blocker is:

```text
No source-defined gauge/BRST differential defines the physical quotient inside
the raw gamma-trace-constrained RS field space.
```

## 6. Impact For Rank 4/Rank 8/Generation Count

No current source promotes either candidate.

```text
rank_4 status: NOT_PROMOTED
rank_8 status: NOT_PROMOTED
three-generation readout: NOT_DERIVED
four-generation readout: NOT_DERIVED
```

If a future source-selected quotient/BRST certificate computes:

```text
rank_H(E_RS^eff) = 4
ind_H(D_RS^phys) = 8
```

then Candidate A survives conditionally, subject to the separate spin-1/2,
additivity, background, and bridge gates.

If it computes:

```text
rank_H(E_RS^eff) = 8
ind_H(D_RS^phys) = 16
```

then Candidate B survives conditionally as the four-generation compact-model
branch.

If it computes another H-index, both candidate readouts fail or must be
reformulated. If it computes only a complex rank, a raw rank, a background
dependent formula, or a compact K3 control class without bridge, no generation
branch is promoted.

The raw `96_C` result does not count as a physical effective rank, does not
become `48_H` without an H-linear trace certificate, and does not reduce to
`4` or `8` by normalization.

## 7. Rollback/Falsification Conditions

Rollback is required if any downstream artifact:

- claims `rank_4` from `ind_H(D_RS)/Ahat(K3)=8/2`;
- claims `rank_8` without a source-defined physical quotient/BRST complex;
- treats `Pi_raw` as `Pi_RS^phys` without the gauge/BRST differential;
- treats raw `96_C` as an effective physical H-rank or APS coefficient rank;
- halves a complex rank without an H-linear trace and H-compatible connection;
- uses the BRST-style `raw - 2 * ghost` formula without deriving the ghost
  bundles and signs from the source gauge symmetry;
- assumes `F=C^16`, `rank_H(F)=8`, or `ch_2(F)[K3]=0` as physical background
  rather than source-selected data;
- cites compact K3 control arithmetic as physical GU evidence without a
  same-operator `K3/Y14` or APS bridge;
- promotes three generations or four generations before the physical RS
  quotient/BRST rank is source-derived;
- selects a normalization after seeing whether it yields `4`, `8`, `24`, or
  `32`.

Falsification is stronger than rollback. This quotient/BRST branch fails if a
complete source-derived gauge/BRST differential cannot be made H-linear, if its
symbol complex is not exact or elliptic under the GU source assumptions, or if
the resulting same-operator bridge to K3/Y14 cannot be supplied while compact
K3 remains the readout surface.

## 8. Next Meaningful Computation

The next computation should build a certificate for the quotient/BRST complex,
not another raw projector rank.

Executable target:

```text
RS_PHYSICAL_QUOTIENT_BRST_COMPLEX_BUILDER
```

Minimum JSON output:

```json
{
  "certificate": "RS_PHYSICAL_QUOTIENT_BRST_COMPLEX",
  "source_operator": null,
  "target_inputs_seen": [],
  "domain": {
    "common_right_H_module": false,
    "compact_or_y14_or_aps": null
  },
  "gamma_trace_constraint": {
    "raw_maps_available": true,
    "source_physical_constraint": false
  },
  "gauge_map": {
    "raw_principal_map_available": true,
    "source_global_gauge_map": false,
    "projected_raw_gauge_image_rank_C": 32
  },
  "brst_or_quotient": {
    "differential_defined": false,
    "ghost_bundles_defined": false,
    "antighost_or_gauge_fixing_defined": false,
    "degree_zero_cohomology_defined": false
  },
  "symbol_gate": {
    "symbol_exact_for_all_nonzero_xi": false,
    "elliptic_or_elliptic_complex": false
  },
  "Pi_RS_phys": {
    "available": false,
    "may_identify_with_Pi_raw": false
  },
  "H_trace": {
    "right_H_structure_verified": false,
    "complex_to_H_conversion_allowed": false
  },
  "background": {
    "rank_C_F": 16,
    "ch2_F_K3": "required"
  },
  "bridge": {
    "same_operator_K3_Y14_or_APS": false,
    "eta_h_spectral_flow_end_terms": "required_if_APS"
  },
  "decision": "MISSING_SOURCE_DEFINED_GAUGE_BRST_DIFFERENTIAL"
}
```

Decision rule:

```text
target input seen -> INVALID_TARGET_DIVISION
raw projector only -> RAW_ONLY_NOT_PHYSICAL_QUOTIENT
no d_RS,-1 -> MISSING_SOURCE_DEFINED_GAUGE_BRST_DIFFERENTIAL
no ghost/gauge-fixing -> MISSING_GHOST_OR_GAUGE_FIXING
no exactness/ellipticity -> NON_ELLIPTIC_OR_UNPROVED_SYMBOL_COMPLEX
no H trace -> COMPLEX_ONLY
no source F/ch2 -> BACKGROUND_UNDERDEFINED
no same-operator bridge -> K3_CONTROL_ONLY
rank_H=4 after all gates -> CANDIDATE_A_SURVIVES_CONDITIONALLY
rank_H=8 after all gates -> CANDIDATE_B_SURVIVES_CONDITIONALLY
other rank after all gates -> CANDIDATES_A_AND_B_FAIL_OR_REFORMULATE
```

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE2_RS_PHYSICAL_QUOTIENT_BRST_COMPLEX_GATE",
  "version": "2026-06-24",
  "verdict": "UNDERDEFINED_PHYSICAL_QUOTIENT_BRST_COMPLEX_MISSING",
  "current_decision": "MISSING_SOURCE_DEFINED_GAUGE_BRST_DIFFERENTIAL",
  "pi_rs_phys_defined": false,
  "source_derived_physical_rank_available": false,
  "promotion_allowed_now": false,
  "three_generations_derived": false,
  "four_generations_derived": false,
  "generation_count_claim_status": "NOT_DERIVED",
  "rank_status": {
    "rank_4": {
      "status": "NOT_PROMOTED",
      "reason": "No source-defined physical quotient/BRST complex defines Pi_RS^phys."
    },
    "rank_8": {
      "status": "NOT_PROMOTED",
      "reason": "No source-defined physical quotient/BRST complex defines Pi_RS^phys."
    },
    "physical_effective_rank": "UNDERDEFINED",
    "raw_rank_C_Pi_raw_E_plus_Pi_raw": 96,
    "raw_rank_status": "RAW_ONLY_NOT_PHYSICAL_EFFECTIVE_RANK"
  },
  "raw_projector_result": {
    "computed_object": "Pi_raw E_+ Pi_raw",
    "field": "C",
    "rank": 96,
    "status": "RAW_ONLY_NOT_PHYSICAL_EFFECTIVE_RANK",
    "promoted_to_Pi_RS_phys": false,
    "promoted_to_effective_rank": false,
    "promoted_to_generation_claim": false
  },
  "quotient_brst_signature": {
    "source_operator": {
      "status": "MISSING"
    },
    "domain": {
      "status": "MISSING_SOURCE_SELECTED_RIGHT_H_DOMAIN",
      "required_for_Pi_RS_phys": true
    },
    "gamma_trace_constraint": {
      "status": "RAW_COMPLEX_AVAILABLE_NOT_PHYSICAL",
      "raw_maps_available": true,
      "physical_constraint_source_defined": false
    },
    "gauge_map": {
      "status": "RAW_PRINCIPAL_SAMPLE_AVAILABLE_SOURCE_GAUGE_MISSING",
      "raw_principal_map_available": true,
      "projected_raw_gauge_image_rank_C": 32,
      "source_global_gauge_map": false
    },
    "gauge_fixing_condition": {
      "status": "MISSING"
    },
    "BRST_differential": {
      "status": "MISSING",
      "required_object": "d_RS,-1"
    },
    "ghost_subtraction": {
      "status": "MISSING_SOURCE_DERIVED",
      "comparison_arithmetic_only": true
    },
    "symbol_exactness": {
      "status": "MISSING",
      "sample_raw_symbol_only": true
    },
    "ellipticity": {
      "status": "MISSING"
    },
    "physical_cohomology": {
      "status": "MISSING"
    },
    "Pi_RS_phys": {
      "status": "MISSING",
      "may_identify_with_Pi_raw": false
    },
    "E_RS_eff": {
      "status": "MISSING",
      "same_domain_as_Pi_RS_phys": false
    },
    "H_linear_trace": {
      "status": "MISSING",
      "complex_to_H_conversion_allowed": false
    },
    "source_selected_F_ch2": {
      "status": "UNDERDEFINED",
      "rank_C_F_context": 16,
      "ch2_F_K3": "required"
    },
    "K3_Y14_bridge": {
      "status": "UNDERDEFINED",
      "same_operator_required": true
    },
    "target_quarantine": {
      "status": "ACTIVE",
      "target_division_forbidden": true,
      "rollback_label": "INVALID_TARGET_DIVISION"
    }
  },
  "source_definition_decisions": {
    "domain": "missing",
    "gauge_map": "raw_principal_sample_only",
    "gamma_trace_constraint": "raw_complex_available_only",
    "ghost_subtraction": "missing_source_derived",
    "ellipticity_or_symbol_exactness": "missing",
    "H_linear_trace": "missing",
    "source_selected_F_ch2": "underdefined",
    "K3_Y14_bridge": "underdefined"
  },
  "first_exact_missing_object": {
    "id": "d_RS,-1",
    "description": "source-defined H-linear gauge/BRST differential from ghost parameters to the gamma-trace-constrained RS field space",
    "why_first": "Without d_RS,-1 there is no physical quotient relation and Pi_RS^phys cannot be distinguished from Pi_raw."
  },
  "candidate_implications": {
    "rank_4_if_source_derived_after_all_gates": "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
    "rank_8_if_source_derived_after_all_gates": "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
    "other_rank_if_source_derived_after_all_gates": "CANDIDATES_A_AND_B_FAIL_OR_REQUIRE_REFORMULATION",
    "raw_rank_96C": "DOES_NOT_PROMOTE_EITHER_CANDIDATE"
  },
  "target_division_status": {
    "forbidden": true,
    "forbidden_formula": "rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2",
    "rollback_label": "INVALID_TARGET_DIVISION"
  },
  "rollback_conditions": [
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_source_defined_physical_quotient_BRST_complex",
    "identifies_Pi_raw_with_Pi_RS_phys_without_gauge_BRST_differential",
    "treats_raw_rank_96C_as_effective_physical_rank",
    "halves_complex_rank_without_H_linear_trace_certificate",
    "uses_BRST_style_subtraction_without_source_derived_ghost_complex",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
    "claims_three_generations_before_source_derived_physical_RS_rank",
    "claims_four_generations_before_source_derived_physical_RS_rank",
    "selects_normalization_after_target_comparison"
  ],
  "next_meaningful_computation": "RS_PHYSICAL_QUOTIENT_BRST_COMPLEX_BUILDER"
}
```
