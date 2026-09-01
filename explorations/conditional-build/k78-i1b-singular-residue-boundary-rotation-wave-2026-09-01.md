---
title: "K78 I1B singular-residue boundary-rotation wave"
status: active_research
doc_type: reverse_scaffold_i1b_singular_residue_boundary_rotation_result
date: 2026-09-01
claim_ceiling: exact indicial-spectrum, unweighted endpoint-class and eigenframe-rotation classification for one repository-owned singular two-component control; no actual source cross-null operator, native measure or physical boundary selector
manifest: lab/process/k78-i1b-singular-residue-boundary-rotation-wave.json
probe: tests/channel-swings/k78_i1b_singular_residue_boundary_rotation_probe.py
---

# K78 I1B singular-residue boundary-rotation wave

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
result: exact singular-residue eigenvalues, unweighted endpoint threshold and half-angle rotation of indicial boundary coordinates for a two-component control
carrier: complex two-component sections on 0<u<1 with kappa=1/4 and real coefficient a LAYER=conditional CHIRALITY=N/A
pairing: positive repository-owned L2(du) pairing for the self-adjoint endpoint classification; an additional u^p du mode census is integrability-only
real_structure: componentwise conjugation preserved by real matrices J, S, H and real kappa,a
grading: two indicial modes u^(-rho)e_plus and u^(rho)e_minus; no gauge, BRST, BV or physical grading
action_owner: repository owns the singular-residue countercontrol only; no filed source action owns its operator, measure or boundary line
target: whether placing a in the singular residue changes endpoint class or boundary coordinates and whether either effect selects log(2) versus log(3) MAP-TYPE=classification
```

## Result first

Moving the tangential coefficient from bounded order into the singular residue
changes both the indicial exponents and their eigenframe. At `kappa=1/4` in
the positive `L2(du)` control, both `a=log(2)` and `a=log(3)` cross the
limit-circle threshold and become limit-point. The endpoint class therefore
detects that the coefficient is singular but does not distinguish those two
values. Their indicial frames do differ by a computable half-angle. That
difference becomes a selector only after an independent owner fixes a physical
boundary line or spectral datum.

Freeze

```text
J=[[0,-1],[1,0]],  S=[[0,1],[1,0]],  H=[[1,0],[0,-1]],
D_(kappa,a)=J d/du+(1/u)(kappa S+a H),   kappa=1/4.            (1)
```

The residue is Hermitian and `J` is skew-Hermitian, so (1) is formally
symmetric for the positive `L2(du)` pairing. Multiplying the zero-mode equation
by `-uJ` gives

```text
u f'+C_(kappa,a) f=0,
C_(kappa,a)=kappa H-aS=[[kappa,-a],[-a,-kappa]].              (2)
```

Since `H^2=S^2=I` and `HS+SH=0`,

```text
C^2=(kappa^2+a^2)I,       rho=sqrt(kappa^2+a^2).             (3)
```

The indicial modes are `u^(-rho)e_+` and `u^(rho)e_-`. In
`L2(du)`, both modes are square-integrable exactly when

```text
rho<1/2.                                                       (4)
```

Thus the singular endpoint is limit-circle for

```text
|a|<sqrt(1/4-kappa^2)=sqrt(3)/4                              (5)
```

and limit-point at and beyond the threshold. Elementary exponential-series
bounds give
`log(2)>1/2>sqrt(3)/4` and `log(3)>1`, so both proposed positive values are
strictly limit-point. Unlike the prior bounded `aH` theorem, the singular
coefficient changes the endpoint domain class. It still does not select
between `log(2)` and `log(3)` by that binary class.

## Exact eigenframe rotation

For `a>=0`, define

```text
cos(theta)=kappa/rho,       sin(theta)=a/rho,
0<=theta<pi/2.                                                  (6)
```

An orthonormal real eigenframe is

```text
e_+=(cos(theta/2),-sin(theta/2)),
e_-=(sin(theta/2), cos(theta/2)).                              (7)
```

Equation (7) diagonalizes `C` with eigenvalues `+rho,-rho`.
Consequently the two candidate values have distinct indicial exponents and
distinct half-angle frames because `rho(a)` and `theta(a)` are strictly
increasing for `a>0` at fixed positive `kappa`.

Suppose, only as a control, that an external owner fixes the component boundary
line `f_2=0` at a cutoff. Writing `f=c_+e_+ + c_-e_-`, that fixed line becomes

```text
c_-/c_+=tan(theta/2).                                         (8)
```

The same component line therefore has an `a`-dependent slope in indicial
coordinates. Conversely, if the boundary slope is allowed to vary freely with
`a`, equation (8) absorbs every value and selects none. Rotation of coordinates
is not a physical boundary law.

## Weighted mode census is not an extension theorem

For the unchanged formal modes but a raw measure `u^p du`, the singular mode
has squared density `u^(p-2rho)`. Both modes are integrable exactly when

```text
rho<(p+1)/2.                                                   (9)
```

At `p=1`, the same rational exponential-series bounds certify

```text
rho(log(2))<1<rho(log(3)).                                    (10)
```

so this raw census distinguishes two modes from one. But (1) has not been
modified by the weight correction required for formal symmetry in
`L2(u^p du)`, and the source owns neither this measure nor this operator.
Equation (10) is therefore an integrability discriminator only, not a
self-adjoint extension or physical coefficient selector.

## Hostile review and claim ceiling

The strongest overclaim would say that the half-angle or weighted count fixes
the I1B coefficient. Neither does. At unweighted positive-control grade both
candidate values share the same limit-point class. The half-angle becomes
observable only relative to an independently fixed boundary line, matching
law or spectrum. The weighted count changes the measure without deriving the
corresponding symmetric operator.

The strongest contrary construction is the prior bounded coefficient: it
leaves domains and Green data unchanged. The weakest reproducibility seam is
analytic domain completeness for the singular expression; the exact probe
certifies the residue algebra, thresholds, interval placements and frame
rotation, not a source-owned maximal-domain theorem.

The operator, `du` pairing, `u^p du` census and fixed component line are
repository-owned controls. They are not the actual cross-null operator,
rank-changing presymplectic quotient, native measure, positive physical
pairing or rank-jump matching law. No prediction, confirmation, held-out score
or GU verdict follows.

## Next condition

Derive the actual source/action-owned cross-null normal operator, measure,
pairing and rank-jump matching law. Then determine whether the coefficient
enters its singular normal matrix and whether a physical boundary relation or
spectral observable fixes the otherwise free half-angle coordinate.

Reproduce with:

```bash
python3 tests/channel-swings/k78_i1b_singular_residue_boundary_rotation_probe.py
python3 tests/channel-swings/k78_i1b_singular_residue_boundary_rotation_probe.py --selftest
```
