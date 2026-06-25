---
title: "Hourly 20260625 1602 Cycle 3 Next Frontier Dependency DAG"
date: "2026-06-25"
run_id: "hourly-20260625-1602"
cycle: 3
lane: 5
doc_type: next_frontier_dependency_dag
artifact_id: "NextFrontierDependencyDagAfter1602_C3_L5_V1"
verdict: "NEXT_FRONTIER_UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART"
owned_path: "explorations/hourly-20260625-1602-cycle3-next-frontier-dependency-dag.md"
companion_audit: "tests/hourly_20260625_1602_cycle3_next_frontier_dependency_dag_audit.py"
---

# Hourly 20260625 1602 Cycle 3 Next Frontier Dependency DAG

## 1. Verdict.

Verdict: **next frontier remains upstream source/proof object production; no
receipt has been accepted and no proof restart is allowed**.

Cycle 1 and cycle 2 did not close any of the five producer routes. They did,
however, sharpen each route into an exact next source/proof object. The next
parallel batch should therefore not repeat broad metadata scans, compatibility
reviews, or downstream proof replay. It should run five disjoint producer lanes:

1. PTUJ accepted source-object branch receipt, followed only later by formula
   visibility.
2. Raw/formal D7 branching transcript for the Shiab Hom-space.
3. Oxford/manuscript/UCSD source-surface receipt for the source-emitted actual
   DGU 0/1 identity packet.
4. RS source-safe capture or fully documented unavailability pass for
   `fBozSSLxFvI` `[00:32:07]-[00:37:41]`.
5. QFT source-defined raw branch/local gauge groupoid packet with a non-import
   screen.

Run-level decision:

```text
accepted_receipt_count: 0
proof_restart_allowed: false
target_import_used: false
claim_promotion_allowed: false
next_parallel_batch_allowed: yes, but only for disjoint upstream producer lanes
downstream_replay_allowed: no
```

## 2. Evidence base read.

The DAG was built from the posture/runbook controls plus all cycle 1 and cycle 2
1602 lane artifacts.

| source | controlling evidence used |
|---|---|
| `RESEARCH-POSTURE.md` | GU reconstruction is the optimization target, but compatibility, locator continuity, and hidden target import cannot become derivation. |
| `process/runbooks/five-lane-frontier-run.md` | A frontier lane must name the first exact missing source/proof object and avoid proof replay before admission. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | The next bank must keep quality holes, dependencies, and anti-overlap explicit; weak padding is forbidden. |
| `explorations/hourly-20260625-1602-cycle1-ptuj-lawful-byte-manifest-continuation.md` | PTUJ still lacks both official/custodian source asset and lawful local byte/toolchain/output manifest. |
| `explorations/hourly-20260625-1602-cycle2-ptuj-source-object-admission-packet.md` | Both PTUJ branches were rejected/blocked; next object is one accepted branch receipt, not formula visibility. |
| `explorations/hourly-20260625-1602-cycle1-ig-d7-proof-transcript-object.md` | IG has typed Shiab positives and chirality exclusions, but no raw/formal D7 proof transcript. |
| `explorations/hourly-20260625-1602-cycle2-ig-raw-formal-d7-branching-transcript-admission.md` | No candidate supplies full B-product summands, multiplicities, dimensions, or FC gate verdicts. |
| `explorations/hourly-20260625-1602-cycle1-dgu-expanded-identity-field-source-scope-bundle.md` | DGU has adjacent Oxford/manuscript/UCSD positives and scoped negatives, but no actual DGU 0/1 identity packet. |
| `explorations/hourly-20260625-1602-cycle2-dgu-source-emitted-actual-01-identity-packet-gate.md` | Strict DGU gate remains blocked; the first missing field is the source-emitted sector rule. |
| `explorations/hourly-20260625-1602-cycle1-rs-visual-frame-capture-or-unavailability-packet.md` | RS has transcript window and stable locator, but no frames, crops, OCR, or typed RS operator. |
| `explorations/hourly-20260625-1602-cycle2-rs-visual-route-unavailability-strengthening-gate.md` | Repo-local absence is documented, but not a full visual unavailability packet. |
| `explorations/hourly-20260625-1602-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid.md` | QFT has a compatibility template only; `iota_b` and typed `R_raw^b(O)` remain absent. |
| `explorations/hourly-20260625-1602-cycle2-qft-source-defined-branch-packet-minimal-schema.md` | Minimal source-defined packet schema and non-import gate are specified, but no packet is admitted. |

