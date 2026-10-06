---
title: "K1216--K1220 general-unital directional visibility/Bell boundary"
status: working_draft_verified
doc_type: conditional_research_result
created: "2026-10-06"
classification: INTERNAL_CONDITIONAL_MATHEMATICS
direction: observed_to_native
claim_effect: none
---

# K1216--K1220 general-unital directional visibility/Bell boundary

```gu-typed-objects
result: sharp relation between general unital-qubit transfer data, directional visibility and optimized CHSH
carrier: imported unital qubit channel and Bell-Choi output LAYER=observed CHIRALITY=N/A
pairing: imported trace/Born state-effect pairing ON=repository_quantum_control
real_structure: real 3x3 Bloch-transfer representation of a complex two-level Hilbert control
grading: directional matrix elements versus singular-spectrum and full-transfer calibration
action_owner: UNTYPED -- no GU owner for the channel, state, pairing, process frames or apparatus
target: cross-anchor identifiability and calibration burden MAP-TYPE=evaluation
```

## Question and ceiling

K1211--K1215 proved the sharp visibility/CHSH relation inside a unital
Pauli-diagonal channel with aligned axes. This packet asks what survives for a
general unital qubit channel when the input and output frames need not be its
principal axes.

Everything here remains an imported finite-dimensional calibration control.
The channel, Bell-Choi preparation, trace/Born pairing, qubit closure,
preparation and measurement frames, locality and apparatus are not supplied by
GU. The calibration anchors earn no prediction or confirmation credit, and
delayed-choice entanglement swapping remains reserved and unscored.

## K1216: Choi correlations preserve the transfer singular spectrum

Write a trace-preserving unital qubit channel in Bloch form

```text
r_out = M r_in,       M in R^(3x3).
```

The Bell state `Phi+` has Pauli correlation matrix
`D=diag(1,-1,1)`. Applying the channel on the first factor gives

```text
T = M D.
```

Because `D D^T=I`,

```text
T T^T = M D D^T M^T = M M^T.
```

Thus the Bell-output correlation singular values are exactly the singular
values `s_1>=s_2>=s_3` of `M`. The optimized CHSH criterion is therefore

```text
S_max = 2 sqrt(s_1^2+s_2^2).
```

The identity is checked on a Pauli diagonal channel, a cyclic unitary rotation
and a rotated rank-one channel. It requires no diagonalization convention.

## K1217: one directional visibility has a wider sharp envelope

Let the measured signed transfer be

```text
V = a^T M b
```

for unit preparation and readout axes `b` and `a`. Since
`|a^T M b|<=s_1`,

```text
S_max/2 = sqrt(s_1^2+s_2^2) >= |V|.
```

A rotated rank-one Pauli channel with singular values `(|V|,0,0)` attains the
lower endpoint. Every unital qubit channel contracts the Bloch ball, so
`s_1,s_2<=1`; hence `S_max<=2sqrt(2)`. A unitary rotation can be chosen with
`a^T R b=V` for every `V` in `[-1,1]`, and all its singular values equal one.
It attains the upper endpoint. Therefore the sharp class-wide interval is

```text
2 |V| <= S_max <= 2 sqrt(2).
```

This is strictly wider than K1212's Pauli principal-axis upper bound
`2sqrt(1+V^2)` whenever `|V|<1`.

## K1218: exact same-visibility separator

At `V=2/5`, the rank-one channel `diag(2/5,0,0)` has canonical Pauli
probabilities `(7,7,3,3)/20`, singular values `(2/5,0,0)` and

```text
S_max^2/4 = 4/25.
```

The unitary `z`-rotation with
`cos(theta)=2/5`, `sin(theta)=sqrt(21)/5` has the same measured matrix entry
and singular values `(1,1,1)`, so

```text
S_max^2/4 = 2.
```

The same directional visibility can therefore range from a sub-classical
rank-one score to the Tsirelson maximum.

## K1219: even three aligned reads do not identify the general score

Three same-label transfers report only the diagonal of `M`. The completely
depolarizing channel `M=0` and the cyclic rotation

```text
    [0 1 0]
P = [0 0 1]
    [1 0 0]
```

both have diagonal `(0,0,0)`. The first has singular values `(0,0,0)` and
`S_max^2/4=0`; the second is an `SO(3)` unitary rotation with singular values
`(1,1,1)` and `S_max^2/4=2`. Off-diagonal frame transport is load-bearing.

## K1220: calibration boundary

Inside the frozen unital-qubit/Bell-Choi/Born class:

- one directional read supplies only the sharp interval above;
- three same-axis reads remain insufficient without independent
  Pauli/principal-axis validation;
- three singular values determine optimized CHSH; and
- the full signed `3x3` transfer matrix is sufficient because its two largest
  singular values determine the score.

K1211--K1215 remains exact as the independently validated Pauli-aligned
subclass. K1004 remains a dephasing-horn theorem and K1009 remains a distinct
common-contrast model. No source, ledger, canon, paper, public-posture,
prediction, confirmation or protected verdict moves.

## Reproduction and hostile controls

Five producers pass `49/49` declared controls. Five probes reject `44/44`
hostile mutations. The checks cover the Choi Gram identity, both sharp
endpoints, the exact `V=2/5` separator, the zero-diagonal cyclic rotation and
the ownership/holdout firewall.
