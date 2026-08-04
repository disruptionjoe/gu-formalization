---
artifact_type: process
status: process
doc_type: process-note
created: 2026-08-04
tier: process
routing: non-routing
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
title: "Wave-discipline gates: the disposition schema, the Layer-0 fork registry, and the dated cutover"
scope: "Explains two process gates and one registry. Creates no claim, verdict, grade, priority, lane movement, or external-datum entry. It records process mechanics only."
---

# Wave-discipline gates (2026-08-04)

Two gates and one registry, built from the 2026-08-04 program-efficiency
council's guard-metric recommendation (its §5.5) and its re-aiming of the pre-
and post-review (§7).

- `process_gates/wave_disposition_schema_audit.py`
- `process_gates/fork_depth_audit.py`
- `lab/process/layer0-fork-registry.yaml`

## What they are for

The council found the program **converging and accelerating**, with one large
measured loss that no wave review could have caught: the highest-fan-out Layer-0
fork in the program — which real Clifford algebra the source actually uses —
was determined at **Wave K, after waves D–J had stacked seven constructions on
the other horn**. Every one of those waves passed its own hostile review. The
defect was in the **queue**, and nothing in the process looked at the queue.

The same window contains two smaller versions of the same shape: three probes
attacking one quantity on one day with three different selectors, when nobody
had computed the size of the space being searched; and one wave introducing a
free object (`J_red`, "source-silent") that four waves later still had no owner.

All three are invisible in a wave's own artifact because a wave is not currently
required to say what it assumed, how large a space it searched, or what it left
un-owned. These gates make it say so.

## Gate A — `wave_disposition_schema_audit.py`

**What it enforces.** Four frontmatter fields on every wave/cycle disposition
artifact:

```yaml
fork_assumed: REAL-CLIFFORD-FORM        # or a list, or `none`
search_space_dim: 200                   # int, expression, or `not_computed`
search_space_dim_reason: "..."          # required iff not_computed
free_object_delta: -1                   # introduced minus retired
residue_touched:                        # or `none`
  - "A4-DE-KINETIC-NORMALIZATION: T3"
  - {id: M-H7, grade: T4}
```

These are the council's **PRE-1** (what fork does this wave assume without
deciding), **PRE-2** (what is the dimension of the space it searches, and can it
be computed before enumeration), **PRE-3** (does it introduce a new un-owned
object) and **POST-1/POST-2** (the free-object delta and the T-grade of every
conditional match touched), made mechanical.

`free_object_delta` is the number the council singled out: *the one quantity
that cannot be improved by writing more artifacts.* Sustained `≥ 0` across three
or more waves is the circling signature.

**The discovery rule** — stated in full in the script docstring, because the
corpus has no single naming convention. A git-tracked `.md` under
`explorations/` is in scope when **any** of:

1. it sits directly under `explorations/cycle-gates-and-audits/` and its
   basename contains `-disposition-` or `-rebase-` (14 files; three of them
   carry no frontmatter at all);
2. its frontmatter declares a wave `doc_type` (`resolver-wave-gate` today; 4
   files);
3. its frontmatter carries a `route_disposition:` key (27 files) — the honest
   structural signal, since a document that dispositions a named wave gate is a
   wave disposition whatever it is filed as. This clause catches the top-level
   `explorations/resolver-wave-*` and `explorations/k77-wave2-*` run artifacts
   that clause 1 misses.

Union at build time: **30 artifacts**. The gate fails if any clause stops
matching, so the rule cannot silently narrow.

## The grandfathering cutover

Every artifact in the corpus predates the schema. A gate that failed on all 30
would be turned off within a day, so the cutover is dated:

> **`SCHEMA_CUTOVER = 2026-08-05`.** Artifacts whose effective creation date is
> on or after that date must comply. Earlier artifacts are reported as `legacy`
> and never fail.

At build time that is **30 legacy / 0 in scope**, and the gate runs green. The
legacy count is printed on every run so the backlog is visible rather than
permanent; it drops as old dispositions are retro-filled, and nothing forces
that work to happen at once.

Two properties keep the cutover from being a loophole:

- **Legacy opt-in is still checked.** A legacy artifact may omit the schema
  entirely, but a field it *does* declare must be well-formed. Early adoption
  cannot land malformed.
- **Backdating does not buy an exemption.** The effective creation date is the
  **maximum** of every date the artifact declares about itself (frontmatter
  `created:`/`date:`, the trailing `YYYY-MM-DD` in the filename) and — when git
  history is present and not shallow — the date the file was first committed.
  Naming a new file `...-2026-08-04.md` does not make it legacy. The git leg is
  skipped on shallow checkouts (CI clones at depth 1, where every file looks
  added at HEAD) and the gate prints which mode it ran in rather than assuming
  silently.

If no date is derivable at all, the gate **fails closed** — the cutover cannot
be applied, so it refuses to grandfather by default.

## Gate B — `fork_depth_audit.py` and the registry

