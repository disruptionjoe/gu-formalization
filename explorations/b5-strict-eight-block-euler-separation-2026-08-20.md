---
title: "B5 strict-eight-block plus Euler separation: exactness does not normalize the Dirac term or Gram"
status: active_research
doc_type: exact_action_object_separation
created: "2026-08-20"
registry: lab/process/b5-strict-eight-block-euler-separation.json
probes:
  - tests/channel-swings/b5_strict_eight_block_euler_separation_probe.py
grade: "AT THE INDEPENDENT B5 FORMAL COMPACT-CORE AND COARSE MULTIPLICITY GRADE, THE STRICT 0->1->13->14 DIFFERENTIAL AND THE FULL-NINE QUADRATIC EULER/HESSIAN FAMILY ARE DISTINCT OBJECTS. THE STRICT COMPLEX RETAINS EIGHT-BLOCK SUPPORT AND EXACTNESS; A SEPARATE SYMMETRIC RANK-TWO HESSIAN CAN HAVE LIVE S->S AND FULL NINE-ENTRY SUPPORT. STRICT NILPOTENCE/ACYCLICITY SUPPLIES NO EQUATION FOR THAT S->S COEFFICIENT OR THE MULTIPLICITY GRAM. AN ACTION BRIDGE RELATING THE TWO OBJECTS REMAINS UNCONSTRUCTED."
target_verdict: B5_STRICT_COMPLEX_AND_QUADRATIC_EULER_OPERATOR_SEPARATED
target_claim: internal target STRICT-EIGHT-BLOCK-PLUS-EULER-SEPARATION; verdict separation is well-typed but does not normalize the Euler coefficient or Gram
canon_verdict_change: none
---

# B5 strict-eight-block plus Euler separation

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds only the independently typed B5 formal compact-core
carrier and its coarse `S + imGamma + kerGamma` bookkeeping. It separates a
strict stage-preserving cochain differential from a quadratic Euler/Hessian
operator. It does not construct the full `128 -> 1792 -> 1792 -> 128` maps,
derive the Hessian from an action or BV symplectic form, choose a Gram or
domain, recover Weinstein's historical preferred middle differential, or
infer a particle or GU verdict.

```gu-typed-objects
result: the strict eight-block B5 complex and the full-nine quadratic Euler operator are distinct; exactness does not normalize the separate S-to-S term or Gram
carrier: d on U0=S, U1=I+R, U2=(I+R)^vee_dens, U3=S^vee_dens; H on folded E=S+I+R density-dual/primal pair LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: multiplicity Gram for primalizing H remains EXTERNAL-VIA-GRAM; action bridge from d to H remains UNTYPED ON=formal-compact-core
real_structure: underlying complex cochain carrier; native Lorentzian real structure and absolute coflip trivialization remain UNTYPED
grading: integer cochain degree 0,1,2,3 for d; quadratic Euler/Hessian role for H, not identified with the cochain degree
action_owner: repository-construction separation only; action/BV bridge relating d and H remains unowned
target: ownership of nilpotence, exactness, Hessian symmetry, the S-to-S Dirac coefficient and Gram MAP-TYPE=evaluation
```

## Result first

The strict route is internally consistent only after two objects are kept
separate:

```text
d:   U0 -> U1 -> U2 -> U3                       strict cochain differential
Q8:  stage-preserving fold of d                  eight eligible S/I/R blocks
H9:  quadratic Euler/Hessian object              may contain live S -> S
G:   multiplicity Gram/primalizer                 converts H9 to an operator
```

The preceding support theorem proved that `Q8` cannot contain `S -> S`. This
result proves the positive separation and its limit. The same exact acyclic
coarse complex survives beside a symmetric rank-two, full-nine-entry Hessian
with a live `S -> S` term. Changing that term or changing the Gram cannot alter
`d1 d0 = 0`, `d2 d1 = 0`, or the ranks of the strict complex because those
data are not arguments of `d`.

