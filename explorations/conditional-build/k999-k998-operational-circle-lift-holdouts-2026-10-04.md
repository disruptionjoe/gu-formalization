---
title: "K999 K998 operational circle and lift holdouts"
status: active_research
doc_type: conditional_operational_holdout_result
created: 2026-10-04
claim_ceiling: conditional finite-band bound and frozen winding holdout only
manifest: lab/process/k999-k998-operational-circle-lift-holdouts.json
probe: tests/channel-swings/k999_k998_operational_circle_lift_holdouts_probe.py
target_claim: NONE-NOT-A-KILL
---

# K999 operational circle and lift holdouts

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: finite-band circular approximation bound and winding-sensitive lift holdout
carrier: circular densities plus unwrapped real-phase records LAYER=observed CHIRALITY=N/A
pairing: Fourier L2 pairing and record-event probability ON=repository_stochastic_model
real_structure: real density and real unwrapped jump count
grading: harmonic cutoff N and integer winding count
action_owner: UNTYPED -- regularity budget charge access apparatus and record are unowned
target: operational separation of circular approximation from real-lift identification MAP-TYPE=evaluation
```

For a circular density with declared Sobolev budget `||p||_{H^s}<=M`, Parseval
gives

```text
sum_{|n|>N} |p_hat(n)|^2 <= M^2 / (1+(N+1)^2)^s.
```

Finite harmonic access can therefore approximate a regularity-bounded circular
law, but it cannot identify an unrestricted law and does not weaken K993. The
regularity class and its numerical budget must be owned rather than fitted
after the data.

A separate real-lift holdout is frozen at `T=2`: compare a base lift with the
K998 lift carrying independent `+2 pi` jumps at rate `0.4`. Every integer
harmonic and the complete circular process are identical. The unwrapped event
"at least one added winding jump" has probabilities `0` and `1-exp(-0.8)`.
This holdout is unscored because the unwrapped record, apparatus and action
owner are absent.
