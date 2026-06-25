---
title: "Hourly 20260625 0601 Cycle 2 QFT Alternate Primary Source Requirement Gate"
date: "2026-06-25"
run: "hourly-20260625-0601"
cycle: 2
lane: 4
doc_type: qft_alternate_primary_source_requirement_gate
artifact_id: "QFTAlternatePrimarySourceRequirementGate_V1"
verdict: "BLOCKED_SCOPED_NEGATIVE_NOT_GLOBAL_DEMOTION"
owned_path: "explorations/hourly-20260625-0601-cycle2-qft-alternate-primary-source-requirement-gate.md"
companion_audit: "tests/hourly_20260625_0601_cycle2_qft_alternate_primary_source_requirement_gate_audit.py"
---

# Hourly 20260625 0601 Cycle 2 QFT Alternate Primary Source Requirement Gate

## 1. Verdict

Verdict: **blocked; manuscript-scoped negative cannot trigger global QFT
demotion**.

The acquired 2021 author manuscript page-window result over PDF pages 54-60 is
a valid local blocker for using that page window as the source receipt for

```text
P_fin^b: F_phys^b(O) -> K_b
```

It is not a global no-go theorem for GU QFT finite-projector routes. It does
not demote alternate primary-source routes, transcript routes, corrected
manuscript routes, audio/video-derived transcript routes, or future acquired
source versions.

Decision:

```text
artifact_id: QFTAlternatePrimarySourceRequirementGate_V1
required_object: P_fin^b: F_phys^b(O) -> K_b
accepted_receipt_count: 0
proof_restart_allowed: false
manuscript_page_window_negative_scope: acquired_2021_author_manuscript_pdf_pages_54_60_only
global_qft_demotion_allowed: false
global_no_go_allowed: false
status: blocked_scoped_negative_requires_alternate_primary_source_or_global_negative_bundle
```

Before any QFT finite-projector route is globally demoted, the repo needs one
of two objects:

```text
AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1
```

that either emits an accepted `P_fin^b` receipt from another primary GU source,
or

```text
GlobalNegativeReceiptBundle_V1
```

covering every declared primary GU source surface and known source version for
the QFT finite projector object.

## 2. Source Facts Read Directly

`RESEARCH-POSTURE.md` requires constructive reconstruction pressure while
forbidding verdict inflation, compatibility treated as derivation, target-data
import, and process discipline treated as physics evidence.

`process/runbooks/five-lane-frontier-run.md` requires each lane to produce a
decision-grade artifact with a verdict, strongest positive route, exact
obstruction, impact, falsification condition, and next meaningful computation.

`AuthorManuscriptQFTFiniteProjectorReceiptGate_V1` established the acquired
manuscript object and exact QFT required object:

```text
source_id: GU-MEDIA-2021-DRAFT-RELEASE
manuscript_object_id: AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE
sha256: 3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4
required_object: P_fin^b: F_phys^b(O) -> K_b
accepted_receipt_count: 0
proof_restart_allowed: false
```

That gate found no accepted manuscript receipt for exact or equivalent
source-side objects:

- `P_fin^b`;
- `F_phys^b(O)`;
- `K_b`;
- finite source extraction projector;
- local representative map into `K_b`;
- finite physical-field-to-source-mode extraction map;
- source-side finite QFT projector rule.

`AuthorManuscriptQFTFiniteProjectorLocatorRow_V1` refined the negative to the
manual page-window pass over PDF pages 54-60. It rejected the strongest local
positive cluster: p. 54 finite/infinite dimension language, p. 55 projection
and reduced Euler-Lagrange language, pp. 56-58 field/Lagrangian/Dirac material,
and p. 60 QFT dictionary and non-chiral Dirac material. Those locators are
QFT-adjacent, but none emits the domain, target, and map required for
`P_fin^b: F_phys^b(O) -> K_b`.

`NegativeReceiptScopeValidityGate_V1` already fixed the controlling scope rule:
the QFT manuscript result is a valid scoped negative receipt for the acquired
2021 manuscript surface, but it is not a global GU absence claim and it does
not authorize proof restart or global demotion.

