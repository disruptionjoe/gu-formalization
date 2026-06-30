---
title: "Hourly 20260625 1702 Cycle 1 QFT Raw Branch Local Gauge Groupoid Packet"
date: "2026-06-25"
run_id: "hourly-20260625-1702"
cycle: 1
lane: 5
doc_type: qft_raw_branch_local_gauge_groupoid_packet
artifact_id: "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_1702_C1_L5_V1"
verdict: "UNDERDEFINED_REQUIRED_SOURCE_FIELDS_ABSENT_NON_IMPORT_SCREEN_ACTIVE"
owned_path: "explorations/hourly-20260625-1702-cycle1-qft-raw-branch-local-gauge-groupoid-packet.md"
companion_audit: "tests/hourly_20260625_1702_cycle1_qft_raw_branch_local_gauge_groupoid_packet_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "process/runbooks/three-cycle-fifteen-hole-run.md"
  - "explorations/hourly-20260625-1602-three-cycle-fifteen-hole-synthesis.md"
  - "explorations/hourly-20260625-1602-cycle3-next-frontier-dependency-dag.md"
  - "explorations/hourly-20260625-1602-cycle2-qft-source-defined-branch-packet-minimal-schema.md"
  - "explorations/hourly-20260625-1602-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
  - "specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md"
---

# Source-defined raw branch/local gauge groupoid packet attempt

## 1. Verdict

Verdict: **underdefined**.

This lane attempted to admit
`SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1` from the required
repo sources. The packet cannot be admitted. The repo has a source-clean schema
and a compatibility template, but it does not source-define the required branch
label `b`, injection/selector `iota_b`, local raw field object
`R_raw^b(O)`, local gauge groupoid `G_b(O)`, restriction maps, action on raw
fields, or packet-level non-import receipt.

Decision:

```text
accepted_receipt_count: 0
source_defined_packet_present: false
all_required_fields_source_defined: false
schema_or_template_present: true
proof_restart_allowed: false
target_import_used: false
promotion_allowed: false
quotient_descent_allowed: false
rho_AB_Bell_CHSH_allowed: false
```

No quotient/descent, finite extraction, `rho_AB`, Bell, or CHSH work was used as
a source selector.

## 2. What was derived directly from repo sources

`RESEARCH-POSTURE.md` permits constructive GU reconstruction, but forbids
verdict inflation, compatibility-as-derivation, and hidden target import.

The frontier runbooks require the first exact missing source/proof object and a
decision-grade next object. They do not allow downstream proof replay from zero
accepted receipts.

The 1602 synthesis and dependency DAG say the QFT route is upstream of
quotient/descent and CHSH work. The next object is the source-defined raw
branch/local gauge groupoid packet with a non-import screen.

The 1602 QFT cycle 1 and cycle 2 artifacts derive the useful schema:

```text
b, O, O_prime
iota_b
U_b(O), U_b(O_prime)
R_raw^b(O), R_raw^b(O_prime)
G_b(O), G_b(O_prime)
gamma_O, gamma_O_prime
res_R, res_G
restriction-stability certificate
packet-level non-import screen
```

They also explicitly decide that the schema is not a receipt: `iota_b`,
`R_raw^b(O)`, `G_b(O)`, restrictions, and the commuting-square proof remain
absent as source-defined fields.

The Type II_1 spectral SM checklist and extension requirements provide adjacent
control discipline, not this QFT packet. They state requirements for a Type
II_1 or semifinite spectral-SM extension, including trace, Breuer-Fredholm
index, KO/reality, subfactor data, recovery, and spectral action convergence.
They do not emit a GU branch label, observed-source injection, raw-field packet,
local gauge groupoid, or restriction-stability square for `R_raw^b(O)`.

## 3. The strongest positive result

The strongest positive result is a **reusable admission matrix** for the packet.
It is strong because it cleanly separates three things that were previously easy
to conflate:

