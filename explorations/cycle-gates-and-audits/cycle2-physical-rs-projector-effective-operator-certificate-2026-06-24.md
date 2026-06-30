---
title: "Cycle 2 Physical RS Projector and Effective Operator Certificate"
date: "2026-06-24"
status: exploration
doc_type: frontier_run_artifact
verdict: "UNDERDEFINED_CERTIFICATE_MISSING"
owned_path: "explorations/cycle-gates-and-audits/cycle2-physical-rs-projector-effective-operator-certificate-2026-06-24.md"
audit:
  - "tests/cycle2_physical_rs_projector_effective_operator_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/cycle1-generation-rs-rank-direct-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/mission-a-generation-count-analytic-machinery-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-clifford-projector-computation-2026-06-24.md"
  - "explorations/generation-sector/y14-k3-bridge-loss-ledger-2026-06-24.md"
  - "tests/rs_clifford_projector_model.py"
---

# Cycle 2 Physical RS Projector and Effective Operator Certificate

## 1. Verdict

**Verdict: underdefined certificate missing.**

The current repository does not yet supply enough structure to compute a physical/effective
Rarita-Schwinger rank `4` or `8`. It supplies explicit raw complex `Cl(4,0)`
gamma-trace projectors and the raw composite

```text
Pi_raw E_+ Pi_raw
```

with complex rank `96`. That is a valid finite matrix computation, but it is not a
physical RS quotient, not a BRST cohomology projector, not an H-linear trace computation,
not a background-dependent `F/ch2` index, and not a same-operator `Y^14 -> K3` transport.

The missing object is a certificate:

```text
C_RS^phys-eff =
  (source_operator,
   M_RS,H^src,
   BRST_or_physical_quotient,
   Pi_RS^phys,
   E_RS^eff,
   Tr_H,
   F_and_ch2,
   K3_Y14_same_operator_bridge,
   rollback_guard)
```

on one common source-selected right-H module. Until that certificate exists, the effective
rank is not merely unknown; the expression whose rank is being requested is not uniquely
typed.

Current decision:

```text
raw_rank_C(Pi_raw E_+ Pi_raw) = 96
raw_rank_96_status = RAW_ONLY_NOT_EFFECTIVE_RANK
rank_H(E_RS^eff) = UNDERDEFINED
three_generation_claim = NOT_DERIVED
four_generation_branch = OPEN_NOT_DERIVED
```

No current repo object supplies the physical/effective certificate. The correct status is
therefore:

```text
UNDERDEFINED_CERTIFICATE_MISSING
```

## 2. Raw Projector Result And Why It Is Insufficient

Cycle 1 and `tests/rs_clifford_projector_model.py` provide a concrete raw calculation. In the
pulled-back complex `Cl(4,0)` model:

```text
S_4^+ = C^2
S_4^- = C^2
F = C^16
V_+ = C^4 tensor S_4^+ tensor F = C^128
V_- = C^4 tensor S_4^- tensor F = C^128
G_+ : V_+ -> S_4^- tensor F = C^32
G_- : V_- -> S_4^+ tensor F = C^32
```

The raw gamma-trace kernels have complex rank:

```text
rank_C(ker G_+) = 96
rank_C(ker G_-) = 96
```

Equivalently, using the full vector-spinor chirality projection:

```text
G_full = [gamma_1 gamma_2 gamma_3 gamma_4] tensor I_16
Pi_raw = orthogonal projector onto ker(G_full)
E_+ = I_vector tensor chiral_projector_+ tensor I_16

domain_dim_C = 256
rank_C(G_full) = 64
rank_C(Pi_raw) = 192
rank_C(E_+) = 128
rank_C(Pi_raw E_+ Pi_raw) = 96
```

This raw result is insufficient for six separate reasons.

1. `Pi_raw` is the orthogonal gamma-trace kernel projector. It is not
   `Pi_RS^phys`.
2. `E_+` is raw four-dimensional spinor chirality. It is not `E_RS^eff`.
3. The projected gauge image is not quotiented away by the raw model; Cycle 1 reports a
   projected gauge image of rank `32_C` and a nonzero raw symbol on it.
4. The rank is complex. No global right-H structure, H-linear projectors, or H-linear trace
   is certified for this physical branch.
5. The coefficient `F=C^16` is only the bookkeeping rank of the internal bundle. The physical
   background `F=s^*S(6,4)` and `ch_2(F)[K3]` are not fixed.
