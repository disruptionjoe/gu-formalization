---
title: "Mission A QFT State-Space Extraction Construction Attempt"
date: "2026-06-24"
status: exploration/construction_attempt
doc_type: qft_state_space_extraction_certificate_attempt
verdict: "CONDITIONAL_CONSTRUCTION_ATTEMPT_BLOCKED_AT_POSITIVE_PHYSICAL_TWO_POINT"
owned_path: "explorations/cycle-gates-and-audits/mission-a-qft-state-space-extraction-2026-06-24.md"
optional_audit:
  - "tests/mission_a_qft_state_space_extraction_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "lab/process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/vz-evasion/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/observer-finality-physical-forcing-gate-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/gu-measurement-channel-chsh-gate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
---

# Mission A QFT State-Space Extraction Construction Attempt

## 1. Verdict

This lane makes the first constructive `QFTStateSpaceExtractionCertificate` attempt for
the smallest defensible source sector I can isolate from the current repo:

```text
QFT-SSX-PS-LR-QUASIFREE-v0:
  fixed operator-spine source sector
  + section-pulled Pati-Salam left/right fermion proxy
  + local CAR algebra/GNS route
  + source-derived two-point/quasifree state slot
  + finite Alice/Bob reduction target
```

The result is **not closed** and is **not a QFT recovery theorem**. The constructive gain
is that the missing object is no longer only named globally. The attempt identifies the
first source-derived state-space object that must exist and gives the pipeline that would
turn it into a local algebra, GNS/Hilbert representation, finite state, observables, and
consistency gates.

Current decision:

```text
QFTStateSpaceExtractionCertificate:
  conditional construction specified
  not source-derived yet

minimal sector:
  Pati-Salam left/right quasifree fermion sector
  useful because one two-point kernel would feed GNS, rho_AB, CHSH, locality,
  unitarity, spin-statistics, and anomaly checks

first exact obstruction:
  PositivePhysicalTwoPointCertificate for the section-pulled physical field complex

rollback:
  if the source cannot produce a positive physical pairing and two-point/quasifree
  covariance without importing the target state, this sector demotes to formal CAR
  plumbing or ansatz/control only
```

The construction attempt uses the Mission A posture: assume GU is substantially correct
as a working hypothesis and ask what quantum state-space object must exist. It still keeps
imports, assumptions, failure conditions, and rollback language explicit.

## 2. If GU Is Correct, What QFT State-Space Object Must Exist

If GU is correct in the source-geometry sense, then for at least one source branch `b`
there must be a source-to-quantum-shadow extraction:

```text
R_QFT^b:
  (I_GU^b, D_GU^b, S_GU^b, section s, constraints, boundary/vacuum data)
  ->
  (O -> A_b(O), omega_b, GNS_b, dynamics_b, observables_b, anomaly_shadow_b)
```

For the minimal fermionic sector selected here, the output must have the following form.

| object | required content | why GU needs it |
|---|---|---|
| `E_phys^b` | section-pulled physical field bundle or complex after gauge/constraint quotient | gives the actual observer-facing field degrees of freedom, not just representation labels |
| `K_b(O)` | local one-particle test/solution space for region `O`, with nulls removed | gives the domain on which the algebra is built |
| `h_b` | positive Hermitian physical pairing on `K_b` | prevents negative-norm or unphysical sectors from becoming states |
| `A_b(O)` | local `*`-algebra, here provisionally a CAR algebra for the fermion branch | gives the state-space object before a vacuum is chosen |
| `omega_b` | positive normalized state on the local/net algebra | gives probabilities and a GNS representation |
| `GNS_b` | `(H_omega, pi_omega, Omega_omega)` | turns the algebraic state into a Hilbert representation |
| `W_b` or `C_b` | source-derived two-point kernel or quasifree covariance | determines the minimal free/quasifree state |
| `alpha_t` | `*`-automorphism dynamics or a self-adjoint generator on the physical Hilbert space | supplies unitarity/state preservation |
| `Obs_b` | admissible local self-adjoint observables/effects | supplies physical readouts, not only Pauli controls |
| `ShadowAnom_b` | full list of observer-facing modes and anomaly result | blocks anomalous extra modes |

