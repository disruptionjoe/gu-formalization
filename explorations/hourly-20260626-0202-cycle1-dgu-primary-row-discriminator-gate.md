---
title: "Hourly 20260626 0202 Cycle 1 DGU Primary Row Discriminator Gate"
date: "2026-06-25"
run_id: "hourly-20260626-0202"
cycle: 1
lane: "DGU"
doc_type: "frontier_gate"
artifact_id: "DGUPrimaryRowDiscriminatorGate_0202_C1_DGU_V1"
verdict: "blocked_no_primary_row_payload_discriminator"
owned_path: "explorations/hourly-20260626-0202-cycle1-dgu-primary-row-discriminator-gate.md"
---

# Hourly 20260626 0202 Cycle 1 DGU Primary Row Discriminator Gate

## 1. Verdict

Verdict: **blocked**.

This lane tests whether the DGU frontier can admit a row discriminator that
separates a source-emitted 0/1 sector rule from typed `D_roll`, VZ replay
spines, or transcript-neighborhood language. It cannot. The discriminator
itself is missing because no primary row payload is present.

Decision state:

```text
target_import_used: false
typed_d_roll_available_as_screen: true
primary_source_row_instance_found: false
primary_row_payload_found: false
row_local_extraction_method_found: false
actual_operator_handle_found: false
row_discriminator_evaluable: false
same_operator_witness_evaluable: false
symbol_certificate_allowed: false
vz_replay_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260626-0103-cycle1-dgu-source-row-payload-gate.md` | Inherited the missing source-row payload. |
| `explorations/hourly-20260626-0103-cycle2-dgu-same-operator-source-row-firewall.md` | Inherited the same-operator order. |
| `explorations/time-as-finality-crosswalk/effect-typed-witness-transport-bidirectional-crosswalk-2026-06-25.md` | Checked typed witness quarantine language. |
| `explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md` | Applied source-to-shadow certificate discipline. |
| `RESEARCH-POSTURE.md` | Rejected compatibility as derivation. |

## 3. Strongest Positive Construction Attempt

The useful construction is a discriminator schema:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1:
  source_id
  exact_locator
  source_row_payload
  extraction_method_to_D_GU_epsilon_0_1_sector_rule
  actual_operator_handle
  typed_D_roll_comparison_policy
  target_import_screen
```

The typed `D_roll` row can remain a comparison screen only after a source row
exists. It cannot provide the source row or the discriminator because it is a
typed reconstruction artifact, not a primary row payload.

## 4. First Exact Obstruction

The first missing field is:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload
```

The first missing discriminator field is:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1.extraction_method_to_D_GU_epsilon_0_1_sector_rule
```

## 5. Constructive Next Object

The next object remains:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1
```

If the next source-mining pass remains negative, it should produce a scoped
negative receipt with exact source windows inspected. It should not produce a
global DGU no-go.

## 6. What This Means For The GU Claim

DGU cannot advance to same-operator, symbol certificate, VZ replay, or proof
restart work. The route is blocked at source-row admission, not at the typed
operator comparison layer.

## 7. Claim-Status Consistency Result

No claim status changes. No source row or downstream proof object is admitted.

## 8. JSON Summary

```json
{
  "artifact_id": "DGUPrimaryRowDiscriminatorGate_0202_C1_DGU_V1",
  "run_id": "hourly-20260626-0202",
  "cycle": 1,
  "lane": "DGU",
  "artifact_path": "explorations/hourly-20260626-0202-cycle1-dgu-primary-row-discriminator-gate.md",
  "verdict_class": "blocked_no_primary_row_payload_discriminator",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "typed_d_roll_available_as_screen": true,
  "primary_source_row_instance_found": false,
  "primary_row_payload_found": false,
  "row_local_extraction_method_found": false,
  "actual_operator_handle_found": false,
  "row_discriminator_evaluable": false,
  "same_operator_witness_evaluable": false,
  "symbol_certificate_allowed": false,
  "vz_replay_allowed": false,
  "proof_restart_allowed": false,
  "first_missing_field": "PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload",
  "first_missing_discriminator_field": "PrimarySourceDGU01SectorRuleRowInstance_V1.extraction_method_to_D_GU_epsilon_0_1_sector_rule",
  "constructive_next_object": "PrimarySourceDGU01SectorRuleRowInstance_V1"
}
```
