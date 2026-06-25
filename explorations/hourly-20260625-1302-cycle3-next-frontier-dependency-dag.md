---
title: "Hourly 20260625 1302 Cycle 3 Next Frontier Dependency DAG"
date: "2026-06-25"
run_id: "hourly-20260625-1302"
cycle: 3
lane: 5
doc_type: next_frontier_dependency_dag
artifact_id: "NextFrontierDependencyDagAfter1302_V1"
verdict: "NEXT_FRONTIER_REMAINS_UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART"
owned_path: "explorations/hourly-20260625-1302-cycle3-next-frontier-dependency-dag.md"
companion_audit: "tests/hourly_20260625_1302_cycle3_next_frontier_dependency_dag_audit.py"
---

# Hourly 20260625 1302 Cycle 3 Next Frontier Dependency DAG

## 1. Verdict

Verdict: **the next frontier after 1302 cycles 1-2 is still upstream
source-object construction, with sharper contracts and no accepted receipts**.

The 1302 cycle 1 lanes reran the five upstream objects named by the 0803 DAG.
None closed: PTUJ lacked an admissible extractor branch; IG remained
conditional on D7 multiplicity/highest-weight verification; DGU lacked actual
0/1 identity fields; RS lacked the UCSD visual frame sequence; QFT had only a
generator taxonomy. Cycle 2 improved those blockers into exact acceptance
protocols, but also left all receipt counts at zero.

Run-level decision:

```text
accepted_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
next_parallel_batch_allowed: yes, only for disjoint upstream source-object gates
next_parallel_batch_not_allowed_for: downstream formula, proof, VZ, RS index,
  finite-QFT, rho_AB, CHSH, or Bell consumers
```

The next five recommended lanes are:

1. `PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST`
2. `IG_D7_MULTIPLICITY_TRANSCRIPT`
3. `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE`
4. `RS_UCSD_FRAME_SEQUENCE_ACQUISITION`
5. `QFT_LOCAL_GAUGE_ACTION_GROUPOID`

These five are parallel-safe because their write scopes and source objects are
disjoint. They are not proof replays. They each attempt to construct or reject
the first missing object named by cycles 1-2.

## 2. Candidate hole bank table

Quality bar used here: a candidate counts only if it names a missing source
object, proof transcript, identity field bundle, local groupoid, restriction
stability proof, receipt, or demotion gate whose resolution would materially
change routing. Summary-only or broad status checks are not counted.