For a quasifree CAR route, the minimal state data are:

```text
K_b                        positive one-particle space
0 <= C_b <= 1              source-derived covariance operator
omega_b(a^*(f) a(g)) = h_b(f, C_b g)
omega_b(odd monomials) = 0
omega_b(higher even monomials) = Wick/Pfaffian rule from C_b
GNS(omega_b) = (H_omega, pi_omega, Omega_omega)
```

For the observer/CHSH reduction, the same state must also produce:

```text
H_A = V_L = (4,2,1) proxy space after physical reduction
H_B = V_R = (4bar,1,2) proxy space after physical reduction
K_AB or rho_AB             finite covariance or density matrix
A, A' in End(H_A)          GU-admissible Alice observables
B, B' in End(H_B)          GU-admissible Bob observables
```

Representation labels alone do not supply any of these state objects. If GU is correct,
the missing object is not "quantize the 4D metric first." It is a positive
source-derived quantum shadow for the observer-facing degrees of freedom.

## 3. Candidate Minimal Sector And Why It Is The Smallest Useful One

### Sector Definition

The candidate sector is:

```text
sector_id:
  QFT-SSX-PS-LR-QUASIFREE-v0

source branch:
  operator_spine conditional branch from the primary interface contract

operator input:
  D_lambda with first-order Phi_d = Phi_2 o d_A and lambda_d != 0

observer localization:
  one fixed section s: X -> Y and one small observer region O subset X

field content:
  section-pulled Pati-Salam left/right fermion proxy
  V_L = (4,2,1)
  V_R = (4bar,1,2)

state ansatz form:
  quasifree/two-point state, not an inserted Bell state

algebra route:
  local CAR net or local CAR algebra family O -> A_b(O)

finite target:
  K_AB or rho_AB on H_A tensor H_B for the existing CHSH gate
```

### Why This Sector Is Smallest

This sector is smaller than full QFT recovery because it avoids the full interacting
Standard Model, the Higgs potential, exact generation count, full SM gauge quotient, and
metric quantization. It asks only for one fixed branch, one physical fermion complex, one
positive local algebra/state route, and one two-point/quasifree source.

It is still useful because one successful two-point object would feed every downstream
gate that is currently parked:

| downstream gate | what the sector would emit |
|---|---|
| `QFTStateSpaceExtractionCertificate` | `K_b`, `h_b`, `A_b(O)`, and GNS/Fock route |
| `QFTStateExtractionCertificate` | `omega_b`, `W_b`, or `C_b` |
| `OBS-CHSH` | `K_AB` or `rho_AB`, plus finite reduction data |
| `ObservableAdmissibilityCertificate` | local algebra elements or finite effects selected by a measurement rule |
| positivity | `h_b >= 0`, `0 <= C_b <= 1`, finite `rho_AB >= 0`, `Tr rho_AB = 1` |
| unitarity | self-adjoint generator or state-preserving `*`-automorphism group |
| locality | graded local commutativity and causal propagation |
| anomaly | list of every observer-facing mode produced by the same shadow |

The main risk is clear: CAR, quasifree GNS, and finite Pati-Salam proxy methods are
standard QFT imports unless GU derives the physical field complex, positive pairing,
statistics choice, covariance, and measurement rule from the source branch.

## 4. Proposed Extraction Pipeline

### 4.1 Field Complex

Start with the fixed source branch:

```text
b =
  (I_GU, D_lambda, lambda_d != 0, section s, connection/background A_0,
   boundary/vacuum convention, gauge constraints)
```

The needed physical field complex is:

```text
F_phys^b(O):
  compactly supported section-pulled fields over O
  -> quotient by equations of motion
  -> quotient by gauge/constraint/ghost nulls
  -> Pati-Salam left/right finite branch if the selector is active
```

Current label:

```text
Construction: field-complex shape specified.
Repo source: typed carrier, section map, operator-spine proposal, Pati-Salam branch.
Blocked: primary D_GU closure, gauge quotient, physical domains, ghost/null removal.
```

