---
artifact_type: council
created: 2026-08-08
subject: "How to integrate lab/process/path-dependencies.yaml so agents actually see it"
verdict: MINIMAL_SOLUTION_IS_THREE_LINES_AND_A_CAP__NOT_LAYER_0__NO_NEW_ROUTINE_GATE
councils: [system, science]
closers: [agent-context-engineer, overbuild-protection]
---

# Council: integrating path dependencies

**The number that decides most of this, measured not assumed:**

```text
process_gates/*.py                        272
named as run every wave (context pack)      3
currently RED and ignored all day           1   (fork_depth_audit)
AGENTS.md mentions "process_gates"          0 times
agent-context-pack.md                     962 lines
PRE-WAVE questions (BINDING)                4
hostile-review charges (BINDING)            3
```

**272 gates exist and about three are alive.** Any proposal that ends in "add a
gate to the run set" is theatre, and the red `fork_depth_audit` proves it: a
*named, binding* gate went red and was reported four times today without being
acted on. Adding a 273rd changes nothing.

---

## System council

**S-1 Agent context engineer.** Agents read `AGENTS.md`, `LANES.yaml`, and the
context pack. **If it is not on that path it does not exist.** But the pack is
already 962 lines and every added line is paid on every session forever. So the
integration must be a *pointer from a surface agents already hit*, not a new
required read. **Verdict: pointer, never a read.**

**S-2 Overbuild protection.** Four risks, all real:
(i) **the 273rd-gate problem** above;
(ii) **receipt rot** — the load-bearing check is "every receipt resolves", which
will break on the next file rename and will be experienced as a chore rather
than a signal;
(iii) **the generated `.md` doubles the surface** and can go stale — a staleness
failure is a maintenance tax that teaches agents to regenerate blindly;
(iv) **unbounded growth** — 4 chains is legible, 40 is another `process_gates/`.
**Verdict: this is one file away from becoming the thing it was built to fix.**

**S-3 Process/gates engineer.** The validator is fine *as a validator*: run it
when the YAML changes, not every wave. That is a pre-commit concern, not a wave
concern. **Do not put it in the routine set.**

**S-4 Onboarding / DX.** A fresh agent's first two minutes are `AGENTS.md`. The
traps are the highest-value content in the repository for a newcomer and the
lowest-value for an expert. That argues for **one line in `AGENTS.md`**, not a
section.

**S-5 Data modeling.** Should this merge into `layer0-fork-registry.yaml`? **No.**
The registry is 468 lines and answers *what are the forks*. This answers *why do
we check*. Merging makes both worse. Cross-link instead.

**S-6 Ops / maintenance.** Nobody will add traps as a standalone ritual.
**It must attach to something that already happens.** Hostile reviews already
*discover* traps — today's three wrong dispositions were each caught by one.
**Filing the trap should be an output of the review, not a separate act.**

---

## Science council

**C-1 Layer-0 semanticist — the load-bearing finding.** **This is NOT Layer 0,
and filing it there would be a category error that creates a homonym in the very
file meant to prevent them.** Layer 0 asks *what does this token mean* — `sigma`
in five senses, `Cl(3,1)` naming opposite algebras. Path dependencies ask *why is
this check worth doing*. Semantics vs justification. Two different objects.
Calling both "Layer 0" is exactly the failure the layer exists to catch.
**Verdict: adjacent to Layer 0, cross-linked, not inside it.**

**C-2 Epistemologist.** The grade vocabulary (`EXACT` / `THEOREM` /
`AUTHOR-STATED` / `CONDITIONAL` / `OPEN`) is *new*, and the repo already grades
artifacts. **Two grading vocabularies is a Layer-0 defect in waiting.** Either
reuse the existing vocabulary or state the mapping. **Unresolved; flagged.**

**C-3 Hostile reviewer.** What breaks it: a chain goes green with rotted
*reasoning* and intact receipts. The gate says so in its docstring, which is
correct and insufficient — **green will be read as verified.** Mitigation: the
`invalidates_if` field is the antidote, and it should be the *first* thing a
reader sees, not the last.

**C-4 Historian / provenance.** Traps duplicate `memory/log.md` and the
improvement register. **But the duplication is the point**: the log is
chronological and the register is work-queued; neither is *indexed by the mistake
an agent is about to make*. Retained, with the overlap named.

**C-5 Prior art.** Three overlapping structures now: the June claim DAG
(bannered today), the fork registry, and this. **Two is the maximum a repo this
size can keep honest.** The June banner is correct; do not create a fourth.

---

## Closing seats: the minimal effective solution

**Agent context engineer + overbuild protection, converged.**

**Do exactly three things. Nothing else.**

1. **One line in `AGENTS.md`**, in the existing read-first block — not a section:
   > Before assuming a fork horn or citing a blocker, check
   > `lab/process/path-dependencies.md` for a chain covering it.

2. **Extend PRE-WAVE Q1, do not add Q5.** Q1 already asks *which fork are you
   assuming*. Append one clause: *"and if a path-dependency chain covers it, name
   the chain."* **Zero new questions.** The binding surface gains a pointer, not
   a burden.

3. **Make trap-filing an output of hostile review.** Charge 3 already emits a
   licensed-edits list. Add: *"if this review found a mistake an agent would
   plausibly repeat, file it as a dated trap."* Traps then accrue from work that
   already happens.

**And one hard constraint, which is the actual overbuild protection:**

> **CAP: 8 chains. Adding a 9th requires retiring one.**

A cap is the only mechanism that has ever worked against the 272-gate failure
mode. It forces the question *is this chain more valuable than the weakest
current one* — which is the question nobody asks when growth is free.

**Explicitly REJECTED, with reasons:**

| proposal | why rejected |
|---|---|
| Add the validator to the routine gate set | 272 gates, ~3 alive. Theatre. |
| Add a 5th PRE-WAVE question | The binding surface is 4 questions; its power is its shortness. |
| File under Layer 0 | Category error — semantics vs justification (C-1). |
| Merge into `layer0-fork-registry.yaml` | Two files answering two questions beats one answering neither (S-5). |
| A section in the context pack | 962 lines already; paid every session forever (S-1). |
| Require chains for every open fork | Backfilled chains have no real traps and would dilute the ones that do. |

**Left unresolved, and named rather than papered over:** the two grading
vocabularies (C-2). That is a genuine Layer-0 risk introduced by this file today,
and it is not fixed by any of the three actions above.
