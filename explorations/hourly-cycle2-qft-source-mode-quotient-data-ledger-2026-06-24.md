---
title: "Hourly Cycle 2 QFT Source-Mode Quotient Data Ledger"
date: "2026-06-24"
status: exploration/ledger
doc_type: qft_source_mode_quotient_data_ledger
verdict: "BLOCKED_AT_MISSING_SOURCE_PROJECTOR_AND_MODE_QUOTIENT_PACKET"
owned_path: "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
companion_audit:
  - "tests/hourly_cycle2_qft_source_mode_quotient_data_ledger_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md"
  - "explorations/cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"
  - "explorations/observer-finality-physical-forcing-gate-2026-06-24.md"
  - "explorations/observer-finality-pati-salam-chsh-fixture-2026-06-24.md"
  - "explorations/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md"
---

# Hourly Cycle 2 QFT Source-Mode Quotient Data Ledger

## 1. Verdict

The source-mode quotient ledger for

```text
K_b = V_L direct_sum V_R
V_L = (4,2,1),      dim_C V_L = 8
V_R = (4bar,1,2),  dim_C V_R = 8
dim_C K_b = 16
```

cannot be filled from current repo sources.

The current files establish a representation carrier, the formal quotient shape, and the
finite equation

```text
H_phys = Q_b^* H_raw Q_b.
```

They do not establish the source-mode data needed to evaluate that equation. In
particular, no current source file supplies:

```text
P_fin^b:
  source projector/extraction map from the physical field complex to K_b

16 local source-mode records:
  each with representation slot, support/local algebra provenance, and gu-derived:
  provenance

H_raw:
  raw Hermitian Gram matrix computed from the GU physical pairing rule

R_b:
  finite EOM, gauge, constraint, ghost, and null representatives

Q_b:
  quotient/projection to physical finite representatives
```

Therefore the decision is:

```text
SourceModeQuotientLedger(K_b):
  blocked at P_fin^b plus local gu-derived mode records

FiniteQuotientGramGate(K_b):
  still blocked

H_phys:
  not computable from current sources

covariance/state/CHSH:
  no promotion
```

This is a stricter form of the Cycle 1 finite Gram block. Cycle 1 identified the missing
finite quotient-Gram data packet. This ledger identifies the first missing field inside
that packet: the source projector and local mode ledger for the 16 finite modes. Without
that object, an identity Gram, Bell state, Pauli observable set, standard free vacuum, or
target CHSH state would be imported control data rather than GU-derived input.

## 2. Required Source-Mode Quotient Ledger Fields

A promotable source-mode quotient packet for this sector must contain all of the following
fields.

| field | required content | current status |
|---|---|---|
| `sector_id` | `QFT-SSX-PS-LR-QUASIFREE-v0` | named |
| `carrier_spec` | `K_b = V_L direct_sum V_R`, dimensions `8 + 8 = 16` | named as representation carrier |
| `base_field` | exact field such as `QQ`, `QQ_i`, `number_field`, or symbolic exact field | missing |
| `source_projector_P_fin_b` | map `P_fin^b: F_phys^b(O) -> K_b` or equivalent source extractor | missing |
| `raw_mode_records` | exactly 16 finite modes with labels, source representatives, and provenance | missing |
| `mode_provenance` | every mode begins with `gu-derived:` and cites operator/section/constraint data | missing |
| `mode_support` | local support or local algebra inclusion for each mode | missing |
| `H_raw` | exact `16 x 16` Hermitian raw Gram matrix from the source pairing | missing |
| `R_b_removed_representatives` | finite columns for EOM, gauge, constraint, ghost, and null directions | missing |
| `removed_direction_roles` | role label for each removed representative column | missing |
| `Q_b` | exact `16 x r` full-column-rank physical quotient/projection representative | missing |
| `quotient_compatibility` | exact check `R_b^* H_raw Q_b = 0` | not checkable |
| `H_phys` | computed matrix `Q_b^* H_raw Q_b` | not computable |
| `positivity_certificate` | exact proof `H_phys >= 0` and `rank(H_phys) > 0` | not available |
| `source_log` | operator, section, physical adjoint/current, quotient rule, and extractor log | missing |
| `forbidden_import_screen` | rejection of identity/Bell/free-vacuum/target data as source | required guardrail only |
| `decision` | blocked, import/control, fail, or promote-positive-seed-only | blocked |

