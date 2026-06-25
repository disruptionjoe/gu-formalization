---
title: "Hourly 20260625 1702 Cycle 3 Next Frontier Dependency DAG"
date: "2026-06-25"
run_id: "hourly-20260625-1702"
cycle: 3
lane: 5
doc_type: next_frontier_dependency_dag
artifact_id: "NextFrontierDependencyDagAfter1702_C3_L5_V1"
verdict: "NEXT_FRONTIER_REMAINS_UPSTREAM_PRODUCER_OBJECTS_ZERO_RECEIPTS"
owned_path: "explorations/hourly-20260625-1702-cycle3-next-frontier-dependency-dag.md"
companion_audit: "tests/hourly_20260625_1702_cycle3_next_frontier_dependency_dag_audit.py"
---

# Hourly 20260625 1702 Cycle 3 Next Frontier Dependency DAG

## 1. Verdict.

Verdict: **next frontier remains upstream producer-object construction; zero
accepted receipts means no proof restart and no downstream proof replay**.

The 1702 cycle 1/2 artifacts did not admit any PTUJ, IG, DGU, RS, or QFT
receipt. They did improve the dependency graph: every route now has a sharper
first missing source/proof object and a finite field matrix. The next batch
should therefore run five disjoint producer lanes, not downstream theorem
replay.

Run-level decision:

```text
accepted_receipt_count: 0
proof_restart_allowed: false
target_import_used: false
claim_promotion_allowed: false
downstream_replay_allowed: false
next_parallel_batch_allowed: yes, but only for disjoint upstream producer lanes
```

Recommended next five producer/admission lanes:

1. PTUJ branch field completion receipt.
2. IG raw/formal D7 branching transcript.
3. DGU source-emitted actual 0/1 same-operator packet.
4. RS UCSD capture-stack execution ledger.
5. QFT source-defined raw branch/local gauge groupoid packet.

## 2. Evidence base.

| source | controlling evidence used |
|---|---|
| `RESEARCH-POSTURE.md` | GU reconstruction is the target, but compatibility, locator continuity, and hidden target import cannot become derivation. |
| `process/runbooks/five-lane-frontier-run.md` | Frontier lanes must identify exact missing proof/source objects and avoid hosted-to-derived promotion. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | Candidate banks must preserve dependencies, anti-overlap rules, and quality filters; padding is forbidden. |
| `explorations/hourly-20260625-1602-cycle3-next-frontier-dependency-dag.md` | The prior DAG established the five upstream producer families and the zero-receipt proof-restart firewall. |
| `explorations/hourly-20260625-1702-cycle1-ptuj-accepted-source-object-branch-receipt.md` | PTUJ still has zero accepted official/custodian or lawful-local source branch receipts. |
| `explorations/hourly-20260625-1702-cycle2-ptuj-branch-field-completion-matrix.md` | PTUJ blocker is now a two-branch missing-field matrix; next object is `PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT`. |
| `explorations/hourly-20260625-1702-cycle1-ig-raw-formal-d7-branching-transcript.md` | IG lacks admitted raw CAS transcript or formal D7 proof; product B is the first finite-data obstruction. |
| `explorations/hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md` | IG next object remains `RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1`, with product B table first. |
| `explorations/hourly-20260625-1702-cycle1-dgu-actual-01-source-surface-receipt.md` | DGU source surfaces are adjacent-only; no source-emitted actual identity packet is admitted. |
| `explorations/hourly-20260625-1702-cycle2-dgu-sector-rule-same-operator-matrix.md` | DGU first missing field is the source-emitted sector rule for the same-operator packet. |
| `explorations/hourly-20260625-1702-cycle1-rs-source-safe-capture-unavailability-pass.md` | RS has reachable official locator and exact window but no frames/OCR/checksums and no full unavailability packet. |
| `explorations/hourly-20260625-1702-cycle2-rs-capture-stack-unavailability-ledger.md` | RS first obstruction is missing source bytes or lawful acquisition route; next object is capture-stack execution. |
| `explorations/hourly-20260625-1702-cycle1-qft-raw-branch-local-gauge-groupoid-packet.md` | QFT has schema/template data only; `iota_b` and typed `R_raw^b(O)` are not source-defined. |
| `explorations/hourly-20260625-1702-cycle2-qft-source-field-locator-classification.md` | QFT locator classification remains schema-only; next object is a source-defined packet with non-import receipt. |