## 3. Strongest Positive Route Still Alive

The strongest positive route still alive is the alternate-primary-source route,
not the inspected page-window route.

Minimum positive bundle:

```text
AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1
```

Required contents:

| field | requirement |
|---|---|
| `bundle_id` | stable bundle identifier |
| `family` | `QFT` |
| `required_object` | `P_fin^b: F_phys^b(O) -> K_b` |
| `primary_source_surfaces` | complete declared source scopes, not outline-only or metadata-only surfaces |
| `source_ids` | exact primary GU source ids, versions, archive ids, hashes, or capture dates |
| `query_log` | exact tokens plus notation variants and source-side paraphrases |
| `inspected_hits` | accepted, quarantined, rejected, or scoped-negative rows with reasons |
| `accepted_receipts` | zero or more `PrimarySourceReceiptInstance_V1` rows |
| `import_screen` | explicit exclusion of standard QFT basis, target-fit Bell/Pauli data, identity Gram controls, and non-source substitutions |
| `proof_restart_policy` | `allowed` only if an accepted receipt emits the domain, target, and map |

An accepted alternate positive receipt must emit all of:

```text
domain: F_phys^b(O) or source-equivalent physical-field quotient
target: K_b or source-equivalent finite carrier
map: P_fin^b or source-equivalent finite extraction/projector/local representative rule
source_provenance: primary GU source surface
local_mode_payload: enough typed information to begin SourceModeQuotientPacket(K_b)
```

Live candidate surfaces include complete primary transcripts, official or
archived video/audio-derived transcripts with checked segment scopes, corrected
or alternate author manuscript versions, and other primary GU source releases.
No such alternate bundle is accepted in this artifact.

## 4. First Exact Obstruction/Missing Object

The first exact obstruction is:

```text
AcceptedPrimarySourceReceiptForQFTPFinB
```

Required emission:

```text
P_fin^b: F_phys^b(O) -> K_b
```

or a source-equivalent finite projector/local representative rule specifying:

1. a physical-field domain equivalent to `F_phys^b(O)`;
2. a finite target carrier equivalent to `K_b`;
3. a map, projection, extraction, or local representative rule from the domain
   to the target;
4. primary GU source provenance for the rule;
5. enough local mode information to begin `SourceModeQuotientPacket(K_b)`.

The manuscript p. 54-60 negative only closes one attempted source surface. The
first missing object for global demotion is larger:

```text
GlobalNegativeReceiptBundle_V1
```

Minimum global-negative fields:

| field | requirement |
|---|---|
| `family` | `QFT` |
| `required_object` | `P_fin^b: F_phys^b(O) -> K_b` |
| `covered_primary_source_surfaces` | all declared primary GU source surfaces and known source versions |
| `excluded_surfaces` | explicit exclusions with reasons; exclusions prevent global demotion |
| `query_log_by_surface` | exact tokens, notation variants, source paraphrases, and inspected hits |
| `negative_decision_by_surface` | valid scoped negative, accepted positive, quarantined, blocked, or rejected |
| `variant_coverage` | `P_fin`, `F_phys`, `K_b`, projector, projection, extraction, local representative, finite mode, source-mode, and notation variants |
| `target_import_screen` | confirms no standard QFT object is imported as source evidence |
| `global_negative_decision` | allowed only if every primary surface is acquired, declared, queried, and negative |

This bundle is missing.

## 5. Impact if Closed

If an alternate primary-source bundle emits an accepted `P_fin^b` receipt, the
QFT branch can restart only at the next source-side proof object:

```text
AcceptedPrimarySourceReceiptForQFTPFinB
  -> SourceModeQuotientPacket(K_b)
  -> H_raw and removed EOM/Gauge/Constraint/Ghost/Null representatives
  -> Q_b
  -> H_phys = Q_b^* H_raw Q_b
  -> possible finite one-particle seed
```

This would not by itself promote finite QFT, covariance, Alice/Bob splitting,
`rho_AB`, Bell/CHSH, or a physical recovery claim.