| id | candidate hole | run-now verdict | immediate dependencies | why quality |
|---|---|---|---|---|
| `PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST` | Build or reject the admissible toolchain/source-byte/output manifest for `TzSEvmqxu48`. | immediate | `C2_PTUJ_TOOLCHAIN_MANIFEST_GATE` | It is the first missing PTUJ object after cycle 2. |
| `PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH` | Acquire or reject an official/custodian source-asset packet for the same PTUJ formula surface. | immediate alternate, not next-five | `C2_PTUJ_TOOLCHAIN_MANIFEST_GATE` | A distinct lawful branch that could bypass local extraction. |
| `PTUJ_FRAME_VISIBILITY_AUDIT` | Inspect checksummed decoded frames or source pages for formula-bearing, formula-negative, or insufficient-resolution status. | sequential | `PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST` | Formula packet cannot start before source bytes and decoded/source outputs exist. |
| `PTUJ_FORMULA_PACKET` | Build `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` from accepted frame/source evidence. | sequential | `PTUJ_FRAME_VISIBILITY_AUDIT`, `PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH` | Converts acquisition into a receipt candidate without conflating metadata. |
| `PTUJ_KEATING_SHEET_IDENTITY` | Compare an accepted PTUJ formula packet to the Keating missing projection sheet. | sequential | `PTUJ_FORMULA_PACKET` | Prevents locator/caption evidence from becoming selector identity. |
| `IG_D7_MULTIPLICITY_TRANSCRIPT` | Produce a raw LiE/Sage/formal D7 transcript for `FC-IRR`, `FC-MULT`, and `FC-HW`. | immediate | `C2_IG_D7_MULTIPLICITY_AUDIT_GATE` | It is the first exact obstruction to the selector theorem. |
| `IG_KERNEL_IRREDUCIBILITY_FORMAL_PROOF` | Formalize `ker(c)` irreducibility and highest weight if CAS transcript is absent or ambiguous. | sequential/support | `IG_D7_MULTIPLICITY_TRANSCRIPT` | Needed if the finite transcript does not directly close `FC-IRR` and `FC-HW`. |
| `IG_SELECTOR_THEOREM_RESTART` | Reattempt `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1`. | sequential | `IG_D7_MULTIPLICITY_TRANSCRIPT`, `IG_K_IG_FAMILY_IDENTITY` | The selector waits on multiplicity and identity, not only Shiab existence. |
| `IG_K_IG_FAMILY_IDENTITY` | Prove the verified D7/Shiab selector is the same family object as `K_IG`. | sequential | `IG_D7_MULTIPLICITY_TRANSCRIPT` | Family identity is a separate gate after the transcript. |
| `IG_FULL_RIVAL_ROW_ELIMINATOR` | Eliminate the full 0803 representation-natural rival matrix row by row. | sequential | `IG_SELECTOR_THEOREM_RESTART`, `IG_K_IG_FAMILY_IDENTITY` | Prevents conditional uniqueness from becoming full source selection. |
| `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE` | Build `DGUIdentityFieldReceiptBundle_V1` for a declared source scope, with query variants and inspected hits. | immediate | `C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE` | It is the first object that can accept identity fields or justify a scoped negative. |
| `DGU_ACTUAL_IDENTITY_WITNESS` | Instantiate `ActualDGU01IdentityWitness_V1` if the receipt bundle emits all actual fields. | sequential | `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE` | Actual identity must precede any certificate or replay. |
| `DGU_SCOPED_NEGATIVE_RECEIPT` | Emit a scoped negative DGU 0/1 receipt only after complete source coverage remains negative. | sequential | `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE` | Converts absence into a bounded result without global no-go inflation. |
| `DGU_SYMBOL_CERTIFICATE` | Compute/check principal symbol and Q-sector blocks for the accepted actual operator. | sequential | `DGU_ACTUAL_IDENTITY_WITNESS` | Symbol data is meaningless without actual typed identity fields. |
| `DGU_VZ_REPLAY_GATE` | Restart VZ backend only against an accepted actual DGU certificate. | sequential | `DGU_SYMBOL_CERTIFICATE` | Directly enforces the DGU/VZ no-replay guard. |
| `RS_UCSD_FRAME_SEQUENCE_ACQUISITION` | Acquire checksummed UCSD frames/crops/OCR for `[00:32:07]-[00:37:41]`. | immediate | `C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT` | It is the first missing RS visual source object. |
| `RS_UCSD_TYPED_OPERATOR_PACKET` | Instantiate `UCSDTypedRSMinusOneOperator_V1` if frames show operator/domain/codomain/slot/quotient fields. | sequential | `RS_UCSD_FRAME_SEQUENCE_ACQUISITION` | Typed operator waits on the frame sequence. |
| `RS_AGGREGATE_ONLY_DEMOTION` | Demote the UCSD visual route to aggregate-only if acquired frames lack pure RS typing. | sequential | `RS_UCSD_FRAME_SEQUENCE_ACQUISITION` | A precise negative consequence, not a transcript-only demotion. |
| `RS_RS_ONLY_QUOTIENT_TEST` | Test source-defined `P_RS`/quotient/family identity after typed operator fields exist. | sequential | `RS_UCSD_TYPED_OPERATOR_PACKET` | Separates aggregate rollup from pure RS receipt. |
| `RS_GENERATION_INDEX_RESTART` | Restart RS index/K3/generation-count work only after typed operator and quotient pass. | sequential | `RS_UCSD_TYPED_OPERATOR_PACKET`, `RS_RS_ONLY_QUOTIENT_TEST` | Prevents two-plus-one transcript language from becoming proof. |
| `QFT_LOCAL_GAUGE_ACTION_GROUPOID` | Define `G_b(O)`, its action on typed `R_raw^b(O)`, and restriction maps. | immediate | `C2_QFT_GAUGE_ACTION_RESTRICTION_GATE` | It is the first missing source-defined gauge generator object. |
| `QFT_GAUGE_RESTRICTION_STABILITY_PROOF` | Prove the gauge orbit relation restricts from `O` to every `O' subset O`. | sequential | `QFT_LOCAL_GAUGE_ACTION_GROUPOID` | Restriction stability is required before generator promotion. |
| `QFT_PHYSICAL_QUOTIENT_FUNCTOR` | Define `tilde_phys^b(O)` and `F_phys^b(O)` from accepted source generators. | sequential | `QFT_GAUGE_RESTRICTION_STABILITY_PROOF` | The quotient waits on a source-defined restriction-stable generator. |
| `QFT_PRAW_PFIN_DESCENT` | Define `P_raw`, prove descent to `P_fin`, and check naturality. | sequential | `QFT_PHYSICAL_QUOTIENT_FUNCTOR`, `QFT_SOURCE_KB_CODOMAIN` | Descent needs a real quotient and codomain. |
| `QFT_SOURCE_KB_CODOMAIN` | Derive or reject source-defined `K_b` without representation-carrier import. | sequential/support | `QFT_PHYSICAL_QUOTIENT_FUNCTOR` | Prevents the target carrier from selecting finite extraction. |
| `QFT_RHO_AB_CHSH_FIREWALL` | Maintain firewall against `rho_AB`, CHSH, Bell, Pauli, and vacuum work before source quotient/descent. | backup/audit | `C2_QFT_GAUGE_ACTION_RESTRICTION_GATE` | Useful guard, but lower priority than constructing the quotient source object. |

