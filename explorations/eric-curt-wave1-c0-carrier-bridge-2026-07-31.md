---
title: "Eric/Curt Wave 1: C0 identifies the bundle and separates the real carriers"
status: construction_result
doc_type: exploration
created: 2026-07-31
run: lab/process/runs/GUH-20260731T181634Z-eric-curt-ten-wave-campaign-c0/run-plan.md
campaign: lab/specifications/eric-curt-ten-wave-construction-campaign-2026-07-31.md
probe: tests/channel-swings/eric_curt_wave1_c0_carrier_bridge_probe.py
grade: "EXACT local rational linear algebra and real-Clifford classification; RECONSTRUCTION for the connection-split bundle bridge; SOURCE-UNCERTAIN for Curt's block-sign attribution and global Zorro ownership. No action selection, physical recovery, or claim-status change."
---

# Eric/Curt Wave 1: C0 identifies the bundle and separates the real carriers

## Result first

Wave 1 gives a useful split verdict:

1. **Underlying bundle:** after choosing a Lorentz metric `h` and a connection
   split of the metric bundle, the musical/Zorro chain is a rank-14 real vector
   bundle isomorphism.
2. **Real metric carrier:** if Curt's total `(7,7)` and the active `(9,5)` are
   literal real signatures, they are not isometric. Sylvester inertia forbids
   it independently of coordinates.
3. **Real Clifford/reality carrier:** the repo's
   `Cl(9,5)=M(64,H)` and the comparator
   `Cl(7,7)=M(128,R)` are different real central-simple algebras. The active
   right-quaternionic structure does not transfer automatically.
4. **Complexification:** both complexify to `M(128,C)`. A complex bridge exists,
   but it erases exactly the real-form information on which the active Krein,
   charge-conjugation, and right-`H` machinery depends.

This supplies partial evidence for the carrier part of the third-lane gate,
but does not pass it because the source convention remains unresolved. It does
not create a Curt lane: there is no
Curt-specific complete action/observation packet or common-domain
discriminator yet.

## Construction used and why

The program-native active carrier is used for the existing action because it
is the carrier on which G1--G3, the DeWitt trace reversal, the right-`H`
structure, and the current/Euler/Krein machinery were actually built. Curt's
`(7,7)` carrier is retained as a source-directed rival because the iceberg
explicitly presents it and because its complex spinor dimension resembles the
source notation. Neither side is declared physically correct.

The construction begins on

\[
Y=\operatorname{Met}_{3,1}(X),\qquad
VY\cong\operatorname{Sym}^2T^*X.
\]

The tautological Lorentz metric supplies

\[
\sharp_h:\pi^*T^*X\longrightarrow\pi^*TX.
\]

A declared connection `nabla` then supplies a horizontal lift

\[
\operatorname{hor}_\nabla:\pi^*TX\longrightarrow H_\nabla Y,
\]

so that

\[
Z_{h,\nabla}(v,\alpha)
=v+\operatorname{hor}_\nabla(\sharp_h\alpha)
\]

is a vector-bundle isomorphism

\[
VY\oplus\pi^*T^*X\cong VY\oplus H_\nabla Y=TY.
\]

This is not canonical from a bare `X`: it depends on `h` and on the ownership
and naturality of the horizontal split. The exact probe represents the map by
the identity only **after** those split coordinates are declared.

## Exact fibre calculation

At `h=diag(1,1,1,-1)`, let

\[
F(k,l)=\operatorname{tr}(h^{-1}kh^{-1}l)
\]

be the raw Frobenius form on `Sym2 T*X`. Its exact inertia is `(7,3)`.
In four dimensions define trace reversal

\[
\tau_h(k)=k-\frac12\operatorname{tr}_h(k)h.
\]

The probe verifies exactly that

\[
\tau_h^2=1,
\qquad
G_{\rm DW}(k,l)=F(k,\tau_h l),
\qquad
\operatorname{inertia}(G_{\rm DW})=(6,4).
\]

Adding the base `(3,1)` block gives the active

\[
G_{9,5}=h\oplus G_{\rm DW},
\qquad
\operatorname{inertia}(G_{9,5})=(9,5).
\]

An exact rational Lorentz boost with `cosh=5/3` and `sinh=4/3` preserves `h`;
its induced `Sym2` action preserves `G_DW`, and `sharp_h` exactly intertwines
the covector and vector actions. This is a nontrivial naturality control, not
just a dimension count.

## The source-signature ambiguity

Curt's iceberg row `CI-09` reports a vertical `(4,6)` and horizontal `(1,3)`
while also reporting total `(7,7)`. If ordered-pair conventions are held fixed,

\[
(4,6)+(1,3)=(5,9),
\]

not `(7,7)`. At least one pair is being ordered differently, one block has an
unstated sign flip, or the total is using a different convention.

There are two simple real block comparators with total `(7,7)`:

\[
h\oplus(-G_{\rm DW})
\quad\text{and}\quad
(-h)\oplus G_{\rm DW}.
\]

They assign the sign flip to different geometric blocks and are not the same
bilinear form. Wave 1 therefore does not choose between them. It uses only the
invariant consequence shared by every literal real `(7,7)` form:

\[
(7,7)\ne(9,5)
\quad\Longrightarrow\quad
\text{no real bilinear-form isometry}.
\]

This is a Layer-0 `UNCERTAIN` at the block dictionary and an exact
`HOMONYM` at the literal total real metric carrier.

## Complex bridge and real obstruction

Multiplying the sign-flipped block by `i` gives a complex congruence. At the
Clifford level,

