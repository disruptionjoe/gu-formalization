---
title: "Hourly 20260625 1503 Cycle 1 QFT Local Gauge Action Groupoid"
date: "2026-06-25"
run_id: "hourly-20260625-1503"
cycle: 1
lane: 5
doc_type: qft_local_gauge_action_groupoid
artifact_id: "LocalGaugeActionGroupoidOnObservedRawGUFields_V1"
verdict: "UNDERDEFINED_CANDIDATE_PACKET_DRAFTED_REPO_SOURCE_OBJECTS_MISSING_NO_GENERATOR_PROMOTED"
owned_path: "explorations/hourly-20260625-1503-cycle1-qft-local-gauge-action-groupoid.md"
companion_audit: "tests/hourly_20260625_1503_cycle1_qft_local_gauge_action_groupoid_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "process/runbooks/three-cycle-fifteen-hole-run.md"
  - "explorations/hourly-20260625-1302-cycle3-next-frontier-dependency-dag.md"
  - "explorations/hourly-20260625-1302-cycle2-qft-gauge-action-restriction-stability-gate.md"
  - "explorations/hourly-20260625-1302-cycle1-qft-congruence-generators.md"
  - "explorations/sc1-oq3-gauge-equivariance-2026-06-23.md"
  - "explorations/type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md"
  - "explorations/dd1-distortion-distinct-canon-sharpen-2026-06-23.md"
  - "explorations/qft-shadow-extraction-certificate-2026-06-24.md"
---

# Hourly 20260625 1503 Cycle 1 QFT Local Gauge Action Groupoid

## 1. Verdict

Verdict: **underdefined; a standard local gauge-action packet can be written as a
candidate, but the repo does not yet contain the source-defined observed raw
field object or branch pullback needed to promote a generator for
`tilde_phys^b(O)`**.

This lane attempted to define or reject:

```text
LocalGaugeActionGroupoidOnObservedRawGUFields_V1
```

The positive side is real: prior repo sources support an `Sp(64)` gauge-action
candidate on connection, curvature, spinor, and ad-valued fields. The standard
local formulas are restriction-compatible once the fields and gauge parameters
are actually defined over a local observed region.

The promotion side fails at the first source-object gate. The repo still lacks a
source-defined typed `R_raw^b(O)` and a source-defined observation/branch map
`iota_b: O -> Y` with enough structure to say which local `Y`-data are observed
over `O subset X`. Therefore no gauge-orbit congruence generator is promoted.

Decision state:

```text
candidate_local_groupoid_packet_written: true
local_groupoid_defined: false
typed_R_raw_b_O_defined: false
branch_iota_b_defined: false
restriction_stability_proved: false
source_defined_generator_count: 0
F_phys_defined: false
P_fin_defined: false
CHSH_work_allowed: false
target_import_used: false
proof_restart_allowed: false
```

## 2. What was derived directly from repo sources

`RESEARCH-POSTURE.md` allows constructive reconstruction but forbids hiding
target data inside the source layer. For this lane, no target Hilbert state,
density matrix, Bell/CHSH datum, Pauli setting, or representation-carrier label
may select a gauge quotient.

The five-lane and three-cycle runbooks require a decision-grade obstruction, not
a summary-only note. The exact gate is the upstream source object named by the
1302 next-frontier DAG:

```text
QFT_LOCAL_GAUGE_ACTION_GROUPOID
  -> QFT_GAUGE_RESTRICTION_STABILITY_PROOF
  -> QFT_PHYSICAL_QUOTIENT_FUNCTOR
  -> QFT_PRAW_PFIN_DESCENT
```

The 1302 cycle 1 QFT congruence-generator artifact established a taxonomy of
possible local physical-equivalence generators and counted zero source-defined,
restriction-stable generators. The gauge-orbit slot required:

```text
typed_R_raw_b_O
H_or_inhomogeneous_G_action_on_R_raw_b_O
local_parameter_restriction_rule
restriction_compatibility_proof
```

The 1302 cycle 2 QFT gauge-action gate sharpened that into the missing object
`LocalGaugeActionGroupoidOnObservedRawGUFields_V1`. It also recorded the existing
positive data:

```text
Sp(64) structure group
principal bundle P -> Y^14
connection space Conn(P)
local/formal gauge transformations Gamma(Ad P)
A -> A^g = g A g^{-1} + g d g^{-1}
F_A -> F_A^g = Ad(g) F_A
```

`sc1-oq3-gauge-equivariance-2026-06-23.md` supplies the source-side algebraic
equivariance of the shiab/Phi construction for the correlated `(Ad, rho)` action
on ad-valued forms and spinors:

