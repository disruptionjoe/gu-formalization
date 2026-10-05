---
title: "K1152 sharp radical-capture rank floor"
status: active_research
doc_type: positive_cohomology_radical_capture_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional necessary condition with sharp control; no functional realization
manifest: lab/process/k1152-sharp-radical-capture-rank-floor.json
probe: tests/channel-swings/k1152_sharp_radical_capture_rank_floor_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1152 sharp radical-capture rank floor

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a general
> linear-algebra theorem applied later to the source-native Hessian. It does not
> supply a GU constraint. Read `lab/methods/source-native-comparator-routing.md`.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp rank floor for removing nongauge Hessian zero modes
carrier: finite symmetric-form carrier LAYER=source-print CHIRALITY=N/A
pairing: symmetric H restricted to ker Q ON=constrained-carrier
real_structure: real finite coefficient space
grading: gauge image inside Hessian kernel and constraint kernel
action_owner: comparator -- source ownership required separately for Q and d
target: rad(H|ker Q)=im d MAP-TYPE=restriction
```

Assume `Hd=0`, `Qd=0`, and the positive-cohomology radical condition
`rad(H|ker Q)=im d`. On `ker H`, the kernel of `Q` is then exactly `im d`:

```text
ker(Q restricted to ker H) = im d.
```

Rank-nullity gives the sharp identity and ambient floor

```text
rank(Q|ker H) = dim ker H - rank d,
rank Q          >= dim ker H - rank d.                  (1)
```

The floor is attained by `H=diag(0,0,1)`, gauge image `span(e1)` and
`Q=(0,1,0)`: the constrained radical is precisely `span(e1)` and the quotient
is the positive `e3` line. An Euler factor `Q=LH` has zero restriction to
`ker H`, so it can attain (1) only when `ker H=im d`. Producer and probe pass
`12/12` and `11/11`.

Functional use still requires the K1150 closed-range, common-product-domain,
uniform-gap and maximal-boundary-generator gates. No protected status moves.
