---
title: "Cycle 1 QFT Positive Physical Two-Point Certificate"
date: "2026-06-24"
status: exploration/certificate_attempt
doc_type: qft_positive_physical_two_point_certificate
verdict: "BLOCKED_AT_PHYSICAL_FIELD_COMPLEX_AND_POSITIVE_PAIRING_SEED"
owned_path: "explorations/cycle-gates-and-audits/cycle1-qft-positive-two-point-certificate-2026-06-24.md"
companion_audit:
  - "tests/cycle1_qft_positive_two_point_certificate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "lab/process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/mission-a-qft-state-space-extraction-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/gu-measurement-channel-chsh-gate-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/barandes-stochastic-quantum-crosswalk-2026-06-24.md"
---

# Cycle 1 QFT Positive Physical Two-Point Certificate

## 1. Verdict

`PositivePhysicalTwoPointCertificate(b)` can be specified precisely for the minimal
sector

```text
QFT-SSX-PS-LR-QUASIFREE-v0
```

but it cannot be constructed from current repo sources.

The current repo supplies a typed source carrier, a conditional operator/action spine,
Pati-Salam left/right representation labels, and downstream CHSH/control gates. It does
not yet supply the section-pulled physical field complex, positive physical pairing, or
source-derived covariance needed to define a physical quasifree state.

Decision:

```text
certificate shell: explicit
candidate CAR/quasifree construction: conditional
source-derived certificate: not closed
first exact obstruction:
  PhysicalFieldComplexAndPositivePairingSeed(b)
not a QFT recovery claim: true
```

The most conservative construction is therefore:

```text
If GU supplies a positive physical one-particle seed
  (D_phys^b, F_phys^b, K_b, h_b)
and then supplies a covariance C_b satisfying 0 <= C_b <= I_b,
then a standard CAR quasifree state omega_b follows.

The current repo does not supply those inputs.
```

This is a useful obstruction, not a dead end. It says the next proof object must be a
source-derived positive one-particle seed before any vacuum, Bell state, standard free
Dirac state, Barandes/Stinespring channel, or finite CHSH state may be promoted.

## 2. What The Repo Already Supplies

The usable input is real but stops before state extraction.

| supplied object | current status | use for this certificate | limitation |
|---|---|---|---|
| Mission A posture | canon | permits aggressive constructive reconstruction with rollback conditions | not evidence for a state |
| five-lane runbook | canon | requires a decision-grade frontier artifact and no overclaiming | process only |
| `QFT-SSX-PS-LR-QUASIFREE-v0` sector | specified in the Mission A QFT extraction attempt | fixes the minimal Pati-Salam left/right quasifree target | sector is not yet a source-derived theory |
| typed operator/action spine | canonical proposal, not proof-grade | supplies `Y`, `P`, `S`, section pullback, and conditional `D_roll` / `Phi_d` language | does not prove primary `D_GU` equals the proposed spine |
| Pati-Salam proxy | representation branch | gives finite labels `V_L=(4,2,1)` and `V_R=(4bar,1,2)` | labels do not determine a state, pairing, covariance, or amplitudes |
| QFT shadow certificate | schema defined, blocked | names the state-space, state, observable, locality, unitarity, spin-statistics, and anomaly debts | says these objects are missing |
| measurement channel CHSH gate | provenance gate | names the downstream need for `rho_AB` and `gu-admissible` observables | current violating states are controls or ansatz |
| Barandes/Stinespring crosswalk | comparator/null-model note | sharpens anti-smuggling around chosen channels | does not source a GU channel or two-point state |

Thus the repo can host the following conditional theorem shape:

```text
source branch b
  -> physical one-particle seed
  -> positive covariance
  -> quasifree CAR state
  -> GNS representation
  -> possible finite observer reduction
```

It cannot yet fill the first two source arrows.

## 3. Candidate Construction Of `K_b`, `h_b`, `C_b`, And `omega_b` If Possible