Therefore the `a D_S` contribution can be retained only as a separately typed
quadratic Euler/Dirac term at the present grade. Strict cochain exactness does
not normalize `a`, does not select `G`, and does not turn ordinary Hessian
symmetry into the BV master equation.

## Equation-ownership table

| statement | owner | licensed use |
| --- | --- | --- |
| `d1 d0 = 0`, `d2 d1 = 0` | strict four-stage differential `d` | cochain nilpotence only |
| ranks `(128,1664,128)` in the actual carrier | strict `d` | necessary profile for full acyclicity; still unbuilt |
| eight-block support, structural `SS=0` | stage-preserving fold `Q8` | eligibility of the folded differential |
| `H9^T = H9` | quadratic Hessian `H9` | ordinary quadratic-action symmetry |
| `M=G^{-1}H9`, `M^T G=GM` | Euler operator plus Gram | formal adjointness for a chosen `G` |
| live `aD_S` / `SS` | separate Euler/Hessian sector | not a cochain arrow |
| classical master equation | action plus BV symplectic/antibracket owner | **not serialized here** |
| a relation `A(d)=H9` | action bridge | **not constructed here** |

This table corrects the tempting but invalid inference that the strict
complex's new nilpotence equations can be applied to the current full-nine
Stage-B coefficient family. They cannot: that family is an Euler operator,
whereas nilpotence belongs to `d`.

## Exact witnesses

The strict coarse control remains

```text
d0 = [[1], [1]],
d1 = [[-6/7, 6/7], [-6/7, 6/7]],
d2 = [[1, -1]].
```

It is nilpotent and exact with ranks `(1,1,1)`. Separately, use the prior
Stage-B symmetric Hessian

```text
H9 = (13/735) (u u^T + v v^T),
u=(1,2,3), v=(4,5,6).
```

`H9` has rank two, all nine entries nonzero, a live `SS` entry, and kernel
`(1,-2,1)`. The canonical and off-diagonal allowed Grams both primalize this
same Hessian to distinct Euler operators. Hence strict exactness coexists with
a full-nine Hessian, but provides no coupling equation that chooses its `SS`
coefficient, its Gram, or its primalized coefficient packet.

The exact rational probe passes `26/26`. A middle-arrow mutation breaks the
strict complex; an attempted `SS` insertion is rejected by support typing; an
`SS` deletion changes the Euler object without changing strict exactness. The
failure paths distinguish the two objects rather than allowing one green
equation to certify both.

## Five-field packet restatement

The five-field packet may no longer call the full-nine Stage-B family the
"actual differential expression." Its ingress target is now a paired object:

1. a strict eight-block differential `d/Q8`, including its own pairing and
   formal-adjoint data;
2. a quadratic Euler/Hessian object `H9` with separately typed `aD_S`;
3. an action/BV bridge proving how `d`, `H9`, the Gram and the antibracket fit
   one variational construction.

The 2026-08-20 all-Gram verdict `EXTERNAL-VIA-GRAM` binds the current
full-nine Euler family. It does **not** determine the formal-adjoint sign of the
strict eight-block differential, because no bridge identifies those two
operators. The packet therefore remains fail-closed: Euler field (iii) is
Gram-relative, strict-differential field (iii) is still uncomputed, and the
action bridge is absent.

## Exact next owner

The smallest next action-owned gate is
`B5-STRICT-DIFFERENTIAL-ACTION-BRIDGE`: construct the quadratic/BV action map
that sends the typed strict `d/Q8` data to an Euler/Hessian object and state
where `aD_S` enters. It must expose an independent classical master-equation
condition rather than relabel Hessian symmetry, and it must declare whether
the strict-differential pairing is the same Gram used to primalize `H9`.

If no such bridge is constructed, the separated objects remain compatible
but unrelated formal controls. The alternative filtered-graph route reopens
only with an explicit field/antifield embedding and its own degree/master
proof. No Gram solve, coflip wave, domain wave, quotient, particle inference or
GU verdict is licensed first.
