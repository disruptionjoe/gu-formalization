---
title: "Hourly Cycle 1 QFT Finite Quotient-Gram Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: qft_finite_quotient_gram_gate
verdict: "BLOCKED_AT_SOURCE_DERIVED_FINITE_QUOTIENT_GRAM_DATA"
owned_path: "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md"
companion_audit:
  - "tests/hourly_cycle1_qft_finite_quotient_gram_gate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"
  - "explorations/cycle1-qft-positive-two-point-certificate-2026-06-24.md"
  - "explorations/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/gu-measurement-channel-chsh-gate-2026-06-24.md"
  - "explorations/observer-finality-physical-forcing-gate-2026-06-24.md"
---

# Hourly Cycle 1 QFT Finite Quotient-Gram Gate

## 1. Verdict

The finite quotient-Gram gate for

```text
K_b = V_L direct_sum V_R,
V_L = (4,2,1),
V_R = (4bar,1,2),
dim_C(K_b) = 16
```

is not closed from current repo sources.

The repo supplies a conditional Pati-Salam left/right representation carrier and the
formal shape of the physical quotient. It does not supply the finite data needed to
compute or certify a GU-derived positive Gram matrix:

| finite object | current decision | reason |
|---|---|---|
| gu-derived finite mode provenance for all 16 modes | missing | representation labels exist, but no source extraction map or local mode list exists |
| `H_raw` | missing | no source-derived physical adjoint, current, or finite raw Gram computation is emitted |
| quotient/projection `Q_b` | missing | equation, gauge, constraint, ghost, and null subspaces are named but not represented |
| gauge/constraint/null representatives | missing | no finite representative matrices or basis vectors are supplied |
| positive `H_phys = Q_b^* H_raw Q_b` | not computed | there is no `H_raw` or `Q_b`; identity positivity would be imported control data |

Therefore the gate verdict is:

```text
FiniteQuotientGramGate(K_b):
  blocked at SourceDerivedFiniteQuotientGramData(b)

strongest current positive seed:
  a control shell on C^8_L direct_sum C^8_R with an identity Hermitian form

promotion status:
  not GU-derived

CHSH/observer status:
  still parked; no source-derived state and no GU-admissible observables
```

This is a useful block. It moves the prior positive-pairing seed one level lower: the
first needed computation is no longer an abstract positive physical pairing, but an exact
finite quotient-Gram computation with explicit source provenance.

## 2. What Was Derived Directly From Repo Sources

The following data can be carried forward directly from the required source artifacts.

### Source Posture And Run Contract

`RESEARCH-POSTURE.md` sets the working posture: assume GU is worth reconstructing, but do
not inflate compatibility into derivation and do not hide target data inside a
reconstruction.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade artifact, exact
missing proof objects, rollback conditions, and no overclaiming. This file therefore
treats an identity Gram matrix, a Bell state, Pauli observables, or a standard vacuum as
controls unless the repo supplies a GU derivation.

### QFT State-Space And Pairing Inputs

`cycle1-qft-positive-two-point-certificate-2026-06-24.md` identifies the first blocker as

```text
PhysicalFieldComplexAndPositivePairingSeed(b)
```

and states that a covariance or two-point function is not physical until `K_b` and a
positive `h_b` exist.

`cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md` refines that blocker to

```text
SourceDerivedPositivePairingOnQuotient(b)
```

and fixes the finite candidate seed space

```text
K_b^fin = K_L^b direct_sum K_R^b
K_L^b ~= V_L = (4,2,1),      dim_C = 8
K_R^b ~= V_R = (4bar,1,2),  dim_C = 8
```

It also gives the finite positivity equations this gate now specializes:

```text
H_phys = Q_b^* H_raw Q_b
H_phys = H_phys^*
H_phys >= 0
rank(H_phys) > 0
```

The same source explicitly warns that

```text
H_b = diag(I_8, I_8)
```

is a valid control pairing but not a GU-derived positive pairing.

### QFT Shadow And Observer Inputs

`qft-shadow-extraction-certificate-2026-06-24.md` keeps the QFT shadow blocked before a
positive state space, state extraction, admissible observables, Born probabilities,
unitarity, spin-statistics, and anomaly closure.

`gu-measurement-channel-chsh-gate-2026-06-24.md` parks `OBS-CHSH` because the repo lacks:

```text
rho_AB
gu-admissible local CHSH observables
finite GU state-preparation map
finite GU Gram data
```