Quality candidates claimed: **26**. The first 25 are direct construction,
receipt, theorem, or demotion gates. The final firewall is quality because it
guards target import, but it is demoted below producer lanes.

## 3. Dependency DAG text

```text
C2_PTUJ_TOOLCHAIN_MANIFEST_GATE
  -> PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST
  -> PTUJ_FRAME_VISIBILITY_AUDIT
  -> PTUJ_FORMULA_PACKET
  -> PTUJ_KEATING_SHEET_IDENTITY

C2_PTUJ_TOOLCHAIN_MANIFEST_GATE
  -> PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH
  -> PTUJ_FORMULA_PACKET

C2_IG_D7_MULTIPLICITY_AUDIT_GATE
  -> IG_D7_MULTIPLICITY_TRANSCRIPT
  -> IG_KERNEL_IRREDUCIBILITY_FORMAL_PROOF
  -> IG_SELECTOR_THEOREM_RESTART

C2_IG_D7_MULTIPLICITY_AUDIT_GATE
  -> IG_D7_MULTIPLICITY_TRANSCRIPT
  -> IG_K_IG_FAMILY_IDENTITY
  -> IG_SELECTOR_THEOREM_RESTART
  -> IG_FULL_RIVAL_ROW_ELIMINATOR

C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE
  -> DGU_IDENTITY_FIELD_RECEIPT_BUNDLE
  -> DGU_ACTUAL_IDENTITY_WITNESS
  -> DGU_SYMBOL_CERTIFICATE
  -> DGU_VZ_REPLAY_GATE

C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE
  -> DGU_IDENTITY_FIELD_RECEIPT_BUNDLE
  -> DGU_SCOPED_NEGATIVE_RECEIPT

C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT
  -> RS_UCSD_FRAME_SEQUENCE_ACQUISITION
  -> RS_UCSD_TYPED_OPERATOR_PACKET
  -> RS_RS_ONLY_QUOTIENT_TEST
  -> RS_GENERATION_INDEX_RESTART

C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT
  -> RS_UCSD_FRAME_SEQUENCE_ACQUISITION
  -> RS_AGGREGATE_ONLY_DEMOTION

C2_QFT_GAUGE_ACTION_RESTRICTION_GATE
  -> QFT_LOCAL_GAUGE_ACTION_GROUPOID
  -> QFT_GAUGE_RESTRICTION_STABILITY_PROOF
  -> QFT_PHYSICAL_QUOTIENT_FUNCTOR
  -> QFT_PRAW_PFIN_DESCENT

C2_QFT_GAUGE_ACTION_RESTRICTION_GATE
  -> QFT_LOCAL_GAUGE_ACTION_GROUPOID
  -> QFT_GAUGE_RESTRICTION_STABILITY_PROOF
  -> QFT_PHYSICAL_QUOTIENT_FUNCTOR
  -> QFT_SOURCE_KB_CODOMAIN
  -> QFT_PRAW_PFIN_DESCENT
```