### 4.2 Algebra/Hilbert/GNS

If `F_phys^b` carries a positive physical pairing `h_b`, define:

```text
K_b(O) = completion(F_phys^b(O) / null(h_b))
A_b(O) = CAR(K_b(O), h_b)
```

For `O_1 subset O_2`, the inclusion of test spaces should induce:

```text
A_b(O_1) -> A_b(O_2)
```

For spacelike separated regions, the required locality condition is graded:

```text
[A_b(O_1), A_b(O_2)]_graded = 0
```

Given a positive normalized state `omega_b`, the GNS construction would emit:

```text
GNS_b = (H_omega, pi_omega, Omega_omega)
```

Current label:

```text
Conditional construction: CAR/GNS route is mathematically standard if K_b, h_b,
and omega_b exist.
Import: standard CAR and GNS theorems are external QFT/operator-algebra machinery.
Blocked as GU-derived: K_b, h_b, and omega_b are not produced by repo source data.
```

### 4.3 State/Two-Point

The minimal quasifree state object is:

```text
PositivePhysicalTwoPointCertificate(b):
  D_phys^b
  K_b
  h_b
  C_b with 0 <= C_b <= 1
  W_b(f,g) = h_b(f, C_b g)
  source_provenance = gu-derived:<operator/section/vacuum/reference>
  positivity/normalization checks
  locality and microlocal/causal compatibility checks
```

The two-point kernel must be a source output. It may not be:

```text
Bell control copied into the GU slot
Pati-Salam/CPT ansatz state relabeled as derived
generic vacuum entanglement with no finite reduction map
ordinary SM free vacuum imported and cited as GU evidence
```

Current label:

```text
Construction: exact certificate shape specified.
Blocked: no source-derived C_b, W_b, vacuum, spectral projection, or Hadamard state.
Import if used today: any standard free Dirac vacuum or externally chosen quasifree
covariance.
```

### 4.4 Finite Observer Reduction

The finite reduction must map the local algebra state to the existing Alice/Bob proxy:

```text
R_AB^b:
  (A_b(O_A), A_b(O_B), omega_b)
  ->
  (H_A, H_B, K_AB or rho_AB)
```

It must specify:

```text
H_A, H_B
finite Gram matrices
basis and smearing choices
direct-sum-to-tensor-product rule
color/isospin contraction
CPT/left-right status
rho_AB role = "gu_derived"
rho_AB provenance starts "gu-derived:"
```

Current label:

```text
Construction: finite target and checks are known from the CHSH gate.
Repo source: Pati-Salam proxy dimensions and executable controls.
Blocked: no GU finite reduction map and no GU-derived rho_AB.
```

### 4.5 Observables

The observable certificate must produce local self-adjoint elements or finite effects:

```text
Obs_b:
  A, A' in End(H_A)
  B, B' in End(H_B)
  provenance = gu-admissible:<measurement-postulate-reference>
```

Checks:

```text
self-adjoint or valid effect
correct spectrum, especially +/-1 if used for CHSH
Alice/Bob local commutation
same-party noncommutation physically justified
no postselection
no future-setting dependence
readout meaning tied to source/observer rules
```

Current label:

```text
Construction: observable gate shape specified.
Repo source: Pauli-style finite controls exist.
Blocked: GU measurement postulate and GU-admissible observables are missing.
Import/control if used today: existing Pauli CHSH settings.
```

### 4.6 Positivity, Unitarity, Locality, And Anomaly Gates

The candidate sector closes only if these gates pass:

| gate | condition | current status |
|---|---|---|
| positivity | `h_b >= 0`, `0 <= C_b <= 1`, `omega_b(1)=1`, finite `rho_AB >= 0`, `Tr rho_AB = 1` | blocked |
| unitarity | self-adjoint generator on physical states, or `*`-automorphism dynamics preserving the state class | missing |
| locality | graded local commutativity plus causal propagation in the observer cone | conditional support only from VZ typed-spine principal symbol |
| spin-statistics | CAR choice follows from GU spin/locality/positivity, not convention alone | missing/imported |
| anomaly | all observer-facing modes listed and perturbative/global/cobordism anomalies checked | open; ordinary SM cancellation is relative only |
| provenance | no Bell, Pauli, SM, or finite Connes target data used as hidden source input | active guardrail, not a proof |