The removed-direction ledger is not optional. It must represent the following roles, even
when a role is empty:

```text
EOM_b:
  equations of motion or formal-adjoint image directions

Gauge_b:
  gauge or BRST-exact directions, if present in the raw finite sector

Constraint_b:
  section, chirality, Gauss-law, gamma-trace, or branch-specific physical constraints

Ghost_b:
  negative-metric gauge-fixing or auxiliary directions that must not survive

Null_b:
  radical directions of the candidate pairing after the previous removals
```

The ledger must distinguish these cases:

```text
role_empty_because_source_proves_empty:
  acceptable if the source log proves no such representatives exist

role_absent_from_packet:
  blocked

role_deleted_after_a_negative_or_target_state_was_used:
  rollback
```

The minimal matrix contract is:

```text
H_raw = H_raw^*
Q_b has full column rank
R_b^* H_raw Q_b = 0
H_phys = Q_b^* H_raw Q_b
H_phys = H_phys^*
H_phys >= 0
rank(H_phys) > 0
```

No covariance, density matrix, or CHSH fixture can substitute for these ledger fields.

## 3. What Current QFT/CHSH Files Establish

`RESEARCH-POSTURE.md` supplies the governing guardrail: assume the GU reconstruction is
worth pursuing, but do not hide target data inside the reconstruction and do not promote
compatibility to derivation.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade artifact with exact
obstructions, rollback conditions, and no overclaiming.

`hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md` establishes the prior finite
gate:

```text
K_b = V_L direct_sum V_R
V_L = (4,2,1)
V_R = (4bar,1,2)
dim_C K_b = 16
H_phys = Q_b^* H_raw Q_b
```

It also decides that `H_raw`, `Q_b`, removed representatives, mode provenance, and
`H_phys` are missing. This ledger accepts that result and asks which missing field comes
first.

`cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md` supplies the deeper seed
shape:

```text
F_phys^b(O) =
  F_raw^b(O) /
  (EOM_b(O) + Gauge_b(O) + Constraint_b(O) + Ghost_b(O) + Null_b(O))

K_b^fin = K_L^b direct_sum K_R^b
```

It warns that `H_b = diag(I_8, I_8)` is only a control pairing unless the source branch
computes it. It also names `P_fin^b` as the finite mode selection map that would make
`K_b` source-derived.

`observer-finality-physical-forcing-gate-2026-06-24.md` establishes that the physical
CHSH gate requires a GU-derived Alice/Bob state and admissible measurements. It does not
let a hand-inserted Bell state count as physical forcing.

`observer-finality-pati-salam-chsh-fixture-2026-06-24.md` establishes executable CHSH
controls. The maximally entangled control reaches `2*sqrt(2)`, and the product control
stays inside the Bell bound. The file explicitly marks the GU state and GU observables as
pending.

`observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md` establishes the strongest
current CHSH-side attempt: a color-mixed SU(2) Bell ansatz and a pure rank-8 Bell ansatz.
Both are valid density matrices and strong controls. Neither is GU-derived.

Together these files establish the following:

| object | established | not established |
|---|---|---|
| `K_b` | representation carrier `V_L direct_sum V_R`, dimension 16 | source-derived local mode list |
| `P_fin^b` | required as the source projector | actual map |
| quotient roles | EOM/gauge/constraint/ghost/null roles named | finite representatives |
| raw Gram | required as `H_raw` | actual matrix |
| quotient map | required as `Q_b` | actual matrix |
| positive physical Gram | formula `Q_b^* H_raw Q_b` | computed `H_phys` |
| covariance/state | downstream need | no `Gamma_b`, `omega_b`, or `rho_AB` |
| CHSH observables | controls exist | no GU-admissible observables |

## 4. Strongest Positive Data Ledger Attempt

The strongest honest ledger that can be built today is a source-mode quotient shell with
available representation labels and missing source data marked explicitly.

