---
title: "Hourly 20260625 0203 Cycle 2 Negative Receipt and Quarantine Policy"
date: "2026-06-25"
run: "hourly-20260625-0203"
cycle: "2"
lane: "4"
doc_type: negative_receipt_quarantine_policy
artifact_id: "NegativeReceiptQuarantinePolicy_V1"
verdict: "CONDITIONAL_POLICY_READY_NEGATIVE_RECEIPTS_REQUIRE_COMPLETE_SURFACE"
owned_path: "explorations/hourly-20260625-0203-cycle2-negative-receipt-quarantine-policy.md"
companion_audit: "tests/hourly_20260625_0203_cycle2_negative_receipt_quarantine_policy_audit.py"
---

# Hourly 20260625 0203 Cycle 2 Negative Receipt and Quarantine Policy

## 1. Verdict

Verdict: **conditional**.

This artifact closes a process-policy gap left after cycle 1. Absence of a
family object in a mined source may become an explicit `negative_receipt` only
when the searched source surface is complete for the stated scope and the query
log is preserved. If the transcript, manuscript, Portal-only material, video
frames, generated transcript basis, or exact locator set is incomplete, the
correct status is `missing`, `quarantined`, or `rejected`, not
`negative_receipt`.

The policy decision is:

```text
negative_receipt = complete acquired source surface + declared source scope +
family-specific query log + exact absence result + no target-import use +
promotion_allowed false
```