```text
Phi(Ad(g) alpha, rho(g) psi) = rho(g) Phi(alpha, psi)
```

`type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md` identifies the GU
connection-fluctuation orbit as the orbit of `Conn(P)` under `Gamma(Ad P)`,
assuming the `Sp(64)` bundle is input. It explicitly does not derive the gauge
group from a Connes-Chamseddine or Type II_1 unitary orbit.

`dd1-distortion-distinct-canon-sharpen-2026-06-23.md` gives a source-side
inhomogeneous gauge/distortion law, showing that connection-difference data can
transform tensorially when the reference is dragged by the gauge label. This is
support for a source gauge-action family, not a local observed quotient.

`qft-shadow-extraction-certificate-2026-06-24.md` parks QFT state-space,
`rho_AB`, observables, Born probabilities, and CHSH until an upstream physical
field quotient and descent exist.

## 3. The strongest positive result

The strongest positive result is a precise candidate packet. It is not promoted,
but it is the next object the repo should try to inhabit.

Fix, as future source data, a branch `b`, observed region `O subset X`, smaller
region `O' subset O`, and a smooth observation map or branch pullback
`iota_b: O -> Y`. Let `U_b(O)` be either `iota_b(O)` or a specified open
neighborhood in `Y` on which pullback and restriction are unambiguous.

Candidate raw object:

```text
R_raw^b(O) =
  {
    A_O in Conn(P|_{U_b(O)}),
    F_O = F_{A_O} in Omega^2(U_b(O), ad P),
    psi_O in Gamma(S_P|_{U_b(O)}),
    alpha_O in Omega^2(U_b(O), ad P) for Phi input,
    Phi_O(alpha_O, psi_O) in Omega^1(U_b(O), S_P),
    optional distortion/section fields explicitly declared by the branch packet
  }
```

The exact field list must be source-declared. This candidate list is admissible
only as a reconstruction template because the repo has not yet supplied
`R_raw^b(O)` itself.

Candidate local groupoid:

```text
G_b(O) = local admissible gauge transformations over U_b(O)
       = smooth sections of Ad(P)|_{U_b(O)}
```

More groupoid-explicitly, objects are local trivialized raw field domains over
`U_b(O)`, and an arrow `g: phi -> psi` is an admissible local gauge parameter
with `psi = gamma_O(g, phi)`. Composition is pointwise multiplication of local
gauge parameters on common domains, and identities are the unit section.

Candidate action maps:

```text
gamma_O(g, A) = A^g = g A g^{-1} + g d g^{-1}
gamma_O(g, F_A) = F_{A^g} = Ad(g) F_A
gamma_O(g, psi) = rho(g) psi
gamma_O(g, alpha) = Ad(g) alpha
gamma_O(g, Phi(alpha, psi)) = rho(g) Phi(alpha, psi)
```

The last line follows from the repo's shiab equivariance result when `alpha` is
ad-valued and the frame is gauge-invariant.

Candidate restriction maps for `O' subset O`:

```text
res^R_{O,O'}:
  restrict each declared field from U_b(O) to U_b(O')

res^G_{O,O'}:
  restrict each gauge parameter g from U_b(O) to U_b(O')
```

Candidate commuting square:

```text
        G_b(O) x R_raw^b(O)  --gamma_O-->  R_raw^b(O)
             |                                |
   res^G x res^R                              res^R
             v                                v
      G_b(O') x R_raw^b(O') --gamma_O'--> R_raw^b(O')

res^R_{O,O'}(gamma_O(g, phi))
  = gamma_O'(res^G_{O,O'} g, res^R_{O,O'} phi)
```

Componentwise, this square is standard for the connection formula, curvature
formula, spinor action, ad-valued form action, and Phi equivariance because all
operations are local differential operations. This gives a strong construction
target.

## 4. The first exact obstruction or missing proof object

The first exact obstruction is not the absence of gauge theory. It is the absence
of a repo-source-defined local observed raw field object and branch map.

The missing proof object is:

```text
SourceObservedRawFieldBranchPacketForRRawBO_V1
```

Minimum required fields:

1. `branch_context`: the branch `b`, source region policy, and exact meaning of
   `O subset X`.
2. `branch_pullback`: a source-defined `iota_b: O -> Y` or equivalent observed
   section/pullback map.
3. `local_Y_domain`: a precise `U_b(O)` and restriction law for
   `O' subset O`.
4. `typed_R_raw_b_O`: the complete field list, regularity class, support policy,
   domains, and operations of `R_raw^b(O)`.