`observer-finality-physical-forcing-gate-2026-06-24.md` says the exact physical-forcing
gate is to derive the Alice/Bob state and admissible measurement operators from the GU
SM-sector zero modes or section-pullback propagator, then compute CHSH. It does not allow
a hand-inserted Bell state to count as physical forcing.

### Directly Usable And Not Directly Usable

| item | directly usable here | not supplied |
|---|---|---|
| sector id | `QFT-SSX-PS-LR-QUASIFREE-v0` | proof-grade primary operator closure |
| finite carrier | `K_b = V_L direct_sum V_R`, dim 16 | local source modes inside that carrier |
| labels | `(4,2,1)` and `(4bar,1,2)` | mode provenance strings beginning `gu-derived:` |
| quotient shape | remove EOM, gauge, constraints, ghosts, nulls | finite representative matrices |
| positivity formula | `H_phys = Q_b^* H_raw Q_b` | computed `H_raw`, `Q_b`, eigenvalues, rank |
| CHSH fixture | downstream executable controls | source-derived state and observables |

## 3. Strongest Positive Finite Seed Construction

The strongest construction currently licensed by the repo is a finite control shell, not
a promoted seed.

Choose ordered labels:

```text
e^L_{a alpha},      a = 1..4, alpha = 1..2
e^R_{bar a dot a},  bar a = 1..4, dot a = 1..2
```

and define the raw finite carrier:

```text
K_raw = span_C{e^L_{a alpha}} direct_sum span_C{e^R_{bar a dot a}}
      ~= C^8_L direct_sum C^8_R.
```

If an exact source data packet is later supplied, it must have this form:

```text
FiniteSourceQuotientGramData(b):
  branch_id:
    QFT-SSX-PS-LR-QUASIFREE-v0

  base_field:
    one of QQ, QQ_i, number_field, symbolic_exact

  raw_modes:
    16 finite modes with labels, local support data, and provenance strings
    beginning gu-derived:

  H_raw:
    16 x 16 Hermitian matrix over the declared exact base field

  R_b:
    finite representative matrix whose columns span EOM, gauge, constraint,
    ghost, and declared null directions in K_raw

  Q_b:
    16 x r full-column-rank representative or projection matrix for physical
    quotient representatives

  H_phys:
    Q_b^* H_raw Q_b

  source_log:
    the operator, section, physical adjoint/current, quotient rule, and local
    mode extractor used to compute the data
```

The gate then checks:

```text
1. every surviving mode has gu-derived provenance;
2. forbidden source strings are absent;
3. H_raw = H_raw^* over the declared exact field;
4. R_b^* H_raw Q_b = 0, so removed directions do not leak into the quotient;
5. H_phys = Q_b^* H_raw Q_b;
6. H_phys = H_phys^*;
7. eigenvalues or exact principal minors certify H_phys >= 0;
8. rank(H_phys) > 0 after null removal;
9. surviving labels remain inside V_L direct_sum V_R;
10. local support data do not insert a nonlocal Alice/Bob state by basis choice.
```

A control construction is available today:

```text
H_raw_control = I_16
Q_b_control = I_16
H_phys_control = I_16
```

This demonstrates that the finite linear algebra is easy once data are inserted. It does
not demonstrate GU positivity. It lacks source modes, a quotient, a GU physical adjoint,
and a derivation of the identity matrix from the source branch.

Promotion criterion:

```text
Promote to positive finite seed only if H_raw and Q_b are source-derived and the
computed H_phys is positive semidefinite with nonzero rank.
```

Even after promotion, this would still be only a positive one-particle seed. It would not
yet be a covariance, vacuum, density matrix, or CHSH result.

## 4. First Exact Obstruction Or Missing Object

The first exact missing object is:

```text
SourceDerivedFiniteQuotientGramData(b)
```

This object sits strictly inside the prior blocker:

```text
PhysicalFieldComplexAndPositivePairingSeed(b)
  -> SourceDerivedPositivePairingOnQuotient(b)
     -> SourceDerivedFiniteQuotientGramData(b)
```

It must emit five finite objects:

```text
1. gu-derived finite mode provenance:
   a source extraction map P_fin^b and 16 local modes in the Pati-Salam LR block.

2. H_raw:
   the raw finite Hermitian Gram matrix computed from the GU physical pairing rule.

3. Q_b:
   the quotient/projection map to physical representatives.

4. removed-direction representatives:
   finite columns for EOM, gauge, constraint, ghost, and null directions.

5. H_phys:
   the computed physical Gram matrix with an exact positivity/rank certificate.
```

