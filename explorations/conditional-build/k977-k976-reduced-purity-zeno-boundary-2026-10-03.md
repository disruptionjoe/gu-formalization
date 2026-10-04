---
title: "K977 K976 reduced-purity Zeno boundary"
status: active_research
doc_type: conditional_reduced_purity_boundary_result
created: 2026-10-03
claim_ceiling: exact short-time purity-order incompatibility under K976 hypotheses only
manifest: lab/process/k977-k976-reduced-purity-zeno-boundary.json
probe: tests/channel-swings/k977_k976_reduced_purity_zeno_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K977 reduced-purity short-time boundary

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: bounded product-state Hamiltonian parents have zero linear purity loss while positive-rate dephasing does not
carrier: pure system input tensor fixed environment state LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert trace purity and partial trace ON=repository_bounded_dilation
real_structure: complex conjugation in chosen Hilbert bases
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction, not Weinstein source or GU action
target: observable short-time consequence of the K976 first-jet obstruction MAP-TYPE=evaluation
```

For a pure system projector `P`, K976 gives
`rho'_S(0)=-i[H_eff,P]`. Hence

```text
d Tr(rho_S(t)^2)/dt |_{t=0}=2 Tr(P rho'_S(0))=0,
```

so purity loss begins at quadratic order for the declared bounded parent. The
K956 dephasing semigroup applied to `|+><+|` instead has

```text
rho_t=(I+e^{-2 gamma t}X)/2,
Tr(rho_t^2)=(1+e^{-4 gamma t})/2
            =1-2 gamma t+O(t^2).
```

For `gamma>0` the short-time orders are incompatible. The explicit bounded
control `H=Z tensor Y`, environment `|0>`, gives coherence `cos(2t)` and
purity `(1+cos^2(2t))/2=1-2t^2+O(t^4)`, confirming the quadratic horn.

This is an observable consequence of the same declared assumptions, not a
universal no-go for singular, reset, correlated or non-Hamiltonian dynamics.
Purity and the positive Born pairing are repository imports, not GU-owned
physics.
