---
artifact_type: construction_result
created: 2026-08-09
status: NONCONSTANT_AFFINE_DESCENT_AND_XI_REDUNDANCY_EXACT__TWO_FROZEN_FRAME_OPEN_SET_BRANCHES__NATIVE_MOVING_GEOMETRY_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_nonconstant_atlas_xi_prolongation_probe.py
  - tests/channel-swings/selected_k77_nonconstant_atlas_xi_prolongation_independent.sage
registry: lab/process/selected-k77-nonconstant-atlas-xi-prolongation.json
---

# Selected K77 nonconstant atlas and Xi prolongation

## Result first

Two gates close, and one becomes much more precise.

First, the v0.109 curvature/distortion family is compatible with a genuine
nonconstant affine gauge atlas in an exact faithful matrix model. The
connection is transformed with

```text
B^g = g^-1 B g + g^-1 dg,
```

not merely conjugated. Two nonconstant, noncommuting transitions close on a
three-patch overlap; direct and sequential connection transforms agree, and
recomputed `F_B`, `D_B T`, `Upsilon` and `Xi` transform covariantly. Omitting
`g^-1 dg` or reversing the cocycle order fires exact planted failures.

Second, the source itself says `Xi=D_omega Upsilon` is redundant when
`Upsilon=0`. In the frozen scalar receiver this is visible off shell:

```text
Xi = 2(b+t) Upsilon (Phi1 wedge Phi1).
```

At either nonzero branch, adding `Xi=0` does not increase the equation
Jacobian rank. It cannot select the remaining amplitude.

## Two homogeneous open-set witnesses

Freeze `Phi1`, Shiab, Hodge, density and observation coefficients on a
contractible coordinate ball and take

```text
B=b Phi1,
T=t Phi1.
```

Then

```text
F_B=b^2(Phi1 wedge Phi1),
D_B T=2bt(Phi1 wedge Phi1).
```

Intersecting this homogeneous ansatz with the v0.109 source residual and
metric-volume trace gives

```text
312(b+t)^2+t=0,
624(b^2+bt+t^2/3)+t=0.
```

Elimination yields

```text
97344 t^2 (43264 t^2 + 832 t + 1)=0.
```

Besides the zero solution there are two exact algebraic-conjugate branches:

```text
t_+ = (-2+sqrt(3))/208,  b_+ = 1/208-sqrt(3)/312,
t_- = (-2-sqrt(3))/208,  b_- = 1/208+sqrt(3)/312.
```

Both lie on the v0.109 invariant family
`f=t^2/3`, `u=-t/312-4t^2/3`. Because all coefficients are constant, the
source residual and metric-volume trace vanish identically on the open ball,
not only at one jet, and the displayed `Xi` vanishes with them.

## What this does and does not select

The existence result is real, but the numerical amplitudes are selected by
the **homogeneous frozen-frame ansatz** `dB=dT=0`. The source did not demand
that ansatz. These numbers are therefore two exact construction witnesses,
not GU-derived dark-energy magnitudes.

The atlas calculation closes the generic gauge-covariance question, not the
actual native geometry. The unresolved object is now specific: move
`Phi1`, the Shiab, Hodge, density and observation section over `Y14`, derive
the complete primitive-epsilon Euler/Noether relation from the selected
action, and test whether the algebraic branches survive those derivatives.

## Scope fences

- **Layer 0:** source `Xi` redundancy is distinct from an off-shell Noether or
  BV identity.
- **Gauge geometry:** exact affine atlas descent is established in a faithful
  local matrix model; the selected full K77 associated bundle is not ported.
- **Symplectic geometry:** two isolated ansatz branches are not yet a reduced
  critical moduli space, and their amplitude is not classified as gauge,
  boundary, modulus or obstruction.
- **Formal integrability:** moving `Phi`/Shiab/Hodge/density/observation jets
  remain the native Spencer burden.
- **PDE/Krein/analytic:** no propagation, common Green domain, positive
  fundamental symmetry, contour, determinant or measure follows.
- **Cosmology:** no physical magnitude, radiative screening, FLRW solution or
  `w(z)` is claimed.

The local algebraic amplitudes are not added to global residue. Five booked
quotients and P1/P2/P3 remain unchanged. Selected Spin-native, two
`U(32,32)` halves and full `U(64,64)` remain distinct.

## Validation

- primary exact route: `42/42 PASS`;
- independent Sage/`QQ(sqrt(3))` route: `14/14 PASS`;
- missing-affine-term and reversed-cocycle plants fire;
- off-shell `Xi` covariance is nonvacuous;
- source redundancy is not promoted to Noether/BV closure.

## Next gate

Port the two algebraic branches into the actual selected K77 moving
`Phi`/Shiab/Hodge/density/observation packet. Derive the complete primitive
epsilon Euler and off-shell Ward/Noether factorization on that same packet,
then decide whether the branches survive and who owns their amplitude. Only
afterward select the 321-versus-1,571 tangent and resume Hessian/BV.
