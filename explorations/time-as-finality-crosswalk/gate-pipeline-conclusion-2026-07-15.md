---
title: "Corrected observer-sheaf gate-pipeline conclusion"
status: exploration
doc_type: conclusion-synthesis
created: 2026-07-15
corrected_by: ADAPTER2-01
verdict: "CONDITIONAL NO-DOMAINS RESULT; ONE GLOBAL RELABELING BIT REMAINS; ITS PHYSICAL MEANING IS OPEN"
---

# Corrected conclusion of the gate pipeline

## What survives

For the tested signed observer-graph model, a vertex-sourced sign assignment is
a coboundary. It is globally consistent, produces no frustrated domains, and
remains consistent under the tested deletion controls. On each connected
component, two globally flipped assignments remain.

This is a conditional signed-graph result. It explains why the passing model
has one global relabeling freedom rather than independently chosen domains.

## What does not survive

The graph result does not identify that global flip with:

- the orientation of a TI issuance arrow;
- the direction of TaF finality;
- positive versus negative Krein norm; or
- the value of `bar(b)`.

The earlier note assigned the remaining graph bit the meaning
"issuance/finality orientation" before a branch-preserving adapter existed.
Correction ADAPTER2-01 shows that the attempted adapter forgets the branch.

## Topological limit

The vertex-sourced passing branch has trivial loop holonomy. The graph topology
does not determine the sign value. Relational edge-sourced signs can carry
nontrivial holonomy, but those are exactly the tested cases that frustrate into
domains.

An H3 or higher-overlap route remains untested, but it cannot inherit a result
from this H1 comparison.

## Current question

The correct downstream question is whether a physical, source-owned map exists
from the remaining sign torsor to an independently constructed finality or
positive-norm polarity. That map is open. The gate pipeline by itself supplies
neither the map nor the physical interpretation.

`bar(b)`, `H59`, Krein positivity, physical issuance, and the generation count
remain open at their prior grades.
