---
title: "Hourly 20260625 1802 Cycle 3 Next Frontier Dependency DAG"
date: "2026-06-25"
run_id: "hourly-20260625-1802"
cycle: 3
lane: 5
doc_type: next_frontier_dependency_dag
artifact_id: "NextFrontierDependencyDagAfter1802_C3_L5_V1"
verdict: "NEXT_FRONTIER_REMAINS_UPSTREAM_PRODUCER_ADMISSION_ZERO_RECEIPTS"
owned_path: "explorations/hourly-20260625-1802-cycle3-next-frontier-dependency-dag.md"
companion_audit: "tests/hourly_20260625_1802_cycle3_next_frontier_dependency_dag_audit.py"
---

# Hourly 20260625 1802 Cycle 3 Next Frontier Dependency DAG

## 1. Verdict.

Verdict: **next frontier remains upstream producer/admission; do not move to
downstream proof replay**.

The 1802 producer and admission gates sharpened the next frontier but admitted
zero receipts. No PTUJ branch, IG Product B transcript, DGU sector/same-operator
packet, RS capture/unavailability branch, or QFT source-field packet is accepted.
That keeps proof restart and downstream replay locked.

Run-level decision:

```text
accepted_receipt_count: 0
proof_restart_allowed: false
target_import_used: false
claim_promotion_allowed: false
downstream_replay_allowed: false
recommended_batch_kind: upstream producer/admission
```

Recommended next five quality lanes:

1. PTUJ single complete branch receipt.
2. IG/ProductB full D7 summand multiplicity dimension receipt.
3. DGU sector-rule plus same-operator source receipt.
4. RS capture/acquisition branch route.
5. QFT iota/R_raw field receipt.

These are not repeats of weak or padded lanes. They are the smallest named
producer/admission objects now exposed by the 1802 gates.

## 2. Evidence base.

| source | controlling evidence used |
|---|---|
| `RESEARCH-POSTURE.md` | GU reconstruction remains the target, but target import, compatibility, and hosted structure are not derivations. |
| `process/runbooks/five-lane-frontier-run.md` | Each lane must name the exact missing proof/source object and avoid downstream replay before admission. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | Candidate banks must distinguish immediate, sequential, overlapping, and demoted lanes; padding is forbidden. |
| `explorations/hourly-20260625-1702-cycle3-next-frontier-dependency-dag.md` | Format and prior zero-receipt firewall only. |
| `explorations/hourly-20260625-1802-cycle1-ptuj-branch-field-completion-receipt.md` | PTUJ admitted zero branches; official and lawful-local rows both miss required fields. |
| `explorations/hourly-20260625-1802-cycle2-ptuj-single-branch-nonconflation-gate.md` | PTUJ must produce one complete branch receipt; cross-branch assembly is rejected. |
| `explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md` | IG lacks admitted raw/formal D7 transcript; Product B full table is the first obstruction. |
| `explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md` | Product B cannot be bypassed by Product A partials, chirality exclusions, or desired multiplicity. |
| `explorations/hourly-20260625-1802-cycle1-dgu-source-emitted-actual-01-same-operator-packet.md` | DGU lacks source-emitted sector rule and same-operator witness. |
| `explorations/hourly-20260625-1802-cycle2-dgu-sector-rule-root-admission-gate.md` | DGU root gate requires sector-rule plus same-operator receipt before symbol or VZ replay. |
| `explorations/hourly-20260625-1802-cycle1-rs-ucsd-capture-stack-execution-ledger.md` | RS capture did not execute because source bytes or lawful acquisition route is missing. |
| `explorations/hourly-20260625-1802-cycle2-rs-capture-unavailability-branch-gate.md` | Neither positive frame branch nor negative visual-denial branch is admitted. |
| `explorations/hourly-20260625-1802-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid-packet.md` | QFT source-defined packet is absent; first missing field set is `iota_b` and typed `R_raw^b(O)`. |
| `explorations/hourly-20260625-1802-cycle2-qft-source-field-upgrade-gate.md` | Schema-only and downstream selector upgrades are denied; source-defined iota/R_raw must come first. |