Fix a candidate branch:

```text
b =
  operator_spine_conditional
  + section s: X -> Y
  + local observer region O subset X
  + Pati-Salam left/right proxy V_L plus V_R
  + boundary/vacuum convention if GU supplies one
  + gauge/constraint/null-removal rule if GU supplies one
```

The explicit certificate would be:

```text
PositivePhysicalTwoPointCertificate(b):
  branch_id: QFT-SSX-PS-LR-QUASIFREE-v0
  source_provenance: gu-derived:<operator/section/constraint/vacuum-or-state-reference>

  D_phys^b:
    section-pulled physical operator or equation in the chosen sector

  F_phys^b(O):
    compactly supported local field/test/solution complex over O
    quotient by equations of motion
    quotient by gauge, ghost, constraint, and null directions

  K_b(O):
    completion of F_phys^b(O) / Null(h_b)

  h_b:
    Hermitian physical pairing with h_b(f, f) >= 0

  C_b:
    h_b-self-adjoint covariance on K_b with 0 <= C_b <= I_b

  W_b:
    W_b(f, g) = h_b(f, C_b g)

  omega_b:
    gauge-invariant quasifree CAR state generated by C_b

  GNS_b:
    (H_omega, pi_omega, Omega_omega)

  gates:
    positivity
    locality
    gauge/null quotient
    observable admissibility
    finite observer reduction if CHSH is claimed
```

If `K_b`, `h_b`, and `C_b` are available, the conditional construction is standard:

```text
A_b(O) = CAR(K_b(O), h_b)

omega_b(1) = 1
omega_b(a(f)) = omega_b(a^*(f)) = 0
omega_b(a^*(f) a(g)) = h_b(f, C_b g)
omega_b(a(f) a^*(g)) = h_b((I_b - C_b) g, f)
omega_b(odd monomials) = 0
omega_b(higher even monomials) = Wick/determinant rule from C_b
```

The CAR quasifree positivity inequalities are:

```text
h_b(f, f) >= 0
0 <= C_b <= I_b
0 <= h_b(f, C_b f) <= h_b(f, f)
0 <= h_b(f, (I_b - C_b) f) <= h_b(f, f)
```

For a finite CHSH reduction, the additional finite checks would be:

```text
rho_AB = rho_AB^*
rho_AB >= 0
Tr(rho_AB) = 1
```

The construction is not closed because the repo has not produced `D_phys^b`,
`F_phys^b(O)`, `h_b`, or `C_b` from GU source data. Choosing `C_b` by hand, taking a
standard free vacuum, or selecting the maximally entangled finite state would turn the
certificate into an import/control result.

## 4. Positivity, Locality, Gauge/Null Quotient, And Observable Gates

### Positivity Gate

The physical Hilbert/CAR route must first pass:

```text
forall f in F_phys^b(O): h_b(f, f) >= 0
Null(h_b) = {f : h_b(f, f) = 0}
K_b(O) = completion(F_phys^b(O) / Null(h_b))
```

Then the covariance must pass:

```text
C_b = C_b^{*_h}
0 <= C_b <= I_b
W_b(f, f) = h_b(f, C_b f) >= 0
h_b(f, (I_b - C_b) f) >= 0
```

Equivalently, in a finite source-mode basis with Gram matrix `H` and two-point matrix
`Gamma`,

```text
H = H^*
H >= 0
0 <= Gamma <= H
C = H^+ Gamma on the positive quotient
spec(C) subset [0, 1]
```

where `H^+` is used only after the null quotient is made explicit.

### Locality Gate

For local regions `O_1` and `O_2`, the certificate must provide isotony:

```text
O_1 subset O_2  =>  K_b(O_1) -> K_b(O_2)
```

and graded locality for spacelike separated regions:

```text
[A_b(O_1), A_b(O_2)]_graded = 0
```

