---
title: "Hourly 20260625 0803 Cycle 3 Receipt Transition Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-0803"
cycle: 3
lane: 2
doc_type: receipt_transition_matrix
artifact_id: "ReceiptTransitionMatrixAfter0803_V1"
verdict: "ZERO_TRANSITIONS_TO_ACCEPTED_ROUTING_OR_PROOF_RESTART"
owned_path: "explorations/hourly-20260625-0803-cycle3-receipt-transition-matrix.md"
companion_audit: "tests/hourly_20260625_0803_cycle3_receipt_transition_matrix_audit.py"
---

# Hourly 20260625 0803 Cycle 3 Receipt Transition Matrix

## 1. Verdict

Verdict: **blocked; zero normalized cycle 1-2 candidate rows transition to
`accepted_for_routing` or `proof_restart_ready`**.

The ten 0803 cycle 1-2 gates improved the frontier by defining contracts,
schemas, rival inventories, and source-origin classifiers. None emitted an
accepted receipt with route-specific family identity. Therefore no route is
ready for proof restart.

Decision state:

```text
artifact: ReceiptTransitionMatrixAfter0803_V1
normalized_candidate_row_count: 25
accepted_receipt_count: 0
accepted_for_routing_count: 0
proof_restart_ready_count: 0
transition_decision: no_candidate_transitioned
```

The strongest positive result is not a proof result. PTUJ now has a precise
acquisition contract; IG now has a rival-eliminator matrix; DGU/Oxford now has
an actual-operator certificate field matrix; RS now has a UCSD source-origin
host classifier; QFT now has a source-equivalence/descent schema. These are
useful next objects, but they remain uninhabited or identity-blocked.

## 2. Candidate transition rules

A candidate row may transition to `accepted_for_routing` only if all of the
following hold:

1. `accepted_receipt` is true.
2. The route-specific identity, selector, acquisition, operator, or quotient
   object is source-clean and accepted.
3. `family_identity` is `passed` where the route has a family identity gate, or
   `not_required` only for a pure acquisition/schema row that does not itself
   claim family routing.
4. The target-import guard is clean.
5. The row is not merely a contract, schema, hosted surface, locator, caption,
   scoped fail, or conditional specification.

A candidate row may transition to `proof_restart_ready` only if it has already
transitioned to accepted routing and the downstream route-specific restart
conditions are also present. For this run, every source artifact reports zero
accepted receipts or non-runnable family identity, so every row has:

```text
accepted_receipt: false
accepted_for_routing: false
proof_restart_ready: false
```

Status vocabulary used in this matrix:

| status | meaning |
|---|---|
| `contract_defined` | the acceptance contract is now explicit, but no satisfying source asset or data exists. |
| `hosted_candidate` | a source or canon surface hosts a plausible candidate or rival, without source-forced selection. |
| `blocked_identity` | the route has source-adjacent material, but lacks the required identity, selector, or family witness. |
| `blocked_acquisition` | the route is stopped before formula/source receipt admission by missing lawful acquisition or asset. |
| `source_schema_shell` | a mathematical schema or conditional object is specified, but source data do not inhabit it. |
| `scoped_fail_preserved` | a prior local fail remains scoped and is not converted into a global no-go. |
| `accepted_for_routing` | accepted receipt plus route-specific identity/selector/acquisition proof passed. |
| `proof_restart_ready` | accepted routing plus route-specific proof restart prerequisites passed. |

## 3. Candidate rows by route

