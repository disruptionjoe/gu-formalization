---
title: "K988 K987 controlled process nonidentifiability"
status: active_research
doc_type: conditional_process_nonidentifiability_result
created: 2026-10-04
claim_ceiling: controlled system-only equality for the declared independent-increment class
manifest: lab/process/k988-k987-controlled-process-nonidentifiability.json
probe: tests/channel-swings/k988_k987_controlled_process_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K988 controlled-process nonidentifiability

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact equality of every finite controlled system-only process in the declared Markov class
carrier: system plus optional inert ancilla and finite CP intervention sequence LAYER=observed CHIRALITY=N/A
pairing: arbitrary supplied positive preparations, instruments and effects ON=controlled_reduced_process
real_structure: inherited from the operational state/effect space
grading: finite time-ordered operational probabilities
action_owner: N/A -- theorem compares imported microscopic models after interval-channel equality
target: process-level identifiability boundary for K983 MAP-TYPE=evaluation
```

Suppose a microscopic phase process has stationary independent increments and
its averaged channel on every interval of length `Delta` is `D_Delta`. For any
finite sequence of system or system-plus-inert-ancilla CP interventions
`A_1,...,A_{n-1}` that does not read the microscopic noise record, conditional
expectation over successive independent increments gives

```text
D_Delta_n o A_{n-1} o ... o A_1 o D_Delta_1.
```

The expression depends only on the interval channels. It is therefore
identical for K986 Brownian diffusion and every K987 symmetric
compound-Poisson horn. Instrument outcomes and feedback based on those system
outcomes are included branchwise by induction; inert ancillas are included by
tensoring each interval channel with the identity.

This strengthens K983 exactly where it left the question open, but only for
the declared independent-increment class. It does not cover access to the
clock or environment record, feedback conditioned on that record, correlated
increments, memoryful processes, or arbitrary microscopic process equality.
