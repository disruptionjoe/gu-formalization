---
title: "Hourly 20260625 1503 Cycle 2 QFT Source Observed Raw Branch Packet"
date: "2026-06-25"
run_id: "hourly-20260625-1503"
cycle: 2
lane: 5
doc_type: qft_source_observed_raw_branch_packet
artifact_id: "SourceObservedRawFieldBranchPacketForRRawBO_V1"
verdict: "UNDERDEFINED_SOURCE_BRANCH_PACKET_ABSENT_CANDIDATE_TEMPLATE_NOT_PROMOTED"
owned_path: "explorations/hourly-20260625-1503-cycle2-qft-source-observed-raw-branch-packet.md"
companion_audit: "tests/hourly_20260625_1503_cycle2_qft_source_observed_raw_branch_packet_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "process/runbooks/three-cycle-fifteen-hole-run.md"
  - "explorations/hourly-20260625-1503-cycle1-qft-local-gauge-action-groupoid.md"
  - "explorations/hourly-20260625-1302-cycle2-qft-gauge-action-restriction-stability-gate.md"
  - "explorations/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/mission-a-qft-state-space-extraction-2026-06-24.md"
  - "explorations/cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"
---

# Hourly 20260625 1503 Cycle 2 QFT Source Observed Raw Branch Packet

## 1. Verdict

Verdict: **underdefined; the repo does not currently contain
`SourceObservedRawFieldBranchPacketForRRawBO_V1` as a source-defined packet**.

Cycle 1 wrote a candidate local gauge-action groupoid, but it correctly did not
promote it because the observed raw field object was missing. This cycle tried
to construct that upstream packet directly. The strict result is negative:
current repo sources give useful templates for a branch, observed region,
section pullback, raw fields, gauge parameters, and restriction square, but they
do not define the packet as source data.

Decision state:

```text
source_branch_packet_present: false
branch_context_defined: false
iota_b_source_defined: false
U_b_O_defined: false
typed_R_raw_b_O_defined: false
G_b_O_defined: false
restriction_maps_defined: false
non_import_screen_present: true
generator_promotion_allowed: false
F_phys_defined: false
P_fin_defined: false
CHSH_work_allowed: false
target_import_used: false
```

The exact first missing object is not `F_phys`, `P_fin`, a density matrix, a
Bell/CHSH fixture, Pauli settings, or representation labels. The first missing
object is the source packet that says what the local observed raw field
`R_raw^b(O)` actually is.

## 2. What was derived directly from repo sources

`RESEARCH-POSTURE.md` permits constructive reconstruction, but forbids
compatibility-as-derivation and target data hidden inside a reconstruction. For
this lane, that means no target Hilbert state, density matrix, Bell/CHSH
control, Pauli setting, finite Pati-Salam representation label, or ordinary QFT
recovery target may select the branch, the observed raw object, the gauge
parameter class, or the quotient.

The runbooks require a decision-grade obstruction. They also require the lane to
identify the first missing proof/source object rather than only restating that
QFT recovery is blocked.

The cycle 1 local gauge groupoid artifact supplies the strongest relevant
predecessor. It established that standard `Sp(64)` gauge action formulas are
available as a candidate over a local `Y`-domain:

```text
P -> Y^14
Conn(P)
Gamma(Ad P)
A -> A^g = g A g^{-1} + g d g^{-1}
F_A -> F_A^g = Ad(g) F_A
psi -> rho(g) psi
alpha -> Ad(g) alpha
Phi(Ad(g) alpha, rho(g) psi) = rho(g) Phi(alpha, psi)
```

The 1302 gauge-action restriction gate gives the same conclusion one level
earlier: gauge-action data exist as candidate source geometry, but not yet as a
source-defined local groupoid acting on a typed `R_raw^b(O)` over observed
regions.

The QFT shadow certificate, the Mission A QFT state-space attempt, and the
physical-field positive-pairing seed all reinforce the same downstream guard:
`F_phys`, positive pairings, finite state spaces, `P_fin`, density matrices,
observables, and CHSH belong after a source-defined physical field quotient.
They cannot be used to define `R_raw^b(O)` or to choose the branch packet.

Directly derived source-clean facts:

```text
candidate_source_carrier_Y: present as a GU source geometry carrier in prior artifacts
candidate_bundle_P_to_Y: present as Sp(64) principal-bundle input in gauge artifacts
candidate_connection_fields: present as formal/source gauge-action data
candidate_spinor_and_ad_valued_fields: present as Phi/shiab equivariance data
candidate_observer_region_O_subset_X: used in QFT local-extraction templates
source_defined_branch_packet_b_O_iota_Rraw: absent
```

## 3. The strongest positive construction attempt

The strongest positive result is a precise template for the missing packet. It
is not promoted because several entries are not source-defined in the repo
sources read for this lane.

Candidate branch context:

```text
b:
  one GU source branch containing P -> Y, field regularity, boundary/vacuum
  convention if any, and observer/section data

O subset X:
  an observed spacetime/observer region

O' subset O:
  a smaller observed region for restriction tests
```

Candidate branch map:

```text
iota_b: O -> Y
```

This may be a section, observation map, or branch pullback. It must be
source-defined. It may not be inferred from a desired finite QFT output.

Candidate local `Y`-domain:

```text
U_b(O):
  either iota_b(O), if all pullbacks and restrictions are defined on that image,
  or a specified open neighborhood in Y with a rule U_b(O') subset U_b(O)
  for O' subset O.
```

Candidate typed raw object:

```text
R_raw^b(O) =
  {
    A_O in Conn(P|_{U_b(O)}),
    F_O = F_{A_O} in Omega^2(U_b(O), ad P),
    psi_O in Gamma(S_P|_{U_b(O)}),
    alpha_O in Omega^2(U_b(O), ad P),
    Phi_O(alpha_O, psi_O) in Omega^1(U_b(O), S_P),
    optional section, distortion, observer, boundary, or constraint data
      only if the source packet explicitly declares them
  }
```

Candidate admissible gauge parameters:

```text
G_b(O) =
  admissible local sections of Ad(P)|_{U_b(O)}
```

The word "admissible" must be defined in the packet. Possible policies include
plain smooth local sections, compactly supported local sections, sections
preserving boundary data, or branch-preserving sections. The repo cannot choose
one by looking at which class makes a later QFT state or CHSH result work.

Candidate restrictions for `O' subset O`:

```text
res^R_{O,O'}:
  restrict every declared raw component from U_b(O) to U_b(O')

res^G_{O,O'}:
  restrict every admissible gauge parameter from U_b(O) to U_b(O')
```

Candidate non-import screen:

```text
reject if b, iota_b, U_b(O), R_raw^b(O), G_b(O), res^R, or res^G
is selected by F_phys, P_fin, rho_AB, Bell/CHSH controls, Pauli settings,
representation-carrier labels, ordinary SM targets, or ordinary QFT recovery
requirements.
```

If all entries above were source-defined, the cycle 1 gauge-action formulas
would then supply the next restriction square to test:

```text
res^R_{O,O'}(gamma_O(g, phi))
  = gamma_{O'}(res^G_{O,O'} g, res^R_{O,O'} phi).
```

This is the correct construction target. It is not a constructed repo object
today.

## 4. The first exact obstruction or missing proof/source object

The first exact obstruction is:

```text
SourceObservedRawFieldBranchPacketForRRawBO_V1
```

It is missing at the packet level. The current repo sources do not provide a
source receipt or formal artifact that simultaneously defines:

1. `branch_context`: the branch `b`, the meaning of `O subset X`, and the policy
   for smaller regions `O' subset O`.
2. `iota_b`: a source-defined observation/section/pullback map `O -> Y`.
3. `U_b(O)`: a local `Y`-domain with an inclusion/restriction policy.
4. `typed_R_raw^b(O)`: the full raw field list, regularity class, domains,
   support/boundary policy, and operations.
5. `G_b(O)`: the admissible gauge parameter class over `U_b(O)`, including
   support, boundary, and branch-preservation rules.
6. `res^R_{O,O'}` and `res^G_{O,O'}`: restriction maps that are defined on the
   declared typed objects.
7. `non_import_screen`: a proof that target QFT, finite-state, Bell/CHSH,
   Pauli, or representation-label data did not select any upstream entry.

The first missing subobject is:

```text
source_defined_iota_b_and_typed_R_raw_b_O
```

Without `iota_b`, `U_b(O)` is not a defined local source domain. Without
`typed_R_raw^b(O)`, `G_b(O)` has no complete action domain and restriction maps
cannot be proved. Therefore the packet remains underdefined even though the
standard gauge formulas are available as a candidate.

## 5. The constructive next object that would remove or test the obstruction

