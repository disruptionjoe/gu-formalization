---
title: "K104 K91-to-K155 action bridge obstruction"
status: active_research
doc_type: typed_same_carrier_pairing_inertia_and_Weyl_coefficient_admission_result
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact non-admission of the frozen K104 K91 action to the exact K155 fixture because its positive real l2 adjoint pairing is not congruent to the K155 distortion lowerer's mixed inertia (260,188,0), and K104 owns no Weyl-dependent same-order A0; no obstruction to all actions, no source verdict, no K155 recomputation and no GU-wide no-go
manifest: lab/process/k104-k91-k155-action-bridge-obstruction-wave.json
probe: tests/channel-swings/k104_k91_k155_action_bridge_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K104 K91-to-K155 action bridge obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this is the hostile admission test for one frozen repository action:
K104's K91 split-`l2` action. It asks whether a real injective same-carrier map
can preserve the pairing that defines the formal adjoint and Green form while
landing on K155's exact distortion packet, and whether K104 owns the
same-order Weyl coefficient used by the fixture. It does not ask whether some
other action could pass.

```gu-typed-objects
result: the frozen K104 K91 action fails K155 admission at adjoint-pairing inertia and Weyl-dependent coefficient ownership
carrier: first 448 physical K104 l2 modes versus K155 metric-10 plus closed Omega1(Cl(7,7)) distortion-448 LAYER=ambient CHIRALITY=N/A
pairing: positive real l2 on K104 versus K155 Hodge/scalar-Clifford distortion lowerer of inertia (260,188,0) ON=frozen_packet
real_structure: real l2 and real Cl(7,7) remain distinct; a real congruence is required and complexification is not a repair
grading: K104 free shift-gauge/BV grading versus K155 moving-action coefficient-jet grading, with no identified graded map
action_owner: repository-construction -- K104 owns K91 only and the separate K155 selected conditional action owns its Weyl A0
target: same-carrier action/adjoint/Green and same-order coefficient admission to the exact K155 fixture MAP-TYPE=evaluation
```

## Inline preflight bookend

The independent gate was derived from K103's six absent K91 bridges and five
absent K155 bridges, not from the K104 construction packet's preferred story.
The lens census covered Sylvester inertia, real congruence, formal-adjoint
pairings, Green forms, coefficient jets, curvature inputs, real-form typing and
claim ceilings. Retrieval fixed K155's exact `(260,188,0)` distortion-lowerer
inertia, rank-nine Weyl zero-order bridge and rank-one rotated metric-radical
leakage. No later artifact changes those values.

The cheapest decisive condition is pairing congruence before any 448-by-448
fixture recomputation. A dimension check alone is deliberately planted as a
non-kill: the first 448 K104 modes do form a real 448-dimensional subspace.
The question is whether that embedding preserves the action's adjoint/Green
pairing. A mixed-sign planted comparator supplies the positive control.

## The inertia obstruction

K104 uses the positive real `l2` pairing. On its first 448 physical modes the
pairing matrix has inertia

```text
inertia(K_K104) = (448,0,0).                                (1)
```

K155's exact distortion lowerer has

```text
inertia(K_K155) = (260,188,0).                              (2)
```

An action-preserving bridge must at least preserve the pairing used to define
the formal adjoint and Green boundary form. For a real injective square map
`T` on the proposed 448-dimensional same carrier this requires

```text
T^T K_K104 T = K_K155.                                     (3)
```

Sylvester's law of inertia makes (3) impossible: real congruence preserves the
numbers of positive, negative and null directions, while (1) and (2) differ by
188 negative directions. This is not a dimension obstruction and not an
artifact of a chosen basis. A planted coefficient with inertia `(260,188,0)`
removes this discriminator, proving the test is sensitive to the required
structure rather than rejecting every 448-dimensional packet.

The conclusion is limited to the frozen positive-pairing K104 action. A new
indefinite action could clear this first gate, subject to every remaining
gauge, BV, domain, Green and coefficient obligation.

## The independent coefficient obstruction

K155's complete order-four fixture uses a Weyl-dependent zero-order bridge of
rank nine. At the reference null covector its metric-radical leakage is zero;
at the fixed rationally rotated covector the leakage has rank one and is
carried solely by that Weyl term. K104 has no curvature variable, Weyl input or
same-order `A_0` coefficient. It therefore cannot reproduce the fixture or
supply an action-owned correction to it.

This is independent of (1)--(3). Even a later indefinite pairing must own the
actual Weyl-dependent coefficient before K155 recomputation is licensed.
K155's existing branch-local verdict remains unchanged.

## What moved

The single-packet K103 reopener splits cleanly:

```text
K91 action/BV/domain/Green owner       CLOSED by K104
same-carrier adjoint pairing to K155   FAILS for K104 by inertia
same-order Weyl A0 owner               ABSENT from K104
K155 exact fixture                     NOT RECOMPUTED; verdict preserved
```

The next candidate cannot be obtained by embedding 448 modes, changing basis,
complexifying or adjoining K155 after the fact. It must be constructed on the
actual K155 field carrier with an adjoint/Green pairing of inertia
`(260,188,0)`, an explicitly owned Weyl-dependent `A_0`, and gauge/BV/domain/
Green maps that still descend to K91.

## Inline postflight bookend

- **Strongest overclaim:** reading the mismatch as an all-action or GU no-go.
  Refused: only the positive-pairing K104 action fails.
- **Strongest contrary construction:** an indefinite K155-carrier action with
  its own Weyl coefficient may exist. It is the exact reopener and is not
  prejudged.
- **Weakest reproducibility seam:** pairing preservation could be weakened to a
  non-injective or quotient map. Such a map would not be the same-carrier
  action/adjoint bridge K103 requires; if proposed, its kernel and descended
  physical pairing must be separately owned rather than hidden.

The exact probe passes `20/20`; its baseline-first hostile selftest catches
`15/15` mutations. Source ownership, K155's result, prediction, confirmation,
canon and public posture do not move.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  tests/channel-swings/k104_k91_k155_action_bridge_obstruction_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  tests/channel-swings/k104_k91_k155_action_bridge_obstruction_probe.py --selftest
```
