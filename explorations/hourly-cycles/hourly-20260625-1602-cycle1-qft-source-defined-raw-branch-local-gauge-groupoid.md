---
artifact_id: "QFTSourceDefinedRawBranchLocalGaugeGroupoidPacket_1602_C1_L5_V1"
run_id: "hourly-20260625-1602"
cycle: 1
lane: 5
verdict: "UNDERDEFINED_TEMPLATE_COMPATIBILITY_SKETCH_PRESENT_SOURCE_DEFINED_PACKET_ABSENT"
owned_path: "explorations/hourly-20260625-1602-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid.md"
companion_audit: "tests/hourly_20260625_1602_cycle1_qft_source_defined_raw_branch_local_gauge_groupoid_audit.py"
source_inputs:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "process/runbooks/three-cycle-fifteen-hole-run.md"
  - "explorations/hourly-20260625-1503-three-cycle-fifteen-hole-synthesis.md"
  - "explorations/hourly-20260625-1503-cycle1-qft-local-gauge-action-groupoid.md"
  - "explorations/hourly-20260625-1503-cycle2-qft-source-observed-raw-branch-packet.md"
  - "explorations/cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"
  - "tests/hourly_20260625_1503_cycle2_qft_source_observed_raw_branch_packet_audit.py"
---

# QFT source-defined raw branch/local gauge groupoid packet

## 1. Verdict

Verdict: **underdefined**.

The repo can state a template and a restriction-compatibility sketch for a raw
branch/local gauge groupoid packet, but it cannot yet define the packet as a
source-defined object. The current sources do not provide a typed branch map
`iota_b`, a typed raw-field object `R_raw^b(O)`, an admissible local gauge
groupoid `G_b(O)`, and restriction maps as source-emitted data. They provide
enough structure to say exactly what must be supplied next.

Decision flags:

```yaml
accepted_receipt_count: 0
proof_restart_allowed: false
target_import_used: false
template_or_compatibility_sketch_present: true
source_defined_packet_present: false
quotient_descent_work_allowed: false
```

## 2. What was derived directly from repo sources

From the 1503 synthesis:

- The three-cycle closeout records zero accepted receipts and no proof restart.
- QFT work is blocked on a source-defined raw branch and local gauge groupoid
  packet before quotient/descent and finite-output claims.
- The named next object after the 1503 QFT lane is a source-defined raw
  branch/local gauge groupoid packet.

From the 1503 local gauge-action groupoid artifact:

- A standard local gauge-action packet can be written as a candidate.
- Candidate fields include connection-like, curvature-like, spinor-like,
  adjoint-valued two-form-like, and equivariant `Phi`-type components.
- Candidate gauge parameters are local admissible sections over a local domain
  `U_b(O)`.
- The intended restriction square is componentwise: restrict the gauge
  parameter and raw field, then compare with first acting locally and then
  restricting.
- The candidate cannot be promoted because the repo lacks source-defined
  `iota_b`, typed `R_raw^b(O)`, admissible `G_b(O)`, and restriction maps.

From the 1503 source-observed raw branch packet artifact and audit:

- The artifact explicitly marked `SourceObservedRawFieldBranchPacketForRRawBO_V1`
  underdefined.
- Its audit requires the packet fields to remain false unless the repo source
  defines them.
- The first missing subobject was already identified as
  `source_defined_iota_b_and_typed_R_raw_b_O`.
- The candidate is only a template, not a promoted source-defined packet.

From the physical-field positive-pairing seed:

- Standard QFT pairings and finite physical outputs may be useful downstream
  only after the physical quotient is source-defined.
- They are not valid selectors for `b`, `iota_b`, `R_raw^b(O)`, `G_b(O)`, or
  restriction maps.

No target Hilbert state, target density matrix, Bell fixture, CHSH fixture,
Pauli setting, representation-carrier label, or desired ordinary-QFT recovery
was used to define the branch packet.

## 3. The strongest positive result

The strongest positive result is a **compatibility template**:

```text
Input shape:
  branch context b
  observed region O and subregion O_prime subset O
  source-defined map iota_b: O -> Y
  local domain U_b(O) in Y with U_b(O_prime) subset U_b(O)
  typed raw fields R_raw^b(O)
  local admissible gauge groupoid G_b(O)
  raw-field restriction res_R_{O,O_prime}
  gauge-parameter restriction res_G_{O,O_prime}

Candidate raw fields:
  A            connection-like field
  F_A          curvature-like field
  psi          spinor-like field
  alpha        adjoint-valued two-form-like field
  Phi_alpha_psi equivariant composite/pairing field

Candidate local gauge object:
  G_b(O) = admissible local sections of AdP over U_b(O)

Candidate compatibility square:
  res_R_{O,O_prime}(gamma_O(g, r))
    =
  gamma_{O_prime}(res_G_{O,O_prime}(g), res_R_{O,O_prime}(r))
```

This is useful because it fixes the exact type signature and the first test that
must be run once source data exist. It is not a source-defined packet. The
template becomes promotable only if the repo supplies the branch map, domains,
field regularity/support rules, admissible gauge class, actions on all declared
components, and restrictions without importing the target finite QFT outcome.

## 4. The first exact obstruction or missing proof/source object

The first obstruction is:

```text
SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1 is absent.
```

The first exact missing subobject is:

```text
source_defined_iota_b_and_typed_R_raw_b_O
```

Reason: without `iota_b`, the local source domain `U_b(O)` is not anchored in a
branch. Without typed `R_raw^b(O)`, the action domain for `G_b(O)` is not
defined. Without both, any proposed `G_b(O)` and restriction maps are only
formal placeholders: they do not yet act on a repo-source raw-field object, and
they cannot be used to begin quotient/descent work.

Required fields still absent as source-defined objects:

- `branch_context_b_O_O_prime`
- `source_defined_iota_b`
- `local_domain_U_b_O`
- `local_domain_U_b_O_prime`
- `typed_R_raw_b_O`
- `typed_R_raw_b_O_prime`
- `admissible_local_gauge_groupoid_G_b_O`
- `admissible_local_gauge_groupoid_G_b_O_prime`
- `raw_field_restriction_res_R_O_O_prime`
- `gauge_parameter_restriction_res_G_O_O_prime`
- `componentwise_action_gamma_O`
- `componentwise_action_gamma_O_prime`
- `restriction_commuting_square_proof`
- `non_import_screen`

## 5. The constructive next object that would remove or test the obstruction

The constructive next object is:

```text
SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1
```

It must be a packet, not a prose analogy. Minimum contents:

```text
packet SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1:
  b:
    source branch identifier and admissibility rule
  O, O_prime:
    observed regions with O_prime subset O
  iota_b:
    typed source-defined map O -> Y or equivalent observed pullback object
  U_b:
    local domains U_b(O), U_b(O_prime), and inclusion/restriction policy
  R_raw:
    typed fields R_raw^b(O), R_raw^b(O_prime)
    component list, domains, regularity, support/boundary policy, operations
  G:
    admissible local gauge groupoids G_b(O), G_b(O_prime)
    object/morphism or parameter class, closure, and branch-preserving rules
  gamma:
    action on every declared component of R_raw
  res_R:
    raw-field restriction R_raw^b(O) -> R_raw^b(O_prime)
  res_G:
    gauge restriction G_b(O) -> G_b(O_prime)
  square:
    proof that action and restriction commute componentwise
  firewall:
    proof that target finite outputs were not used as selectors
```

The first test after such a packet exists is:

```text
GaugeOrbitGeneratorRestrictionTest_V1
```

That test may count one promotable generator only if the source-defined action
is restriction-stable on every declared raw-field component.

## 6. What this means for the QFT/GU claim

The QFT/GU claim remains pre-quotient for this branch. The current repo supports
the statement that a plausible local gauge-action template has been identified,
but it does not support the stronger statement that GU has produced a
source-defined QFT raw branch with local gauge groupoid and descent-ready
restriction maps.

Consequences:

- No physical quotient `F_phys^b(O)` is source-defined from this packet.
- No finite extraction `P_fin^b` is source-defined from this packet.
- No `rho_AB`, Bell, or CHSH claim may be promoted from this packet.
- No generator can be counted as an accepted source-defined
  restriction-stable gauge-orbit generator.