| ledger slot | strongest current entry | decision |
|---|---|---|
| `sector_id` | `QFT-SSX-PS-LR-QUASIFREE-v0` | available |
| `carrier_spec` | `K_b = (4,2,1) direct_sum (4bar,1,2)` | carrier only |
| `basis_pattern` | `e^L_{a alpha}`, `e^R_{bar a dot alpha}` | label pattern only |
| `source_projector_P_fin_b` | no map supplied | missing |
| `raw_mode_records` | no 16 source representatives supplied | missing |
| `mode_provenance` | no `gu-derived:` mode strings supplied | missing |
| `mode_support` | no local support or local algebra inclusion supplied | missing |
| `base_field` | no exact matrix field declared | missing |
| `H_raw` | no raw source Gram supplied | missing |
| `R_b` | no EOM/gauge/constraint/ghost/null columns supplied | missing |
| `Q_b` | no physical quotient/projection matrix supplied | missing |
| `H_phys` | cannot evaluate `Q_b^* H_raw Q_b` | not computable |
| `positivity_certificate` | no eigenvalue, LDL, principal-minor, or interval proof | missing |
| `forbidden_import_screen` | guardrail can be specified | available as policy only |

A conventional control packet can be written:

```text
raw_mode_labels_control = e_1, ..., e_16
H_raw_control = I_16
Q_b_control = I_16
R_b_control = empty
H_phys_control = I_16
```

This is useful as a software plumbing check, but it is not source-mode quotient data. It
has no `P_fin^b`, no local source representatives, no physical adjoint/current, no
removed-direction proof, and no source log. It must be recorded as:

```text
decision: import/control
promotion: forbidden
```

The same applies to the CHSH controls and ansatz states:

```text
Bell control state:
  valid fixture data, not GU source data

Pauli-type observables:
  valid fixture controls, not GU-admissible measurements yet

standard free vacuum or Hadamard/Fock input:
  comparator only unless derived from the GU source branch
```

Therefore the strongest positive result is not a partial computation of `H_phys`. It is a
precise input contract that can reject the obvious false positives.

## 5. First Exact Missing Object

The first exact missing object is:

```text
SourceProjectorPFinBWithLocalModeRecords(b)
```

It must supply:

```text
P_fin^b:
  F_phys^b(O) -> K_b

mode_records:
  16 records m_i with:
    label
    raw representative in F_raw^b(O) or Sol_raw^b(O)
    image in K_b
    representation slot in V_L or V_R
    local support or local algebra inclusion
    provenance beginning gu-derived:
    source branch/operator/section/constraint reference
```

This object comes before `H_raw` in the dependency order:

```text
P_fin^b plus mode records
  -> source raw representatives
  -> H_raw computed from the physical pairing/current
  -> R_b removed-direction representatives
  -> Q_b quotient representatives
  -> H_phys = Q_b^* H_raw Q_b
  -> positivity/rank certificate
```

Why this is first:

```text
The repo can name the target 16-dimensional carrier.
The repo cannot say which 16 source modes occupy that carrier.
Until the modes are source-selected and localized, a Gram matrix would be a matrix on
chosen labels, not a source-derived physical Gram.
```

If a future artifact supplies `P_fin^b` and the 16 local mode records but still lacks
`H_raw`, then the next exact blocker becomes:

```text
SourceRawGramRuleAndMatrix(b)
```

If it supplies `P_fin^b` and `H_raw` but lacks `R_b` and `Q_b`, the next blocker becomes:

```text
FinitePhysicalQuotientRepresentatives(b)
```

As of the current required sources, the block is earlier than both.

## 6. Impact For H_phys, Covariance, And CHSH

`H_phys` is not computable from current sources because both inputs to

```text
H_phys = Q_b^* H_raw Q_b
```

are absent. More precisely:

```text
H_raw:
  absent because there are no source-selected finite mode representatives and no
  source-derived raw physical pairing matrix.

Q_b:
  absent because there are no finite EOM/gauge/constraint/ghost/null representatives
  from which to construct physical quotient representatives.
```

The covariance gate is also blocked. A candidate quasifree covariance would have to obey

```text
Gamma_b = Gamma_b^*
0 <= Gamma_b <= H_phys
```

on the positive quotient. Since `H_phys` is not available, this inequality has no
source-derived finite metric in which to be evaluated.