## 3. Candidate bank and quality filter.

Quality filter: a candidate counts only if it names an exact source object,
proof object, admission packet, row extraction, unavailability packet, finite
transcript field, or bounded downstream gate whose resolution would materially
change GU reconstruction routing. Guard-only locks are useful but lower
priority than producing upstream objects.

| id | class | why it matters |
|---|---|---|
| `PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT` | immediate parallel-safe producer | It is the first PTUJ object that can raise `accepted_receipt_count` from zero. |
| `PTUJ_OFFICIAL_CUSTODIAN_FORMULA_SOURCE_ASSET_PACKET` | parallel-safe alternate within PTUJ, not same batch with local branch | It can complete the official branch if it supplies asset kind, content access, checksum/custody, and visibility scope. |
| `PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST` | parallel-safe alternate within PTUJ, not same batch with official branch | It can complete the local branch if it supplies lawful bytes, toolchain identity, decode scope, outputs, and checksums. |
| `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH` | sequential deferred | It cannot begin before exactly one accepted PTUJ source branch exists. |
| `PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY` | sequential deferred | It needs accepted formula-bearing or formula-negative visibility result first. |
| `IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | immediate parallel-safe producer | It is the only IG object that can decide `FC-IRR`, `FC-MULT`, and `FC-HW`. |
| `IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE` | support/sequential | Cycle 2 names this as the first finite obstruction for `FC-MULT`. |
| `IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET` | support/sequential | It is needed for `FC-IRR` and `FC-HW` after D7 conventions/output are fixed. |
| `IG_RAW_CAS_TOOLCHAIN_RECEIPT_OR_FORMAL_PROOF_IDENTITY` | support lane | It supplies tool/proof provenance for an admissible transcript. |
| `IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT` | sequential deferred | It cannot identify the selector family before finite transcript admission. |
| `IG_FULL_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY` | sequential deferred | Chirality exclusions are not full uniqueness; this waits for accepted finite data. |
| `DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET` | immediate parallel-safe producer | It is the first DGU object that can admit the actual 0/1 operator used by DGU/VZ. |
| `DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT` | support/sequential | It is the first missing same-operator field. |
| `DGU_OXFORD_FRAME_SLIDE_TRANSCRIPT_ROW_EXTRACTION_AROUND_BOSONIC_ANCHORS` | support lane | It can supply or refute the source row needed by the same-operator matrix. |
| `DGU_NEGATIVE_PRIMARY_SOURCE_RECEIPT_FOR_SAME_OPERATOR_PACKET` | sequential deferred | It is valid only after complete acquired Oxford/manuscript/UCSD coverage is documented. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | sequential deferred | Symbol replay is forbidden before an actual same-operator packet exists. |
| `DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET` | sequential deferred | VZ replay must wait for the admitted packet and symbol relation. |
| `RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW` | immediate parallel-safe producer | It can deterministically emit either a frame/OCR packet or a complete unavailability packet. |
| `RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE` | support lane | It is the first missing field upstream of both RS branches. |
| `RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST` | sequential deferred | It depends on successful capture. |
| `RS_FULL_VISUAL_UNAVAILABILITY_PACKET` | sequential/alternate deferred | It depends on a non-transient capture denial plus archive/slide/local/tool coverage. |
| `RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISUAL_FIELDS` | sequential deferred | It requires visible fields; transcript/locator evidence is not enough. |
| `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | immediate parallel-safe producer | It is the first QFT object that can turn schema-only rows into admitted source fields. |
| `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT` | support/sequential | It is the first missing field set for the QFT packet. |
| `QFT_G_B_ACTION_RESTRICTION_COMPONENT_LAW_PACKET` | sequential deferred | It needs source-defined `iota_b` and `R_raw^b(O)` first. |
| `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | sequential deferred | It should run only after the full source-defined packet exists. |
| `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | sequential deferred | Quotient/descent waits for restriction-stable source-defined gauge action. |
| `QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL` | demoted guard | Important as a lock, but not a producer lane. |
| `GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL` | demoted guard | Important discipline, but it does not produce a receipt. |
| `GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH` | demoted guard | Useful integration check, lower priority than source/proof-object construction. |