The policy does not assert that any current cycle 1 row is already a negative
receipt. It defines when a future source-mining row can be promoted from missing
or quarantined absence into an auditable negative control.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` supplies the governing constraint: source process is not
physics evidence, compatibility is not derivation, and target data cannot be
hidden inside a reconstruction. Therefore a negative receipt is only a
provenance and routing object. It cannot demote or promote a mathematical claim
by itself.

`process/runbooks/five-lane-frontier-run.md` supplies the verdict vocabulary and
the rule that a lane must identify the first exact obstruction and avoid
overlap. This policy uses that vocabulary for receipt status, not for proof
status.

`PrimarySourceReceiptIntakeProtocol_V1` supplies the positive receipt schema:
exact source kind, source id, locator, exact fragment, emitted object type,
emitted formula or rule, representation context, import controls, acceptance
status, and `promotion_allowed = false`. This policy adds the parallel negative
case: exact searched scope, query log, and explicit absence are required before
absence can be recorded as a receipt.

Cycle 1 source packets supply the observed surfaces:

| cycle 1 packet | direct policy derivation |
|---|---|
| `OxfordPortalReceiptMiningPacket_V1` | Oxford/Portal is an official source surface, but Portal-only preface/post-lecture material is not locally mined; current rows remain quarantined, not negative receipts. |
| `UCSDTranscriptReceiptMiningPacket_V1` | UCSD is a local raw transcript with timestamped locators; it can support quarantined or missing rows now and could support a negative receipt only for a declared query scope over the complete local transcript or a complete acquired component. |
| `JRETranscriptReceiptMiningPacket_V1` | JRE #1453 and #1628 are indexed transcript surfaces, but transcript text is not repo-local; their absences are `missing`, not negative receipts. |
| `KeatingTOEModernReceiptMiningPacket_V1` | Outline-only rows, metadata-only rows, visible generated transcript excerpts, and DESI-facing summaries are locator candidates only; they cannot become accepted receipts or negative receipts. |
| `AuthorManuscriptReceiptAvailabilityPacket_V1` | The 2021 draft-release page is official chronology and a pointer to an unacquired manuscript; absence of formulas on the release page is not absence in the manuscript. |

## 3. Status Transition Rules: missing -> quarantined -> rejected -> negative_receipt -> accepted_for_routing

The allowed status vocabulary for cycle 2 receipt rows is:

```text
missing
quarantined
rejected
negative_receipt
accepted_for_routing
```

The statuses are not a required linear promotion ladder. They are a controlled
state machine:

| status | meaning | allowed next statuses |
|---|---|---|
| `missing` | The necessary surface, transcript, manuscript, locator, or extraction batch has not been acquired or checked. Absence is not evidence. | `quarantined`, `rejected`, `negative_receipt`, `accepted_for_routing` after acquisition and intake evidence is added. |
| `quarantined` | A source surface or fragment is relevant but incomplete, ambiguous, adjacent, generated, outline-only, metadata-only, target-facing, or representation-unclear. It may guide mining but cannot restart proof work. | `rejected`, `negative_receipt`, `accepted_for_routing` after second-pass evidence. |
| `rejected` | The candidate is the wrong source kind, lacks a locator, uses target data, is only repo reconstruction, or cannot bear the claimed receipt role. Rejection is about the candidate row, not necessarily the source surface. | Normally terminal for that row; a new row may be opened with better evidence. |
| `negative_receipt` | A complete acquired source surface was searched for the declared family object using a preserved query log and no emitted object was found. This is an explicit absence receipt for the declared scope only. | Terminal for that source scope unless a new source version, corrected transcript, new locator, or expanded query scope is acquired. |
| `accepted_for_routing` | A source fragment emits the required object with locator, representation context, no target import, and intake acceptance. It only routes to family identity checking. | Family-limited proof restart may begin; claim promotion remains forbidden until proof/canon gates pass. |

### 3.1 Missing to Quarantined

Move `missing` to `quarantined` when the repo has a plausible surface or
fragment, but at least one acceptance condition is incomplete:

- transcript or manuscript is not acquired;
- locator is approximate or outline-only;
- source is generated transcript excerpt rather than verified transcript;
- source is metadata, release chronology, or episode description only;
- fragment is adjacent to the family object but does not emit it;
- representation mapping is ambiguous;
- target-facing language is present and source-side provenance of the object is
  not established.

### 3.2 Quarantined to Rejected

Move `quarantined` to `rejected` when the candidate row cannot serve as the
claimed receipt even after reasonable disambiguation:

- source kind is repo reconstruction, secondary commentary, release metadata,
  or literature background for a primary GU receipt;
- locator does not exist or cannot be recovered;
- candidate uses target coefficients, target outcomes, DESI/dark-energy
  comparisons, CHSH values, desired ranks, or VZ closure targets to select the
  object;
- generated transcript text remains unverifiable for the needed fragment;
- the source contradicts the claimed emitted object.

### 3.3 Quarantined or Missing to Negative Receipt

Move to `negative_receipt` only when all of these are true:

1. `complete_acquired_source_surface = true` for the declared scope.
2. The scope is named: source id, component, version, transcript/manuscript
   capture, timestamp/page/paragraph range, and any excluded components.
3. A `query_log` is preserved with family-specific search terms, synonyms,
   notation variants, inspected hit list, and false-positive decisions.
4. The searched surface is strong enough to answer the absence question. For
   example, complete Oxford transcript can answer an Oxford-transcript absence;
   it cannot answer absence in Portal-only preface material or the 2021 draft.
5. The row states the exact required object absent: IG selector, RS
   action/operator, QFT finite projector, or DGU/VZ actual action/operator/EL.
6. `target_data_seen` is empty or explicitly marked as excluded from selection.
7. `promotion_allowed = false` and `restart_gate = blocked`.

### 3.4 Quarantined or Missing to Accepted for Routing

Move to `accepted_for_routing` only when a source fragment emits the required
family object, not merely a compatible topic label. The row must include exact
locator, short exact fragment or formula, emitted object type, representation
context, normalization choices, no target import, and family identity check
pending.

## 4. Source-Kind Policy Table for Cycle 1 Surfaces

| source kind or cycle 1 surface | current policy status | may become negative receipt? | may become accepted for routing? | control |
|---|---|---:|---:|---|
| Complete official transcript with exact local capture, e.g. complete scoped UCSD transcript | `quarantined` or `missing` until query log exists | yes, for declared transcript scope only | yes, if required object is emitted | Raw transcript status must be recorded; query log required for negative receipt. |
| Partial official transcript, starter claim rows, or locally captured excerpts | `quarantined` | no, unless the declared scope is only the captured excerpt and that limited scope is useful | yes, only for an emitted object inside the excerpt | Must not infer absence in uncaptured components. |
| Oxford 2013 / Portal Special availability rows | `quarantined` | not yet | not yet | Official surface exists, but exact Portal-only mining is incomplete. |
| JRE #1453 / #1628 indexed transcript surfaces without repo-local transcript text | `missing` | no | no | Transcript acquisition and extraction rows are prerequisite. |
| TOE/Jaimungal outline timestamps | `quarantined` | no | no | Outline labels locate topics only; they do not search the source text. |
| Keating, Apple, YouTube, podcast, or official page metadata | `quarantined` or `rejected` depending row role | no | no | Metadata can locate a source but cannot establish object presence or absence. |
| Visible generated transcript excerpt | `quarantined` | no | no | Generated text can guide mining; it is not accepted unless checked against primary audio/video or official transcript. |
| 2021 draft-release page without manuscript text | `missing` for manuscript content; `rejected` as formula receipt | no | no | Release metadata is chronology and pointer only. |
| Repo-authored reconstruction or local paper | `rejected` for primary GU receipt | no | no | It may propose reconstruction but cannot be a primary GU source receipt. |
| Literature index or published no-go background | `rejected` for primary GU receipt | no | no | Background may guide proof work, not GU source receipt intake. |

## 5. Target-Import Controls

Target-facing language is valuable for search prioritization but forbidden as a
selector.

The following controls are mandatory:

- DESI, dark-energy data, FLRW targets, CHSH/Bell outputs, observed ranks,
  generation counts, desired SM spectra, and VZ success criteria cannot select
  an IG object, a DGU/VZ operator, an RS differential, or a QFT projector.
- A DESI/dark-energy segment may become a search lead for a source-side action
  or operator only if the action or operator is emitted before comparison to
  target data in the checked fragment.
- Generated transcript excerpts that mention DESI or dark energy are
  automatically quarantined until checked against primary audio/video or an
  official transcript.
- Repo reconstructions may define candidate objects for proof exploration, but
  they must be marked `candidate_import` or `target_import` unless a primary
  source independently emits the object.
- A negative receipt cannot be created by searching only target-facing words.
  The query log must include source-side object terms and notation variants for
  the required family object.

## 6. Strongest Positive Result

The strongest positive result is a precise separation between absence and
non-acquisition:

```text
Cycle 1 identified useful source surfaces and locator candidates, but only a
complete acquired source surface plus a preserved family query log can produce
an explicit negative receipt.
```

This lets future workers record true negative controls without overreading
outline, metadata, generated transcript, release, or reconstruction rows. It
also makes the current cycle 1 result sharper: the repo is not saying the JRE,
Oxford/Portal, Keating/TOE, UCSD, or 2021 manuscript surfaces lack the required
objects globally. It is saying no accepted source receipt has yet been produced
from the currently acquired and checked surfaces.

## 7. First Exact Obstruction

The first exact obstruction is:

```text
No cycle 1 surface has both complete acquired scope and preserved family query
log sufficient to instantiate NegativeReceiptInstance_V1 for any of the four
family blockers.
```

The obstruction is procedural and precedes proof work. For unacquired JRE and
2021 manuscript text, absence is `missing`. For outline-only TOE/Jaimungal and
metadata-only Keating surfaces, absence is `quarantined` or `rejected` by source
kind. For UCSD, the local transcript gives useful hints, but a negative receipt
still requires a declared complete query pass and query log for the exact family
object.

## 8. GU Claim Impact and Forbidden Promotions

No GU claim is promoted.

Allowed statement:

```text
The repo now has a policy for distinguishing missing acquisition, quarantine,
rejection, explicit negative receipt, and accepted source routing after cycle 1.
```

Forbidden promotions:

```text
IG selects K_IG.
RS source-derived d_RS,-1 is established.
QFT P_fin^b is supplied.
DGU/VZ actual D_GU^epsilon 0/1 is identified.
Any cycle 1 source globally lacks the required object.
Outline-only material proves absence.
Metadata-only material proves absence.
Generated transcript excerpt is an accepted transcript receipt.
DESI or dark-energy target language selects an IG or DGU/VZ object.
Repo reconstruction is a primary GU source receipt.
VZ evasion, dark-energy recovery, FLRW recovery, rank/generation readout,
finite-QFT recovery, covariance, CHSH, or Bell recovery is derived.
```

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "NegativeReceiptQuarantinePolicy_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0203",
  "cycle": 2,
  "lane": 4,
  "verdict": "CONDITIONAL_POLICY_READY_NEGATIVE_RECEIPTS_REQUIRE_COMPLETE_SURFACE",
  "verdict_class": "conditional",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0203-cycle2-negative-receipt-quarantine-policy.md",
    "companion_audit": "tests/hourly_20260625_0203_cycle2_negative_receipt_quarantine_policy_audit.py"
  },
  "status_vocabulary": [
    "missing",
    "quarantined",
    "rejected",
    "negative_receipt",
    "accepted_for_routing"
  ],
  "status_transition_rules": {
    "missing": {
      "meaning": "surface transcript manuscript locator or extraction batch not acquired or checked",
      "absence_is_evidence": false,
      "allowed_next_statuses": [
        "quarantined",
        "rejected",
        "negative_receipt",
        "accepted_for_routing"
      ]
    },
    "quarantined": {
      "meaning": "relevant but incomplete ambiguous adjacent generated outline-only metadata-only target-facing or representation-unclear",
      "proof_restart_allowed": false,
      "allowed_next_statuses": [
        "rejected",
        "negative_receipt",
        "accepted_for_routing"
      ]
    },
    "rejected": {
      "meaning": "candidate row cannot serve the claimed receipt role",
      "normally_terminal_for_row": true
    },
    "negative_receipt": {
      "meaning": "complete acquired source surface searched for declared family object with preserved query log and no emitted object found",
      "proof_restart_allowed": false,
      "promotion_allowed": false
    },
    "accepted_for_routing": {
      "meaning": "source fragment emits required object and may be routed to family mathematical identity check",
      "claim_promotion_allowed_at_intake": false
    }
  },
  "negative_receipt_requirements": {
    "complete_acquired_source_surface": true,
    "declared_source_scope": true,
    "query_log_required": true,
    "family_specific_query_terms_required": true,
    "notation_variants_required": true,
    "inspected_hits_and_false_positive_decisions_required": true,
    "exact_required_object_absence_required": true,
    "target_import_forbidden": true,
    "promotion_allowed": false,
    "restart_gate": "blocked"
  },
  "surfaces_that_cannot_be_negative_receipts_without_more_acquisition": [
    "outline_only",
    "metadata_only",
    "release_metadata_only",
    "generated_transcript_excerpt",
    "indexed_transcript_without_repo_local_text",
    "unacquired_author_manuscript",
    "repo_reconstruction_artifact",
    "literature_index"
  ],
  "cycle1_source_kind_policy": [
    {
      "surface": "complete_official_transcript_declared_scope",
      "current_status": "quarantined_or_missing_until_query_log_exists",
      "can_become_negative_receipt": true,
      "can_become_accepted_for_routing": true,
      "control": "complete scope and query log required for negative receipt"
    },
    {
      "surface": "partial_transcript_or_starter_claim_rows",
      "current_status": "quarantined",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": true,
      "control": "cannot infer absence in uncaptured components"
    },
    {
      "surface": "Oxford_2013_Portal_Special_availability_rows",
      "current_status": "quarantined",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "Portal-only preface and post-lecture material still need exact mining"
    },
    {
      "surface": "JRE_indexed_transcript_surfaces_without_local_text",
      "current_status": "missing",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "transcript acquisition and extraction rows required first"
    },
    {
      "surface": "TOE_Jaimungal_outline_timestamps",
      "current_status": "quarantined",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "outline labels locate topics only"
    },
    {
      "surface": "metadata_only",
      "current_status": "quarantined_or_rejected",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "metadata locates a source but cannot establish object presence or absence"
    },
    {
      "surface": "generated_transcript_excerpt",
      "current_status": "quarantined",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "must be checked against primary audio video or official transcript"
    },
    {
      "surface": "2021_draft_release_page_without_manuscript_text",
      "current_status": "missing_for_manuscript_content_rejected_as_formula_receipt",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "release metadata is chronology and pointer only"
    },
    {
      "surface": "repo_reconstruction_artifact",
      "current_status": "rejected",
      "can_become_negative_receipt": false,
      "can_become_accepted_for_routing": false,
      "control": "not a primary GU source receipt"
    }
  ],
  "target_import_controls": {
    "DESI_target_language_can_select_IG_or_DGU_object": false,
    "dark_energy_target_language_can_select_IG_or_DGU_object": false,
    "target_data_can_select_RS_or_QFT_object": false,
    "generated_transcript_excerpt_can_be_accepted": false,
    "repo_reconstruction_can_be_primary_source_receipt": false,
    "source_side_object_must_precede_target_comparison": true,
    "negative_receipt_query_log_must_include_source_side_object_terms": true
  },
  "family_required_objects": {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1"
  },
  "strongest_positive_result": "cycle 1 source surfaces are now separated into non-acquired absence, quarantined locator candidates, rejected non-primary rows, future negative receipt candidates, and accepted-routing criteria",
  "first_exact_obstruction": {
    "id": "NegativeReceiptInstance_V1",
    "missing_for_all_cycle1_surfaces": true,
    "description": "no cycle 1 surface has both complete acquired scope and preserved family query log sufficient to record explicit absence of a required object"
  },
  "no_claim_promotions": {
    "IG_K_IG_selected": false,
    "RS_d_RS_minus_1_source_derived": false,
    "QFT_P_fin_b_supplied": false,
    "DGU_actual_operator_identified": false,
    "cycle1_source_globally_lacks_required_object": false,
    "outline_only_material_proves_absence": false,
    "metadata_only_material_proves_absence": false,
    "generated_transcript_excerpt_accepted": false,
    "DESI_or_dark_energy_selects_IG_or_DGU": false,
    "repo_reconstruction_is_primary_receipt": false,
    "VZ_evasion_closed": false,
    "dark_energy_or_FLRW_recovered": false,
    "finite_QFT_or_CHSH_recovered": false,
    "physical_rank_or_generation_readout": false
  },
  "forbidden_promotions": [
    "IG selects K_IG",
    "RS source-derived d_RS,-1 is established",
    "QFT P_fin^b is supplied",
    "DGU/VZ actual D_GU^epsilon 0/1 is identified",
    "any cycle 1 source globally lacks the required object",
    "outline-only material proves absence",
    "metadata-only material proves absence",
    "generated transcript excerpt is an accepted transcript receipt",
    "DESI or dark-energy target language selects an IG or DGU/VZ object",
    "repo reconstruction is a primary GU source receipt",
    "VZ evasion dark-energy FLRW rank generation finite-QFT covariance CHSH or Bell recovery is derived"
  ]
}
```