The typed operator spine and VZ-style principal-symbol work may help define the causal
cone, but they do not by themselves prove microcausality for the live algebra or
positivity for the live state.

### Gauge/Null Quotient Gate

The quotient must be part of the source construction, not a post hoc deletion:

```text
F_raw^b(O)
  -> impose equations of motion
  -> quotient gauge and constraint directions
  -> remove ghosts/nulls
  -> prove h_b descends to a positive pairing
```

If negative-norm modes survive the quotient, the certificate fails in this sector. If
the quotient is not specified, the certificate is underdefined.

### Observable Gate

The CAR state alone does not supply a physical CHSH claim. A downstream observable gate
must provide:

```text
local self-adjoint algebra elements or finite effects
provenance = gu-admissible:<measurement-postulate-reference>
Alice/Bob local commutation
same-party noncommutation justified by a physical readout rule
no postselection
no future-setting dependence
```

The existing Pauli/CHSH observables remain controls until this gate is sourced by GU.

## 5. First Exact Obstruction

The first missing proof object is:

```text
PhysicalFieldComplexAndPositivePairingSeed(b)
```

It must emit:

```text
D_phys^b
F_raw^b(O)
equation/gauge/ghost/constraint/null quotient
F_phys^b(O)
h_b
K_b(O)
proof that h_b(f, f) >= 0 on the quotient
source_provenance = gu-derived:<operator/section/constraint-reference>
```

This is the first obstruction because the inequality `0 <= C_b <= I_b` is not even a
physical statement until `K_b` and `h_b` exist. A covariance is a positive contraction
relative to a positive pairing. Without the pairing and quotient, the symbol `C_b` is only
an inserted matrix or formal kernel.

The smallest worked check that would test the obstruction is a finite matrix seed check:

```text
Input from GU source:
  one local source-defined mode basis e_1,...,e_n in the section-pulled sector
  H_ij = h_b(e_i, e_j)
  Gamma_ij = W_b(e_i, e_j)
  provenance strings beginning gu-derived:

Check:
  H = H^*
  H >= 0
  quotient rank(H) > 0
  Gamma = Gamma^*
  0 <= Gamma <= H on the quotient
  C = H^+ Gamma has generalized eigenvalues in [0, 1]
  no provenance contains control:, ansatz:, imported-vacuum:, free-vacuum:, Bell, Pauli,
  Barandes, or Stinespring as the source of the state
```

For the minimal Pati-Salam left/right test, `n=2` is already meaningful: one
source-selected left mode and one source-selected right mode. A stronger finite check
would use the full `V_L plus V_R` proxy basis. Either outcome is decisive:

| finite check result | decision |
|---|---|
| no source modes or no `H` | blocked at physical seed |
| `H` indefinite after quotient | fail this sector |
| `H >= 0` but `Gamma` is missing | positive state space possible, state extraction blocked |
| `0 <= Gamma <= H` with clean provenance | promote to conditional quasifree state input |
| `Gamma` copied from a free vacuum, Bell state, or ansatz | import/control, not GU evidence |

## 6. What This Means For The Steelman Anti-Quantize-Gravity Direction

This lane strengthens the anti-quantize-gravity steelman by making its quantum debt
sharper.

The GU route need not start by quantizing the four-dimensional metric. It can try to
recover observer-facing quantum theory as a shadow of source geometry, section pullback,
operator structure, and reduction data. But the route still owes a positive local quantum
state. Avoiding metric quantization does not remove the need for:

```text
physical field complex
positive pairing
two-point/covariance state
GNS or equivalent representation
local observables
Born probabilities
unitarity or state-preserving dynamics
spin-statistics and anomaly compatibility
```

The certificate therefore gives the steelman a fair test:

```text
If source geometry produces (K_b, h_b, C_b) with 0 <= C_b <= I_b, then GU can begin to
recover quantum state space without importing metric quantization.

If the only available route is a conventional free vacuum, a Bell state, a Pauli control
fixture, or a chosen stochastic/CPTP channel, then the anti-quantize-gravity branch has
not yet recovered QFT. It has only hosted or simulated target data.
```

