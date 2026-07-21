---
title: "P-LATTICE-SWEEP admission: wake satisfied, compiler blocked on axis schema"
status: active_research
doc_type: exploration
created: 2026-07-21
run_ref: RUN-20260721-033643-repository-work-cycle-cai-hourly
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
outcome: P-LATTICE-SWEEP-BLOCKED-PARAMETERIZATION
test: tests/recovery-contract/construction_space_lattice_admission.py
---

# P-LATTICE-SWEEP admission

## Selection and wake audit

Three owner-local paths were rechecked before work selection:

| path | wake / admission evidence | result |
|---|---|---|
| `P-LATTICE-SWEEP` | round 11 records both `P-K2` and `P-77-REAL-INDEX` resolved | **AWAKE** |
| `P-OBS-LEG` | round 12 records Prediction Packet 1 frozen | **AWAKE**, but lower-ranked Lane 2 / observational work |
| `PRED-CANDIDATE-PACKETS` | portfolio state `READY`, priority 20; PP1 already frozen, PP2/PP3 remain conditional | eligible alternative, but below active Lane 1 construction-space priority 25 |

`P-LATTICE-SWEEP` was therefore selected. This run executes only its bounded
compiler-admission gate. It does not perform a repo-wide search.

## Admission question

Can the current construction-space map be consumed as a target-free candidate
generator over the declared Layer 0 plus L1-L7 template without an agent
inventing missing axis values or compatibility rules?

## Exact inventory

The current map has 11 cells and 44 sector-track slots. Every cell has a prose
`axis_notes` field, but:

- zero of 11 cells has a structured, total `axis_signature`;
- no top-level `axis_domains` enumerate admissible values;
- no top-level `compatibility_constraints` say which cross-axis combinations
  are legal;
- no canonicalization/deduplication rule says when two generated tuples are the
  same construction;
- only C1 says in prose that it has a complete Layer0+L1-L7 signature, while
  the other cells are expressed as partial deltas from C1;
- the protocol calls this a "six-axis template" while listing Layer 0 and
  L1-L7. The names are usable research prose, but the cardinality/nomenclature
  must be frozen before becoming a compiler schema.

The map is an effective human coverage ledger. It is not yet a generative
grammar.

## Why prose expansion is forbidden

Filling omitted axes from familiar physics defaults would silently choose the
conventional construction. Filling them from C1 would silently choose the GU
program-native construction. Both violate the geometer-versus-physics object
discipline. Treating every omitted axis as a wildcard would instead generate
combinations that may be type-incompatible and would make the expressiveness
guard meaningless.

The compiler therefore stops before candidate enumeration. This is a
parameterization block, not evidence for or against any construction.

## Minimal unblock packet

The next bounded lattice step is `P-LATTICE-SCHEMA-FREEZE`:

1. freeze the canonical axis names and settle the six-versus-eight naming;
2. enumerate typed domains for each axis, including an explicit
   `program_native | conventional | imported` construction tag where relevant;
3. migrate all 11 cells to total structured signatures, using `unknown` rather
   than inferred defaults;
4. freeze cross-axis compatibility constraints and tuple canonicalization;
5. only then enumerate new tuples and attach a first falsification test at
   birth.

## Disposition

- `P-LATTICE-SWEEP`: `BLOCKED_PARAMETERIZATION` after a successful wake.
- No new construction cell is generated or graded.
- `P-OBS-LEG` remains awake and `PRED-CANDIDATE-PACKETS` remains an eligible
  Lane 2 alternative; neither is executed in this run.
- B5 remains parked at `B5-MIDDLE-SOURCE-GAP`; nothing here supplies or designs
  around its missing differential.
- No claim, canon, verdict, or public posture changes.
