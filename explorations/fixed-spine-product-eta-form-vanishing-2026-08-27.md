---
title: "The fixed-spine product vertical-Dirac eta form vanishes; the global family remains unbuilt"
status: exploration
doc_type: determination
created: "2026-08-27"
grade: "EXACT PRODUCT-FAMILY SPIN-GEOMETRY STATEMENT; NO GLOBAL P(TX) FAMILY OR BASE INTEGRAL"
scripts:
  - tests/dim13/fixed_spine_product_eta_form_probe.py
target_claim: "DIM13-LINK-O3 / M-H5"
target_claim_verdict: "FIXED-SPINE-ETA-ZERO__GLOBAL-ETA-OPEN"
comparator_classification: INTERNAL_STRUCTURAL_ONLY
canon_verdict_change: none
---

# Fixed-spine product eta-form ceiling

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: fixed-spine product vertical-Dirac eta-form vanishing
carrier: product spinor family over RP3 with vertical fiber S6 LAYER=ambient CHIRALITY=S-CHIRALITY-UNTYPED
pairing: standard L2 spinor pairing ON=unit-round-S6 product family
real_structure: complex spin Dirac family with unique vertical spin structure
grading: even-dimensional vertical chirality
action_owner: repository-construction -- global GU end and family remain unbuilt
target: fixed-product Bismut-superconnection eta form MAP-TYPE=pullback from one fixed vertical operator
```

Scope: this result binds only the already verified noncanonical fixed-spine
product `S(nu_x) ~= RP3 x S6`. It neither constructs nor identifies the global
link `S(nu) -> P(TX)`, and it supplies no global horizontal distribution,
superconnection or seven-dimensional base integral.

## The direct product-family argument

Choose the product metric and product horizontal distribution supplied by any
one trivialization of the verified rank-seven normal bundle over the fixed
`RP3` spine. The vertical family is then the constant unit-round `S6` Dirac
operator.

The unit sphere has scalar curvature `6*5=30`, so Lichnerowicz gives

```text
D_S6^2 = nabla* nabla + Scal/4 >= 15/2.
```

The vertical operator is invertible. Because the fiber is even-dimensional,
chirality anticommutes with `D_S6` and pairs every nonzero eigenvalue with its
negative; the degree-zero eta component is zero. Because the family and its
connection are pulled back from one fixed fiber and the product horizontal
curvature is zero, the superconnection integrand has no positive base-degree
component. Hence the complete eta form of this fixed product family is zero.

This is stronger and cleaner than the old one-line reflection suggestion on
the model. It uses no unproved source action and no numerical spectrum.

## Why the reflection shortcut is not the proof

Reflection in the trivial real summand is a globally defined fiberwise map on
the product, but it restricts to a degree-minus-one, orientation-reversing map
of `S6`. It is therefore not silently a Spin-family automorphism; using it as
one would require extra Pin/orientation bookkeeping. The direct constant-family
argument avoids that category error.

The observation matters at the global boundary. Even if a corresponding
fiberwise involution exists over `P(TX)`, one must still construct the global
normal identification, metric, spin/Pin lift, horizontal distribution and
superconnection before claiming that a reflection reverses the actual eta
form. Nothing here supplies those objects.

## Verification and consequence

`python3 tests/dim13/fixed_spine_product_eta_form_probe.py --selftest` checks
the Lichnerowicz, parity, constant-family and scope premises and catches five
planted mutations. M-H5 advances by closing the fixed-product eta clause, but
remains `VERIFIED LIVE` for the actual global normal/TX packet, higher framing,
reflection/spin/horizontal compatibility on that family and the full base
eta-form integral.