The CHSH gate remains parked. A CHSH result would require:

```text
rho_AB
A, A' in the Alice algebra
B, B' in the Bob algebra
locality/NAC data
GU-admissible measurement provenance
```

The current Pati-Salam fixtures provide controls and strong ansatz states, not the source
data above. Even a future positive `H_phys` would promote only a positive finite
one-particle seed. It would not by itself produce a covariance, a density matrix, an
Alice/Bob tensor-product reduction, or admissible noncommuting observables.

Therefore:

```text
positive finite seed:
  not promoted

covariance:
  not defined as physical source data

rho_AB:
  missing

CHSH violation:
  not claimed
```

## 7. Rollback/Falsification Conditions

The ledger should drive the following decisions.

| condition | decision |
|---|---|
| no `P_fin^b` | blocked at source projector |
| no 16 local `gu-derived:` mode records | blocked at source-mode provenance |
| no local support or local algebra inclusion | fail local observer input |
| `H_raw` absent after modes are supplied | blocked at raw Gram |
| `H_raw != H_raw^*` | fail raw Gram |
| removed-direction roles omitted | blocked at quotient ledger |
| `R_b^* H_raw Q_b != 0` | fail quotient by gauge/EOM/constraint leakage |
| `Q_b` missing or not full column rank | blocked/fail quotient execution |
| `H_phys != Q_b^* H_raw Q_b` | fail physical Gram computation |
| `H_phys` has a negative eigenvalue after quotient | fail this finite seed sector |
| `rank(H_phys) = 0` | fail nontrivial seed, or report quotient-erased branch |
| identity Gram appears without source log | import/control, no promotion |
| Bell state, Pauli setting, free vacuum, Hadamard/Fock state, or CHSH target chooses data | rollback target import |
| direct sum `K_b` is silently treated as `H_A tensor H_B` | rollback tensor-product import |
| clean packet gives `H_phys >= 0` and nonzero rank | promote positive finite seed only |
| clean positive seed plus later source covariance | advance to covariance gate, not CHSH claim |

These conditions are falsification-friendly. A negative `H_phys` after a correctly
executed quotient is a real failure of this finite Pati-Salam LR quasifree seed. A missing
packet is not a failure of GU, but it is a block on this branch's QFT recovery claim.

## 8. Next Meaningful Finite Computation

The next useful computation is not another Bell fixture. It is an exact finite packet:

```text
packet_id:
  source_mode_quotient_packet_for_QFT_SSX_PS_LR_QUASIFREE_v0

base_field:
  QQ, QQ_i, number_field, or symbolic_exact

source_projector:
  P_fin^b: F_phys^b(O) -> K_b

mode_records:
  16 source-derived local modes

H_raw:
  exact 16 x 16 Hermitian matrix

R_b:
  exact 16 x m removed-direction matrix with role labels

Q_b:
  exact 16 x r physical quotient representative matrix
```

The computation should then run:

```text
1. Verify exactly 16 mode records.
2. Verify every mode provenance begins gu-derived:.
3. Verify every mode has local support or local algebra inclusion.
4. Reject forbidden source strings: control:, ansatz:, Bell, Pauli, free-vacuum,
   Hadamard, Fock, identity-pairing, target, CHSH, Stinespring, CPTP.
5. Verify H_raw = H_raw^*.
6. Verify each removed role is present or source-proved empty.
7. Verify Q_b has full column rank.
8. Verify R_b^* H_raw Q_b = 0.
9. Compute H_phys = Q_b^* H_raw Q_b.
10. Verify H_phys = H_phys^*.
11. Certify H_phys >= 0 exactly.
12. Verify rank(H_phys) > 0.
13. Emit the decision table outcome.
```

Possible outputs:

| computation result | outcome |
|---|---|
| missing projector or mode ledger | blocked |
| missing raw Gram | blocked |
| missing quotient representatives | blocked |
| imported identity Gram | import/control |
| gauge/EOM/constraint leakage | fail |
| negative physical norm | fail |
| zero-rank quotient | fail nontrivial seed |
| clean positive nonzero quotient | promote positive finite seed only |

The first promotable object is therefore:

```text
PositiveFiniteOneParticleSeed(K_b)
```

not:

```text
quasifree covariance
QFT state
rho_AB
CHSH violation
```

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE2_QFT_SOURCE_MODE_QUOTIENT_DATA_LEDGER",
  "version": "2026-06-24",
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "ledger_id": "SourceModeQuotientLedger",
  "verdict": "BLOCKED_AT_MISSING_SOURCE_PROJECTOR_AND_MODE_QUOTIENT_PACKET",
  "status": "blocked",
  "finite_gram_gate_status": "still_blocked",
  "can_compute_H_phys_from_current_sources": false,
  "positive_seed_promoted": false,
  "covariance_promoted": false,
  "chsh_promoted": false,
  "not_a_chsh_or_qft_recovery_claim": true,
  "K_b": {
    "formula": "K_b=V_L direct_sum V_R",
    "V_L": "(4,2,1)",
    "V_R": "(4bar,1,2)",
    "dim_C_V_L": 8,
    "dim_C_V_R": 8,
    "dim_C_K_b": 16,
    "status": "representation_carrier_only_until_P_fin_b_modes_H_raw_R_b_and_Q_b_are_supplied"
  },
  "required_ledger_fields": [
    "sector_id",
    "carrier_spec",
    "base_field",
    "source_projector_P_fin_b",
    "raw_mode_records",
    "mode_provenance",
    "mode_support",
    "H_raw",
    "R_b_removed_representatives",
    "removed_direction_roles",
    "Q_b",
    "quotient_compatibility",
    "H_phys",
    "positivity_certificate",
    "source_log",
    "forbidden_import_screen",
    "decision"
  ],
  "removed_direction_roles": [
    "EOM_b",
    "Gauge_b",
    "Constraint_b",
    "Ghost_b",
    "Null_b"
  ],
  "current_source_supply": {
    "sector_id": "named",
    "carrier_spec": "named_as_representation_carrier",
    "base_field": "missing",
    "source_projector_P_fin_b": "missing",
    "raw_mode_records": "missing",
    "mode_provenance": "missing",
    "mode_support": "missing",
    "H_raw": "missing",
    "R_b_removed_representatives": {
      "EOM_b": "missing",
      "Gauge_b": "missing",
      "Constraint_b": "missing",
      "Ghost_b": "missing",
      "Null_b": "missing"
    },
    "removed_direction_roles": "named_but_not_represented",
    "Q_b": "missing",
    "quotient_compatibility": "not_checkable",
    "H_phys": "not_computable",
    "positivity_certificate": "missing",
    "source_log": "missing",
    "forbidden_import_screen": "guardrail_available_not_source_data",
    "enough_to_compute_H_phys": false
  },
  "what_current_files_establish": [
    "research_posture_forbids_target_data_as_reconstruction",
    "five_lane_runbook_requires_decision_grade_artifacts",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "formal_quotient_roles_EOM_gauge_constraint_ghost_null",
    "finite_formula_H_phys_equals_Q_star_H_raw_Q",
    "identity_Gram_is_control_only_without_source_derivation",
    "CHSH_fixture_controls_pass_but_GU_state_and_observables_are_pending",
    "strongest_CHSH_candidate_states_are_ansatz_not_GU_derived"
  ],
  "strongest_positive_data_attempt": {
    "status": "ledger_shell_only",
    "available_entries": [
      "sector_id",
      "carrier_spec",
      "basis_label_pattern",
      "forbidden_import_screen"
    ],
    "missing_entries": [
      "source_projector_P_fin_b",
      "raw_mode_records",
      "mode_provenance",
      "mode_support",
      "base_field",
      "H_raw",
      "R_b_removed_representatives",
      "Q_b",
      "H_phys",
      "positivity_certificate",
      "source_log"
    ],
    "control_identity_packet": {
      "H_raw_control": "I_16",
      "Q_b_control": "I_16",
      "H_phys_control": "I_16",
      "decision": "import_control",
      "promotion": "forbidden_without_source_log_P_fin_b_modes_and_quotient_representatives"
    }
  },
  "first_exact_missing_object": {
    "id": "SourceProjectorPFinBWithLocalModeRecords",
    "formal_name": "P_fin^b_and_16_gu_derived_local_source_mode_records",
    "why_first": "the_repo_names_K_b_but_does_not_identify_which_local_source_modes_occupy_that_carrier",
    "must_emit": [
      "P_fin_b_from_F_phys_b_O_to_K_b",
      "exactly_16_mode_records",
      "raw_representatives",
      "representation_slots",
      "local_support_or_local_algebra_inclusion",
      "provenance_beginning_gu_derived",
      "source_branch_operator_section_constraint_reference"
    ],
    "next_blocker_if_supplied_without_Gram": "SourceRawGramRuleAndMatrix",
    "next_blocker_if_Gram_supplied_without_quotient": "FinitePhysicalQuotientRepresentatives"
  },
  "H_phys_covariance_chsh_impact": {
    "H_phys": "not_computable_without_H_raw_and_Q_b",
    "covariance": "blocked_because_0_le_Gamma_b_le_H_phys_has_no_source_derived_H_phys",
    "rho_AB": "missing",
    "CHSH": "parked",
    "positive_H_phys_would_promote_only": "positive_finite_one_particle_seed",
    "positive_H_phys_would_not_promote": [
      "quasifree_covariance",
      "QFT_state",
      "rho_AB",
      "Alice_Bob_tensor_product_reduction",
      "GU_admissible_observables",
      "CHSH_violation"
    ]
  },
  "forbidden_target_imports": [
    "identity_Gram_as_GU_derivation",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_covariance_or_CHSH_state",
    "Stinespring_or_CPTP_channel_as_GU_source_without_derivation",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
    "ordinary_SM_or_Pati_Salam_labels_as_physical_Gram"
  ],
  "decision_table": {
    "missing_P_fin_b": "blocked",
    "missing_16_gu_derived_local_modes": "blocked",
    "missing_local_support": "fail_local_observer_input",
    "missing_H_raw": "blocked",
    "H_raw_not_Hermitian": "fail_raw_Gram",
    "missing_removed_direction_roles": "blocked",
    "missing_Q_b": "blocked",
    "Q_b_not_full_column_rank": "fail_quotient_execution",
    "R_star_H_raw_Q_nonzero": "fail_gauge_EOM_constraint_leakage",
    "H_phys_not_equal_Q_star_H_raw_Q": "fail_physical_Gram_computation",
    "H_phys_negative": "fail_finite_seed",
    "H_phys_rank_zero": "fail_nontrivial_seed_or_report_quotient_erased_branch",
    "identity_Gram_without_source_log": "import_control",
    "Bell_Pauli_free_vacuum_or_CHSH_target_used": "rollback_target_import",
    "direct_sum_silently_used_as_tensor_product": "rollback_tensor_product_import",
    "clean_packet_H_phys_psd_nonzero_rank": "promote_positive_finite_seed_only",
    "clean_positive_seed_plus_later_source_covariance": "advance_to_covariance_gate_not_CHSH_claim"
  },
  "next_meaningful_finite_computation": {
    "id": "exact_source_mode_quotient_packet_for_K_b",
    "input_packet": "SourceModeQuotientPacket",
    "packet_id": "source_mode_quotient_packet_for_QFT_SSX_PS_LR_QUASIFREE_v0",
    "steps": [
      "verify_exactly_16_mode_records",
      "verify_all_mode_provenance_starts_gu_derived",
      "verify_local_support_or_local_algebra_inclusion",
      "reject_forbidden_source_strings",
      "verify_H_raw_equals_H_raw_star",
      "verify_removed_roles_present_or_source_proved_empty",
      "verify_Q_b_full_column_rank",
      "verify_R_star_H_raw_Q_equals_zero",
      "compute_H_phys_equals_Q_star_H_raw_Q",
      "verify_H_phys_equals_H_phys_star",
      "certify_H_phys_positive_semidefinite_exactly",
      "verify_rank_H_phys_positive",
      "emit_decision_table_outcome"
    ],
    "first_promotable_output": "PositiveFiniteOneParticleSeed_K_b",
    "not_yet": [
      "quasifree_covariance",
      "QFT_state",
      "rho_AB",
      "CHSH_violation"
    ]
  }
}
```
