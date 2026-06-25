---
title: "Hourly 20260625 0203 Cycle 3 Author Manuscript Acquisition Row"
date: "2026-06-25"
run: "hourly-20260625-0203"
cycle: 3
lane: 4
doc_type: author_manuscript_acquisition_row
artifact_id: "AuthorManuscriptAcquisitionRow_V1"
verdict: "BLOCKED_MANUSCRIPT_NOT_ACQUIRED_RELEASE_PAGE_NOT_RECEIPT"
owned_path: "explorations/hourly-20260625-0203-cycle3-author-manuscript-acquisition-row.md"
companion_audit: "tests/hourly_20260625_0203_cycle3_author_manuscript_acquisition_row_audit.py"
---

# Hourly 20260625 0203 Cycle 3 Author Manuscript Acquisition Row

## 1. Verdict

Verdict: **blocked**.

This artifact instantiates:

```text
AuthorManuscriptAcquisitionRow_V1
```

for:

```text
GU-MEDIA-2021-DRAFT-RELEASE
```

Decision:

```text
author_manuscript_acquired_now: false
release_page_accepted_as_receipt: false
manuscript_receipt_rows_evaluable_now: false
proof_restart_allowed: false
claim_promotion_allowed: false
```

The official release page is a chronology and pointer surface. It is not the
2021 author manuscript/draft, does not supply manuscript page, section,
equation, paragraph, or derivation-cell locators, and cannot emit IG, RS, QFT,
or DGU/VZ receipt rows.