6. The K3 calculation is compact control data. It is not yet transported from the same
   noncompact `Y^14` physical operator, nor corrected by APS eta, kernel, spectral-flow, and
   end terms.

Therefore `96_C` is a raw sanity result only. It cannot be halved, normalized, divided, or
quotiented into `4` or `8` without additional proof objects.

## 3. Certificate Definition For `Pi_RS^phys` And `E_RS^eff`

The certificate must be typed before any rank is meaningful. A minimal acceptable definition
is the following.

```text
C_RS^phys-eff.source_operator =
  D_GU | D_roll | explicitly branched comparison operator
```

This field must specify where the RS sector comes from. A comparison operator is allowed only
if it is labeled as comparison, not as a source-derived GU result.

```text
C_RS^phys-eff.M_RS,H^src =
  one source-selected right-H module or Hilbert completion
  on which Pi_RS^phys, E_RS^eff, the physical operator, and the trace all act
```

The common module cannot be inferred from the raw complex fiber alone. It must include the
bundle, right-H action, connection/domain, coefficient background, and whether the problem is
compact K3, projected weighted `Y^14`, or an APS compactification.

The physical projector must then be an H-linear idempotent on this same module:

```text
Pi_RS^phys : M_RS,H^src -> M_RS,H^src
Pi_RS^phys^2 = Pi_RS^phys
Pi_RS^phys is H-linear
image(Pi_RS^phys) = physical RS degree-zero states
```

`image(Pi_RS^phys)` must be one of:

```text
gauge-fixed representatives of the physical quotient
BRST harmonic representatives
degree-zero cohomology of an elliptic RS complex
the finite projected tau-discrete physical sector, if the Y^14 route is used
```

It is not enough to require gamma-trace-freeness. The certificate must also encode the gauge
map, gauge-fixing condition or ghost complex, and symbol-level exactness/ellipticity.

The effective operator must be an H-linear finite-rank/K-theory idempotent on the same module:

```text
E_RS^eff : M_RS,H^src -> M_RS,H^src
E_RS^eff^2 = E_RS^eff
E_RS^eff is H-linear
E_RS^eff Pi_RS^phys = Pi_RS^phys E_RS^eff = E_RS^eff
rank_H(E_RS^eff) = Tr_H(E_RS^eff), only after Tr_H is certified
```

Equivalently, the certificate may replace `E_RS^eff` by a fully specified K-theory symbol or
elliptic-complex class whose degree-zero and degree-four Chern character components are
computed. But in that case the artifact must state that it is computing an index class, not a
fiberwise projector rank.

The direct rank expression becomes well-typed only after this data exists:

```text
rank_H(Pi_RS^phys E_RS^eff Pi_RS^phys)
```

on the common `M_RS,H^src`. The current repository does not define that expression.

## 4. Required Quotient/BRST, H-Trace, Background, And Bridge Data

The physical quotient/BRST data must include:

| field | required content | current status |
|---|---|---|
| `G_+, G_-` | gamma-trace maps with conventions and adjoints | raw maps computed only |
| `gauge_symbol` | principal gauge map, such as `epsilon -> xi tensor epsilon` | raw sample checked; not quotiented |
| `gauge_condition` | gauge-fixing condition producing an elliptic operator | missing |
| `BRST_complex` | ghost/antighost/subtraction complex, signs, degrees, and cohomology | missing |
| `symbol_exactness` | proof for nonzero covectors, or failure certificate | missing |
| `physical_cohomology` | identified degree-zero physical RS states | missing |
| `Pi_RS^phys` | H-linear projector to those states | missing |

The H-linear trace data must include:

```text
right_H_action J or equivalent right-H module structure
J^2 = -1 in the complex presentation
all gamma, gauge, ghost, projector, operator, and bridge maps commute with right H
connection preserves the right-H structure
Tr_C(A) = 2 Tr_H(A) only for certified H-linear finite-rank A
index_C = 2 index_H only for certified H-linear Fredholm operators
```

Without this field, the raw complex number `96` remains `96_C`. The naive value `48_H` is not
a proof object, and neither `4` nor `8` follows from it.

The background data must include:

```text
F = s^*S(6,4) or the explicitly branched comparison coefficient bundle
rank_C(F) = 16
rank_H(F) = 8, only if the H-certificate covers F
k = ch_2(F)[K3]
connection and curvature conventions for F
proof that k is fixed, symbolic, or irrelevant to the computed index
```