## 3. Candidate bank and quality filter.

Quality filter used here: a candidate counts only if it names an exact
source object, proof object, admission packet, source-surface receipt,
unavailability packet, or bounded downstream gate whose resolution would
materially change GU reconstruction routing. A summary-only review, repeated
metadata search, compatibility essay, or downstream proof replay from zero
receipts is not counted.

| id | quality decision | why it matters |
|---|---|---|
| `PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT` | immediate producer | It is the first PTUJ object that can turn locator/provenance into inspectable source content. |
| `PTUJ_OFFICIAL_CUSTODIAN_SOURCE_ASSET_MANIFEST` | alternate producer | It can close the official branch if it supplies content access, custody/checksum, and visibility scope. |
| `PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST` | alternate producer | It can close the local branch if exact bytes, toolchain, decode scope, and checksummed outputs are supplied. |
| `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT` | sequential | It cannot run before one PTUJ branch receipt is accepted. |
| `PTUJ_KEATING_SHEET_IDENTITY_AFTER_VISIBILITY` | sequential | It needs a formula-bearing or formula-negative PTUJ visibility decision first. |
| `IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | immediate producer | It is the first proof object that can decide `FC-IRR`, `FC-MULT`, and `FC-HW`. |
| `IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE` | support/sequential | Cycle 2 identified missing product B data as the first IG obstruction. |
| `IG_PRODUCT_A_KERNEL_IRREDUCIBILITY_AND_HIGHEST_WEIGHT_PACKET` | support/sequential | It supplies the `ker(c)` irreducibility/highest-weight fields needed for `FC-IRR` and `FC-HW`. |
| `IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT` | sequential | It cannot identify the selector family before finite D7 admission. |
| `IG_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY` | sequential | It prevents chirality-only screening from being treated as full uniqueness. |
| `DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT` | immediate producer | It is the narrowest source-surface receipt that can admit or reject the actual DGU 0/1 packet. |
| `DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT` | support/sequential | Cycle 2 named the sector rule as the first missing DGU field. |
| `DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE` | support/sequential | It tests domain, codomain, coefficients, Q/projector relation, symbol, and family identity as one same-operator packet. |
| `DGU_BROADER_NEGATIVE_PRIMARY_SOURCE_RECEIPT` | sequential | It is allowed only after the declared Oxford/manuscript/UCSD source surface has been inspected. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | sequential | Symbol replay is forbidden until the actual identity packet is accepted. |
| `RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS` | immediate producer | It distinguishes the two next RS outcomes: checksummed visual packet or full source/tool/access unavailability. |
| `RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW` | alternate producer | It can supply frames, crops, OCR, visible operator fields, and checksums. |
| `RS_UCSD_VISUAL_UNAVAILABILITY_PACKET_FULL_COVERAGE` | alternate producer | It can document official video, slide, archive, local inventory, and tool/access failures. |
| `RS_FRAME_OCR_OPERATOR_FIELD_TABLE` | sequential | It requires captured frames/crops/OCR first. |
| `RS_TYPED_MINUS_ONE_OPERATOR_INTAKE` | sequential | It cannot start from transcript/locator evidence alone. |
| `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT` | immediate producer | It is the first packet that can turn the QFT template into source-defined branch data. |
| `QFT_SOURCE_LOCATOR_CLASSIFICATION_FOR_IOTA_RRAW_G` | support/sequential | It enumerates mentions of `b`, `iota_b`, `R_raw`, `G_b`, and restrictions as source/candidate/downstream/import. |
| `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | sequential | It is not runnable until the source-defined packet exists. |
| `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | sequential | It must wait for a source-defined restriction-stable gauge action. |
| `QFT_PFIN_RHO_CHSH_FIREWALL` | demoted guard | Useful as a lock, but lower value than producing the upstream packet. |
| `GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL` | demoted guard | Important run discipline, but not a producer lane. |

Quality candidates claimed: **26**. The immediate next five are the five
producer lanes, not the support, sequential, or demoted guard lanes.

## 4. Next five parallel-safe lanes.

| lane | recommended object | owned-surface description | source/proof object to produce | why parallel-safe |
|---|---|---|---|---|
| A | `PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT` | PTUJ `TzSEvmqxu48` official/custodian source asset or lawful local byte/toolchain/output branch only. | `PTUJ_SourceObjectAdmissionPacket_1602_V1.accepted_branch_receipt` with exactly one accepted branch and no target import. | It touches PTUJ media/source-object admission only and does not inspect formulas until a receipt exists. |
| B | `IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | D7 finite representation proof/transcript surface for the Shiab Hom-space only. | `RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1` with full A/B summands, multiplicities, dimensions, kernel, highest weight, and FC verdicts. | It is pure finite D7 proof data and does not depend on PTUJ, DGU, RS, or QFT source acquisition. |
| C | `DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT` | Oxford bosonic anchors, 2021 manuscript sections 8-12, and UCSD rolled-family windows only. | `OxfordManuscriptUCSDSourceSurfaceReceiptForSourceEmittedActualDGU01IdentityPacket_V1`. | It consumes DGU source-surface evidence and explicitly excludes VZ replay or typed-spine promotion. |
| D | `RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS` | UCSD visual route for `fBozSSLxFvI` `[00:32:07]-[00:37:41]` only. | Either `UCSDFrameSequenceForRolledOperatorWindow_V1` or `UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1`. | It is a visual capture/unavailability lane and does not decide typed RS or generation/index claims. |
| E | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT` | QFT branch packet fields `b`, `iota_b`, `U_b(O)`, `R_raw^b(O)`, `G_b(O)`, restrictions, and non-import screen only. | `SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1` or an explicit field-by-field source absence decision. | It is source-branch schema admission and does not run quotient, finite extraction, or CHSH work. |

## 5. Sequential/dependent lanes to defer.

| deferred lane | must wait for | reason |
|---|---|---|
| `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT` | `PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT` | There is no inspectable PTUJ source content yet. |
| `PTUJ_KEATING_SHEET_IDENTITY_AFTER_VISIBILITY` | `PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT` | Identity comparison requires a formula-bearing or formula-negative PTUJ result. |
| `IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE` | `IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | It audits or extracts the B-product data from the transcript/proof object. |
| `IG_PRODUCT_A_KERNEL_IRREDUCIBILITY_AND_HIGHEST_WEIGHT_PACKET` | `IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | It supplies the kernel data only after finite D7 conventions/output are fixed. |
| `IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT` | `IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE` | Family identity is downstream of finite selector admission. |
| `IG_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY` | `IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT` | Rival elimination requires an accepted selector-family candidate. |
| `DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT` | `DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT` | The sector rule must be extracted from the inspected source surface. |
| `DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE` | `DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT` | Same-operator domain/codomain/coefficient/Q/symbol fields need the sector rule first. |
| `DGU_BROADER_NEGATIVE_PRIMARY_SOURCE_RECEIPT` | `DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT` | A broader negative requires declared source coverage. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | `DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE` | Symbol replay is forbidden without an accepted actual identity packet. |
| `RS_FRAME_OCR_OPERATOR_FIELD_TABLE` | `RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS` | It needs frames/crops/OCR or a full unavailability decision. |
| `RS_TYPED_MINUS_ONE_OPERATOR_INTAKE` | `RS_FRAME_OCR_OPERATOR_FIELD_TABLE` | Typed RS fields cannot be read from transcript/locator alone. |
| `QFT_SOURCE_LOCATOR_CLASSIFICATION_FOR_IOTA_RRAW_G` | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT` | It is useful as a fallback or subpass if the producer lane cannot find source definitions directly. |
| `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT` | The restriction square needs source-defined `R_raw`, `G_b`, actions, and restrictions. |
| `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | `QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST` | Quotient/descent should begin only after source-defined restriction stability. |
| `QFT_PFIN_RHO_CHSH_FIREWALL` | `QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP` | Finite QFT/Bell work is downstream and cannot select the raw branch. |

## 6. Dependency edges and anti-overlap notes.

Explicit dependency edges:

```text
PTUJ_SourceObjectAdmissionPacket_1602_V1
  -> PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT
  -> PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT
  -> PTUJ_KEATING_SHEET_IDENTITY_AFTER_VISIBILITY

IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_ADMISSION_1602_C2_L2_V1
  -> IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE
  -> IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE
  -> IG_PRODUCT_A_KERNEL_IRREDUCIBILITY_AND_HIGHEST_WEIGHT_PACKET
  -> IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT
  -> IG_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY

SourceEmittedActualDGU01IdentityPacket_V1
  -> DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT
  -> DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT
  -> DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE
  -> DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET

DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT
  -> DGU_BROADER_NEGATIVE_PRIMARY_SOURCE_RECEIPT

RSVisualRouteUnavailabilityStrengtheningGate_1602_C2_L4_V1
  -> RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS
  -> RS_FRAME_OCR_OPERATOR_FIELD_TABLE
  -> RS_TYPED_MINUS_ONE_OPERATOR_INTAKE

SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_MinimalSchema_1602_C2_L5
  -> QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT
  -> QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST
  -> QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP
  -> QFT_PFIN_RHO_CHSH_FIREWALL
```

Anti-overlap notes:

- PTUJ owns only `TzSEvmqxu48` source-object admission. It must not run formula
  visibility or Keating identity until a branch receipt exists.
- IG owns only finite D7 transcript/proof admission. It must not use PTUJ,
  generation count, or target uniqueness to select the Hom-space route.
- DGU owns only the Oxford/manuscript/UCSD actual identity packet surface. It
  must not run VZ replay, symbol certification, or typed-spine promotion.
- RS owns only source-safe visual capture or full documented unavailability for
  the UCSD window. It must not promote transcript/locator evidence to typed RS.
- QFT owns only source-defined raw branch/local gauge groupoid admission. It
  must not run physical quotient, finite extraction, `rho_AB`, Bell, or CHSH
  lanes as source selectors.
- The five recommended lanes have disjoint source surfaces and write scopes:
  PTUJ media asset admission; D7 proof transcript; DGU source-surface receipt;
  UCSD RS visual capture/unavailability; QFT raw branch packet.

## 7. Machine-readable JSON summary.

```json
{
  "artifact_id": "NextFrontierDependencyDagAfter1602_C3_L5_V1",
  "run_id": "hourly-20260625-1602",
  "cycle": 3,
  "lane": 5,
  "verdict": "NEXT_FRONTIER_UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART",
  "verdict_class": "blocked",
  "quality_candidates_claimed": 26,
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "claim_promotion_allowed": false,
  "recommended_next_five": [
    {
      "id": "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT",
      "route_family": "PTUJ",
      "owned_surface_description": "PTUJ TzSEvmqxu48 official/custodian source asset or lawful local byte/toolchain/output branch only",
      "produce": "PTUJ_SourceObjectAdmissionPacket_1602_V1.accepted_branch_receipt",
      "must_not_do": "formula visibility audit or Keating identity before one source branch is accepted"
    },
    {
      "id": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "route_family": "IG",
      "owned_surface_description": "D7 finite representation proof/transcript surface for the Shiab Hom-space only",
      "produce": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
      "must_not_do": "use target physics, generation count, or desired uniqueness as transcript evidence"
    },
    {
      "id": "DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT",
      "route_family": "DGU",
      "owned_surface_description": "Oxford bosonic anchors plus 2021 manuscript sections 8-12 plus UCSD rolled-family windows only",
      "produce": "OxfordManuscriptUCSDSourceSurfaceReceiptForSourceEmittedActualDGU01IdentityPacket_V1",
      "must_not_do": "restart VZ replay or promote the typed spine before the actual packet is accepted"
    },
    {
      "id": "RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS",
      "route_family": "RS",
      "owned_surface_description": "UCSD visual route for fBozSSLxFvI [00:32:07]-[00:37:41] only",
      "produce": "UCSDFrameSequenceForRolledOperatorWindow_V1 or UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1",
      "must_not_do": "promote transcript or locator evidence to a typed pure-RS operator"
    },
    {
      "id": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT",
      "route_family": "QFT",
      "owned_surface_description": "QFT source branch fields b, iota_b, U_b(O), R_raw^b(O), G_b(O), restrictions, and non-import screen only",
      "produce": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
      "must_not_do": "run quotient, finite extraction, rho_AB, Bell, or CHSH work as source selectors"
    }
  ],
  "quality_candidates": [
    "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT",
    "PTUJ_OFFICIAL_CUSTODIAN_SOURCE_ASSET_MANIFEST",
    "PTUJ_LAWFUL_LOCAL_BYTE_TOOLCHAIN_OUTPUT_MANIFEST",
    "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT",
    "PTUJ_KEATING_SHEET_IDENTITY_AFTER_VISIBILITY",
    "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
    "IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE",
    "IG_PRODUCT_A_KERNEL_IRREDUCIBILITY_AND_HIGHEST_WEIGHT_PACKET",
    "IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT",
    "IG_RIVAL_ROW_ELIMINATION_AFTER_FAMILY_IDENTITY",
    "DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT",
    "DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT",
    "DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE",
    "DGU_BROADER_NEGATIVE_PRIMARY_SOURCE_RECEIPT",
    "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
    "RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS",
    "RS_UCSD_FRAME_SEQUENCE_FOR_ROLLED_OPERATOR_WINDOW",
    "RS_UCSD_VISUAL_UNAVAILABILITY_PACKET_FULL_COVERAGE",
    "RS_FRAME_OCR_OPERATOR_FIELD_TABLE",
    "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE",
    "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT",
    "QFT_SOURCE_LOCATOR_CLASSIFICATION_FOR_IOTA_RRAW_G",
    "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
    "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP",
    "QFT_PFIN_RHO_CHSH_FIREWALL",
    "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL"
  ],
  "sequential_deferred": [
    {
      "id": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT",
      "wait_for": "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT",
      "reason": "no inspectable PTUJ source content exists yet"
    },
    {
      "id": "PTUJ_KEATING_SHEET_IDENTITY_AFTER_VISIBILITY",
      "wait_for": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT",
      "reason": "identity comparison needs an accepted visibility result"
    },
    {
      "id": "IG_PRODUCT_B_FULL_SUMMAND_MULTIPLICITY_DIMENSION_TABLE",
      "wait_for": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "reason": "product B data must come from the admitted transcript or proof"
    },
    {
      "id": "IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT",
      "wait_for": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "reason": "selector family identity is downstream of finite D7 admission"
    },
    {
      "id": "DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT",
      "wait_for": "DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT",
      "reason": "cycle 2 named source-emitted sector rule as the first missing DGU field"
    },
    {
      "id": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
      "wait_for": "DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE",
      "reason": "symbol replay requires an accepted actual same-operator packet"
    },
    {
      "id": "RS_FRAME_OCR_OPERATOR_FIELD_TABLE",
      "wait_for": "RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS",
      "reason": "field extraction needs frames/crops/OCR or a full unavailability decision"
    },
    {
      "id": "RS_TYPED_MINUS_ONE_OPERATOR_INTAKE",
      "wait_for": "RS_FRAME_OCR_OPERATOR_FIELD_TABLE",
      "reason": "typed RS cannot start from transcript or locator evidence alone"
    },
    {
      "id": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
      "wait_for": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT",
      "reason": "the restriction square needs source-defined raw fields and local gauge groupoids"
    },
    {
      "id": "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP",
      "wait_for": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
      "reason": "quotient/descent must wait for source-defined restriction-stable gauge action"
    }
  ],
  "dependency_edges": [
    {
      "from": "PTUJ_SourceObjectAdmissionPacket_1602_V1",
      "to": "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT",
      "kind": "producer_admission"
    },
    {
      "from": "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT",
      "to": "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT",
      "kind": "sequential_visibility_after_receipt"
    },
    {
      "from": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_ADMISSION_1602_C2_L2_V1",
      "to": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "kind": "same_missing_proof_object_sharpened"
    },
    {
      "from": "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
      "to": "IG_K_IG_FAMILY_IDENTITY_AFTER_D7_TRANSCRIPT",
      "kind": "family_identity_after_finite_admission"
    },
    {
      "from": "SourceEmittedActualDGU01IdentityPacket_V1",
      "to": "DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT",
      "kind": "source_surface_receipt_for_actual_packet"
    },
    {
      "from": "DGU_OXFORD_MANUSCRIPT_UCSD_SOURCE_SURFACE_RECEIPT",
      "to": "DGU_SOURCE_EMITTED_SECTOR_RULE_RECEIPT",
      "kind": "first_missing_field"
    },
    {
      "from": "DGU_ACTUAL_01_IDENTITY_PACKET_FIELD_TABLE",
      "to": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
      "kind": "symbol_certificate_after_accepted_packet"
    },
    {
      "from": "RSVisualRouteUnavailabilityStrengtheningGate_1602_C2_L4_V1",
      "to": "RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS",
      "kind": "source_tool_access_pass"
    },
    {
      "from": "RS_SOURCE_SAFE_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PASS",
      "to": "RS_FRAME_OCR_OPERATOR_FIELD_TABLE",
      "kind": "operator_fields_after_visual_packet"
    },
    {
      "from": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_MinimalSchema_1602_C2_L5",
      "to": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT",
      "kind": "minimal_schema_to_source_packet"
    },
    {
      "from": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT",
      "to": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
      "kind": "restriction_test_after_packet"
    },
    {
      "from": "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
      "to": "QFT_PHYSICAL_QUOTIENT_DESCENT_SETUP",
      "kind": "quotient_after_restriction_stability"
    }
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
      "details": "PTUJ media branch, D7 transcript, DGU source-surface receipt, RS UCSD visual window, and QFT source branch packet are distinct surfaces"
    },
    {
      "check": "no_downstream_replay_in_recommended_lanes",
      "passed": true,
      "details": "formula visibility, VZ symbol replay, typed RS intake, quotient/descent, and CHSH work are deferred"
    },
    {
      "check": "no_target_import",
      "passed": true,
      "details": "each recommended lane carries a no-target-import guard"
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
    "accepted_PTUJ_source_branch_receipt_then_visibility_audit",
    "accepted_IG_raw_or_formal_D7_branching_transcript",
    "accepted_DGU_source_emitted_actual_01_identity_packet",
    "accepted_RS_visual_frame_packet_with_typed_fields",
    "accepted_QFT_source_defined_raw_branch_local_gauge_groupoid_packet_and_restriction_stability"
  ]
}
```