| required field | source-defined from read sources | schema-defined | import/downstream risk | admission decision |
|---|---:|---:|---:|---|
| branch label `b` | no | yes | yes, if selected by desired QFT sector | reject as receipt |
| injection/selector `iota_b` | no | yes | yes, if chosen to land in target finite data | reject as receipt |
| local domains `U_b(O)`, `U_b(O')` | no | yes | yes, if inferred from target quotient | reject as receipt |
| local raw fields `R_raw^b(O)`, `R_raw^b(O')` | no | yes | yes, if populated from ordinary QFT fields | reject as receipt |
| local gauge groupoids `G_b(O)`, `G_b(O')` | no | yes | yes, if imported from standard gauge theory | reject as receipt |
| action on raw fields `gamma` | no | yes | yes, if standard action is pasted in | reject as receipt |
| restriction maps `res_R`, `res_G` | no | yes | yes, if fitted to make descent work | reject as receipt |
| restriction-stability proof | no | yes as target theorem shape | yes, if proved only after quotient choice | reject as receipt |
| non-import screen | no as packet receipt | yes as schema gate | no import detected in this lane | active but not sufficient |

This is constructive: it tells the next worker exactly what a positive packet
must supply, and it prevents target QFT controls from masquerading as source
definitions.

## 4. The first exact obstruction or missing proof/source object

The first exact obstruction is:

```text
SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1 is not present.
```

The first missing subobject remains:

```text
source_defined_iota_b_and_typed_R_raw_b_O
```

This is first because `iota_b` anchors `U_b(O)` in the source branch, and
`R_raw^b(O)` gives `G_b(O)` an action domain. Without those two source-defined
objects, the local gauge groupoid, action, restrictions, and restriction square
are only typed placeholders.

## 5. The constructive next object that would remove or test the obstruction

Construct:

```text
SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1
```

Minimum acceptance contents:

```text
1. source provenance for every packet field;
2. branch label b and branch admissibility rule;
3. observed regions O_prime subset O;
4. source-defined iota_b: O -> Y or equivalent observed pullback;
5. source local domains U_b(O), U_b(O_prime);
6. typed R_raw^b(O), R_raw^b(O_prime), with components and admissibility;
7. local gauge groupoids G_b(O), G_b(O_prime), with object/morphism classes;
8. gamma action on every declared raw field component;
9. restriction maps res_R and res_G preserving declared classes;
10. componentwise proof that action and restriction commute;
11. non-import screen rejecting QFT target selectors.
```

Then run:

```text
GaugeOrbitGeneratorRestrictionTest_V1
```

That test is not licensed until the packet exists.

## 6. What this means for the QFT/GU claim

The QFT/GU route remains pre-recovery. The repo can now say precisely what
source-defined packet is missing, but it cannot claim that GU has produced a
local raw branch, a local gauge groupoid, a physical quotient, a finite
extraction, or a Bell/CHSH state.

The Type II_1 path remains adjacent and potentially useful as a control
framework, but it does not supply the missing raw branch packet. A semifinite
spectral triple, a principal graph, or a Breuer-Fredholm index cannot be used as
the selector for `b`, `iota_b`, `R_raw^b(O)`, or `G_b(O)` unless a separate
source bridge derives those fields.

## 7. Next meaningful proof or computation step

Run a bounded source-locator/classifier for exactly the packet fields:

```text
QFTSourceFieldLocatorClassificationForIotaRRawG_V1
```

It should enumerate every mention of `b`, `iota_b`, `R_raw`, `G_b`, `res_R`,
`res_G`, and `gamma`, then classify each as:

```text
source_definition | schema_template | analogy | downstream_target | import_control
```

The packet may be admitted only if every required field has a
`source_definition` row and the non-import screen passes.

## 8. Machine-readable JSON summary

