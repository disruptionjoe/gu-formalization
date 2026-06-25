---
title: "Hourly Cycle 1 RS Effective Rank Certificate"
date: "2026-06-24"
status: exploration
doc_type: frontier_run_artifact
verdict: "UNDERDEFINED_PHYSICAL_EFFECTIVE_RANK_CERTIFICATE_MISSING"
owned_path: "explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md"
audit:
  - "tests/hourly_cycle1_rs_effective_rank_certificate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "roadmap/objection-triage-register.md"
  - "explorations/cycle1-generation-rs-rank-direct-gate-2026-06-24.md"
  - "explorations/mission-a-generation-count-analytic-machinery-2026-06-24.md"
  - "explorations/generation-count-rs-rank-gate-2026-06-24.md"
  - "tests/rs_clifford_projector_model.py"
  - "tests/rs_k3_symbol_index_formula_audit.py"
---

# Hourly Cycle 1 RS Effective Rank Certificate

## 1. Verdict

**Verdict: underdefined physical/effective rank certificate missing.**

The repository currently justifies a raw complex gamma-trace projector calculation, not a
source-derived physical RS effective rank. The physical rank expression needed by OBJ-GEN is
not yet well typed:

```text
rank_H(Pi_RS^phys E_RS^eff Pi_RS^phys)
```

because the repo has not supplied a common source-selected right-H module, physical/BRST
quotient, effective coefficient idempotent or K-class, H-linear trace certificate,
source-selected background, and same-operator `Y14 -> K3` bridge.

Current decision:

```text
raw rank_C(Pi_raw E_+ Pi_raw) = 96, established as raw-only context
rank 4 = NOT_JUSTIFIED
rank 8 = NOT_JUSTIFIED
physical effective rank = UNDERDEFINED
three-generation promotion = forbidden now
four-generation promotion = forbidden now
```

This is not a decision for "neither" in the strong sense of a computed physical rank other
than `4` or `8`. It is a decision that neither `4` nor `8` is justified yet, because the
physical object whose rank would decide between them has not been constructed. Target division
is explicitly invalid:

```text
rank_H(E_RS^eff) = ind_H(D_RS) / Ahat(K3) = 8 / 2
```

when `ind_H(D_RS)=8` is imported from the desired three-generation readout.

## 2. What Existing Code/Sources Actually Establish

The required sources establish the following bounded facts.

`RESEARCH-POSTURE.md` sets the governing rule: pursue the GU reconstruction hypothesis, but
do not inflate compatibility, hosted structure, or target-matched arithmetic into derivation.
The relevant forbidden move here is hiding target data inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade artifact with exact
obstruction, rollback conditions, and no promotion from "compatible" to "derived."

`roadmap/objection-triage-register.md` identifies OBJ-GEN as load-bearing. Its decisive
gate is a direct source-derived rank computation returning `4` or `8` without dividing by a
target index.

`explorations/generation-count-rs-rank-gate-2026-06-24.md` separates Candidate A and
Candidate B:

```text
Candidate A: rank_H(E_RS^eff)=4, ind_H(D_RS)=8, total index 24
Candidate B: rank_H(E_RS^eff)=8, ind_H(D_RS)=16, total index 32
```

It also records that neither candidate has been eliminated or derived by the existing
OQ-RK1/OQ-RK2 material.

`explorations/mission-a-generation-count-analytic-machinery-2026-06-24.md` identifies the
missing analytic object as `RS_GU^phys`: a source-derived gauge-fixed or BRST elliptic
Fredholm complex with H-structure, symbol class, background Chern character, and
`Y14 -> K3` or APS bridge data.

`explorations/cycle1-generation-rs-rank-direct-gate-2026-06-24.md` records the closest raw
direct matrix proxy:

```text
Pi_raw = orthogonal projector onto the raw gamma-trace kernel
E_+ = raw 4D spinor chirality projector
rank_C(Pi_raw E_+ Pi_raw) = 96
```

It explicitly demotes this result as raw-only and not a candidate effective rank.

`tests/rs_clifford_projector_model.py` establishes explicit raw complex `Cl(4,0)`
gamma-trace projectors and a sampled raw projected symbol. It verifies:

```text
rank_C(ker G_+) = 96
rank_C(ker G_-) = 96
P_+^2 = P_+
P_-^2 = P_-
G_+ P_+ = 0
G_- P_- = 0
sample raw projected symbol rank_C = 96
projected gauge image rank_C = 32, not quotiented away
```

