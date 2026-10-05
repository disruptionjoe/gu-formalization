---
title: "K1081 common-domain functional Hessian"
status: active_research
doc_type: conditional_functional_hessian_domain_theorem
created: 2026-10-04
claim_ceiling: exact constant-coefficient flat-torus functional theorem for the repository-owned candidate; no source-selected GU Hessian
manifest: lab/process/k1081-k1080-functional-hessian-domain.json
probe: tests/channel-swings/k1081_k1080_functional_hessian_domain_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1081 common-domain functional Hessian

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> action-domain construction, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_ACTION_DOMAIN`.

```gu-typed-objects
result: the constant matrix pencil lifts to one positive self-adjoint flat-torus Hessian
carrier: L2(T3;R^2) with form domain H1 and operator domain H2 LAYER=observed CHIRALITY=N/A
pairing: standard positive L2 pairing and its closed H1 quadratic form ON=candidate_action
real_structure: real Fourier coefficients with conjugate mode pairing
grading: spatial Fourier modes tensored with the supplied internal carrier
action_owner: repository-construction -- K1036 candidate, not a source-selected GU action
target: Fourier identification of the K1080 functional-domain seam MAP-TYPE=isomorphism
```

Let `B=diag(2,3)>0`, `C=diag(6,15)>0`, and

```text
H = -Delta tensor B + C
```

on `L2(T3;R^2)`. Its closed positive form has domain `H1`; its unique
self-adjoint realization has domain `H2`. Fourier transformation gives the
exact fibre `H_hat(k)=|k|^2 B+C`, so every mode is a restriction of one
operator on one common domain rather than an unrelated finite matrix. Compact
Sobolev embedding makes the resolvent compact and the spectrum discrete.

The fixtures at `|k|^2=0,1,2,3` give eigenvalues `(6,15)`, `(8,18)`,
`(10,21)`, and `(12,24)`. The producer passes `10/10`; the hostile probe
rejects `12/12` domain, fibre, compactness, ownership and scope mutations.

## Boundary

This closes the functional-domain seam for the K1036 repository candidate. It
does not supply a source-selected GU action, curved stationary background,
boundary domain or physical BV cohomology.