If `k=0` is used, the certificate must prove flatness/triviality for the actual physical
background. It cannot be imported because it makes the arithmetic convenient.

The K3/Y14 bridge data must be same-operator data:

```text
same physical RS complex on both sides
same right-H structure
same F background and ch_2(F)
same symbol class or a proved compact homotopy
same boundary operator if APS is used
```

The bridge may take either of two shapes.

```text
Unitary discrete-sector bridge:
  U : L^2_H(K3, E_RS^phys) -> P_disc L^2_H(Y^14, E_RS^phys)
  U^{-1} P_disc D_RS^Y P_disc U = D_RS^K3 + compact homotopy
```

or:

```text
APS bridge:
  Ind_Y_RS =
    bulk_K3_like_index
    - (eta(A_RS^phys) + h(A_RS^phys))/2
    + SF_bridge
    + C_end
```

The current bridge ledger classifies this data as underdefined. Compact K3 arithmetic is
therefore control-only until a same-operator bridge closes.

## 5. Branch Outcomes If Rank 4 Or Rank 8 Later Closes

The comparison values remain useful, but only after the certificate computes the effective
rank/index independently.

If a future source-selected certificate proves:

```text
rank_H(E_RS^eff) = 4
Ind_H(D_RS^phys) = 8
```

after quotient/BRST, H-trace, background, and bridge corrections are included, then Candidate
A survives. Conditional on the separate spin-1/2 contribution and additivity gates, the total
would be:

```text
16 + 8 = 24
```

which matches a three-generation readout. That future outcome would not validate any earlier
target-fed derivation of `4`; it would supersede it by an independent certificate.

If a future source-selected certificate proves:

```text
rank_H(E_RS^eff) = 8
Ind_H(D_RS^phys) = 16
```

with all corrections paid, then Candidate B survives. Conditional on the same additivity
normalization, the total would be:

```text
16 + 16 = 32
```

which is a four-generation compact-model branch, not a three-generation result.

If the certificate returns any other H-index, both Candidate A and Candidate B fail or must be
reformulated. If it returns only a complex index, a background-dependent expression, or a K3
control index with no same-operator bridge, then no generation-count branch is promoted.

Rollback condition for both branches:

```text
rank_H(E_RS^eff) = Ind_H(D_RS)/Ahat(K3)
```

is invalid if `Ind_H(D_RS)` was itself inserted from the desired generation count. The label
for that failure is `INVALID_TARGET_DIVISION`.

## 6. First Exact Obstruction

The first exact obstruction is the missing common typed domain:

```text
M_RS,H^src
```

The repo has raw complex fibers and raw projectors, but it does not yet define a
source-selected right-H physical module or BRST cohomology on which both

```text
Pi_RS^phys
E_RS^eff
```

act as H-linear idempotents. Because the common domain is missing, `Pi_RS^phys E_RS^eff
Pi_RS^phys` is not a defined physical operator. The obstruction appears before any rank
calculation.

The shortest obstruction statement is:

```text
Pi_RS^raw exists; Pi_RS^phys and E_RS^eff on a common source-selected right-H module do not.
```

## 7. Impact For Generation-Count Claims

The impact is restrictive but informative.

No positive three-generation claim follows from the current repo objects. The current raw
rank `96_C` is not promoted to an effective rank, an H-index, or a generation count. The
K3 raw and BRST-style formulas remain compact control data unless a physical source operator
and same-operator bridge are supplied.

Allowed current statement:

```text
The raw Cl(4,0) projector computation gives rank_C(Pi_raw E_+ Pi_raw)=96.
The physical/effective RS rank remains underdefined because Pi_RS^phys,
E_RS^eff, quotient/BRST data, H-linear trace, F/ch2, and the K3/Y14 bridge
are not yet certified on one source-selected right-H module.
```

Forbidden current statements:

```text
a source-derived effective H-rank 4 certificate already exists.
a source-derived effective H-rank 8 certificate already exists.
the three-generation branch is closed.
raw rank 96 reduces to the effective APS rank.
K3 control arithmetic is physical GU generation-count evidence.
```

This does not kill the Mission A branch. It says exactly what mathematical object would have
to exist if the branch is correct, and it prevents the raw calculation from being mistaken for
the physical certificate.

## 8. Next Meaningful Computation

The next computation should be a certificate builder, not another raw projector rank. A useful
executable target would serialize the following object:

