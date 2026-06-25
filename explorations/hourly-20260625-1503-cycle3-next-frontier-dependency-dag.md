---
title: "Hourly 20260625 1503 Cycle 3 Next Frontier Dependency DAG"
date: "2026-06-25"
run_id: "hourly-20260625-1503"
cycle: 3
lane: 5
doc_type: next_frontier_dependency_dag
artifact_id: "NextFrontierDependencyDagAfter1503_V1"
verdict: "UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART"
owned_path: "explorations/hourly-20260625-1503-cycle3-next-frontier-dependency-dag.md"
companion_audit: "tests/hourly_20260625_1503_cycle3_next_frontier_dependency_dag_audit.py"
---

# Hourly 20260625 1503 Cycle 3 Next Frontier Dependency DAG

## 1. Verdict

Verdict: **upstream source objects/no receipts/no proof restart**.

Cycle 1 commit `b1a2cc5` and cycle 2 commit `74090c4` sharpened the same five
source-object routes, but did not close any of them. The current frontier is
therefore still upstream source-object construction, not downstream proof replay.

Run-level decision:

```text
accepted_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
upstream_source_object_no_target_import_firewall: active
next_parallel_batch_allowed: yes, only for disjoint upstream source-object gates
next_parallel_batch_not_allowed_for: VZ replay, IG selector theorem replay,
  DGU symbol certificate, RS generation/index restart, QFT F_phys/P_fin/rho_AB/CHSH
```

The 1503 learnings are sharper than the 1302 DAG:

| route family | cycle 1 sharpened object | cycle 2 sharpened object | current blocker |
|---|---|---|---|
| PTUJ | lawful local source-byte/toolchain/output manifest absent | official/custodian branch metadata-only; no source asset | source bytes or official/custodian formula asset |
| IG | D7 transcript absent | formal proof object not admitted; chirality screen only | full D7 transcript/proof packet for `FC-IRR`, `FC-MULT`, `FC-HW` |
| DGU | identity-field receipt bundle stayed negative | scoped source-window negative for actual 0/1 packet | broader source-scope identity-field packet or bounded negative |
| RS | no repo-local frame sequence | stable locator present, but no frames/crops/OCR and no unavailability packet | capture visual frames or document non-transient unavailability |
| QFT | candidate gauge groupoid not promoted | source-observed raw branch underdefined | source-defined raw branch and local gauge groupoid packet |

The recommended next five are:

1. `PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION`
2. `IG_D7_PROOF_TRANSCRIPT_OBJECT`
3. `DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE`
4. `RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET`
5. `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET`

These five are parallel-safe because they consume disjoint source surfaces and
write disjoint outputs. They are not proof replays. They each attempt to supply
the first upstream object named by cycle 1 and cycle 2.

## 2. Candidate hole bank table

Quality bar used here: a candidate counts only if it names a missing source
object, proof transcript, formal packet, bounded negative receipt, branch
decision, or firewall whose resolution would materially change the GU
reconstruction map. Summary-only review and proof replay are not counted.