This is strong raw Clifford evidence. It is not a physical quotient, not a BRST cohomology
calculation, and not an index theorem.

`tests/rs_k3_symbol_index_formula_audit.py` checks compact K3 characteristic-class
arithmetic. In the flat `F=C^16` branch it reports full vector-spinor, raw gamma-trace-free,
BRST-style comparison, and spinor coefficient formulas. The skipped tests are decisive:
the physical GU gauge-fixed RS symbol class and actual `ch2(F)[K3]` are not supplied.

Therefore the existing repo establishes:

```text
raw gamma-trace projector: established over C
raw projected symbol sanity: established over C
K3 control formulas: established as arithmetic/control data
physical/BRST quotient: missing
effective coefficient bundle: missing
H-linear trace: missing
source-selected background: missing
same-operator Y14-to-K3 bridge: missing
source-derived rank 4 or 8: not established
```

## 3. Strongest Positive Construction Attempt

The strongest positive construction is not another raw rank. It is a layered certificate that
would make the requested rank expression well typed before comparison to either candidate.

The certificate should have this shape:

```text
RS_EFFECTIVE_RANK_CERTIFICATE =
  raw_gamma_trace_projector:
    Pi_raw from the existing Cl(4,0) matrix model

  physical_or_BRST_quotient:
    gauge map, gauge fixing or ghost complex, symbol exactness, ellipticity,
    and a source-derived degree-zero physical state space

  Pi_RS^phys:
    H-linear idempotent onto that physical state space

  E_RS^eff:
    H-linear effective coefficient idempotent, or equivalent K-theory symbol
    class, acting on the same source-selected module

  H_linear_trace:
    right-H action, H-compatible connection, and a legitimate trace/index
    conversion from complex data to H-data

  source_selected_background:
    F=s^*S(6,4) or a labeled comparison bundle, rank_C(F)=16,
    H-structure status, and k=ch2(F)[K3]

  same_operator_bridge:
    either an H-unitary Y14 discrete-sector bridge or APS formula for the
    same physical RS operator, including eta, h, spectral flow, and end terms

  target_quarantine:
    proof that rank 4, rank 8, three generations, and four generations were
    not inputs to the construction
```

There is a plausible positive route through these layers:

1. Use `Pi_raw` only as the gamma-trace part of the physical complex.
2. Add a source-derived gauge/BRST complex so that the raw projected gauge image is removed
   by a real quotient rather than by prose.
3. Package the quotient as an H-linear elliptic symbol class or as `Pi_RS^phys`.
4. Define `E_RS^eff` as the actual finite effective coefficient bundle or K-class produced
   by that physical complex.
5. Evaluate the H-linear trace or index with the actual pulled-back background.
6. Transport the same operator from `Y14` to K3, or pay the APS correction terms.
7. Only then compare the computed rank/index with `4` and `8`.

If every layer were supplied, the branch could decide Candidate A, Candidate B, or failure.
The existing repo supplies only the first raw layer and compact control arithmetic.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact missing proof object is the common physical domain and quotient:

```text
M_RS,H^src =
  source-selected right-H RS module or Hilbert completion
  equipped with gamma-trace maps, gauge/BRST data, connection,
  coefficient background, and compact/Y14/APS domain choice
```

On this same object the repo would need:

```text
Pi_RS^phys : M_RS,H^src -> M_RS,H^src
E_RS^eff   : M_RS,H^src -> M_RS,H^src
Tr_H       : finite-rank or Fredholm H-linear trace/index readout
```

with:

```text
(Pi_RS^phys)^2 = Pi_RS^phys
(E_RS^eff)^2 = E_RS^eff
Pi_RS^phys and E_RS^eff are H-linear
Pi_RS^phys E_RS^eff Pi_RS^phys is defined on M_RS,H^src
image(Pi_RS^phys) is the physical quotient or BRST cohomology
```

The repo currently has:

```text
Pi_RS^raw available as a raw complex gamma-trace projector
E_+ available as raw chirality in the Cl(4,0) model
```

but not:

```text
Pi_RS^phys
E_RS^eff
M_RS,H^src
physical quotient or BRST cohomology
H-linear trace certificate
source-selected F/ch2 background
same-operator Y14-to-K3 bridge
```

Because the common physical domain is missing, the obstruction occurs before the rank
calculation. The expression `rank_H(Pi_RS^phys E_RS^eff Pi_RS^phys)` is not a defined
physical quantity in the current repository.

## 5. What Would Change If The Obstruction Closed

