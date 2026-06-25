---
title: "Cycle 1 Generation RS Rank Direct Gate"
date: "2026-06-24"
status: exploration
doc_type: frontier_run_artifact
verdict: "UNDERDEFINED_RAW_DIRECT_RANK_NOT_CANDIDATE"
owned_path: "explorations/cycle1-generation-rs-rank-direct-gate-2026-06-24.md"
audit:
  - "tests/cycle1_generation_rs_rank_direct_gate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "roadmap/objection-triage-register.md"
  - "explorations/mission-a-generation-count-analytic-machinery-2026-06-24.md"
  - "explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md"
  - "explorations/generation-count-rs-rank-gate-2026-06-24.md"
  - "tests/rs_clifford_projector_model.py"
  - "tests/rs_k3_symbol_index_formula_audit.py"
---

# Cycle 1 Generation RS Rank Direct Gate

## 1. Verdict

**Verdict: underdefined for the physical direct rank gate.**

The current repository does not compute a source-derived rank `4` or rank `8` for

```text
Pi_RS * E_+ * Pi_RS
```

in the needed physical quaternionic/Clifford model. The existing executable code computes
raw complex `Cl(4,0)` gamma-trace projectors and a sampled raw projected RS symbol. Those
are real checks, but they do not define the physical/effective APS coefficient projector.

The closest direct raw calculation that can be assembled from the existing code is:

```text
Pi_raw = orthogonal projector onto ker([gamma_1 ... gamma_4] tensor I_16)
E_+    = I_vector tensor chiral_projector_+ tensor I_16
rank_C(Pi_raw E_+ Pi_raw) = 96
```

If one naively halves this complex rank after a compatible right-H structure were supplied,
the number would be `48`, not `4` or `8`. That halving is not itself certified by the code.

Therefore:

```text
rank 4: not justified by current machinery
rank 8: not justified by current machinery
three-generation candidate: not promoted
four-generation candidate: not promoted, still undismissed
current gate: UNDERDEFINED_RAW_DIRECT_RANK_NOT_CANDIDATE
```

Rollback condition: any claim that obtains `rank_H=4` by writing
`rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2` is target-fed and must be marked
`INVALID_TARGET_DIVISION`.

## 2. What Existing Computation/Tests Actually Establish

The requested sources establish the following, and no more.

`roadmap/objection-triage-register.md` identifies OBJ-GEN as the load-bearing weak point.
Its decisive first test is a direct Clifford-algebra rank computation returning `4` or `8`
without dividing by the desired RS index.

`explorations/generation-count-rs-rank-gate-2026-06-24.md` records why the old OQ-RK1/OQ-RK2
route does not close the gate. It says the surviving APS expression consumed
`rank_H(S_RS^+)=4` as a physical-DOF or reverse-engineered input. The direct rank object must
therefore be computed before comparison with `ind_H(D_RS)=8`.

`explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md` and
`tests/rs_clifford_projector_model.py` compute an explicit complex `Cl(4,0)` model:

```text
S_4^+ = C^2
S_4^- = C^2
F = C^16
V_+ = C^4 tensor S_4^+ tensor F = C^128
V_- = C^4 tensor S_4^- tensor F = C^128
G_+ : V_+ -> S_4^- tensor F = C^32
G_- : V_- -> S_4^+ tensor F = C^32
```

The code verifies:

```text
rank_C(ker G_+) = 96
rank_C(ker G_-) = 96
P_+^2 = P_+
P_-^2 = P_-
G_+ P_+ = 0
G_- P_- = 0
```

For the sampled covector `xi=(1,2,3,4)`, the restricted raw projected symbol has
`rank_C=96`. The projected principal gauge image has `rank_C=32`, and the raw symbol is
nonzero on it. Thus the raw gamma-trace projector is not already a physical gauge quotient.

`tests/rs_k3_symbol_index_formula_audit.py` checks characteristic-class arithmetic only. In
the flat `F=C^16` branch it gives:

```text
full vector-spinor q=0:        ind_C = -640, ind_H = -320 if H-linear
raw gamma-trace-free q=1:      ind_C = -608, ind_H = -304 if H-linear
BRST-style q=-1 if derived:    ind_C = -672, ind_H = -336 if H-linear
spinor coefficient:            ind_C =   32, ind_H =   16 if H-linear
```

These are compact K3 control formulas. None is a source-derived RS contribution `8`, and none
selects an effective rank `4` or `8`.

## 3. Direct-Rank Calculation Attempt Or Why The Physical One Is Not Yet Well-Defined

The nearest well-typed raw calculation is a full complex 4D vector-spinor calculation, using
the same functions already present in `tests/rs_clifford_projector_model.py`.

Define:

```text
G_full = [gamma_1 gamma_2 gamma_3 gamma_4] tensor I_16 :
  C^4_vector tensor C^4_spinor tensor C^16 -> C^4_spinor tensor C^16

Pi_raw = I - G_full^* (G_full G_full^*)^{-1} G_full

E_+ = I_4_vector tensor (1 + chirality_4)/2 tensor I_16
```

