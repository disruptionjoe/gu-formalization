---
title: "Conditional-Ledger Advancement — delta index"
status: active_research
doc_type: overview
updated_at: "2026-08-15"
---

# Conditional-ledger advancement — delta index

Artifacts of the Joe-directed channel `conditional_ledger_advancement`. The
channel **never edits the sequential ledger**: every file here is a
**versionless delta or assessment against an exact base revision**, for the
canonical owner to disposition. Nothing here has moved a ledger row.

The channel's other standing rule is that a grant is never laundered into a
derivation. A row advances carrying its named grant as an explicit condition,
or it does not advance. `DERIVED_CONDITIONAL -> DERIVED` has been proposed once
in this channel and was **refused** by the executing agent as laundering.

## Deltas, base revision `a148ed80` (ledger `v0.258`, 84 rows / 82 active)

| id | scope | outcome | certificate |
|---|---|---|---|
| `la1` | embedding cascade + zero-grant candidates | **0 verdicts moved.** Group A already banked; the embedding grant is worth **0 bits**; six field-level migrations proposed | 36/36 |
| `la2` | `AC-A1` cascade | **1 verdict advance**, conditional. Briefed grant **rejected as tautologous**; `AC-A2`/`AC-A3` gain a *declared* condition | 65/65 |
| `la3` | chiral-16 shadow | **0 verdicts moved**, correctly. Routing verdict `CONVENTIONAL_COMPARATOR`; the grant's chirality clause is **exactly inert** | 41/41 |
| `la4` | REPRESENTATION axis, 35 rows | **13** independent grants; a **one-vertex cut reaching 28 of 29** open rows | 37/37 |
| `la5` | ANOMALY_CONSISTENCY axis, 26 rows | **7** handles; **11 rows no grant can ever move**; 5 unknowns, 2 of them physics | 127/127 |
| `la6` | LAGRANGIAN axis, 21 rows | **12** DOF but a **unique 2-object cover**, of which exactly **one is constructible** | 130/130 |

## Ledger-wide result

**82 rows resolve to 32 formal degrees of freedom** (13 + 7 + 12). More
sharply: LA-4's representation cut vertex and LA-6's cover object `A` are the
**same object** — the operative completed second action — independently
identified by two agents using independently declared vocabularies, and
certified on `LT-SM6` by exact substring. It reaches **28 of 29** on
REPRESENTATION and **18 of 20** on LAGRANGIAN.

The practical consequence is that the ledger is not a backlog of independent
items. It is largely one construction with a very large fan-out, and partial
grants buy close to nothing.

## Provenance correction

**`la6`'s two files are committed under `f93a596c`, whose message describes the
anomaly axis (`la5`).** The parent staged the whole directory while the
Lagrangian agent was still writing, so its output was swept into the preceding
commit. `d9451294` then carried `la4` alone. No content is lost or altered and
no history was rewritten; this note is the correction of record.

The general hazard is recorded because it recurred: **staging a directory while
a concurrent writer is active mis-attributes that writer's output.** Stage
explicit paths.

## Known reproducibility note

`la4-representation-axis-incidence-probe.py` resolves the ledger by relative
path and must be run from the repository root. The other probes run from
either location.