## 3. Updated quality candidate bank.

Quality filter: a candidate counts only if it names a source object, proof
object, receipt, transcript field, branch gate, or bounded downstream gate whose
resolution changes the reconstruction DAG. Guard-only locks are tracked but do
not take next-batch producer slots.

| id | class | why it matters |
|---|---|---|
| `PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT` | immediate producer | First PTUJ object capable of raising accepted receipt count from zero without cross-branch assembly. |
| `PTUJ_OFFICIAL_CUSTODIAN_FORMULA_SOURCE_ASSET_PACKET` | support producer | Supplies the official branch fields if the custodian asset exists. |
| `PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST` | support producer | Supplies the lawful-local branch fields if source bytes and tool outputs exist. |
| `PTUJ_BRANCH_CHECKSUM_CUSTODY_ROW` | support producer | Separates source-object custody from locator continuity. |
| `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH` | sequential deferred | Requires one accepted branch receipt first. |
| `PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY` | sequential deferred | Requires accepted visibility output first. |
| `IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT` | immediate producer | First IG obstruction; Product B cannot be bypassed. |
| `IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | support producer | Broader transcript can admit Product B plus Product A. |
| `IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET` | sequential/support | Needed after Product B for `FC-IRR` and `FC-HW`. |
| `IG_FC_IRR_FC_MULT_FC_HW_VERDICT_PACKET` | sequential deferred | Verdicts wait for Product B and Product A data. |
| `IG_K_IG_SELECTOR_FAMILY_IDENTITY_AFTER_FC_GATES` | sequential deferred | Selector identity waits for closed finite gates. |
| `IG_FULL_RIVAL_ROW_ELIMINATION_AFTER_SELECTOR_IDENTITY` | sequential deferred | Rival elimination is downstream of selector family identity. |
| `DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT` | immediate producer | Root DGU gate named by cycle 2; typed spine and VZ replay cannot bypass it. |
| `DGU_OXFORD_BOSONIC_ANCHOR_ROW_EXTRACTION` | support producer | Best source-row route for the sector/same-operator receipt. |
| `DGU_MANUSCRIPT_UCSD_CROSS_INDEX_FOR_ZERO_ONE_FORM_FAMILY` | support producer | Helps test whether source rows identify the same actual operator. |
| `DGU_ACTUAL_D_GU_EPSILON_0_1_FIELD_PACKET` | support/sequential | Packet fields require source-emitted sector rule and same-operator witness. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | sequential deferred | Symbol certification consumes an accepted packet. |
| `DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET` | sequential deferred | VZ replay is downstream of operator and symbol admission. |
| `RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE` | immediate producer | First RS missing object for both positive capture and negative branch evaluation. |
| `RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW` | sequential/support | Requires lawful acquisition or browser capture object. |
| `RS_UCSD_FULL_VISUAL_DENIAL_PACKET` | sequential/alternate | Requires complete denial coverage because the official locator is reachable. |
| `RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST` | sequential deferred | Requires captured frames before OCR/checksum work. |
| `RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISIBLE_FIELDS` | sequential deferred | Typed RS cannot start from transcript or locator evidence. |
| `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT` | immediate producer | First QFT source field receipt; schema/downstream upgrades are denied. |
| `QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET` | sequential/support | Requires source-defined `iota_b` and typed `R_raw^b(O)`. |
| `QFT_COMPONENT_ACTION_RESTRICTION_LAW_PACKET` | sequential deferred | Requires source-defined group/action fields. |
| `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | sequential deferred | Requires full source packet and component law. |
| `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | sequential deferred | Requires restriction-stable source-defined action. |
| `QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL` | demoted guard | Important anti-import lock, not a producer receipt. |
| `GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL` | demoted guard | Integration invariant, not a producer lane. |
| `GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH` | demoted guard | Useful audit, but lower priority than the five source/proof producers. |

Quality candidates claimed: **31**.

## 4. Immediate parallel-safe next lanes.

| lane | recommended object | source/proof object to produce | why parallel-safe |
|---|---|---|---|
| A | `PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT` | One complete official/custodian or lawful-local PTUJ branch receipt, with no mixed-branch assembly. | PTUJ-only source branch admission; no formula visibility or Keating identity. |
| B | `IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT` | Full Product B D7 summand multiplicity/dimension table or an admitted raw/formal transcript containing it. | Finite D7/ProductB proof object only; no target generation or selector-family restart. |
| C | `DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT` | Source-emitted sector rule plus same-operator witness for actual `D_GU^epsilon` 0/1 packet. | DGU source-row admission only; no typed-spine substitution, symbol certificate, or VZ replay. |
| D | `RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE` | Lawful acquisition/browser capture route for `fBozSSLxFvI` `[00:32:07]-[00:37:41]`, or evidence sufficient to start a full denial packet. | RS capture/acquisition only; no typed RS intake or transcript promotion. |
| E | `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT` | Source-defined `iota_b` and typed `R_raw^b(O)` receipt with explicit non-import provenance. | QFT raw field admission only; no quotient, finite extraction, `rho_AB`, Bell, or CHSH selection. |

Decision on downstream proof replay: **not allowed**. Every recommended lane is
a producer/admission lane. The batch may proceed in parallel only because the
five route families and owned source surfaces are disjoint.

## 5. Sequentially deferred lanes.

| deferred lane | must wait for | reason |
|---|---|---|
| `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH` | `PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT` | No inspectable PTUJ source content is admitted yet. |
| `PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY` | `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH` | Identity comparison requires accepted source visibility output. |
| `IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET` | `IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT` | Product B is first; Product A partials cannot bypass it. |
| `IG_FC_IRR_FC_MULT_FC_HW_VERDICT_PACKET` | Product B and Product A packets | FC verdicts require finite data, not desired multiplicity. |
| `IG_K_IG_SELECTOR_FAMILY_IDENTITY_AFTER_FC_GATES` | `IG_FC_IRR_FC_MULT_FC_HW_VERDICT_PACKET` | Selector-family identity is downstream of closed finite gates. |
| `DGU_ACTUAL_D_GU_EPSILON_0_1_FIELD_PACKET` | `DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT` | Actual packet fields need the root source receipt first. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | `DGU_ACTUAL_D_GU_EPSILON_0_1_FIELD_PACKET` | Symbol certification consumes an admitted operator packet. |
| `DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET` | `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | VZ replay is downstream proof replay. |
| `RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW` | `RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE` | Frames require lawful acquisition or browser capture object. |
| `RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISIBLE_FIELDS` | `RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST` | Typed RS requires visible operator fields. |
| `QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET` | `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT` | Group/action fields need source-defined raw domain. |
| `QFT_COMPONENT_ACTION_RESTRICTION_LAW_PACKET` | `QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET` | Component law needs source-defined group/action data. |
| `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | Quotient/descent waits for restriction-stable source-defined action. |

## 6. Demoted guard lanes.

| guard | demotion reason |
|---|---|
| `GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL` | Already enforced by all routes; not a producer. |
| `GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH` | Important integration check, but it should attach to returned producer artifacts. |
| `PTUJ_METADATA_AND_CROSS_BRANCH_ASSEMBLY_FIREWALL` | Should be embedded in the PTUJ lane. |
| `IG_DESIRED_MULTIPLICITY_AND_GENERATION_TARGET_FIREWALL` | Should be embedded in the IG/ProductB lane. |
| `DGU_TYPED_SPINE_AND_VZ_REPLAY_FIREWALL` | Should be embedded in the DGU sector/same-operator lane. |
| `RS_TRANSCRIPT_LOCATOR_PROMOTION_FIREWALL` | Should be embedded in the RS capture/acquisition lane. |
| `QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL` | Should be embedded in the QFT iota/R_raw lane. |

## 7. Dependency edges.

```text
PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT_1802_C1_L1_V1
  -> PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1
  -> PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT
  -> PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH
  -> PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY

IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_1802_C1_L2_V1
  -> IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1
  -> IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT
  -> IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET
  -> IG_FC_IRR_FC_MULT_FC_HW_VERDICT_PACKET
  -> IG_K_IG_SELECTOR_FAMILY_IDENTITY_AFTER_FC_GATES

SourceEmittedActualDGU01SameOperatorPacket_V1
  -> DGUSectorRuleRootAdmissionGate_V1
  -> DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT
  -> DGU_ACTUAL_D_GU_EPSILON_0_1_FIELD_PACKET
  -> DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET
  -> DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET

UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_1802_C1_L4_V1
  -> RSCaptureUnavailabilityBranchGate_1802_C2_L4_V1
  -> RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE
  -> RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW
  -> RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST
  -> RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISIBLE_FIELDS

SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_1802_C1_L5_V1
  -> QFTSourceFieldUpgradeGate_1802_C2_L5_V1
  -> QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT
  -> QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET
  -> QFT_COMPONENT_ACTION_RESTRICTION_LAW_PACKET
  -> QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST
  -> QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP
```

Anti-overlap rules:

- PTUJ must not combine official metadata with lawful-local schema into one
  synthetic receipt.
- IG must not use Product A partials, chirality exclusions, desired
  multiplicity, or target generation count to bypass Product B.
- DGU must not use typed spine, symbol relation, or VZ replay to produce the
  missing source-emitted sector/same-operator receipt.
- RS must not promote transcript, locator, or failed local capture into a frame
  packet or visual-denial packet.
- QFT must not use schema, quotient/descent, finite extraction, `rho_AB`, Bell,
  CHSH, or ordinary-QFT recovery as source selectors.

## 8. Machine-readable JSON summary.

```json
{
  "artifact_id": "NextFrontierDependencyDagAfter1802_C3_L5_V1",
  "run_id": "hourly-20260625-1802",
  "cycle": 3,
  "lane": 5,
  "artifact_path": "explorations/hourly-20260625-1802-cycle3-next-frontier-dependency-dag.md",
  "owned_path": "explorations/hourly-20260625-1802-cycle3-next-frontier-dependency-dag.md",
  "companion_audit": "tests/hourly_20260625_1802_cycle3_next_frontier_dependency_dag_audit.py",
  "verdict": "NEXT_FRONTIER_REMAINS_UPSTREAM_PRODUCER_ADMISSION_ZERO_RECEIPTS",
  "verdict_class": "blocked",
  "recommended_batch_kind": "upstream_producer_admission",
  "quality_candidates_claimed": 31,
  "accepted_receipt_count": 0,
  "proof_restart": false,
  "proof_restart_allowed": false,
  "target_import": false,
  "target_import_used": false,
  "claim_promotion_allowed": false,
  "downstream_replay_allowed": false,
  "no_downstream_replay_in_recommended_lanes": true,
  "accepted_receipt_count_by_route": {
    "PTUJ": 0,
    "IG": 0,
    "DGU": 0,
    "RS": 0,
    "QFT": 0
  },
  "quality_candidates": [
    "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT",
    "PTUJ_OFFICIAL_CUSTODIAN_FORMULA_SOURCE_ASSET_PACKET",
    "PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST",
    "PTUJ_BRANCH_CHECKSUM_CUSTODY_ROW",
    "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH",
    "PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY",
    "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT",
    "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
    "IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET",
    "IG_FC_IRR_FC_MULT_FC_HW_VERDICT_PACKET",
    "IG_K_IG_SELECTOR_FAMILY_IDENTITY_AFTER_FC_GATES",
    "IG_FULL_RIVAL_ROW_ELIMINATION_AFTER_SELECTOR_IDENTITY",
    "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT",
    "DGU_OXFORD_BOSONIC_ANCHOR_ROW_EXTRACTION",
    "DGU_MANUSCRIPT_UCSD_CROSS_INDEX_FOR_ZERO_ONE_FORM_FAMILY",
    "DGU_ACTUAL_D_GU_EPSILON_0_1_FIELD_PACKET",
    "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
    "DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET",
    "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
    "RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW",
    "RS_UCSD_FULL_VISUAL_DENIAL_PACKET",
    "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST",
    "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISIBLE_FIELDS",
    "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT",
    "QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET",
    "QFT_COMPONENT_ACTION_RESTRICTION_LAW_PACKET",
    "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
    "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP",
    "QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL",
    "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL",
    "GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH"
  ],
  "recommended_next_five": [
    {
      "id": "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT",
      "route_family": "PTUJ",
      "owned_surface": "PTUJ_TzSEvmqxu48_single_branch_receipt",
      "produce": "one complete official/custodian or lawful-local PTUJ branch receipt with no cross-branch assembly",
      "must_not_do": "formula visibility, Keating identity, metadata-as-receipt, locator-continuity-as-receipt, or proof restart"
    },
    {
      "id": "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT",
      "route_family": "IG",
      "owned_surface": "IG_ProductB_D7_summand_multiplicity_dimension_table",
      "produce": "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1 or a raw/formal D7 transcript containing it",
      "must_not_do": "Product A partial bypass, chirality-only bypass, desired multiplicity import, target generation count, or selector-family restart"
    },
    {
      "id": "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT",
      "route_family": "DGU",
      "owned_surface": "DGU_sector_rule_same_operator_source_rows",
      "produce": "source-emitted sector rule plus same-operator witness for actual D_GU^epsilon 0/1 packet",
      "must_not_do": "typed-spine substitution, symbol certificate, VZ replay, or adjacent-surface promotion"
    },
    {
      "id": "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
      "route_family": "RS",
      "owned_surface": "RS_fBozSSLxFvI_capture_acquisition_window",
      "produce": "lawful source acquisition or browser capture route for fBozSSLxFvI [00:32:07]-[00:37:41], or evidence sufficient to start full visual denial",
      "must_not_do": "transcript promotion, locator promotion, failed-local-capture-as-unavailability, typed RS intake, generation restart, or index restart"
    },
    {
      "id": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT",
      "route_family": "QFT",
      "owned_surface": "QFT_source_defined_iota_and_R_raw_fields",
      "produce": "source-defined iota_b and typed R_raw^b(O) receipt with explicit non-import provenance",
      "must_not_do": "schema-only upgrade, quotient/descent, finite extraction, rho_AB, Bell, CHSH, or ordinary-QFT recovery as source selectors"
    }
  ],
  "immediate_parallel_safe_lanes": [
    "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT",
    "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT",
    "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT",
    "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
    "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT"
  ],
  "support_lanes": [
    "PTUJ_OFFICIAL_CUSTODIAN_FORMULA_SOURCE_ASSET_PACKET",
    "PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST",
    "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
    "DGU_OXFORD_BOSONIC_ANCHOR_ROW_EXTRACTION",
    "RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW",
    "QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET"
  ],
  "sequential_deferred": [
    {"id": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH", "wait_for": "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT", "reason": "source visibility requires one accepted branch"},
    {"id": "PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY", "wait_for": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH", "reason": "identity comparison requires accepted visibility output"},
    {"id": "IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET", "wait_for": "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT", "reason": "Product B is the first non-bypassable finite obstruction"},
    {"id": "IG_K_IG_SELECTOR_FAMILY_IDENTITY_AFTER_FC_GATES", "wait_for": "IG_FC_IRR_FC_MULT_FC_HW_VERDICT_PACKET", "reason": "selector identity waits for finite gates"},
    {"id": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET", "wait_for": "DGU_ACTUAL_D_GU_EPSILON_0_1_FIELD_PACKET", "reason": "symbol certificate consumes accepted operator packet"},
    {"id": "DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET", "wait_for": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET", "reason": "VZ replay is downstream proof replay"},
    {"id": "RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW", "wait_for": "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE", "reason": "frames require acquisition or browser capture"},
    {"id": "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISIBLE_FIELDS", "wait_for": "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST", "reason": "typed intake requires visible operator fields"},
    {"id": "QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET", "wait_for": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT", "reason": "group/action fields need source-defined raw domain"},
    {"id": "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP", "wait_for": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST", "reason": "quotient waits for restriction-stable source action"}
  ],
  "demoted_guard_lanes": [
    "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL",
    "GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH",
    "PTUJ_METADATA_AND_CROSS_BRANCH_ASSEMBLY_FIREWALL",
    "IG_DESIRED_MULTIPLICITY_AND_GENERATION_TARGET_FIREWALL",
    "DGU_TYPED_SPINE_AND_VZ_REPLAY_FIREWALL",
    "RS_TRANSCRIPT_LOCATOR_PROMOTION_FIREWALL",
    "QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL"
  ],
  "dependency_edges": [
    {"from": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT_1802_C1_L1_V1", "to": "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1", "kind": "admission_refinement"},
    {"from": "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1", "to": "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT", "kind": "producer_admission"},
    {"from": "PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT", "to": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH", "kind": "sequential_after_receipt"},
    {"from": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_1802_C1_L2_V1", "to": "IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1", "kind": "first_obstruction_refinement"},
    {"from": "IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1", "to": "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT", "kind": "producer_admission"},
    {"from": "IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT", "to": "IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET", "kind": "sequential_finite_gate"},
    {"from": "SourceEmittedActualDGU01SameOperatorPacket_V1", "to": "DGUSectorRuleRootAdmissionGate_V1", "kind": "root_gate_refinement"},
    {"from": "DGUSectorRuleRootAdmissionGate_V1", "to": "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT", "kind": "producer_admission"},
    {"from": "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT", "to": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET", "kind": "downstream_after_packet"},
    {"from": "UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_1802_C1_L4_V1", "to": "RSCaptureUnavailabilityBranchGate_1802_C2_L4_V1", "kind": "branch_gate_refinement"},
    {"from": "RSCaptureUnavailabilityBranchGate_1802_C2_L4_V1", "to": "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE", "kind": "producer_admission"},
    {"from": "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE", "to": "RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW", "kind": "frame_packet_after_acquisition"},
    {"from": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_1802_C1_L5_V1", "to": "QFTSourceFieldUpgradeGate_1802_C2_L5_V1", "kind": "upgrade_gate_refinement"},
    {"from": "QFTSourceFieldUpgradeGate_1802_C2_L5_V1", "to": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT", "kind": "producer_admission"},
    {"from": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT", "to": "QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET", "kind": "source_field_order"},
    {"from": "QFT_SOURCE_DEFINED_G_B_O_AND_ACTION_DOMAIN_PACKET", "to": "QFT_COMPONENT_ACTION_RESTRICTION_LAW_PACKET", "kind": "component_law_after_fields"}
  ],
  "anti_overlap_checks": [
    {"check": "route_family_disjoint", "passed": true, "details": "PTUJ, IG, DGU, RS, and QFT appear exactly once"},
    {"check": "owned_surface_descriptions_disjoint", "passed": true, "details": "single PTUJ branch, ProductB D7 table, DGU sector/same-operator rows, RS acquisition route, and QFT iota/R_raw fields are distinct"},
    {"check": "no_downstream_replay_in_recommended_lanes", "passed": true, "details": "visibility, Keating identity, selector identity, VZ replay, typed RS, quotient/descent, rho_AB, Bell, and CHSH are deferred or guarded"},
    {"check": "no_target_import", "passed": true, "details": "each recommended lane carries a no-target-import guard"},
    {"check": "no_same_mathematical_question_duplicates", "passed": true, "details": "each lane asks a different source/proof-object admission question"}
  ]
}
```
