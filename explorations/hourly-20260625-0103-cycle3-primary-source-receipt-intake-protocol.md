---
title: "Hourly 20260625 0103 Cycle 3 Primary Source Receipt Intake Protocol"
date: "2026-06-25"
run: "hourly-20260625-0103"
cycle: "3"
lane: "5"
doc_type: primary_source_receipt_intake_protocol
artifact_id: "PrimarySourceReceiptIntakeProtocol_V1"
verdict: "CONDITIONAL_PROTOCOL_READY_RECEIPTS_STILL_MISSING"
owned_path: "explorations/hourly-20260625-0103-cycle3-primary-source-receipt-intake-protocol.md"
companion_audit: "tests/hourly_20260625_0103_cycle3_primary_source_receipt_intake_protocol_audit.py"
---

# Hourly 20260625 0103 Cycle 3 Primary Source Receipt Intake Protocol

## 1. Verdict

Verdict: **conditional**.

This artifact closes a process gate, not a mathematical or physical claim gate.
It defines the repo-local intake protocol for future primary GU source receipts
and gives family-specific routing for IG, RS, QFT, and DGU/VZ. It does **not**
assert that any of the missing receipts has been found.

The protocol is ready to use when a new source fragment, transcript row,
manuscript locator, or derivation cell is submitted. Downstream proof workers
must remain stopped until a receipt instance passes the intake schema,
rejection/import controls, family routing, and restart gate below.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` supplies the governing discipline: source process is not
physics evidence, compatibility is not derivation, and no branch may hide target
data inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` supplies the worker contract and
verdict vocabulary. This lane must produce a decision-grade artifact, identify
the first obstruction, and avoid overlap with sibling workers.

`explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md`
establishes the immediate predecessor state. The first global missing object is:

```text
RepoLocalPrimaryGUSourceReceiptMap_V1
```

The same ledger blocks all four families at primary-source receipt level:

| family | required object still missing |
|---|---|
| IG | `SourceForcedCodomainSelectorForK_IG` |
| RS | `source.action_or_operator for d_RS,-1` |
| QFT | `P_fin^b: F_phys^b(O) -> K_b` |
| DGU/VZ | `operator_source_primary_action_or_EL for D_GU^epsilon 0/1` |

`sources/media-index.md`, `sources/media-contributor-tasks-v1.md`, and
`sources/README.md` give the source-surface discipline. Media rows are
provenance and chronology unless an exact transcript, timestamp, manuscript
locator, or archived fragment is tied to a claim. This protocol therefore
accepts source receipts only as provenance-to-object bridges; it does not
promote their mathematical correctness.

## 3. Strongest Positive Protocol

The strongest positive result is a four-family intake protocol with a single
schema, explicit source kinds, quarantine controls, family routing, and a
sequential proof-restart gate.

### 3.1 Required Receipt Schema

Every candidate receipt must instantiate this schema before any family worker
can consume it:

| field | required meaning |
|---|---|
| `receipt_id` | stable repo-local identifier for the candidate receipt |
| `family` | exactly one of `IG`, `RS`, `QFT`, `DGU_VZ` |
| `required_object` | the blocked family object the receipt claims to supply |
| `source_kind` | one accepted source kind from Section 3.2 |
| `source_id` | source identifier, URL, archive id, manuscript id, or local source path |
| `locator` | timestamp, page, section, equation, row, or derivation-cell locator |
| `source_status` | verification status: `raw`, `transcript_checked`, `archived`, `manuscript_checked`, or `rejected` |
| `exact_fragment` | exact fragment, short quote, formula, or precise paraphrase with locator |
| `emitted_object_type` | `selector`, `action`, `operator`, `differential`, `projector`, `EL_equation`, `constraint`, or `negative_control` |
| `emitted_formula_or_rule` | the formula, rule, or explicit "none supplied" result extracted from the source |
| `representation_context` | source-side notation and how it maps to repo notation |
| `normalization_choices` | sign, scale, projection, coefficient, gauge, and convention choices explicitly present or absent |
| `target_data_seen` | target-facing data touched during extraction, normally empty |
| `import_status` | `source_emitted`, `candidate_import`, `target_import`, `ambiguous`, or `rejected` |
| `acceptance_status` | `accepted_for_routing`, `quarantined`, `rejected`, or `needs_second_reader` |
| `promotion_allowed` | always `false` at intake |
| `restart_gate` | downstream proof restart decision: `closed`, `blocked`, or `family_limited` |
| `audit_notes` | short reason for the intake decision |