| row id | route | source/object | status | accepted receipt | accepted for routing | family identity | proof restart ready | first obstruction | next object |
|---|---|---|---|---:|---:|---|---:|---|---|
| `PTUJ_SOURCE_LOCATORS` | PTUJ_Keating | PTUJ page, YouTube/oEmbed/thumbnail, Keating transcript, manuscript adjacency | `blocked_acquisition` | false | false | blocked | false | metadata and locators are not formula-bearing source assets | `LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` |
| `PTUJ_LOCAL_EXTRACTOR_CONTRACT` | PTUJ_Keating | `LawfulLocalTzSEvmqxu48FrameExtractor_V1` | `contract_defined` | false | false | not_runnable | false | no admitted `yt-dlp`/`ffmpeg` or equivalent extractor path with provenance | `LawfulLocalTzSEvmqxu48FrameExtractor_V1` |
| `PTUJ_OFFICIAL_SOURCE_ASSET_CONTRACT` | PTUJ_Keating | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1` | `contract_defined` | false | false | not_runnable | false | no official/custodian source package, manifest, checksum, or formula visibility evidence | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1` |
| `PTUJ_FORMULA_PACKET` | PTUJ_Keating | `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` | `blocked_acquisition` | false | false | not_runnable | false | no formula-bearing frame, sheet, page, or complete full-resolution formula-negative audit | `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` |
| `PTUJ_KEATING_SHEET` | PTUJ_Keating | `KeatingRevealed_ShiabProjectionSheet_V1` | `blocked_acquisition` | false | false | not_runnable | false | the transcript gives a missing-sheet locator, not the sheet | `KeatingRevealed_ShiabProjectionSheet_V1` |
| `PTUJ_MANUSCRIPT_SELECTOR_IDENTITY` | PTUJ_Keating | manuscript pages 41-44 as adjacent Shiab candidate | `blocked_identity` | false | false | blocked | false | no source-emitted identity to the Keating sheet or `SourceForcedCodomainSelectorForK_IG` | `manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG` |
| `IG_DISPLAYED_OR_CANON_SHIAB` | IG_selector | displayed/canon Cl(9,5) Shiab Clifford contraction | `hosted_candidate` | false | false | failed_missing_witness | false | existence is not source-forced selection | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_EXTERIOR_COVARIANT_DERIVATIVE` | IG_selector | exterior/covariant derivative rival | `hosted_candidate` | false | false | failed_missing_witness | false | no Bianchi/highest-weight eliminator excludes derivative-type rivals | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_EINSTEIN_RICCI_CONTRACTION` | IG_selector | Einstein/Ricci-style contraction rival | `hosted_candidate` | false | false | failed_missing_witness | false | no source rule distinguishes Shiab from contraction-only analogs | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_HODGE_DIMENSION_SHIFT` | IG_selector | Hodge/star or dimension-shift rival | `hosted_candidate` | false | false | failed_missing_witness | false | no dimension/signature/representation criterion rules it out | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_SYMMETRIC_PRODUCT` | IG_selector | symmetric product or symmetric derivative rival | `hosted_candidate` | false | false | failed_missing_witness | false | no highest-weight decomposition eliminates the symmetric branch | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_PROJECTION_DEPENDENT_SHIAB` | IG_selector | projection-dependent Shiab variants | `hosted_candidate` | false | false | failed_missing_witness | false | projector policy and projection-loss behavior are not source-selected | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_LOWER_ORDER_DRESSED` | IG_selector | lower-order dressed or torsion/gauge-deformed variants | `hosted_candidate` | false | false | failed_missing_witness | false | no source rigidity rule forbids dressing | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_OXFORD_VISUAL_VARIANT` | IG_selector | Oxford 02:33:43 visual formula variant | `blocked_identity` | false | false | blocked | false | formula identity to manuscript/canon/notes selector is missing | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `IG_PTUJ_MISSING_SHEET_VARIANT` | IG_selector | PTUJ/Keating missing-sheet variant | `blocked_acquisition` | false | false | blocked | false | recovered sheet or source-equivalent calculation is absent | `LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` |
| `IG_UCSD_MIDDLE_MAP_VARIANT` | IG_selector | UCSD omega-one to omega-d-minus-one middle-map variant | `hosted_candidate` | false | false | failed_missing_witness | false | UCSD motivates a middle map but does not tie an explicit selector to `K_IG` | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` |
| `DGU_OXFORD_023510` | DGU_Oxford | Oxford 02:35:10 bosonic replacement equation | `blocked_identity` | false | false | blocked | false | no identity witness to actual `D_GU^epsilon` 0/1 data | `ActualDGU01OperatorCertificateInstance_V1` |
| `DGU_OXFORD_023612` | DGU_Oxford | Oxford 02:36:12 `S_omega = J_omega` anchor | `blocked_identity` | false | false | blocked | false | no sector rule, domain/codomain, coefficients, projectors, or principal-symbol data | `ActualDGU01OperatorCertificateInstance_V1` |
| `DGU_ACTUAL_OPERATOR_CERTIFICATE` | DGU_Oxford | actual `D_GU^epsilon` 0/1 certificate object | `blocked_identity` | false | false | blocked | false | source-clean actual-operator identity witness is absent | `source_clean_identity_witness_for_actual_D_GU_epsilon_0_1` |
| `DGU_CERTIFICATE_FIELD_MATRIX` | DGU_Oxford | certificate field matrix, ten required fields | `blocked_identity` | false | false | blocked | false | zero of ten certificate fields are accepted | `ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness` |
| `RS_EQUATION_1010` | RS | manuscript equation 10.10 image/cell route | `scoped_fail_preserved` | false | false | failed | false | local cell typing found no pure RS minus-one rule | `ImageTypedRSMinusOneRuleCell_V1` only if new source evidence appears |
| `RS_UCSD_HOSTED_OPERATOR_IDEA` | RS | UCSD rolled-up Dirac/de Rham/Rarita-Schwinger source-origin surface | `hosted_candidate` | false | false | not_runnable | false | hosted aggregate operator idea lacks pure-RS source/target typing | `UCSDTypedRSMinusOneOperator_V1` |
| `RS_UCSD_TYPED_OPERATOR_SPEC` | RS | conditional `UCSDTypedRSMinusOneOperator_V1` specification | `source_schema_shell` | false | false | not_runnable | false | no exact slide/frame operator packet, pure-RS projection, or family certificate | `UCSDTypedRSMinusOneOperator_V1` |
| `QFT_LOCAL_PHYSICAL_QUOTIENT_SHELL` | QFT | `LocalPhysicalFieldQuotientAndNaturalityLemma_V1` | `source_schema_shell` | false | false | not_required | false | `F_phys^b(O)`, `K_b`, and `P_fin^b` are not source-defined | `SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1` |
| `QFT_EQUIVALENCE_DESCENT_SCHEMA` | QFT | `SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1` | `source_schema_shell` | false | false | not_required | false | schema is specified but source congruence generators are absent | `CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1` |

