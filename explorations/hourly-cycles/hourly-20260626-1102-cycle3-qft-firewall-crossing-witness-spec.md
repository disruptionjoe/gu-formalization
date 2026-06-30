---
title: "Hourly 20260626 1102 Cycle 3 QFT Firewall-Crossing Witness Spec"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 3
lane: 5
doc_type: "frontier_run_lane_artifact"
artifact_id: "QFTFirewallCrossingWitness_1102_C3_L5_V1"
verdict: "closed_witness_spec_defined_and_applied_no_firewall_crossing_witness_present"
owned_path: "explorations/hourly-20260626-1102-cycle3-qft-firewall-crossing-witness-spec.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 3 QFT Firewall-Crossing Witness Spec

## 1. Verdict

Verdict: **closed witness spec with negative current application**.

This artifact defines:

```text
QFTFirewallCrossingWitness_V1
```

It is the exact witness shape that would be required to cross the cycle-2
host/schema-to-authority firewall without smuggling target-side QFT data. The
spec is defined and applied to the current repo state. No witness is present.

Current decision state:

```text
witness_spec_defined: true
witness_spec_applied: true
firewall_crossing_witness_present: false
source_context_locator_found: false
cover_vocabulary_authorized: false
admissibility_authority_found: false
qft_cover_declaration_retry_allowed: false
local_records_unlocked: false
brsch_checks_unlocked: false
carrier_work_allowed: false
target_import_used: false
claim_status_change: false
```

This does not repeat the QFT source search. It consumes the prior negative
receipts and the cycle-2 firewall, then states the exact positive witness that
would be needed to invalidate that local firewall in a future run.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the anti-inflation discipline used by this
witness spec:

```text
compatibility is not derivation
target data must not be hidden inside reconstruction
failed gates must not be rescued by optimism
```

`process/runbooks/five-lane-frontier-run.md` supplies the local verdict and
frontier-run discipline:

```text
hosted structure is not selected structure
schema/verifier objects close only the gate they actually prove
do not let "hosted by" become "selected by"
```

`hourly-20260626-1003-cycle3-qft-context-locator-authority-receipt.md`
directly records the prior receipt failure:

```text
source_context_locator_found: false
cover_vocabulary_authorized: false
admissibility_authority_found: false
qft_cover_declaration_retry_allowed: false
local_records_unlocked: false
brsch_checks_unlocked: false
carrier_work_allowed: false
```

It also identifies the first obstruction:

```text
QFTSourceContextLocatorAndCoverAuthorityReceipt_V1
  .source_context_locator_with_cover_authority_absent
```

`hourly-20260626-1102-cycle1-qft-locator-authority-receipt-retry.md` reruns
the receipt with stricter candidate classes and finds no row classified as:

```text
source_locator_and_authority
source_locator_only
authority_only
```

Its strongest positive result is only negative infrastructure:

```text
host_infrastructure
schema_or_verifier_only
downstream_target_selector
```

`hourly-20260626-1102-cycle2-qft-host-schema-authority-firewall.md` converts
that negative receipt into a repo-local governance firewall. It directly
records:

```text
generic_host_as_locator_allowed: false
schema_as_cover_authority_allowed: false
brsch_as_cover_generator_allowed: false
firewall_crossing_witness_present: false
```

It also names the first missing object:

```text
SameContextSourceLocatorAuthorityEdge_QFT_V1
```

Narrow current-state checks for this lane were limited to witness existence,
not a new QFT source search. The owned output file did not exist before this
artifact, no cycle-3 QFT witness artifact was present, and the only exact
`firewall_crossing_witness` hit in `explorations/*.md` was the cycle-2 negative
record above.

## 3. Firewall-Crossing Witness Spec And Field Table

Definition:

```text
QFTFirewallCrossingWitness_V1 is an inhabited source-side certificate that:
  1. locates the QFT source context to be covered;
  2. authorizes cover vocabulary for that same located context;
  3. supplies source-side admissibility authority for cover formation before
     local records, BrSch checks, transition generators, carrier work, local
     algebra, anomaly checks, SM matching, Bell/CHSH, EFT, or target physics;
  4. ties locator, vocabulary authority, and admissibility authority by an
     explicit same-context dependency edge;
  5. includes a dependency DAG with no forbidden downstream or target edge;
  6. carries anti-smuggling fields that reject host-only, schema-only,
     verifier-only, guard-only, and downstream-selected constructions.
```

Acceptance predicate:

```text
accept QFTFirewallCrossingWitness_V1 only if all required fields are inhabited
by source-side rows or source-authorized row pairs, all authority fields type
over the same located QFT context, and target_import_used is false.
```

Rejection predicate:

```text
reject if any required field is supplied only by generic host notation,
Obj_QFTBr field names, BrSch/Mor_schema, packet verifier contracts,
anti-smuggling policy alone, local-record success, carrier viability, local
algebra, anomaly, SM, Bell/CHSH, EFT, or target-physics behavior.
```

| witness field | required content | verifier check | current repo result |
|---|---|---|---:|
| `witness_id` | stable id for this exact witness instance | unique and attached to a source-side packet | spec only, no instance |
| `source_scope` | exact source family or source-authorized artifact scope searched | prior to cover declaration, local records, BrSch checks, carrier work, and target tests | source scope exists in prior receipts, but no positive witness |
| `same_context_source_locator.source_row_id` | source row that locates the QFT context to be covered | row is not host notation and not a schema placeholder | absent |
| `same_context_source_locator.source_handle` | citation or repo-local source handle | handle resolves to the row that supplies the locator | absent |
| `same_context_source_locator.located_context` | the QFT source context over which a cover will be formed | context is mathematical and source-located, not downstream-selected | absent |
| `same_context_source_locator.context_type` | type of the located context | type is specific enough to type domains, overlaps, and restrictions | absent |
| `same_context_source_locator.qft_relation` | relation between located context and intended QFT branch/context | relation is source-side, not inferred from later QFT success | absent |
| `cover_vocabulary_authority.authority_row_id` | source row or source-authorized dependency edge licensing cover vocabulary | row authorizes vocabulary over the same located context | absent |
| `cover_vocabulary_authority.domain_kind` | allowed domain/context kind for `U_i` | every domain lives over `located_context` | absent |
| `cover_vocabulary_authority.index_kind` | allowed index-set kind for `I` | `I` is licensed by authority, not chosen by convenience | absent |
| `cover_vocabulary_authority.overlap_kind` | allowed `U_ij`, `U_ijk`, and higher-overlap vocabulary if needed | overlaps are source-typed, not formal placeholders | absent |
| `cover_vocabulary_authority.restriction_kind` | allowed restriction-map vocabulary | restriction maps are source-typed over the same context | absent |
| `admissibility_authority.source_rule_id` | source-side rule admitting cover formation | rule precedes local records, BrSch, carriers, and targets | absent |
| `admissibility_authority.cover_predicate` | predicate that decides when a source cover may be formed | predicate is positive authority, not merely a rejection guard | absent |
| `same_context_edge.edge_id` | explicit edge tying locator, vocabulary authority, and admissibility authority | all three roles type over the same located context | absent |
| `dependency_DAG.nodes` | nodes for locator, vocabulary authority, admissibility authority, precedence, and guards | complete enough to audit provenance | no positive DAG instance |
| `dependency_DAG.allowed_edges` | source-side dependency edges among witness fields | no edge to downstream success or target data | no positive DAG instance |
| `dependency_DAG.forbidden_edges` | explicit forbidden edge list | rejects local records, BrSch success, carrier viability, local algebra, anomaly, SM, Bell/CHSH, EFT, and target physics as selectors | guard present only as negative discipline |
| `anti_smuggling.forbidden_input_tags` | tags for host-only, schema-only, verifier-only, guard-only, downstream-target, target-import | every candidate field declares and passes tag checks | guard present only as negative discipline |
| `anti_smuggling.target_import_receipt` | receipt that no field is selected by target data | must be `target_import_used: false` with a field-level audit | negative guard present, no positive witness |
| `prelocal_lock_receipt` | confirmation that cover declaration, local records, BrSch checks, and carrier work remain locked until witness acceptance | lock must not be used as positive authority | present as lock discipline |
| `semantic_lift` | permission to retry `QFTAdmittedSourceCoverDeclarationCandidate_V1` with actual `I`, `U_i`, cover relation, overlaps, and restrictions | emitted only after all witness fields pass | not achieved |