Why this is first:

```text
The repo can name K_b as a representation carrier.
The repo can state the quotient formula.
The repo can state the positivity equation.
The repo cannot evaluate the equation because its finite inputs are absent.
```

The obstruction is not the lack of a Bell state. It is earlier: no source-derived
positive finite one-particle Gram exists yet. A Bell state, standard free vacuum,
Hadamard/Fock state, Pauli setting, or identity pairing would skip the gate.

Exact rollback conditions:

| result | decision |
|---|---|
| no `P_fin^b` or mode provenance | blocked at finite mode extraction |
| no `H_raw` | blocked at physical pairing |
| no `Q_b` or representatives | blocked at quotient |
| `R_b^* H_raw Q_b != 0` | gauge/constraint leakage |
| `H_phys` has a negative eigenvalue | fail this finite seed sector |
| `rank(H_phys) = 0` | quotient erased the seed |
| `H_phys = I_16` with no source computation | control/import, not GU evidence |
| modes are globally chosen with no local support | nonlocal finite fixture, not local QFT input |

## 5. Failure Modes: Negative Norm, Gauge Leakage, Imported Identity Gram, Nonlocal Finite Modes

### Negative Norm

The finite seed fails if

```text
exists v in im(Q_b): v^* H_raw v < 0
```

or equivalently if `H_phys` has a negative eigenvalue after all declared quotient
directions have been removed. This is a physical Hilbert/CAR obstruction. It cannot be
fixed by deleting the negative vector after using it to choose a state.

### Gauge Leakage

The quotient fails if removed directions still pair with physical representatives:

```text
R_b^* H_raw Q_b != 0.
```

Here `R_b` must include the finite EOM, gauge, constraint, ghost, and declared-null
representatives. If these columns are not supplied, the quotient has not been executed.
If charged field modes are used as intermediate CAR generators, the later observable
gate must still specify the gauge-invariant physical readouts or superselection rule.

### Imported Identity Gram

The identity matrix is allowed as a control:

```text
H_control = I_16.
```

It is forbidden as a promoted GU result unless the source computation produces it. The
audit rule is:

```text
identity Gram + no source_log = import/control
identity Gram + source_log + quotient certificate = possible derived result
```

The phrase "Pati-Salam labels carry the standard Hermitian metric" is not enough. Labels
select representation slots. They do not compute a physical pairing, remove constraints,
or prove positivity.

### Nonlocal Finite Modes

The finite modes must carry local support or local algebra provenance. A globally chosen
basis of `V_L direct_sum V_R` can build a convenient finite matrix, but it can also hide
the Alice/Bob correlation in the basis choice.

Required local data:

```text
mode_support:
  O, O_A, O_B, or a stated local smearing region

local_map:
  F_phys^b(O) -> K_b or A_b(O) -> finite algebra

left_right_status:
  representation label plus local origin, not only a global internal index
```

Without this, a later CHSH value would test a nonlocal finite fixture rather than a
GU-derived local measurement channel.

## 6. Impact For CHSH/Observer Forcing

This gate does not upgrade `OBS-CHSH`.

Reason:

```text
K_b = V_L direct_sum V_R
```

is a finite one-particle carrier. The CHSH fixture needs a two-party finite state and
observables:

```text
H_A tensor H_B
rho_AB
A, A' in End(H_A)
B, B' in End(H_B)
```

A positive `H_phys` on `K_b` would be useful because it would make the one-particle
finite seed legitimate. It would not by itself provide:

```text
C_b or W_b
omega_b
rho_AB
direct-sum-to-tensor-product reduction
GU-admissible measurement observables
CHSH > 2
```

Therefore the observer/finality physical-forcing status remains:

```text
OBS-CHSH:
  parked

formal controls:
  still useful

current violating finite states:
  controls or ansatz only

upgrade condition:
  first pass the finite quotient-Gram gate,
  then derive a positive covariance/state,
  then derive admissible observables,
  then run the CHSH gate without weakening provenance rules.
```

If the finite Gram gate fails because `H_phys` is indefinite, the candidate Pati-Salam
left/right quasifree route fails before CHSH. If the finite Gram gate passes but no
source-derived covariance exists, the repo would have a positive one-particle seed but
still no physical CHSH state.

## 7. Next Meaningful Finite Computation