5. `admissible_gauge_parameters`: the exact sheaf/groupoid `G_b(O)` and any
   boundary, support, observer, or branch-preserving restrictions.
6. `action_on_all_components`: action maps for every component of `R_raw^b(O)`,
   including any section/observer/distortion fields if present.
7. `restriction_commuting_square`: a proof of the square in section 3 for every
   declared component.
8. `congruence_proof`: proof that the orbit relation generated by `G_b(O)` is a
   congruence for the operations of `R_raw^b(O)`.
9. `non_import_proof`: proof that no target Hilbert state, density matrix,
   Bell/CHSH control, Pauli setting, representation label, or QFT recovery target
   selected the quotient.

Because fields 2 and 4 are absent in the current repo sources read for this
lane, the local groupoid is a candidate template rather than a defined repo
object. Consequently the generator count remains zero.

## 5. The constructive next object that would remove or test the obstruction

The next object should be:

```text
SourceObservedRawFieldBranchPacketForRRawBO_V1
```

It should be deliberately smaller than a full QFT reconstruction. It only needs
to make one observed branch and one local gauge action precise enough to run the
restriction square.

Acceptance contract:

```text
input:
  b, O, O', iota_b, P -> Y, S_P, and a declared local field list

emit:
  U_b(O)
  U_b(O')
  R_raw^b(O)
  R_raw^b(O')
  G_b(O)
  G_b(O')
  res^R_{O,O'}
  res^G_{O,O'}
  gamma_O
  gamma_O'

prove:
  res^R_{O,O'} gamma_O(g, phi)
    = gamma_O'(res^G_{O,O'} g, res^R_{O,O'} phi)
  for A, F_A, psi, ad-valued Phi inputs, Phi outputs, and every additional
  source-declared component.
```

If that packet closes, then exactly one source-defined,
restriction-stable gauge-orbit generator family may be counted. If it fails,
the failure will be localized to one of three precise places:

```text
missing_iota_b
missing_or_overbroad_R_raw_b_O
admissible_gauge_parameter_class_not_restriction_stable
```

## 6. What this means for `F_phys`, `P_raw/P_fin`, `rho_AB`, and CHSH

For `F_phys`:

```text
F_phys^b(O)` is not defined.
tilde_phys^b(O)` has no promoted gauge-orbit generator from this lane.
```

For `P_raw/P_fin`:

```text
P_raw^b(O)` may be a later extraction map, but no descent check is allowed yet.
P_fin^b` is not defined because the physical quotient domain is absent.
```

For `rho_AB`:

```text
No finite density matrix, covariance, two-point state, or Hilbert-state object is
unlocked by this lane.
```

For CHSH:

```text
CHSH work remains downstream and parked. Bell controls and Pauli settings can
test later finite outputs, but they cannot define `R_raw^b(O)`, `G_b(O)`, the
gauge action, or the local physical quotient.
```

Representation labels can remain downstream bookkeeping after a source quotient
exists. They are not selectors for this local groupoid and they do not count as
source-defined physical equivalence.

## 7. Next meaningful proof/computation step

Run:

```text
GaugeOrbitGeneratorRestrictionTest_V1
```

but only after a source artifact emits `SourceObservedRawFieldBranchPacketForRRawBO_V1`.

The proof target is:

```text
For every O' subset O, if phi ~_gauge,O psi in R_raw^b(O), then
res^R_{O,O'} phi ~_gauge,O' res^R_{O,O'} psi in R_raw^b(O').
```

The computation should be componentwise and local:

```text
A      : restrict A^g and compare with (A|O')^(g|O')
F_A    : restrict Ad(g)F_A and compare with Ad(g|O')F_A|O'
psi    : restrict rho(g)psi and compare with rho(g|O')psi|O'
alpha  : restrict Ad(g)alpha and compare with Ad(g|O')alpha|O'
Phi    : use repo Phi equivariance after restriction
extras : test every branch-declared section/distortion/observer component
```

No target Hilbert state, density matrix, Bell/CHSH control, Pauli setting, or
representation label should appear in that proof except as an explicitly
forbidden selector.

## 8. Machine-readable JSON summary