\[
M(64,\mathbb H)\otimes_\mathbb R\mathbb C
\cong M(128,\mathbb C)
\cong
M(128,\mathbb R)\otimes_\mathbb R\mathbb C.
\]

But the real algebras remain different. Their minimal real modules have
dimensions `256` and `128`, respectively. The vertical phase also fails to
commute with ordinary real conjugation. Consequently:

- the complex `U(64,64)`-type source presentation can remain a common
  container candidate;
- it is not a real-form or right-quaternionic identification;
- active `K`, `C`, Hodge, Shiab, Euler, Green, and Ward operators may not be
  transferred without explicit intertwiners.

## Layer-0 dictionary

| object | disposition | reason |
|---|---|---|
| rank-14 underlying split bundle | `SAME-OBJECT`, conditional | `Z_(h,nabla)` is an isomorphism after `h` and a horizontal split are supplied |
| canonicality from bare `X` | `HOMONYM` | a chosen/naturally owned connection split is additional structure |
| displayed real metric carrier | `HOMONYM` if signatures are literal | `(7,7)` and `(9,5)` have different inertia |
| source block-sign attribution | `UNCERTAIN` | reported component signatures do not add to the reported total under one ordering convention |
| complex Clifford carrier | `SAME-OBJECT` up to noncanonical complex isomorphism | both complexify to `M(128,C)` |
| real Clifford/reality carrier | `HOMONYM` | real matrix-algebra types and minimal modules differ |
| right-`H` structure | `UNCERTAIN` on the source container | no real/reality intertwiner is supplied |
| source and repo actions | `UNCERTAIN` across carriers | carrier-dependent primitives have not been ported |

## Curt steps `CI-01`--`CI-12`

| steps | Wave 1 disposition |
|---|---|
| `CI-01`--`CI-04` | metric bundle, vertical bundle, and rank counts retained |
| `CI-05`--`CI-07` | bundle bridge constructed conditionally on `h,nabla`; global natural ownership open |
| `CI-08` | raw Frobenius form computed exactly |
| `CI-09` | trace reversal computed; block-sign arithmetic remains source-uncertain; literal total real form is not active `(9,5)` |
| `CI-10`--`CI-12` | complex container relation survives; real spinor/reality reduction does not transfer |

## Constraint-surplus ledger

The local negative is invariant rather than fitted: inertia and real Clifford
type cannot be changed by a real change of basis. No coefficient adjustment
can repair them.

The global bridge's surplus is `SURPLUS-UNCOMPUTABLE`. The source has not yet
fixed:

- which block carries the sign convention;
- which connection owns the Zorro horizontal split;
- the naturality group required of that split; or
- whether `U(64,64)` is intended only as a complex container with a later real
  reduction.

Those are charged choices, not free successes.

## Non-regression matrix

| family | Wave 1 effect |
|---|---|
| inhomogeneous group/cocycle/distortion | preserved; these are bundle-level grammar |
| G2/G3 action/Euler/Ward packet | remains built on active `(9,5)`; not yet ported or source-selected |
| gravity and trace reversal | active exact fibre calculation strengthened; no physical Einstein recovery claimed |
| odd matter/Krein | active right-`H` machinery preserved; no transfer to `(7,7)` claimed |
| Higgs/Yukawa | `varpi`/`T` fork untouched and downstream |
| quantum/domain | complex equivalence does not supply a physical real/Krein domain |
| cosmology/dark sector | untouched |
| P1/P2/P3 | carried without consumption; no count inference |

## Source-priority correction after transcript reinspection

Curt's detailed argument does distinguish the two arithmetic comparators.
He explicitly places the choice on the vertical trace line, choosing vertical
`(4,6)` and then motivating total `(7,7)` through the split spin
representation. The source-directed comparator is therefore
`R77_VERTICAL_FLIP`; `R77_BASE_FLIP` is retained only as a hostile control.

This does not close the source dictionary. With one ordered signature
convention, spoken `(4,6)+(1,3)` gives `(5,9)`. The minimal reconstruction is
that the chimeric `H*` contribution enters as `(3,1)`, giving `(7,7)`, but the
transcript does not state that map. C0's real-form non-equivalence remains;
only the ordering of its rival branches changes.

## Third-lane verdict

- `TG-1 CARRIER`: **partial evidence only**. Literal real `(7,7)` is
  non-equivalent, but the result has not survived the unresolved source
  convention/block-attribution check required to pass the gate.
- `TG-2 DYNAMICS`: **open**; no separate complete action/observation packet.
- `TG-3 DISCRIMINATOR`: **open**; no same-domain no-refit difference.

The conjunction is false. Curt stays a rival track inside the Eric lane.

## Wave 2 handoff

Wave 2 should not choose a carrier by taste. It should parameterize the
target-blind action census by

\[
r\in\{(9,5),\ (7,7)_{\rm baseflip},\ (7,7)_{\rm verticalflip},\
\text{complex container}\},
\]

and classify every primitive as:

1. carrier-independent;
2. real-form dependent;
3. pairing/reality dependent; or
4. blocked by the unresolved source dictionary.

Only the carrier-independent IG/cocycle/distortion grammar transfers
automatically. Hodge, Clifford, Krein, charge-conjugation, Shiab, Euler-dual,
Green, and Ward realizations require explicit ports.

## Nonclaims

Wave 1 does not select `(9,5)` or `(7,7)`, prove Curt wrong, prove Eric right,
construct a global canonical connection split, establish unitary physics,
recover a Higgs or field equation, consume external datum, derive a count, or
create a third lane.
