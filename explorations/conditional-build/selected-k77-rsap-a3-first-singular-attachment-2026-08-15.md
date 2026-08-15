---
title: "Selected-K77 RSAP split-A3 first singular attachment"
status: active_research
doc_type: exact_singular_symplectic_moment_atlas_attachment
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a3-first-singular-attachment.json
probe: tests/channel-swings/selected_k77_rsap_a3_first_singular_attachment_probe.py
grade: "FIRST SPLIT-A3 SUBREGULAR ATTACHMENT CONSTRUCTED AT 98D; 91 TO 90 MAP-RANK LOSS AND WALL/CARTAN/BLOCK-PIVOT COCYCLE STRICT"
canon_verdict_change: none
---

# Selected-K77 RSAP split-`A3` first singular attachment

## Result first

The completed split-`A3` regular block-pivot atlas now attaches to one generic
codimension-one split-root centralizer jump. This closes the seam that neither
predecessor could close alone.

The banked wall packet constructed

```text
S82 x T*(SL(2,R)/SO(1,1)) x T*R6
```

as a smooth `98D` symplectic realization of the local target
`S82 x sl2* x R6_zero`, with map rank `91` off the wall and `90` on its zero
section. The newer regular packet completed

```text
S72 x T*(SL(4,R)/SO(2,2)) x T*R4
```

over every split-regular block-pivot chart, also at `98D` and map rank `91`.
The missing fact was that the two constructions describe the same opposite-
signature root neighborhood and have compatible transition maps.

Embed the root across one positive and one negative coordinate of
`H22=diag(1,1,-1,-1)`. Its `sl2` isotropy is `so(1,1)`, exactly the homogeneous
pair used by the wall carrier. On the nonzero transverse cone, the wall chart's
banked `SO(1,1)` gauge and fixed Weyl conjugation give the split Cartan chart.
Every Cartan-to-block-pivot arrow is then an ordinary base transition with its
canonical cotangent lift. Composition therefore preserves the complete moment
map and tautological primitive strictly on both regular sides. The zero section
remains smooth and supplies the wall preimage.

The first wall/Cartan/block-pivot triple closes by the chain rule. Thus one
split-`A3` subregular attachment is constructed; other `A3` real forms,
adjacent two-wall intersections, deeper strata, zero charge and all-strata
RSAP remain open.

## Layer 0 and exact root embedding

This is a classical symplectic/Poisson atlas statement. It is not an
action-selected phase space, quantization, spectrum or physical claim.

Let the second basis vector have positive `H22` sign and the third negative
sign. In the corresponding `2 x 2` block set

```text
H = E22-E33,   E=E23,   F=E32.
```

They obey `[H,E]=2E`, `[H,F]=-2F`, `[E,F]=H`. For the symmetric-pair
involution `theta(X)=-H22 X^T H22`,

```text
theta(E+F)=E+F,       theta(H)=theta(E-F)=-(H,E-F).
```

Hence the embedded fixed algebra is the split one-dimensional
`so(1,1)=span(E+F)`, while the two-dimensional moving space is
`span(H,E-F)=ann(so(1,1))` under the invariant pairing. This is precisely the
`SL(2,R)/SO(1,1)` factor, with `SO(1,1)` conjugate to the split Cartan subgroup
`A` used in the earlier wall packet.

The exact subregular control

```text
lambda0 = diag(3,1,1,-5)
```

has one repeated opposite-sign eigenvalue. Its centralizer in `sl4` has
dimension five: the embedded `sl2` plus a two-dimensional centre. Its
intersection with the moving symmetric-pair space has dimension four, versus
three at a regular diagonal value. Therefore the cotangent moment differential

```text
dJ_(e,lambda)(X,delta lambda) = [X,lambda] + delta lambda,
X,delta lambda in m
```

has rank

```text
dim(m)+rank(ad_lambda|m) = 9+(9-3)=15   regular,
                           9+(9-4)=14   at lambda0.
```

Adding the common `72D` identity leaf and the `T*R4 -> R4_zero` projection
gives the required full map ranks `91` and `90`. The `sl4` orbit rank changes
`12 -> 10`, so the complete target Poisson rank changes `84 -> 82`.

## Reconciliation with the banked wall model

Inside `sl4`, the subregular centralizer is `sl2 + R2`. The existing four
external zero coordinates complete this to

```text
sl2 + R2 + R4 = sl2 + R6,
```

exactly the transverse target previously constructed from
`T*(SL2/SO(1,1)) x T*R6`. Dimension accounting agrees in both descriptions:

```text
regular:  S72 + T*(SL4/SO22) + T*R4 = 72+18+8 = 98,
wall:     S82 + T*(SL2/SO11) + T*R6 = 82+4+12 = 98.
```

The two formulas regroup the same smooth carrier near the selected wall; they
do not add a field or change dimension.

## Strict overlap and first triple

Call the wall-to-Cartan base map `f_CW` and a Cartan-to-block-pivot map
`f_BC`. Both are already constructed on their nonempty regular domains. Their
cotangent lifts are

```text
x' = f(x),       xi'=(Df(x))^(-T) xi.
```

Consequently

```text
xi'^T dx' = xi^T dx
```

for each arrow and for `f_BW=f_BC composed with f_CW`. The geometric moment
map is unchanged by coordinates. The same composition works for every
block-pivot chart meeting either nonzero split-root side, because the complete
regular atlas already proved all such Cartan/block transitions.

On a wall/Cartan/block-pivot triple, base Jacobians multiply by the chain rule
and inverse-transpose cotangent Jacobians multiply in reverse order. The
ordered product with the return map is identity. The moment and primitive
Cech defects are therefore zero. No contractibility premise or logarithm
branch is used.

## Hostile claim ceiling and next gate

- One generic opposite-sign split-root subregular attachment constructs.
- The full carrier stays `98D`; map rank changes `91 -> 90` exactly as target
  Poisson rank changes `84 -> 82`.
- The result composes two previously banked constructions; it does not claim a
  new physical carrier or a global all-strata map.
- Compact or mixed `A3` walls, adjacent `A2` intersections, deeper singular
  strata and zero charge remain open.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

The next exact gate is the first adjacent split-`A2` two-wall intersection.
The principal `A2` symmetric-pair factor is now available, but it must be
attached to both first-wall charts and pass the first wall/wall/`A2` cocycle
before any deeper-strata conclusion.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a3_first_singular_attachment_probe.py
```

The certificate uses exact integer and rational linear algebra only.
