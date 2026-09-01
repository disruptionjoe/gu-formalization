---
title: "K77 I1B radial-domain indicial classification wave"
status: active_research
doc_type: reverse_scaffold_i1b_radial_domain_result
date: 2026-09-01
claim_ceiling: exact weighted-L2 indicial classification for the frozen two-dimensional regular-singular cross-null control with bounded tangential perturbation; no actual source-owned cross-null operator, positive pairing, self-adjoint extension, boundary law or counterterm policy
manifest: lab/process/k77-i1b-radial-domain-indicial-classification-wave.json
probe: tests/channel-swings/k77_i1b_radial_domain_indicial_classification_probe.py
---

# K77 I1B radial-domain indicial classification wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: regular-singular radial indicial and weighted-L2 mode-count classification
carrier: repository-owned two-dimensional degenerating I1B Darboux plane on 0<u<epsilon LAYER=conditional CHIRALITY=N/A
pairing: positive Euclidean control norm with weighted measure u^p du; not the source-owned Green form or a physical Hilbert pairing
real_structure: real two-component sections with residue R=-I2/2+C and C having real eigenvalues plus-or-minus s
grading: radial asymptotic order only; no gauge, BRST, BV or self-adjoint-extension grading
action_owner: source owns the I1B rank jump and transgression grammar only; the radial operator, positive norm and boundary-domain test are repository-derived
target: whether leading cross-null radial admissibility can distinguish A_y=aH, including a=log(2) and a=log(3) MAP-TYPE=classification
```

## Freeze the radial normal problem

The previous packets leave the compatible singular residue

```text
R=-I2/2+C,        tr(C)=0,                        (1)
```

and tangential connection `A_y=aH`. Freeze the regular-singular control

```text
u psi'(u)+(R+u a H)psi(u)=0                      (2)
```

on `0<u<epsilon`, with a positive control norm and measure `u^p du`. The
coefficient `u aH` is bounded and lower radial order; the indicial family is
therefore

```text
I(z)=z I2+R.                                     (3)
```

This is a boundary-domain test, not an assertion that (2) is the full physical
I1B operator.

## Exact indicial thresholds

Suppose `C` is real semisimple with eigenvalues `+s,-s`, `s>=0`. The two
indicial modes have leading behavior

```text
psi_+(u)=u^(1/2-s)(v_+ + O(u)),
psi_-(u)=u^(1/2+s)(v_- + O(u)).                   (4)
```

For a mode with `C`-eigenvalue `c`, its squared weighted norm behaves as

```text
integral_0^epsilon u^(p+1-2c) du.                (5)
```

It is finite exactly when

```text
c < (p+2)/2.                                     (6)
```

For the Darboux Pfaffian weight `p=1`, both modes are admissible for
`0<=s<3/2`; the `+s` mode is logarithmically divergent at `s=3/2`; and only
the `-s` mode survives for `s>3/2`.

## The tangential coefficient is indicially invisible

The bounded term `u aH` changes the regular `O(u)` factors in (4), not the
roots of (3). Consequently the leading weighted-`L2` mode count is identical
for every finite `a`, including `log(2)` and `log(3)`.

An exact noncommuting control makes this independence nontrivial. Let

```text
C=s [[0,1],[1,0]],       H=diag(1,-1).            (7)
```

Then `C` still has eigenvalues `+s,-s`, while

```text
[C,H]=[[0,-2s],[2s,0]],
tr([C,H]^2)=-8s^2,                                (8)
```

which is nonzero for `s!=0`. Thus the same horn can have nonzero invariant
mixed curvature and nevertheless give the same leading radial-domain count
for `a=log(2)` and `a=log(3)`. Local radial integrability by itself does not
choose between them.

## What a real boundary law would still have to own

Weighted integrability supplies a maximal admissible asymptotic space, not a
self-adjoint or variational boundary condition. Selection could still enter
through a source/action-owned Green pairing, boundary symplectic form,
Lagrangian subspace, global monodromy constraint, finite-bare rule or
counterterm-renormalized extension. Those structures may couple `a` to the
boundary data; none is supplied by the indicial roots alone.

The positive Euclidean norm used here is explicitly a control. The native I1B
Green form is alternating, and treating its trace polynomial as a positive
norm would repeat the ownership error isolated by the previous wave.

## Hostile review and ceiling

The strongest overstatement would call coefficient-blind indicial roots a
proof that no boundary condition can select `a`. The missing boundary pairing
and extension law prevent that conclusion. The strongest contrary route is a
global or variational boundary condition depending on `a`; it remains open
because it is not encoded in the frozen normal operator. The weakest
reproducibility seam is dropping the factor `u` before `aH`, which would move
the tangential coefficient into the residue and change the problem.

No source-owned cross-null operator, physical positive pairing, self-adjoint
extension, counterterm policy, prediction or confirmation is obtained.

## Next condition

Derive the actual cross-null operator and Green boundary form from the source
action, classify its minimal/maximal domains and admissible Lagrangian
extensions, and test whether the finite-bare or renormalized law depends on
`a`. Otherwise supply an independent mixed residue whose lineage excludes the
tested coefficient.