If a `GlobalNegativeReceiptBundle_V1` closes with no accepted receipts across
all primary GU surfaces and source versions, then QFT finite-projector routes
depending on a source-derived `P_fin^b` should be demoted from live to globally
blocked at the source-receipt layer. That would still be a source-receipt
demotion, not a mathematical proof that no stronger future reformulation of GU
could exist.

Current impact:

```text
accepted_receipt_count: 0
proof_restart_allowed: false
global_qft_demotion_allowed: false
manuscript_scoped_negative_valid: true
alternate_primary_source_route_alive: true
```

## 6. Falsification/Demotion Condition

Falsification of the manuscript-window negative occurs if a corrected extraction
or manual reading of PDF pages 54-60 emits the required domain, target, and map.

Falsification of the broader manuscript negative occurs if another page, table,
diagram cell, equation, appendix, or notation variant in the same acquired
manuscript object emits:

```text
P_fin^b: F_phys^b(O) -> K_b
```

or an equivalent finite source extraction/local representative rule.

Positive restart condition:

```text
An AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1 contains at least
one accepted PrimarySourceReceiptInstance_V1 for P_fin^b with domain, target,
map, primary-source provenance, import screen, and local-mode payload.
```

Global demotion condition:

```text
GlobalNegativeReceiptBundle_V1 covers every primary GU source surface and known
source version for QFT P_fin^b, preserves query and variant logs for each,
inspects every hit, excludes target import, and emits zero accepted receipts.
```

Until that global bundle exists, the p. 54-60 scoped negative cannot be used as
a global no-go or global demotion.

## 7. Next Meaningful Source/Proof Computation

Next source computation:

```text
QFTAlternatePrimarySourceQueryBundle_V1
```

Run order:

1. declare candidate primary GU source surfaces and versions;
2. acquire complete local source objects or cite stable archive ids/hashes;
3. preserve exact query terms, notation variants, and source-side paraphrases;
4. inspect candidate hits for domain, target, and map;
5. emit accepted, quarantined, rejected, or scoped-negative rows;
6. update the alternate bundle and only then decide whether proof restart or
   source-route demotion is allowed.

Next proof computation if a positive receipt appears:

```text
SourceModeQuotientPacket(K_b)
```