## 5. What Can Be Built From Repo Sources Now Versus Imported Or Blocked

| object | current classification | decision-grade statement |
|---|---|---|
| source carrier `Y`, `P`, `S`, `Sp(64)`, section slot | Construction from repo source | typed by the primary interface contract |
| `D_lambda` operator-spine principal block | Conditional construction from repo source | usable only if primary `D_GU` contains `Phi_d` with `lambda_d != 0` |
| VZ causal principal-symbol support | Conditional construction from repo source | helps locality/causality only; not a state-space or unitarity proof |
| Pati-Salam branch `V_L`, `V_R` | Construction from repo source as representation branch | labels finite spaces but does not define a state |
| local CAR algebra schema | Import plus conditional construction | standard if physical `K_b,h_b` exist; not GU-derived until source supplies them |
| GNS construction | Import plus conditional construction | standard for a positive state; no source-derived `omega_b` yet |
| quasifree covariance `C_b` or two-point `W_b` | Blocked | this is the first exact missing object for the candidate sector |
| finite `rho_AB` | Blocked | current violating states are controls or ansatz, not GU outputs |
| Pauli/CHSH observables | Control/import | good test plumbing; not GU-admissible observables |
| positivity checks | Construction-ready | finite and algebraic checks are specified but have no live GU state input |
| unitarity | Blocked | no self-adjoint physical generator or state-preserving dynamics supplied |
| locality | Conditional/blocked | VZ supports a principal-symbol cone under operator-spine assumptions; microcausality for the live net is missing |
| anomaly | Open/relative | ordinary SM cancellation works only after exact ordinary shadow is supplied |
| full SM gauge/Higgs/generation packet | Blocked/open | Pati-Salam branch exists; selector, Higgs emergence, and generation count remain open |

Thus the current repo can build a precise **certificate shell** and a **conditional
operator-algebra construction route**. It cannot yet build a source-derived
Hilbert/GNS/local algebra state object.

## 6. First Exact Obstruction Or Missing Proof Object

The first exact obstruction for this construction attempt is:

```text
PositivePhysicalTwoPointCertificate(b)
```

This object must include:

```text
1. D_phys^b:
     the section-pulled, gauge-fixed physical operator or equation in the chosen sector.

2. F_phys^b and K_b:
     physical test/solution spaces after equation, gauge, ghost, and null quotients.

3. h_b:
     positive Hermitian pairing on the physical one-particle space.

4. C_b or W_b:
     source-derived covariance/two-point kernel.

5. positivity:
     0 <= C_b <= 1 for the CAR quasifree route, or equivalent algebraic positivity.

6. provenance:
     gu-derived:<operator/section/vacuum/reference>, with no Bell/SM/Pauli target input.

7. locality/causal compatibility:
     graded microcausality and compatibility with the observer cone.

8. finite reduction:
     K_AB or rho_AB with Hermitian, PSD, trace-one checks when CHSH is claimed.
```

Why this is the first obstruction:

```text
Without D_phys^b and h_b, the CAR algebra is only imported formalism over a proxy
space. Without C_b or W_b, there is no positive state omega_b and no GNS/Hilbert
state-space extraction. Without finite reduction, there is no rho_AB for the
observer/CHSH gate.
```

This obstruction is constructive rather than merely negative. It says exactly what object
must be computed next and exactly how it can fail.

Failure conditions:

```text
no positive physical pairing after constraints
no Green-hyperbolic or causally well-posed physical operator in the chosen sector
only imported/free-vacuum covariance is available
two-point kernel is not positive or not normalized
state depends on Bell/CHSH target settings
finite reduction is not tensor-factorizable into Alice/Bob spaces
derived rho_AB is separable or gives CHSH <= 2 for all admissible observables
extra observer-facing modes have uncanceled anomalies
```