| id | candidate hole | run-now verdict | immediate dependencies | why quality |
|---|---|---|---|---|
| `PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION` | Continue from cycle 2 by obtaining either an official/custodian formula asset or a lawful local source-byte/toolchain/output manifest for `TzSEvmqxu48`. | immediate | `C1_PTUJ_SOURCE_BYTE_MANIFEST`, `C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH` | It is the only PTUJ gate that can enable visibility without metadata promotion. |
| `PTUJ_CUSTODIAN_REQUEST_PACKET` | Draft a precise custodian request for a source video package, still, sheet scan, or immutable source asset with checksum/custody fields. | immediate alternate | `C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH` | It tests the official branch without pretending oEmbed or thumbnails are assets. |
| `PTUJ_LOCAL_TOOLCHAIN_ADMISSION` | Admit or reject exact extractor/decoder executables, commands, lawful basis, source bytes, and output checksum manifest. | immediate alternate | `C1_PTUJ_SOURCE_BYTE_MANIFEST` | It could unblock a local visibility audit if lawful bytes are supplied. |
| `PTUJ_FORMULA_VISIBILITY_AUDIT` | Inspect accepted frames/source assets for formula-bearing, formula-negative, or insufficient-resolution status. | sequential | `PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION` | It must wait for real source content. |
| `PTUJ_KEATING_SHEET_IDENTITY` | Compare accepted PTUJ formula object to the Keating/Shiab projection sheet route. | sequential | `PTUJ_FORMULA_VISIBILITY_AUDIT` | It prevents formula identity from being inferred from locator continuity. |
| `IG_D7_PROOF_TRANSCRIPT_OBJECT` | Produce a raw LiE/Sage/FormalD7 proof transcript for `FC-IRR`, `FC-MULT`, and `FC-HW`. | immediate | `C1_IG_D7_MULTIPLICITY_TRANSCRIPT`, `C2_IG_D7_PROOF_OBJECT_ADMISSION` | It is the first IG proof object still missing after 1503. |
| `IG_FULL_SUMMAND_DIMENSION_AUDIT` | Audit full summand lists and dimension totals for both required D7 tensor products. | sequential/support | `IG_D7_PROOF_TRANSCRIPT_OBJECT` | It distinguishes proof object admission from selected-summand checking. |
| `IG_KERNEL_HIGHEST_WEIGHT_HAND_PROOF` | Supply an admissible hand proof of `ker(c)` irreducibility and highest weight if CAS is unavailable. | sequential alternate | `IG_D7_PROOF_TRANSCRIPT_OBJECT` or CAS absence | It is a valid alternate proof object only if full finite data are present. |
| `IG_K_IG_FAMILY_IDENTITY` | Prove the admitted Shiab/D7 selector is the same source family object as `K_IG`. | sequential | `IG_D7_PROOF_TRANSCRIPT_OBJECT` | It is separate from finite multiplicity and blocks selector restart. |
| `IG_RIVAL_ROW_ELIMINATION_AFTER_IDENTITY` | Eliminate representation-natural rivals only after transcript and family identity pass. | sequential | `IG_K_IG_FAMILY_IDENTITY` | It prevents chirality-only screening from becoming full uniqueness. |
| `DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE` | Expand the DGU source scope beyond the inspected manuscript/UCSD window and rerun the actual 0/1 field table. | immediate | `C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE`, `C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET` | It can either find the actual packet or produce a broader bounded negative. |
| `DGU_OXFORD_FRAME_OPERATOR_SCOPE` | Inspect Oxford frames/slides for actual `D_GU^epsilon` sector rule, typed 0/1 domain/codomain, and projector data. | immediate alternate | `C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET` | Cycle 2 explicitly left Oxford frames uninspected. |
| `DGU_OLD_SHIAB_OPERATOR_NOTES_SCOPE` | Search old Shiab/operator-choice notes for the actual 0/1 sector identity packet. | immediate alternate | `C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET` | It targets a named source surface, not a global no-go. |
| `DGU_BROADER_SCOPED_NEGATIVE_RECEIPT` | Emit `NegativePrimarySourceReceiptInstance_V1` if the expanded source scope remains field-negative. | sequential | `DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE` | It converts absence into a bounded result with rollback conditions. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | Compute symbol and Q-sector certificate only from an accepted actual 0/1 packet. | sequential | `DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE` | It is valuable only after source identity exists. |
| `RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET` | Capture checksummed frames/crops/OCR for `fBozSSLxFvI` `[00:32:07]-[00:37:41]`, or document non-transient unavailability. | immediate | `C1_RS_FRAME_SEQUENCE_ACQUISITION`, `C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET` | It is the first RS visual source object after the stable locator. |
| `RS_SOURCE_SAFE_CAPTURE_TOOLCHAIN_MANIFEST` | Admit capture toolchain, command, time sampling, and output checksums for the UCSD visual route. | immediate alternate | `C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET` | It separates locator from visual receipt. |
| `RS_FRAME_OCR_OPERATOR_TABLE` | Build a frame/crop/OCR table for operator name, domain, codomain, slot, rule kind, quotient, and projection fields. | sequential | `RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET` | It turns frames into a typed source packet candidate. |
| `RS_TYPED_MINUS_ONE_OPERATOR_PACKET` | Instantiate `UCSDTypedRSMinusOneOperator_V1` from visible source fields if present. | sequential | `RS_FRAME_OCR_OPERATOR_TABLE` | Typed RS cannot start from transcript aggregate language. |
| `RS_AGGREGATE_ONLY_DEMOTION_AFTER_VISUAL_PASS` | Demote visual route to aggregate-only only if captured/documented visuals lack pure RS fields. | sequential | `RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET` | It makes demotion evidence-based rather than transcript-only. |
| `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | Construct source-defined `b`, `iota_b`, `U_b(O)`, typed `R_raw^b(O)`, `G_b(O)`, restrictions, and non-import screen. | immediate | `C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID`, `C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET` | It is the first QFT source packet needed before generator promotion. |
| `QFT_RAW_BRANCH_SOURCE_LOCATOR` | Locate repo source for `b`, observed region, section/pullback map, and local `Y`-domain. | immediate alternate | `C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET` | It targets the first missing subobject: `iota_b` plus typed raw fields. |
| `QFT_GAUGE_RESTRICTION_STABILITY_TEST` | Prove `res^R(gamma_O(g, phi)) = gamma_O'(res^G(g), res^R(phi))` after the packet is source-defined. | sequential | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | It is the first promotable generator test. |
| `QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET` | Define `tilde_phys^b(O)` and `F_phys^b(O)` only after a source-defined restriction-stable generator exists. | sequential | `QFT_GAUGE_RESTRICTION_STABILITY_TEST` | It prevents `F_phys` from selecting the raw branch. |
| `QFT_PRAW_PFIN_DESCENT_AFTER_QUOTIENT` | Define `P_raw`, `P_fin`, and descent/naturality only after physical quotient and source codomain exist. | sequential | `QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET` | It parks finite-QFT extraction until the source quotient exists. |
| `QFT_RHO_AB_CHSH_BELL_FIREWALL` | Maintain firewall against `rho_AB`, Bell, CHSH, Pauli, and target Hilbert-state selection of upstream packets. | demoted backup | `C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET` | It is useful as a guard, but lower value than constructing the source packet. |
| `GLOBAL_NO_RECEIPT_CLAIM_PROMOTION_FIREWALL` | Enforce no claim promotion or proof restart while accepted receipt count is zero. | demoted backup | all five cycle 2 artifacts | It protects the run but does not itself produce a missing source object. |
| `THREE_CYCLE_SYNTHESIS_WITH_ROUTE_STATUS` | Synthesize the three-cycle result into closed/blocked/underdefined/source-negative statuses. | demoted backup | all cycle 3 artifacts | Useful closeout, but not a frontier source-object producer. |