No proof computation should run before the source receipt exists.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "QFTAlternatePrimarySourceRequirementGate_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0601",
  "cycle": 2,
  "lane": 4,
  "verdict": "BLOCKED_SCOPED_NEGATIVE_NOT_GLOBAL_DEMOTION",
  "status": "blocked_scoped_negative_requires_alternate_primary_source_or_global_negative_bundle",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0601-cycle2-qft-alternate-primary-source-requirement-gate.md",
    "companion_audit": "tests/hourly_20260625_0601_cycle2_qft_alternate_primary_source_requirement_gate_audit.py",
    "artifact_id": "QFTAlternatePrimarySourceRequirementGate_V1"
  },
  "required_object": "P_fin^b: F_phys^b(O) -> K_b",
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "source_facts_read_directly": {
    "research_posture": "constructive reconstruction pressure with no verdict inflation, compatibility-as-derivation, target import, or process-as-physics evidence",
    "five_lane_runbook": "decision-grade artifact with verdict, positive route, exact obstruction, impact, falsification condition, and next computation",
    "receipt_gate": "AuthorManuscriptQFTFiniteProjectorReceiptGate_V1 found zero accepted receipts for P_fin^b in the acquired 2021 author manuscript",
    "locator_row": "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1 found no accepted projector row in PDF pages 54-60",
    "scope_gate": "NegativeReceiptScopeValidityGate_V1 classifies the QFT manuscript negative as manuscript-scoped only"
  },
  "manuscript_scoped_negative": {
    "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
    "manuscript_object_id": "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
    "sha256": "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
    "page_window": "PDF pages 54-60",
    "valid_scoped_negative": true,
    "global_no_go_allowed": false,
    "global_demotion_allowed": false,
    "scoped_negative_not_global_no_go": true
  },
  "strongest_positive_route_still_alive": {
    "id": "AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1",
    "status": "alive_but_not_instantiated",
    "accepted_receipt_required": true,
    "candidate_surfaces": [
      "complete_primary_transcripts",
      "official_or_archived_video_audio_derived_transcripts",
      "corrected_or_alternate_author_manuscript_versions",
      "other_primary_GU_source_releases"
    ],
    "accepted_receipt_must_emit": {
      "domain": "F_phys^b(O) or source-equivalent physical-field quotient",
      "target": "K_b or source-equivalent finite carrier",
      "map": "P_fin^b or source-equivalent finite extraction/projector/local representative rule",
      "source_provenance": "primary GU source surface",
      "local_mode_payload": "enough typed information to begin SourceModeQuotientPacket(K_b)"
    }
  },
  "first_exact_obstruction": {
    "id": "AcceptedPrimarySourceReceiptForQFTPFinB",
    "missing": true,
    "required_object": "P_fin^b: F_phys^b(O) -> K_b",
    "missing_components": [
      "physical-field domain equivalent to F_phys^b(O)",
      "finite target carrier equivalent to K_b",
      "map/projection/extraction/local representative rule",
      "primary GU source provenance",
      "local mode information for SourceModeQuotientPacket(K_b)"
    ]
  },
  "alternate_primary_source_bundle_required": {
    "id": "AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1",
    "required_before_positive_restart": true,
    "required_fields": [
      "bundle_id",
      "family",
      "required_object",
      "primary_source_surfaces",
      "source_ids",
      "query_log",
      "inspected_hits",
      "accepted_receipts",
      "import_screen",
      "proof_restart_policy"
    ]
  },
  "global_negative_bundle_required_before_global_demotion": {
    "id": "GlobalNegativeReceiptBundle_V1",
    "missing": true,
    "required_before_qft_finite_projector_routes_demoted": true,
    "required_fields": [
      "family",
      "required_object",
      "covered_primary_source_surfaces",
      "excluded_surfaces",
      "query_log_by_surface",
      "negative_decision_by_surface",
      "variant_coverage",
      "target_import_screen",
      "global_negative_decision"
    ],
    "must_cover": "all primary GU source surfaces and known source versions for QFT P_fin^b",
    "accepted_receipt_count_required_for_global_negative": 0
  },
  "impact_if_closed": {
    "if_positive_alternate_receipt": "restart only at SourceModeQuotientPacket(K_b), not at downstream physics claims",
    "if_global_negative_bundle_closes": "demote source-derived QFT finite-projector routes to globally blocked at the source-receipt layer",
    "current_global_qft_demotion_allowed": false,
    "current_alternate_primary_source_route_alive": true
  },
  "falsification_and_demotion_conditions": {
    "manuscript_window_negative_falsified_by": "corrected extraction or manual reading of PDF pages 54-60 emits P_fin^b or equivalent finite source extraction/local representative rule",
    "positive_restart_condition": "AlternatePrimarySourceQFTFiniteProjectorReceiptBundle_V1 contains at least one accepted PrimarySourceReceiptInstance_V1 for P_fin^b",
    "global_demotion_condition": "GlobalNegativeReceiptBundle_V1 covers every primary GU source surface and known source version, preserves query and variant logs, inspects all hits, excludes target import, and emits zero accepted receipts"
  },
  "next_meaningful_source_or_proof_computation": {
    "source_computation": "QFTAlternatePrimarySourceQueryBundle_V1",
    "proof_computation_if_positive_receipt": "SourceModeQuotientPacket(K_b)",
    "proof_restart_currently_allowed": false,
    "steps": [
      "declare candidate primary GU source surfaces and versions",
      "acquire complete local source objects or stable archive ids/hashes",
      "preserve exact query terms, notation variants, and source-side paraphrases",
      "inspect candidate hits for domain, target, and map",
      "emit accepted, quarantined, rejected, or scoped-negative rows",
      "update alternate bundle before deciding restart or demotion"
    ]
  }
}
```