The exact object that must exist before manuscript receipt rows can be evaluated
is an acquired 2021 GU author manuscript/draft object, represented locally or by
a stable archive record, with provenance, checksum or archive id, locator
discipline, and a family query log.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` supplies the controlling discipline: the repository may
pursue GU constructively, but it must not promote compatibility, chronology,
metadata, or process discipline into derivation evidence.

`process/runbooks/five-lane-frontier-run.md` supplies the lane contract:
produce a decision-grade object, state the first exact obstruction, avoid
overlap with other workers, and use the verdict vocabulary.

`AuthorManuscriptReceiptAvailabilityPacket_V1` establishes that
`GU-MEDIA-2021-DRAFT-RELEASE` is indexed, but no local or indexed author
manuscript/draft receipt exists. It also establishes that the release page can
be used for official chronology and as a pointer only.

`TranscriptManuscriptAcquisitionQueue_V1` ranks the 2021 manuscript/draft
acquisition as the first manuscript gate and says mining waits until the draft
is acquired and checksummed or archived.

`RepoLocalPrimaryGUSourceReceiptMap_V1` records the process map and zero
accepted receipts. Its author-draft rows remain `missing_manuscript` for all
four families and block proof restart.

`NegativeReceiptQuarantinePolicy_V1` forbids treating absence from a release
page as absence from an unacquired manuscript. A negative receipt requires a
complete acquired source surface plus declared scope and query log.

`sources/media-index.md` gives the source id, date, and official page pointer:
`GU-MEDIA-2021-DRAFT-RELEASE`, 2021-04-01, "Geometric Unity author's working
draft release", status `metadata-checked`, use for chronology, and "use the
draft itself for claim extraction."

## 3. Acquisition Row Schema

`AuthorManuscriptAcquisitionRow_V1` is an acquisition gate, not a receipt row.
It records whether the manuscript object exists in a form strong enough to
permit later receipt evaluation.

Required fields:

| field | requirement |
|---|---|
| `artifact` | `AuthorManuscriptAcquisitionRow_V1` |
| `source_id` | Stable source id from `sources/media-index.md`. |
| `current_state` | One of `not_acquired`, `acquired_pending_query`, `queried_no_receipt`, or `receipt_candidates_ready`. |
| `required_provenance` | Must include acquisition origin, acquisition date, `local_or_archive_path`, `checksum_or_archive_id`, custodian or archive basis, and access notes. |
| `acceptable_local_archive_evidence` | A local file path under repo-controlled source storage or a stable archive identifier with enough metadata to re-fetch or verify the same object. |
| `checksum_archive_requirement` | SHA-256 or equivalent content checksum for local files, or immutable archive id for an archive object. |
| `locator_requirements` | Page, section, equation, paragraph, or derivation-cell locators tied to the acquired manuscript object. |
| `family_query_plan_after_acquisition` | Family-specific search plan for IG, RS, QFT, and DGU/VZ, run only after acquisition. |
| `release_page_accepted_as_receipt` | Always false unless the release page itself contains the manuscript text and exact locators; current row is false. |
| `proof_restart_allowed` | False until a later receipt row is accepted and passes family identity checking. |
| `claim_promotion_allowed` | False at this gate. |
| `restart_policy` | Acquire, verify, locate, query, instantiate receipt candidates, apply intake, then perform family identity check before proof restart. |

This row can move from `not_acquired` to `acquired_pending_query` only after the
manuscript object is captured with provenance and checksum/archive evidence.
It can move to `receipt_candidates_ready` only after the family query plan
produces exact candidate locators from that acquired object.

## 4. Current Row for GU-MEDIA-2021-DRAFT-RELEASE

| field | value |
|---|---|
| `source_id` | `GU-MEDIA-2021-DRAFT-RELEASE` |
| `current_state` | `not_acquired` |
| `source_surface_available_now` | official release page metadata and chronology pointer |
| `author_manuscript_acquired` | `false` |
| `release_page_accepted_as_receipt` | `false` |
| `release_page_allowed_use` | chronology and acquisition pointer only |
| `required_provenance` | acquisition origin, acquisition date, `local_or_archive_path`, `checksum_or_archive_id`, custodian/archive basis, access notes |
| `acceptable_local_archive_evidence` | local manuscript path with checksum, or stable archive record with archive id and retrieval metadata |
| `locator_requirements` | page, section, equation, paragraph, or derivation-cell locators from the acquired manuscript itself |
| `family_query_plan_required` | yes, after acquisition only |
| `proof_restart_allowed` | `false` |
| `claim_promotion_allowed` | `false` |
| `first_missing_object` | acquired 2021 GU author manuscript/draft object with provenance and checksum/archive id |

No manuscript receipt row can be evaluated from the release page alone. The
release page can justify opening this acquisition row and can help identify the
target object. It cannot instantiate a formula, action, operator, selector,
projector, derivation-cell, negative receipt, or family proof restart.

## 5. Post-Acquisition Family Query Plan

After the manuscript object is acquired and verified, run a family query pass
against the acquired manuscript text and any attached displayed formulas.

| family | required object focus | query targets |
|---|---|---|
| IG | `SourceForcedCodomainSelectorForK_IG` | codomain selector, witness category, Shiab, projection selector, parent-action selector, eliminator, `K_IG`, observerse, `U^14` |
| RS | `source.action_or_operator for d_RS,-1` | action, operator, Noether identity, BRST rule, gauge variation, source complex, Rarita-Schwinger, `d_RS,-1` |
| QFT | `P_fin^b: F_phys^b(O) -> K_b` | finite extraction, projector, local representative, source mode, quantization, `P_fin`, `F_phys`, `K_b` |
| DGU_VZ | `operator_source_primary_action_or_EL for D_GU^epsilon 0/1` | primary action, operator, Euler-Lagrange equation, principal symbol, projectors, coefficients, first-order terms, `D_GU`, `epsilon`, VZ |

Each hit must produce:

```text
source_id
manuscript_object_id
local_or_archive_path
checksum_or_archive_id
exact locator
short exact fragment or formula reference
emitted object type
emitted formula or rule
representation context
import controls
receipt candidate status
```

Checked absences require the negative-receipt policy: complete declared scope,
preserved query log, notation variants, inspected hits, false-positive
decisions, and `promotion_allowed = false`.

## 6. Strongest Positive Result

The strongest positive result is a precise acquisition gate:

```text
GU-MEDIA-2021-DRAFT-RELEASE has a stable source id and official chronology,
but the author manuscript/draft object is not acquired.
```

This is useful because it prevents three errors at once:

- treating the release page as manuscript content;
- treating non-acquisition as a negative receipt;
- restarting family proof work before a manuscript object, locator, and family
  identity check exist.

## 7. First Exact Obstruction

The first exact obstruction is:

```text
AcquiredAuthorManuscriptObject_V1 for GU-MEDIA-2021-DRAFT-RELEASE
```

with:

```text
local_or_archive_path
checksum_or_archive_id
provenance record
locator basis
family query log after acquisition
```

Until that object exists, the repo cannot evaluate whether the manuscript emits
the IG selector, RS action/operator, QFT finite projector, or DGU/VZ actual
operator/action/EL object. This obstruction is upstream of all family
mathematical identity checks.

## 8. GU Claim Impact and Forbidden Promotions

No GU claim is promoted.

Allowed statement:

```text
The repo has an acquisition row for the 2021 GU author manuscript/draft release,
but the manuscript is not acquired and the release page is not a receipt.
```

Forbidden promotions:

```text
IG selects K_IG.
RS source-derived d_RS,-1 is established.
QFT P_fin^b is supplied.
DGU/VZ actual D_GU^epsilon 0/1 is identified.
The 2021 author manuscript contains any required object.
The release page is a manuscript receipt.
The release page is a negative receipt for manuscript content.
Any manuscript receipt row is evaluable before local_or_archive_path and
checksum_or_archive_id exist.
Family proof restart is allowed from acquisition metadata.
VZ evasion, dark-energy recovery, FLRW recovery, finite-QFT recovery, rank or
generation readout, CHSH, or Bell recovery is derived.
```

Restart policy:

```text
proof_restart_allowed = false
```

Restart can be reconsidered only after:

1. The manuscript object is acquired and verified.
2. Exact manuscript locators are mined.
3. Candidate receipt rows are instantiated from those locators.
4. `PrimarySourceReceiptIntakeProtocol_V1` accepts a candidate for routing.
5. The candidate passes family mathematical identity checking.

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "AuthorManuscriptAcquisitionRow_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0203",
  "cycle": 3,
  "lane": 4,
  "verdict": "BLOCKED_MANUSCRIPT_NOT_ACQUIRED_RELEASE_PAGE_NOT_RECEIPT",
  "verdict_class": "blocked",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0203-cycle3-author-manuscript-acquisition-row.md",
    "companion_audit": "tests/hourly_20260625_0203_cycle3_author_manuscript_acquisition_row_audit.py",
    "row_id": "AuthorManuscriptAcquisitionRow_V1:GU-MEDIA-2021-DRAFT-RELEASE"
  },
  "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
  "source_surface": {
    "indexed_in": "sources/media-index.md",
    "date": "2021-04-01",
    "status": "metadata-checked",
    "available_now": "official_release_page_chronology_pointer",
    "release_page_accepted_as_receipt": false,
    "release_page_allowed_use": "chronology_and_acquisition_pointer_only"
  },
  "current_row": {
    "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
    "current_state": "not_acquired",
    "author_manuscript_acquired": false,
    "manuscript_receipt_rows_evaluable": false,
    "release_page_accepted_as_receipt": false,
    "required_before_receipt_rows_can_be_evaluated": "AcquiredAuthorManuscriptObject_V1 with local_or_archive_path checksum_or_archive_id provenance locator basis and family query log",
    "proof_restart_allowed": false,
    "claim_promotion_allowed": false
  },
  "acquisition_row_schema": {
    "required_fields": [
      "artifact",
      "source_id",
      "current_state",
      "required_provenance",
      "acceptable_local_archive_evidence",
      "checksum_archive_requirement",
      "locator_requirements",
      "family_query_plan_after_acquisition",
      "release_page_accepted_as_receipt",
      "proof_restart_allowed",
      "claim_promotion_allowed",
      "restart_policy"
    ],
    "current_state_vocabulary": [
      "not_acquired",
      "acquired_pending_query",
      "queried_no_receipt",
      "receipt_candidates_ready"
    ]
  },
  "required_provenance": [
    "acquisition_origin",
    "acquisition_date",
    "local_or_archive_path",
    "checksum_or_archive_id",
    "custodian_or_archive_basis",
    "access_notes"
  ],
  "acceptable_local_archive_evidence": [
    "repo_local_manuscript_file_with_sha256_checksum",
    "stable_archive_record_with_archive_id_and_retrieval_metadata"
  ],
  "checksum_archive_requirement": {
    "local_file": "sha256_or_equivalent_content_checksum_required",
    "archive_object": "immutable_archive_id_required",
    "release_page_link_only_satisfies_requirement": false
  },
  "locator_requirements": [
    "page_locator",
    "section_locator",
    "equation_locator",
    "paragraph_locator",
    "derivation_cell_locator"
  ],
  "family_query_plan_after_acquisition": {
    "IG": {
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "query_targets": [
        "codomain selector",
        "witness category",
        "Shiab",
        "projection selector",
        "parent-action selector",
        "eliminator",
        "K_IG",
        "observerse",
        "U^14"
      ]
    },
    "RS": {
      "required_object": "source.action_or_operator for d_RS,-1",
      "query_targets": [
        "action",
        "operator",
        "Noether identity",
        "BRST rule",
        "gauge variation",
        "source complex",
        "Rarita-Schwinger",
        "d_RS,-1"
      ]
    },
    "QFT": {
      "required_object": "P_fin^b: F_phys^b(O) -> K_b",
      "query_targets": [
        "finite extraction",
        "projector",
        "local representative",
        "source mode",
        "quantization",
        "P_fin",
        "F_phys",
        "K_b"
      ]
    },
    "DGU_VZ": {
      "required_object": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
      "query_targets": [
        "primary action",
        "operator",
        "Euler-Lagrange equation",
        "principal symbol",
        "projectors",
        "coefficients",
        "first-order terms",
        "D_GU",
        "epsilon",
        "VZ"
      ]
    }
  },
  "strongest_positive_result": "stable source id and official chronology exist for future acquisition, while manuscript content remains unacquired",
  "first_exact_obstruction": {
    "id": "AcquiredAuthorManuscriptObject_V1",
    "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
    "missing": true,
    "required_fields": [
      "local_or_archive_path",
      "checksum_or_archive_id",
      "provenance_record",
      "locator_basis",
      "family_query_log_after_acquisition"
    ]
  },
  "restart_policy": {
    "proof_restart_allowed": false,
    "steps_before_restart": [
      "acquire_and_verify_manuscript_object",
      "mine_exact_manuscript_locators",
      "instantiate_candidate_receipt_rows",
      "apply_PrimarySourceReceiptIntakeProtocol_V1",
      "perform_family_mathematical_identity_check"
    ]
  },
  "no_claim_promotions": {
    "claim_promotion_allowed": false,
    "IG_K_IG_selected": false,
    "RS_d_RS_minus_1_source_derived": false,
    "QFT_P_fin_b_supplied": false,
    "DGU_actual_operator_identified": false,
    "author_manuscript_contains_required_object": false,
    "release_page_is_manuscript_receipt": false,
    "release_page_is_negative_receipt_for_manuscript": false,
    "manuscript_receipt_rows_evaluable_before_provenance_and_checksum": false,
    "family_proof_restart_from_acquisition_metadata": false,
    "VZ_dark_energy_FLRW_QFT_rank_generation_CHSH_Bell_recovered": false
  },
  "forbidden_promotions": [
    "IG selects K_IG",
    "RS source-derived d_RS,-1 is established",
    "QFT P_fin^b is supplied",
    "DGU/VZ actual D_GU^epsilon 0/1 is identified",
    "the 2021 author manuscript contains any required object",
    "release page accepted as manuscript receipt",
    "release page accepted as negative receipt for manuscript content",
    "manuscript receipt rows evaluated before local_or_archive_path and checksum_or_archive_id exist",
    "family proof restart from acquisition metadata",
    "VZ dark-energy FLRW finite-QFT rank generation CHSH or Bell recovery is derived"
  ]
}
```
