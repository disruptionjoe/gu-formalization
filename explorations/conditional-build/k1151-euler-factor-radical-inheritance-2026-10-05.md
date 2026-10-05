---
title: "K1151 Euler-factor radical inheritance"
status: active_research
doc_type: source_euler_factor_constraint_theorem
created: 2026-10-05
claim_ceiling: exact finite-symbol theorem for Euler-row postprocessors; no nonfactor boundary or KT/BFV map classified
manifest: lab/process/k1151-euler-factor-radical-inheritance.json
probe: tests/channel-swings/k1151_euler_factor_radical_inheritance_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1151 Euler-factor radical inheritance

> **GU-COMPARATOR-ROUTING — scope before inference.** This tests one
> source-owned class: constraints obtained only by linearly postprocessing the
> source Euler equations. Read `lab/methods/source-native-comparator-routing.md`
> before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: radical inheritance theorem for Q=L H
carrier: one finite source-Hessian symbol carrier LAYER=source-print CHIRALITY=N/A
pairing: symmetric source Hessian H ON=fixed-symbol-field-space
real_structure: real finite coefficient space
grading: gauge image to fields to Euler rows
action_owner: source-action -- H and every linear row postprocessor of H
target: positive nonzero constrained cohomology MAP-TYPE=evaluation
```

Let `H:V->V*` be symmetric, let the owned gauge map `d` satisfy `Hd=0`,
and form a constraint only by postprocessing Euler rows:

```text
Q = L H .
```

Then `ker H` is contained in `ker Q`. More strongly, for every `v in ker H`
and every `w in ker Q`, `H(v,w)=0`; hence

```text
ker H subset rad(H restricted to ker Q).                 (1)
```

Therefore the K1144 equality `rad(H|ker Q)=im d` can hold for an Euler-factor
constraint only if `ker H=im d`. The exact four-dimensional control has a
two-dimensional Hessian kernel, a rank-one gauge image and one surviving
nongauge radical direction; all four radical pairings vanish. Producer and
probe pass `12/12` and `11/11`.

This does not classify a constraint or trace map that is not factored through
`H`, enlarge the gauge/KT image, choose a boundary domain or construct a
physical quotient. No protected status moves.
