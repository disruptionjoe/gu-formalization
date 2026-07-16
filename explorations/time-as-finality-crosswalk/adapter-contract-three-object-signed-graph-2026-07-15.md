---
title: "Tri-repo adapter contract: GU Gate 2a = TaF T39 = TI E155/E160 are one Z/2 signed-graph object at the consistency level; the value is forgotten orientation"
status: exploration
doc_type: cross-repo-adapter-contract
created: 2026-07-15
grade: "ONE proven adapter contract at CONSISTENCY grade (three independent algorithms agree 720/720; it is Harary's balance theorem). The value/direction is shown to be FORGOTTEN STRUCTURE the shared object cannot carry. Structural, not physical; the cross-repo identity stays Joe-gated; the value stays formal-grade open."
provenance: "Joe, chat 2026-07-15: build the three-object adapter comparison; find the isomorphism or the obstruction."
depends_on:
  - explorations/time-as-finality-crosswalk/gate-pipeline-conclusion-2026-07-15.md
  - explorations/time-as-finality-crosswalk/ti-question-finality-orientation-as-krein-sign-2026-07-15.md
runnable:
  - explorations/time-as-finality-crosswalk/adapter_three_object.py
external_anchors:
  - "GU: Gate 2a (explorations/.../gate2a_f2_consistency.py) -- XOR-SAT on the observer nerve"
  - "TaF: T39 CSP reframing -- binary {-1,+1} CSP; obstruction = parity conflict / negative cycle / signed-graph 2-colourability"
  - "TI: E155 (Ext_S confluent off the opposite-polarity SBP fork) + E160 (A: ExtCat -> B(Z/2))"
  - "TaF T23 IPT: (source, target, map, preserved invariants, allowed losses, obstruction) -- the adapter is an IPT in this exact sense"
verdict: "ISO at consistency level (proven, 3 independent algorithms, Harary). ADAPTER OBSTRUCTION at direction/value level: orientation is forgotten structure. This structurally EXPLAINS W211 (GU's object is undirected, so it CANNOT fix the sign internally) and derives the tri-repo division of labor rather than assuming it."
---

# Tri-repo adapter contract: one signed-graph object, with orientation forgotten

## What was tested

Whether GU Gate 2a, TaF T39, and TI E155/E160 are the **same** ℤ/2 object under an explicit map, or merely
three things that both smell like ℤ/2. Common instance: a **signed graph** (nodes; edges labelled `+1`
agree/same, `-1` disagree/opposite-polarity). Three **independent** algorithms:

- **GU (Gate 2a):** XOR-SAT — potential assignment on a spanning forest, count violated non-tree edges.
- **TaF (T39):** signed-graph balance — BFS 2-colouring, detect parity conflict (negative cycle).
- **TI (E155/E160):** ℤ/2 holonomy — fundamental-cycle loop-products; `[J]=0` in `H^1` iff all trivial.

## Result 1 — ISO at the consistency level (proven)

```
instances: 720 | all-three-agree: 720 | disagreements: 0
```

Across 720 random signed graphs (sizes 20/40/80 x negative-density 0.0-0.5), the three independent algorithms
returned the **identical** balanced/unbalanced verdict **every time**. Controls: triangle `+++` balanced,
`++-` unbalanced, in all three. This is not a coincidence — it is **Harary's balance theorem**:

> signed-graph balance  =  no negative cycle  =  the ℤ/2 1-cocycle is exact (`[J]=0` in `H^1`)
>   =  XOR-CSP satisfiable  =  signed 2-colourable.

So **GU Gate 2a = TaF T39 = TI E155/E160 as one object at the consistency level.** The dictionary:

| role | GU Gate 2a | TaF T39 | TI E155/E160 |
|---|---|---|---|
| node | observer (nerve vertex) | observer site | `Ext_S` object / constraint state |
| ℤ/2 edge label | coupling `J` (agree/disagree) | `{-1,+1}` CSP constraint | edge parity / E160 transport label |
| obstruction | frustrated cycle | negative cycle / parity conflict | non-trivial `H^1` holonomy = SBP fork |
| "consistent" | SAT / coboundary | balanced / 2-colourable | `[J]=0`, confluent off fork |

This is **one proven adapter contract** (the object the tri-repo rule wants before any identity), at
consistency grade.

## Result 2 — the adapter OBSTRUCTION is the orientation (forgotten structure)

Constructing balanced graphs (coboundary/vertex-sourced branch) and putting an **orientation** on the edges
(the TI `Ext_S` arrow / TaF T18 finality arrow):

```
re-orientation changed the balance verdict in: 0/100 cases
global-sign solution count = 2^components; components: {1: 92, 2: 8}
```

**Orientation is invisible to the shared object** (0/100). The balanced object leaves a **free ℤ/2 per
connected component** (2 solutions; 92/100 graphs are one component -> exactly **one** free bit). That single
free bit is exactly `bar(b)`'s undetermined value. In TaF's IPT language (T23): **preserved invariant = the
`H^1` balance class; allowed loss = the orientation; the value bit is the forgotten structure.**

## Why this matters — it structurally EXPLAINS W211 and DERIVES the tri-repo split

- **W211 explained.** The GU observer nerve is **undirected** (agree/disagree is symmetric), so GU's object
  is *only* the balance signed-graph — which **forgets the orientation**. Therefore GU **cannot fix the sign
  internally**: not by lack of effort, but because its object structurally has no orientation to read. That is
  exactly W211's "the bit is GU-internally undecidable / a free ℤ/2," now with a **structural cause**.
- **The tri-repo division of labor, derived not assigned.** The orientation lives only in a **directed**
  structure. GU has none (undirected nerve). TI has it (`Ext_S` directed morphisms). TaF has it (T18 one-way
  finality arrow). So "GU owns boundary content (the undirected consistency object); TI/TaF own the finality
  orientation (the directed arrow that fixes the value)" is **forced by the mathematics**, not an org chart.
- **The value's location is now exact.** `bar(b)` = the orientation of the finality arrow = the one bit the
  shared balance object forgets. Consistency (no domains) is triple-secured; the value requires the directed
  finality object, whose **direction TaF itself flags open (T57)**.

## Honest status

- This is **one** adapter contract, at **consistency/structural grade**. The tri-repo rule wants **>= 2**
  proven adapter contracts before any cross-repo identity; the identity `bar(b) = finality orientation`
  stays **Joe-gated**.
- Nothing physical: `Issue[S]^physical = false` (TI); the generation **number** stays behind the source
  action (GU); the finality-arrow **direction** stays open (TaF T57).
- What genuinely advanced: the three-way convergence is now a **proven isomorphism at consistency grade** (not
  superficial), and the value is **exactly located** as the forgotten orientation — with a structural reason
  GU cannot supply it and TI/TaF must.
