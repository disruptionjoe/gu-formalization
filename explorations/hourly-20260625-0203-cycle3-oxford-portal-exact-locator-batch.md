---
title: "Hourly 20260625 0203 Cycle 3 Oxford Portal Exact Locator Batch"
date: "2026-06-25"
run: "hourly-20260625-0203"
cycle: 3
lane: 2
doc_type: oxford_portal_exact_locator_batch
artifact_id: "OxfordPortalExactLocatorBatch_V1"
verdict: "BLOCKED_BATCH_SPECIFIED_ZERO_ACCEPTED_RECEIPTS"
owned_path: "explorations/hourly-20260625-0203-cycle3-oxford-portal-exact-locator-batch.md"
companion_audit: "tests/hourly_20260625_0203_cycle3_oxford_portal_exact_locator_batch_audit.py"
---

# Hourly 20260625 0203 Cycle 3 Oxford Portal Exact Locator Batch

## 1. Verdict

Verdict: **blocked**.

This artifact creates:

```text
OxfordPortalExactLocatorBatch_V1
```

as the gate specification for exact locator mining over the Oxford 2013
lecture surface and the Portal Special release surface. It does not perform
fresh transcript mining, does not browse, and does not accept any receipt.

Decision:

```text
best_official_surface: Oxford 2013 / Portal Special
batch_status: specified_ready_for_execution
accepted_receipt_count: 0
negative_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
first_obstruction: exact acquired component plus query log plus emitted required object
```

The expected current result is therefore confirmed repo-locally:

- Oxford/Portal is the best official public source surface for first-pass GU
  exact locator mining.