The next object should be a deliberately small source packet, not a QFT recovery
claim:

```text
SourceObservedRawFieldBranchPacketForRRawBO_V1
```

Minimum acceptance contract:

```text
input/source:
  b
  X and Y
  O subset X and O' subset O
  P -> Y
  any spinor/ad/distortion bundles used by the raw object

emit:
  iota_b: O -> Y
  U_b(O) and U_b(O')
  typed R_raw^b(O) and R_raw^b(O')
  G_b(O) and G_b(O')
  res^R_{O,O'}
  res^G_{O,O'}
  non_import_screen
```

Validation conditions:

```text
1. iota_b is source-defined, not inferred from finite output data.
2. U_b(O') is compatible with U_b(O) for O' subset O.
3. every component of R_raw^b(O) has a declared domain and regularity class.
4. G_b(O) acts on every declared component or the component is explicitly
   invariant with proof.
5. res^R and res^G map admissible objects to admissible objects.
6. no forbidden target selector appears in the packet provenance.
```

Once this packet exists, the next proof is the cycle 1
`GaugeOrbitGeneratorRestrictionTest_V1`. If the packet does not exist, no gauge
generator should be promoted.

## 6. What this means for gauge generator promotion, `F_phys`, `P_fin`, and CHSH

Gauge generator promotion:

```text
not allowed.
```

The gauge formulas remain a candidate. The generator becomes promotable only
after `G_b(O)` is source-defined, acts on a typed `R_raw^b(O)`, and the
restriction square is proved for every declared component.

For `F_phys`:

```text
F_phys^b(O) is not defined.
tilde_phys^b(O) has no promoted gauge-orbit generator from this lane.
```

For `P_fin`:

```text
P_fin^b is not defined.
P_raw/P_fin descent tests are not allowed because the source physical quotient
domain is absent.
```

For CHSH:

```text
CHSH work remains parked.
rho_AB, Bell controls, Pauli settings, and target finite spaces cannot define
the branch packet, raw object, gauge action, or quotient.
```

Representation labels may remain useful after a source packet and physical
quotient exist. They do not select `b`, `iota_b`, `R_raw^b(O)`, `G_b(O)`, or
the physical equivalence relation.

## 7. Next meaningful proof/source computation step

Run a source-object locator or write a new source packet with the following
single target:

```text
FindOrConstructSourceObservedRawFieldBranchPacketForRRawBO_V1
```

The computation should answer, in order:

```text
1. Is there a repo-source branch b with an explicit observed map iota_b: O -> Y?
2. Does that branch define U_b(O) for local observed regions?
3. Does it emit a complete typed R_raw^b(O), including every field component
   on which gauge action will later be tested?
4. Does it emit admissible G_b(O), rather than merely the global formal group
   Gamma(Ad P)?
5. Do res^R and res^G preserve the declared classes for O' subset O?
6. Does the packet pass the non-import screen?
```

Only after those six questions close should the repo run:

```text
GaugeOrbitGeneratorRestrictionTest_V1
```

The first promotable output would be one source-defined,
restriction-stable gauge-orbit generator family. Until then, the correct status
is underdefined.

## 8. Machine-readable JSON summary

