---
title: "Cycle 2 QFT Physical Field Complex And Positive Pairing Seed"
date: "2026-06-24"
status: exploration/seed_attempt
doc_type: qft_physical_field_positive_pairing_seed
verdict: "UNDERDEFINED_POSITIVITY_IMPORTED_IF_STANDARD_PAIRING_IS_USED"
owned_path: "explorations/cycle-gates-and-audits/cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"
companion_audit:
  - "tests/cycle2_qft_physical_field_positive_pairing_seed_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "lab/process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/cycle1-qft-positive-two-point-certificate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/mission-a-qft-state-space-extraction-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/gu-measurement-channel-chsh-gate-2026-06-24.md"
---

# Cycle 2 QFT Physical Field Complex And Positive Pairing Seed

## 1. Verdict

`PhysicalFieldComplexAndPositivePairingSeed(b)` can be specified one level deeper for
the candidate sector

```text
QFT-SSX-PS-LR-QUASIFREE-v0
```

but it still cannot be constructed as a GU-derived positive seed from the current repo.

Decision:

```text
D_phys^b:
  conditional candidate only, obtained by section-pulling the typed operator spine and
  projecting to the Pati-Salam left/right block.

gauge/null quotient:
  quotient shape is explicit, but the repo does not yet supply the live constraint,
  ghost, charged-field, observable, and null-removal rules needed to execute it.

h_b:
  a standard positive Dirac/Cauchy or finite Hermitian pairing can be written down,
  but that positivity is imported unless GU supplies the physical adjoint/current/Gram
  form and proves it descends to the quotient.

K_b:
  finite candidate seed space is K_b^fin = V_L direct_sum V_R, with
  V_L = (4,2,1), V_R = (4bar,1,2), complex dimension 16.
  It is source-derived only if its modes, quotient map, and Gram matrix come from
  D_phys^b and the GU section/constraint data.

current verdict:
  underdefined for GU-derived positivity;
  import/control if filled by the standard identity pairing;
  not a QFT recovery claim.
```

The useful positive result is narrow: this file fixes the smallest seed object that would
remove the Cycle 1 blocker. The negative result is also narrow: current repo data do not
produce the positive physical pairing. They only allow a conventional positive pairing
to be hosted on the representation labels.

## 2. Candidate Physical Complex And Quotient

Fix the working branch

```text
b =
  operator_spine_conditional
  + section s_0: X -> Y
  + observer region O subset X
  + Pati-Salam left/right projector Pi_PS
  + physical/gauge/constraint projector Pi_phys if supplied
  + boundary or vacuum convention if supplied
```

The typed operator spine supplies the proposal-level source operator `D_roll` and the
section-pullback language. It does not prove that this is the primary `D_GU`. Therefore
the candidate physical operator is conditional:

```text
D_phys^b := Pi_phys Pi_PS s_0^*(D_roll) Pi_PS Pi_phys
```

with all lower-order, domain, gauge-fixing, and constraint terms retained in the
unresolved physical block. If the primary operator later lacks the `Phi_d` first-order
block, has `lambda_d = 0`, or uses a different field sector, this candidate must be
replaced.

The minimal Pati-Salam left/right field bundle is specified only as a target shape:

```text
E_PS^b(O) = E_L^b(O) direct_sum E_R^b(O)

finite internal fibers:
  V_L = (4,2,1),       dim_C V_L = 8
  V_R = (4bar,1,2),   dim_C V_R = 8
```

The four-dimensional spinor factor, chirality convention, physical adjoint, and exact
relation between `s_0^*S` and this left/right observer block remain part of the missing
physical reduction. Representation labels do not by themselves define a physical field
complex.

A minimal raw test-function complex can be written as:

```text
F_raw^b(O) = Gamma_c(O, E_PS^b)
D_phys^b: F_raw^b(O) -> Gamma_c(O, F_PS^b)
```

or, if the Green-hyperbolic/solution route is supplied:

```text
Sol_raw^b(O) =
  { psi in Gamma_sc(E_PS^b over D(O)) : D_phys^b psi = 0 and constraints hold }
```

The physical quotient must be part of the source construction:

```text
F_phys^b(O) =
  F_raw^b(O) /
  (EOM_b(O) + Gauge_b(O) + Constraint_b(O) + Ghost_b(O) + Null_b(O))
```

