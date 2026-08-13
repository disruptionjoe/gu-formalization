---
artifact_type: construction_result
created: 2026-08-08
status: TILTED_AFFINE_COCYCLE_EXACT__V70_EDGE_TYPE_MISMATCH__BRIDGE_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS__TILTED_AFFINE_ONEFORM_COCYCLE__SOURCE-SILENT__BOUNDARY_ZEROFORM_EDGE_BRIDGE
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_tilted_edge_bundle_type_bridge_probe.py
  - tests/channel-swings/selected_k77_tilted_edge_bundle_type_bridge_independent.sage
registry: lab/process/selected-k77-tilted-edge-bundle-type-bridge.json
---

# Selected K77 tilted edge-bundle type bridge

## Result first

The source/repository tilted subgroup passes an exact global-cocycle surrogate,
but it does **not** directly globalize the v0.70 boundary edge variable.

On a noncommuting rational three-patch fixture, with

\[
c_{ij}=h_{ij}^{-1}d h_{ij},\qquad h_{02}=h_{01}h_{12},
\]

the exact identity

\[
c_{02}=\operatorname{Ad}(h_{12}^{-1})c_{01}+c_{12}
\]

holds. Consequently an affine connection-like one-form patches consistently.
A group-valued boundary frame `u` separately patches by
`u_1=u_0h_01`, `u_2=u_1h_12=u_0h_02`.

Layer 0 separates them. The v0.70 edge coordinate is a boundary zero-form
whose infinitesimal shift is `xi`; the tilted affine component is an
ad-valued one-form whose shift is `D_A0 xi`. In the exact local `A0=0`
fixture, constant nonzero `xi` moves the former while the derivative term
vanishes. A universal direct identity must also work on that admissible
fixture, so it is killed. The two cocycles close **separately**.

There is also no nonzero natural zero-order `GL(V)`-equivariant map
`V* -> 1`: two diagonal frame generators already force both components of a
candidate covector contraction to zero. A bridge needs owned extra structure:
a differential, a group-valued dressing, a normal/soldering contraction, or an
inverse derivative with its basepoint, zero-mode and domain data.

The v0.70 local quotient remains exact:

```text
local extended dimension/rank/kernel: 60/40/20
local conditional quotient dimension/rank: 40/40
global quotient added: 0
P1/P2/P3 consumed: 0
```

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| tilted affine field | `a_i in Omega^1(ad P)` with affine Maurer-Cartan gluing | boundary zero-form edge frame |
| boundary edge frame | group-valued zero-form `u_i` with multiplicative gluing | affine connection difference |
| infinitesimal edge shift | `delta u=u xi`, equal to `xi` at identity | `D_A0 xi` |
| infinitesimal tilted shift | ad-valued one-form `D_A0 xi` | the gauge parameter itself |
| coordinate descent | overlap cocycle for `u` or `a` | descent of the preboundary two-form and kernel |
| local quotient | v0.70 exact finite contact reduction | global BFV phase space or analytic domain |

The same letter-level gauge notation can hide a derivative and a form-degree
change. The constant-parameter witness is the decisive check that the two
objects are not homonyms for one construction.

## Source return

Weinstein explicitly supplies the inhomogeneous gauge group, the tilted
homomorphism using the distinguished Levi-Civita/Zorro connection, and the
associated affine Maurer-Cartan component. The source claim ledger records the
tilted left/right actions and the intended double-coset relation.

The checked sources do not supply a boundary edge frame, a BFV completion, or
a map from the tilted ad-valued one-form to the v0.70 zero-form edge coordinate.

```text
SOURCE-CONFIRMS__TILTED_AFFINE_ONEFORM_COCYCLE__
SOURCE-SILENT__BOUNDARY_ZEROFORM_EDGE_BRIDGE
```

## Exact three-patch calculation

The probe uses noncommuting `GL(2,Q)` matrices `h01,h12`, independent rational
first jets `dh01,dh12`, and the product-rule jet
`dh02=dh01 h12+h01 dh12`. It verifies:

- the Maurer-Cartan one-cocycle exactly;
- two-step and direct affine one-form patching agree;
- two-step and direct group-valued edge-frame patching agree;
- reversed overlap order, wrong adjoint side and homogeneous-only gluing all fail.

Sage independently reproduces the cocycle and the rank-two naturality
obstruction over `QQ`.

## Why no direct bridge exists

Linearizing `h=1+t xi` gives

\[
\left.\frac{d}{dt}\right|_{0}(h^{-1}d h)=d\xi,
\qquad
\left.\frac{d}{dt}\right|_{0}(u h)=u\xi.
\]

At `A0=0`, constant `xi` has `d xi=0` but `u xi` is generically nonzero. A chosen normal
can contract a one-form, but that imports a normal/soldering choice and still
misses the constant zero mode. An inverse derivative needs a basepoint or
zero-mode quotient and an analytic domain. These are possible construction
routes, not consequences of the tilted cocycle alone.

## Mandatory symplectic reading

Coordinate gluing is not enough. The next construction must provide a dressed
preboundary potential/two-form on the group-valued edge bundle, prove its
overlap naturality, identify its characteristic kernel, and show the reduced
form is independent of trivialization. Until that is done, the five scoped
quotients remain local and conditional.

## What changed

- the exact tilted affine cocycle is no longer open;
- the ordinary group-valued edge-frame cocycle is exact on the fixture;
- direct zero-form/one-form identification is killed;
- the missing bridge is narrowed to explicitly typed construction classes;
- no quotient, residue, verdict, datum or public-posture movement occurs.

```text
Ledger v0.71 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
headline_delta: NONE
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

## Seven-axis disposition

- **Layer 0:** zero-form edge frame and affine one-form are separated before
  any quotient claim.
- **L1 syntactic:** both overlap laws and the candidate bridge types are explicit.
- **L2 type:** group-valued zero-form, ad-valued one-form, `xi`, `D xi`,
  coordinate descent and presymplectic descent remain distinct.
- **L3 algebraic:** noncommuting rational triple overlaps, planted failures and
  an independent Sage route pass exactly.
- **L4 geometric:** the exact finite `A0=0` bundle-cocycle fixture passes; the actual
  labelled `Y14` boundary bundle and full tilted action remain open.
- **L5 variational:** v0.70 local presymplectic result is retained, but no
  global dressed preboundary form is claimed.
- **L6 analytic:** inverse-derivative/domain, polarization and common Green/Krein
  domain data remain open.
- **L7 physical:** no BFV, positivity, unitarity, Einstein, Standard Model or
  cosmology conclusion is claimed.

## Constraint fence

```text
new bulk fields: 0
new boundary-coordinate dimensions: 0
new coefficient freedom: 0
new scoped quotients: 0
direct identity bridge: killed
typed global bridge: open
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

## Next gate

Construct the group-valued boundary edge frame and its dressed preboundary
two-form on the actual `H`-bundle. Then relate it to the tilted affine one-form
through an owned differential, soldering/normal contraction or inverse-domain
map and prove overlap naturality of the full form, moment map and characteristic
kernel before opening full BFV and common-domain work.