```json
{
  "artifact_id": "SourceObservedRawFieldBranchPacketForRRawBO_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-1503",
  "cycle": 2,
  "lane": 5,
  "verdict": "UNDERDEFINED_SOURCE_BRANCH_PACKET_ABSENT_CANDIDATE_TEMPLATE_NOT_PROMOTED",
  "verdict_class": "underdefined",
  "owned_path": "explorations/hourly-20260625-1503-cycle2-qft-source-observed-raw-branch-packet.md",
  "companion_audit": "tests/hourly_20260625_1503_cycle2_qft_source_observed_raw_branch_packet_audit.py",
  "source_branch_packet_present": false,
  "branch_context_defined": false,
  "iota_b_source_defined": false,
  "U_b_O_defined": false,
  "typed_R_raw_b_O_defined": false,
  "G_b_O_defined": false,
  "restriction_maps_defined": false,
  "non_import_screen_present": true,
  "generator_promotion_allowed": false,
  "F_phys_defined": false,
  "P_fin_defined": false,
  "CHSH_work_allowed": false,
  "target_import_used": false,
  "candidate_template_written": true,
  "candidate_branch_context": {
    "b": "one_source_branch_with_P_to_Y_field_regularities_boundary_or_vacuum_and_observer_data",
    "O": "observed_region_subset_X",
    "O_prime": "smaller_observed_region_subset_O",
    "status": "template_not_source_defined"
  },
  "candidate_iota_b": {
    "display": "iota_b: O -> Y",
    "allowed_kind": "source_defined_section_observation_map_or_branch_pullback",
    "status": "missing_source_definition"
  },
  "candidate_U_b_O": {
    "display": "U_b(O) subset Y",
    "policy": "iota_b_image_or_specified_open_neighborhood_with_U_b_O_prime_subset_U_b_O",
    "status": "missing_because_iota_b_missing"
  },
  "candidate_R_raw_b_O_components": [
    "connection_A",
    "curvature_F_A",
    "spinor_psi",
    "ad_valued_two_form_alpha",
    "Phi_alpha_psi",
    "optional_source_declared_section_distortion_observer_boundary_or_constraint_fields"
  ],
  "candidate_G_b_O": "admissible_local_sections_of_AdP_over_U_b_O",
  "candidate_restriction_maps": {
    "res_R_O_O_prime": "restrict_every_declared_raw_component_from_U_b_O_to_U_b_O_prime",
    "res_G_O_O_prime": "restrict_every_admissible_gauge_parameter_from_U_b_O_to_U_b_O_prime",
    "status": "template_only"
  },
  "candidate_next_square": "res_R(gamma_O(g,phi)) = gamma_O_prime(res_G(g),res_R(phi))",
  "what_was_derived_directly": [
    "standard_candidate_Sp64_gauge_action_formulas_from_prior_gauge_artifacts",
    "candidate_P_to_Y_and_Gamma_AdP_source_geometry_context",
    "Phi_shiab_equivariance_template_for_ad_valued_and_spinor_inputs",
    "downstream_QFT_state_space_and_CHSH_objects_are_parked_until_source_quotient_exists"
  ],
  "first_exact_obstruction": {
    "id": "SourceObservedRawFieldBranchPacketForRRawBO_V1",
    "missing": true,
    "first_missing_subobject": "source_defined_iota_b_and_typed_R_raw_b_O",
    "required_fields": [
      "branch_context_b_O_O_prime",
      "source_defined_iota_b",
      "local_Y_domain_U_b_O",
      "typed_R_raw_b_O",
      "typed_R_raw_b_O_prime",
      "admissible_G_b_O",
      "admissible_G_b_O_prime",
      "raw_field_restriction_res_R_O_O_prime",
      "gauge_parameter_restriction_res_G_O_O_prime",
      "non_import_screen"
    ],
    "blocks": [
      "LocalGaugeActionGroupoidOnObservedRawGUFields_V1",
      "gauge_orbit_generator_promotion",
      "tilde_phys_b_O",
      "F_phys^b(O)",
      "P_raw_descent_test",
      "P_fin^b",
      "rho_AB",
      "CHSH"
    ]
  },
  "strongest_positive_construction_attempt": {
    "id": "source_observed_raw_branch_packet_template",
    "classification": "candidate_not_promoted",
    "statement": "A source-clean packet can be specified as b,O,O_prime,iota_b,U_b(O),typed R_raw^b(O),admissible G_b(O),restriction maps,and a non-import screen; current repo sources do not define it.",
    "does_not_use_target_data": true
  },
  "downstream_impact": {
    "gauge_generator_promotion_allowed": false,
    "F_phys_defined": false,
    "P_raw_descent_allowed": false,
    "P_fin_defined": false,
    "rho_AB_work_allowed": false,
    "CHSH_work_allowed": false
  },
  "next_meaningful_step": {
    "id": "FindOrConstructSourceObservedRawFieldBranchPacketForRRawBO_V1",
    "then": "GaugeOrbitGeneratorRestrictionTest_V1",
    "first_promotable_output": "one_source_defined_restriction_stable_gauge_orbit_generator_family"
  },
  "forbidden_selectors": [
    "F_phys_as_selector_for_R_raw_b_O",
    "P_fin_as_selector_for_R_raw_b_O",
    "target_Hilbert_state_as_branch_selector",
    "target_density_matrix_as_branch_selector",
    "Bell_or_CHSH_control_as_branch_or_gauge_selector",
    "Pauli_setting_as_branch_or_gauge_selector",
    "representation_label_as_branch_or_gauge_selector",
    "ordinary_QFT_recovery_target_as_branch_packet_selector"
  ]
}
```