where:

```text
EOM_b(O):
  image of D_phys^b or of the formal adjoint in the test-function quotient.

Gauge_b(O):
  source-specified gauge or BRST-exact directions.
  For a pure charged spinor CAR field this may be zero at the field-algebra level,
  while the physical observable algebra is the gauge-invariant subalgebra.
  If the ambient 0/1 form-spinor sector has gauge or constraint directions, they
  must be listed explicitly rather than deleted after the fact.

Constraint_b(O):
  section, chirality, gamma-trace, Gauss-law, or other physical constraints that the
  actual branch imposes.

Ghost_b(O):
  negative-metric auxiliary or gauge-fixing fields that must not survive into the
  physical one-particle space.

Null_b(O):
  radical of the candidate pairing after the previous quotients.
```

For the quotient to be valid, `D_phys^b` and `h_b` must be compatible:

```text
h_b(gauge_or_constraint_direction, physical_field) = 0
h_b(eom_direction, physical_field) = 0
h_b(null_direction, physical_field) = 0
h_b descends to F_phys^b(O)
```

The current repo does not supply the data needed to check those equations. This is why
the complex is specified but not constructed.

## 3. Candidate Positive Pairing And Positivity Conditions

There are two useful candidate pairings. Both are currently imports unless GU derives
their ingredients.

### 3.1 Continuum Dirac/Cauchy Candidate

If the section `s_0` gives a time-oriented globally hyperbolic observer geometry, if the
physical spinor adjoint is selected, and if `D_phys^b` has a conserved current, then a
standard positive one-particle pairing would have the form:

```text
h_b([psi], [phi]) =
  integral over Sigma of
    psi^dagger J_b gamma_b(n) phi dSigma_b
```

Here:

```text
Sigma:
  a Cauchy surface for the observer region.

n:
  future unit normal.

J_b:
  the source-derived physical adjoint/fundamental symmetry needed to turn the
  indefinite spinor bilinear into a Hermitian Hilbert pairing.

gamma_b(n):
  the section-pulled Clifford action of the normal.

internal metric:
  a positive Hermitian form on V_L direct_sum V_R, if one is source-selected.
```

This pairing is positive only under nontrivial conditions:

```text
1. h_b([f], [g]) = conjugate(h_b([g], [f])).
2. h_b([f], [f]) >= 0 after the equation/gauge/constraint/ghost quotient.
3. h_b([f], [f]) = 0 exactly for the declared null directions.
4. the quotient by Null_b is performed before completing the space.
5. D_phys^b is compatible with the current so h_b is independent of Sigma.
6. gauge or BRST directions are in the radical, not negative-norm survivors.
7. the chosen adjoint/current is source-derived, not selected to mimic the standard
   free Dirac vacuum.
```

The repo does not currently supply `J_b`, the conserved current, the full physical
domain, or the proof that the quotient removes every negative-norm direction.

### 3.2 Finite Gram Candidate

For the finite Pati-Salam seed, choose labels

```text
e^L_{a alpha},    a = 1..4, alpha = 1..2
e^R_{bar a dot alpha},    bar a = 1..4, dot alpha = 1..2
```

and set

```text
K_b^fin = span_C{e^L_{a alpha}} direct_sum span_C{e^R_{bar a dot alpha}}
        ~= C^8_L direct_sum C^8_R.
```

A conventional finite positive pairing is:

```text
h_b^fin(v, w) = v^* H_b w
H_b = diag(I_8, I_8)
```

or, with source data allowed:

```text
H_b =
  [ H_LL  H_LR ]
  [ H_RL  H_RR ],

H_b = H_b^*
H_b >= 0
rank(H_b after quotient) > 0
```

The identity matrix `diag(I_8, I_8)` is a valid mathematical control pairing. It is not
a GU derivation. It imports the standard compact Hermitian metrics on the Pati-Salam
representation labels and silently assumes that no physical negative or null directions
survive.

The positivity conditions for the finite seed are:

```text
H_raw = H_raw^*
Gauge_b^* H_raw Q_b = 0
EOM_b^* H_raw Q_b = 0
H_phys = Q_b^* H_raw Q_b
H_phys = H_phys^*
H_phys >= 0
rank(H_phys) > 0
```

