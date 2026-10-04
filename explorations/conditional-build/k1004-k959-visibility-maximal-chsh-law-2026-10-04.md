---
title: "K1004 visibility and maximal CHSH law"
status: active_research
doc_type: conditional_cross_anchor_law_correction
created: 2026-10-04
claim_ceiling: imported common-semigroup visibility/Bell relation only
manifest: lab/process/k1004-k959-visibility-maximal-chsh-law.json
probe: tests/channel-swings/k1004_k959_visibility_maximal_chsh_law_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1004 visibility and maximal CHSH law

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: corrected fixed and optimized Bell relations to K958 visibility
carrier: one imported K956 coherence parameter represented in Bell and two-path controls LAYER=observed CHIRALITY=N/A
pairing: imported trace and interferometric probability pairings ON=repository_quantum_control
real_structure: complex qubit controls
grading: frozen Bell witness versus optimized Bell witness
action_owner: UNTYPED -- common semigroup and apparatus relation are imported
target: cross-anchor operational law MAP-TYPE=evaluation
```

K958 gives `V=lambda`. K959's linear identity survives after its witness is
named:

```text
S_fixed/sqrt(2)-1=V.
```

The optimized relation is instead

```text
S_max=2 sqrt(1+V^2),       S_max^2/4-1=V^2.
```

If an experiment requires CHSH margin `delta>0`, so `S_max>=2+delta`, then

```text
V>=sqrt(delta+delta^2/4).
```

For `delta=1/10`, the required squared visibility is `41/400`. This makes the
finite-resolution burden explicit: every nonzero ideal visibility violates
under exact optimization, but an owned statistical and systematic error budget
is needed to resolve that violation. The `V=2/5` K1002 separator is frozen as
an unscored protocol holdout.
