---
title: "K1141 constraint propagation intertwiner criterion"
status: active_research
doc_type: exact_finite_constraint_propagation_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional propagation criterion; no action ownership or functional domain
manifest: lab/process/k1141-constraint-propagation-intertwiner-criterion.json
probe: tests/channel-swings/k1141_constraint_propagation_intertwiner_criterion_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1141 constraint propagation intertwiner criterion

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests
> propagation for a supplied source-native constraint candidate. Solving for a
> row generator does not make the constraint source-owned. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact propagation and induced row-evolution criterion
carrier: finite real field fibre with full-row-rank constraint Q and generator G LAYER=source-print CHIRALITY=N/A
pairing: auxiliary positive coordinate pairing used only for the right inverse ON=constraint-row-space
real_structure: real matrices
grading: field directions versus constraint rows
action_owner: comparator -- theorem evaluates a separately action-owned map
target: K1140 propagation gate MAP-TYPE=evaluation
```

Let `Q:V->C` have full row rank and let `G:V->V` generate the linearized
field evolution. Then

```text
ker Q is G-invariant  iff  there exists R:C->C with QG=RQ.       (1)
```

The forward implication is the quotient-map theorem: `QG` is constant on the
fibres of the surjection `Q`, so it factors uniquely through `C`. With the
coordinate right inverse `S=Q*(QQ*)^-1`, the unique row generator is

```text
R = Q G S = Q G Q* (Q Q*)^-1.                                  (2)
```

Conversely, `(1)` gives `QGv=RQv=0` whenever `Qv=0`. The exact pass fixture
uses `Q=(1,0,0)` and a generator whose first row is `(2,0,0)`, yielding
`R=(2)`. Changing that row to `(2,1,0)` breaks propagation. This criterion is
finite-dimensional and algebraic; a common closed operator domain, boundary
traces, action ownership and physical cohomology remain separate. The producer
passes `12/12`; the hostile probe rejects `10/10` mutations.