Quality candidates claimed: **28**. The first 25 are direct source-object,
proof-object, receipt, bounded-negative, or branch-decision gates. The final
three are demoted guard/synthesis candidates and should not replace producer
lanes unless explicitly requested.

## 3. Dependency DAG text

```text
1503_C1_COMMIT_b1a2cc5
  -> C1_PTUJ_SOURCE_BYTE_MANIFEST
  -> C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH
  -> PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION
  -> PTUJ_FORMULA_VISIBILITY_AUDIT
  -> PTUJ_KEATING_SHEET_IDENTITY

C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH
  -> PTUJ_CUSTODIAN_REQUEST_PACKET
  -> PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION

C1_PTUJ_SOURCE_BYTE_MANIFEST
  -> PTUJ_LOCAL_TOOLCHAIN_ADMISSION
  -> PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION

1503_C1_COMMIT_b1a2cc5
  -> C1_IG_D7_MULTIPLICITY_TRANSCRIPT
  -> C2_IG_D7_PROOF_OBJECT_ADMISSION
  -> IG_D7_PROOF_TRANSCRIPT_OBJECT
  -> IG_FULL_SUMMAND_DIMENSION_AUDIT
  -> IG_K_IG_FAMILY_IDENTITY
  -> IG_RIVAL_ROW_ELIMINATION_AFTER_IDENTITY

C2_IG_D7_PROOF_OBJECT_ADMISSION
  -> IG_KERNEL_HIGHEST_WEIGHT_HAND_PROOF
  -> IG_D7_PROOF_TRANSCRIPT_OBJECT

1503_C1_COMMIT_b1a2cc5
  -> C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE
  -> C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET
  -> DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE
  -> DGU_BROADER_SCOPED_NEGATIVE_RECEIPT

C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET
  -> DGU_OXFORD_FRAME_OPERATOR_SCOPE
  -> DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE

C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET
  -> DGU_OLD_SHIAB_OPERATOR_NOTES_SCOPE
  -> DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE

DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE
  -> DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET

1503_C1_COMMIT_b1a2cc5
  -> C1_RS_FRAME_SEQUENCE_ACQUISITION
  -> C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET
  -> RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET
  -> RS_FRAME_OCR_OPERATOR_TABLE
  -> RS_TYPED_MINUS_ONE_OPERATOR_PACKET

C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET
  -> RS_SOURCE_SAFE_CAPTURE_TOOLCHAIN_MANIFEST
  -> RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET

RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET
  -> RS_AGGREGATE_ONLY_DEMOTION_AFTER_VISUAL_PASS

1503_C1_COMMIT_b1a2cc5
  -> C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID
  -> C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET
  -> QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET
  -> QFT_GAUGE_RESTRICTION_STABILITY_TEST
  -> QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET
  -> QFT_PRAW_PFIN_DESCENT_AFTER_QUOTIENT

C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET
  -> QFT_RAW_BRANCH_SOURCE_LOCATOR
  -> QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET
```

