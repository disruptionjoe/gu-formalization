---
title: "K1001 K957 optimized CHSH correction"
status: active_research
doc_type: conditional_bell_witness_scope_correction
created: 2026-10-04
claim_ceiling: imported damped-Bell-state optimization theorem only
manifest: lab/process/k1001-k957-optimized-chsh-correction.json
probe: tests/channel-swings/k1001_k957_optimized_chsh_correction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1001 optimized CHSH correction

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: optimized CHSH value for the imported K956 phase-damped Bell state and scope correction for K957
carrier: two imported qubits with Bell-diagonal state rho_lambda LAYER=observed CHIRALITY=N/A
pairing: imported positive trace state/effect pairing ON=repository_quantum_control
real_structure: complex two-qubit Hilbert space with Hermitian adjoint
grading: Alice versus Bob tensor factors
action_owner: UNTYPED -- K956 dephasing and measurement optimization are repository controls
target: fixed-witness versus state-optimal Bell value MAP-TYPE=evaluation
```

K956 sends `|Phi+><Phi+|` to the Bell-diagonal state

```text
rho_lambda=(I tensor I+lambda X tensor X-lambda Y tensor Y+Z tensor Z)/4.
```

Its correlation tensor is `T=diag(lambda,-lambda,1)`, so `T^T T` has
eigenvalues `1,lambda^2,lambda^2`. The two largest eigenvalues give

```text
S_max(lambda)=2 sqrt(1+lambda^2).
```

One explicit maximizing choice is `A0=Z`, `A1=X` and
`B0,1=(Z +/- lambda X)/sqrt(1+lambda^2)`. Thus every `lambda>0`
violates CHSH, while `lambda=0` exactly saturates the classical boundary.

K957's arithmetic survives. Its `sqrt(2)(1+lambda)` is the value obtained by
keeping the settings optimal at the Bell endpoint `lambda=1` fixed while the
state damps. It is not the state-optimal CHSH value after damping. The old
threshold `lambda>sqrt(2)-1` therefore belongs to that frozen witness only.

Hostile review preserves the strongest contrary reading: if an experiment
pre-registers and freezes K957's settings, its finite witness threshold is
operationally correct. Reoptimization is a different measurement protocol and
must be owned rather than silently assumed. No GU source, action, state,
observable, prediction or confirmation follows.