## 4. Route status summaries

| route | row count | dominant status | accepted receipts | accepted for routing | proof restart ready | route summary |
|---|---:|---|---:|---:|---:|---|
| PTUJ_Keating | 6 | `blocked_acquisition` / `contract_defined` | 0 | 0 | 0 | Acquisition contract is defined, but no lawful extractor, official asset, formula packet, or Keating sheet exists. |
| IG_selector | 10 | `hosted_candidate` | 0 | 0 | 0 | Shiab and rival families are inventoried, but no Bianchi/highest-weight selector theorem eliminates rivals or passes identity. |
| DGU_Oxford | 4 | `blocked_identity` | 0 | 0 | 0 | Oxford/manuscript/UCSD material remains adjacent to actual DGU 0/1 data, not identified with it. |
| RS | 3 | mixed `scoped_fail_preserved`, `hosted_candidate`, `source_schema_shell` | 0 | 0 | 0 | Equation 10.10 remains a scoped fail; UCSD hosts an aggregate operator idea but not a typed pure-RS minus-one rule. |
| QFT | 2 | `source_schema_shell` | 0 | 0 | 0 | Quotient/descent schema is explicit, but no source congruence generators or descended finite extraction exist. |

Status counts:

| status | count |
|---|---:|
| `contract_defined` | 2 |
| `hosted_candidate` | 9 |
| `blocked_identity` | 6 |
| `blocked_acquisition` | 4 |
| `source_schema_shell` | 3 |
| `scoped_fail_preserved` | 1 |
| `accepted_for_routing` | 0 |
| `proof_restart_ready` | 0 |

## 5. Transition decision

No candidate transitioned.

The deciding invariant is:

```text
accepted_for_routing requires accepted_receipt_count > 0
and route-specific identity / selector / acquisition / operator / quotient
status passed.
```

Every route fails before that invariant:

- PTUJ fails at acquisition and source-asset admission.
- IG fails at source-natural selector and rival elimination.
- DGU/Oxford fails at actual `D_GU^epsilon` 0/1 identity.
- RS preserves the equation 10.10 scoped fail and keeps UCSD as a hosted,
  underdefined aggregate operator surface.
- QFT fails before extraction because the source physical equivalence relation
  and descent data are absent.

Therefore:

```text
any_candidate_transitioned_to_accepted_for_routing: false
any_candidate_transitioned_to_proof_restart_ready: false
```

## 6. Next object queue

Priority queue for the next sequential work:

