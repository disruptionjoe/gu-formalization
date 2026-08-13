---
artifact_type: conditional_build_result
created: 2026-08-07
status: TT_MASSLESS_HELICITY2_AND_MASSIVE_AXIAL_WEIGHT2_WITH_EXTRA_OPEN__EULER_PREBOUNDARY_EXACT__COMPLETE_PHYSICAL_QUOTIENT_OPEN
source_return: SOURCE-CONFIRMS__NORM_SQUARE__SOURCE-SILENT__TT_OWNER_MAP
ledger: lab/process/conditional-physics-ledger-v0.40.json
canon_verdict_change: none
---

# Selected second-layer TT Euler, preboundary and helicity

## Result in plain English

The second action has now reached a genuine spin-two result on its exact
zero-fermion transverse-traceless sector.  The complete selected `Cl2`
quadratic form was already

```text
kappa_1^2 [
  (15376/13689) ||II||^2
  -(340/4563) ||H||^2
].
```

Composing those fixed coefficients with the exact Gauss identity and the
already-tested TT normalization gives, without fitting,

```text
P_TT(box)
 = kappa_1^2 (14356/13689)
   box (box + 1922/3589).
```

Consequently the selected second layer contains:

- one massless helicity-`+/-2` TT pair;
- one massive TT plus/cross pair of axial `SO(2)` spin weight `+/-2` at exact
  dimensionless mass-square `1922/3589` in the inherited `mu_DW` convention;
  its full massive `SO(3)` little-group representation is not yet built; and
- opposite local Green signs at the two poles.

This fires `TT_MASSLESS_HELICITY2_AND_MASSIVE_AXIAL_WEIGHT2_WITH_EXTRA_OPEN`.
It rescues the second-layer TT
route after the first-layer `N2` modes proved to be helicity one.  It does not
yet show that the complete scalar/vector/constraint quotient contains only
the intended two spin-two pairs; it is not the complete physical spectrum.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| section variation | TT variation of the metric section through the exact Gauss/observer map | 100 arbitrary `II` coefficients treated as independent matter |
| total residual | zero-fermion pure-Gauss bosonic tangent, which the 01:20 source pass proved equals the selected bosonic block | the coupled nonzero-fermion direct-sum Hessian |
| two polarizations | the weight-two `SO(2)` representation on plus/cross modulo ordinary diffeomorphisms | a multiplicity-two kernel of unknown spin |
| preboundary | local fourth-order action potential and its antisymmetrized current | a selected Green-Lagrangian domain or reduced BFV phase space |
| opposite signs | pole derivative/Green signs on the finite TT module | global positive energy, unitarity or a bounded right-`H` fundamental symmetry |

The source confirms the residual norm-square architecture. It does not publish
the selected `Cl2 -> II` owner map, the coefficients above, their TT Euler
polynomial or the physical quotient. Source return:
`SOURCE-CONFIRMS__NORM_SQUARE__SOURCE-SILENT__TT_OWNER_MAP`.

## Exact coefficient composition

Write

```text
A = 15376/13689,
B = -340/4563.
```

The traced Gauss identity is

```text
||II||^2 = ||H||^2 - R^X.
```

Therefore

```text
A||II||^2+B||H||^2 = (A+B)||H||^2-A R^X.
```

The inherited TT convention has `P_H(s)=s^2` and
`P_II(s)=s(s+1/2)`. Linearity fixes

```text
C4 = A+B = 14356/13689,
C2 = A/2 = 7688/13689,
m^2 = C2/C4 = 1922/3589.
```

Both coefficients are nonzero and `m^2>0`. Thus the selected trace correction
neither erases the Einstein pole nor collapses the two poles into the
degenerate Willmore/Bach double pole. It shifts the pure-`II` value `1/2` to
the exact value above.

The propagator residues are

```text
Res(s=0)    = +13689/7688,
Res(s=-m^2) = -13689/7688,
```

before the common nonzero `kappa_1^2` factor. The sign pairing is the expected
finite Krein shape, but it is not a global domain theorem.

## Euler and preboundary classes

For either TT polarization, a one-dimensional exact representative is

```text
L_TT = (C4/2)(h'')^2 -(C2/2)(h')^2.
```

Its action variation is

```text
E(h) = C4 h'''' + C2 h'',

theta(h,delta h)
 = C4(h'' delta h' - h''' delta h)
   -C2 h' delta h.
```

The probe verifies coefficientwise and after integration that

```text
delta L = E(h) delta h + d theta.
```

The endpoint term is nonzero on a planted exact polynomial pair. Its
antisymmetrized field-space variation is also exact, nonzero and
antisymmetric. Hence the preboundary class cannot be silently discarded, but
no boundary condition or polarization is selected here.

## Null little-group type

At `k=(1,0,0,1)`, the ordinary metric-diffeomorphism image has rank four.
The plus/cross tensors span rank two and intersect it trivially. The transverse
rotation `J_12` descends as

```text
J_TT = [ 0 -2]
       [ 2  0],

J_TT^2 = -4 I,
char(J_TT) = x^2+4.
```

At the massless root this is the real helicity-`+/-2` module. The planted
helicity-one comparator fails. The same plus/cross plane has axial `SO(2)`
weight `+/-2` at the massive root, while the pole Green coefficients have
opposite signs. This does not establish a full massive `SO(3)` spin-two
multiplet; its possible spin projections `0,+/-1` are part of the open
scalar/vector/constraint quotient.

## Six-lens hostile review

- **Differential geometry:** the result uses the actual metric-bundle normal
  `Sym2(T*X)` and the exact Gauss identity. It is flat/principal TT grade; the
  curved ambient and complete constraint system remain open.
- **Representation theory:** the computation establishes weight two, not just
  dimension two. It does not enumerate every scalar/vector quotient class.
- **Variational PDE:** the fourth-order polynomial and Green concomitant are
  action-derived and exact. Global hyperbolicity, repeated-root domains and
  nonlinear constraint propagation are untested.
- **Symplectic geometry:** the local preboundary potential and current are
  nonzero. No Green-Lagrangian boundary condition, covariant phase space or BFV
  reduction follows automatically.
- **Krein/operator theory:** opposite pole signs give a finite Krein pair. A
  common closed right-`H` domain, bounded fundamental symmetry and loop
  stability remain open.
- **Source criticism:** the source owns the two-layer architecture, not this
  coefficient or physical-carrier conclusion.

Both hostile charges fire as fences: the summary must not promote a TT
subquotient to the complete graviton spectrum, and the calculation must not
continue defending the superseded single-carrier “other Clifford grades”
queue after the source typed spinor Euler equations separately.

## Progress and next gate

```text
Ledger v0.40 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 4
  - selected TT Euler polynomial
  - action-derived fourth-order preboundary potential
  - exact helicity-two TT quotient
  - opposite local pole Green signs
frontier_conditions_opened: 1
  - complete scalar/vector/constraint physical quotient
remaining_named_conditions: 3
  - complete constrained bosonic characteristic complex
  - coupled nonzero-fermion direct-sum Hessian
  - common global Green/Krein plus odd BV/BFV domain
```

No coefficient is selected, no fifth quotient is booked, and P1/P2/P3 remain unused.
Curt remains formally separate and no third lane is promoted.

## Reproduction

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_tt_euler_preboundary_helicity_probe.py
```

The exact probe passes `44/44` with four planted failures.
An independent Sage rational reconstruction returns
`(C4,C2,m2,P'(0),P'(-m2)) =
(14356/13689,7688/13689,1922/3589,7688/13689,-7688/13689)`.