```json
{
  "artifact_id": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_1702_C1_L5_V1",
  "target_packet_id": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
  "run_id": "hourly-20260625-1702",
  "cycle": 1,
  "lane": 5,
  "owned_path": "explorations/hourly-20260625-1702-cycle1-qft-raw-branch-local-gauge-groupoid-packet.md",
  "companion_audit": "tests/hourly_20260625_1702_cycle1_qft_raw_branch_local_gauge_groupoid_packet_audit.py",
  "verdict": "UNDERDEFINED_REQUIRED_SOURCE_FIELDS_ABSENT_NON_IMPORT_SCREEN_ACTIVE",
  "verdict_class": "underdefined",
  "accepted_receipt_count": 0,
  "source_defined_packet_present": false,
  "all_required_fields_source_defined": false,
  "schema_or_template_present": true,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "target_import_used_as_source_selector": false,
  "required_field_matrix": [
    {"field": "branch_label_b", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "injection_selector_iota_b", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "local_domains_U_b_O_and_U_b_O_prime", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "local_raw_field_space_R_raw_b_O_and_R_raw_b_O_prime", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "local_gauge_groupoids_G_b_O_and_G_b_O_prime", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "action_gamma_on_raw_fields", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "restriction_maps_res_R_and_res_G", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "restriction_stability_certificate", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "reject_as_receipt"},
    {"field": "packet_level_non_import_screen", "source_defined": false, "schema_defined": true, "import_used": false, "downstream_selector_allowed": false, "admission": "active_but_not_sufficient"}
  ],
  "source_defined_vs_schema_import_booleans": {
    "branch_label_b_source_defined": false,
    "iota_b_source_defined": false,
    "R_raw_b_O_source_defined": false,
    "G_b_O_source_defined": false,
    "restriction_maps_source_defined": false,
    "action_source_defined": false,
    "non_import_screen_packet_receipt_present": false,
    "minimal_schema_defined": true,
    "compatibility_template_present": true,
    "import_used_for_any_required_field": false
  },
  "non_import_screen": {
    "status": "active_no_target_import_detected_but_no_packet_receipt",
    "reject_if_selected_by": [
      "F_phys",
      "P_fin",
      "rho_AB",
      "Bell",
      "CHSH",
      "Pauli_settings",
      "target_Hilbert_data",
      "target_density_matrix",
      "ordinary_QFT_recovery_requirement",
      "standard_SM_representation_labels",
      "imported_positive_pairing",
      "finite_target_correlations"
    ],
    "source_selectors_used": [],
    "forbidden_source_selectors_used": []
  },
  "downstream_locks": {
    "restriction_stability_test_allowed": false,
    "gauge_generator_promotion_allowed": false,
    "quotient_descent_allowed": false,
    "finite_extraction_allowed": false,
    "F_phys_allowed": false,
    "P_fin_allowed": false,
    "rho_AB_allowed": false,
    "Bell_allowed": false,
    "CHSH_allowed": false
  },
  "first_obstruction": {
    "id": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_absent",
    "missing": true,
    "first_missing_subobject": "source_defined_iota_b_and_typed_R_raw_b_O",
    "reason": "iota_b anchors U_b(O), typed R_raw^b(O) supplies the action domain for G_b(O), and both are needed before restrictions, action stability, or non-import admission can be tested."
  },
  "next_object": {
    "id": "QFTSourceFieldLocatorClassificationForIotaRRawG_V1",
    "description": "Classify every occurrence of b, iota_b, R_raw, G_b, gamma, res_R, and res_G as source_definition, schema_template, analogy, downstream_target, or import_control.",
    "acceptance_followup": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
    "then_test": "GaugeOrbitGeneratorRestrictionTest_V1"
  },
  "promotion_firewall": {
    "promotion_allowed": false,
    "claim_promotion_blocked": true,
    "proof_restart_allowed": false,
    "no_quotient_descent_before_packet": true,
    "no_finite_extraction_before_packet": true,
    "no_rho_AB_Bell_CHSH_as_source_selector": true,
    "type_ii1_requirements_not_substitute_packet": true
  }
}
```
