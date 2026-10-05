---
title: "K1079 two-mode commutator witness"
status: active_research
doc_type: conditional_two_mode_hessian_commutator_certificate
created: 2026-10-04
claim_ceiling: exact finite-rank two-mode witness and positive two-by-two counterexample; no functional or GU-source no-go
manifest: lab/process/k1079-k1078-two-mode-commutator-witness.json
probe: tests/channel-swings/k1079_k1078_two_mode_commutator_witness_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1079 two-mode commutator witness

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> Hessian diagnostic, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_OBSTRUCTION`.

```gu-typed-objects
result: two normalized modal Hessians recover the gradient-mass commutator exactly
carrier: two spatial evaluations of one finite-rank quotient Hessian LAYER=observed CHIRALITY=N/A
pairing: H(lambda)=lambda X+Y with X=A^-1B and Y=A^-1C ON=candidate_action
real_structure: real finite-dimensional phase space
grading: common supplied kinetic normalization and two distinct known spatial modes
action_owner: repository-construction -- firing example is not a GU Hessian
target: K1077 simultaneous-normal-mode premise MAP-TYPE=evaluation
```

For distinct `lambda_1,lambda_2`, exact algebra gives

```text
[H(lambda_1),H(lambda_2)]
  = (lambda_1-lambda_2)[X,Y].
```

Two independently supplied modal Hessians therefore test the common-normal-mode
premise directly. A nonzero commutator rejects one fixed normal basis; it does
not reject positivity or the quadratic action.

The positive example

```text
X=diag(1,2),       Y=[[2,1],[1,3]]
```

has `[X,Y] != 0` and frequency branches

```text
omega_+/-^2 = (3 lambda+5 +/- sqrt((lambda+1)^2+4))/2.
```

Neither branch is affine, even though the matrix pencil is affine and positive
for `lambda>=0`. This firing counterexample prevents applying K1078 after
checking positivity alone. A functional use still requires a common domain and
controlled unbounded-operator commutators. The producer passes `10/10`; the
hostile probe rejects `10/10` identity, counterexample, domain, ownership and
scope mutations.

## Next condition

Apply the witness only after a native action supplies one positive functional
Hessian, kinetic normalization and two modal restrictions on a common domain.
