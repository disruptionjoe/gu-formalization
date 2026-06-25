---
title: "Hourly 20260625 0301 Cycle 3 Finite Local QFT Extraction Map Spec"
date: "2026-06-25"
run: "hourly-20260625-0301"
cycle: 3
lane: 4
doc_type: finite_local_qft_extraction_map_spec
artifact_id: "FiniteLocalQFTExtractionMapSpec_V1"
verdict: "CONDITIONAL_RECONSTRUCTION_GRADE_SPEC_SOURCE_DERIVATION_UNDERDEFINED"
owned_path: "explorations/hourly-20260625-0301-cycle3-finite-local-qft-extraction-map-spec.md"
companion_audit: "tests/hourly_20260625_0301_cycle3_finite_local_qft_extraction_map_spec_audit.py"
---

# Hourly 20260625 0301 Cycle 3 Finite Local QFT Extraction Map Spec

## 1. Verdict

Verdict: **conditional**, with source derivation still **underdefined**.

This artifact constructs:

```text
FiniteLocalQFTExtractionMapSpec_V1
```

as a source-facing mathematical specification for the missing QFT object:

```text
P_fin^b: F_phys^b(O) -> K_b
```

The specification can be made **reconstruction-grade conditional** because the
manuscript supplies enough compatible source-side context to name an
observation context, candidate physical field source, pullback/naturality
requirements, and non-import gate. It cannot be promoted to a **source-derived
map** because the operation `P_fin^b`, the finite codomain `K_b`, and a
finite-stability proof are not emitted by the queried sources.

Decision:

```text
source_derived: false
reconstruction_grade_conditional: true
underdefined_without_new_object: true
accepted_receipt_count: 0
finite_qft_recovery_promoted: false
qft_targets_used_to_select_map: []
first_missing_object: SourceEmittedFiniteLocalExtractionOperatorWithFiniteCodomain_V1
```

This is a specification, not a receipt, proof, or recovery computation. It is
valid only as a target object for future source mining or reconstruction work.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the controlling discipline: GU should be
constructively reconstructed where possible, but no mathematical or physical
claim may be promoted through compatibility, optimism, or hidden target import.

`process/runbooks/five-lane-frontier-run.md` supplies the decision-grade lane
contract and verdict vocabulary. In particular, "compatible with" does not mean
"derived from", and "hosted by" does not mean "selected by".

`AuthorManuscriptQFTFiniteExtractionReceiptSearch_V1` supplies the immediate
input state: the 2021 manuscript has QFT-adjacent observation, pullback,
field-content, quantization, projection, and measurement context, but accepted
receipt count is zero for `P_fin^b: F_phys^b(O) -> K_b` or an equivalent finite
local extraction/projector rule.

`ManuscriptCriticalDisplayEquationIndex_V1` supplies page-level routing: raw
text extraction is adequate for locating source families but not for
identity-grade receipt closure. It does not promote any QFT finite projector.

`Hourly20260625_0301_Cycle2TransitionLedger_V1` promotes the Cycle 3 object
`FiniteLocalQFTExtractionMapSpec_V1` as the next QFT lane, with the question:
can a non-imported source-facing finite extraction specification be written
from manuscript-compatible data, or does QFT receipt work remain underdefined?

From `Geometric_UnityDraftApril1st2021.pdf`, the source-compatible inputs are:

| manuscript locator | source-compatible datum | role in this spec |
|---|---|---|
| p.16, Definition 3.1 | Observerse triples `(X^n, Y^d, {iota})`, local open sets `U_x`, local Riemannian embeddings, pullback metric, normal bundle. | Observation context `O`. |
| p.17, Definition 3.2 | Native fields on `X` or `Y`; invasive fields on `X` are pullbacks from `Y`; different observations pull back different quantized values. | Source-side pullback and observation dependence. |
| p.25-p.26 | Observation of `Y` from `X` via local section/pullback; pullback of bundles; splitting of `TY`; observation as generator of pullback data. | Naturality/pullback compatibility requirement. |
| p.31-p.33 | GU field content: `omega=(beta, chi)=((epsilon, varpi), (nu, zeta))`, table over `Omega^0_Y` and `Omega^1_Y`, `H`, `A`, `N`, and `G=H semidirect N`. | Candidate source field content before finite extraction. |
| p.49-p.50 | Observed field content begins by pulling back bundles and jets; `nu` and `zeta` host bundles are analyzed at zeroth order under observation. | Candidate `F_phys^b(O)` should be local and pullback-aware. |
| p.54 | Summary distinguishes finite-dimensional bundle structure from infinite-dimensional `H -> G -> A x A -> N` structures. | Confirms finite/infinite tension but not a map. |
| p.55-p.57 | Projections remove redundancy in Euler-Lagrange equations; `omega=(epsilon,varpi)` and gauge-covariant Shiab/projection context. | Projection context only; not accepted as `P_fin^b`. |
| p.56 | Connections have adequate quantization theory; metric field on `X` is separated from quantized structures on `Y`. | Quantization context for source space, not finite selection. |
| p.58-p.59 | Measurement analogy: states of `Y` are sampled and displayed on `X`; conventional Hilbert-space language appears only as comparison. | Measurement/readout context, not observable algebra extraction. |
| p.64 | Gravity on `X`, Standard Model fields native to `Y`, and localized gravity sections pull back different content. | Observation covariance/naturality pressure. |

Nothing in these sources directly defines `F_phys^b(O)`, `K_b`, or
`P_fin^b`. Those names remain specification fields, not source receipts.

## 3. The Strongest Positive Result

The strongest positive result is a precise non-import specification shell:

```text
FiniteLocalQFTExtractionMapSpec_V1 =
  (O, F_phys^b(O), P_fin^b, K_b, naturality, non_import, finite_stability)
```

where each field is either source-derived or explicitly reconstruction-labeled.

| field | candidate definition | evidence label | status |
|---|---|---|---|
| `O` | A local observation datum `O=(U subset X, iota_U: U -> Y, g_X=iota_U^*g_Y, N_iota)` in the Observerse sense. | source-derived from manuscript pp.16-17 and pp.25-26 | defined |
| `F_phys^b(O)` | Replacement label `F_GU,loc^b(O)`: local `O`-restricted/pullback-aware GU physical field data generated from `omega=(epsilon,varpi,nu,zeta)` on `Y`, together with any local jet/spray data needed before equations are evaluated. | reconstruction label using manuscript pp.31-33 and pp.49-50 | candidate only |
| `P_fin^b` | A finite extraction operation from `F_GU,loc^b(O)` to `K_b`; it must be a rule defined before QFT target comparison. | not source-derived | missing operation |
| `K_b` | A finite carrier/codomain indexed by `b`; it must carry dimension, representation/bundle dependence, and observation dependence if any. | not source-derived in this source pass | missing codomain |
| naturality/covariance | For observation refinements, changes of local section, pullbacks, and gauge transformations, `P_fin^b` must commute with the induced maps up to specified canonical isomorphism. | source-facing requirement from pullback/gauge context | required, unproved |
| non-import condition | No Gram matrix, CHSH/Bell target, `rho_AB`, desired finite recovery, target-fitted Hilbert state, or Pauli/control choice may select `P_fin^b`, `K_b`, or representatives. | repo guardrail and Cycle 2 target-import guard | defined |
| finite-stability test | A future candidate passes only if output dimension is finite, independent of irrelevant representative choices, stable under allowed pullback/gauge changes, and non-selected by QFT targets. | reconstruction audit criterion | specified, not passed |

The constructive value is that future work can no longer ask vaguely for a
"finite QFT projector." It must supply the missing operation and codomain while
passing the exact non-import and stability gates below.

### Candidate Specification

Let:

```text
O = (U, iota_U, g_X, N_iota)
```

where `U subset X` is a local open observation neighborhood and
`iota_U: U -> Y` is an Observerse local observation map.

Define a reconstruction-labeled source placeholder:

```text
F_GU,loc^b(O)
```

as the smallest local field-data object that contains:

```text
omega|_{Y_O} = (epsilon, varpi, nu, zeta)|_{Y_O}
```

and is compatible with:

```text
iota_U^*(bundles, fields, and required jets/sprays)
```