### 3.2 Accepted Source Kinds

Accepted source kinds are deliberately narrow:

| source kind | accepted use | minimum locator |
|---|---|---|
| `official_transcript` | source-native wording, formulas, and terminology | source id plus timestamp or paragraph |
| `official_video_or_audio_with_timestamp` | primary public statement when transcript is absent | URL plus timestamp range |
| `author_manuscript_or_draft` | formulas, definitions, derivation cells, actions, operators | page, section, equation, or paragraph |
| `official_site_page` | release context, source-surface link, official wording | URL plus heading or paragraph |
| `archived_primary_fragment` | stable preservation of one of the above | archive id plus original locator |
| `source_attached_visual` | diagram or visual aid only when tied to source context | source id plus visual locator |

Non-primary summaries, wiki paraphrases, AI summaries, commentary, reception
pieces, and downstream reconstruction notes are discovery aids only. They may
open a candidate receipt, but they cannot satisfy `accepted_for_routing`
without one accepted source kind.

### 3.3 Rejection and Import Controls

A candidate receipt is rejected or quarantined before family routing when any
of these controls fires:

| control | result |
|---|---|
| no exact locator | `rejected` |
| no emitted formula, rule, operator, selector, action, differential, projector, EL equation, constraint, or negative-control result | `rejected` unless explicitly filed as a negative receipt |
| source kind is commentary, secondary index, AI summary, or unverified paraphrase | `quarantined` as discovery aid |
| source fragment is compatible with the desired object but does not emit or select it | `candidate_import` and `quarantined` |
| extraction uses target coefficients, target spectra, physical rank, desired dark-energy sign, CHSH output, or VZ closure target | `target_import` and `rejected` |
| notation map changes source meaning to fit a repo branch | `ambiguous` and `needs_second_reader` |
| only a representation label is supplied | `quarantined` |
| only raw computation is supplied without source locator | `rejected` |
| source contradicts the proposed emitted object | `rejected` or filed as `negative_control` |

At intake, `promotion_allowed` is always false. Acceptance only means:

```text
this source fragment is precise enough to route to a family proof worker
```

It never means:

```text
the GU claim is proved, the downstream construction is correct, or the family
gate is closed.
```

## 4. Family-Specific Routing

Each accepted or quarantined receipt is routed by family and required object.

| family | accepts receipt for | route after intake | restart condition |
|---|---|---|---|
| IG | source-selected codomain, witness category, Shiab/projection selector, parent-action selector, or eliminator for `K_IG` | `K_IGSourceSelectorReceiptQueue` | only restart IG eliminator/finality work after a source-emitted selector or negative-control eliminator is accepted |
| RS | source action, operator, Noether identity, BRST rule, gauge variation, or actual-DGU source for `d_RS,-1` | `RSSourceActionReceiptQueue` | only restart projection/finality/loss and rank work after the differential origin is source-emitted |
| QFT | finite source extraction map, local representative, or projector `P_fin^b: F_phys^b(O) -> K_b` | `QFTPFinBReceiptQueue` | only restart one-mode certificate and 16-mode packet work after `P_fin^b` or a negative obstruction is accepted |
| DGU_VZ | primary action, operator, EL equation, principal symbol, projectors, coefficients, or first-order terms for actual `D_GU^epsilon 0/1` | `DGUOperatorReceiptQueue` | only restart actual-operator certificate and VZ closure work after actual operator receipt is accepted |