The next computation should be an exact finite matrix packet, not another Bell fixture.

### Input Packet

```text
packet_id:
  finite_source_quotient_Gram_packet_for_QFT_SSX_PS_LR_QUASIFREE_v0

base_field:
  QQ, QQ_i, number_field, or symbolic_exact

raw_basis:
  16 source-derived modes in K_raw = V_L direct_sum V_R

mode records:
  label
  representation block
  source extractor P_fin^b
  local support
  provenance beginning gu-derived:

H_raw:
  exact 16 x 16 Hermitian matrix

R_b:
  exact 16 x m removed-direction matrix with column roles
  EOM, gauge, constraint, ghost, null

Q_b:
  exact 16 x r quotient representative matrix
```

### Computation

```text
1. Verify all mode provenance begins gu-derived:.
2. Reject provenance containing control:, ansatz:, Bell, Pauli, free-vacuum,
   Hadamard, Fock, identity-pairing, target, CHSH, or Stinespring as a source.
3. Check H_raw = H_raw^* exactly.
4. Check Q_b has full column rank.
5. Check removed directions are quotient-radical directions:
   R_b^* H_raw Q_b = 0.
6. Compute H_phys = Q_b^* H_raw Q_b.
7. Check H_phys = H_phys^* exactly.
8. Certify H_phys >= 0 by exact eigenvalue, LDL, principal-minor, or rational interval
   proof appropriate to the declared base field.
9. Check rank(H_phys) > 0 after null removal.
10. Emit every negative, zero, and positive direction with provenance.
```

### Decisions

| computation result | promoted decision |
|---|---|
| clean provenance, exact quotient, `H_phys >= 0`, nonzero rank | promote positive finite seed only |
| same, plus later `0 <= Gamma <= H_phys` | promote candidate quasifree covariance input |
| missing provenance or local support | blocked |
| identity Gram without source log | import/control |
| negative eigenvalue after quotient | fail finite seed |
| gauge/constraint leakage | fail quotient execution |
| nonlocal mode extraction | fail local observer input |