Cross-route dependencies:

- `PTUJ_FORMULA_PACKET` waits on real toolchain/source bytes or an official
  source asset. It must not be run from captions, oEmbed, storyboard, thumbnail,
  or locator evidence.
- `IG_SELECTOR_THEOREM_RESTART` waits on the D7 multiplicity transcript and
  `IG_K_IG_FAMILY_IDENTITY`. Shiab existence and chirality exclusions alone do
  not select `K_IG`.
- `DGU_SYMBOL_CERTIFICATE` and `DGU_VZ_REPLAY_GATE` wait on actual identity
  fields accepted by `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE`.
- `RS_UCSD_TYPED_OPERATOR_PACKET` waits on acquired UCSD frames/slides, and
  `RS_GENERATION_INDEX_RESTART` waits on typed operator plus RS-only
  quotient/family identity.
- `QFT_PHYSICAL_QUOTIENT_FUNCTOR`, `QFT_PRAW_PFIN_DESCENT`, `rho_AB`, CHSH, and
  Bell work wait on a local gauge groupoid/action and restriction-stability
  proof.

## 4. Immediate parallel-safe lanes

These five are safe to run together because they consume disjoint cycle 2
products and use disjoint write scopes:

| lane | candidate id | prerequisite | proposed write scope |
|---|---|---|---|
| A | `PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST` | `C2_PTUJ_TOOLCHAIN_MANIFEST_GATE` | `explorations/hourly-20260625-1302-next-ptuj-toolchain-source-byte-manifest.md` |
| B | `IG_D7_MULTIPLICITY_TRANSCRIPT` | `C2_IG_D7_MULTIPLICITY_AUDIT_GATE` | `explorations/hourly-20260625-1302-next-ig-d7-multiplicity-transcript.md` |
| C | `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE` | `C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE` | `explorations/hourly-20260625-1302-next-dgu-identity-field-receipt-bundle.md` |
| D | `RS_UCSD_FRAME_SEQUENCE_ACQUISITION` | `C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT` | `explorations/hourly-20260625-1302-next-rs-ucsd-frame-sequence-acquisition.md` |
| E | `QFT_LOCAL_GAUGE_ACTION_GROUPOID` | `C2_QFT_GAUGE_ACTION_RESTRICTION_GATE` | `explorations/hourly-20260625-1302-next-qft-local-gauge-action-groupoid.md` |

## 5. Sequential lanes and why not parallel

