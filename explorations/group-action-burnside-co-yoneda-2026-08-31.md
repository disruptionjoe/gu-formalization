---
artifact_type: exploration
status: active_research
doc_type: exact_additive_co_yoneda_equivalence
created: 2026-08-31
title: "Additive co-Yoneda for Burnside restriction correspondences"
owner: gu-formalization
claim_status: repository_derived
claim_ceiling: "Additive equivalence between the supplied all-middle coend and iterated restriction-correspondence hom group; no biset bicategory, 2-morphism coherence, ambidexterity, Mackey 2-functor, source action, or physical realization."
target_claim: "INTERNAL — composition from the additive all-middle coend is an additive equivalence with canonical identity-leg inverse; verdict: CONSTRUCTED"
canon_verdict_change: none
lean: Lean/GUFormalization/GroupActionBurnsideCoYoneda.lean
probe: tests/channel-swings/group_action_burnside_co_yoneda_probe.py
---

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: additive co-Yoneda equivalence for supplied restriction correspondences
carrier: additive all-middle coend and actual iterated restriction-correspondence hom group LAYER=toy CHIRALITY=N/A
pairing: NONE
real_structure: UNTYPED; no real, complex, antilinear or Krein structure enters
grading: additive Burnside hom groups; no physical grading
action_owner: repository-construction over supplied finite group actions and restriction functors
target: composition is an additive equivalence MAP-TYPE=isomorphism
```

# Additive co-Yoneda for Burnside restriction correspondences

## Result

The additive all-middle quotient is now identified with the represented
iterated restriction-correspondence group. Composition supplies the forward
additive map. The inverse sends an already-composed correspondence to the
canonical middle object `Res_psi C`, retaining the correspondence as its first
leg and using the identity as its second leg.

The right inverse is ordinary composition with an identity. The left inverse
is the co-Yoneda balance relation: every pair `[x,y]` is equal to the canonical
identity-leg pair `[x compose Res(y), id]`. Lean proves both homomorphism
equalities and packages composition as an additive equivalence.

The exact GF(2) control uses the earlier eight-generator, two-middle-object
presentation. Its quotient and target are both one-dimensional, composition
is nonzero, and every generator differs from the canonical section of its
composite by generated relations. Removing balance makes the two middle-object
generators inequivalent; removing either additivity family leaves a kernel.

## Scientific boundary

This is a hom-group co-Yoneda theorem. It is not a biset bicategory: no
2-morphism carrier, horizontal 2-composition, associator, unitor, pentagon or
triangle coherence is constructed. It proves no ambidexterity or Mackey
2-functor and supplies no source-native or physical realization.