The computation should output JSON next to any mathematical note so future audits can
check the matrix fields directly.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE1_QFT_FINITE_QUOTIENT_GRAM_GATE",
  "version": "2026-06-24",
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "gate_id": "FiniteQuotientGramGate",
  "verdict": "BLOCKED_AT_SOURCE_DERIVED_FINITE_QUOTIENT_GRAM_DATA",
  "status": "blocked",
  "qft_recovered": false,
  "positive_seed_promoted": false,
  "chsh_claimed": false,
  "not_a_chsh_or_qft_recovery_claim": true,
  "K_b": {
    "formula": "K_b=V_L direct_sum V_R",
    "V_L": "(4,2,1)",
    "V_R": "(4bar,1,2)",
    "dim_C_V_L": 8,
    "dim_C_V_R": 8,
    "dim_C_K_b": 16,
    "status": "representation_carrier_only_until_source_modes_and_Gram_are_supplied"
  },
  "current_repo_supply": {
    "gu_derived_mode_provenance": "missing_individual_modes",
    "source_extraction_map_P_fin_b": "missing",
    "H_raw": "missing",
    "Q_b": "missing",
    "removed_direction_representatives": "missing",
    "H_phys": "not_computed",
    "positive_H_phys": "not_established",
    "identity_Gram": "control_only_if_inserted",
    "rho_AB": "missing",
    "gu_admissible_observables": "missing"
  },
  "derived_directly_from_sources": [
    "Mission_A_posture_and_no_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "sector_id_QFT_SSX_PS_LR_QUASIFREE_v0",
    "finite_carrier_K_b_as_V_L_direct_sum_V_R",
    "Pati_Salam_labels_V_L_4_2_1_and_V_R_4bar_1_2",
    "quotient_shape_EOM_gauge_constraint_ghost_null",
    "finite_positivity_equation_H_phys_equals_Q_star_H_raw_Q",
    "OBS_CHSH_parked_until_rho_AB_and_gu_admissible_observables"
  ],
  "strongest_positive_finite_seed_construction": {
    "control_carrier": "C^8_L direct_sum C^8_R",
    "control_H_raw": "I_16",
    "control_Q_b": "I_16",
    "control_H_phys": "I_16",
    "control_status": "finite_linear_algebra_control_not_GU_derivation",
    "promotion_condition": "source_derived_H_raw_and_Q_b_compute_positive_nonzero_H_phys"
  },
  "first_exact_obstruction": {
    "id": "SourceDerivedFiniteQuotientGramData",
    "inside": [
      "PhysicalFieldComplexAndPositivePairingSeed",
      "SourceDerivedPositivePairingOnQuotient"
    ],
    "must_emit": [
      "gu_derived_finite_mode_provenance",
      "source_extraction_map_P_fin_b",
      "H_raw",
      "Q_b",
      "EOM_gauge_constraint_ghost_null_representatives",
      "H_phys",
      "positive_semidefinite_nonzero_rank_certificate",
      "local_support_data"
    ],
    "why_first": "K_b_and_the_positivity_formula_are_named_but_the_finite_inputs_to_evaluate_H_phys_are_absent"
  },
  "finite_gram_input_contract": {
    "packet_id": "finite_source_quotient_Gram_packet_for_QFT_SSX_PS_LR_QUASIFREE_v0",
    "required_finite_Gram_fields": [
      "branch_id",
      "base_field",
      "raw_basis",
      "mode_provenance",
      "mode_support",
      "source_extraction_map_P_fin_b",
      "H_raw",
      "R_b_removed_direction_matrix",
      "removed_direction_roles",
      "Q_b",
      "H_phys",
      "source_log"
    ],
    "allowed_exact_base_fields": [
      "QQ",
      "QQ_i",
      "number_field",
      "symbolic_exact"
    ],
    "expected_shapes": {
      "H_raw": "16x16",
      "R_b": "16xm",
      "Q_b": "16xr",
      "H_phys": "rxr"
    },
    "finite_checks": [
      "all_mode_provenance_starts_gu_derived",
      "no_forbidden_provenance",
      "H_raw_equals_H_raw_star",
      "Q_b_full_column_rank",
      "R_star_H_raw_Q_equals_zero",
      "H_phys_equals_Q_star_H_raw_Q",
      "H_phys_equals_H_phys_star",
      "H_phys_positive_semidefinite_exact_certificate",
      "rank_H_phys_positive",
      "surviving_modes_inside_Pati_Salam_LR_block",
      "local_support_not_global_nonlocal_fixture"
    ]
  },
  "failure_modes": {
    "negative_norm": "negative_eigenvalue_of_H_phys_after_quotient_fails_seed",
    "gauge_leakage": "R_star_H_raw_Q_nonzero_or_missing_R_b_blocks_quotient_execution",
    "imported_identity_Gram": "I_16_without_source_log_is_control_import_not_GU_derivation",
    "nonlocal_finite_modes": "global_basis_without_local_support_fails_local_observer_input"
  },
  "forbidden_promotions": [
    "imported_identity_Gram_as_GU_derivation",
    "Pati_Salam_labels_as_positive_pairing",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_CHSH_state_or_covariance",
    "Stinespring_or_CPTP_channel_as_GU_source_without_GU_derivation",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map"
  ],
  "chsh_observer_impact": {
    "obs_chsh_status": "parked",
    "positive_H_phys_would_imply": "positive_one_particle_seed_only",
    "positive_H_phys_would_not_imply": [
      "C_b",
      "W_b",
      "omega_b",
      "rho_AB",
      "direct_sum_to_tensor_product_reduction",
      "gu_admissible_observables",
      "CHSH_violation"
    ],
    "requires_before_chsh_claim": [
      "positive_finite_quotient_Gram",
      "source_derived_covariance_or_state",
      "finite_Alice_Bob_reduction",
      "gu_admissible_observables",
      "locality_NAC_for_live_data"
    ]
  },
  "next_meaningful_finite_computation": {
    "id": "exact_finite_source_quotient_Gram_computation_for_K_b",
    "input_packet": "FiniteSourceQuotientGramData",
    "first_promotable_output": "positive_finite_seed_if_H_phys_psd_nonzero_rank_with_clean_provenance",
    "not_yet": [
      "quasifree_covariance",
      "QFT_state",
      "rho_AB",
      "CHSH_claim"
    ],
    "decision_table": {
      "missing_H_raw_or_Q_b": "blocked",
      "identity_Gram_without_source_log": "import_control",
      "R_star_H_raw_Q_nonzero": "gauge_leakage_fail",
      "H_phys_negative": "finite_seed_fail",
      "H_phys_rank_zero": "quotient_erased_seed",
      "H_phys_positive_clean_provenance": "promote_positive_finite_seed_only"
    }
  }
}
```
