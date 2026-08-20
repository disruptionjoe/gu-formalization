---
title: "B5 four-stage roll-support gate: the strict stage-preserving fold has an eight-block ceiling"
status: active_research
doc_type: exact_action_complex_gate
created: "2026-08-20"
registry: lab/process/b5-four-stage-roll-support.json
probes:
  - tests/channel-swings/b5_four_stage_roll_support_probe.py
grade: "AT THE INDEPENDENT B5 FORMAL COMPACT-CORE AND COARSE MULTIPLICITY GRADE, THE TYPED 0->1->13->14 COCHAIN COMPLEX WITH STAGE-PRESERVING HODGE/KREIN HIGH-TO-LOW ROLLS HAS EXACTLY EIGHT ELIGIBLE S/I/R BLOCKS AND STRUCTURALLY ZERO S->S. AN EXACT ACYCLIC 1->2->2->1 CONTROL RETAINS ALL EIGHT ELIGIBLE BLOCKS AND NORMALIZED W131 Q=1. THE CURRENT FULL-NINE-BLOCK STAGE-B FAMILY IS THEREFORE NOT THE ROLL OF THIS STRICT DIFFERENTIAL. THIS DOES NOT EXCLUDE A FILTERED GRAPH/BV ROLL THAT MIXES STAGES OR AN EIGHT-BLOCK DIFFERENTIAL WITH A SEPARATE EULER/DIRAC TERM."
target_verdict: B5_STRICT_FOUR_STAGE_FOLD_HAS_EIGHT_BLOCK_CEILING
target_claim: internal target B5-ACTION-OWNED-FOUR-STAGE-DIFFERENTIAL; verdict strict stage-preserving fold cannot realize current full-nine-block family
canon_verdict_change: none
---

# B5 four-stage roll-support gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds only the repository's independently typed B5
`U0 -> U1 -> U2 -> U3` carrier, the declared stage-preserving Hodge/Krein
high-to-low fold, and the coarse `S + imGamma + kerGamma` support bookkeeping.
It does not recover Weinstein's historical preferred middle differential,
construct the full `128 -> 1792 -> 1792 -> 128` maps, choose a filtered graph
embedding, select a pairing, prove global cohomology, or infer a particle or
GU verdict.

```gu-typed-objects
result: a strict stage-preserving B5 four-stage fold has eight-block support and cannot equal the current full-nine-block Stage-B family
carrier: U0=S, U1=I+R, U2=(I+R)^vee_dens, U3=S^vee_dens; folded halves E=S+I+R LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: formal Hodge/Krein primalization on the high-form density-dual stages; normalization and global domain remain UNTYPED ON=four-stage-carrier
real_structure: underlying complex cochain carrier; native Lorentzian real structure and absolute coflip trivialization remain UNTYPED
grading: integer cochain degree 0,1,2,3 with ordinary form degrees 0,1,13,14
action_owner: repository-construction at strict stage-preserving fold grade; filtered graph/BV mixing remains unowned
target: eligibility of the current full-nine-block Stage-B family as a rolled strict differential MAP-TYPE=evaluation
```

## Layer 0: three different operators

The 2026-07-29 first write typed the four stages as

```text
U0 = S                         rank 128,  form 0
U1 = I + R                     rank 1792, form 1
U2 = (I + R)^vee_dens          rank 1792, form 13
U3 = S^vee_dens                rank 128,  form 14.
```

A strict cochain differential is the three-arrow object

```text
d0: U0 -> U1,
d1: U1 -> U2,
d2: U2 -> U3.
```

It is not the same object as the rolled odd operator on two rank-1920 parity
halves, and neither is automatically the nine-block quadratic Euler family
`D_c` or its density-dual Hessian. The existing coordinate inclusion into the
relative BV carrier was already proved vacuous for rolling; a nontrivial
filtered graph embedding is additional data.

## Exact fold-support theorem