Closing the first obstruction would make the rank question meaningful. It would not by
itself force rank `4` or rank `8`.

If a source-selected certificate proves:

```text
rank_H(E_RS^eff) = 4
ind_H(D_RS^phys) = 8
```

with quotient/BRST, H-trace, background, and same-operator bridge data supplied, then
Candidate A survives as a conditional three-generation comparison. It would still depend on
the separate spin-1/2 contribution, additivity, and readout normalization gates.

If a source-selected certificate proves:

```text
rank_H(E_RS^eff) = 8
ind_H(D_RS^phys) = 16
```

with the same gates closed, then Candidate B survives as a conditional four-generation
comparison. It would not be a failure of the rank gate; it would be a different compact-model
generation branch.

If the certificate proves a different H-rank or H-index, both Candidate A and Candidate B
fail or need reformulation.

If the certificate proves only a complex rank, a background-dependent formula, a compact K3
control index, or a raw projector rank, no generation branch is promoted.

If the certificate cannot define a source-selected physical quotient or BRST complex, the
current branch remains underdefined and OBJ-GEN stays open.

## 6. Rollback/Falsification Conditions

Rollback is required if any artifact or downstream claim does one of the following:

- claims rank `4` from `8 / Ahat(K3)` or another target division;
- claims rank `8` before constructing `Pi_RS^phys` and `E_RS^eff`;
- promotes raw rank `96_C`, raw H-halving, or a raw gamma-trace kernel to an effective APS
  coefficient rank;
- claims a physical RS rank while omitting the physical quotient, gauge fixing, or BRST
  complex;
- converts a complex rank or index to an H-rank or H-index without an H-linear trace
  certificate;
- assumes `F=C^16`, `rank_H(F)=8`, or `ch2(F)[K3]=0` for the physical background without
  source selection;
- treats compact K3 control arithmetic as physical GU evidence without a same-operator
  `Y14 -> K3` bridge or APS correction terms;
- promotes three generations before a source-derived physical RS rank;
- promotes four generations before a source-derived physical RS rank;
- selects a normalization after seeing whether it gives `4`, `8`, `24`, or `32`.

Falsification is stronger than rollback. The effective-rank branch would be falsified or
forced into reformulation if a complete source-selected certificate returns a stable H-rank
outside `{4, 8}`, if the physical quotient/BRST complex is provably non-elliptic, or if the
same-operator bridge cannot exist for the physical RS operator while K3 is still being used
as the physical readout.

## 7. Next Meaningful Computation

The next computation should be a certificate builder, not a new raw rank.

Minimum executable target:

```text
RS_EFFECTIVE_RANK_CERTIFICATE_BUILDER
```

It should emit a JSON object with these fields:

```json
{
  "source_operator": null,
  "target_inputs_seen": [],
  "raw_gamma_trace_projector": {
    "available": true,
    "field": "C",
    "rank_C_context": 96
  },
  "physical_or_BRST_quotient": {
    "available": false,
    "symbol_exact": false,
    "elliptic": null
  },
  "common_right_H_module": {
    "available": false,
    "connection_preserves_H": false
  },
  "effective_coefficient_bundle": {
    "available": false,
    "same_domain_as_physical_projector": false
  },
  "H_linear_trace": {
    "available": false,
    "complex_to_H_conversion_allowed": false
  },
  "source_selected_background": {
    "rank_C_F": 16,
    "ch2_F_K3": "required"
  },
  "same_operator_bridge": {
    "Y14_to_K3": false,
    "APS_eta_h_spectral_flow_end_terms": "required_if_APS"
  },
  "decision": "UNDERDEFINED_PHYSICAL_EFFECTIVE_RANK"
}
```

Decision rule:

```text
target input seen -> INVALID_TARGET_FED
raw projector only -> RAW_ONLY_NOT_PHYSICAL
no quotient/BRST -> MISSING_PHYSICAL_QUOTIENT
no E_RS^eff -> MISSING_EFFECTIVE_COEFFICIENT
no H trace -> COMPLEX_ONLY
no source background -> BACKGROUND_UNDERDEFINED
no same-operator bridge -> K3_CONTROL_ONLY
rank_H=4 after all gates -> CANDIDATE_A_SURVIVES_CONDITIONALLY
rank_H=8 after all gates -> CANDIDATE_B_SURVIVES_CONDITIONALLY
other rank after all gates -> CANDIDATES_A_AND_B_FAIL_OR_REFORMULATE
```