- The exact-locator batch is now specified.
- Current accepted receipts are zero.
- Portal-only preface and post-lecture material remain unmined locally.
- Proof restart remains blocked for IG, RS, QFT, and DGU/VZ.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` sets the governing discipline. The repo should pursue GU
reconstruction aggressively, but process progress, compatibility, public
framing, and source-surface availability are not mathematical derivations.

`process/runbooks/five-lane-frontier-run.md` supplies the lane contract: make a
decision-grade artifact, identify the exact obstruction, and do not promote
claims past the evidence.

`OxfordPortalReceiptMiningPacket_V1` establishes that Oxford 2013 and Portal
Special are official or source-native high-priority surfaces, while current
local rows do not emit any of the four family blocker objects.

`RepoLocalPrimaryGUSourceReceiptMap_V1` records the aggregate state after cycle
2: the process map exists, but accepted receipts remain zero and proof restart
is false for every source surface and family.

`TranscriptManuscriptAcquisitionQueue_V1` ranks Oxford/Portal exact-locator
work as immediately runnable source-side work. It also states that the exact
Portal-only preface and post-lecture material is still a missing artifact for
local locator purposes.

`NegativeReceiptQuarantinePolicy_V1` controls absence claims. A negative row
requires a complete acquired source component, declared scope, preserved query
log, inspected hits and false-positive decisions, exact absence of the required
object, no target import, `promotion_allowed = false`, and
`restart_gate = blocked`.

`sources/media-index.md` gives the source identifiers and statuses:

| source id | local derivation |
|---|---|
| `GU-MEDIA-2013-OXFORD` | primary public lecture surface; `transcript-available`; strongest source for claim-mined GU terminology already used in local logs |
| `GU-MEDIA-2020-PORTAL-SPECIAL` | official release surface for Oxford recording plus contextual preface and post-lecture presentation; `transcript-available` via Oxford page |
| `GU-POD-2020-PORTAL-SPECIAL` | Portal Group transcript surface for the full GU presentation; high-priority canonical public presentation surface |

`sources/claim-ledger-v1-draft.md` gives the useful Oxford starter rows.
Local Oxford starter rows are useful, but they are not accepted receipts.
They cover source-native terminology and framing: four flavors, observation
split, observerse, `U^{14} = met(X^4)`, projection operator `pi`,
base/observerse distinction, Sector I replacement/recovery, pullback language,
14-dimensional framing, minimal-assumption methodology, and one synthesized
chirality avoidance row flagged as reconstruction. These rows are useful
search anchors. They are not accepted receipts for IG, RS, QFT, or DGU/VZ.

## 3. Source Components and Local Availability

The batch must treat Oxford/Portal as components, not as one undifferentiated
surface. A negative result on one component cannot prove absence in another.

| component id | component | local availability | current row status | batch consequence |
|---|---|---|---|---|
| `oxford_2013_transcript` | Oxford 2013 lecture transcript substance | locally represented by starter rows in `sources/claim-ledger-v1-draft.md`; `sources/media-index.md` marks transcript available | useful starter rows; no accepted receipt | exact-locator pass may start here using starter rows as anchors |
| `portal_special_shared_oxford_substance` | Portal Special rebroadcast/shared Oxford lecture substance | covered only insofar as it shares Oxford lecture substance already represented by Oxford starter rows | useful shared surface; no accepted receipt | duplicate hits must be deduplicated to Oxford locators unless Portal adds distinct wording |
| `portal_special_preface` | Portal-only contextual preface before the Oxford lecture | not locally mined in the starter ledger | missing component | cannot support accepted or negative receipt until acquired and searched |
| `portal_special_postlecture` | Portal-only post-lecture presentation or contextual material | not locally mined in the starter ledger | missing component | cannot support accepted or negative receipt until acquired and searched |

Current acceptance decision:

```text
local_oxford_starter_rows_are_useful: true
local_oxford_starter_rows_are_accepted_receipts: false
portal_only_preface_postlecture_locally_mined: false
accepted_receipt_count: 0
```

## 4. Exact-Locator Query Plan by Family

Each family pass must record exact component, exact locator, query terms,
inspected hits, false-positive decisions, emitted object type, emitted formula
or rule, and intake status. Query hits are candidates only. A row becomes
accepted only if the source fragment emits the required family object and a
formula or rule under the intake protocol.

| family | required object | source-side query families | starter rows useful for targeting | accept only if fragment emits |
|---|---|---|---|---|
| IG | `SourceForcedCodomainSelectorForK_IG` | `observerse`; `Shiab`; projection; `pi`; codomain; selector; target; source; parent; witness; lower-order; rigidity; Sector I; replacement/recovery; pullback | observerse rows; `U^{14} = met(X^4)`; `pi`; Sector I; pullback | a source-forced codomain selector for `K_IG`, not merely projection vocabulary |
| RS | `source.action_or_operator for d_RS,-1` | Rarita; spinor; spin 3/2; gravitino; action; operator; differential; variation; Noether; BRST; gauge; complex; rolled; ship-in-a-bottle | observation split, fields on `Y`/`U`, pullback, general field-content framing | an action/operator/Noether/BRST rule whose identity can be checked against `d_RS,-1` |
| QFT | `P_fin^b: F_phys^b(O) -> K_b` | finite; quantization; local; physical; projector; projection; quotient; representative; mode; Hilbert; state; algebra; covariance; pullback | `pi`; pullback; fields observed on `X`; observerse/base distinction | a finite source projector or extraction map with source and codomain, not broad quantization talk |
| DGU_VZ | `operator_source_primary_action_or_EL for D_GU^epsilon 0/1` | action; operator; equation; Euler; Lagrange; Euler-Lagrange; field equation; `D_GU`; epsilon; theta; alpha; principal symbol; coefficient; projector; variation; inhomogeneous; Vafa-Witten; VZ | `U^{14} = met(X^4)`; `pi`; Sector I; fields on `Y`/`U`; minimal-assumption methodology | actual GU action/operator/EL data for `D_GU^epsilon` 0/1, not compatibility with a later typed-spine model |

Batch execution order:

1. Search `oxford_2013_transcript` exact text from the strongest starter
   anchors outward.
2. Search `portal_special_shared_oxford_substance` only for wording not already
   represented by Oxford rows.
3. Acquire and search `portal_special_preface`.
4. Acquire and search `portal_special_postlecture`.
5. Emit candidate rows or scoped missing rows for each family/component pair.
6. Promote absence to `negative_receipt` only after complete component scope and
   query log requirements are met.

## 5. Candidate Row Output Schema and Negative-Row Requirements

The batch output type is:

```text
OxfordPortalExactLocatorRow_V1
```

Required fields:

| field | requirement |
|---|---|
| `batch_id` | `OxfordPortalExactLocatorBatch_V1` |
| `source_id` | one of `GU-MEDIA-2013-OXFORD`, `GU-MEDIA-2020-PORTAL-SPECIAL`, `GU-POD-2020-PORTAL-SPECIAL` |
| `source_component` | one of `oxford_2013_transcript`, `portal_special_shared_oxford_substance`, `portal_special_preface`, `portal_special_postlecture` |
| `component_availability` | `starter_rows_available`, `shared_substance_available`, `missing_not_locally_mined`, or `complete_acquired_scope` |
| `family` | `IG`, `RS`, `QFT`, or `DGU_VZ` |
| `required_object` | family blocker from the cycle 2 map |
| `query_terms` | exact source-side terms and notation variants searched |
| `exact_locator` | timestamp, paragraph, section, page, or transcript locator; unavailable for missing components |
| `exact_fragment_or_absence` | short source fragment, or an explicit scoped absence result |
| `emitted_object_type` | source-emitted object class, or `none_supplied` |
| `emitted_formula_or_rule` | source-emitted formula/rule, or `none_supplied` |
| `starter_row_used` | true only if a local Oxford starter row guided the search |
| `starter_row_is_accepted_receipt` | always false unless a future exact fragment independently satisfies intake; current value false |
| `target_data_seen` | list target-facing terms seen; empty or excluded before selection |
| `import_status` | `source_emitted`, `candidate_import`, `target_import`, `ambiguous`, or `none_supplied` |
| `acceptance_status` | `missing`, `quarantined`, `negative_receipt`, `accepted_for_routing`, or `rejected` |
| `proof_restart_allowed` | false unless a future row is accepted and then passes family identity check |
| `promotion_allowed` | false |

Negative rows require all of the following:

```text
complete_acquired_source_component: true
declared_component_scope: true
query_log_preserved: true
family_specific_terms_and_notation_variants_preserved: true
inspected_hits_and_false_positive_decisions_preserved: true
exact_required_object_absence_recorded: true
target_import_excluded: true
promotion_allowed: false
proof_restart_allowed: false
```

No current Oxford/Portal row satisfies these negative-row requirements for the
full Oxford/Portal surface, because Portal-only preface and post-lecture
material are not locally mined.

## 6. Strongest Positive Result

The strongest positive result is not a receipt. It is a scoped gate:

```text
Oxford/Portal is the best official source surface for first exact-locator
mining, and the repo now has a family-by-family batch specification that can
produce candidate rows, scoped missing rows, or future negative receipts without
promoting any GU claim.
```

The local Oxford starter rows are genuinely useful because they identify
source-native vocabulary and nearby transcript neighborhoods: observerse,
`U^{14} = met(X^4)`, `pi`, Sector I, and pullback language. They should be used
as search anchors and representation controls. They must not be treated as
accepted receipts for the four family blockers.

## 7. First Exact Obstruction

The first exact obstruction is:

```text
No Oxford/Portal component currently has an exact local locator whose fragment
emits any of the four required family objects with an emitted formula or rule.
```

The component-level obstruction is sharper:

```text
Oxford 2013 transcript: starter rows exist, but no family-object receipt row.
Portal shared Oxford substance: available only as shared Oxford substance unless
distinct Portal wording is exact-located.
Portal-only preface: not locally mined.
Portal-only postlecture: not locally mined.
```

The proof restart obstruction is:

```text
accepted PrimarySourceReceiptInstance_V1
-> family mathematical identity check
-> family-limited proof restart
```

The first arrow has not been reached for Oxford/Portal.

## 8. GU Claim Impact and Forbidden Promotions

No GU claim is promoted.

Allowed statement:

```text
Oxford/Portal is the lead official public source surface for exact-locator
mining, and Oxford starter rows provide useful terminology anchors.
```

Forbidden promotions:

```text
Oxford starter rows are accepted receipts.
Portal Special preface/postlecture is locally mined.
IG selects K_IG.
RS source-derived d_RS,-1 is established.
QFT P_fin^b is supplied.
DGU/VZ actual D_GU^epsilon 0/1 is identified.
Any Oxford/Portal component globally lacks the required object without complete
component scope and query log.
Proof restart is allowed.
VZ evasion is closed.
Dark-energy, FLRW, rank, generation, finite-QFT, covariance, rho_AB, CHSH, or
Bell recovery is derived.
```

The batch may improve source discipline. It does not improve proof status until
an accepted receipt and family identity check exist.

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "OxfordPortalExactLocatorBatch_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0203",
  "cycle": 3,
  "lane": 2,
  "verdict": "BLOCKED_BATCH_SPECIFIED_ZERO_ACCEPTED_RECEIPTS",
  "verdict_class": "blocked",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0203-cycle3-oxford-portal-exact-locator-batch.md",
    "companion_audit": "tests/hourly_20260625_0203_cycle3_oxford_portal_exact_locator_batch_audit.py",
    "batch_id": "OxfordPortalExactLocatorBatch_V1"
  },
  "source_surface": {
    "best_official_surface": "Oxford 2013 / Portal Special",
    "source_ids": [
      "GU-MEDIA-2013-OXFORD",
      "GU-MEDIA-2020-PORTAL-SPECIAL",
      "GU-POD-2020-PORTAL-SPECIAL"
    ],
    "status": "official_source_surface_available_exact_locator_batch_specified"
  },
  "source_components": [
    {
      "component_id": "oxford_2013_transcript",
      "label": "Oxford transcript",
      "source_id": "GU-MEDIA-2013-OXFORD",
      "local_availability": "starter_rows_available_in_claim_ledger_v1_draft",
      "current_row_status": "quarantined_starter_rows",
      "useful_for_batch": true,
      "accepted_receipt": false
    },
    {
      "component_id": "portal_special_shared_oxford_substance",
      "label": "Portal Special shared Oxford substance",
      "source_id": "GU-MEDIA-2020-PORTAL-SPECIAL",
      "local_availability": "covered_only_as_shared_oxford_substance",
      "current_row_status": "quarantined_shared_surface",
      "useful_for_batch": true,
      "accepted_receipt": false
    },
    {
      "component_id": "portal_special_preface",
      "label": "Portal-only preface",
      "source_id": "GU-POD-2020-PORTAL-SPECIAL",
      "local_availability": "missing_not_locally_mined",
      "current_row_status": "missing_component",
      "useful_for_batch": true,
      "accepted_receipt": false
    },
    {
      "component_id": "portal_special_postlecture",
      "label": "Portal-only postlecture",
      "source_id": "GU-POD-2020-PORTAL-SPECIAL",
      "local_availability": "missing_not_locally_mined",
      "current_row_status": "missing_component",
      "useful_for_batch": true,
      "accepted_receipt": false
    }
  ],
  "local_starter_rows": {
    "useful": true,
    "accepted_receipts": false,
    "source": "sources/claim-ledger-v1-draft.md",
    "anchors": [
      "four_flavors",
      "observation_split",
      "observerse",
      "U^14 = met(X^4)",
      "pi_projection_operator",
      "base_observerse_distinction",
      "Sector_I_replacement_recovery",
      "pullback_language",
      "fourteen_dimensional_framing",
      "minimal_assumption_methodology"
    ]
  },
  "query_plan": [
    {
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "query_terms": [
        "observerse",
        "Shiab",
        "projection",
        "pi",
        "codomain",
        "selector",
        "target",
        "source",
        "parent",
        "witness",
        "lower-order",
        "rigidity",
        "Sector I",
        "replacement",
        "recovery",
        "pullback"
      ],
      "accept_only_if": "source-forced codomain selector for K_IG",
      "starter_rows_are_accepted_receipts": false
    },
    {
      "family": "RS",
      "required_object": "source.action_or_operator for d_RS,-1",
      "query_terms": [
        "Rarita",
        "spinor",
        "spin 3/2",
        "gravitino",
        "action",
        "operator",
        "differential",
        "variation",
        "Noether",
        "BRST",
        "gauge",
        "complex",
        "rolled",
        "ship-in-a-bottle"
      ],
      "accept_only_if": "source action operator Noether or BRST rule checking against d_RS,-1",
      "starter_rows_are_accepted_receipts": false
    },
    {
      "family": "QFT",
      "required_object": "P_fin^b: F_phys^b(O) -> K_b",
      "query_terms": [
        "finite",
        "quantization",
        "local",
        "physical",
        "projector",
        "projection",
        "quotient",
        "representative",
        "mode",
        "Hilbert",
        "state",
        "algebra",
        "covariance",
        "pullback"
      ],
      "accept_only_if": "finite source projector or extraction map with source and codomain",
      "starter_rows_are_accepted_receipts": false
    },
    {
      "family": "DGU_VZ",
      "required_object": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
      "query_terms": [
        "action",
        "operator",
        "equation",
        "Euler",
        "Lagrange",
        "Euler-Lagrange",
        "field equation",
        "D_GU",
        "epsilon",
        "theta",
        "alpha",
        "principal symbol",
        "coefficient",
        "projector",
        "variation",
        "inhomogeneous",
        "Vafa-Witten",
        "VZ"
      ],
      "accept_only_if": "actual GU action operator or EL data for D_GU^epsilon 0/1",
      "starter_rows_are_accepted_receipts": false
    }
  ],
  "candidate_row_schema": [
    "batch_id",
    "source_id",
    "source_component",
    "component_availability",
    "family",
    "required_object",
    "query_terms",
    "exact_locator",
    "exact_fragment_or_absence",
    "emitted_object_type",
    "emitted_formula_or_rule",
    "starter_row_used",
    "starter_row_is_accepted_receipt",
    "target_data_seen",
    "import_status",
    "acceptance_status",
    "proof_restart_allowed",
    "promotion_allowed"
  ],
  "negative_row_requirements": {
    "complete_acquired_source_component": true,
    "declared_component_scope": true,
    "query_log_preserved": true,
    "family_specific_terms_and_notation_variants_preserved": true,
    "inspected_hits_and_false_positive_decisions_preserved": true,
    "exact_required_object_absence_recorded": true,
    "target_import_excluded": true,
    "promotion_allowed": false,
    "proof_restart_allowed": false
  },
  "strongest_positive_result": "Oxford/Portal is the best official source surface for first exact-locator mining and the family-by-family batch is specified.",
  "first_exact_obstruction": "No Oxford/Portal component currently has an exact local locator whose fragment emits any of the four required family objects with an emitted formula or rule.",
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "negative_receipt_count": 0,
  "portal_only_preface_postlecture_locally_mined": false,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "no_claim_promotion": true,
  "no_claim_promotions": {
    "oxford_starter_rows_are_accepted_receipts": false,
    "portal_preface_postlecture_locally_mined": false,
    "IG_K_IG_selected": false,
    "RS_d_RS_minus_1_source_derived": false,
    "QFT_P_fin_b_supplied": false,
    "DGU_actual_operator_identified": false,
    "proof_restart_allowed": false,
    "VZ_evasion_closed": false,
    "dark_energy_FLRW_rank_generation_QFT_CHSH_recovered": false
  },
  "forbidden_promotions": [
    "Oxford starter rows are accepted receipts",
    "Portal Special preface/postlecture is locally mined",
    "IG selects K_IG",
    "RS source-derived d_RS,-1 is established",
    "QFT P_fin^b is supplied",
    "DGU/VZ actual D_GU^epsilon 0/1 is identified",
    "Any Oxford/Portal component globally lacks the required object without complete component scope and query log",
    "Proof restart is allowed",
    "VZ evasion dark-energy FLRW rank generation finite-QFT covariance rho_AB CHSH or Bell recovery is derived"
  ],
  "next_meaningful_step": "Execute OxfordPortalExactLocatorBatch_V1 over Oxford transcript, shared Portal Oxford substance, and acquired Portal-only preface/postlecture components before any proof restart."
}
```