## 4. Cross-route dependency notes

- PTUJ: cycle 2 proved only locator/metadata continuity. `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1`
  and the lawful local byte/toolchain manifest remain alternatives, not receipts.
- IG: chirality exclusions and Shiab existence are accepted narrow facts, but
  no selector theorem can restart without full D7 finite data, `K_IG` family
  identity, and rival elimination.
- DGU: cycle 2's result is a scoped source-window negative, not a global no-go.
  Symbol certificates and VZ replay wait on an accepted actual 0/1 identity
  packet.
- RS: the stable official video locator is positive, but it is not a frame
  packet. Typed RS and generation/index work wait on frames/crops/OCR or a
  documented unavailability packet.
- QFT: standard gauge formulas are candidate machinery only. `F_phys`, `P_fin`,
  `rho_AB`, Bell, CHSH, Pauli settings, and representation labels cannot define
  the source-observed raw branch.
- The shared firewall is: **upstream-source-object/no target-import firewall**.
  Downstream target objects may not select upstream branch data, source assets,
  representation proof packets, operator identities, frame packets, or QFT raw
  fields.

## 5. Immediate parallel-safe lanes

| lane | candidate id | prerequisite | proposed write scope |
|---|---|---|---|
| A | `PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION` | `C1_PTUJ_SOURCE_BYTE_MANIFEST`, `C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH` | `explorations/hourly-20260625-next-ptuj-official-source-asset-or-lawful-byte-manifest.md` |
| B | `IG_D7_PROOF_TRANSCRIPT_OBJECT` | `C1_IG_D7_MULTIPLICITY_TRANSCRIPT`, `C2_IG_D7_PROOF_OBJECT_ADMISSION` | `explorations/hourly-20260625-next-ig-d7-proof-transcript-object.md` |
| C | `DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE` | `C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE`, `C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET` | `explorations/hourly-20260625-next-dgu-expanded-identity-field-source-scope-bundle.md` |
| D | `RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET` | `C1_RS_FRAME_SEQUENCE_ACQUISITION`, `C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET` | `explorations/hourly-20260625-next-rs-visual-frame-capture-or-unavailability.md` |
| E | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | `C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID`, `C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET` | `explorations/hourly-20260625-next-qft-source-defined-raw-branch-local-gauge-groupoid.md` |

## 6. Sequential lanes and why not parallel

