---
title: "K1023 event-ready herald ordering theorem"
status: active_research
doc_type: conditional_event_ready_ordering_theorem
created: 2026-10-04
claim_ceiling: exact ordering condition preserving a predictable-input local ceiling, plus a post-settings selection countermodel
manifest: lab/process/k1023-k1022-event-ready-herald-ordering.json
probe: tests/channel-swings/k1023_k1022_event_ready_herald_ordering_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1023 event-ready herald ordering theorem

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: pre-settings herald safety theorem and post-settings local countermodel
carrier: sequential heralded CHSH trials LAYER=observed CHIRALITY=N/A
pairing: herald filtration against conditional setting-pair laws ON=repository_quantum_control
real_structure: binary events and real conditional probabilities
grading: exact conditional theorem and finite counterexample
action_owner: UNTYPED -- the herald, causal order, setting source and locality are not GU owned
target: event-ready no-postselection protocol MAP-TYPE=evaluation
```

Let `H_i` be fixed from past and source information before `X_i,Y_i` are
generated. The herald may correlate arbitrarily with the hidden device state.
What is required is that, after conditioning on `H_i=1` and the past, the
setting law remains independent of that hidden state. K1014 then applies on
the heralded trials with the same predictable law `pi_i`, so the conditional
local ceiling remains `1-min_j pi_i(j)`.

Ordering is load-bearing. Take the deterministic local strategy
`a(x)=0,b(y)=0`. It wins on `(0,0),(0,1),(1,0)` and loses only on `(1,1)`.
A selector that reads the settings first and declares `H=1` exactly on the
three winning pairs accepts three quarters of uniform trials and has retained
win rate one. This is a fully local perfect retained sample.

Thus “event-ready” means more than attaching a herald label: its causal
measurability and the conditional freshness of later settings must be proved.
This packet constructs neither a physical herald nor a spacelike timing
theorem.