where `Q_b` is the quotient/projection map to physical representatives. If a future
two-point or covariance matrix `Gamma_b` is added, the additional CAR positivity check
would be:

```text
Gamma_b = Gamma_b^*
0 <= Gamma_b <= H_phys
spec(H_phys^+ Gamma_b) subset [0,1] on the positive quotient
```

This file does not add `Gamma_b` or a vacuum. It only specifies the seed that would make
such a covariance meaningful.

## 4. Finite Seed Space `K_b` And What Would Make It Source-Derived

The finite seed space for this cycle is:

```text
K_b := K_b^fin = K_L^b direct_sum K_R^b

K_L^b ~= V_L = (4,2,1),       dim_C K_L^b = 8
K_R^b ~= V_R = (4bar,1,2),   dim_C K_R^b = 8

dim_C K_b = 16
```

This is the one-particle finite seed for a local CAR/quasifree route:

```text
A_b^fin = CAR(K_b, h_b^fin)
```

It is not yet the Alice/Bob density matrix. A density matrix on `H_A tensor H_B` would
be a later finite observer reduction of a positive state or covariance. The direct sum
`K_L^b direct_sum K_R^b` must not be silently replaced by a tensor-product Bell state.

`K_b` becomes source-derived only if the following are emitted with `gu-derived:`
provenance:

```text
1. source branch:
   exact operator, section, physical domain, constraints, and boundary/vacuum status.

2. mode selection:
   a source projector or extraction map
   P_fin^b: F_phys^b(O) -> K_b
   selecting the 8 left and 8 right modes.

3. quotient map:
   explicit map Q_b from raw representatives to physical representatives, including
   every gauge, constraint, ghost, and null direction removed.

4. Gram matrix:
   H_b,ij = h_b(e_i, e_j) computed from the source pairing, not set to the identity
   because that is convenient.

5. positivity proof:
   H_phys >= 0 on the quotient, with negative eigenvalues and residual nulls reported.

6. locality:
   support or localization data showing the left/right finite modes arise from the
   intended observer regions and do not build in nonlocal Alice/Bob correlations.

7. no target data:
   no Bell state, Pauli setting, standard free vacuum, Hadamard/Fock vacuum, or CHSH
   target value is used to choose the basis, Gram matrix, or quotient.
```

At present the repo supplies item 1 only conditionally and supplies the Pati-Salam
representation labels for item 2. It does not supply the source projector, quotient map,
Gram matrix, or positivity proof.

## 5. Failure Modes: Negative Norm, Gauge Leakage, Target-Fitted Vacuum, Nonlocal Observables

### Negative Norm

The seed fails if `H_phys` has a negative eigenvalue after the quotient:

```text
exists f in F_phys^b(O): h_b(f, f) < 0.
```

This is a hard failure for the CAR/GNS Hilbert route in this sector. It cannot be repaired
by declaring the negative direction unphysical after using it in a state extraction.

### Gauge Leakage

The seed fails or remains underdefined if gauge, ghost, or constraint directions are not
removed before positivity is claimed:

```text
h_b(gauge_direction, physical_field) != 0
```

or if the finite `K_b` contains charged/gauge directions while the claimed physical
observable algebra is supposed to be gauge invariant. Charged field algebras can be useful
intermediate objects, but a physical measurement claim must state the invariant
observable or superselection rule.

### Target-Fitted Vacuum

The seed fails as GU evidence if `h_b`, `Gamma_b`, `C_b`, `omega_b`, or `rho_AB` is chosen
to reproduce a known target:

```text
Bell state
Pauli CHSH optimum
standard free Dirac vacuum
Hadamard/Fock vacuum
Pati-Salam CPT ansatz
ordinary SM state data
chosen Barandes/Stinespring/CPTP channel
```

This is the target-fitted failure mode: the pairing or state is adjusted to match an
external quantum target and then relabeled as source-derived.

Those objects may be controls or comparators. They may not be the source of the GU
positive pairing or state.

### Nonlocal Observables

The seed fails as an observer-facing local QFT input if the finite left/right modes are
selected by global projections whose support cannot be assigned to local regions, or if
the Alice/Bob tensor split is inserted without a local algebra map:

```text
O_A spacelike O_B
A_b(O_A) and A_b(O_B) defined
graded local commutation verified
finite reduction respects the two local inclusions
```

Without this, a future CHSH value would test a nonlocal fixture, not a GU-derived local
measurement channel.

## 6. First Exact Obstruction

Within the conditional operator-spine branch, the first exact obstruction is:

```text
SourceDerivedPositivePairingOnQuotient(b)
```

This is the next object inside `PhysicalFieldComplexAndPositivePairingSeed(b)`. It must
emit:

```text
D_phys^b:
  section-pulled physical Pati-Salam left/right operator, including domains and
  lower-order terms relevant to adjoints and constraints.

Q_b:
  explicit quotient/projection map removing EOM, gauge, constraint, ghost, and null
  directions.

J_b or equivalent:
  source-derived physical adjoint/fundamental symmetry or conserved current.

h_b:
  Hermitian physical pairing before and after quotient.

H_phys:
  finite Gram matrix on K_b, computed from h_b and Q_b.

positivity proof:
  H_phys >= 0 and rank(H_phys) > 0, or a reported negative/null failure.

provenance:
  gu-derived:<operator/section/constraint/current/reference>
```

Why this is first:

```text
The repo can name a conditional D_phys^b by projecting the typed spine.
The repo can name K_b by using the Pati-Salam left/right labels.
But the repo cannot decide whether the quotient carries a positive Hermitian form.
Without that, C_b is not a positive contraction, omega_b is not a state, and GNS_b is
only imported operator-algebra plumbing.
```

Globally, if the typed operator spine is not accepted as branch data, then primary
`D_GU` closure is even earlier. This file conditions on the spine only to expose the next
obstruction after that assumption.

## 7. Impact For QFT State-Space Extraction

Cycle 1 remains blocked before a positive two-point function. This Cycle 2 seed narrows
the blocker:

```text
old blocker:
  PhysicalFieldComplexAndPositivePairingSeed(b)

new first exact internal blocker:
  SourceDerivedPositivePairingOnQuotient(b)
```

Consequences:

```text
1. A formal CAR algebra can be hosted on K_b^fin with an imported identity pairing.
   That is useful control plumbing, not QFT recovery.

2. A source-derived QFT state-space claim requires h_b to be positive on the quotient
   before any covariance C_b or two-point W_b is meaningful.

3. If h_b is derived but no covariance is derived, the repo would have a candidate
   one-particle state space but still no vacuum/state extraction.

4. If h_b is indefinite after quotient, this Pati-Salam left/right quasifree sector
   fails as a physical Hilbert/CAR seed.

5. If h_b is positive only because the standard finite Hermitian pairing was inserted,
   the status is import/control, not GU-derived positivity.
```

Therefore this artifact does not promote `QFTStateSpaceExtractionCertificate`,
`QFTStateExtractionCertificate`, or `OBS-CHSH`. It makes the next finite computation
small enough to be decisive.

## 8. Next Meaningful Finite Computation

The next computation should be a finite quotient-Gram audit, not another Bell fixture.

Minimal input:

```text
branch_id = QFT-SSX-PS-LR-QUASIFREE-v0
basis labels:
  e^L_{a alpha}, e^R_{bar a dot alpha}
provenance for each mode:
  gu-derived:<operator/section/projector/reference>
raw Gram matrix:
  H_raw,ij = h_raw(e_i, e_j)
quotient/projection matrix:
  Q_b
gauge/constraint/null representatives:
  G_b, C_bare_b, N_b
```

Finite checks:

```text
1. no provenance string contains control:, ansatz:, imported-vacuum:, free-vacuum:,
   Bell, Pauli, Hadamard, Fock, target, or CHSH.

2. H_raw = H_raw^*.

3. every listed gauge, EOM, ghost, and constraint direction pairs trivially with the
   physical quotient representatives.

4. H_phys = Q_b^* H_raw Q_b.

5. H_phys = H_phys^*.

6. eigenvalues(H_phys) >= -tolerance.

7. rank(H_phys) > 0 after removing numerical nulls.

8. all surviving basis labels still map to the declared Pati-Salam left/right block.
```

If and only if this passes, the next finite covariance check can be added:

```text
Gamma_b = Gamma_b^*
Gamma_b >= 0
H_phys - Gamma_b >= 0
spec(H_phys^+ Gamma_b) subset [0,1]
```

