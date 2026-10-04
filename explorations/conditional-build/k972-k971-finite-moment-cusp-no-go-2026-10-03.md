---
title: "K972 K971 finite-moment cusp no-go"
status: active_research
doc_type: conditional_finite_moment_no_go
created: 2026-10-03
claim_ceiling: finite-first-moment no-go for exact positive spectral characteristic functions only
manifest: lab/process/k972-k971-finite-moment-cusp-no-go.json
probe: tests/channel-swings/k972_k971_finite_moment_cusp_no_go_probe.py
target_claim: NONE-NOT-A-KILL
---

# K972 finite-moment cusp no-go

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: finite absolute first spectral moment excludes exact positive-rate exponential coherence
carrier: arbitrary probability spectral measure mu on R LAYER=observed CHIRALITY=N/A
pairing: positive spectral expectation ON=declared_measure
real_structure: characteristic-function conjugation phi(-t)=conjugate(phi(t))
grading: degree-zero; no BV or gauge grading
action_owner: UNTYPED -- structural theorem on a supplied positive spectral state
target: generalization of K971 beyond the Cauchy example MAP-TYPE=evaluation
```

Let `mu` be any probability measure with
`integral |omega| dmu(omega)<infinity` and define

```text
phi(t)=integral exp(i omega t) dmu(omega).
```

The difference quotient is dominated by `|omega|`, since
`|exp(i omega t)-1|/|t|<=|omega|`. Dominated convergence therefore gives

```text
phi'(0)=i integral omega dmu(omega).
```

Thus `phi` is differentiable at zero. For `a>0`, the target
`exp(-a|t|)` has right derivative `-a` and left derivative `+a`; it is not
differentiable at zero. No positive spectral characteristic function with a
finite absolute first moment can equal it on a neighborhood of zero, hence not
for all real time.

This does not exclude nonautonomous dynamics, reset laws, singular white-noise
limits, or general open-system generators. It isolates the exact price paid by
the positive autonomous spectral-parent class. K973 tests the stronger physical
finite-variance consequence. No GU or protected verdict moves.
