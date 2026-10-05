---
title: "K1133 zero-kappa symbol-null propagation audit"
status: active_research
doc_type: source_i1b_zero_kappa_constraint_propagation_audit
created: 2026-10-05
claim_ceiling: exact current selected-Shiab propagation failure; different source differential may reopen
manifest: lab/process/k1133-zero-kappa-symbol-null-propagation-audit.json
probe: tests/channel-swings/k1133_zero_kappa_symbol_null_propagation_audit_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1133 zero-kappa symbol-null propagation audit

> **GU-COMPARATOR-ROUTING — scope before inference.** This audits the selected
> `comm/symi/symi` I1B distortion operator, not Weinstein's unrecovered
> preferred historical Shiab or every possible completion. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: zero-kappa symbol-null propagation audit
carrier: Omega1(Cl(7,7)) all-grade distortion symbol LAYER=source-print CHIRALITY=N/A
pairing: formal Euler/Green pairing ON=selected distortion equations
real_structure: real Cl(7,7) symbol
grading: complete Clifford-grade chains and causal conormal strata
action_owner: source-action -- selected I1B zero-kappa horn
target: proposed non-gauge propagated constraint complex MAP-TYPE=evaluation
```

The zero-kappa horn has large principal nullspaces, but K132 already provides
the decisive compatibility test. In its exact 56-dimensional normal/tangent
block, the normal kernel has dimension `24` while only `11` directions remain
in the common normal-tangential kernel. Thirteen normal-null directions are
lost before any global propagation claim.

Lower-order compatibility also fails on both available background classes:

- on generic Ricci-flat Weyl germs, `D_B^2=ad(F_B)` is nonzero, so the
  selected distortion operator does not form a complex;
- on the flat or curvature-central exception, K133 finds that the selected
  Euler symbol is not square-zero. Its causal ranks `130912,130912,122746`
  all exceed the `114688` rank ceiling for a square-zero endomorphism on the
  `229376`-dimensional carrier.

Thus the symbol null rows are characteristic data, not an action-owned
propagated non-gauge constraint complex. A different source-owned differential,
coefficient completion or background may reopen the calculation. The producer
passes `12/12`; the hostile probe rejects `11/11` mutations.