Quality candidates claimed: **30**. The immediate next five are the five
producer/admission lanes. Support lanes can be embedded as sub-obligations or
run later if a producer lane needs a narrower extraction step.

## 4. Next five parallel-safe lanes.

| lane | recommended object | owned source surface | source/proof object to produce | why parallel-safe |
|---|---|---|---|---|
| A | `PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT` | PTUJ `TzSEvmqxu48` official/custodian asset branch or lawful local byte/toolchain branch only. | Exactly one accepted PTUJ branch row with all required fields present and no metadata-as-receipt promotion. | It touches PTUJ media/source-object admission only and forbids formula visibility before receipt. |
| B | `IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | Finite D7 representation proof/transcript surface for the Shiab Hom-space only. | Raw CAS receipt or formal proof for products A and B, including product B full table, `FC-IRR`, `FC-MULT`, and `FC-HW`. | It is finite representation data and does not depend on PTUJ, DGU, RS, or QFT source acquisition. |
| C | `DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET` | Oxford frames/slides/transcript rows around bosonic anchors, cross-indexed with manuscript Sections 8-12 and UCSD zero/one-form family language. | Source-emitted sector rule, actual `D_GU^epsilon` identity, domain/codomain, coefficients, Q/projector relation, symbol relation, family identity, and same-operator witness. | It consumes DGU source rows and explicitly excludes VZ replay, typed-spine substitution, and symbol certification until admission. |
| D | `RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW` | UCSD/Keating video `fBozSSLxFvI` `[00:32:07]-[00:37:41]` visual acquisition surface only. | Either `UCSDFrameSequenceForRolledOperatorWindow_V1` with frame/crop/OCR/checksums or full `UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1`. | It is a capture/unavailability lane and does not decide typed RS, generation, or index claims. |
| E | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | QFT source branch fields `b`, `iota_b`, `U_b(O)`, `R_raw^b(O)`, `G_b(O)`, actions, restrictions, and packet-level non-import receipt only. | `SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1`, starting with source-defined `iota_b` and typed `R_raw^b(O)`. | It is source-field admission and does not run quotient, finite extraction, `rho_AB`, Bell, or CHSH. |

## 5. Sequential lanes to defer.

| deferred lane | must wait for | reason |
|---|---|---|
| `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH` | `PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT` | There is no inspectable PTUJ source content yet. |
| `PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY` | `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH` | Identity comparison requires visibility outcome and checksummed source/output content. |
| `IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE` | `IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | Product B data must be admitted as part of, or extracted from, the transcript/proof object. |
| `IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET` | `IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | Kernel/cokernel and highest-weight claims need the transcript/proof convention and output. |
| `IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT` | `IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | Family identity is downstream of finite selector admission. |
| `IG_FULL_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY` | `IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT` | Rival elimination requires an accepted selector-family candidate. |
| `DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT` | `DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET` | It is a required subfield; if absent, the whole packet remains blocked. |
| `DGU_NEGATIVE_PRIMARY_SOURCE_RECEIPT_FOR_SAME_OPERATOR_PACKET` | complete acquired Oxford/manuscript/UCSD source surface | A broader negative needs explicit source-window coverage and rollback conditions. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | `DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET` | Symbol replay requires an accepted actual same-operator packet. |
| `DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET` | `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | VZ replay depends on accepted operator identity and symbol relation. |
| `RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST` | `RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW` | Frame/OCR work requires a successful capture route. |
| `RS_FULL_VISUAL_UNAVAILABILITY_PACKET` | failed capture execution plus complete archive/slide/local/tool ledger | Official locator is reachable, so unavailability needs stronger coverage. |
| `RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISUAL_FIELDS` | `RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST` | Typed RS fields cannot be read from transcript/locator evidence alone. |
| `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT` | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | This is the first packet subobject, not a downstream proof replay lane. |
| `QFT_G_B_ACTION_RESTRICTION_COMPONENT_LAW_PACKET` | `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT` | Local gauge groupoid/action laws need a source-defined raw field domain. |
| `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | Restriction-stability proof needs all source-defined packet fields. |
| `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | Quotient/descent must wait for source-defined restriction-stable action. |

## 6. Demoted guard lanes.

These remain valuable checks but should not consume producer slots in the next
five-lane batch unless a coordinator explicitly converts them into an audit
attached to a producer lane.

| guard | demotion reason |
|---|---|
| `QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL` | It prevents target import but cannot source-define `iota_b` or `R_raw^b(O)`. |
| `GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL` | It is already enforced by every route; it is not a source/proof object producer. |
| `GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH` | Useful after artifacts return, but lower priority than producing missing receipts. |
| `DGU_TYPED_SPINE_SUBSTITUTION_FIREWALL` | Important as a DGU guard; should be embedded in the DGU packet lane. |
| `RS_TRANSCRIPT_LOCATOR_PROMOTION_FIREWALL` | Important as an RS guard; should be embedded in the RS capture lane. |
| `PTUJ_METADATA_AS_RECEIPT_FIREWALL` | Important as a PTUJ guard; should be embedded in the PTUJ branch receipt lane. |

## 7. Dependency edges and anti-overlap rules.

Explicit dependency edges:

```text
PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1
  -> PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT
  -> PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH
  -> PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY

IG_FINITE_TRANSCRIPT_ADMISSION_MATRIX_1702_C2_L2_V1
  -> IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE
  -> IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE
  -> IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET
  -> IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT
  -> IG_FULL_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY

DGUSectorRuleSameOperatorAdmissionMatrix_V1
  -> DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET
  -> DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT
  -> DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET
  -> DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET

DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET
  -> DGU_NEGATIVE_PRIMARY_SOURCE_RECEIPT_FOR_SAME_OPERATOR_PACKET

RSCaptureStackUnavailabilityLedger_1702_C2_L4_V1
  -> RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW
  -> RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST
  -> RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISUAL_FIELDS

RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW
  -> RS_FULL_VISUAL_UNAVAILABILITY_PACKET

QFTSourceFieldLocatorClassificationForIotaRRawG_1702_C2_L5_V1
  -> QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET
  -> QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT
  -> QFT_G_B_ACTION_RESTRICTION_COMPONENT_LAW_PACKET
  -> QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST
  -> QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP
```

Anti-overlap rules for the next producer batch:

- PTUJ owns only `TzSEvmqxu48` branch field completion. It must not run formula
  visibility, Keating identity, or IG selector comparisons until one branch is
  accepted.
- IG owns only finite D7 transcript/proof admission. It must not use target
  generation count, desired uniqueness, PTUJ data, or GU success as evidence.
- DGU owns only source-emitted actual 0/1 same-operator packet admission. It
  must not substitute the typed spine, run VZ replay, or issue symbol
  certificates before packet admission.
- RS owns only source-safe capture or full visual unavailability for
  `fBozSSLxFvI` `[00:32:07]-[00:37:41]`. It must not promote transcript or
  locator evidence to a typed pure-RS operator.
- QFT owns only source-defined raw branch/local gauge groupoid packet
  admission. It must not run physical quotient, finite extraction, `rho_AB`,
  Bell, or CHSH work as source selectors.
- The five recommended route families and source surfaces are disjoint:
  PTUJ media branch; IG finite D7 proof transcript; DGU source row/same-operator
  packet; RS UCSD visual acquisition; QFT source-defined raw branch packet.

## 8. Machine-readable JSON summary.

```json
{
  "artifact_id": "NextFrontierDependencyDagAfter1702_C3_L5_V1",
  "run_id": "hourly-20260625-1702",
  "cycle": 3,
  "lane": 5,
  "verdict": "NEXT_FRONTIER_REMAINS_UPSTREAM_PRODUCER_OBJECTS_ZERO_RECEIPTS",
  "verdict_class": "blocked",
  "quality_candidates_claimed": 30,
  "accepted_receipt_count": 0,
  "proof_restart": false,
  "proof_restart_allowed": false,
  "target_import": false,
  "target_import_used": false,
  "claim_promotion_allowed": false,
  "downstream_replay_allowed": false,
  "recommended_next_five": [
    {
      "id": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
      "route_family": "PTUJ",
      "owned_surface": "PTUJ_TzSEvmqxu48_branch_field_completion",
      "owned_surface_description": "PTUJ TzSEvmqxu48 official/custodian asset branch or lawful local byte/toolchain branch only",
      "produce": "one accepted PTUJ branch row with all required fields present",
      "must_not_do": "formula visibility, Keating identity, metadata-as-receipt promotion, or proof restart before receipt",
      "anti_overlap_guard": "PTUJ-only media/source-object admission"
    },
    {
      "id": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "route_family": "IG",
      "owned_surface": "finite_D7_Shiab_Hom_space_transcript",
      "owned_surface_description": "D7 finite representation proof/transcript surface for the Shiab Hom-space only",
      "produce": "raw CAS receipt or formal proof with product A and B tables and FC verdicts",
      "must_not_do": "use target generation count, desired uniqueness, or GU success as representation-theory evidence",
      "anti_overlap_guard": "IG-only finite proof object"
    },
    {
      "id": "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET",
      "route_family": "DGU",
      "owned_surface": "DGU_Oxford_manuscript_UCSD_same_operator_source_rows",
      "owned_surface_description": "Oxford rows around bosonic anchors cross-indexed with manuscript Sections 8-12 and UCSD zero/one-form family language",
      "produce": "SourceEmittedActualDGU01SameOperatorPacket_V1 or scoped negative receipt",
      "must_not_do": "typed-spine substitution, VZ replay, or symbol certificate before accepted packet",
      "anti_overlap_guard": "DGU-only same-operator source row extraction"
    },
    {
      "id": "RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW",
      "route_family": "RS",
      "owned_surface": "RS_UCSD_fBozSSLxFvI_visual_window",
      "owned_surface_description": "UCSD/Keating video fBozSSLxFvI [00:32:07]-[00:37:41] visual acquisition surface only",
      "produce": "UCSDFrameSequenceForRolledOperatorWindow_V1 or UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1",
      "must_not_do": "promote transcript or locator evidence to typed RS, generation, or index claim",
      "anti_overlap_guard": "RS-only visual capture/unavailability"
    },
    {
      "id": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET",
      "route_family": "QFT",
      "owned_surface": "QFT_source_defined_raw_branch_packet_fields",
      "owned_surface_description": "QFT source branch fields b, iota_b, U_b(O), R_raw^b(O), G_b(O), actions, restrictions, and non-import receipt only",
      "produce": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
      "must_not_do": "run quotient, finite extraction, rho_AB, Bell, or CHSH work as source selectors",
      "anti_overlap_guard": "QFT-only source-field admission"
    }
  ],
  "quality_candidates": [
    "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
    "PTUJ_OFFICIAL_CUSTODIAN_FORMULA_SOURCE_ASSET_PACKET",
    "PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST",
    "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH",
    "PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY",
    "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
    "IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE",
    "IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET",
    "IG_RAW_CAS_TOOLCHAIN_RECEIPT_OR_FORMAL_PROOF_IDENTITY",
    "IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT",
    "IG_FULL_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY",
    "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET",
    "DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT",
    "DGU_OXFORD_FRAME_SLIDE_TRANSCRIPT_ROW_EXTRACTION_AROUND_BOSONIC_ANCHORS",
    "DGU_NEGATIVE_PRIMARY_SOURCE_RECEIPT_FOR_SAME_OPERATOR_PACKET",
    "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
    "DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET",
    "RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW",
    "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
    "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST",
    "RS_FULL_VISUAL_UNAVAILABILITY_PACKET",
    "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISUAL_FIELDS",
    "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET",
    "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT",
    "QFT_G_B_ACTION_RESTRICTION_COMPONENT_LAW_PACKET",
    "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
    "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP",
    "QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL",
    "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL",
    "GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH"
  ],
  "immediate_parallel_safe_lanes": [
    "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
    "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
    "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET",
    "RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW",
    "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET"
  ],
  "support_lanes": [
    "PTUJ_OFFICIAL_CUSTODIAN_FORMULA_SOURCE_ASSET_PACKET",
    "PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST",
    "IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE",
    "IG_PRODUCT_A_KERNEL_COKERNEL_HIGHEST_WEIGHT_PACKET",
    "IG_RAW_CAS_TOOLCHAIN_RECEIPT_OR_FORMAL_PROOF_IDENTITY",
    "DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT",
    "DGU_OXFORD_FRAME_SLIDE_TRANSCRIPT_ROW_EXTRACTION_AROUND_BOSONIC_ANCHORS",
    "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
    "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT"
  ],
  "sequential_deferred": [
    {
      "id": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH",
      "wait_for": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
      "reason": "no inspectable PTUJ source content exists until one branch is accepted"
    },
    {
      "id": "PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY",
      "wait_for": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH",
      "reason": "identity comparison needs accepted visibility outcome"
    },
    {
      "id": "IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE",
      "wait_for": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "reason": "product B table must be admitted as transcript/proof data"
    },
    {
      "id": "IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT",
      "wait_for": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "reason": "selector family identity is downstream of finite admission"
    },
    {
      "id": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
      "wait_for": "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET",
      "reason": "symbol certificate requires actual same-operator packet"
    },
    {
      "id": "DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET",
      "wait_for": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
      "reason": "VZ replay depends on accepted operator identity and symbol relation"
    },
    {
      "id": "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST",
      "wait_for": "RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW",
      "reason": "frame/OCR manifest requires successful capture execution"
    },
    {
      "id": "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISUAL_FIELDS",
      "wait_for": "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST",
      "reason": "typed RS requires visible operator fields"
    },
    {
      "id": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
      "wait_for": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET",
      "reason": "restriction-stability proof needs source-defined packet fields"
    },
    {
      "id": "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP",
      "wait_for": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
      "reason": "quotient/descent waits for source-defined restriction-stable action"
    }
  ],
  "demoted_guard_lanes": [
    "QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL",
    "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL",
    "GLOBAL_TARGET_IMPORT_AUDIT_FOR_NEXT_BATCH",
    "DGU_TYPED_SPINE_SUBSTITUTION_FIREWALL",
    "RS_TRANSCRIPT_LOCATOR_PROMOTION_FIREWALL",
    "PTUJ_METADATA_AS_RECEIPT_FIREWALL"
  ],
  "dependency_edges": [
    {"from": "PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1", "to": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT", "kind": "producer_admission"},
    {"from": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT", "to": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH", "kind": "sequential_visibility_after_receipt"},
    {"from": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_ACCEPTED_BRANCH", "to": "PTUJ_KEATING_IDENTITY_COMPARISON_AFTER_VISIBILITY", "kind": "identity_after_visibility"},
    {"from": "IG_FINITE_TRANSCRIPT_ADMISSION_MATRIX_1702_C2_L2_V1", "to": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE", "kind": "finite_transcript_producer"},
    {"from": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE", "to": "IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE", "kind": "first_finite_obstruction"},
    {"from": "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE", "to": "IG_K_IG_FAMILY_IDENTITY_AFTER_TRANSCRIPT", "kind": "family_identity_after_finite_admission"},
    {"from": "DGUSectorRuleSameOperatorAdmissionMatrix_V1", "to": "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET", "kind": "same_operator_packet_producer"},
    {"from": "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET", "to": "DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT", "kind": "first_missing_field"},
    {"from": "DGU_SOURCE_EMITTED_ACTUAL_01_SAME_OPERATOR_PACKET", "to": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET", "kind": "symbol_certificate_after_packet"},
    {"from": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET", "to": "DGU_VZ_REPLAY_AFTER_ACCEPTED_SAME_OPERATOR_PACKET", "kind": "vz_replay_after_symbol"},
    {"from": "RSCaptureStackUnavailabilityLedger_1702_C2_L4_V1", "to": "RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW", "kind": "capture_stack_producer"},
    {"from": "RS_UCSD_CAPTURE_STACK_EXECUTION_LEDGER_FOR_ROLLED_OPERATOR_WINDOW", "to": "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST", "kind": "frame_manifest_after_capture"},
    {"from": "RS_FRAME_CROP_OCR_CHECKSUM_MANIFEST", "to": "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE_AFTER_VISUAL_FIELDS", "kind": "typed_rs_after_visible_fields"},
    {"from": "QFTSourceFieldLocatorClassificationForIotaRRawG_1702_C2_L5_V1", "to": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET", "kind": "source_packet_producer"},
    {"from": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET", "to": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT", "kind": "first_missing_field_set"},
    {"from": "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_SUBOBJECT", "to": "QFT_G_B_ACTION_RESTRICTION_COMPONENT_LAW_PACKET", "kind": "action_domain_before_groupoid_laws"},
    {"from": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET", "to": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST", "kind": "restriction_test_after_packet"},
    {"from": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST", "to": "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP", "kind": "quotient_after_restriction_stability"}
  ],
  "anti_overlap_checks": [
    {
      "check": "route_family_disjoint",
      "passed": true,
      "details": "recommended lanes cover PTUJ, IG, DGU, RS, and QFT exactly once"
    },
    {
      "check": "owned_surface_descriptions_disjoint",
      "passed": true,
      "details": "PTUJ media branch, finite D7 transcript, DGU same-operator source rows, RS visual acquisition, and QFT source-field packet are distinct surfaces"
    },
    {
      "check": "no_downstream_replay_in_recommended_lanes",
      "passed": true,
      "details": "formula visibility, Keating identity, K_IG family identity, VZ replay, typed RS intake, quotient/descent, and CHSH work are deferred"
    },
    {
      "check": "no_target_import",
      "passed": true,
      "details": "each recommended lane carries a no-target-import guard"
    },
    {
      "check": "no_same_mathematical_question_duplicates",
      "passed": true,
      "details": "each lane asks a different source/proof-object admission question"
    }
  ],
  "accepted_receipt_count_by_route": {
    "PTUJ": 0,
    "IG": 0,
    "DGU": 0,
    "RS": 0,
    "QFT": 0
  },
  "proof_restart_forbidden_until": [
    "accepted_PTUJ_branch_field_completion_receipt_then_visibility_audit",
    "accepted_IG_raw_or_formal_D7_branching_transcript",
    "accepted_DGU_source_emitted_actual_01_same_operator_packet",
    "accepted_RS_visual_frame_packet_with_visible_operator_fields",
    "accepted_QFT_source_defined_raw_branch_local_gauge_groupoid_packet_and_restriction_stability"
  ]
}
```
