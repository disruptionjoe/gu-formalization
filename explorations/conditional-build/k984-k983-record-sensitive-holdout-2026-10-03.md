---
title: "K984 K983 record-sensitive holdout"
status: active_research
doc_type: conditional_preregistered_record_holdout
created: 2026-10-03
claim_ceiling: frozen conditional holdout with no data or empirical score
manifest: lab/process/k984-k983-record-sensitive-holdout.json
probe: tests/channel-swings/k984_k983_record_sensitive_holdout_probe.py
target_claim: NONE-NOT-A-KILL
---

# K984 record-sensitive holdout

Classification: `INTERNAL_PREREGISTERED_HOLDOUT`.

```gu-typed-objects
result: frozen Poisson count-record holdout strictly finer than the system endpoint parity
carrier: K981 system plus an independently accessible clock or environment count record LAYER=observed CHIRALITY=N/A
pairing: imported positive system pairing and classical count readout ON=repository_stochastic_model
real_structure: computational-basis conjugation plus real count probabilities
grading: degree-zero endpoint and record events
action_owner: UNTYPED -- no GU action owns the clock or makes its record observable
target: distinct empirical resolution required by K980 MAP-TYPE=evaluation
```

The holdout is frozen before scoring:

- calibrate `gamma` only from the prior system dephasing data;
- fix `T=2` without using record data;
- expose the full count `N_T`, not merely its parity;
- test `P(N_T=n)=exp(-gamma T)(gamma T)^n/n!`, mean `gamma T`, and variance `gamma T`;
- do not refit `gamma` on the holdout.

The system endpoint reads only parity because `Z^{n+2}=Z^n`. The count record
strictly refines parity: at the frozen positive `gamma T`, two-or-more events
have positive probability, and counts `n` and `n+2` give the same endpoint
unitary. Thus the holdout is inequivalent to endpoint tomography.

No empirical score is assigned. Execution requires a native action or
microscopic model that makes the record operationally available and links it
to each system trial. The reduced semigroup alone supplies no such observable.
