---
title: "Selected-K155 null fivefold third-lower coefficient"
status: active_research
doc_type: exact_third_jet_closed_null_action_and_restricted_fivefold_gate
created: "2026-08-20"
registry: lab/process/selected-k155-null-fivefold-third-lower.json
probe: tests/channel-swings/selected_k155_null_fivefold_third_lower_probe.py
grade: "K155 EXTENDS THE EXACT 448-DIMENSIONAL SELECTED-ACTION PACKET THROUGH THE MINIMAL THIRD COEFFICIENT JETS. TEN-POINT EXACT INTERPOLATION CERTIFIES THE DEGREE-NINE MOVING-SHIAB POLYNOMIAL AND THE SAME 32-LABEL CLOSURE. AT BOTH NULL COVECTORS THE RAW THIRD JET AND SECOND FORMAL-EULER LOWER JET HAVE RANK 238, THE PRINCIPAL THIRD JET RANK 258, AND [P^5]_2 RANK 82. K152'S ORDER-TWO BRIDGE HAS JET RANKS 4,1,4 AND ITS WEYL-DEPENDENT ZERO-ORDER COEFFICIENT HAS RANK 9. ALL FOUR ORDER-FOUR CONTRIBUTIONS AND THEIR COMPLETE SUM HAVE RANK ONE. THEY KILL DIFFEOMORPHISMS AT BOTH COVECTORS. ON THE FIXED NONZERO ALIGNED WEYL BACKGROUND THE REFERENCE ROW FACTORS THROUGH ELL_N, BUT THE RATIONALLY ROTATED COVECTOR HAS EXACT RANK-ONE METRIC-RADICAL LEAKAGE CARRIED SOLELY BY THE WEYL ZERO-ORDER TERM. THE FLAT CONTROL REMOVES THAT LEAKAGE. THIS KILLS RADICAL DESCENT FOR THIS SELECTED CONDITIONAL BRANCH AND FIXTURE; IT IS NOT A VERDICT ON THE UNRECOVERED HISTORICAL SHIAB OR GU."
target_claim: K154_NEXT_GATE__NULL_FIVEFOLD_THIRD_LOWER_AND_COMPLETE_ORDER4_BRIDGE_ACTION
target_verdict: NULL_ACTION_PACKET_448D_THIRD_JET_CLOSED__P5_THIRD_LOWER_RANK82_LIVE__COMPLETE_ORDER4_RANK1_GAUGE_ZERO__ROTATED_METRIC_RADICAL_LEAKAGE_RANK1_WEYL_ZERO_ORDER_ONLY__SELECTED_BRANCH_DESCENT_ROUTE_KILLED
canon_verdict_change: none
---

# Selected-K155 null fivefold third-lower coefficient

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K155 binds the repository-selected conditional `comm/symi/symi`
distortion operator and K152 bridge on the exact 448-dimensional packets at
`n0=(1,0,0,1)` and `n1=(1,3/5,0,4/5)`. It computes one pure-coordinate third
jet of the selected inner-Spin chart and the corresponding complete order-four
coefficient of `K P^5 K A` on K152's fixed aligned Ricci-flat Weyl family.
The rotated covector is tested in that same fixed background; this is not a
co-rotation of the background or an all-chart covariance theorem. The result
does not recover Weinstein's preferred historical Shiab or define a quotient,
inverse, domain, BFV class, physical mode, positivity or propagator.

```gu-typed-objects
result: K155 exact null fivefold third-lower coefficient and radical-leakage witness
carrier: LAYER=ambient CHIRALITY=N/A metric 10-packet through a closed Omega1(Cl(7,7)) 448-packet
pairing: DeWitt ON=metric-10 and Hodge/scalar-Clifford ON=distortion-448
real_structure: real Cl(7,7) with exact complex-coordinate bookkeeping
grading: one-form/Clifford grading with finite third-jet action closure
action_owner: repository-construction
target: third-lower restricted fivefold coefficient MAP-TYPE=homomorphism
```

