---
title: "K108 K105 quadratic-ray cone normalization boundary"
status: active_research
doc_type: quadratic_state_cone_invariant_normalization_classification
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact invariant-convex classification on the K105 blind carrier under the proved compact product subgroup; no claim that the repository-coordinate compactification is a source-owned physical state space
manifest: lab/process/k108-k105-quadratic-ray-cone-normalization-boundary-wave.json
probe: tests/channel-swings/k108_k105_quadratic_ray_cone_normalization_boundary_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K108 K105 quadratic-ray cone normalization boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet attaches K77's abstract quadratic sign escape to the actual
K105 coefficient-blind distortion sector. It classifies the normalizations
invariant under the exact compact product subgroup proved by K106, constructs
one compact repository-coordinate control, and records the remaining relative-
weight ambiguity. It adds no action, rank-one selector, source attribution or
physical-state interpretation.

```gu-typed-objects
result: the K-positive quadratic-ray lift evades sign; although its open cone is nonclosed, its closure has faithful compact normalizations invariant under O(256) times O(183), forming a two-weight family not uniquely selected by that symmetry
carrier: Sym2 of the K105 distortion blind carrier with inertia (256,183,0) LAYER=ambient CHIRALITY=N/A
pairing: positive block and negative block traces induced by the frozen K105 coordinate decomposition ON=repository_owned_action_control
real_structure: coefficientwise real quadratic lift q(v)=v tensor v
grading: even quadratic extension; v and -v define the same ray
action_owner: repository-construction; the algebra unit supplies a compact mathematical control but no source-owned state datum
target: closed faithfully normalized compact convex repository-control base MAP-TYPE=evaluation
```

## Inline preflight bookend

The raw-linear sign obstruction is exact, and K107 forbids manufacturing a
rank-one selector from the owned equivariant algebra. A quadratic density is a
different target type, so the cheapest honest test is to attach that extension
without enlarging K106's proved symmetry. The relevant group is the compact
subgroup

```text
G_b = O(E_+) times O(E_-),    dim E_+=256, dim E_-=183,
```

not the larger pseudo-orthogonal group. Consequently boosts mixing the two
blocks are not licensed by K106. This distinction changes the answer: positive
invariant majorants exist.

## Quadratic escape and its open boundary

Let `V=E_+ direct-sum E_-`, let `K=I_+ direct-sum (-I_-)`, and set

```text
q(v)=v tensor v in Sym2(V).
```

Then `q(v)=q(-v)`. Let `C+` be the finite positive hull of `q(v)` for
`K(v,v)>0`. Every generator is a nonzero positive-semidefinite form, so `C+`
is pointed. Polarization with sufficiently large positive shifts shows that
its linear span is all of `Sym2(V)`.

The cone is not closed. For positive unit `e`, negative unit `f`, and
`v_n=((n+1)/n)e+f`, every `v_n` is K-positive while `q(v_n)` converges to the
nonzero null ray `q(e+f)`. K-contraction is strictly positive on every nonzero
element of `C+` and vanishes on that limit, so the limit is not in `C+`.

## Exact invariant-normalization classification

A linear functional on `Sym2(V)` is represented by a symmetric form `H`.
Invariance under `G_b` forces all cross-block terms to vanish and each diagonal
block to be scalar. Therefore

```text
H_(a,b) = a I_+ direct-sum b I_-,
u_(a,b)(A) = a tr(P_+ A) + b tr(P_- A).                    (1)
```

The invariant space is two-dimensional. For every `a,b>0`, `H_(a,b)` is
positive definite, so `u_(a,b)` is faithful on every nonzero positive-
semidefinite element of `closure(C+)`. The normalized base

```text
B_(a,b)={A in closure(C+) : u_(a,b)(A)=1}                 (2)
```

is closed and bounded in finite dimension and hence compact. In particular,
the algebra unit gives the exact repository-coordinate control `H_(1,1)=I`.
No extra operator is needed for this mathematical compactification.

The symmetry does not uniquely select the relative block weight. For example,
`I` and `I_+ direct-sum 2I_-` are invariant, positive definite and
nonproportional. Their normalized representatives assign different weights to
a negative-block ray relative to a positive-block ray. Thus the exact result
is existence plus a projective one-parameter normalization family, not a
normalization obstruction.

The unit control is still not a physical-state theorem. The packet has no
source-owned physical quotient, observable-effect pairing, preparation rule,
Born interpretation, locality or dynamics certificate. Those burdens cannot
be obtained by calling the repository-coordinate trace a physical unit effect.

## Inline postflight bookend

- **Strongest overclaim:** “the quadratic extension has no compact invariant
  normalization.” Refused. That would require a pseudo-orthogonal boost
  symmetry not proved by K106; the actual compact product subgroup admits the
  family (1).
- **Strongest contrary construction:** the algebra unit produces a closed,
  compact, faithfully normalized repository-control base. Preserved as the
  positive result, without physical promotion.
- **Weakest reproducibility seam:** a `(2,1)` surrogate cannot prove the large
  dimensions. The theorem uses only the two nontrivial orthogonal blocks; the
  probe solves their invariant-form equations exactly and checks two distinct
  positive majorants plus the null-boundary sequence.

No K105 rank-one line is selected, and no source, action, quotient, physical
state, Born rule, prediction, confirmation, canon, paper, ledger or public
posture moves.

## Reproduction

```bash
uv run --with sympy==1.14.0 python \
  tests/channel-swings/k108_k105_quadratic_ray_cone_normalization_boundary_probe.py
uv run --with sympy==1.14.0 python \
  tests/channel-swings/k108_k105_quadratic_ray_cone_normalization_boundary_probe.py --selftest
```