| priority | route | next object | why this is next |
|---:|---|---|---|
| 1 | PTUJ_Keating | `LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` | It is the first object that can turn metadata and locators into an auditable source/frame/asset packet. |
| 2 | IG_selector | `SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1` | It is the first object that can select Shiab against representation-natural rivals. |
| 3 | DGU_Oxford | `source_clean_identity_witness_for_actual_D_GU_epsilon_0_1` | It is required before actual DGU certificate, VZ replay, or physical-recovery work. |
| 4 | RS | `UCSDTypedRSMinusOneOperator_V1` | It is the first possible alternate RS source-origin operator after equation 10.10's scoped fail. |
| 5 | QFT | `CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1` | It is required before `F_phys^b(O)`, `P_fin^b`, local mode images, `rho_AB`, CHSH, or Bell work. |

## 7. Machine-readable JSON summary

```json
{
  "artifact": "ReceiptTransitionMatrixAfter0803_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0803",
  "cycle": 3,
  "lane": 2,
  "source_cycles": [1, 2],
  "verdict": "ZERO_TRANSITIONS_TO_ACCEPTED_ROUTING_OR_PROOF_RESTART",
  "verdict_class": "blocked",
  "status_vocabulary": [
    "contract_defined",
    "hosted_candidate",
    "blocked_identity",
    "blocked_acquisition",
    "source_schema_shell",
    "scoped_fail_preserved",
    "accepted_for_routing",
    "proof_restart_ready"
  ],
  "required_routes": [
    "PTUJ_Keating",
    "IG_selector",
    "DGU_Oxford",
    "RS",
    "QFT"
  ],
  "row_count": 25,
  "route_counts": {
    "PTUJ_Keating": 6,
    "IG_selector": 10,
    "DGU_Oxford": 4,
    "RS": 3,
    "QFT": 2
  },
  "status_counts": {
    "contract_defined": 2,
    "hosted_candidate": 9,
    "blocked_identity": 6,
    "blocked_acquisition": 4,
    "source_schema_shell": 3,
    "scoped_fail_preserved": 1,
    "accepted_for_routing": 0,
    "proof_restart_ready": 0
  },
  "transition_counts": {
    "accepted_receipt_count": 0,
    "accepted_for_routing_count": 0,
    "proof_restart_ready_count": 0,
    "transitioned_to_accepted_for_routing": 0,
    "transitioned_to_proof_restart_ready": 0
  },
  "transition_decision": {
    "any_candidate_transitioned_to_accepted_for_routing": false,
    "any_candidate_transitioned_to_proof_restart_ready": false,
    "why_not": "Every route lacks the route-specific accepted receipt plus source-clean identity, selector, lawful acquisition, pure operator, or source equivalence/descent data required for routing."
  },
  "route_status": {
    "PTUJ_Keating": {
      "row_count": 6,
      "status_counts": {
        "blocked_acquisition": 3,
        "contract_defined": 2,
        "blocked_identity": 1
      },
      "accepted_receipts": 0,
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1 has no admitted extractor branch or official source-asset branch.",
      "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1"
    },
    "IG_selector": {
      "row_count": 10,
      "status_counts": {
        "hosted_candidate": 8,
        "blocked_identity": 1,
        "blocked_acquisition": 1
      },
      "accepted_receipts": 0,
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1 is missing.",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    "DGU_Oxford": {
      "row_count": 4,
      "status_counts": {
        "blocked_identity": 4
      },
      "accepted_receipts": 0,
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "source_clean_identity_witness_for_actual_D_GU_epsilon_0_1 is missing.",
      "next_object": "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness"
    },
    "RS": {
      "row_count": 3,
      "status_counts": {
        "scoped_fail_preserved": 1,
        "hosted_candidate": 1,
        "source_schema_shell": 1
      },
      "accepted_receipts": 0,
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "UCSDTypedRSMinusOneOperator_V1 lacks pure-RS source/target typing, slot, formula, projection or quotient, and family identity.",
      "next_object": "UCSDTypedRSMinusOneOperator_V1"
    },
    "QFT": {
      "row_count": 2,
      "status_counts": {
        "source_schema_shell": 2
      },
      "accepted_receipts": 0,
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "source_defined_congruence_generators_for_tilde_phys_b_O are absent.",
      "next_object": "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1"
    }
  },
  "candidate_rows": [
    {
      "row_id": "PTUJ_SOURCE_LOCATORS",
      "route": "PTUJ_Keating",
      "source_object": "PTUJ page, YouTube/oEmbed/thumbnail, Keating transcript, manuscript adjacency",
      "candidate_status": "blocked_acquisition",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "metadata and locators are not formula-bearing source assets",
      "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1"
    },
    {
      "row_id": "PTUJ_LOCAL_EXTRACTOR_CONTRACT",
      "route": "PTUJ_Keating",
      "source_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
      "candidate_status": "contract_defined",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_runnable",
      "proof_restart_ready": false,
      "first_obstruction": "no admitted local extractor path with provenance",
      "next_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1"
    },
    {
      "row_id": "PTUJ_OFFICIAL_SOURCE_ASSET_CONTRACT",
      "route": "PTUJ_Keating",
      "source_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
      "candidate_status": "contract_defined",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_runnable",
      "proof_restart_ready": false,
      "first_obstruction": "no official source package, manifest, checksum, or formula visibility evidence",
      "next_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1"
    },
    {
      "row_id": "PTUJ_FORMULA_PACKET",
      "route": "PTUJ_Keating",
      "source_object": "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
      "candidate_status": "blocked_acquisition",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_runnable",
      "proof_restart_ready": false,
      "first_obstruction": "no formula-bearing frame, sheet, page, or complete formula-negative audit",
      "next_object": "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1"
    },
    {
      "row_id": "PTUJ_KEATING_SHEET",
      "route": "PTUJ_Keating",
      "source_object": "KeatingRevealed_ShiabProjectionSheet_V1",
      "candidate_status": "blocked_acquisition",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_runnable",
      "proof_restart_ready": false,
      "first_obstruction": "missing-sheet locator does not supply the sheet",
      "next_object": "KeatingRevealed_ShiabProjectionSheet_V1"
    },
    {
      "row_id": "PTUJ_MANUSCRIPT_SELECTOR_IDENTITY",
      "route": "PTUJ_Keating",
      "source_object": "manuscript pages 41-44 as adjacent Shiab candidate",
      "candidate_status": "blocked_identity",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "no source identity to Keating sheet or SourceForcedCodomainSelectorForK_IG",
      "next_object": "manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG"
    },
    {
      "row_id": "IG_DISPLAYED_OR_CANON_SHIAB",
      "route": "IG_selector",
      "source_object": "displayed/canon Cl(9,5) Shiab Clifford contraction",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "existence is not source-forced selection",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_EXTERIOR_COVARIANT_DERIVATIVE",
      "route": "IG_selector",
      "source_object": "exterior/covariant derivative rival",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "no eliminator excludes derivative-type rivals",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_EINSTEIN_RICCI_CONTRACTION",
      "route": "IG_selector",
      "source_object": "Einstein/Ricci-style contraction rival",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "no source rule distinguishes Shiab from contraction-only analogs",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_HODGE_DIMENSION_SHIFT",
      "route": "IG_selector",
      "source_object": "Hodge/star or dimension-shift rival",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "no criterion rules out star-like alternatives",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_SYMMETRIC_PRODUCT",
      "route": "IG_selector",
      "source_object": "symmetric product or symmetric derivative rival",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "no highest-weight decomposition eliminates the symmetric branch",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_PROJECTION_DEPENDENT_SHIAB",
      "route": "IG_selector",
      "source_object": "projection-dependent Shiab variants",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "projector policy and projection-loss behavior are not source-selected",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_LOWER_ORDER_DRESSED",
      "route": "IG_selector",
      "source_object": "lower-order dressed or torsion/gauge-deformed variants",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "no source rigidity rule forbids dressing",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_OXFORD_VISUAL_VARIANT",
      "route": "IG_selector",
      "source_object": "Oxford 02:33:43 visual formula variant",
      "candidate_status": "blocked_identity",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "formula identity to manuscript/canon/notes selector is missing",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "IG_PTUJ_MISSING_SHEET_VARIANT",
      "route": "IG_selector",
      "source_object": "PTUJ/Keating missing-sheet variant",
      "candidate_status": "blocked_acquisition",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "recovered sheet or source-equivalent calculation is absent",
      "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1"
    },
    {
      "row_id": "IG_UCSD_MIDDLE_MAP_VARIANT",
      "route": "IG_selector",
      "source_object": "UCSD omega-one to omega-d-minus-one middle-map variant",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed_missing_witness",
      "proof_restart_ready": false,
      "first_obstruction": "UCSD motivates a middle map but does not tie an explicit selector to K_IG",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "row_id": "DGU_OXFORD_023510",
      "route": "DGU_Oxford",
      "source_object": "Oxford 02:35:10 bosonic replacement equation",
      "candidate_status": "blocked_identity",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "no identity witness to actual D_GU_epsilon 0/1 data",
      "next_object": "ActualDGU01OperatorCertificateInstance_V1"
    },
    {
      "row_id": "DGU_OXFORD_023612",
      "route": "DGU_Oxford",
      "source_object": "Oxford 02:36:12 S_omega = J_omega anchor",
      "candidate_status": "blocked_identity",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "no sector rule, domain/codomain, coefficients, projectors, or principal-symbol data",
      "next_object": "ActualDGU01OperatorCertificateInstance_V1"
    },
    {
      "row_id": "DGU_ACTUAL_OPERATOR_CERTIFICATE",
      "route": "DGU_Oxford",
      "source_object": "actual D_GU_epsilon 0/1 certificate object",
      "candidate_status": "blocked_identity",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "source-clean actual-operator identity witness is absent",
      "next_object": "source_clean_identity_witness_for_actual_D_GU_epsilon_0_1"
    },
    {
      "row_id": "DGU_CERTIFICATE_FIELD_MATRIX",
      "route": "DGU_Oxford",
      "source_object": "certificate field matrix, ten required fields",
      "candidate_status": "blocked_identity",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "blocked",
      "proof_restart_ready": false,
      "first_obstruction": "zero of ten certificate fields are accepted",
      "next_object": "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness"
    },
    {
      "row_id": "RS_EQUATION_1010",
      "route": "RS",
      "source_object": "manuscript equation 10.10 image/cell route",
      "candidate_status": "scoped_fail_preserved",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "failed",
      "proof_restart_ready": false,
      "first_obstruction": "local cell typing found no pure RS minus-one rule",
      "next_object": "ImageTypedRSMinusOneRuleCell_V1 only if new source evidence appears"
    },
    {
      "row_id": "RS_UCSD_HOSTED_OPERATOR_IDEA",
      "route": "RS",
      "source_object": "UCSD rolled-up Dirac/de Rham/Rarita-Schwinger source-origin surface",
      "candidate_status": "hosted_candidate",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_runnable",
      "proof_restart_ready": false,
      "first_obstruction": "hosted aggregate operator idea lacks pure-RS source/target typing",
      "next_object": "UCSDTypedRSMinusOneOperator_V1"
    },
    {
      "row_id": "RS_UCSD_TYPED_OPERATOR_SPEC",
      "route": "RS",
      "source_object": "conditional UCSDTypedRSMinusOneOperator_V1 specification",
      "candidate_status": "source_schema_shell",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_runnable",
      "proof_restart_ready": false,
      "first_obstruction": "no exact slide/frame operator packet, pure-RS projection, or family certificate",
      "next_object": "UCSDTypedRSMinusOneOperator_V1"
    },
    {
      "row_id": "QFT_LOCAL_PHYSICAL_QUOTIENT_SHELL",
      "route": "QFT",
      "source_object": "LocalPhysicalFieldQuotientAndNaturalityLemma_V1",
      "candidate_status": "source_schema_shell",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_required",
      "proof_restart_ready": false,
      "first_obstruction": "F_phys_b_O, K_b, and P_fin_b are not source-defined",
      "next_object": "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1"
    },
    {
      "row_id": "QFT_EQUIVALENCE_DESCENT_SCHEMA",
      "route": "QFT",
      "source_object": "SourceDefinedLocalPhysicalFieldEquivalenceRelationAndDescentData_V1",
      "candidate_status": "source_schema_shell",
      "accepted_receipt": false,
      "accepted_for_routing": false,
      "family_identity": "not_required",
      "proof_restart_ready": false,
      "first_obstruction": "schema is specified but source congruence generators are absent",
      "next_object": "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1"
    }
  ],
  "next_object_queue": [
    {
      "priority": 1,
      "route": "PTUJ_Keating",
      "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1"
    },
    {
      "priority": 2,
      "route": "IG_selector",
      "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
    },
    {
      "priority": 3,
      "route": "DGU_Oxford",
      "next_object": "source_clean_identity_witness_for_actual_D_GU_epsilon_0_1"
    },
    {
      "priority": 4,
      "route": "RS",
      "next_object": "UCSDTypedRSMinusOneOperator_V1"
    },
    {
      "priority": 5,
      "route": "QFT",
      "next_object": "CandidateCongruenceGeneratorsForLocalGUPhysicalFieldEquivalence_V1"
    }
  ]
}
```
