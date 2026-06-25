---
title: "Hourly 20260625 2028 Cycle 2 QFT Iota R Raw Before Groupoid"
date: "2026-06-25"
run_id: "hourly-20260625-2028"
cycle: 2
lane: 5
doc_type: admission_order_firewall
artifact_id: "QFTIotaRRawBeforeGroupoid_2028_C2_L5_V1"
verdict: "underdefined"
owned_path: "explorations/hourly-20260625-2028-cycle2-qft-iota-rraw-before-groupoid.md"
---

# Hourly 20260625 2028 Cycle 2 QFT Iota R Raw Before Groupoid

## 1. Verdict

Verdict: **underdefined**.

Cycle 1 confirmed that source-defined `iota_b` and typed `R_raw^b(O)` are
absent. Those fields must precede `G_b(O)`, action/restriction laws,
quotient/descent, finite extraction, `rho_AB`, Bell, CHSH, and proof restart.

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260625-2028-cycle1-qft-iota-rraw-delta-receipt.md` | Current underdefined source-field result. |
| `explorations/hourly-20260625-1802-cycle2-qft-source-field-upgrade-gate.md` | Prior schema/downstream upgrade denial. |
| `explorations/mission-a-qft-state-space-extraction-2026-06-24.md` | Positive QFT context, not a source-field receipt. |

## 3. Strongest Positive Construction Attempt

The valid order is:

```text
QFTSourceDefinedIotaBAndTypedRRawBOReceipt_V1
  -> QFTSourceDefinedGBOAndActionDomainPacket_V1
  -> QFTComponentActionRestrictionLawPacket_V1
  -> QFTPhysicalQuotientDescentSetup
```

The first object is absent.

## 4. First Exact Obstruction

The first obstruction is object-level underdefinition. No source map `iota_b`
anchors the branch-local domain, and no typed `R_raw^b(O)` supplies the action
domain.

## 5. Constructive Next Object

Construct or source-cite `iota_b` and `R_raw^b(O)` with non-import provenance.

## 6. Claim-Status Consistency Result

No QFT claim status changes. No quotient, finite, Bell, or CHSH claim is
promoted.

## 7. Next Meaningful Step

Do not define the groupoid from ordinary-QFT targets. First define the raw
source fields.

## 8. Machine-readable JSON summary

```json
{
  "artifact_id": "QFTIotaRRawBeforeGroupoid_2028_C2_L5_V1",
  "run_id": "hourly-20260625-2028",
  "cycle": 2,
  "lane": 5,
  "route": "QFT",
  "artifact_path": "explorations/hourly-20260625-2028-cycle2-qft-iota-rraw-before-groupoid.md",
  "owned_path": "explorations/hourly-20260625-2028-cycle2-qft-iota-rraw-before-groupoid.md",
  "decision_target": "QFT_IOTA_RRAW_BEFORE_GROUPOID_FIREWALL",
  "verdict_class": "underdefined",
  "admission_firewall": true,
  "accepted_receipt_count": 0,
  "upstream_required": "QFTSourceDefinedIotaBAndTypedRRawBOReceipt_V1",
  "downstream_blocked": [
    "QFTSourceDefinedGBOAndActionDomainPacket_V1",
    "QFTComponentActionRestrictionLawPacket_V1",
    "QFTPhysicalQuotientDescentSetup",
    "rho_AB_Bell_CHSH_or_finite_extraction"
  ],
  "invalid_bypasses": [
    "schema_only_upgrade",
    "ordinary_QFT_recovery_as_source_selector",
    "quotient_descent_before_source_fields",
    "finite_extraction_as_source_selector",
    "rho_AB_Bell_CHSH_as_source_selector"
  ],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "target_import_used": false,
  "claim_status_consistency_triggered": false
}
```