## 7. Constructive Next Computation

The next computation should be narrow and falsifiable:

```text
Compute or refute PositivePhysicalTwoPointCertificate
for QFT-SSX-PS-LR-QUASIFREE-v0.
```

Concrete work packet:

1. Fix the branch data:

   ```text
   branch = operator_spine
   lambda_d = 1 unless the primary operator changes it
   section = one explicit local observer section s_0
   background = one explicit A_0 and boundary/vacuum convention
   region = one small observer causal diamond O
   ```

2. Pull the operator to the section and isolate the physical left/right fermion block:

   ```text
   D_phys,s0 on E_L plus E_R
   E_L fiber = (4,2,1)
   E_R fiber = (4bar,1,2)
   ```

3. Prove or refute a positive physical pairing:

   ```text
   h_b(f,g) >= 0 after equation/gauge/null quotient
   no negative-norm survivor
   ```

4. Build a candidate two-point kernel from source data, not from a Bell target:

   ```text
   W_b(f,g) or C_b
   check Hermitian/quasifree positivity
   check 0 <= C_b <= 1 for CAR
   check covariance under the allowed source symmetries
   ```

5. Reduce to the finite Alice/Bob proxy:

   ```text
   choose source-defined local modes f_i in H_A and g_j in H_B
   compute K_AB
   emit rho_AB only if the finite state is Hermitian, PSD, trace one, and source-derived
   ```

6. Only after the state exists, derive or reject admissible observables:

   ```text
   if observables are only Pauli controls, keep status control/import
   if GU supplies gu-admissible observables, run the existing CHSH gate unchanged
   ```

7. Run the consistency gates:

   ```text
   positivity
   unitarity or state-preserving dynamics
   graded locality/NAC
   spin-statistics source justification
   anomaly shadow for all produced modes
   ```

Expected honest outcomes:

| computation result | decision |
|---|---|
| source-derived positive `C_b` and local algebra state exist | promote this sector to conditional QFT state-space evidence, still not full QFT recovery |
| only standard free Dirac/quasifree vacuum can be imported | classify as import/control plumbing |
| no positive pairing after constraints | fail this sector |
| positive state exists but finite reduction is separable/classical | fail physical CHSH forcing for this sector |
| positive state exists but extra anomalous modes survive | block or fail anomaly shadow |

## 8. Claim Certificate Table

| claim | current certificate | construction supplied here | import labels | first missing object | rollback condition |
|---|---|---|---|---|---|
| `QFTStateSpaceExtractionCertificate` | conditional construction attempt, not closed | local CAR/GNS state-space route for `PS-LR-QUASIFREE-v0` | standard CAR, GNS, quasifree theorems unless GU derives them | `PositivePhysicalTwoPointCertificate(b)` plus physical field complex | no positive `K_b,h_b,C_b` from source data |
| `PS-LR-QUASIFREE-v0` | smallest useful candidate sector | fixed operator-spine, Pati-Salam left/right branch, finite observer target | CAR/statistics and finite proxy are imported/control until derived | source-derived two-point kernel and finite reduction | covariance copied from Bell/free-vacuum target or finite reduction not source-defined |
| `PhysicalFieldComplexCertificate` | partial/blocked | field-complex shape and quotient obligations | standard gauge/BRST language if used before GU supplies it | `D_phys^b`, domains, gauge quotient, ghost/null ledger | negative norm, unconstrained gauge sector, or primary operator mismatch |
| `QFTStateExtractionCertificate` | blocked | quasifree state formula once `C_b` exists | external vacuum or Hadamard state if inserted | `C_b` or `W_b` with `gu-derived:` provenance | state not positive, not normalized, or target-fitted |
| `ObservableAdmissibilityCertificate` | blocked | finite/local observable check shape | current Pauli settings are controls | GU measurement postulate | observables are not source-admissible or hide postselection |
| `LocalityCausalityCertificate` | conditional/blocked | graded locality requirement and VZ dependency named | AQFT locality theorem if imported | microcausality for the live net and NAC for live settings | VZ operator assumption fails or local commutation fails |
| `UnitarityCertificate` | missing | self-adjoint or `*`-automorphism requirement named | standard evolution theorem if imported | physical generator/dynamics preserving `omega_b` | nonunitary evolution or non-preserved state class |
| `SpinStatisticsCertificate` | missing/imported | CAR route makes the needed statistic explicit | CAR choice is imported until GU derives it | source spin-statistics theorem | wrong statistics or spin-statistics hypotheses fail |
| `AnomalyShadowCertificate` | open/relative | anomaly mode-list requirement attached to the same sector | ordinary SM anomaly formulas only after exact shadow | full observer-facing mode list and anomaly computation | extra anomalous mode survives or ordinary SM shadow is assumed |
| `OBS-CHSH` | parked | route to `rho_AB` named | Bell/Pati-Salam ansatz and Pauli controls remain controls | `rho_AB` plus `gu-admissible` observables | derived state/settings give no violation or violation comes from ansatz |