Minimum crossing condition:

```text
source_context_locator_found = true
cover_vocabulary_authorized = true
admissibility_authority_found = true
same_context_edge_present = true
dependency_DAG_forbidden_edge_free = true
target_import_used = false
```

The current repo satisfies only the negative guard and lock fields. Those are
necessary for a witness verifier, but they are not the witness.

## 4. Strongest Positive Construction Attempt

The strongest construction available without target import is:

```text
host layer:
  X, Y = Met(X), pi: Y -> X, local opens O subset X

schema layer:
  Obj_QFTBr fields, including source_locator and domain_boundary_data

verifier layer:
  BrSch, Mor_schema, packet verifier contracts, candidate cover verifier

guard layer:
  no-target-import discipline, forbidden-input tags, dependency-DAG screens

attempted firewall crossing:
  host layer supplies same_context_source_locator
  schema layer supplies cover_vocabulary_authority
  verifier/guard layer supplies admissibility_authority
```

This is the strongest construction because it uses only repo-local objects and
does not appeal to local-QFT success, anomaly cancellation, SM fit, Bell/CHSH,
EFT, carrier viability, or target physics.

It still fails. The host layer can make a future source context type-check, but
it does not state that the QFT context to be covered has been source-located.
The schema layer lists fields a future record must contain, but field names do
not authorize the cover vocabulary. `BrSch` and packet verifiers can reject or
check supplied records, but they do not generate a source cover and do not
positively admit cover formation. The guard layer prevents bad crossings, but a
guard is not positive authority.

Strongest positive result:

```text
host_schema_verifier_guard_stack_available: true
firewall_crossing_witness_present: false
```

## 5. First Exact Obstruction Or Missing Object

The first exact obstruction is:

```text
QFTFirewallCrossingWitness_V1.same_context_source_locator_authority_edge_absent
```

Expanded failure order:

```text
1. no admitted same-context source locator row locates the QFT source context
   to be covered;
2. no source row or source-authorized edge authorizes cover vocabulary over
   that same context;
3. no source-side admissibility rule admits cover formation before local
   records, BrSch checks, transition generators, carrier work, or target tests;
4. no explicit edge ties locator, vocabulary authority, and admissibility
   authority to one source-located context;
5. no positive dependency DAG instance exists for the witness;
6. only negative anti-smuggling and lock discipline is present;
7. no admitted cover declaration retry is allowed;
8. local records, BrSch checks, transitions, descent cocycle, hidden key,
   carrier work, local algebra, anomaly, SM, Bell/CHSH, and EFT remain locked
   as source evidence.
```

The first missing object can be named more constructively as:

```text
SameContextSourceLocatorAuthorityEdge_QFT_V1
```

It must be a source-side edge or source-authorized row pair, not a host,
schema, verifier, or downstream-success edge.

## 6. Constructive Next Object

Build:

```text
QFTFirewallCrossingWitnessCandidatePacket_V1
```

Minimum fields:

```text
source_scope:
  exact source family or source-authorized repo artifact scope;
  statement that the packet is prior to cover declaration, local records,
  BrSch checks, transition generation, carrier work, local algebra, anomaly,
  SM, Bell/CHSH, EFT, and target physics.

same_context_source_locator:
  source_row_id;
  source/citation handle;
  located QFT context;
  mathematical context type;
  proof that the row is not generic host notation or schema vocabulary.

cover_vocabulary_authority:
  authority_row_id or source-authorized dependency edge;
  allowed domain/context kind;
  allowed index-set kind;
  allowed overlap and restriction vocabulary;
  proof that vocabulary is authorized over the same located context.

admissibility_authority:
  source_rule_id;
  positive predicate admitting cover formation;
  proof that the rule precedes local records, BrSch checks, carriers, and
  target tests.

same_context_edge:
  edge_id;
  source-side proof that locator, vocabulary authority, and admissibility
  authority all type over the same located QFT context.

dependency_DAG:
  nodes for every witness field;
  allowed source-side edges;
  forbidden-edge audit;
  no edge to local-record success, BrSch success, transition success, carrier
  viability, local algebra, anomaly, SM, Bell/CHSH, EFT, or target physics.

anti_smuggling_receipt:
  forbidden_input_tags;
  target_import_receipt;
  host/schema/verifier/guard-only rejection receipt;
  downstream-selector rejection receipt.
```

Pass condition:

```text
emit PositiveQFTFirewallCrossingWitness_V1 only if the packet supplies all
minimum fields and classifies at least one source row or source-authorized row
pair as source_locator_and_authority for the same QFT context.
```

Fail condition:

```text
emit NegativeQFTFirewallCrossingWitness_V1 if all candidates remain
host_infrastructure, schema_or_verifier_only, guard_only,
downstream_target_selector, locator_only_without_authority,
authority_only_without_locator, or absent.
```

## 7. Meaning For QFT Cover/Local-Record/Carrier Claims

No QFT cover, local-record, `BrSch`, transition, carrier, local algebra,
state-space, anomaly, Standard Model, Bell/CHSH, or EFT claim is unlocked.

Allowed statement:

```text
The repo has a precise firewall-crossing witness spec and a verifier-ready
field table. It also has host/schema/verifier/guard infrastructure that can
check or host a future witness.
```

Forbidden statement:

```text
Because the witness spec, host geometry, Obj_QFTBr, BrSch, packet verifiers,
or anti-smuggling guards exist, the repo may retry QFT cover declaration or
proceed to local records, BrSch checks, carrier work, local algebra, anomaly,
SM, Bell/CHSH, EFT, or target physics as source-selected.
```

Lock table:

| object or lane | current status | reason |
|---|---:|---|
| `QFTAdmittedSourceCoverDeclarationCandidate_V1` retry | locked | no firewall-crossing witness |
| source cover declaration | locked | no same-context locator plus cover authority |
| local records `r_i in Obj_QFTBr(U_i)` | locked | no admitted `I`, `U_i`, overlaps, or restrictions |
| `BrSch` checks | locked | verifier has no admitted local-record inputs |
| transition generator and field transport | locked | no source cover, overlaps, restrictions, or local records |
| descent cocycle and hidden-key emission | locked | no source action or admissibility predicate |
| carrier and local groupoid work | locked as source evidence | carrier viability is a downstream selector |
| local algebra, QFT state, anomaly, SM, Bell/CHSH, EFT | locked as source evidence | target-side success cannot cross the firewall upstream |

No claim status changes follow from this artifact.

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain:

```text
descent-quotient + provenance-verifier
```

Forbidden shortcut:

```text
Do not promote generic host geometry, source indices, open-cover notation,
Obj_QFTBr fields, BrSch, Mor_schema, packet verifiers, anti-smuggling guards,
local records, BrSch success, transitions, carrier viability, local algebra,
anomaly, SM, Bell/CHSH, EFT, or target physics into a QFT firewall-crossing
witness.
```

First invariant:

```text
same_context_firewall_crossing_invariant:
  the source context locator, cover vocabulary authority, and admissibility
  authority all type over one source-located QFT context, and the dependency
  DAG has no forbidden edge to host-only, schema-only, verifier-only,
  guard-only, downstream-success, or target-import selectors.
```

Kill condition:

```text
Kill a proposed QFTFirewallCrossingWitness_V1 if:
  1. the locator is generic host notation;
  2. the locator is only a field named source_locator;
  3. the vocabulary authority is only cover notation or schema vocabulary;
  4. BrSch, Mor_schema, or a packet verifier is used as a cover generator;
  5. an anti-smuggling guard is treated as positive source authority;
  6. locator and authority are not tied by a source-side same-context edge;
  7. the admissibility rule does not precede local records, BrSch checks,
     carriers, and target tests;
  8. any witness field is selected because local-QFT, anomaly, SM, Bell/CHSH,
     EFT, carrier, local algebra, or target behavior works.
```

## 9. Certificate/Witness Shape

| certificate component | required content | current result |
|---|---|---:|
| public inputs | read-first posture, runbook, prior QFT locator-authority receipts, cycle-2 firewall, narrow witness-existence check | present |
| witness | source locator, cover vocabulary authority, admissibility authority, same-context edge, dependency DAG, anti-smuggling receipt | absent |
| verifier predicate | field completeness, same-context typing, source-side authority, precedence before downstream work, forbidden-edge-free DAG | specified |
| semantic lift | permission to retry admitted QFT cover declaration with actual `I`, `U_i`, cover relation, overlaps, restrictions | not achieved |
| anti-smuggling guard | rejects host-only, schema-only, verifier-only, guard-only, downstream-selected, and target-import candidates | present as guard |
| lock receipt | cover declaration, local records, BrSch checks, and carrier work remain locked until witness acceptance | present |
| kill condition | generic host locator, schema authority, BrSch-as-generator, guard-as-authority, missing same-context edge, downstream selector | triggered |

Certificate result:

```text
witness_spec_defined: true
witness_spec_applied: true
certificate_inhabited: false
firewall_crossing_witness_present: false
first_failed_field: same_context_source_locator_authority_edge
semantic_lift_to_cover_declaration: false
```

## 10. JSON Summary

```json
{
  "artifact_id": "QFTFirewallCrossingWitness_1102_C3_L5_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 3,
  "lane": 5,
  "artifact_path": "explorations/hourly-20260626-1102-cycle3-qft-firewall-crossing-witness-spec.md",
  "verdict_class": "closed_witness_spec_defined_and_applied_no_firewall_crossing_witness_present",
  "witness_spec_defined": true,
  "witness_spec_applied": true,
  "firewall_crossing_witness_present": false,
  "source_context_locator_found": false,
  "cover_vocabulary_authorized": false,
  "admissibility_authority_found": false,
  "same_context_edge_present": false,
  "dependency_DAG_positive_instance_present": false,
  "dependency_DAG_forbidden_edge_free": false,
  "anti_smuggling_guard_present": true,
  "qft_cover_declaration_retry_allowed": false,
  "local_records_unlocked": false,
  "brsch_checks_unlocked": false,
  "carrier_work_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "claim_status_consistency_triggered": false,
  "current_state_check_repeated_qft_source_search": false,
  "host_schema_verifier_guard_stack_available": true,
  "first_exact_obstruction": "QFTFirewallCrossingWitness_V1.same_context_source_locator_authority_edge_absent",
  "first_missing_object": "SameContextSourceLocatorAuthorityEdge_QFT_V1",
  "constructive_next_object": "QFTFirewallCrossingWitnessCandidatePacket_V1",
  "retry_after_positive_witness": "QFTAdmittedSourceCoverDeclarationCandidate_V1",
  "terrain": [
    "descent-quotient",
    "provenance-verifier"
  ],
  "forbidden_shortcut": "promote_host_schema_verifier_guard_downstream_success_or_target_physics_into_QFT_firewall_crossing_witness",
  "first_invariant": "same_context_firewall_crossing_invariant_with_source_locator_cover_vocabulary_authority_admissibility_authority_and_forbidden_edge_free_dependency_DAG",
  "kill_condition": "reject_if_locator_is_host_or_schema_placeholder_vocabulary_is_schema_only_BrSch_or_verifier_used_as_generator_guard_used_as_authority_same_context_edge_missing_admissibility_not_prelocal_or_downstream_success_selects_fields"
}
```
