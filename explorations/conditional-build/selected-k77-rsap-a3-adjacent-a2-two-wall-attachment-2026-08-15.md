---
title: "Selected-K77 RSAP split-A3 adjacent-A2 two-wall attachment"
status: active_research
doc_type: exact_singular_symplectic_moment_atlas_attachment
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a3-adjacent-a2-two-wall-attachment.json
probe: tests/channel-swings/selected_k77_rsap_a3_adjacent_a2_two_wall_attachment_probe.py
grade: "FIRST ADJACENT SPLIT-A2 TWO-WALL ATTACHMENT CONSTRUCTED AT 98D; 91 TO 90 TO 88 MAP-RANK SCHEDULE AND WALL/WALL/A2 COCYCLE STRICT"
canon_verdict_change: none
---

# Selected-K77 RSAP split-`A3` adjacent-`A2` two-wall attachment

## Result first

The first split-`A3` singular wall now extends across one adjacent two-wall
intersection. On a signature-`(2,2)` block choose three coordinates ordered
with signs `(+,-,+)`. Both adjacent simple roots cross opposite-sign
coordinates, so each rank-one restriction is the already constructed
`sl(2,R)/so(1,1)` wall. Together they generate the principal symmetric pair

```text
sl(3,R)/so(2,1),
```

whose cotangent realization was independently proved to be onto and rank eight
over every regular `sl3` covector, including regular nilpotents.

The resulting local carrier is

```text
S78 x T*(SL(3,R)/SO(2,1)) x T*R5.
```

It remains smooth and `98D`. Its full map rank is `91` off both walls, `90`
on either one-wall face, and `88` at their `A2` intersection, while target
Poisson rank is respectively `84`, `82`, and `78`. Both wall restrictions
recover the banked `S82 x T*(SL2/SO11) x T*R6` model. Their canonical
cotangent lifts preserve the geometric moment map and tautological primitive,
and the first wall/wall/`A2` ordered cocycle closes strictly.

This constructs one adjacent split-`A2` intersection inside the split-`A3`
carrier. It does not classify every two-wall type, another `A3` real form,
deeper strata, zero charge, or a global all-strata RSAP.

## Layer 0 and root typing

This is a classical symplectic/Poisson atlas statement. It is not an
action-selected phase space, quantization, spectrum, or physical claim.

Let `Q=diag(1,-1,1)` and

```text
theta(X) = -Q X^T Q.
```

Its fixed algebra is `so(2,1)` and its moving space is the five-dimensional
space of trace-free `Q`-self-adjoint matrices. For the two adjacent roots
`alpha_1=(1,2)` and `alpha_2=(2,3)`, the signature product is `-1`. In each
root `sl2`, therefore,

```text
E+F is fixed,          H and E-F are moving.
```

The fixed line is `so(1,1)`, not `so(2)`. Thus both faces are exactly the
opposite-sign split wall type used by the predecessor, rather than an
unlicensed compact substitution. Reordering the selected three coordinates
inside the completed block-pivot atlas is a Weyl/base transition and its
cotangent lift; it adds no field.

## Centralizers and the exact rank schedule

Use the regular and wall controls

```text
lambda_reg = diag(2,0,-2),
lambda_1   = diag(1,1,-2),
lambda_2   = diag(2,-1,-1),
lambda_A2  = 0.
```

At a regular control, the centralizer in `sl3` has dimension two and the
centralizer in the moving space also has dimension two. At either wall, the
`sl3` centralizer is `sl2 + R`, of dimension four; its intersection with
`so(2,1)` has dimension one and its moving intersection has dimension three.
At the intersection the full five-dimensional moving space centralizes zero.

At `[e,lambda]` the cotangent moment differential splits into the moving
variation and the bracket image:

```text
dJ(X,delta lambda) = [X,lambda] + delta lambda,
X,delta lambda in m.
```

The two summands lie in the fixed and moving halves. Hence the principal `A2`
factor has map ranks

```text
5+(5-2)=8   regular,
5+(5-3)=7   on either wall,
5+(5-5)=5   at the A2 intersection.
```

The `sl3` orbit ranks are `6`, `4`, and `0`. Adding the common `78D` leaf and
the five external zero coordinates gives

| locus | target Poisson rank | map rank | fibre dimension |
| --- | ---: | ---: | ---: |
| regular | `84` | `91` | `7` |
| either adjacent wall | `82` | `90` | `8` |
| `A2` two-wall intersection | `78` | `88` | `10` |

The one-dimensional centre of `sl2 + R`, together with the external `R5`, is
the `R6` centre of each banked first-wall model. Thus restriction of the `A2`
factor recovers both wall carriers without changing the `98D` source.

## Two attachments and the first wall/wall/`A2` cocycle

Let `f_1` and `f_2` be the two embedded-root gauges from the first-wall charts
to the principal-`A2` chart on their regular overlaps. Each is an actual base
diffeomorphism inherited from the banked root gauges and the completed
block-pivot atlas. Its cotangent lift is

```text
x' = f_i(x),       xi' = (Df_i(x))^(-T) xi,
```

so `xi'^T dx'=xi^T dx` and the geometric moment map is unchanged. On the
three-chart overlap the wall-to-wall base map is `f_2^{-1} f_1`; consequently
the ordered base product and the inverse-transpose cotangent product are both
identity by the chain rule. The `A2` Weyl generators also obey the exact braid
relation `s1 s2 s1=s2 s1 s2`. The moment and primitive Cech defects therefore
vanish. No contractibility, logarithm branch, twist, or integrality assumption
is used.

## Hostile ceiling and next gate

- One adjacent split-`A2` two-wall attachment constructs.
- The carrier remains `98D`, with the exact map-rank schedule
  `91 -> 90 -> 88`.
- Both rank-one restrictions are opposite-sign split walls; no compact wall is
  silently imported.
- The result is local to one `A2` subsystem. It does not classify every
  two-wall orbit or prove a global singular atlas.
- No canon, ledger, residue, quotient datum, physical interpretation, or public
  posture changes.

The next exact gate is to classify the remaining split-`A3` two-wall types
under the completed block-pivot/Weyl atlas, then attach the first genuinely
three-wall or mixed-real-form intersection. Deeper strata, zero charge, and
all-strata RSAP remain open.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a3_adjacent_a2_two_wall_attachment_probe.py
```

The certificate uses exact integer and rational linear algebra only.