- Quotient/descent work may begin only as a conditional sketch, not as a
  source-backed proof route.

## 7. Next meaningful proof or computation step

Search for, or construct, one concrete source-defined branch packet with the
minimum contents in section 5. If no such object exists, the next computation is
a negative locator: enumerate repo sources that mention `iota_b`, `R_raw^b(O)`,
`G_b(O)`, and restriction maps, then mark each mention as source definition,
template, downstream target, or analogy. The first promotable output would be
one restriction-stable local gauge-orbit generator family backed by that packet.

## 8. Machine-readable JSON summary

```json
{
  "artifact_id": "QFTSourceDefinedRawBranchLocalGaugeGroupoidPacket_1602_C1_L5_V1",
  "run_id": "hourly-20260625-1602",
  "cycle": 1,
  "lane": 5,
  "verdict": "UNDERDEFINED_TEMPLATE_COMPATIBILITY_SKETCH_PRESENT_SOURCE_DEFINED_PACKET_ABSENT",
  "verdict_class": "underdefined",
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "required_fields": [
    "branch_context_b_O_O_prime",
    "source_defined_iota_b",
    "local_domain_U_b_O",
    "local_domain_U_b_O_prime",
    "typed_R_raw_b_O",
    "typed_R_raw_b_O_prime",
    "admissible_local_gauge_groupoid_G_b_O",
    "admissible_local_gauge_groupoid_G_b_O_prime",
    "raw_field_restriction_res_R_O_O_prime",
    "gauge_parameter_restriction_res_G_O_O_prime",
    "componentwise_action_gamma_O",
    "componentwise_action_gamma_O_prime",
    "restriction_commuting_square_proof",
    "non_import_screen"
  ],
  "present_fields": [
    "template_or_compatibility_sketch",
    "candidate_raw_field_component_list",
    "candidate_local_gauge_action_formulas",
    "candidate_restriction_square_shape",
    "promotion_firewall_statement"
  ],
  "missing_fields": [
    "source_defined_iota_b",
    "source_defined_raw_fields_R_raw_b_O",
    "source_defined_local_gauge_groupoid_G_b_O",
    "source_defined_restriction_maps_res_R_and_res_G",
    "source_defined_restriction_commuting_square_proof",
    "complete_non_import_screen_for_packet_construction"
  ],
  "template_or_compatibility_sketch_present": true,
  "source_defined_packet_present": false,
  "iota_b_source_defined": false,
  "R_raw_b_O_source_defined": false,
  "G_b_O_source_defined": false,
  "restriction_maps_source_defined": false,
  "quotient_descent_work_allowed": false,
  "first_obstruction": {
    "id": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
    "missing": true,
    "first_missing_subobject": "source_defined_iota_b_and_typed_R_raw_b_O",
    "why_first": "iota_b anchors U_b(O), and typed R_raw^b(O) gives G_b(O) an action domain; without both, groupoid and restriction maps remain templates."
  },
  "next_object": {
    "id": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
    "description": "A source-defined packet containing b, O, O_prime, iota_b, U_b domains, typed R_raw fields, admissible G_b groupoids, gamma actions, res_R/res_G restrictions, a componentwise commuting-square proof, and a non-import firewall.",
    "then_test": "GaugeOrbitGeneratorRestrictionTest_V1",
    "first_promotable_output": "one_source_defined_restriction_stable_gauge_orbit_generator_family"
  },
  "promotion_firewall": {
    "no_target_hilbert_state_selector": true,
    "no_target_density_matrix_selector": true,
    "no_bell_or_chsh_selector": true,
    "no_pauli_setting_selector": true,
    "no_representation_label_selector": true,
    "no_physical_quotient_selector": true,
    "no_finite_extraction_selector": true,
    "claim_promotion_blocked": true
  },
  "downstream": {
    "F_phys_defined": false,
    "P_fin_defined": false,
    "rho_AB_work_allowed": false,
    "CHSH_work_allowed": false,
    "gauge_generator_promoted": false
  }
}
```
