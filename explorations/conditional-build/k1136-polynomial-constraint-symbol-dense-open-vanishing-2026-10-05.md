---
title: "K1136 polynomial constraint-symbol dense-open vanishing"
status: active_research
doc_type: exact_local_constraint_symbol_identity_theorem
created: 2026-10-05
claim_ceiling: exact polynomial and real-analytic symbol theorem; nonlocal and distributional shell data remain open
manifest: lab/process/k1136-polynomial-constraint-symbol-dense-open-vanishing.json
probe: tests/channel-swings/k1136_polynomial_constraint_symbol_dense_open_vanishing_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1136 polynomial constraint-symbol dense-open vanishing

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests a
> possible constraint mechanism for the source-native I1B pencil; it neither
> supplies a source constraint nor excludes nonlocal spectral data. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: dense-open identity theorem for finite-order local constraint symbols
carrier: finite-dimensional symbol fibres over a connected covector chart LAYER=source-print CHIRALITY=N/A
pairing: none required beyond componentwise symbol coordinates ON=local-symbol-bundle
real_structure: real polynomial or real-analytic matrix entries
grading: covector degree and field-equation rows
action_owner: comparator -- theorem constrains a future source-action local map
target: K1135 exceptional-shell reopener MAP-TYPE=restriction
```

Let `Q(xi)` be the symbol of a finite-order local differential constraint.
Every matrix entry is polynomial in the covector `xi`. If `Q` vanishes on a
nonempty open subset of a connected covector chart, restrict an entry to
generic affine lines crossing that set. The resulting one-variable polynomial
vanishes on an interval and is therefore zero. Varying the line proves every
entry vanishes identically. The same componentwise conclusion holds for a
real-analytic symbol by analytic continuation.

The regularity matters. A merely smooth function may be supported on a shell
or compact region, and a distributional spectral projector can be shell
supported. Those objects are not finite-order local differential symbols and
would need their own action or boundary ownership. The exact degree-three
control uses nodes `0,1,2,3`; its Vandermonde determinant is `12`, so four
zero values force all four coefficients to vanish. The producer passes
`12/12`; the hostile probe rejects `10/10` mutations.
