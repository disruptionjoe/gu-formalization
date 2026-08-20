---
title: "Selected-K154 null fivefold second-lower coefficient"
status: active_research
doc_type: exact_second_jet_closed_null_action_and_restricted_fivefold_gate
created: "2026-08-20"
registry: lab/process/selected-k154-null-fivefold-second-lower.json
probe: tests/channel-swings/selected_k154_null_fivefold_second_lower_probe.py
grade: "K154 EXTENDS K153'S EXACT 448-DIMENSIONAL NULL ACTION PACKET THROUGH THE MINIMAL SECOND COEFFICIENT JETS. THE SECOND-JET ACTION CLOSURE REMAINS 32 CLIFFORD LABELS AT BOTH THE REFERENCE AND RATIONALLY ROTATED NULL COVECTORS. THE RAW SECOND JET AND FIRST FORMAL-EULER LOWER JET HAVE RANK 241; THE GENERALIZED PRINCIPAL SECOND JET HAS RANK 260. THE VARIABLE FIFTH POWER HAS A LIVE RANK-16 ORDER-THREE COEFFICIENT [P^5]_3, WHILE A FIRST-JET TRUNCATION CHANGES IT AND FULL FREEZING ERASES IT. K152'S MOVING ORDER-TWO BRIDGE SYMBOL HAS RANK FOUR AND ITS FIRST JET IS LIVE AT RANK ONE. NEVERTHELESS THE DIRECT AND BRIDGE-JET CONTRIBUTIONS TO [K P^5 K A]_5 VANISH SEPARATELY AT BOTH NULL COVECTORS. THIS IS NO RESTRICTED LEAKAGE THROUGH THE SECOND LOWER ORDER, NOT A ZERO FULL CURVED REMAINDER. ORDERS FOUR AND BELOW REMAIN OPEN."
target_claim: K153_NEXT_GATE__NULL_FIVEFOLD_SECOND_LOWER_AND_COMPLETE_ORDER5_BRIDGE_ACTION
target_verdict: NULL_ACTION_PACKET_448D_SECOND_JET_CLOSED__P5_SECOND_LOWER_RANK16_LIVE__MOVING_BRIDGE_FIRST_JET_RANK1_LIVE__RESTRICTED_ORDER5_DIRECT_AND_BRIDGE_JET_TERMS_ZERO_AT_REFERENCE_AND_ROTATED_NULL__ORDERS4_AND_BELOW_OPEN
canon_verdict_change: none
---

# Selected-K154 null fivefold second-lower coefficient

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K154 binds the repository-selected conditional `comm/symi/symi`
distortion operator and K152 mixed bridge on the exact 448-dimensional packets
closed under the selected coordinate action at `n0=(1,0,0,1)` and
`n1=(1,3/5,0,4/5)`. It computes only the second-lower coefficient of `P^5`
and the complete order-five coefficient of `K P^5 K A` along this selected
inner-Spin chart. It does not recover Weinstein's preferred historical Shiab
or compute all coordinate/mixed jets, later lower orders, a quotient, inverse,
domain, BFV class, physical mode, positivity or propagator.

```gu-typed-objects
result: K154 exact null fivefold second-lower coefficient
carrier: LAYER=ambient CHIRALITY=N/A metric 10-packet through a closed Omega1(Cl(7,7)) 448-packet
pairing: DeWitt ON=metric-10 and Hodge/scalar-Clifford ON=distortion-448
real_structure: real Cl(7,7) with exact complex-coordinate bookkeeping
grading: one-form/Clifford grading with finite second-jet action closure
action_owner: repository-construction
target: second-lower restricted fivefold coefficient MAP-TYPE=homomorphism
```

## 0. Route, correction currency and typed coefficient

K153 proves `[K P^5 K A]_6=0` after exact first-jet action closure and leaves
the next total-order coefficient to the minimal second jets. Mechanism-level
retrieval found no later artifact computing that coefficient. K154 continues
the K148-corrected DeWitt chain and K149--K153 moving-operator stack; it does
not consume a superseded source interpretation.

For `P=A(t)D+B(t)`, write the top three coefficient layers of `P^m` as
`T_m D^m + L_m D^(m-1) + M_m D^(m-2)`. At the jet origin, K154 uses the
complete recurrence

```text
T_(m+1) = A T_m,
L_(m+1) = A L_m + A (T_m)' + B T_m,
M_(m+1) = A M_m + A (L_m)' + B L_m.
```

Thus `M_5` requires `A(0)`, `A'(0)`, `A''(0)`, `B(0)` and `B'(0)`. The
formal-Euler identity fixes `B'(0)=-K C_raw''(0)^T/2`; it is not an optional
plain-transpose correction. An independent scalar K149 full composition
matches all three recurrence layers exactly.

## 1. Second-jet closure and live unrestricted coefficient

Closing K152's eight bridge labels under every polynomially live second-jet
selected-Shiab output stabilizes at the same exact carrier for both covectors:

```text
labels = 0,1,...,31,
dimension = 32 * 14 = 448,
lowerer inertia = (260,188).
```

The new jets are live:

```text
rank C_raw''(0) = 241,
rank A''(0) = 260,
rank B'(0) = 241,
rank [P^5]_3 = 16.
```

The reference and rotated packets have the same ranks. A first-jet truncation
still produces a rank-16 candidate but not the same matrix, proving that rank
alone cannot certify the coefficient. Freezing all coefficient motion makes
the second-lower term zero. Replacing the native indefinite lowerer by the
positive identity continues to destroy the frozen fifth-step nilpotence law.

## 2. Complete order-five bridge restriction

K152's bridge has differential orders two and zero, with no order-one
coefficient. At the null jet origin `[P^5]_5=0`. The complete total-order-five
coefficient is therefore

```text
[K P^5 K A]_5
  = K [P^5]_3 K A_2
    + 4 K [P^5]_4 K (A_2)'.
```

The second term cannot be omitted: the moving bridge symbol has rank four and
its first jet has rank one at both exact null covectors. Exact composition
nevertheless gives

```text
K [P^5]_3 K A_2 = 0,
4 K [P^5]_4 K (A_2)' = 0,
[K P^5 K A]_5 = 0
```

separately at `n0` and `n1`. The live rank-16 unrestricted coefficient and
live rank-one bridge jet each land in the relevant annihilating subspaces; the
zero is not caused by freezing either input or by cancellation between the two
terms. Hence the metric radical and diffeomorphism image have no leakage at
this order.

## 3. Claim ceiling and next gate

K154 advances the exact restricted-zero boundary from order six through order
five. It does not prove `P^5=0`, `K P^5 K A=0`, preservation at every lower
order, or an endomorphism of `H_n/G_n`. The calculation is exact on the two
selected null representatives and selected inner-Spin coordinate chart; it is
not an all-chart or mixed-jet theorem.

K155 should compute the complete order-four coefficient. That horizon first
combines `[P^5]_2`, the first and second jets of the moving order-two bridge,
and K152's Weyl-dependent zero-order bridge coefficient, so it needs the
minimal third coefficient jets and must retain the same closure, recurrence,
pairing, frozen, truncation, reference/rotated and nonvacuity controls.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k154_null_fivefold_second_lower_probe.py
```