## Machine-Readable Summary

```json
{
  "artifact": "MISSION_A_QFT_STATE_SPACE_EXTRACTION",
  "version": "2026-06-24",
  "verdict": "CONDITIONAL_CONSTRUCTION_ATTEMPT_BLOCKED_AT_POSITIVE_PHYSICAL_TWO_POINT",
  "qft_recovered": false,
  "not_a_qft_recovery_theorem": true,
  "primary_certificate": "QFTStateSpaceExtractionCertificate",
  "minimal_sector": {
    "id": "QFT-SSX-PS-LR-QUASIFREE-v0",
    "source_branch": "operator_spine_conditional",
    "operator_condition": "D_lambda_contains_Phi_d_with_lambda_d_nonzero",
    "field_proxy": ["V_L=(4,2,1)", "V_R=(4bar,1,2)"],
    "algebra_route": "local_CAR_net_or_local_CAR_algebra",
    "state_route": "two_point_or_quasifree_covariance",
    "finite_target": "K_AB_or_rho_AB_for_existing_CHSH_gate",
    "status": "conditional_construction_blocked"
  },
  "construction_labels": {
    "construction_from_repo_now": [
      "typed_source_carrier",
      "section_slot",
      "operator_spine_principal_block_conditional",
      "Pati_Salam_left_right_representation_proxy",
      "certificate_pipeline"
    ],
    "imports_if_used_now": [
      "standard_CAR_algebra_theorem",
      "standard_GNS_theorem",
      "standard_quasifree_state_theorem",
      "external_free_Dirac_or_Hadamard_vacuum",
      "Pauli_CHSH_control_observables"
    ],
    "blocked_as_gu_derived": [
      "D_phys_section_pulled_operator",
      "physical_field_complex",
      "positive_pairing_h_b",
      "source_derived_covariance_C_b",
      "source_derived_two_point_W_b",
      "finite_rho_AB",
      "gu_admissible_observables",
      "unitary_or_state_preserving_dynamics",
      "full_anomaly_shadow"
    ]
  },
  "state_space_object_required_if_gu_correct": {
    "local_algebra": "O_to_A_b_O",
    "one_particle_space": "K_b",
    "positive_pairing": "h_b",
    "state": "omega_b",
    "two_point": "W_b",
    "quasifree_covariance": "C_b",
    "gns": ["H_omega", "pi_omega", "Omega_omega"],
    "dynamics": "alpha_t_or_self_adjoint_generator",
    "observables": "Obs_b",
    "anomaly_shadow": "ShadowAnom_b"
  },
  "gates": [
    {
      "id": "positivity",
      "required": ["h_b_positive", "zero_le_C_b_le_one", "omega_positive_normalized", "rho_AB_psd_trace_one"],
      "status": "blocked"
    },
    {
      "id": "unitarity",
      "required": ["self_adjoint_generator_or_star_automorphism", "state_class_preserved"],
      "status": "missing"
    },
    {
      "id": "locality",
      "required": ["graded_microcausality", "NAC_for_live_settings", "causal_cone_compatibility"],
      "status": "conditional_blocked"
    },
    {
      "id": "anomaly",
      "required": ["all_observer_modes_listed", "perturbative_global_cobordism_checks", "extra_mode_policy"],
      "status": "open"
    },
    {
      "id": "observables",
      "required": ["gu_admissible_measurement_rule", "self_adjoint_or_effects", "local_readout_provenance"],
      "status": "blocked"
    }
  ],
  "first_exact_obstruction": {
    "id": "PositivePhysicalTwoPointCertificate",
    "requires": [
      "D_phys_b",
      "F_phys_b",
      "K_b",
      "h_b",
      "C_b_or_W_b",
      "positivity",
      "source_provenance",
      "locality_causal_compatibility",
      "finite_reduction"
    ],
    "why_first": "without_positive_pairing_and_two_point_state_the_CAR_GNS_route_is_only_imported_formalism"
  },
  "claim_certificates": [
    {
      "claim": "QFTStateSpaceExtractionCertificate",
      "status": "conditional_construction_attempt_blocked",
      "proof_grade": "construction_attempt",
      "missing": ["PositivePhysicalTwoPointCertificate", "PhysicalFieldComplexCertificate"],
      "rollback": "no_positive_K_h_C_from_source_data"
    },
    {
      "claim": "QFTStateExtractionCertificate",
      "status": "blocked",
      "proof_grade": "specified_missing_object",
      "missing": ["source_derived_C_b_or_W_b", "omega_b"],
      "rollback": "state_imported_target_fitted_nonpositive_or_not_normalized"
    },
    {
      "claim": "ObservableAdmissibilityCertificate",
      "status": "blocked",
      "proof_grade": "specified_missing_object",
      "missing": ["GU_measurement_postulate", "gu_admissible_local_observables"],
      "rollback": "Pauli_controls_or_postselected_observables_used_as_GU"
    },
    {
      "claim": "UnitarityCertificate",
      "status": "missing",
      "proof_grade": "not_constructed",
      "missing": ["self_adjoint_generator_or_star_automorphism"],
      "rollback": "nonunitary_or_state_not_preserved"
    },
    {
      "claim": "AnomalyShadowCertificate",
      "status": "open",
      "proof_grade": "relative_only",
      "missing": ["full_observer_mode_list", "extra_mode_anomaly_checks"],
      "rollback": "extra_anomalous_observer_mode_survives"
    },
    {
      "claim": "OBS-CHSH",
      "status": "parked",
      "proof_grade": "executable_controls_only",
      "missing": ["rho_AB", "gu_admissible_observables"],
      "rollback": "derived_state_separable_or_violation_only_from_ansatz"
    }
  ],
  "forbidden_promotions": [
    "claiming_QFT_recovery_from_certificate_shell",
    "treating_Pati_Salam_labels_as_a_state",
    "copying_Bell_state_into_GU_slot",
    "treating_Pauli_controls_as_GU_admissible_observables",
    "using_VZ_principal_symbol_as_unitarity_or_state_extraction",
    "using_ordinary_SM_anomaly_cancellation_as_full_GU_anomaly_shadow",
    "importing_standard_free_vacuum_as_GU_derived"
  ],
  "next_computation": {
    "id": "compute_or_refute_PositivePhysicalTwoPointCertificate_for_QFT_SSX_PS_LR_QUASIFREE_v0",
    "steps": [
      "fix_operator_spine_branch_section_background_region",
      "derive_D_phys_section_pulled_left_right_block",
      "prove_or_refute_positive_pairing_h_b",
      "compute_source_derived_C_b_or_W_b",
      "reduce_to_K_AB_or_rho_AB",
      "derive_or_reject_gu_admissible_observables",
      "run_positivity_unitarity_locality_anomaly_gates"
    ]
  }
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `lab/process/runbooks/five-lane-frontier-run.md`
- `explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md`
- `explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
- `explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md`
- `explorations/vz-evasion/vz-proof-grade-closure-attempt-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-physical-forcing-gate-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/gu-measurement-channel-chsh-gate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md`