| candidate id | must wait for | why not parallel now |
|---|---|---|
| `PTUJ_FORMULA_VISIBILITY_AUDIT` | `PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION` | There is still no inspectable source content. |
| `PTUJ_KEATING_SHEET_IDENTITY` | `PTUJ_FORMULA_VISIBILITY_AUDIT` | Identity comparison needs an accepted formula-bearing PTUJ object. |
| `IG_FULL_SUMMAND_DIMENSION_AUDIT` | `IG_D7_PROOF_TRANSCRIPT_OBJECT` | It audits a transcript/proof object that does not yet exist. |
| `IG_KERNEL_HIGHEST_WEIGHT_HAND_PROOF` | transcript absence or ambiguous transcript | It should answer the exact gap left by transcript/proof admission. |
| `IG_K_IG_FAMILY_IDENTITY` | `IG_D7_PROOF_TRANSCRIPT_OBJECT` | Family identity is downstream of finite selector data. |
| `IG_RIVAL_ROW_ELIMINATION_AFTER_IDENTITY` | `IG_K_IG_FAMILY_IDENTITY` | Rival elimination requires an accepted source-family candidate. |
| `DGU_BROADER_SCOPED_NEGATIVE_RECEIPT` | `DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE` | A bounded negative requires declared expanded coverage. |
| `DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET` | accepted DGU actual 0/1 packet | Symbol data must belong to the accepted actual operator. |
| `RS_FRAME_OCR_OPERATOR_TABLE` | `RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET` | It needs captured frames/crops/OCR or a documented unavailability decision. |
| `RS_TYPED_MINUS_ONE_OPERATOR_PACKET` | `RS_FRAME_OCR_OPERATOR_TABLE` | Typed RS fields must be visible or source-tied first. |
| `RS_AGGREGATE_ONLY_DEMOTION_AFTER_VISUAL_PASS` | visual capture or documented unavailability | Demotion should follow visual evidence, not transcript-only absence. |
| `QFT_GAUGE_RESTRICTION_STABILITY_TEST` | `QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET` | The restriction square needs defined `R_raw^b(O)` and `G_b(O)`. |
| `QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET` | `QFT_GAUGE_RESTRICTION_STABILITY_TEST` | The quotient waits on a source-defined generator. |
| `QFT_PRAW_PFIN_DESCENT_AFTER_QUOTIENT` | `QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET` | Descent waits on source quotient and codomain. |

## 7. Demoted backups

| backup lane | why demoted |
|---|---|
| `QFT_RHO_AB_CHSH_BELL_FIREWALL` | Important guard, but it does not construct the source raw branch. |
| `GLOBAL_NO_RECEIPT_CLAIM_PROMOTION_FIREWALL` | Maintains discipline, but producer lanes have higher information gain. |
| `THREE_CYCLE_SYNTHESIS_WITH_ROUTE_STATUS` | Useful closeout, but not a missing source-object lane. |
| broad PTUJ metadata refresh | Cycle 2 already shows metadata-only; source asset or bytes are required. |
| broad DGU/VZ replay review | VZ replay is downstream of actual DGU identity fields. |
| transcript-only RS reinterpretation | Cycle 2 already separated locator/transcript from visual packet. |
| general IG uniqueness essay | IG now needs finite D7 proof data, not prose uniqueness. |

## 8. Machine-readable JSON summary

