---
title: "P-LATTICE-SCHEMA-FREEZE: total typed signatures without inferred defaults"
status: active_research
doc_type: exploration
created: 2026-07-21
run_ref: RUN-20260721-043714-repository-work-cycle-cai-hourly
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
outcome: P-LATTICE-SCHEMA-FROZEN
test: tests/recovery-contract/construction_space_lattice_schema_freeze.py
---

# P-LATTICE-SCHEMA-FREEZE

## Outcome

The compiler blocker from `P-LATTICE-SWEEP-ADMISSION` is resolved at schema
grade. The map now has a canonical machine shape, frozen domains, typed
construction-side provenance, explicit compatibility rules, tuple
canonicalization, and a total signature for each of its 11 existing cells.

No new cell was generated or graded in this run.

## Canonical shape and legacy name

The authoritative template resolves the apparent cardinality conflict:

```text
Layer 0 semantic-alignment precondition + seven structural axes L1-L7.
```

“Six-axis” remains the historical protocol name because L1-L6 were the original
hextuple. It is not the current machine cardinality. L7 was ratified later and
Layer 0 is a precondition rather than a peer axis.

Canonical ordered keys are:

```text
[L0, L1, L2, L3, L4, L5, L6, L7]
```

## Domain freeze

Class identifiers are frozen from
`lab/specifications/six-axis/six-axis-template.md`. Each structural axis also
admits `unknown` and `custom`; `custom` requires a justification and evidence
reference before generation. Layer 0 uses its native three-valued domain:
`same_object`, `homonym`, `uncertain`.

Every axis entry carries:

- `class_id` — the frozen domain member;
- `construction_side` — one of `program_native`, `conventional`, `imported`,
  `mixed_explicit`, or `unknown`;
- `relation` — what the old prose actually established: baseline completion,
  inheritance from C1, a declared delta, preservation across the signature
  port, or unknown.

The construction-side tag is part of tuple identity. A same-named
program-native object and conventional object never canonicalize to one cell.

## Conservative migration

All 11 cells now contain all eight ordered keys. The prior map named deltas but
did not supply specialist-checkable class labels. Therefore every L1-L7 class
is migrated as `unknown`, and every L0 value as `uncertain`; the old notes are
preserved as relation metadata only. This is intentionally stricter than
guessing that an omitted axis inherits a familiar default.

The signatures are total as records but remain non-generative. `unknown` and
`uncertain` are tracked work, never wildcards.

## Compatibility and canonicalization

The schema freezes the two canon-owned coupling rules already on record:

1. Sorkin causal-set L1 requires Sorkin causal-order L4.
2. RG/universality L5 requires RG-flow coordination L6.

It also freezes three safety rules already required by repository governance:

- a Layer-0 homonym requires both objects and their relating map;
- an indefinite-Krein L7 requires its superselection and probability rule;
- an unknown/uncertain/custom-without-justification slot is not generative.

Tuple identity is the ordered `(class_id, construction_side)` pair at L0-L7
plus a future `spec_ref` when a custom or refined class needs it. Relation notes,
evidence lists, and sector grades are not identity. Fully specified identical
tuples may deduplicate only after compatibility passes; tuples containing an
unknown do not deduplicate or generate.

## Handoff

The next bounded step is `P-LATTICE-SIGNATURE-RESOLUTION-C1`: resolve the C1
baseline from its manifest into specialist-checkable L0-L7 classes and
construction-side tags, then propagate only explicitly inherited values to
C2/C3/C5/C10. Enumeration remains forbidden until at least one complete tuple
passes the compatibility gate.

`P-OBS-LEG` remains an awake Lane 2 alternative. B5 remains parked at
`B5-MIDDLE-SOURCE-GAP`; the schema does not fill or route around its missing
differential. No claim, canon, verdict, grade, or public posture changes.