| candidate id | must wait for | why not parallel now |
|---|---|---|
| `PTUJ_FRAME_VISIBILITY_AUDIT` | `PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST` | There are no decoded/source outputs to inspect yet. |
| `PTUJ_FORMULA_PACKET` | `PTUJ_FRAME_VISIBILITY_AUDIT` or `PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH` | A formula packet requires actual source evidence. |
| `PTUJ_KEATING_SHEET_IDENTITY` | `PTUJ_FORMULA_PACKET` | Identity comparison needs a formula-bearing object. |
| `IG_KERNEL_IRREDUCIBILITY_FORMAL_PROOF` | `IG_D7_MULTIPLICITY_TRANSCRIPT` | It should respond to the transcript's exact gap or ambiguity. |
| `IG_K_IG_FAMILY_IDENTITY` | `IG_D7_MULTIPLICITY_TRANSCRIPT` | Family identity should not be attempted before the selector source map is verified. |
| `IG_SELECTOR_THEOREM_RESTART` | `IG_D7_MULTIPLICITY_TRANSCRIPT`, `IG_K_IG_FAMILY_IDENTITY` | Multiplicity and identity are prerequisites, not side notes. |
| `IG_FULL_RIVAL_ROW_ELIMINATOR` | `IG_SELECTOR_THEOREM_RESTART`, `IG_K_IG_FAMILY_IDENTITY` | Rival rows require an actual candidate selector and family identity. |
| `DGU_ACTUAL_IDENTITY_WITNESS` | `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE` | Actual identity fields must be emitted first. |
| `DGU_SCOPED_NEGATIVE_RECEIPT` | `DGU_IDENTITY_FIELD_RECEIPT_BUNDLE` | A negative receipt requires complete source-scope absence evidence. |
| `DGU_SYMBOL_CERTIFICATE` | `DGU_ACTUAL_IDENTITY_WITNESS` | Symbol and Q-sector data must belong to the accepted actual operator. |
| `DGU_VZ_REPLAY_GATE` | `DGU_SYMBOL_CERTIFICATE` | VZ replay is downstream of actual certificate data. |
| `RS_UCSD_TYPED_OPERATOR_PACKET` | `RS_UCSD_FRAME_SEQUENCE_ACQUISITION` | Typed fields must be visible or source-tied in frames/slides. |
| `RS_AGGREGATE_ONLY_DEMOTION` | `RS_UCSD_FRAME_SEQUENCE_ACQUISITION` | Demotion requires acquired visual coverage, not transcript-only absence. |
| `RS_RS_ONLY_QUOTIENT_TEST` | `RS_UCSD_TYPED_OPERATOR_PACKET` | The quotient test needs a typed operator candidate. |
| `RS_GENERATION_INDEX_RESTART` | `RS_UCSD_TYPED_OPERATOR_PACKET`, `RS_RS_ONLY_QUOTIENT_TEST` | Generation/index work is a consumer of typed RS data and quotient identity. |
| `QFT_GAUGE_RESTRICTION_STABILITY_PROOF` | `QFT_LOCAL_GAUGE_ACTION_GROUPOID` | The proof needs defined groupoid/action/restriction maps. |
| `QFT_PHYSICAL_QUOTIENT_FUNCTOR` | `QFT_GAUGE_RESTRICTION_STABILITY_PROOF` | `F_phys` is not defined until a source generator is stable. |
| `QFT_SOURCE_KB_CODOMAIN` | `QFT_PHYSICAL_QUOTIENT_FUNCTOR` | Codomain selection must follow the source quotient, not target representation labels. |
| `QFT_PRAW_PFIN_DESCENT` | `QFT_PHYSICAL_QUOTIENT_FUNCTOR`, `QFT_SOURCE_KB_CODOMAIN` | Descent requires both domain quotient and codomain. |

## 6. Lower-quality backup lanes and why demoted

| backup lane | why demoted |
|---|---|
| Broad PTUJ metadata re-review | Cycle 2 already records metadata/storyboard/caption as non-receipts; source bytes or official asset is the real gate. |
| General IG source identity survey | The first blocker is finite D7 multiplicity/highest-weight transcript; survey work risks bypassing the exact obstruction. |
| Broad DGU/VZ status update | DGU/VZ is gated by actual identity fields; status work would not change replay permissions. |
| Transcript-only RS reinterpretation | Cycle 2 already rejects transcript-only promotion; frame acquisition is the missing object. |
| Broad QFT/Bell alignment | Bell/CHSH/rho work is downstream of local gauge groupoid, quotient, and descent. |
| Global negative receipt bundle | Current absences are source-scoped and incomplete; global no-go work is premature. |
| Proof-restart firewall only | Useful as an audit, but it does not produce the missing source objects. |

## 7. Machine-readable JSON summary