```json
{
  "artifact": "NextFrontierDependencyDagAfter1503_V1",
  "artifact_id": "NextFrontierDependencyDagAfter1503_V1",
  "run_id": "hourly-20260625-1503",
  "cycle": 3,
  "lane": 5,
  "verdict": "UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART",
  "verdict_phrase": "upstream source objects/no receipts/no proof restart",
  "cycle_commits": {
    "cycle_1": "b1a2cc5",
    "cycle_2": "74090c4"
  },
  "quality_candidates_claimed": 28,
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "upstream_source_object_no_target_import_firewall": true,
  "firewall_label": "upstream-source-object/no target-import firewall",
  "route_families": ["PTUJ", "IG", "DGU", "RS", "QFT"],
  "next_five_recommended_lanes": [
    "PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION",
    "IG_D7_PROOF_TRANSCRIPT_OBJECT",
    "DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE",
    "RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET",
    "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET"
  ],
  "run_learning_summary": {
    "PTUJ": "official/custodian branch metadata-only; continue official source asset or lawful source-byte manifest",
    "IG": "proof-object admission blocked; produce D7 proof/transcript object",
    "DGU": "scoped source-window negative; expand identity-field source-scope bundle",
    "RS": "stable locator but no frames/crops/OCR; capture visual packet or document unavailability",
    "QFT": "source-observed raw branch underdefined; construct source-defined raw branch/local gauge groupoid packet"
  },
  "known_objects": [
    "C1_PTUJ_SOURCE_BYTE_MANIFEST",
    "C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH",
    "C1_IG_D7_MULTIPLICITY_TRANSCRIPT",
    "C2_IG_D7_PROOF_OBJECT_ADMISSION",
    "C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE",
    "C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET",
    "C1_RS_FRAME_SEQUENCE_ACQUISITION",
    "C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET",
    "C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID",
    "C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET",
    "PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION",
    "PTUJ_CUSTODIAN_REQUEST_PACKET",
    "PTUJ_LOCAL_TOOLCHAIN_ADMISSION",
    "PTUJ_FORMULA_VISIBILITY_AUDIT",
    "PTUJ_KEATING_SHEET_IDENTITY",
    "IG_D7_PROOF_TRANSCRIPT_OBJECT",
    "IG_FULL_SUMMAND_DIMENSION_AUDIT",
    "IG_KERNEL_HIGHEST_WEIGHT_HAND_PROOF",
    "IG_K_IG_FAMILY_IDENTITY",
    "IG_RIVAL_ROW_ELIMINATION_AFTER_IDENTITY",
    "DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE",
    "DGU_OXFORD_FRAME_OPERATOR_SCOPE",
    "DGU_OLD_SHIAB_OPERATOR_NOTES_SCOPE",
    "DGU_BROADER_SCOPED_NEGATIVE_RECEIPT",
    "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
    "RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET",
    "RS_SOURCE_SAFE_CAPTURE_TOOLCHAIN_MANIFEST",
    "RS_FRAME_OCR_OPERATOR_TABLE",
    "RS_TYPED_MINUS_ONE_OPERATOR_PACKET",
    "RS_AGGREGATE_ONLY_DEMOTION_AFTER_VISUAL_PASS",
    "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET",
    "QFT_RAW_BRANCH_SOURCE_LOCATOR",
    "QFT_GAUGE_RESTRICTION_STABILITY_TEST",
    "QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET",
    "QFT_PRAW_PFIN_DESCENT_AFTER_QUOTIENT",
    "QFT_RHO_AB_CHSH_BELL_FIREWALL",
    "GLOBAL_NO_RECEIPT_CLAIM_PROMOTION_FIREWALL",
    "THREE_CYCLE_SYNTHESIS_WITH_ROUTE_STATUS"
  ],
  "candidates": [
    {"id": "PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION", "route_family": "PTUJ", "quality": true, "parallel_safe": true, "sequential": false, "demoted_backup": false, "dependencies": ["C1_PTUJ_SOURCE_BYTE_MANIFEST", "C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH"]},
    {"id": "PTUJ_CUSTODIAN_REQUEST_PACKET", "route_family": "PTUJ", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": false, "dependencies": ["C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH"]},
    {"id": "PTUJ_LOCAL_TOOLCHAIN_ADMISSION", "route_family": "PTUJ", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": false, "dependencies": ["C1_PTUJ_SOURCE_BYTE_MANIFEST"]},
    {"id": "PTUJ_FORMULA_VISIBILITY_AUDIT", "route_family": "PTUJ", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION"]},
    {"id": "PTUJ_KEATING_SHEET_IDENTITY", "route_family": "PTUJ", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["PTUJ_FORMULA_VISIBILITY_AUDIT"]},
    {"id": "IG_D7_PROOF_TRANSCRIPT_OBJECT", "route_family": "IG", "quality": true, "parallel_safe": true, "sequential": false, "demoted_backup": false, "dependencies": ["C1_IG_D7_MULTIPLICITY_TRANSCRIPT", "C2_IG_D7_PROOF_OBJECT_ADMISSION"]},
    {"id": "IG_FULL_SUMMAND_DIMENSION_AUDIT", "route_family": "IG", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["IG_D7_PROOF_TRANSCRIPT_OBJECT"]},
    {"id": "IG_KERNEL_HIGHEST_WEIGHT_HAND_PROOF", "route_family": "IG", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["IG_D7_PROOF_TRANSCRIPT_OBJECT"]},
    {"id": "IG_K_IG_FAMILY_IDENTITY", "route_family": "IG", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["IG_D7_PROOF_TRANSCRIPT_OBJECT"]},
    {"id": "IG_RIVAL_ROW_ELIMINATION_AFTER_IDENTITY", "route_family": "IG", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["IG_K_IG_FAMILY_IDENTITY"]},
    {"id": "DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE", "route_family": "DGU", "quality": true, "parallel_safe": true, "sequential": false, "demoted_backup": false, "dependencies": ["C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE", "C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET"]},
    {"id": "DGU_OXFORD_FRAME_OPERATOR_SCOPE", "route_family": "DGU", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": false, "dependencies": ["C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET"]},
    {"id": "DGU_OLD_SHIAB_OPERATOR_NOTES_SCOPE", "route_family": "DGU", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": false, "dependencies": ["C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET"]},
    {"id": "DGU_BROADER_SCOPED_NEGATIVE_RECEIPT", "route_family": "DGU", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE"]},
    {"id": "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET", "route_family": "DGU", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE"]},
    {"id": "RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET", "route_family": "RS", "quality": true, "parallel_safe": true, "sequential": false, "demoted_backup": false, "dependencies": ["C1_RS_FRAME_SEQUENCE_ACQUISITION", "C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET"]},
    {"id": "RS_SOURCE_SAFE_CAPTURE_TOOLCHAIN_MANIFEST", "route_family": "RS", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": false, "dependencies": ["C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET"]},
    {"id": "RS_FRAME_OCR_OPERATOR_TABLE", "route_family": "RS", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET"]},
    {"id": "RS_TYPED_MINUS_ONE_OPERATOR_PACKET", "route_family": "RS", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["RS_FRAME_OCR_OPERATOR_TABLE"]},
    {"id": "RS_AGGREGATE_ONLY_DEMOTION_AFTER_VISUAL_PASS", "route_family": "RS", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET"]},
    {"id": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET", "route_family": "QFT", "quality": true, "parallel_safe": true, "sequential": false, "demoted_backup": false, "dependencies": ["C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID", "C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET"]},
    {"id": "QFT_RAW_BRANCH_SOURCE_LOCATOR", "route_family": "QFT", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": false, "dependencies": ["C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET"]},
    {"id": "QFT_GAUGE_RESTRICTION_STABILITY_TEST", "route_family": "QFT", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET"]},
    {"id": "QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET", "route_family": "QFT", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["QFT_GAUGE_RESTRICTION_STABILITY_TEST"]},
    {"id": "QFT_PRAW_PFIN_DESCENT_AFTER_QUOTIENT", "route_family": "QFT", "quality": true, "parallel_safe": false, "sequential": true, "demoted_backup": false, "dependencies": ["QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET"]},
    {"id": "QFT_RHO_AB_CHSH_BELL_FIREWALL", "route_family": "QFT", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": true, "dependencies": ["C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET"]},
    {"id": "GLOBAL_NO_RECEIPT_CLAIM_PROMOTION_FIREWALL", "route_family": "GLOBAL", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": true, "dependencies": ["C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH", "C2_IG_D7_PROOF_OBJECT_ADMISSION", "C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET", "C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET", "C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET"]},
    {"id": "THREE_CYCLE_SYNTHESIS_WITH_ROUTE_STATUS", "route_family": "GLOBAL", "quality": true, "parallel_safe": false, "sequential": false, "demoted_backup": true, "dependencies": ["GLOBAL_NO_RECEIPT_CLAIM_PROMOTION_FIREWALL"]}
  ],
  "immediate_parallel_safe_lanes": [
    {"id": "PTUJ_OFFICIAL_SOURCE_ASSET_OR_LAWFUL_BYTE_MANIFEST_CONTINUATION", "route_family": "PTUJ", "prerequisites": ["C1_PTUJ_SOURCE_BYTE_MANIFEST", "C2_PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH"], "write_scope": "explorations/hourly-20260625-next-ptuj-official-source-asset-or-lawful-byte-manifest.md"},
    {"id": "IG_D7_PROOF_TRANSCRIPT_OBJECT", "route_family": "IG", "prerequisites": ["C1_IG_D7_MULTIPLICITY_TRANSCRIPT", "C2_IG_D7_PROOF_OBJECT_ADMISSION"], "write_scope": "explorations/hourly-20260625-next-ig-d7-proof-transcript-object.md"},
    {"id": "DGU_EXPANDED_IDENTITY_FIELD_SOURCE_SCOPE_BUNDLE", "route_family": "DGU", "prerequisites": ["C1_DGU_IDENTITY_FIELD_RECEIPT_BUNDLE", "C2_DGU_ACTUAL_01_SOURCE_WINDOW_PACKET"], "write_scope": "explorations/hourly-20260625-next-dgu-expanded-identity-field-source-scope-bundle.md"},
    {"id": "RS_VISUAL_FRAME_CAPTURE_OR_DOCUMENTED_UNAVAILABILITY_PACKET", "route_family": "RS", "prerequisites": ["C1_RS_FRAME_SEQUENCE_ACQUISITION", "C2_RS_VISUAL_LOCATOR_UNAVAILABILITY_PACKET"], "write_scope": "explorations/hourly-20260625-next-rs-visual-frame-capture-or-unavailability.md"},
    {"id": "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET", "route_family": "QFT", "prerequisites": ["C1_QFT_LOCAL_GAUGE_ACTION_GROUPOID", "C2_QFT_SOURCE_OBSERVED_RAW_BRANCH_PACKET"], "write_scope": "explorations/hourly-20260625-next-qft-source-defined-raw-branch-local-gauge-groupoid.md"}
  ],
  "sequential_lanes": [
    "PTUJ_FORMULA_VISIBILITY_AUDIT",
    "PTUJ_KEATING_SHEET_IDENTITY",
    "IG_FULL_SUMMAND_DIMENSION_AUDIT",
    "IG_KERNEL_HIGHEST_WEIGHT_HAND_PROOF",
    "IG_K_IG_FAMILY_IDENTITY",
    "IG_RIVAL_ROW_ELIMINATION_AFTER_IDENTITY",
    "DGU_BROADER_SCOPED_NEGATIVE_RECEIPT",
    "DGU_SYMBOL_CERTIFICATE_FROM_ACCEPTED_PACKET",
    "RS_FRAME_OCR_OPERATOR_TABLE",
    "RS_TYPED_MINUS_ONE_OPERATOR_PACKET",
    "RS_AGGREGATE_ONLY_DEMOTION_AFTER_VISUAL_PASS",
    "QFT_GAUGE_RESTRICTION_STABILITY_TEST",
    "QFT_PHYSICAL_QUOTIENT_FUNCTOR_FROM_SOURCE_PACKET",
    "QFT_PRAW_PFIN_DESCENT_AFTER_QUOTIENT"
  ],
  "demoted_backups": [
    "QFT_RHO_AB_CHSH_BELL_FIREWALL",
    "GLOBAL_NO_RECEIPT_CLAIM_PROMOTION_FIREWALL",
    "THREE_CYCLE_SYNTHESIS_WITH_ROUTE_STATUS"
  ],
  "proof_replay_forbidden_until": [
    "accepted_PTUJ_formula_source_asset_or_lawful_frame_packet",
    "accepted_IG_D7_proof_transcript_object_and_K_IG_family_identity",
    "accepted_DGU_actual_01_identity_packet",
    "accepted_RS_visual_typed_operator_packet",
    "accepted_QFT_source_defined_raw_branch_and_restriction_stable_gauge_groupoid"
  ]
}
```
