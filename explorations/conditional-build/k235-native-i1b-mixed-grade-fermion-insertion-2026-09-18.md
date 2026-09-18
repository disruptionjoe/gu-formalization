---
title: "K235 native I1B mixed-grade mode and displayed four-field insertion"
status: active_research
doc_type: exact_local_bosonic_symbol_and_formal_fermion_candidate_insertion
created: "2026-09-18"
registry: lab/process/k235-native-i1b-mixed-grade-fermion-insertion.json
solver: tests/channel-swings/k235_native_i1b_mixed_grade_fermion_insertion.py
probe: tests/channel-swings/k235_native_i1b_mixed_grade_fermion_insertion_probe.py
grade: "EXACT ONE-ENTRY SELECTED-I1B MIXED-GRADE SYMBOL AND FORMAL ALL-SLOT INSERTION INTO THE DISPLAYED SOURCE FERMION CANDIDATE; NO SELECTED FULL OPERATOR, COMMON DOMAIN OR PHYSICAL MODE"
canon_verdict_change: none
---

# K235 native I1B mixed-grade mode and four-field insertion

> **GU-COMPARATOR-ROUTING — scope before inference.** This uses the native
> first-order bosonic action and the source-displayed four-field operator,
> not a conventional Einstein/Dirac, Higgs/VEV or ordinary chiral-family
> comparator. Read `lab/methods/source-native-comparator-routing.md` and the
> exact source/ledger rows before transferring any result.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: one nonzero selected-I1B Cl1/Cl2 normal-symbol cross and the first variation of all sixteen cells of the displayed draft four-field candidate; no physical mode
carrier: native Omega1(Cl(7,7)) distortion at local T=0 and the displayed four-field full-Dirac S insertion LAYER=ambient+source-print BRIDGE=local_clifford_action CHIRALITY=S-FULL-DIRAC
pairing: selected-Shiab formal I1B trace/Hodge normal coefficient on the distortion block; source-displayed fermion bilinear remains formal ON=local_bosonic_symbol_and_candidate_spinor_matrix
real_structure: real Cl(7,7) coefficient for the bosonic cross; global barred-field reality and operative fermion adjoint UNTYPED
grading: Cl1 odd and Cl2 even under locally supplied full-Dirac volume chirality; source-global plus/minus interpretation remains UNTYPED
action_owner: source-print for the candidate four-field matrix; repository-construction for the selected comm/symi/symi Shiab and this local mixed mode
target: formal candidate insertion and its exact missing global/domain inputs, not physical cohomology MAP-TYPE=not-a-map
```

## Exact first attempt

On the K127/K128 local flat Ricci-flat `T=0`, zero-fermion stationary germ,
take independent distortion directions

```text
o = dx^0 tensor gamma_1        (Cl1, odd),
e = dx^2 tensor gamma_1 gamma_2 (Cl2, even).
```

This is the selected `comm/symi/symi` Shiab coefficient of `I1B`, not a
uniquely selected historical Shiab or an imported Maxwell mode. Fix a formal
normal `n=dx^0`. In the full 28-dimensional invariant label block (label
`2` and its normal flip `3`), the ordered raw-density contractions are
`B_n(o,e)=2` and `B_n(e,o)=0`. Formal integration by parts gives
`E_n(o,e)=(2-0)/2=1`, `E_n(e,o)=-1`; the block has rank six. The independent
all-basis replay agrees with the direct selected-Shiab contraction and
detects a wrong first product channel, which kills this entry. Distortion
transforms tensorially at `T=0`; K132's action-owned diffeomorphism generator
has no distortion column, so this pair is non-gauge *as a bosonic symbol
direction*. It is not a physical quotient eigenmode.

For the **displayed** draft-2021 equation (9.16) candidate only, complex
`Cl(7,7)` volume chirality makes `o` off-diagonal and `e` diagonal in a
locally supplied `S=S+⊕S-` grading. Holding the metric and `d0` fixed, write
their spin-action blocks as `O_pm,O_mp` and `E_pp,E_mm`. Differentiating
every displayed cell gives the formal insertion (row/column order exactly
as the source extraction):

The exact Clifford squares are `gamma_1²=-1` and
`(gamma_1 gamma_2)²=-1`. Thus, in this local full-Dirac Clifford
representation, both odd off-diagonal maps and both even diagonal maps are
invertible between their corresponding halves. This certifies nonzero
unstarred spin-action blocks; it does not imply the separate `*odot` maps,
formal barred maps or their globally closed operators are invertible.

```text
  [ *odot(E_pp)    *odot(O_pm)       E_pp          O_pm ]
  [ *odot(O_mp)    *odot(E_mm)       O_mp          E_mm ]
  [ -bar(E_pp)*    -bar(O_pm)*       0             0    ]
  [ -bar(O_mp)*    -bar(E_mm)*       0             0    ]