```json
{
  "artifact": "NextFrontierDependencyDagAfter1302_V1",
  "run_id": "hourly-20260625-1302",
  "cycle": 3,
  "lane": 5,
  "verdict": "NEXT_FRONTIER_REMAINS_UPSTREAM_SOURCE_OBJECTS_NO_RECEIPTS_NO_PROOF_RESTART",
  "quality_candidates_claimed": 26,
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "known_objects": [
    "C2_PTUJ_TOOLCHAIN_MANIFEST_GATE",
    "C2_IG_D7_MULTIPLICITY_AUDIT_GATE",
    "C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE",
    "C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT",
    "C2_QFT_GAUGE_ACTION_RESTRICTION_GATE",
    "PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST",
    "PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH",
    "PTUJ_FRAME_VISIBILITY_AUDIT",
    "PTUJ_FORMULA_PACKET",
    "PTUJ_KEATING_SHEET_IDENTITY",
    "IG_D7_MULTIPLICITY_TRANSCRIPT",
    "IG_KERNEL_IRREDUCIBILITY_FORMAL_PROOF",
    "IG_SELECTOR_THEOREM_RESTART",
    "IG_K_IG_FAMILY_IDENTITY",
    "IG_FULL_RIVAL_ROW_ELIMINATOR",
    "DGU_IDENTITY_FIELD_RECEIPT_BUNDLE",
    "DGU_ACTUAL_IDENTITY_WITNESS",
    "DGU_SCOPED_NEGATIVE_RECEIPT",
    "DGU_SYMBOL_CERTIFICATE",
    "DGU_VZ_REPLAY_GATE",
    "RS_UCSD_FRAME_SEQUENCE_ACQUISITION",
    "RS_UCSD_TYPED_OPERATOR_PACKET",
    "RS_AGGREGATE_ONLY_DEMOTION",
    "RS_RS_ONLY_QUOTIENT_TEST",
    "RS_GENERATION_INDEX_RESTART",
    "QFT_LOCAL_GAUGE_ACTION_GROUPOID",
    "QFT_GAUGE_RESTRICTION_STABILITY_PROOF",
    "QFT_PHYSICAL_QUOTIENT_FUNCTOR",
    "QFT_PRAW_PFIN_DESCENT",
    "QFT_SOURCE_KB_CODOMAIN",
    "QFT_RHO_AB_CHSH_FIREWALL"
  ],
  "candidates": [
    {"id": "PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST", "quality": true, "parallel_safe": true, "sequential": false, "dependencies": ["C2_PTUJ_TOOLCHAIN_MANIFEST_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-ptuj-toolchain-source-byte-manifest.md"},
    {"id": "PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH", "quality": true, "parallel_safe": false, "sequential": false, "dependencies": ["C2_PTUJ_TOOLCHAIN_MANIFEST_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-ptuj-official-source-asset-branch.md"},
    {"id": "PTUJ_FRAME_VISIBILITY_AUDIT", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST"], "write_scope": "explorations/hourly-20260625-1302-next-ptuj-frame-visibility-audit.md"},
    {"id": "PTUJ_FORMULA_PACKET", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["PTUJ_FRAME_VISIBILITY_AUDIT", "PTUJ_OFFICIAL_SOURCE_ASSET_BRANCH"], "write_scope": "explorations/hourly-20260625-1302-next-ptuj-formula-packet.md"},
    {"id": "PTUJ_KEATING_SHEET_IDENTITY", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["PTUJ_FORMULA_PACKET"], "write_scope": "explorations/hourly-20260625-1302-next-ptuj-keating-sheet-identity.md"},
    {"id": "IG_D7_MULTIPLICITY_TRANSCRIPT", "quality": true, "parallel_safe": true, "sequential": false, "dependencies": ["C2_IG_D7_MULTIPLICITY_AUDIT_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-ig-d7-multiplicity-transcript.md"},
    {"id": "IG_KERNEL_IRREDUCIBILITY_FORMAL_PROOF", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["IG_D7_MULTIPLICITY_TRANSCRIPT"], "write_scope": "explorations/hourly-20260625-1302-next-ig-kernel-irreducibility-formal-proof.md"},
    {"id": "IG_SELECTOR_THEOREM_RESTART", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["IG_D7_MULTIPLICITY_TRANSCRIPT", "IG_K_IG_FAMILY_IDENTITY"], "write_scope": "explorations/hourly-20260625-1302-next-ig-selector-theorem-restart.md"},
    {"id": "IG_K_IG_FAMILY_IDENTITY", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["IG_D7_MULTIPLICITY_TRANSCRIPT"], "write_scope": "explorations/hourly-20260625-1302-next-ig-k-ig-family-identity.md"},
    {"id": "IG_FULL_RIVAL_ROW_ELIMINATOR", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["IG_SELECTOR_THEOREM_RESTART", "IG_K_IG_FAMILY_IDENTITY"], "write_scope": "explorations/hourly-20260625-1302-next-ig-full-rival-row-eliminator.md"},
    {"id": "DGU_IDENTITY_FIELD_RECEIPT_BUNDLE", "quality": true, "parallel_safe": true, "sequential": false, "dependencies": ["C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-dgu-identity-field-receipt-bundle.md"},
    {"id": "DGU_ACTUAL_IDENTITY_WITNESS", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["DGU_IDENTITY_FIELD_RECEIPT_BUNDLE"], "write_scope": "explorations/hourly-20260625-1302-next-dgu-actual-identity-witness.md"},
    {"id": "DGU_SCOPED_NEGATIVE_RECEIPT", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["DGU_IDENTITY_FIELD_RECEIPT_BUNDLE"], "write_scope": "explorations/hourly-20260625-1302-next-dgu-scoped-negative-receipt.md"},
    {"id": "DGU_SYMBOL_CERTIFICATE", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["DGU_ACTUAL_IDENTITY_WITNESS"], "write_scope": "explorations/hourly-20260625-1302-next-dgu-symbol-certificate.md"},
    {"id": "DGU_VZ_REPLAY_GATE", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["DGU_SYMBOL_CERTIFICATE"], "write_scope": "explorations/hourly-20260625-1302-next-dgu-vz-replay-gate.md"},
    {"id": "RS_UCSD_FRAME_SEQUENCE_ACQUISITION", "quality": true, "parallel_safe": true, "sequential": false, "dependencies": ["C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT"], "write_scope": "explorations/hourly-20260625-1302-next-rs-ucsd-frame-sequence-acquisition.md"},
    {"id": "RS_UCSD_TYPED_OPERATOR_PACKET", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["RS_UCSD_FRAME_SEQUENCE_ACQUISITION"], "write_scope": "explorations/hourly-20260625-1302-next-rs-ucsd-typed-operator-packet.md"},
    {"id": "RS_AGGREGATE_ONLY_DEMOTION", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["RS_UCSD_FRAME_SEQUENCE_ACQUISITION"], "write_scope": "explorations/hourly-20260625-1302-next-rs-aggregate-only-demotion.md"},
    {"id": "RS_RS_ONLY_QUOTIENT_TEST", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["RS_UCSD_TYPED_OPERATOR_PACKET"], "write_scope": "explorations/hourly-20260625-1302-next-rs-only-quotient-test.md"},
    {"id": "RS_GENERATION_INDEX_RESTART", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["RS_UCSD_TYPED_OPERATOR_PACKET", "RS_RS_ONLY_QUOTIENT_TEST"], "write_scope": "explorations/hourly-20260625-1302-next-rs-generation-index-restart.md"},
    {"id": "QFT_LOCAL_GAUGE_ACTION_GROUPOID", "quality": true, "parallel_safe": true, "sequential": false, "dependencies": ["C2_QFT_GAUGE_ACTION_RESTRICTION_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-qft-local-gauge-action-groupoid.md"},
    {"id": "QFT_GAUGE_RESTRICTION_STABILITY_PROOF", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["QFT_LOCAL_GAUGE_ACTION_GROUPOID"], "write_scope": "explorations/hourly-20260625-1302-next-qft-gauge-restriction-stability-proof.md"},
    {"id": "QFT_PHYSICAL_QUOTIENT_FUNCTOR", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["QFT_GAUGE_RESTRICTION_STABILITY_PROOF"], "write_scope": "explorations/hourly-20260625-1302-next-qft-physical-quotient-functor.md"},
    {"id": "QFT_PRAW_PFIN_DESCENT", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["QFT_PHYSICAL_QUOTIENT_FUNCTOR", "QFT_SOURCE_KB_CODOMAIN"], "write_scope": "explorations/hourly-20260625-1302-next-qft-praw-pfin-descent.md"},
    {"id": "QFT_SOURCE_KB_CODOMAIN", "quality": true, "parallel_safe": false, "sequential": true, "dependencies": ["QFT_PHYSICAL_QUOTIENT_FUNCTOR"], "write_scope": "explorations/hourly-20260625-1302-next-qft-source-kb-codomain.md"},
    {"id": "QFT_RHO_AB_CHSH_FIREWALL", "quality": true, "parallel_safe": false, "sequential": false, "dependencies": ["C2_QFT_GAUGE_ACTION_RESTRICTION_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-qft-rho-ab-chsh-firewall.md"}
  ],
  "immediate_parallel_safe_lanes": [
    {"id": "PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST", "prerequisites": ["C2_PTUJ_TOOLCHAIN_MANIFEST_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-ptuj-toolchain-source-byte-manifest.md"},
    {"id": "IG_D7_MULTIPLICITY_TRANSCRIPT", "prerequisites": ["C2_IG_D7_MULTIPLICITY_AUDIT_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-ig-d7-multiplicity-transcript.md"},
    {"id": "DGU_IDENTITY_FIELD_RECEIPT_BUNDLE", "prerequisites": ["C2_DGU_IDENTITY_FIELD_PROTOCOL_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-dgu-identity-field-receipt-bundle.md"},
    {"id": "RS_UCSD_FRAME_SEQUENCE_ACQUISITION", "prerequisites": ["C2_RS_UCSD_FRAME_ACQUISITION_CONTRACT"], "write_scope": "explorations/hourly-20260625-1302-next-rs-ucsd-frame-sequence-acquisition.md"},
    {"id": "QFT_LOCAL_GAUGE_ACTION_GROUPOID", "prerequisites": ["C2_QFT_GAUGE_ACTION_RESTRICTION_GATE"], "write_scope": "explorations/hourly-20260625-1302-next-qft-local-gauge-action-groupoid.md"}
  ],
  "sequential_lanes": [
    "PTUJ_FRAME_VISIBILITY_AUDIT",
    "PTUJ_FORMULA_PACKET",
    "PTUJ_KEATING_SHEET_IDENTITY",
    "IG_KERNEL_IRREDUCIBILITY_FORMAL_PROOF",
    "IG_SELECTOR_THEOREM_RESTART",
    "IG_K_IG_FAMILY_IDENTITY",
    "IG_FULL_RIVAL_ROW_ELIMINATOR",
    "DGU_ACTUAL_IDENTITY_WITNESS",
    "DGU_SCOPED_NEGATIVE_RECEIPT",
    "DGU_SYMBOL_CERTIFICATE",
    "DGU_VZ_REPLAY_GATE",
    "RS_UCSD_TYPED_OPERATOR_PACKET",
    "RS_AGGREGATE_ONLY_DEMOTION",
    "RS_RS_ONLY_QUOTIENT_TEST",
    "RS_GENERATION_INDEX_RESTART",
    "QFT_GAUGE_RESTRICTION_STABILITY_PROOF",
    "QFT_PHYSICAL_QUOTIENT_FUNCTOR",
    "QFT_SOURCE_KB_CODOMAIN",
    "QFT_PRAW_PFIN_DESCENT"
  ],
  "next_five_goals_recommendation": [
    "PTUJ_TOOLCHAIN_SOURCE_BYTE_MANIFEST",
    "IG_D7_MULTIPLICITY_TRANSCRIPT",
    "DGU_IDENTITY_FIELD_RECEIPT_BUNDLE",
    "RS_UCSD_FRAME_SEQUENCE_ACQUISITION",
    "QFT_LOCAL_GAUGE_ACTION_GROUPOID"
  ],
  "proof_restart_allowed": false,
  "accepted_receipt_count": 0
}
```