Expected decisions:

| finite result | decision |
|---|---|
| no source projector or no `H_raw` | blocked at source-derived pairing |
| `H_phys` indefinite | fail this seed sector |
| `H_phys >= 0` but rank zero | quotient erased the seed |
| `H_phys >= 0` with clean provenance | promote positive seed, still no state until covariance exists |
| `H_phys = I_16` with no source derivation | import/control positive pairing |
| `Gamma_b` copied from Bell/free-vacuum data | target-smuggling rollback |

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE2_QFT_PHYSICAL_FIELD_POSITIVE_PAIRING_SEED",
  "version": "2026-06-24",
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "seed_id": "PhysicalFieldComplexAndPositivePairingSeed",
  "verdict": "UNDERDEFINED_POSITIVITY_IMPORTED_IF_STANDARD_PAIRING_IS_USED",
  "status": "underdefined",
  "qft_recovered": false,
  "not_a_qft_recovery_claim": true,
  "can_produce_positive_pairing_from_current_repo": false,
  "positive_pairing_status": "not_source_derived; standard_positive_pairing_would_be_imported_control",
  "positivity_not_assumed_silently": true,
  "candidate_physical_complex": {
    "D_phys_b": "Pi_phys Pi_PS s0_pullback_D_roll Pi_PS Pi_phys",
    "D_phys_b_display": "D_phys^b := Pi_phys Pi_PS s_0^*(D_roll) Pi_PS Pi_phys",
    "status": "conditional_specification_not_constructed",
    "depends_on": [
      "operator_spine_conditional",
      "section_s0",
      "Pati_Salam_projector_Pi_PS",
      "physical_constraint_projector_Pi_phys",
      "primary_D_GU_closure_if_the_spine_is_not_assumed"
    ],
    "raw_space": "F_raw^b(O)=Gamma_c(O,E_PS^b)",
    "finite_internal_fibers": {
      "V_L": "(4,2,1)",
      "V_R": "(4bar,1,2)",
      "dim_C_V_L": 8,
      "dim_C_V_R": 8
    }
  },
  "quotient": {
    "formula": "F_phys^b(O)=F_raw^b(O)/(EOM_b+Gauge_b+Constraint_b+Ghost_b+Null_b)",
    "status": "specified_not_executed",
    "must_remove": [
      "equations_of_motion",
      "gauge_or_BRST_exact_directions",
      "physical_constraints",
      "ghost_or_negative_metric_auxiliaries",
      "radical_of_h_b"
    ],
    "descent_conditions": [
      "h_b(gauge_direction,physical_field)=0",
      "h_b(eom_direction,physical_field)=0",
      "h_b(null_direction,physical_field)=0",
      "h_b_descends_to_F_phys_b"
    ]
  },
  "candidate_positive_pairing": {
    "h_b": "Hermitian_physical_pairing_on_F_phys_b_or_finite_Gram_pairing_on_K_b",
    "continuum_candidate": "integral_Sigma psi_dagger J_b gamma_b(n) phi dSigma_b",
    "finite_candidate": "h_b_fin(v,w)=v_star H_b w",
    "control_Gram": "H_b=diag(I_8,I_8)",
    "control_Gram_status": "imported_positive_pairing_not_GU_derived",
    "required_source_data": [
      "physical_adjoint_or_fundamental_symmetry_J_b",
      "conserved_current_or_equivalent_Gram_rule",
      "source_internal_Hermitian_form",
      "quotient_map_Q_b",
      "proof_no_negative_norm_survivors"
    ],
    "positivity_conditions": [
      "h_b(f,g)=conjugate(h_b(g,f))",
      "h_b(f,f)>=0_on_quotient",
      "Null_h_b_removed_before_completion",
      "H_phys=Q_b_star_H_raw_Q_b",
      "H_phys=H_phys_star",
      "H_phys>=0",
      "rank_H_phys>0"
    ]
  },
  "finite_seed_space": {
    "K_b": "K_b^fin=K_L^b direct_sum K_R^b",
    "K_L_b": "V_L=(4,2,1)",
    "K_R_b": "V_R=(4bar,1,2)",
    "dimension_complex": 16,
    "basis_pattern": [
      "e^L_{a alpha}, a=1..4, alpha=1..2",
      "e^R_{bar a dot alpha}, bar_a=1..4, dot_alpha=1..2"
    ],
    "algebra_route": "A_b^fin=CAR(K_b,h_b^fin)",
    "not_yet": [
      "rho_AB",
      "omega_b",
      "C_b",
      "W_b",
      "GU_admissible_observables"
    ],
    "source_derived_requirements": [
      "gu_derived_source_branch",
      "gu_derived_mode_projector_P_fin_b",
      "explicit_quotient_map_Q_b",
      "Gram_matrix_H_b_computed_from_h_b",
      "positivity_proof_H_phys_ge_0",
      "local_support_or_local_algebra_map",
      "no_target_data"
    ]
  },
  "first_exact_obstruction": {
    "id": "SourceDerivedPositivePairingOnQuotient",
    "inside": "PhysicalFieldComplexAndPositivePairingSeed",
    "why_first_within_conditional_spine": "D_phys_b_and_K_b_can_be_named_conditionally_but_the_repo_cannot_compute_or_prove_a_positive_Hermitian_pairing_on_the_quotient",
    "must_emit": [
      "D_phys_b",
      "Q_b",
      "J_b_or_conserved_current",
      "h_b",
      "H_phys",
      "proof_H_phys_positive_semidefinite_and_nonzero_rank",
      "gu_derived_provenance"
    ]
  },
  "failure_modes": [
    "negative_norm_after_quotient",
    "gauge_leakage",
    "target_fitted_vacuum_or_covariance",
    "nonlocal_observables_or_nonlocal_finite_modes"
  ],
  "forbidden_imports": [
    "claiming_QFT_recovery_from_seed_shell",
    "using_Pati_Salam_labels_as_a_positive_pairing",
    "setting_H_b_to_identity_as_GU_derivation",
    "imported_free_Dirac_vacuum",
    "imported_Hadamard_or_Fock_vacuum",
    "copying_Bell_state_into_GU_slot",
    "using_Pauli_controls_as_GU_observables",
    "target_fitted_CHSH_covariance",
    "chosen_Barandes_Stinespring_or_CPTP_channel_as_GU_source"
  ],
  "rollback_conditions": [
    "rollback_primary_operator_mismatch",
    "rollback_missing_physical_quotient",
    "rollback_missing_source_adjoint_or_current",
    "rollback_indefinite_H_phys",
    "rollback_zero_rank_after_quotient",
    "rollback_identity_Gram_imported_as_derivation",
    "rollback_imported_vacuum_or_target_state",
    "rollback_gauge_leakage",
    "rollback_nonlocal_finite_reduction"
  ],
  "impact": {
    "qft_state_space_extraction": "still_blocked_before_source_derived_positive_pairing",
    "positive_two_point": "cannot_be_defined_as_physical_positive_contraction_until_h_b_and_K_b_are_source_derived",
    "obs_chsh": "remains_parked_until_state_and_observables_are_source_derived"
  },
  "next_meaningful_finite_computation": {
    "id": "finite_source_quotient_Gram_audit_for_K_b",
    "input_required": [
      "mode_basis_with_gu_derived_provenance",
      "H_raw",
      "Q_b",
      "gauge_constraint_ghost_null_representatives"
    ],
    "checks": [
      "no_forbidden_provenance",
      "H_raw_equals_H_raw_star",
      "quotient_directions_pair_trivially",
      "H_phys_equals_Q_star_H_raw_Q",
      "H_phys_equals_H_phys_star",
      "eigenvalues_H_phys_ge_minus_tolerance",
      "rank_H_phys_positive",
      "surviving_labels_match_Pati_Salam_LR_block"
    ],
    "covariance_check_after_seed_only": [
      "Gamma_b_equals_Gamma_b_star",
      "Gamma_b_ge_0",
      "H_phys_minus_Gamma_b_ge_0",
      "spec_H_phys_plus_Gamma_b_subset_0_1"
    ]
  }
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `lab/process/runbooks/five-lane-frontier-run.md`
- `explorations/cycle-gates-and-audits/cycle1-qft-positive-two-point-certificate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/mission-a-qft-state-space-extraction-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/gu-measurement-channel-chsh-gate-2026-06-24.md`
