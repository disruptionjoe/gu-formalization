---
title: "K1006 depolarized damped-Bell state"
status: active_research
doc_type: conditional_noisy_bell_state_interface
created: 2026-10-04
claim_ceiling: exact two-parameter imported-state classification only
manifest: lab/process/k1006-k1005-depolarized-damped-bell-state.json
probe: tests/channel-swings/k1006_k1005_depolarized_damped_bell_state_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1006 depolarized damped-Bell state

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact state and correlation spectrum for an isotropically depolarized K956 damped Bell control
carrier: two imported qubits with rho_(p,lambda) LAYER=observed CHIRALITY=N/A
pairing: imported positive trace state/effect pairing ON=repository_quantum_control
real_structure: complex two-qubit Hilbert space with Hermitian adjoint
grading: Alice versus Bob tensor factors
action_owner: UNTYPED -- neither p nor lambda is selected by a GU action
target: noisy Bell calibration interface MAP-TYPE=evaluation
```

Extend K956 by an independently typed isotropic contrast `0<=p<=1`:

```text
rho_(p,lambda)=p rho_lambda+(1-p)I_4/4,   0<=lambda<=1.
```

The four state eigenvalues are

```text
(1+p+2p lambda)/4,
(1+p-2p lambda)/4,
(1-p)/4,
(1-p)/4.
```

They are nonnegative throughout the declared square and sum to one. The
correlation tensor is

```text
T_(p,lambda)=p diag(lambda,-lambda,1).
```

At `p=4/5`, `lambda=2/5`, the state spectrum is
`(61/100,29/100,1/20,1/20)` and the correlation tensor is
`diag(8/25,-8/25,4/5)`.

This is a repository-selected noise family. It neither follows from K956's
dephasing generator nor supplies a GU physical quotient, detector model or
error law. Its role is to expose which ideal K1001 conclusions survive one
explicit additional noise parameter.