Then:

```text
domain dimension_C = 4 * 4 * 16 = 256
rank_C(G_full) = 64
rank_C(Pi_raw) = 192
rank_C(E_+) = 128
rank_C(Pi_raw E_+ Pi_raw) = 96
```

This agrees with the chiral raw gamma-trace kernel rank already reported by the existing
model. It is a useful sanity check: the raw direct projector composite is not mysterious,
and it does not return `4` or `8`.

But this calculation is not the desired physical direct rank, for five reasons.

1. `Pi_raw` is the orthogonal gamma-trace kernel projector. It is not a gauge-fixed or BRST
   physical RS projector.
2. `E_+` is the 4D spinor chirality projector in the raw complex model. The effective APS
   coefficient `E_RS^eff` has not been constructed.
3. The rank is complex. The code does not certify a global right-H structure, H-linear trace,
   or H-compatible connection for the relevant K3/background branch.
4. The internal field `F=C^16` is inserted as a coefficient module. The actual
   source-selected Sp(64) background and `ch_2(F)[K3]` are still open.
5. The calculation is local/fiberwise. It does not provide the same-operator `Y^14 -> K3`
   bridge or APS correction theorem needed to interpret a K3 compact control rank as the GU
   physical RS index.

So the direct raw object is well-defined and returns `96_C`. The direct physical/effective
object required by OBJ-GEN is not yet well-defined.

## 4. Whether Rank 4, Rank 8, Neither, Or Underdefined Is Currently Justified

The current justified statuses are:

| rank/status | currently justified? | reason |
|---|---:|---|
| raw complex rank `96` | yes | computed by the existing `Cl(4,0)` projector model and by the reconstructed raw composite `Pi_raw E_+ Pi_raw` |
| naive raw H-rank `48` | not as a proof | only follows after an H-structure conversion that this code does not certify |
| effective H-rank `4` | no | previous appearances divide the desired RS index `8` by `Ahat(K3)=2` or use physical DOF input |
| effective H-rank `8` | no | live Candidate B comparison, but not computed by the current code |
| physical direct rank of `Pi_RS E_+ Pi_RS` | underdefined | the physical projector/quotient, H-linear trace, background, and bridge are not specified |

Thus the correct proof-contract answer is:

```text
neither rank 4 nor rank 8 is currently justified;
the requested physical direct-rank gate is underdefined;
the raw computable proxy returns 96_C, not a candidate effective rank.
```

## 5. First Exact Obstruction Or Missing Proof Object

The first exact missing proof object is:

```text
Pi_RS^phys :
  source-selected right-H K3 vector-spinor data
  -> physical/effective RS coefficient data
```

This is not the raw gamma-trace projector, which already exists. It must include:

```text
source_operator:
  D_GU, D_roll, or an explicitly branched comparison operator

common_domain:
  the right-H module on which Pi_RS, E_+, and Pi_RS E_+ Pi_RS all act

physical_quotient_or_BRST_complex:
  gamma-trace constraint, gauge map, gauge fixing, ghosts/subtractions,
  and symbol-level exactness/ellipticity

effective_coefficient_bundle:
  E_RS^eff or an equivalent K-theory symbol class whose rank/Chern character is computed

H_linear_trace_certificate:
  right-H structure, H-linear projectors, H-compatible connection,
  and legitimate complex-to-H rank/index conversion

source_selected_background:
  the actual F=s^*S(6,4) or Sp(64) background, including ch_2(F)[K3]

K3_or_Y14_bridge:
  same-operator unitary discrete-sector bridge or APS theorem with eta, h,
  spectral flow, and end corrections
```

The shortest obstruction statement is:

```text
The repo has Pi_RS^raw, but not Pi_RS^phys/E_RS^eff.
```

Without `Pi_RS^phys` and `E_RS^eff`, the expression `Pi_RS * E_+ * Pi_RS` has no unique
physical rank. Different well-typed raw interpretations give raw ranks such as `96_C`, while
the desired `4` arises only after target division.

## 6. Implication For Three-Generation And Four-Generation Candidates

Candidate A:

```text
rank_H(E_RS^eff)=4
ind_H(D_RS)=2*4=8
ind_H(D_GU)=16+8=24
three SM generations
```

Status: **open, not derived**. The current code does not promote Candidate A. Any statement
that Candidate A is derived from the direct rank gate must be rolled back unless the physical
projector/effective coefficient object is supplied and ranked without using `8/Ahat(K3)`.

Candidate B:

```text
rank_H(E_RS^eff)=8
ind_H(D_RS)=2*8=16
ind_H(D_GU)=16+16=32
four-generation compact-model branch
```

Status: **open, not derived**. Candidate B remains undismissed because no source-derived
calculation has selected Candidate A. The raw rank `96_C` does not promote Candidate B either;
it shows that the raw projector object is not the effective APS rank object.

