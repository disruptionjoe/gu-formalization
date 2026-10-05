---
title: "K1143 constrained energy radical descent"
status: active_research
doc_type: exact_constrained_energy_quotient_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional energy descent theorem; no GU physical quotient
manifest: lab/process/k1143-constrained-energy-radical-descent.json
probe: tests/channel-swings/k1143_constrained_energy_radical_descent_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1143 constrained energy radical descent

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem composes
> propagation with a supplied Hessian pairing. It neither supplies the source
> constraint nor proves a functional Hamiltonian realization. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact conservation and radical-quotient descent criterion
carrier: finite real field fibre with propagated constraint kernel LAYER=source-print CHIRALITY=N/A
pairing: symmetric Hessian H restricted to ker Q ON=constraint-kernel
real_structure: real linear Hamiltonian data
grading: constrained states, restricted radical and quotient
action_owner: comparator -- H Q and G must be supplied independently
target: K1140 graph-inertia plus propagation gates MAP-TYPE=restriction
```

Assume `G*H+HG=0` and `ker Q` is `G`-invariant. Then the quadratic form
`v*Hv` is conserved along every constrained solution. If `H|ker Q` is
nonnegative, its radical is automatically `G`-invariant: for radical `r`,
`H(Gr,k)=-H(r,Gk)=0` for every constrained `k`, because both `Gr` and `Gk`
remain constrained. Hence both the evolution and the form descend to

```text
ker Q / rad(H|ker Q),
```

where the induced form is positive definite. The exact control uses
`Q=(1,0,0,0)`, `H=diag(0,0,2,2)` and a generator that scales the constrained
radical direction while rotating the last two coordinates. Propagation and
`H`-skewness pass exactly; the quotient Gram is `diag(2,2)` and has dimension
two. Removing propagation makes the restriction dynamically unusable, while
changing one positive entry to `-2` leaves propagation intact but defeats
positivity. Thus propagation and nonnegative restriction are independent
obligations. The producer passes `12/12`; the hostile probe rejects `11/11`
mutations.
