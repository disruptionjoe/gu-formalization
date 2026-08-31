---
artifact_type: exploration
status: active_research
doc_type: exact_all_middle_set_valued_coend_construction
created: 2026-08-31
title: "All-middle Burnside balance quotient and universal factorization"
owner: gu-formalization
claim_status: repository_derived
claim_ceiling: "All-intermediate-object set-valued coend presentation for supplied additive restriction correspondences; no additive/category-valued coend, bicategory, ambidexterity, Mackey 2-functor, source action, or physical realization."
target_claim: "INTERNAL — arbitrary intermediate morphisms generate a balanced quotient through which every balanced evaluator factors uniquely; verdict: CONSTRUCTED"
canon_verdict_change: none
lean: Lean/GUFormalization/GroupActionBurnsideBisetCoend.lean
probe: tests/channel-swings/group_action_burnside_all_middle_coend_probe.py
---

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: all-middle balance quotient with set-valued factorization and uniqueness
carrier: supplied additive Burnside-span objects, restriction correspondences and arbitrary intermediate morphisms LAYER=toy CHIRALITY=N/A
pairing: NONE
real_structure: UNTYPED; no real, complex, antilinear or Krein structure enters
grading: completed span hom-groups and generated balance-equivalence classes; no physical grading
action_owner: repository-construction; supplied finite group actions only
target: all-intermediate-object balanced quotient MAP-TYPE=quotient
```

# All-middle Burnside balance quotient and universal factorization

## Result

For every intermediate additive Burnside-span object `B`, consider pairs

```text
x in Hom_H(A, Res_phi B),
y in Hom_K(B, Res_psi C).
```

For an arbitrary intermediate morphism `k : B -> B'`, Lean proves the balance
equation joining the pair `(Res(k) after x, y)` at `B'` to `(x, y after k)` at
`B`. Taking the equivalence closure over all objects and all such morphisms
gives an all-middle quotient. Restriction-correspondence composition descends
to it.

The universal surface is explicit: any set-valued evaluator constant on every
balance move factors through the quotient, and a map with the prescribed value
on every representative is unique. This is the set-valued coend factorization
property missing from the preceding fixed-middle construction.

The finite control retains the nonnormal `S3` two-double-coset discriminator
from the fixed-middle result and adds a two-object category in which an actual
bridge morphism joins corresponding representatives. The all-middle quotient
has two classes, the hostile fixed-middle-only version has four, and an
over-quotient has one. Enumeration gives exactly four Boolean balanced
evaluators and four maps from the two-class quotient, with unique
factorization.

## Scientific boundary

This is a genuine all-middle set-valued coend presentation at the current
supplied-action ceiling. It is not an additive or category-valued coend, not a
biset bicategory, not ambidexterity, and not a Mackey 2-functor. It constructs
no source-native action, physical carrier, observable, prediction, or GU
verdict.