Barandes/Stinespring belongs here only as a comparator and null model. A stochastic
process represented by a CPTP map and unitary dilation can show how much quantum-looking
behavior a chosen channel can reproduce. It cannot source `C_b` or `omega_b` unless GU
first derives the stochastic channel itself with `gu-derived:` provenance.

## 7. Next Meaningful Proof Or Computation Step

The next step is not another prose synthesis and not another Bell fixture. It is the
finite source-mode seed check above.

Concrete work packet:

1. Fix one branch:

```text
branch = QFT-SSX-PS-LR-QUASIFREE-v0
operator = D_roll only if the primary operator gate accepts the typed spine
section = explicit local section s_0
region = one small causal diamond O
sector = one left mode in V_L and one right mode in V_R, then scale to full proxy
```

2. Derive or fail the physical seed:

```text
D_phys^b
F_phys^b(O)
h_b
K_b(O)
```

3. Compute finite matrices from source data:

```text
H_ij = h_b(e_i, e_j)
Gamma_ij = W_b(e_i, e_j)
```

4. Run the finite positivity contraction check:

```text
H >= 0
0 <= Gamma <= H
spec(H^+ Gamma) subset [0, 1]
```

5. Only after this passes, define:

```text
W_b(f, g) = h_b(f, C_b g)
omega_b = quasifree CAR state from C_b
GNS_b = GNS(omega_b)
```

6. Then, and only then, attempt the finite observer reduction:

```text
omega_b restricted to source-selected Alice/Bob modes
-> finite CAR covariance
-> any claimed rho_AB with rho_AB >= 0 and Tr(rho_AB) = 1
-> gu-admissible observables if the measurement postulate exists
```

Rollback conditions:

```text
rollback_seed_missing:
  no D_phys^b, no F_phys^b, or no h_b from source data

rollback_indefinite_pairing:
  h_b is indefinite after gauge/null quotient

rollback_covariance_missing:
  no source-derived W_b or C_b after the positive seed exists

rollback_covariance_not_positive:
  Gamma is not Hermitian, not positive, or not bounded above by H

rollback_imported_vacuum:
  state is a standard free Dirac/Hadamard/Fock vacuum inserted without GU derivation

rollback_target_smuggling:
  state is copied from Bell, Pauli, Pati-Salam ansatz, or CHSH target data

rollback_barandes_overuse:
  Barandes/Stinespring supplies the state or channel before GU derives the channel
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE1_QFT_POSITIVE_PHYSICAL_TWO_POINT_CERTIFICATE",
  "version": "2026-06-24",
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "certificate_id": "PositivePhysicalTwoPointCertificate",
  "verdict": "BLOCKED_AT_PHYSICAL_FIELD_COMPLEX_AND_POSITIVE_PAIRING_SEED",
  "status": "blocked",
  "qft_recovered": false,
  "not_a_qft_recovery_claim": true,
  "can_construct_from_current_repo": false,
  "conditional_construction_available": true,
  "repo_supplies": [
    "typed_source_carrier",
    "conditional_operator_action_spine",
    "section_pullback_language",
    "Pati_Salam_left_right_representation_proxy",
    "QFT_shadow_certificate_schema",
    "CHSH_provenance_gate",
    "Barandes_Stinespring_comparator_note"
  ],
  "candidate_construction": {
    "K_b": "completion_of_F_phys_b_O_mod_Null_h_b",
    "h_b": "positive_Hermitian_physical_pairing_on_quotient",
    "C_b": "h_b_self_adjoint_positive_contraction_0_le_C_b_le_I_b",
    "W_b": "W_b(f,g)=h_b(f,C_b_g)",
    "omega_b": "gauge_invariant_quasifree_CAR_state_generated_by_C_b",
    "GNS_b": ["H_omega", "pi_omega", "Omega_omega"]
  },
  "positivity_inequalities": [
    "h_b(f,f)>=0",
    "0<=C_b<=I_b",
    "0<=h_b(f,C_b_f)<=h_b(f,f)",
    "0<=h_b(f,(I_b-C_b)_f)<=h_b(f,f)",
    "H>=0",
    "0<=Gamma<=H",
    "rho_AB>=0",
    "Tr(rho_AB)=1"
  ],
  "first_exact_obstruction": {
    "id": "PhysicalFieldComplexAndPositivePairingSeed",
    "why_first": "C_b_is_a_physical_positive_contraction_only_after_K_b_and_h_b_exist",
    "must_emit": [
      "D_phys_b",
      "F_raw_b_O",
      "equation_gauge_ghost_constraint_null_quotient",
      "F_phys_b_O",
      "h_b",
      "K_b_O",
      "proof_h_b_positive_on_quotient",
      "source_provenance_gu_derived"
    ]
  },
  "blocked_as_gu_derived": [
    "D_phys_b",
    "F_phys_b_O",
    "h_b",
    "K_b_O",
    "C_b",
    "W_b",
    "omega_b",
    "rho_AB",
    "gu_admissible_observables"
  ],
  "forbidden_shortcuts": [
    "claiming_QFT_recovery_from_certificate_shell",
    "using_representation_labels_as_quantum_state",
    "using_Pati_Salam_pairing_as_density_matrix",
    "copying_Bell_state_into_GU_slot",
    "using_Pauli_controls_as_GU_observables",
    "imported_free_Dirac_vacuum",
    "imported_Hadamard_or_Fock_vacuum",
    "generic_vacuum_entanglement_without_finite_reduction",
    "chosen_CPTP_or_Stinespring_channel_as_GU_source",
    "Barandes_correspondence_as_state_derivation"
  ],
  "barandes_stinespring_role": {
    "allowed_role": "comparator_null_model_only",
    "may_source_channel": false,
    "exception": "only_if_GU_independently_derives_the_stochastic_or_CPTP_channel_with_gu_derived_provenance"
  },
  "smallest_worked_check": {
    "id": "finite_source_mode_positive_contraction_check",
    "minimal_modes": "one_source_selected_left_mode_and_one_source_selected_right_mode",
    "inputs": ["H_ij=h_b(e_i,e_j)", "Gamma_ij=W_b(e_i,e_j)", "gu_derived_provenance"],
    "checks": [
      "H_equals_H_star",
      "H_positive_semidefinite",
      "rank_after_null_quotient_positive",
      "Gamma_equals_Gamma_star",
      "Gamma_positive_semidefinite",
      "H_minus_Gamma_positive_semidefinite",
      "generalized_eigenvalues_in_unit_interval",
      "no_forbidden_provenance"
    ]
  },
  "rollback_conditions": [
    "rollback_seed_missing",
    "rollback_indefinite_pairing",
    "rollback_covariance_missing",
    "rollback_covariance_not_positive",
    "rollback_imported_vacuum",
    "rollback_target_smuggling",
    "rollback_barandes_overuse",
    "rollback_observable_gate_missing",
    "rollback_anomaly_or_unitarity_failure"
  ],
  "steelman_anti_quantize_gravity_meaning": "The_branch_can_avoid_starting_with_metric_quantization_only_if_source_geometry_derives_positive_quantum_state_data; otherwise_it_hosts_or_imports_quantum_theory.",
  "next_step": "derive_or_refute_PhysicalFieldComplexAndPositivePairingSeed_then_run_finite_source_mode_positive_contraction_check"
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `lab/process/runbooks/five-lane-frontier-run.md`
- `explorations/cycle-gates-and-audits/mission-a-qft-state-space-extraction-2026-06-24.md`
- `explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/gu-measurement-channel-chsh-gate-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/barandes-stochastic-quantum-crosswalk-2026-06-24.md`
