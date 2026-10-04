---
title: "K1028 locality-compromise fraction boundary"
status: active_research
doc_type: conditional_locality_compromise_boundary
created: 2026-10-04
claim_ceiling: sharp aggregate local ceiling from a supplied bounded fraction of causally uncertified trials
manifest: lab/process/k1028-k1027-locality-compromise-fraction-boundary.json
probe: tests/channel-swings/k1028_k1027_locality_compromise_fraction_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1028 locality-compromise fraction boundary

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: sharp score ceiling under a bounded locality-compromise fraction
carrier: binary CHSH-game trials partitioned into audited-good and compromised subsets LAYER=observed CHIRALITY=N/A
pairing: convex mixture of conditional win ceilings ON=repository_quantum_control
real_structure: real probabilities with deterministic subset-size bound
grading: exact conditional probability theorem
action_owner: UNTYPED -- no causal audit or communication model is GU owned
target: memory-compatible local score ceiling MAP-TYPE=evaluation
```

If good trials obey conditional local ceiling `b` and predictable compromise
indicators `c_i`, fixed before the corresponding score `W_i`, satisfy
`sum_i c_i <= qn`, compromised trials must be allowed win ceiling one. The
sharp aggregate bound is

```text
(1-q)b+q = b+q(1-b).
```

For finite counts this is `[(n-C)b+C]/n`. The bound is attained by saturating
`b` on every good trial and winning every compromised trial. The correction
is therefore smaller than the coarse additive `q`, but it vanishes only when
the audit certifies all trials.

The theorem consumes a supplied pre-score bound on causally uncertified or
communication-capable trials. A label selected after observing whether a trial
won is outside the theorem: such post-selection could bias the retained good
set. The result does not construct the causal audit or prove physical locality.
