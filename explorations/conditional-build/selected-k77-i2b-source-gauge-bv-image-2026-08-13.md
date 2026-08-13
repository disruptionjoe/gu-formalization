---
title: Selected K77 I2B source tangent and gauge/BV image
date: 2026-08-13
lane: Eric / Lane 1 / conditional Build
grade: EXACT_LOCAL_SELECTED_REAL_K77_FIXED_BACKGROUND
verdict_change: none
canon_change: none
public_posture_change: none
---

# Selected K77 I2B source tangent and gauge/BV image

## Result in plain English

The twelve surviving fixed-background Euler equations are not removed by the
source's tilted quotient or by the genuine local adjoint gauge image on the
selected distortion field.

The crucial distinction is:

- `alpha` is an arbitrary variation of the source field `varpi`; it is a
  physical Euler test direction, not a gauge direction;
- the tilted source subgroup has `alpha=D_A zeta`, so its image in
  `delta T=alpha-D_A zeta` is exactly zero; and
- after passing to the distortion `T`, residual gauge motion is homogeneous
  adjoint motion. Its projected image on the 196-real Cl1 bank has rank 25.

That rank-25 image is disjoint from the twelve diagonal cells. The branch
Euler covector annihilates the gauge image, as Noether theory requires, but is
still nonzero on the quotient. Therefore the equations survive gauge descent.

This kills one tempting escape: calling all `varpi` translations gauge would
erase the field itself, not construct a physical quotient. The next live route
is the actual moving reference/metric/section/Hodge/Shiab response (or a larger
action-owned moving graph), not an external datum and not a fitted restriction.

## Layer 0

The source chart is

\[
  \delta T=\alpha-D_A\zeta .
\]

At the selected grade, write the projected adjoint map as

\[
  G:\mathfrak{spin}(7,7)\longrightarrow
  \Omega^1\otimes\mathrm{Cl}_1,
  \qquad \zeta\longmapsto[\zeta,H_q].
\]

Then the source chart has matrix

\[
  [I_{196}\; -G]
\]

and the tilted graph has matrix

\[
  \begin{bmatrix}G\\I_{91}\end{bmatrix}.
\]

Their composition is zero, while the source chart has rank 196. Thus the
tilted quotient retains all 196 distortion coordinates. It does not quotient
the distortion away.

## Exact gauge image

The trace-Hq base has the two real-form components

\[
  i\,e^{12}\otimes\gamma_{12}
  +e^{13}\otimes\gamma_{13}.
\]

The exact real-Clifford computation uses all 91 grade-two generators. It finds:

| quantity | exact value |
|---|---:|
| selected T-bank dimension | 196 |
| grade-two gauge parameters | 91 |
| projected adjoint-image rank | 25 |
| coordinate support rows | 26 |
| stabilizer dimension | 66 |
| twelve-cell intersection | 0 |
| tilted-graph T-image rank | 0 |

The 26 supported coordinates are

\[
 (12,a),\ a\ne12,\qquad (13,a),\ a\ne13.
\]

The rotation in the `12-13` plane couples two of those cells, so their span has
rank 25, equal to `91-66`. The surviving Euler space is instead

\[
 \operatorname{span}\{(0,0),\ldots,(11,11)\},
\]

and hence has zero intersection with the gauge image.

Clifford-grade selection makes this the complete projected even-Clifford
contribution to the Cl1 bank: grade two maps Cl1 to Cl1; grade zero is central;
the other grades do not return a Cl1 component.

## Variational and symplectic meaning

Let `e` be the twelve-cell branch Euler covector. The exact checks give

\[
  e^T G=0,
  \qquad e\ne0.
\]

This is the correct Ward behavior. It means `e` descends to a nonzero covector
on the local gauge quotient. A gauge-basic Euler equation is not the same as a
vanishing Euler equation.

Calling the full `alpha` image gauge would instead quotient by the identity map
on the 196 field coordinates. That planted alternative deletes the physical
distortion field and is rejected at Layer 0.

## Source return

- `SOURCE-CONFIRMS` (`SC-ACT-01`): the action is written in the source
  coordinates `(epsilon,varpi)`, with `T=varpi-epsilon^{-1}d_0 epsilon` and
  arbitrary `varpi+s alpha` variation.
- `SOURCE-CONFIRMS`: the right-trivialized source grammar gives
  `delta T=alpha-D_A zeta` and the tilted graph lies in its kernel.
- `SOURCE-SILENT`: the source does not print the selected 196-cell K77 bank,
  its rank-25 adjoint image, or the twelve-cell quotient intersection.
- `REPOSITORY-DERIVES`: the exact local negative result above.

## Fences

This result is conditional on the selected real K77 fixed-background bank. It
does not construct the full BV/Koszul--Tate complex, reducibility tower, global
BFV phase space, edge modes, common Krein domain, or the full moving
metric/reference/section/Hodge/Shiab response. The two
`C^(32,32)` carrier halves, their block subgroup, and the full `U(64,64)` action
parent remain distinct and unported.

No ledger verdict, residue, quotient count, P1/P2/P3 assignment, canon claim,
or public posture changes.

## Next gate

Construct the actual source/action-owned moving geometric Fréchet response on
the twelve-cell covector: vary the reference connection, metric, observation
section, Hodge/Shiab coefficients and moving trace-Hq frame together, preserving
the exact Ward identity. Test whether its image supplies the two determinant-80
Euler shapes without fitting a cancellation.

## Executable receipt

`tests/channel-swings/selected_k77_i2b_source_gauge_bv_image_probe.py`
passes 53/53 exact, source, Layer-0, preflight, planted and scope checks.