```

All twelve potentially nonzero entries and the four displayed southeast
zeros are retained. The `bar` and star symbols remain formal: the draft
describes barred and unbarred fields as four independent classical fields,
and the extraction does not select their global reality, density, pairing
or operative adjoint. The source says one can *begin with operators like*
this matrix and explicitly admits a nonzero southeast variant. The local
Clifford parity is not a source selection of the complete operator.

## What this changes and what it does not

This meets the first source-facing challenger with an actual native non-gauge
bosonic cross coefficient and a complete **formal displayed-candidate**
fermion insertion on the same local zero-fermion germ. It removes the excuse
that the selected low-grade bosonic mode or its source-matrix slot pattern is
not even calculable. It does **not** construct a nonzero-fermion stationary
background; at zero fermion the even bilinear current starts at cubic order
and the quadratic boson/fermion Hessian remains a direct sum (the prior K77
current-order theorem). Thus the matrix above is an operator response/vertex,
not a mixed boson–single-fermion quadratic entry or a common eigenmode.

The exact next dependency for physical use is an action-owned choice of the
full `S` grading/representation and the complete fermion operator branch,
with barred-field reality/density/adjoint and a common closed domain on a
source-legal stationary background. Only then test coupled constraints,
boundary/BV quotient, positive real/Krein pairing, observed representations
and `2+1`/chirality. The source admits the displayed ingredients but does
not select that complete package. The local flat germ does not become a
source-global vacuum. The selected-Shiab cross entry cannot settle the
different Shiab members or a supplied Maxwell model.

Strongest contrary reading: calling `E_n(o,e)=1` a physical propagating
mixed mode confuses one principal coefficient with a closed action/operator
and quotient. Strongest source objection: interpreting `S+/-` as source-
selected at equation (9.16) ignores its unsubscripted full Dirac carrier and
the candidate/nonzero-southeast warnings. Weakest reproducibility seam is
the local Clifford-to-global bundle/adjoint descent; the independent probe
replays the *local* 28-basis calculation, not that missing seam. A wrong
product-channel plant nulls the entry, while reversing one direction flips
its sign. No external specialist novelty or acceptance is asserted.

SC-ACT-01/02 remain `ASSERTS`, SC-META-53 remains `UNCERTAIN`, and ledger
v0.263 LT-GR6b/LT-SM8 remain `NEEDS`. K224's `1.7933e-22` farther-headroom,
K229's 81.83-times selected upper, K234's fixed-ray result, K215, the
coalescent/quotient/reference boundaries and the inherited broad full-rule
ceiling are unchanged. No source register, physics ledger, canon, physical
claim, paper or public posture moves.

Reproduce:

```sh
PYTHONDONTWRITEBYTECODE=1 _local/cas-venv/bin/python tests/channel-swings/k235_native_i1b_mixed_grade_fermion_insertion.py
PYTHONDONTWRITEBYTECODE=1 _local/cas-venv/bin/python tests/channel-swings/k235_native_i1b_mixed_grade_fermion_insertion_probe.py
```