Cross-family receipts are not merged automatically. A receipt that appears to
touch multiple families must be cloned into family-specific receipt instances,
each with its own `required_object`, locator, import status, and restart gate.

## 5. First Exact Obstruction

The first exact obstruction is that the repo has no accepted instance of:

```text
PrimarySourceReceiptInstance_V1
```

for any of the four missing family objects. Cycle 2 identified the missing map;
this artifact defines the intake rule for entries in that map. The map is still
empty until a receipt instance passes the protocol.

The obstruction is earlier than proof search. A downstream worker cannot decide
operator finality, rank, positivity, VZ closure, dark-energy recovery, or CHSH
recovery from a source candidate whose import status is `candidate_import`,
`target_import`, `ambiguous`, or `rejected`.

## 6. Constructive Next Object

The constructive next object is:

```text
RepoLocalPrimaryGUSourceReceiptMap_V1
```

with entries of type:

```text
PrimarySourceReceiptInstance_V1
```

The first accepted instance should be added only after a two-step review:

1. Intake review checks source kind, locator, exact fragment, emitted object,
   representation context, import status, and no-target-data discipline.
2. Family review checks whether the emitted object is mathematically the object
   required by the family gate, or only a related candidate.

If step 1 passes and step 2 fails, the receipt remains valid provenance but
does not restart downstream proof work.

## 7. GU Impact and Sequential Gate

No GU claim is promoted by this protocol.

Allowed statement:

```text
The repo now has an intake protocol for deciding whether future primary GU
source fragments are precise enough to route to IG, RS, QFT, or DGU/VZ proof
workers.
```

Forbidden promotions:

```text
IG selects K_IG.
RS source-derived d_RS,-1 is established.
QFT P_fin^b is supplied.
DGU/VZ actual D_GU^epsilon 0/1 is identified.
VZ evasion is closed.
Dark-energy, FLRW, rank, generation, finite QFT, covariance, or CHSH recovery
is derived.
```

Sequential restart rule:

```text
source intake acceptance
-> family mathematical identity check
-> family-limited downstream restart
-> proof worker may attempt closure
-> claim promotion still requires the normal proof/canon promotion gate
```

