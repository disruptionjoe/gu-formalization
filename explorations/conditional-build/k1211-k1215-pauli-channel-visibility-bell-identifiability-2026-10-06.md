---
title: "K1211--K1215 Pauli-channel visibility/Bell identifiability envelope"
status: active_research
doc_type: conditional_cross_anchor_identifiability
created: 2026-10-06
claim_ceiling: exact finite Pauli-channel calibration boundary only
target_claim: NONE-NOT-A-KILL
---

# K1211--K1215 Pauli-channel visibility/Bell identifiability envelope

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: sharp relation between Pauli transfer data, fringe visibility and optimized CHSH
carrier: imported unital Pauli-diagonal qubit channel and Bell-Choi output LAYER=observed CHIRALITY=N/A
pairing: imported trace/Born state-effect pairing ON=repository_quantum_control
real_structure: complex two-level Hilbert control with Hermitian adjoint
grading: one-axis and two-axis calibration versus full diagonal transfer
action_owner: UNTYPED -- no GU owner for the channel, state, pairing, axes or apparatus
target: cross-anchor identifiability and calibration burden MAP-TYPE=evaluation
```

K1211 writes a Pauli-diagonal channel as

```text
E(I)=I, E(X)=lambda_x X, E(Y)=lambda_y Y, E(Z)=lambda_z Z.
```

Its four Pauli probabilities are

```text
(1 + lambda_x + lambda_y + lambda_z)/4,
(1 + lambda_x - lambda_y - lambda_z)/4,
(1 - lambda_x + lambda_y - lambda_z)/4,
(1 - lambda_x - lambda_y + lambda_z)/4.
```

Complete positivity is exactly their nonnegativity, equivalently
`1+lambda_z >= |lambda_x+lambda_y|` and
`1-lambda_z >= |lambda_x-lambda_y|`. Acting on one half of `Phi_plus`
gives correlation tensor `diag(lambda_x,-lambda_y,lambda_z)`, so optimized
CHSH is twice the square root of the sum of the two largest squared transfer
coefficients.

K1212 fixes one nonnegative fringe axis `lambda_x=V`. Complete positivity
implies

```text
lambda_y^2 + lambda_z^2
 <= ((1+V)^2 + (1-V)^2)/2
 = 1+V^2.
```

Together with `|lambda_i|<=1`, every two-coordinate squared sum is at most
`1+V^2`, while the two largest squares sum to at least `V^2`. Both bounds are
attained:

```text
diag(V,0,0):   S_max=2V,
diag(V,V,1):   S_max=2 sqrt(1+V^2).
```

Thus the sharp fixed-visibility interval is

```text
2V <= S_max <= 2 sqrt(1+V^2).
```

K1213 freezes the rational separator `V=2/5`. The channel
`diag(2/5,0,0)` has `S_max^2/4=4/25` and is CHSH-local, while
`diag(2/5,2/5,1)` has `S_max^2/4=29/25` and violates CHSH. Both are exact CP
Pauli mixtures. The K1004 equality is therefore a theorem of its imported
dephasing horn, not a law of visibility alone.

K1214 fixes two signed transfer reads. Complete positivity leaves precisely

```text
|lambda_x+lambda_y|-1 <= lambda_z <= 1-|lambda_x-lambda_y|.
```

At `(lambda_x,lambda_y)=(4/5,3/5)`, the interval is `[2/5,4/5]`.
The lower endpoint gives `S_max^2/4=1`; the upper gives `32/25`. Identical
two-axis data can therefore touch the classical boundary or violate CHSH.

K1215 closes only the conditional calibration question. Three transfer
magnitudes identify optimized CHSH inside the frozen Pauli-diagonal Bell-output
class; three signed coefficients identify the Pauli probabilities and channel
inside that class. Unitality, trace preservation, Pauli diagonality, common
axis transport, the Bell state, trace/Born pairing, locality and apparatus
remain independent imported obligations. K1009's two-parameter common-contrast
model is retained, and delayed-choice entanglement swapping remains a distinct
unscored held-out family.

The calibration anchors earn no prediction or confirmation credit. No GU
state, channel, quotient, observable algebra, Born rule, local net, apparatus,
source claim, ledger row, canon surface, paper or public posture moves.

## Hostile review

- Strongest overclaim: treating `V` as a universal Bell witness. K1213 gives
  exact channels with the same `V` and opposite CHSH dispositions.
- Strongest contrary construction: the lower horn `diag(V,0,0)` is CP for all
  `0<=V<=1` and never violates CHSH, even though the K1004 horn violates for
  every positive `V`.
- Weakest seam: the theorem assumes a common Pauli-diagonal channel and aligned
  transfer axes across the interference and Bell controls. It does not prove
  that any physical apparatus, much less GU, supplies that identification.

## Next condition

Construct a typed owner for the state/effect pairing and channel axes, or
validate a broader non-Pauli channel class. Preserve delayed-choice
entanglement swapping as the distinct held-out family and do not use the
calibration anchors themselves for confirmation credit.