```json
{
  "artifact_id": "LocalGaugeActionGroupoidOnObservedRawGUFields_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-1503",
  "cycle": 1,
  "lane": 5,
  "verdict": "UNDERDEFINED_CANDIDATE_PACKET_DRAFTED_REPO_SOURCE_OBJECTS_MISSING_NO_GENERATOR_PROMOTED",
  "verdict_class": "underdefined",
  "owned_path": "explorations/hourly-20260625-1503-cycle1-qft-local-gauge-action-groupoid.md",
  "companion_audit": "tests/hourly_20260625_1503_cycle1_qft_local_gauge_action_groupoid_audit.py",
  "candidate_local_groupoid_packet_written": true,
  "candidate_R_raw_b_O_specified": true,
  "candidate_G_b_O_specified": true,
  "candidate_action_maps_specified": true,
  "candidate_restriction_square_specified": true,
  "local_groupoid_defined": false,
  "typed_R_raw_b_O_defined": false,
  "branch_iota_b_defined": false,
  "restriction_stability_proved": false,
  "gauge_action_generator_source_defined": false,
  "source_defined_generator_count": 0,
  "restriction_stable_generator_count": 0,
  "F_phys_defined": false,
  "physical_equivalence_relation_defined": false,
  "P_raw_descent_allowed": false,
  "P_fin_defined": false,
  "rho_AB_work_allowed": false,
  "CHSH_work_allowed": false,
  "target_import_used": false,
  "proof_restart_allowed": false,
  "candidate_action_data": {
    "fiber_group": "Sp(64)",
    "global_or_formal_gauge_group": "Gamma(Ad P)",
    "connection_action_formula_present": true,
    "curvature_action_formula_present": true,
    "spinor_action_formula_present": true,
    "ad_valued_phi_equivariance_present": true,
    "inhomogeneous_distortion_equivariance_present": true
  },
  "candidate_R_raw_b_O_components": [
    "connection_A",
    "curvature_F_A",
    "spinor_psi",
    "ad_valued_two_form_alpha",
    "Phi_alpha_psi",
    "optional_source_declared_distortion_or_section_fields"
  ],
  "candidate_G_b_O": "smooth_admissible_local_sections_of_AdP_over_U_b_O",
  "candidate_action_maps": {
    "A": "A^g = g A g^{-1} + g d g^{-1}",
    "F_A": "F_A^g = Ad(g) F_A",
    "psi": "psi^g = rho(g) psi",
    "alpha": "alpha^g = Ad(g) alpha",
    "Phi": "Phi(Ad(g) alpha, rho(g) psi) = rho(g) Phi(alpha, psi)"
  },
  "candidate_commuting_square": "res_R(gamma_O(g, phi)) = gamma_O_prime(res_G(g), res_R(phi))",
  "first_exact_obstruction": {
    "id": "SourceObservedRawFieldBranchPacketForRRawBO_V1",
    "missing": true,
    "required_fields": [
      "branch_context_b_O_O_prime",
      "source_defined_iota_b",
      "local_Y_domain_U_b_O",
      "typed_R_raw_b_O",
      "typed_R_raw_b_O_prime",
      "admissible_gauge_groupoid_G_b_O",
      "action_gamma_O_on_all_raw_components",
      "raw_field_restriction_res_R_O_O_prime",
      "gauge_parameter_restriction_res_G_O_O_prime",
      "restriction_commuting_square",
      "congruence_compatibility_proof",
      "non_import_proof"
    ],
    "blocks": [
      "local_groupoid_definition",
      "gauge_orbit_generator_promotion",
      "tilde_phys_b_O",
      "F_phys^b(O)",
      "P_raw_descent_test",
      "P_fin^b",
      "rho_AB",
      "CHSH"
    ]
  },
  "strongest_positive_result": {
    "id": "candidate_standard_local_Sp64_gauge_action_packet",
    "classification": "candidate_not_promoted",
    "statement": "Standard local gauge action formulas give a plausible restriction-commuting packet for connection, curvature, spinor, and ad-valued Phi fields once source-defined R_raw_b_O and iota_b exist.",
    "does_not_use_target_data": true
  },
  "next_meaningful_step": {
    "id": "GaugeOrbitGeneratorRestrictionTest_V1",
    "requires": "SourceObservedRawFieldBranchPacketForRRawBO_V1",
    "goal": "prove_componentwise_restriction_stability_for_the_source_defined_local_gauge_action",
    "first_promotable_output": "one_source_defined_restriction_stable_gauge_orbit_generator_family"
  },
  "forbidden_promotions": [
    "target_Hilbert_state_as_gauge_congruence_selector",
    "target_density_matrix_as_gauge_congruence_selector",
    "Bell_or_CHSH_control_as_gauge_congruence_selector",
    "Pauli_observable_as_gauge_congruence_selector",
    "representation_carrier_label_as_gauge_congruence_selector",
    "ordinary_QFT_recovery_target_as_gauge_generator_selector",
    "K_b_direct_sum_label_as_F_phys_quotient"
  ]
}
```