The first useful positive computation is therefore not a numeric rank. It is filling
`source_operator`, `physical_or_BRST_quotient`, and `common_right_H_module` with real data.
The first useful negative computation is proving that no such quotient can be elliptic and
H-linear under the current GU branch assumptions.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "RS_EFFECTIVE_RANK_CERTIFICATE",
  "version": "2026-06-24",
  "verdict": "UNDERDEFINED_PHYSICAL_EFFECTIVE_RANK_CERTIFICATE_MISSING",
  "current_decision": "UNDERDEFINED_NOT_RANK_4_NOT_RANK_8",
  "source_derived_physical_rank_available": false,
  "promotion_allowed_now": false,
  "three_generations_derived": false,
  "four_generations_derived": false,
  "generation_count_claim_status": "NOT_DERIVED",
  "rank_status": {
    "rank_4": {
      "status": "NOT_JUSTIFIED",
      "would_mean_if_source_derived": "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
      "current_reason": "No Pi_RS^phys/E_RS^eff/H-trace/background/bridge certificate exists."
    },
    "rank_8": {
      "status": "NOT_JUSTIFIED",
      "would_mean_if_source_derived": "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
      "current_reason": "No Pi_RS^phys/E_RS^eff/H-trace/background/bridge certificate exists."
    },
    "neither": {
      "status": "NOT_DECIDED",
      "reason": "No source-derived physical rank has been computed; raw 96_C is not a physical effective rank."
    },
    "physical_effective_rank": "UNDERDEFINED",
    "raw_rank_C_Pi_raw_E_plus_Pi_raw": 96,
    "raw_rank_status": "RAW_ONLY_NOT_EFFECTIVE_RANK"
  },
  "certificate_layers": {
    "raw_gamma_trace_projector": {
      "status": "ESTABLISHED_RAW_COMPLEX_ONLY",
      "object": "Pi_raw",
      "field": "C",
      "rank_context_C": 96,
      "may_promote_to_physical_rank": false
    },
    "physical_BRST_quotient": {
      "status": "MISSING",
      "required_for_physical_rank": true
    },
    "effective_coefficient_bundle": {
      "status": "MISSING",
      "required_object": "E_RS^eff"
    },
    "H_linear_trace": {
      "status": "MISSING",
      "complex_to_H_conversion_allowed": false
    },
    "source_selected_background": {
      "status": "UNDERDEFINED",
      "known_context": "rank_C(F)=16 in raw/control models",
      "missing": "source-selected F and ch2(F)[K3]"
    },
    "same_operator_Y14_to_K3_bridge": {
      "status": "UNDERDEFINED",
      "required_for_physical_promotion": true
    },
    "target_fed_route": {
      "status": "FORBIDDEN",
      "rollback_label": "INVALID_TARGET_DIVISION"
    }
  },
  "target_division_status": {
    "forbidden": true,
    "forbidden_formula": "rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2",
    "rollback_label": "INVALID_TARGET_DIVISION"
  },
  "first_exact_obstruction": "No common source-selected right-H physical module or BRST cohomology is defined on which Pi_RS^phys and E_RS^eff both act as H-linear idempotents and admit an H-linear trace.",
  "missing_proof_objects": [
    "M_RS,H^src_common_domain",
    "physical_or_BRST_quotient",
    "Pi_RS^phys",
    "E_RS^eff",
    "H_linear_trace_certificate",
    "source_selected_F_and_ch2_background",
    "same_operator_Y14_to_K3_or_APS_bridge",
    "target_quarantine_certificate"
  ],
  "candidate_implications": {
    "rank_4_if_source_derived": "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
    "rank_8_if_source_derived": "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
    "other_rank_if_source_derived": "CANDIDATES_A_AND_B_FAIL_OR_REQUIRE_REFORMULATION",
    "raw_rank_96C": "DOES_NOT_PROMOTE_EITHER_CANDIDATE"
  },
  "rollback_conditions": [
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_source_derived_physical_rank",
    "promotes_raw_rank_96C_to_effective_APS_rank",
    "omits_physical_quotient_or_BRST_while_claiming_physical_RS_rank",
    "converts_complex_rank_to_H_rank_without_H_linear_trace_certificate",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
    "claims_three_generations_before_source_derived_physical_RS_rank",
    "claims_four_generations_before_source_derived_physical_RS_rank",
    "selects_normalization_after_target_comparison"
  ],
  "next_meaningful_computation": "RS_EFFECTIVE_RANK_CERTIFICATE_BUILDER"
}
```
