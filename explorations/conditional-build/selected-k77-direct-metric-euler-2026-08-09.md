---
title: "Selected K77 direct ten-component metric Euler"
date: 2026-08-09
status: EXACT_RANK_ONE_TRACE_DEMAND__DYNAMIC_VEV_CANCELLATION_OPEN
grade: "Exact finite real-K77 first variation on the selected Spin-native parent; no full stationary vacuum, Einstein equation, dark-energy magnitude, BV quotient or domain claim"
---

# Selected K77 direct ten-component metric Euler

## Result

The repaired nontrivial branch

```text
B* =  Phi1/156
T* = -Phi1/78
A* = -Phi1/156
```

is critical in all 1,470 admitted low-grade `B` directions and all 1,470
admitted low-grade `T` directions, and its raw translation residual is zero.
It is nevertheless not a full bosonic saddle. Its direct metric Euler
covector is nonzero but has rank only one: all nine traceless metric directions
vanish, while one Lorentz-trace direction survives.

In the canonical physical `Sym2(T*X)` order

```text
(00,01,02,03,11,12,13,22,23,33),
```

the normalized covector is

```text
(-7/9126, 0, 0, 0, +7/9126, 0, 0, +7/9126, 0, +7/9126).
```

This is one generated cosmological-type trace demand, not ten independent
failures and not a loss of the ten-dimensional Einstein receiver.

## Layer 0

Four objects must remain distinct:

1. metric variation at fixed coordinate `B/T` coefficients;
2. metric variation at fixed source variables `(varpi,epsilon)`, where
   `delta T=-delta B_LC`;
3. variation in a co-moving Clifford frame transporting `Phi`, Hodge and the
   selected Shiab; and
4. the intrinsic total first variation.

The prior all-ten normal bank proved exact co-moving transport of the complete
pairing/Hodge/Phi/Shiab packet, while showing that its left/right owner split is
not canonical. On the present branch this no longer blocks the first
variation: any change of low-grade field lift changes it by

```text
<E_B, delta B> + <E_T, delta T> = 0.
```

The fixed-`B/T`, fixed-`varpi`, and co-moving routes therefore agree on the
full admitted low-grade tangent without a new vertical connection or datum.
This lift-independence is branch-relative; the old noncritical fixture remains
a planted counterexample.

## Exact derivation

At the repaired branch, the selected first-action polynomial evaluates to

```text
L_1(B*,T*) = 7/18252.
```

For the trace-reversed physical gimmel

```text
G(g) = g direct-sum D_g
```

the exact ten induced metric derivatives give

```text
rho(h) = (1/2) Tr(G^-1 delta G) = -2 Tr(g^-1 h).
```

Thus the density covector is

```text
(-2,0,0,0,+2,0,0,+2,0,+2),
```

of rank one with kernel dimension nine. Functorial transport holds the scalar
action value fixed in the co-moving frame; the remaining coordinate top-form
motion is `rho(h)L_1`. Multiplication gives the displayed metric Euler
covector. In the fixed `Sym2` coordinate basis `sqrt(abs(det G))=8`, so the
coordinate coefficient is exactly eight times the normalized covector. The
Hodge volume factor is already inside this density response and is not counted
again.

An independent Sage/QQ derivation reconstructed the DeWitt matrix, all ten
normal derivatives, the action polynomial and both normalized and coordinate
covectors without reading the primary output.

## The second action cannot cancel it on this branch

The selected second layer is a residual-square action. Since the raw residual
is zero here,

```text
delta I_2 = 2 <Upsilon, delta Upsilon> = 0
```

for every first variation. It therefore cannot cancel the nonzero first-action
trace at this same background. This preserves the distinction between the two
action parents rather than silently merging their roles.

## Source return and constructive interpretation

- `SOURCE-CONFIRMS`: Weinstein's released action uses the full upstairs
  two-connection difference `T_omega` and a nonlinear first action.
- `SOURCE-CONFIRMS`: his cosmological argument calls for a movable
  `varpi`/curvature VEV relation rather than a separately fixed `Lambda g`.
- `SOURCE-SILENT`: the repaired K77 branch, its rank-one metric covector and
  any exact cancellation of it.

The new result should therefore be used as a demand on the construction, not
as a no-go. The existing dynamic cosmological/curvature sector is now the
first comparison target: vary it on this same branch and ask whether it emits
the exact opposite rank-one covector. If an already-owned VEV amplitude is
selected by that one equation with no new coefficient, the fit has positive
constraint content. If a new freely adjustable counterterm is introduced only
to cancel the number, the result is merely relocated fine-tuning.

No physical scale is derived by the rational coefficient above; it is in the
normalization of the selected finite action. No radiative stability,
vacuum-energy screening, observed magnitude, `w(z)`, DESI prediction or
Einstein identification follows.

## Consequence for sequencing

The direct metric gate is closed, but it closes negatively for full
stationarity. The 321-versus-1,571 field-tangent selection and full Hessian
should not be promoted on a noncritical background. The efficient successor is:

1. construct the existing dynamic `varpi`/curvature VEV metric-stress packet;
2. test exact cancellation of the one trace covector with preregistered
   constraint surplus and no fixed `Lambda` insertion;
3. if it closes, resume tangent selection, the full first/second-action Hessian,
   action BV, trace soldering, domain and odd BFV;
4. if it fails, search the smallest action-owned trace sector or an alternate
   common branch before expanding the Hessian.

## Validation and fences

- primary exact route: `45/45 PASS` after all-ten naturality receipts;
- independent Sage/QQ route: `11/11 PASS`;
- all 1,470 `B/T` lift corrections annihilate the first variation;
- rank-one, double-density and raw-residual-as-saddle plants fire;
- selected Spin-native, two `U(32,32)` halves and full `U(64,64)` remain
  distinct;
- P1/P2/P3 remain unchanged and unused.

No stationarity, Einstein equation, Standard Model recovery, positivity,
hyperbolicity, contour, global domain, BV/BFV quotient, dark-energy magnitude,
chirality, mass, index or generation count is claimed.
