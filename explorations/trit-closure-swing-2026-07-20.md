---
title: "TRIT-INTERPRETATION closure swing: the nested three-question chain has no natural cyclic closure"
status: "exploration / pre-registered closure swing executed; CLOSURE-FAILS-NATURALITY at finite structural grade"
doc_type: exploration
created: 2026-07-20
directed_by: "RUN-20260720-193705-repository-work-cycle-cai-hourly; executes the bound successor in trit-triage-2026-07-20.md"
lane: 1
channel: TRIT-INTERPRETATION
provenance_grade: "finite structural theorem over the already-extracted three-question nesting; no P2C truth transfer"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
probe: tests/channel-swings/trit_closure_probe.py
---

# Trit closure swing

## Bound question

The triage pre-registered one successor: test whether the trit's canonical,
unoriented `Z/3` could be the cyclic closure of the nested three-question chain

```text
world >= access >= standpoint
```

by a natural wrap from standpoint back to world. The proposed closure had to
remain conjugation-symmetric, reproduce an order-three action, and reject a
directed-chain control. The later Node A/B fork is carried rather than ignored:
the trit is now known at fixture grade as an external `S_3` label on three
structurally isomorphic Krein copies, not as a clock, nesting, or two-form.

This swing tests the program-native object actually named by the bound: the
finite access-question nesting as extracted in the triage. It does not replace
that object with a standard-physics phase clock or silently promote the later
`S_3` label into an internal GU construction.

## Result: `CLOSURE-FAILS-NATURALITY`

A three-element total order has only the identity order automorphism. Its
automorphism group therefore contains no element of order three. Either
candidate wrap

```text
world -> access -> standpoint -> world
```

adds a new relation not supplied by the nesting. The reverse wrap does the
same. Conjugation symmetry merely says that the two imported orientations are
equivalent; it does not make either wrap natural.

The arity equality `3 = 3` is consequently insufficient. The nesting supplies
three positions but not the cyclic action required by the trit. The proposed
closure reading cannot provide the trit without importing exactly the new wrap
datum it was meant to explain.

## Controls

The deterministic probe exhausts all six permutations of three points.

| Check | Outcome | Meaning |
|---|---|---|
| Total-order automorphisms | identity only | The extracted nesting has trivial symmetry. |
| Order-three automorphism | absent | No natural `Z/3` action is supplied. |
| Directed-path plant | identity only | The pre-registered directed-chain control fails as required. |
| Undirected-triangle positive control | all six permutations | A genuine unoriented triangle has full `S_3`. |
| Triangle three-cycles | both orientations present | The control reproduces conjugation-symmetric order-three structure. |

The positive control matters: the test admits the later trit shape when the
missing wrap edges are actually part of the structure. It refuses only the
claim that a nesting supplies those edges for free.

## Interpretation

Candidate 5's closure reading is killed at finite structural grade. This is not
a P2C result and not a cross-repository claim: the P2C surface was consumed only
through the frozen shape constants already recorded by the GU triage. It does
not say that access, standpoint, or observer structure is irrelevant. It says
that the named total-order nesting does not naturally generate the external
`S_3` label.

The adverse result agrees with the later fork rather than rescuing it:

- Node A found full `S_3` interchangeability;
- Node B found three isomorphic copies and no simplex/nesting realization; and
- the source-object characterization records the external `S_3` label as a
  load-bearing item not supplied by the intaken programs.

The TRIT-INTERPRETATION channel is therefore closed on interpretation shape.
The surviving question is provenance: what external source object supplies the
`S_3` label and its matching to the commutant cube-root subgroup? That question
belongs to the B.5 source-object/two-gate program and must not be relabeled as a
P2C cyclic closure.

## Receipt and boundary

`python tests/channel-swings/trit_closure_probe.py` returns seven passing checks
and the headline `CLOSURE-FAILS-NATURALITY`. The probe is pure Python, finite,
deterministic, and uses no Lake/Lean build or heavy computation.

Exploration grade only. No claim, canon, scientific-status, public-posture, or
cross-repository truth movement. No external action. A future source object may
supply a cyclic label, but that would be new typed structure, not a natural
automorphism of this nesting.
