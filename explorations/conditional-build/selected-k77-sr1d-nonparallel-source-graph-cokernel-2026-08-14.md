---
title: "Selected-K77 SR-1D nonparallel source-graph cokernel"
status: active_research
doc_type: exact_class_obstruction
created: "2026-08-14"
registry: lab/process/selected-k77-sr1d-nonparallel-source-graph-cokernel.json
probe: tests/channel-swings/selected_k77_sr1d_nonparallel_source_graph_cokernel_probe.py
grade: "EXACT LOCAL FORMAL TWO-JET CLASS KILL OVER FIXED CANONICAL POINT/ONE-JET"
canon_verdict_change: none
---

# Selected-K77 SR-1D nonparallel source-graph cokernel

## Result first

The nonparallel second-jet reopener has zero constrained metric-graph image.
Both exact SR-1C point/one-jets are killed across **every compatible formal
second jet** over the fixed canonical carrier.

Let `h_m` be an arbitrary correction to the derivative of the `9,555`
symmetric first-jet variables in spatial direction `m`. The already-owned
unreduced Euler differentiation gives the exact matrix identities

```text
j1_m E_T = A h_m,
j1_m E_B = 2 A h_m,
j1_m(E_B-E_T) = A h_m,
```

where `A` is the same `196 x 9,555` rank-`195` action map for every direction
and both algebraic roots. A formal solution must satisfy the differentiated
translation equation

```text
A h_m = 0.
```

Therefore `j1(E_B-E_T)=0` on the entire compatible fibre—not only on the
parallel representative. Inherited differentiated Bianchi and Ricci/Spencer
constraints can shrink that fibre but cannot restore an image already killed
by the translation rows.

The consequence is immediate for both remaining source graphs:

```text
E_epsilon = D_B^!(E_B-E_T)+(D_epsilon S)^!K_S = 0,
(D_g B_Z)^!(E_B-E_T) = 0.
```

The moving-Shiab primitive summand was already proved zero on the fixed
one-jet. Primitive epsilon hence stays closed throughout the compatible
second-jet class. But the total fixed-`varpi` metric row remains

```text
(33703t/468-3/52)(1,0,0,0,-1,0,0,-1,0,-1),
```

which is nonzero on both roots of `28392t^2+91t-351`. The constrained graph
map has rank zero into the one-dimensional trace receiver; the identity
functional on that receiver is an exact left-cokernel certificate against the
nonzero target.

This closes SR-1D. No larger second-jet solve over the same point/one-jet can
repair metric stationarity.

## Exact map accounting

Per spatial direction, the differentiated system has

```text
variables:                 9,555
translation rows:            196
inherited Bianchi rows:     5,096
translation rank:             195
combined rank:              4,290
combined nullity:           5,265
```

Across fourteen directions this is `133,770` serialized variables. The
directionwise action/Bianchi kernel has dimension `73,710` before
cross-direction Ricci/Spencer restrictions. This large kernel is not a rescue:
its complete momentum-jet image is zero because the momentum map is literally
the translation constraint block.

An unconstrained planted second-jet cell fires both `j1E_T` and `j1p`, so the
zero image is not caused by a dead map. It is produced by imposing the source
field equation.

## Why the result is stronger than the parallel kill

The predecessor chose `h_m=0`, proved it compatible, and found zero graph
return. That left open the possibility that a nonzero compatible `h_m` might
generate the opposite trace. SR-1D computes the whole affine fibre. Since

```text
j1p(h_m)-j1p(0) = A h_m
```

and the same `A h_m` must vanish for differentiated translation stationarity,
every compatible choice has the predecessor's zero graph return. No explicit
basis for the large kernel is needed to prove the image theorem.

Primitive epsilon does not provide a looser escape. Its formal adjoint also
factors through `j1p`, while its other moving-Shiab summand is fixed and zero.

## Scope boundary

This is a class-wide kill only over the fixed canonical SR-1C point/one-jet:

```text
T=t Phi1,
DT=-F_BZ+(-t/312-t^2)C+Q,
28392t^2+91t-351=0.
```

It does not exclude:

- a distinct canonical `B_Z` first jet or nonhomogeneous `T,DT` branch;
- a different source-derived Zorro reconstruction;
- the scalar curvature/VEV branch after an actual canonical realization; or
- a source-global stationary background outside the selected K77 parent.

The residual-square second action still has zero first variation at the
printed-residual-zero point and cannot repair this first-action trace.

## Reverse-scaffold consequence

VRS-5 must move up one grade rather than sideways in the same second-jet
fibre. The next gate is `SR-1E`:

```text
construct or exhaust a genuinely distinct canonical point/first-jet branch;
recompute point translation and inherited Bianchi rows;
derive its j1E_T, j1E_B and source-graph relation rather than inheriting A;
test primitive epsilon and total fixed-varpi metric stationarity on that same
carrier before any further prolongation.
```

The highest-value discriminator is whether a new canonical first jet creates
an inhomogeneous `j1p` component not locked to `j1E_T`. If every canonical
first jet retains the factorization `j1p=j1E_T` on shell, that becomes the
structural trace theorem; it is not proved here.

`SR-1` remains `BACKGROUND-MISSING`, `SR-2` remains blocked and VRS-6 has no
background premise. No ledger, canon, residue, quotient datum or public
posture changes. No physical cohomology, superposition law, Born rule,
spectrum or empirical prediction follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_sr1d_nonparallel_source_graph_cokernel_probe.py
```

The exact probe passes `40/40`.