```json
{
  "certificate": "RS_PHYS_EFFECTIVE_OPERATOR_CERTIFICATE",
  "source_operator": null,
  "common_right_H_module": {
    "provided": false,
    "compact_or_y14_or_aps": null
  },
  "Pi_RS": {
    "raw_gamma_trace_projector_available": true,
    "physical_projector_available": false,
    "quotient_or_BRST_available": false
  },
  "E_RS_eff": {
    "available": false,
    "same_domain_as_Pi_RS_phys": false,
    "h_linear_idempotent": false
  },
  "H_trace": {
    "right_H_structure_verified": false,
    "H_linear_trace_available": false
  },
  "background": {
    "rank_C_F": 16,
    "ch2_F_K3": "required"
  },
  "bridge": {
    "same_operator_K3_Y14_bridge": false,
    "APS_eta_h_spectral_flow_end_terms": "required_if_APS"
  },
  "decision": "UNDERDEFINED_CERTIFICATE_MISSING"
}
```

The first successful advance would fill `source_operator`, `common_right_H_module`, and
`quotient_or_BRST_available` with real data. The first decisive negative advance would prove
that no source-selected quotient/BRST complex can be elliptic or H-linear under the stated
branch assumptions.

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE2_PHYSICAL_RS_PROJECTOR_EFFECTIVE_OPERATOR_CERTIFICATE",
  "version": "2026-06-24",
  "verdict": "UNDERDEFINED_CERTIFICATE_MISSING",
  "current_decision": "NO_CURRENT_REPO_OBJECT_COMPUTES_EFFECTIVE_RS_RANK",
  "positive_three_generation_claim": false,
  "three_generations_derived": false,
  "generation_count_claim_status": "NOT_DERIVED",
  "promotion_allowed_now": false,
  "raw_projector_result": {
    "computed_object": "Pi_raw E_+ Pi_raw",
    "field": "C",
    "rank": 96,
    "status": "RAW_ONLY_NOT_EFFECTIVE_RANK",
    "promoted_to_effective_rank": false,
    "promoted_to_generation_claim": false
  },
  "rank_status": {
    "rank_H_E_RS_eff_4": "NOT_JUSTIFIED",
    "rank_H_E_RS_eff_8": "NOT_JUSTIFIED",
    "physical_effective_rank": "UNDERDEFINED",
    "raw_rank_C_Pi_raw_E_plus_Pi_raw": 96
  },
  "required_certificate": {
    "source_operator": "missing",
    "common_right_H_module": "missing",
    "Pi_RS_phys": "missing",
    "E_RS_eff": "missing",
    "quotient_or_BRST": "missing",
    "H_linear_trace": "missing",
    "F_ch2_background": "missing",
    "K3_Y14_same_operator_bridge": "missing"
  },
  "current_repo_objects": {
    "Pi_RS_raw": "available_as_raw_complex_gamma_trace_projector",
    "raw_projector_rank": "available_complex_rank_96",
    "symbol_index_contract": "specified_skeleton_not_physical_certificate",
    "K3_control_formulas": "available_control_only",
    "Y14_K3_bridge": "underdefined"
  },
  "first_exact_obstruction": "No common source-selected right-H physical module or BRST cohomology is defined on which Pi_RS^phys and E_RS^eff both act as H-linear idempotents.",
  "branch_outcomes": {
    "if_rank_H_E_RS_eff_4_and_index_H_8_close": "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
    "if_rank_H_E_RS_eff_8_and_index_H_16_close": "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
    "if_other_rank_closes": "CANDIDATES_A_AND_B_FAIL_OR_REQUIRE_REFORMULATION",
    "if_complex_only_or_background_dependent": "NO_GENERATION_COUNT_PROMOTION",
    "if_bridge_missing": "K3_CONTROL_ONLY"
  },
  "rollback_conditions": [
    "claims_three_generations_before_source_derived_RS_rank",
    "promotes_raw_rank_96C_to_effective_APS_rank",
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_Pi_RS_phys_and_E_RS_eff_certificate",
    "omits_quotient_or_BRST_while_claiming_physical_RS_rank",
    "converts_complex_rank_to_H_rank_without_H_linear_trace",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections"
  ],
  "rollback_label_for_target_division": "INVALID_TARGET_DIVISION",
  "next_meaningful_computation": "RS_PHYS_EFFECTIVE_OPERATOR_CERTIFICATE_BUILDER"
}
```