## 0. Exact route and interpolation certificate

K154 proves `[K P^5 K A]_5=0` and leaves order four to third coefficient
jets and K152's zero-order bridge. Mechanism retrieval found no later
calculation of that complete coefficient. K155 continues the K148-corrected
DeWitt chain and K149--K154 moving-operator stack without importing a
superseded source reading.

For the third-order conjugation series, `Phi_1(t)` has degree three and
`Phi_2(t)=Phi_1(t) wedge Phi_1(t)/2` has degree six. The selected two-term
Shiab is therefore degree at most nine. Ten exact rational samples determine
its support and coefficient jets. This replaces an expensive symbolic support
simplification without changing the polynomial object.

For `P=A(t)D+B(t)`, the coefficient recurrence is

```text
C_(m+1,r) = A C_(m,r-1) + A (C_(m,r))' + B C_(m,r).
```

K155 propagates only the coordinate jets that can reach the top four layers.
An independent scalar K149 composition agrees exactly at orders `5,4,3,2`.

## 1. Third-jet closure and live unrestricted layer

Both null packets close on the same carrier:

```text
labels = 0,1,...,31,
dimension = 32 * 14 = 448,
lowerer inertia = (260,188).
```

The new exact ranks agree at `n0` and `n1`:

```text
rank C_raw'''(0) = 238,
rank A'''(0) = 258,
rank B''(0) = 238,
rank [P^5]_2 = 82.
```

The preceding fifth-power ranks replay as `0,4,16` at orders `5,4,3`.
Removing the third principal and second lower jets changes `[P^5]_2`; full
freezing erases it. The native indefinite lowerer remains essential to the
frozen fifth-step nilpotence.

## 2. Complete order-four bridge coefficient

K152 has bridge orders two and zero and no order-one coefficient. Since
`[P^5]_5=0` at the null jet origin, the complete order-four coefficient is

```text
[K P^5 K A]_4
  = K [P^5]_2 K A_2
    + 3 K [P^5]_3 K (A_2)'
    + 6 K [P^5]_4 K (A_2)''
    + K [P^5]_4 K A_0.
```

The order-two bridge has exact jet ranks `4,1,4`; the Weyl-dependent
zero-order coefficient has rank nine. Every displayed contribution has rank
one and their sum has rank one at both covectors. The complete coefficient
annihilates the four-dimensional diffeomorphism image at both covectors.

The principal metric radical behaves differently on the fixed nonzero Weyl
background:

```text
n0: rank([K P^5 K A]_4 restricted to H_n0) = 0,
n1: rank([K P^5 K A]_4 restricted to H_n1) = 1.
```

At `n1`, the first three derivative contributions separately annihilate
`H_n1`; the rank-one leakage is carried solely by the Weyl-dependent `A_0`
term. The flat control `q=0` removes it. One exact witness in metric-slot order
`(00,01,02,03,11,12,13,22,23,33)` is

```text
h = (6/5,1,0,0,0,0,0,0,0,0),
ell_n1^T h = 0,
([K P^5 K A]_4 h)_224 = 2532096 q / 125 != 0 for q != 0.
```

Thus this is curvature-dependent restricted leakage, not failure of the
diffeomorphism identity and not an artifact of the variable differential
terms.

## 3. Route verdict and reopening condition

The selected conditional null-characteristic radical-descent route fails on
this exact nonzero Weyl fixture at order four. Lower orders cannot repair a
failure of the order-four coefficient, so continuing mechanically to K156 is
not licensed for this route.

The verdict is branch- and construction-scoped. It does not bind the
unrecovered preferred historical Shiab, a different source/action-selected
coefficient, or a separately owned same-order correction. Reopen this descent
candidate only when one of those owners is supplied and typed strongly enough
to recompute the complete order-four coefficient. Otherwise return to the
broader GU substantial-arc frontier rather than extending the K-sequence.

Reproduce:

```bash
uv run --with sympy==1.14.0 python \
  tests/channel-swings/selected_k155_null_fivefold_third_lower_probe.py
```