Use the existing stage-preserving high-to-low maps

```text
rho13: U2 -> I+R,
rho14: U3 -> S,
```

and order both folded parity halves as `E=S+I+R`. Cochain degree then places
the three arrows in the following coarse blocks:

| arrow | folded blocks |
| --- | --- |
| `d0: S -> I+R` | `IS`, `RS` |
| `d1: I+R -> (I+R)^vee` | `II`, `IR`, `RI`, `RR` |
| `d2: (I+R)^vee -> S^vee` | `SI`, `SR` |

These are exactly eight of the nine `S/I/R` blocks. No degree-`+1` arrow has
type `S -> S`. Therefore the rolled coarse matrix has the structural form

```text
M_roll = [[0,   *, *],
          [*,   *, *],
          [*,   *, *]].
```

The current Stage-B target requires all nine entries nonzero. In particular,
its `a D_S` block is `S -> S`. The strict stage-preserving four-stage fold
therefore cannot be that target, independently of coefficient values, Gram,
formal-adjoint sign, nilpotence, acyclicity or domain.

This is a target-eligibility obstruction, not a four-stage no-go. A nonzero
`S -> S` block could arise only by adding a non-cochain Euler/Dirac term or by
constructing the still-unowned filtered graph/BV roll that mixes the declared
low/high stages. Either changes the object and must carry its own typing and
master-equation proof.

## Exact positive acyclic control

At coarse multiplicity grade, take

```text
d0 = [[1], [1]],
d1 = [[-6/7, 6/7], [-6/7, 6/7]],
d2 = [[1, -1]].
```

Then

```text
d1 d0 = 0,
d2 d1 = 0,
rank(d0,d1,d2) = (1,1,1).
```

The `1 -> 2 -> 2 -> 1` complex is exact: adjacent ranks sum to two at both
middle stages. Its fold is

```text
[[0,  1,   -1],
 [1, -6/7,  6/7],
 [1, -6/7,  6/7]].
```

All eight eligible blocks are nonzero. Under the house nine-block
normalization, its `RR=6/7` gives exactly `q=1`; only `a=0`. Thus the support
obstruction is sharp: strict acyclicity and normalized W131 support coexist,
but not with full-nine support.

For the actual typed ranks, acyclicity would require arrow ranks
`(128,1664,128)`. The probe records this necessary rank profile but does not
claim to construct the full maps or their cohomology.

## Controls and consequence

The exact rational probe passes `22/22`. A one-entry middle mutation or wrong
terminal adjoint breaks nilpotence. A singular high-to-low roll is rejected.
A planted `S -> S` entry is detected as degree-violating, while the acyclic
control proves that the eight-block support is not vacuous.

The current full-nine-block Stage-B family is therefore ineligible as the
direct fold of the strict four-stage differential it was waiting for. The
prior Gram-underdetermination result remains correct for that Euler family,
but linear four-stage nilpotence/acyclicity cannot normalize it until the
object mismatch is repaired.

Field (iii) remains `EXTERNAL-VIA-GRAM` for the current nine-block family, and
the five-field packet remains fail-closed. No Gram, action, global domain,
quotient, source-preferred operator, particle result or GU verdict is selected.

## Exact next owner

Choose one action-owned route before another normalization solve:

1. `ACTION-OWNED-FILTERED-GRAPH-ROLL`: construct the non-stage-preserving
   field/antifield graph embedding that produces `S -> S`, and prove its
   cochain/BV degree and master-equation compatibility; or
2. `STRICT-EIGHT-BLOCK-PLUS-EULER-SEPARATION`: keep the strict differential
   eight-block, type `a D_S` as a separate quadratic Euler/Dirac term, and
   restate which object the five-field packet is meant to normalize.

Until one route is owned, do not call the current full-nine matrix the actual
`0 -> 1 -> 13 -> 14` differential and do not count its kernel as four-stage
acyclicity.