If the eventual source-selected physical rank is `4`, Candidate A survives. If it is `8`,
Candidate B survives. If it is another value, both candidate readouts fail or must be
reformulated. If the physical object remains undefinable, OBJ-GEN stays blocked at the
proof-contract level.

## 7. Next Meaningful Computation

The next computation should not ask the raw projector model for another rank. It should
construct a certificate that separates raw, physical, and target-fed objects.

Minimum executable target:

```text
tests/rs_effective_rank_certificate.py
```

Required fields:

```json
{
  "computed_object": "raw|gauge_fixed|brst_complex|effective_coefficient",
  "target_inputs_seen": [],
  "domain": "explicit right-H module",
  "Pi_RS": {
    "raw_gamma_trace_projector": true,
    "physical_projector": false,
    "gauge_quotient_or_BRST": false
  },
  "E_plus": {
    "chirality_projector": true,
    "effective_coefficient_projector": false
  },
  "rank": {
    "field": "C|H",
    "value": null,
    "h_trace_certificate": false
  },
  "background": {
    "rank_C_F": 16,
    "ch2_F_K3": "required"
  },
  "bridge": {
    "same_operator_Y14_to_K3": false,
    "APS_eta_h_spectral_flow_accounted": false
  },
  "decision": "RAW_ONLY_OR_UNDERDEFINED"
}
```

Decision rule:

```text
target input seen                         -> INVALID_TARGET_DIVISION
raw Pi_RS only                            -> RAW_RANK_ONLY
no physical quotient/BRST                 -> MISSING_PHYSICAL_QUOTIENT
no H-linear trace                         -> COMPLEX_ONLY
no source-selected F/ch2                  -> BACKGROUND_UNDERDEFINED
no same-operator bridge                   -> K3_CONTROL_ONLY
rank_H=4 after all gates                  -> CANDIDATE_A_SURVIVES
rank_H=8 after all gates                  -> CANDIDATE_B_SURVIVES
other rank after all gates                -> BOTH_CANDIDATES_FAIL_OR_REFORMULATE
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE1_GENERATION_RS_RANK_DIRECT_GATE",
  "version": "2026-06-24",
  "verdict": "UNDERDEFINED_RAW_DIRECT_RANK_NOT_CANDIDATE",
  "positive_three_generation_claim": false,
  "three_generations_derived": false,
  "generation_count_claim_status": "NOT_DERIVED",
  "current_decision": "NO_SOURCE_DERIVED_RANK_4_OR_8",
  "rank_status": {
    "rank_4": "NOT_JUSTIFIED",
    "rank_8": "NOT_JUSTIFIED",
    "raw_rank_C_Pi_raw_E_plus_Pi_raw": 96,
    "raw_naive_rank_H_if_halvable": 48,
    "physical_effective_rank": "UNDERDEFINED"
  },
  "existing_code_establishes": [
    "raw_complex_Cl4_gamma_trace_projectors",
    "raw_projector_idempotence_and_gamma_trace_kernel",
    "sample_raw_projected_symbol_rank_C_96",
    "projected_gauge_image_not_quotiented",
    "K3_characteristic_class_control_arithmetic"
  ],
  "target_division_status": {
    "forbidden": true,
    "forbidden_formula": "rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2",
    "rollback_label": "INVALID_TARGET_DIVISION"
  },
  "missing_objects": [
    "Pi_RS^phys_or_effective_RS_projector",
    "physical_DOF_quotient_or_BRST_complex",
    "effective_coefficient_bundle_E_RS_eff",
    "H_linear_trace_certificate",
    "source_selected_background_F_and_ch2",
    "same_operator_Y14_to_K3_or_APS_bridge"
  ],
  "first_exact_obstruction": "The repo has Pi_RS^raw but not a source-selected physical/effective projector Pi_RS^phys or E_RS^eff on a common right-H module.",
  "candidate_implications": {
    "candidate_A_three_generations": "OPEN_NOT_DERIVED",
    "candidate_B_four_generations": "OPEN_NOT_DERIVED",
    "raw_rank_96C": "DOES_NOT_PROMOTE_EITHER_CANDIDATE"
  },
  "rollback_conditions": [
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_three_generations_before_source_derived_RS_rank",
    "labels_raw_gamma_trace_rank_as_effective_APS_rank",
    "omits_physical_quotient_or_BRST_while_claiming_physical_RS_rank",
    "converts_complex_rank_to_H_rank_without_H_linear_trace_certificate",
    "assumes_flat_or_trivial_background_without_source_selected_ch2",
    "uses_compact_K3_control_without_same_operator_bridge_or_APS_corrections"
  ],
  "next_meaningful_computation": "RS_EFFECTIVE_RANK_CERTIFICATE_WITH_RAW_PHYSICAL_TARGET_SEPARATION"
}
```