where `Y_O` denotes the portion of `Y` addressed by the observation `O`.
The superscript/index `b` is a bookkeeping label for the finite extraction
sector; it is not source-defined by the manuscript and must not be identified
with a target QFT basis unless a source object supplies that identification.

A valid future map must have the form:

```text
P_fin^b: F_GU,loc^b(O) -> K_b
```

with:

```text
dim(K_b) < infinity
```

and with `K_b` specified before any recovery calculation.

### Naturality/Covariance Rules

A candidate `P_fin^b` must provide at least the following commutative or
controlled-noncommutative diagrams:

| transformation | required rule |
|---|---|
| observation restriction `V subset U` | Restriction before extraction and extraction before restriction must agree through a named finite transition map `r^K_{UV}`. |
| change of observation section `iota_U -> iota'_U` | Pullback field transport induced by the observation change must be matched by a finite carrier transport `T^K_{iota,iota'}`. |
| gauge action by source-side `H` or `G` where defined | `P_fin^b(g . phi) = rho_b(g) P_fin^b(phi)` or a stated quotient/invariance rule, with `rho_b` source-defined. |
| representative or redundancy projection | If equations/projections remove redundancy, the kernel or quotient must be named before finite extraction is accepted. |
| local coordinate/frame change | Output must transform by the declared finite carrier action, not by target-fitted basis relabeling. |

These are required because the manuscript makes observation, pullback, native
versus invasive fields, gauge actions, and projection/redundancy central. The
manuscript does not prove the diagrams for `P_fin^b`.

### Non-Import Gate

The following are forbidden as inputs to selection:

```text
Gram
CHSH
Bell
rho_AB
desired finite recovery
standard Bell state
Pauli controls
target-fitted Hilbert factorization
ordinary QFT vacuum/state as source data
post hoc choice of K_b to match a recovery calculation
```

Allowed inputs are only source-facing GU data: observation/pullback structure,
native field content, gauge/connection structures, source-side projection or
quotient objects, and explicitly labeled reconstruction assumptions.

### Finite-Stability Test

A candidate future `P_fin^b` passes the finite-stability test only if all of the
following are shown without target import:

1. `K_b` is finite-dimensional or otherwise finite in the declared sense.
2. `P_fin^b(phi)` is defined for every admitted local field datum
   `phi in F_GU,loc^b(O)`.
3. Gauge-equivalent or projection-equivalent source representatives have the
   same finite output, or have outputs related by a declared finite action.
4. Observation restrictions and section changes satisfy the naturality rules.
5. The finite image is not chosen by Gram, CHSH, Bell, `rho_AB`, or desired
   finite recovery.
6. The test emits a falsifiable failure mode: dimension blow-up, undefined
   representative, noncommuting pullback square, gauge noncovariance, or target
   import.

Current status:

```text
finite_stability_test_specified: true
finite_stability_test_passed: false
reason_not_passed: P_fin^b and K_b are not source-emitted or constructed
```

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
SourceEmittedFiniteLocalExtractionOperatorWithFiniteCodomain_V1
```

Required shape:

```text
source: F_phys^b(O) or a source-defined replacement
operation: P_fin^b
codomain: K_b with finite structure
transport: finite maps implementing pullback/gauge/observer covariance
proof: finite-stability test passes without QFT target selection
```

The obstruction appears first at the operation/codomain pair. The manuscript
supports a local observation context and local field-content source, but no
source object selects finite representatives or a finite carrier. Without that
pair, the finite-stability test cannot be run.

This blocks source derivation, but not constructive reconstruction. A future
worker may propose `P_fin^b` and `K_b`, but the proposal must be labeled
reconstruction until a source locator or proof object supplies them.

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The next constructive object is:

```text
SourceEmittedOrReconstructedFiniteCarrierAndExtractionRule_V1
```

Minimum fields:

| field | required content |
|---|---|
| `source_locator_or_reconstruction_axiom` | Either a manuscript/source locator, or an explicit reconstruction axiom label. |
| `observation_context` | `O=(U,iota_U,g_X,N_iota)` or a stricter source-equivalent object. |
| `source_space` | `F_phys^b(O)` or replacement `F_GU,loc^b(O)` with admitted field and jet data. |
| `operation` | Exact rule for `P_fin^b`, including kernel, quotient, projection, cutoff, or representative selection. |
| `codomain` | Exact finite `K_b`, including dimension and representation/bundle dependence. |
| `transport_maps` | `r^K`, `T^K`, and gauge/coordinate actions or invariance rules. |
| `finite_stability_certificate` | A computation or proof of finite dimension, totality on admitted data, and stability under required transformations. |
| `non_import_audit` | Machine-checkable record that no QFT target selected the operation or codomain. |

The first useful pilot should be a one-sector, one-observation certificate:

```text
SingleObservationFiniteExtractionPilot_V1
```

It should choose one manuscript-compatible field sector, one local observation
window, and one candidate finite quotient/projection, then fail or pass the
finite-stability test without using QFT targets.

## 6. What This Means For The Relevant GU Claim

Allowed claim:

```text
The 2021 manuscript and current repo artifacts support a source-facing
specification for where a finite local QFT extraction map would have to live:
inside Observerse-local pullback-aware GU field data, with strict covariance
and non-import requirements.
```

Not allowed:

```text
GU derives finite local QFT extraction.
The manuscript supplies P_fin^b.
The manuscript defines K_b.
Finite QFT recovery is restarted.
Gram/CHSH/Bell/rho_AB recovery is evidence for choosing P_fin^b.
Finite stability is proved.
```

The relevant GU claim remains open but blocked at a sharper object. GU can host
the desired map only if a finite carrier and extraction rule are supplied from
source or from an explicitly labeled reconstruction axiom that passes the
finite-stability and non-import gates.

## 7. Next Meaningful Proof Or Computation Step

Build:

```text
SingleObservationFiniteExtractionPilot_V1
```

using one observation `O` and one source-compatible field sector from
`omega=(epsilon,varpi,nu,zeta)`. The pilot should try to define a finite
quotient/projection and finite carrier without target data, then run the
finite-stability test. The expected useful outcomes are:

```text
closed: a source locator emits P_fin^b and K_b;
conditional: a reconstruction axiom defines them and passes the stability test;
fail: the proposed operation is infinite, noncovariant, or undefined;
import: the proposed operation depends on QFT target data;
underdefined: no operation/codomain pair is specified.
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "FiniteLocalQFTExtractionMapSpec_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0301",
  "cycle": 3,
  "lane": 4,
  "verdict": "CONDITIONAL_RECONSTRUCTION_GRADE_SPEC_SOURCE_DERIVATION_UNDERDEFINED",
  "verdict_class": "conditional",
  "source_derived": false,
  "reconstruction_grade_conditional": true,
  "underdefined_without_new_object": true,
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0301-cycle3-finite-local-qft-extraction-map-spec.md",
    "companion_audit": "tests/hourly_20260625_0301_cycle3_finite_local_qft_extraction_map_spec_audit.py"
  },
  "source_basis": {
    "posture": "RESEARCH-POSTURE.md",
    "runbook": "process/runbooks/five-lane-frontier-run.md",
    "cycle2_qft_receipt": "explorations/hourly-20260625-0301-cycle2-manuscript-qft-finite-extraction-receipt.md",
    "cycle2_display_index": "explorations/hourly-20260625-0301-cycle2-manuscript-critical-display-equation-index.md",
    "cycle2_transition_ledger": "explorations/hourly-20260625-0301-cycle2-transition-ledger.json",
    "source_pdf": "Geometric_UnityDraftApril1st2021.pdf"
  },
  "accepted_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "finite_qft_recovery_promoted": false,
  "qft_proof_promotion_allowed": false,
  "spec_fields": {
    "observation_context": {
      "symbol": "O",
      "candidate": "O=(U subset X, iota_U: U -> Y, g_X=iota_U^*g_Y, N_iota)",
      "evidence_label": "source_derived",
      "source_locators": ["PDF p.16 Definition 3.1", "PDF p.17 Definition 3.2", "PDF p.25-p.26 observation via pullback"],
      "status": "defined"
    },
    "source_space": {
      "symbol": "F_GU,loc^b(O)",
      "replaces": "F_phys^b(O)",
      "candidate": "local pullback-aware GU field data from omega=(epsilon,varpi,nu,zeta) plus required local jets or sprays",
      "evidence_label": "reconstruction_label_from_source_context",
      "source_locators": ["PDF p.31-p.33 field content", "PDF p.49-p.50 observed field content"],
      "status": "candidate_only"
    },
    "operation": {
      "symbol": "P_fin^b",
      "candidate": "finite extraction/projector/quotient/local representative rule",
      "evidence_label": "not_source_derived",
      "source_locators": [],
      "status": "missing_operation"
    },
    "codomain": {
      "symbol": "K_b",
      "candidate": "finite carrier indexed by b with dimension and representation or bundle dependence specified before target comparison",
      "evidence_label": "not_source_derived",
      "source_locators": [],
      "status": "missing_codomain"
    },
    "naturality_covariance": {
      "required_rules": [
        "observation_restriction_commutes_with_finite_transition_map",
        "change_of_observation_section_matches_finite_carrier_transport",
        "gauge_action_is_equivariant_or_quotiented_by_source_defined_rule",
        "representative_redundancy_kernel_or_quotient_is_named_before_acceptance",
        "local_frame_change_acts_through_declared_finite_carrier_action"
      ],
      "evidence_label": "source_facing_requirement",
      "source_locators": ["PDF p.17 native_vs_invasive_fields", "PDF p.25-p.26 pullback and splitting", "PDF p.32-p.33 H A N G actions", "PDF p.55-p.57 projection and gauge covariance context"],
      "status": "required_unproved"
    },
    "non_import_condition": {
      "forbidden_selection_inputs": [
        "Gram",
        "CHSH",
        "Bell",
        "rho_AB",
        "desired_finite_recovery",
        "standard_Bell_state",
        "Pauli_controls",
        "target_fitted_Hilbert_factorization",
        "ordinary_QFT_vacuum_or_state_as_source_data",
        "post_hoc_choice_of_K_b_to_match_recovery"
      ],
      "qft_targets_used_to_select_map": [],
      "target_import_detected": false,
      "status": "defined"
    },
    "finite_stability_test": {
      "specified": true,
      "passed": false,
      "required_checks": [
        "K_b_is_finite",
        "P_fin_b_total_on_admitted_local_data",
        "gauge_or_projection_equivalent_representatives_have_declared_equal_or_transformed_outputs",
        "observation_restrictions_and_section_changes_satisfy_naturality",
        "finite_image_not_selected_by_forbidden_qft_targets",
        "falsifiable_failure_mode_emitted"
      ],
      "current_failure_reason": "P_fin^b_and_K_b_are_not_source_emitted_or_constructed",
      "status": "specified_not_passed"
    }
  },
  "strongest_positive_result": "A precise source-facing non-import specification shell can be written from Observerse pullback, field-content, quantization, projection, and measurement context.",
  "first_exact_obstruction": {
    "id": "SourceEmittedFiniteLocalExtractionOperatorWithFiniteCodomain_V1",
    "missing": true,
    "description": "No source-emitted operation P_fin^b and finite codomain K_b with transport maps and finite-stability proof are available."
  },
  "constructive_next_object": {
    "id": "SourceEmittedOrReconstructedFiniteCarrierAndExtractionRule_V1",
    "pilot": "SingleObservationFiniteExtractionPilot_V1",
    "required_fields": [
      "source_locator_or_reconstruction_axiom",
      "observation_context",
      "source_space",
      "operation",
      "codomain",
      "transport_maps",
      "finite_stability_certificate",
      "non_import_audit"
    ]
  },
  "impact_on_GU_claim": "GU_QFT_finite_extraction_branch_open_but_blocked_at_operation_and_codomain",
  "no_claim_promotions": {
    "GU_derives_finite_local_QFT_extraction": false,
    "manuscript_supplies_P_fin_b": false,
    "manuscript_defines_K_b": false,
    "finite_QFT_recovery_restarted": false,
    "Gram_CHSH_Bell_rho_AB_selects_map": false,
    "finite_stability_proved": false,
    "QFT_proof_promoted": false
  },
  "next_meaningful_step": "Build SingleObservationFiniteExtractionPilot_V1 and run finite-stability plus non-import checks."
}
```