**The registry** (`lab/process/layer0-fork-registry.yaml`) is the queue surface:
one row per Layer-0 fork, with a stable id that dispositions cite. It currently
holds **12 forks, 10 open and 2 settled** — the pack's live forks (carrier
split, ambient signature, the two in-repo 2+1s, kinematic-vs-physical carrier),
the four cheap forks the council named as live and unscheduled (`eps` character,
section-vs-observerse, `J_red` ownership, vertical Frobenius trace), two forks
from the GEOMETER-VS-PHYSICS-OBJECTS table that are explicitly unsettled
(generation-count codomain, the number 14), and the two settled ones:

- **`REAL-CLIFFORD-FORM`** — `Cl(7,7) = M128(R)` vs `Cl(9,5) = M64(H)`. Settled
  to `(7,7)` at **Wave K, 2026-08-04**, by deriving the real form from the
  source's own arithmetic rather than choosing it; `(9,5)` is demoted to a
  conditional comparator with an explicit import ban, since the two algebras are
  not real-isomorphic and complexification carries neither the real pairing nor
  the right-`H` structure. The row carries a `measured_cost:` field recording
  that this was settled **late**, at seven stacked waves. The gate asserts that
  field is present and stated — the loss stays legible in the record.
- **`IMPOSTER-LABEL-AB`** — settled to **A**, 2026-08-03, confidence 0.90, by
  filed hostile field-specialist review (J5). Label-level only; the block is
  kinematically vectorlike and `PH-K1-PHYSICAL` stays open.

Note the Layer-0 split the registry preserves: `REAL-CLIFFORD-FORM` is settled,
`SIGNATURE-AMBIENT` ((9,5) vs (7,7) as the ambient signature) is **not**. They
are different objects and the pack treats "(9,5)" as a homonym here.

**The depth counter.** The gate reads every `fork_assumed:` declaration,
resolves it against the registry, and counts how many dispositions have stacked
on each still-**open** fork. Past `fork_stack_threshold` (registry-configured,
default **3**), each further disposition must carry:

```yaml
fork_stack_acknowledged: "why proceeding on an undetermined horn is still the
  right call, and what it costs if the other branch is right"
```

Accepted shapes: a bare reason string (covers every over-threshold fork in that
disposition), a mapping of fork id → reason, or a mapping/list with
`fork`/`forks` and `reason` keys. A checkbox word (`yes`, `noted`, `tbd`, …) or
anything under 12 characters is rejected — the field is a reason, not a tick.

**This is not a refusal.** Proceeding on an undetermined fork stays allowed;
sometimes it is correct, and the program has no way to force a fork closed. What
becomes mandatory is *saying so, in the artifact, with a reason*, so the cost
lands in the record instead of surfacing seven waves later.

**"Consecutive", defined.** For an open fork nothing has broken the stack — the
fork was never settled at any point in the sequence — so every disposition that
declared it belongs to one unbroken run, and depth is simply the count in date
order. Working on a different fork in between does **not** reset the counter; a
counter that resets when you spend a day elsewhere measures nothing. **Settling
the fork is what clears it**, which is the intended exit.

At build time no disposition declares a fork yet (the whole corpus is legacy),
so every depth is 0 and the gate runs green. It starts biting with the first
post-cutover wave.

## How to add a fork to the registry

1. **Type it first.** A fork row is a Layer-0 typing act: two or more named
   horns for one object, such that a result derived under one horn does not
   silently transfer to the other. If you cannot state the horns, you have a
   question, not a fork.
2. **Pick a stable id.** `UPPER-KEBAB`, unique, and permanent — dispositions
   cite ids, so titles may be reworded freely and ids may not be renamed.
3. **Fill the required keys:** `id`, `title`, `horns` (≥ 2), `status`
   (`open`|`settled`), `fan_out` (say how wide, in words), `sources` (≥ 1
   repo-relative path that resolves — the gate checks).
4. **If it is settled**, additionally give `settled_side`, `settled_how` (how,
   not merely that), `settled_at` (a date), and `settled_by` (the artifacts that
   did the work, all resolving). An `open` row may not carry any of those four —
   half-settled rows are rejected, because a half-settled fork is exactly what
   an agent reads as settled.
5. **If the fork was settled late**, record `measured_cost:` — what was built on
   the losing horn before it was decided. That is the number this whole
   mechanism exists to make visible.
6. **Run** `PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python
   process_gates/fork_depth_audit.py`.

A row in `REQUIRED_FORK_IDS` (in the gate) cannot be deleted from the registry
without editing the gate — removing a live fork has to be a deliberate act.

## Boundaries

Both gates read files as data, execute nothing, and evaluate no mathematics. A
green run says the disposition record is shaped correctly and the queue's fork
stacking is declared; it says nothing about whether any wave is correct, and it
moves no claim status, canon verdict, proof status, grade, priority, lane, or
public posture. Whether a settlement recorded in the registry is *right* is the
settling artifact's business; the registry records the typing and the pointer.

Both gates are picked up by `.github/workflows/python-ci.yml` automatically —
that workflow already loops over `process_gates/*.py`, so no workflow edit was
needed.
