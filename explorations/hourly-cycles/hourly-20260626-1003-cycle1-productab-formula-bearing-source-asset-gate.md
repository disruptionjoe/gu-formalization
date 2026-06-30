---
title: "Hourly 20260626 1003 Cycle 1 ProductAB Formula Bearing Source Asset Gate"
date: "2026-06-26"
run_id: "hourly-20260626-1003"
cycle: 1
lane: 4
doc_type: "frontier_run_lane_artifact"
artifact_id: "FormulaBearingPTUJOrKeatingSourceAssetGate_1003_C1_L4_V1"
verdict: "blocked_no_formula_bearing_ptuj_or_keating_source_asset"
owned_path: "explorations/hourly-20260626-1003-cycle1-productab-formula-bearing-source-asset-gate.md"
claim_status_change: false
---

# Hourly 20260626 1003 Cycle 1 ProductAB Formula Bearing Source Asset Gate

## 1. Verdict

Verdict: **blocked**.

`FormulaBearingPTUJOrKeatingSourceAsset_V1` is not present in the repo-local
source/media artifacts. No PTUJ or Keating object currently has all required
fields:

```text
content access or source bytes
checksum or custody
decode/output manifest
bounded formula-visibility scope
```

Therefore visible-formula transcription remains disallowed, and no ProductAB
member is emitted.

Decision state:

```text
formula_bearing_source_asset_present: false
content_access_or_source_bytes_present: false
checksum_or_custody_present: false
decode_output_manifest_present: false
formula_visibility_scope_present: false
visible_formula_transcription_allowed: false
productab_member_emitted: false
target_import_used: false
claim_status_change: false
```

This is a repo-local asset gate decision, not a global no-go over PTUJ, Keating,
or Product A/B.

## 2. What Was Derived Directly From Repo Sources

Read-first sources establish the governing constraints:

| source | direct consequence |
|---|---|
| `RESEARCH-POSTURE.md` | Do not convert compatibility, metadata, or optimism into a derivation. |
| `process/runbooks/five-lane-frontier-run.md` | This lane must decide the first missing proof object and avoid claim-status changes. |
| `explorations/remaining-math-topography-ledger-v0-2026-06-26.md` | ProductAB/PTUJ lives first on provenance-verifier terrain; downstream spectral/descent work is premature without a source witness. |
| `explorations/hourly-20260626-0904-cycle3-productab-formula-visibility-prereq.md` | The prerequisite gate closed with content/source bytes, checksum/custody, decode manifest, and visibility scope all absent. |
| `explorations/hourly-20260626-0904-cycle2-productab-ptuj-acquisition-manifest.md` | PTUJ route identity exists, but no branch-pure source-byte object, decoded output manifest, frame checksum, or Keating sheet package exists. |
| `sources/media-index.md` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is metadata-checked only; Keating surfaces are metadata-checked or timestamp-needed, not mined formula assets. |
| `sources/media-mining-coverage-gaps-v1.md` | Keating/JRE/TOE follow-up mining remains an explicit coverage gap; it has not supplied a source object. |

Additional repo-local file checks found:

| checked object class | result |
|---|---|
| `sources/` raw media files | none; `sources/` contains markdown ledgers only |
| PTUJ/Keating named image/video/subtitle/json files | none found |
| repo-local PDFs | only `Geometric_UnityDraftApril1st2021.pdf`, checksum `sha256:3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4` |
| binary/media-like files | unrelated RS manuscript render PNGs and automation JSON; no PTUJ/Keating source asset |

The manuscript PDF is a useful comparison/reference object. It is not the
requested PTUJ/Keating frame, video source-byte object, or Keating missing-sheet
asset.

## 3. Strongest Positive Result

The strongest positive result remains route identity, not formula-bearing
content:

```text
target video id: TzSEvmqxu48
official PTUJ page identity/caption locator
YouTube oEmbed metadata for TzSEvmqxu48
Keating missing-sheet transcript window
repo-local author manuscript PDF with checksum
prior Oxford reference still checksum row from earlier artifacts
```

This is enough to know which object should be acquired. It is not enough to
transcribe a visible formula or emit a ProductAB member.

## 4. First Exact Obstruction

First exact obstruction:

```text
FormulaBearingPTUJOrKeatingSourceAsset_V1.content_access_or_source_bytes
is missing.
```

Branch-local expansion:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
is absent.

LawfulLocalTzSEvmqxu48FrameExtractor_V1.source_byte_object
is absent.

