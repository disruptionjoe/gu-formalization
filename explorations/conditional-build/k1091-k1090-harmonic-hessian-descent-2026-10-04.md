---
title: "K1091 harmonic Hessian descent criterion"
status: active_research
doc_type: conditional_harmonic_hessian_descent
created: 2026-10-04
claim_ceiling: exact finite Hilbert-complex criterion for a self-adjoint Hessian to act on harmonic cohomology
manifest: lab/process/k1091-k1090-harmonic-hessian-descent.json
probe: tests/channel-swings/k1091_k1090_harmonic_hessian_descent_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1091 harmonic Hessian descent criterion

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> finite Hilbert-complex theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_COHOMOLOGY_THEOREM`.

```gu-typed-objects
result: a self-adjoint Hessian acts on harmonic cohomology exactly when it commutes with the harmonic projector
carrier: finite Hilbert complex C0 --d0--> C1 --d1--> C2 with d1 d0=0 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing defining adjoints and the harmonic representative space ON=conditional_gauge_hessian
real_structure: real Euclidean or complex Hermitian finite complex
grading: cochain degrees zero, one and two; physical carrier H1=ker(d1) intersect ker(d0*)
action_owner: repository-construction -- no source-selected GU BV/BFV complex
target: K1090 physical-cohomology seam MAP-TYPE=quotient
```

For a finite Hilbert complex, degree one has the orthogonal Hodge splitting

```text
C1 = im(d0) direct_sum H1 direct_sum im(d1*),
H1 = ker(d1) intersect ker(d0*).
```

Let `P_H` be the orthogonal projector onto `H1` and let `L=L*` be a supplied
Hessian. Then `L` induces the same self-adjoint operator on harmonic
representatives exactly when

```text
[L,P_H]=0.
```

Indeed, `L(H1) subset H1` is equivalent to vanishing of the off-diagonal
block `(I-P_H)L P_H`. Self-adjointness makes the opposite block its adjoint,
so both vanish exactly when the commutator vanishes. Positivity of `L` then
restricts to positivity of `L|H1`, but the complex and its pairing must already
be owned.

The exact control uses `d0=(1,0,0)^T`, `d1=(0,0,1)`, hence
`P_H=diag(0,1,0)`. The good Hessian `diag(0,3,5)` commutes with `P_H`; the
mixed Hessian from K1092 does not. The producer passes `11/11`; the hostile
probe rejects `10/10` criterion, splitting, control and ownership mutations.

This theorem supplies a test for a future action-owned complex. It constructs
neither the GU differential nor a functional closed domain.