Until that sequence is satisfied for a family, the only safe parallel work is
source mining, transcript locator extraction, receipt-schema validation, and
audit hardening. Target-facing proof work remains stopped.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "PrimarySourceReceiptIntakeProtocol_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0103",
  "cycle": 3,
  "lane": 5,
  "verdict": "CONDITIONAL_PROTOCOL_READY_RECEIPTS_STILL_MISSING",
  "verdict_class": "conditional",
  "mission": "Mission_A_source_intake_process_gate",
  "not_a_claim_promotion": true,
  "predecessor_missing_object": "RepoLocalPrimaryGUSourceReceiptMap_V1",
  "first_exact_obstruction": {
    "id": "PrimarySourceReceiptInstance_V1",
    "missing": true,
    "description": "no family has an accepted receipt instance satisfying source kind locator emitted object import controls and restart gate"
  },
  "receipt_schema_required_fields": [
    "receipt_id",
    "family",
    "required_object",
    "source_kind",
    "source_id",
    "locator",
    "source_status",
    "exact_fragment",
    "emitted_object_type",
    "emitted_formula_or_rule",
    "representation_context",
    "normalization_choices",
    "target_data_seen",
    "import_status",
    "acceptance_status",
    "promotion_allowed",
    "restart_gate",
    "audit_notes"
  ],
  "accepted_source_kinds": [
    "official_transcript",
    "official_video_or_audio_with_timestamp",
    "author_manuscript_or_draft",
    "official_site_page",
    "archived_primary_fragment",
    "source_attached_visual"
  ],
  "accepted_emitted_object_types": [
    "selector",
    "action",
    "operator",
    "differential",
    "projector",
    "EL_equation",
    "constraint",
    "negative_control"
  ],
  "import_controls": {
    "allowed_import_statuses": [
      "source_emitted",
      "candidate_import",
      "target_import",
      "ambiguous",
      "rejected"
    ],
    "accepted_for_restart_requires": [
      "source_emitted",
      "accepted_for_routing",
      "target_data_seen_empty",
      "family_mathematical_identity_check_passed"
    ],
    "rejection_triggers": [
      "no_exact_locator",
      "secondary_or_ai_summary_only",
      "raw_computation_without_source_locator",
      "target_coefficients_or_outputs_used",
      "representation_label_only",
      "source_contradicts_emitted_object"
    ],
    "quarantine_triggers": [
      "candidate_compatible_but_not_source_emitted",
      "unverified_paraphrase",
      "ambiguous_notation_map",
      "commentary_or_reception_only"
    ]
  },
  "family_routing": [
    {
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "receipt_queue": "K_IGSourceSelectorReceiptQueue",
      "accepted_receipt_kinds": [
        "source-selected codomain",
        "witness category",
        "Shiab/projection selector",
        "parent-action selector",
        "K_IG eliminator"
      ],
      "downstream_restart_blocked_until": "source-emitted selector or negative-control eliminator accepted",
      "promotion_allowed": false
    },
    {
      "family": "RS",
      "required_object": "source.action_or_operator for d_RS,-1",
      "receipt_queue": "RSSourceActionReceiptQueue",
      "accepted_receipt_kinds": [
        "source action",
        "operator",
        "Noether identity",
        "BRST rule",
        "gauge variation",
        "actual-DGU source for d_RS,-1"
      ],
      "downstream_restart_blocked_until": "source-emitted differential origin accepted",
      "promotion_allowed": false
    },
    {
      "family": "QFT",
      "required_object": "P_fin^b: F_phys^b(O) -> K_b",
      "receipt_queue": "QFTPFinBReceiptQueue",
      "accepted_receipt_kinds": [
        "finite source extraction map",
        "local representative",
        "source projector P_fin^b",
        "negative obstruction"
      ],
      "downstream_restart_blocked_until": "P_fin^b or negative obstruction accepted",
      "promotion_allowed": false
    },
    {
      "family": "DGU_VZ",
      "required_object": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
      "receipt_queue": "DGUOperatorReceiptQueue",
      "accepted_receipt_kinds": [
        "primary action",
        "operator",
        "EL equation",
        "principal symbol",
        "projectors",
        "coefficients",
        "extra first-order terms"
      ],
      "downstream_restart_blocked_until": "actual D_GU^epsilon 0/1 operator receipt accepted",
      "promotion_allowed": false
    }
  ],
  "sequential_gate": [
    "source_intake_acceptance",
    "family_mathematical_identity_check",
    "family_limited_downstream_restart",
    "proof_worker_attempts_closure",
    "normal_proof_or_canon_promotion_gate"
  ],
  "downstream_restart_policy": {
    "IG": "restart only IG eliminator finality after source selector or negative-control eliminator",
    "RS": "restart only RS projection finality loss and rank work after source differential origin",
    "QFT": "restart only QFT one-mode and 16-mode work after P_fin^b or negative obstruction",
    "DGU_VZ": "restart only actual-operator certificate and VZ closure after actual operator receipt"
  },
  "no_claim_promotions": {
    "IG_K_IG_selected": false,
    "RS_d_RS_minus_1_source_derived": false,
    "QFT_P_fin_b_supplied": false,
    "DGU_actual_operator_identified": false,
    "VZ_evasion_closed": false,
    "dark_energy_or_FLRW_recovered": false,
    "QFT_state_or_CHSH_recovered": false,
    "physical_rank_or_generation_readout": false
  },
  "constructive_next_object": {
    "id": "RepoLocalPrimaryGUSourceReceiptMap_V1",
    "entry_type": "PrimarySourceReceiptInstance_V1",
    "next_step": "instantiate one candidate receipt from primary GU source mining and run intake before any downstream proof restart"
  }
}
```