KeatingRevealed_ShiabProjectionSheet_V1
is absent.
```

Since the source object is absent, the checksum/custody field, decode/output
manifest, and formula-visibility scope cannot be satisfied downstream.

## 5. Constructive Next Object

The constructive next object is:

```text
FormulaBearingPTUJOrKeatingSourceAsset_V1.accepted_branch_payload
```

It can close through exactly one branch:

| branch | payload needed |
|---|---|
| Official/custodian PTUJ | official source asset record, immutable locator/path, content access, custody or checksum, declared formula-visibility scope, and no-target-import guard |
| Lawful-local PTUJ | lawful acquisition basis, source bytes/source package, source-byte checksum, acquisition tool identity, decoder identity, decode scope, output manifest, output checksums, formula-visibility scope, and no-target-import guard |
| Keating sheet | sheet scan/photo/source package, custody or checksum, visible formula/rule transcription scope, and link to the missing-sheet locator |

Any one branch must be internally complete. It cannot borrow formula visibility
from the manuscript, custody from the PTUJ page, and identity from Oxford.

## 6. What This Means For The Relevant GU Claim

ProductAB remains locked at the source-provenance layer:

```text
visible_formula_transcription_allowed: false
productab_member_emitted: false
binding_gate_allowed: false
K_IG_restart_allowed_from_this_route: false
```

No GU claim is promoted or downgraded. The result only says that the current
repo-local source/media corpus does not contain the formula-bearing PTUJ or
Keating proof object required to proceed.

## 7. Next Meaningful Proof Or Computation Step

The next meaningful step is acquisition-plus-verification, not representation
theory:

1. Acquire either an official/custodian PTUJ source asset package, a lawful-local
   `TzSEvmqxu48` source-byte object with decoder output, or the Keating sheet
   scan/photo/source package.
2. Record immutable locator/path, custody basis, SHA-256 or equivalent checksum,
   and acquisition/decode command versions where applicable.
3. Produce a bounded formula-visibility scope: timestamps/frames/pages, output
   paths, output checksums, and uncertainty marks.
4. Only then run visible formula transcription and the ProductAB
   frame/manuscript/Oxford identity test.

If a complete lawful pass yields no legible formula/projection rule, the correct
result is a scoped PTUJ/Keating visual-route negative.

## 8. Terrain Classification

Suspected terrain:

```text
provenance-verifier, with downstream spectral-phase and descent-quotient only
after a source witness exists
```

Forbidden shortcut:

```text
Do not treat PTUJ captions, oEmbed metadata, thumbnails, manuscript formulas,
Oxford stills, finite Product A/B host rows, alpha/beta behavior, chirality,
generation count, anomaly behavior, dark-energy behavior, or K_IG rescue value
as the missing formula-bearing PTUJ/Keating asset.
```

First invariant to test:

```text
one branch-pure accepted payload with source bytes or content access, checksum
or custody, decode/output manifest if local, and bounded visible-formula scope
before any member selection
```

Kill condition:

```text
Reject the route if a complete branch-pure acquisition/decode pass exposes no
legible formula/projection rule, or if the proposed member is selected from
target ProductAB behavior rather than visible source content.
```

## 9. Certificate/Witness Shape

| field | required content |
|---|---|
| public inputs | selected branch id, source id, stable locator/path, acquisition basis, checksum/custody record, decoder identity if local |
| witness | source bytes/stills/sheet, decoded output manifest, output checksums, bounded frame/page/time scope, visible transcription with uncertainty marks |
| verifier predicate | branch purity, checksum/custody match, decode reproducibility, formula visibility, transcription boundedness, no cross-branch assembly |
| semantic lift | permission to run PTUJ/Keating visible-formula transcription and then ProductAB member/identity tests |
| anti-smuggling guard | verifier must fail if member selection depends on target ProductAB row action, alpha/beta coefficients, chirality, anomaly, generation count, dark-energy behavior, or K_IG usefulness |

## 10. JSON Summary

```json
{
  "artifact_id": "FormulaBearingPTUJOrKeatingSourceAssetGate_1003_C1_L4_V1",
  "run_id": "hourly-20260626-1003",
  "cycle": 1,
  "lane": 4,
  "artifact_path": "explorations/hourly-20260626-1003-cycle1-productab-formula-bearing-source-asset-gate.md",
  "verdict": "blocked",
  "formula_bearing_source_asset_present": false,
  "content_access_or_source_bytes_present": false,
  "checksum_or_custody_present": false,
  "decode_output_manifest_present": false,
  "formula_visibility_scope_present": false,
  "visible_formula_transcription_allowed": false,
  "productab_member_emitted": false,
  "target_import_used": false,
  "claim_status_change": false,
  "first_exact_obstruction": "FormulaBearingPTUJOrKeatingSourceAsset_V1.content_access_or_source_bytes_missing",
  "constructive_next_object": "FormulaBearingPTUJOrKeatingSourceAsset_V1.accepted_branch_payload",
  "terrain": [
    "provenance-verifier",
    "spectral-phase_after_source_witness",
    "descent-quotient_after_source_witness"
  ],
  "strongest_positive_result": "route_identity_metadata_and_missing_sheet_locator_only",
  "claim_status_consistency_triggered": false
}
```

