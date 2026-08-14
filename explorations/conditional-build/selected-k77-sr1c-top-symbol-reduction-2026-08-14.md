---
title: "Selected-K77 SR-1C action-owned top-symbol reduction"
status: active_research
doc_type: construction_result
created: "2026-08-14"
lane_id: SRC-RES-COH-01
registry: lab/process/selected-k77-sr1c-top-symbol-reduction.json
probe: tests/channel-swings/selected_k77_sr1c_top_symbol_reduction_probe.py
grade: "EXACT ACTION-OWNED PRIMITIVE TOP SYMBOL AND STRUCTURAL METRIC ORDER REDUCTION; LOWER MIXED O_SR1C BANK STILL MISSING"
canon_verdict_change: none
---

# Selected-K77 SR-1C action-owned top-symbol reduction

## Result first

The first actual top block of `O_SR1C` now constructs. With the repository
Green-sign convention, the action-owned primitive-epsilon principal symbol is

```text
sigma_top(E_epsilon)(k)a
  = -(1/2) k wedge S_selected(k wedge a).
```

On the complete 196-column K77 one-form/grade-one potential bank, its generic
connection-symbol input rank is 182 and its output rank is exactly 13 on each
nonzero covector orbit:

| covector | input rank | action-owned top rank | nonzero columns |
|---|---:|---:|---:|
| positive | 182 | 13 | 13 |
| negative | 182 | 13 | 13 |
| null | 182 | 13 | 28 |

This block is independent of the algebraic amplitude `t`, so it is identical
on both roots of `28392t^2+91t-351`.

The nominal fixed-`varpi` metric envelope also reduces. The selected source
density is jointly affine in its highest `g^2` and `varpi^1` jets. Therefore
the metric `g^4` block and the mixed `varpi^3` block vanish identically. The
safe metric envelope falls from

```text
(g,varpi,epsilon) <= (4,3,3)
```

to

```text
(g,varpi,epsilon) <= (3,2,3).
```

The `epsilon^3` metric cross-block is not removed: the coefficient of the
metric second jet contains `T=varpi-B(g,epsilon)`, and a source-shaped exact
control leaves an `epsilon^3` term live. Whether the selected tensor
coefficient cancels on the K77 branch remains uncomputed.

The disposition is therefore

```text
ACTION_OWNED_PRIMITIVE_EPSILON_TOP_SYMBOL_RANK_13_ON_ALL_COVECTOR_ORBITS
__METRIC_G4_AND_VARPI3_TOP_BLOCKS_EXACTLY_ZERO
__O_SR1C_LOWER_MIXED_BANK_TYPE_MISSING.
```

This is a strict advance inside VRS-5, not completion of `O_SR1C`.

## Action-owned derivation

Write the selected first-action path average and its adjoint receiver as

```text
Fbar = F_B + (1/2)D_B T + (1/3)T^2,
Y    = S_selected^! T.
```

For independent `B,T` variation, the derivative-bearing pieces of the two
Euler covectors are

```text
E_B,top = D_B^!Y,
E_T,top = S_selected((1/2)D_B T) + (1/2)D_B^!Y.
```

Hence the connection momentum `p=E_B-E_T` has

```text
p_top = (1/2)D_B^!S_selected^!T
        -(1/2)S_selected(D_B T).
```

Primitive epsilon applies one further `D_B^!`. At principal-symbol grade,
the exterior adjoint symbol is wedge by `k` up to the already-fixed Green
sign, and its square vanishes:

```text
sigma(D_B^!)^2 = k wedge k wedge = 0.
```

The adjoint-square term therefore cancels, leaving exactly

```text
-(1/2) k wedge S_selected(k wedge a).
```

The earlier eddy result had computed this finite K77 matrix only for the
source-printed rival and correctly left the action-owned degree-fourteen row
open. The formula above supplies the missing ownership derivation at top
principal grade. It does not identify the full lower-order action Euler with
the printed endpoint.

## Exact K77 coefficient result

The probe reconstructs the complete selected `comm/symi/symi` bank rather
than importing only its rank. For each positive, negative and null covector it
builds all `14 x 14=196` potential columns, computes `k wedge a`, applies the
selected Shiab, and applies the final `k wedge`. Exact sparse ranks give the
table above.

The rank-thirteen result is not a physical mode count. It is an action-owned
top Euler-symbol rank on a generic adjoint connection-symbol carrier. The same
selected Shiab continues to close on the separate rank-91 algebraic-Riemann
carrier; that earlier Bianchi result is not contradicted.

## Structural metric order reduction

In primitive coordinates, `B(g,epsilon)` has first source order and
`T=varpi-B`. The path average contains the highest derivatives only through

```text
F_B                 linear in g^2,
(1/2)D_B T          linear in g^2 and varpi^1,
```

while `T`, the Shiab coefficients, Hodge, frame, density and lowerer do not
introduce another `g^2` or `varpi^1` factor. Thus the density has neither a
`(g^2)^2` term nor a `g^2 varpi^1` term.

For the metric Euler operator, the nominal `g^4` coefficient is the Hessian
of the density with respect to `g^2`, and the nominal `varpi^3` coefficient is
the corresponding mixed top Hessian. Both are exactly zero. This is a
structural zero certificate, not a finite-difference inference.

The same argument does not remove `epsilon^3`. The highest metric coefficient
may depend on the first epsilon jet through `T`. Two total derivatives can
therefore reach `epsilon^3`. The exact scalar control in the probe retains
both this slot and a `varpi^2` slot while killing `g^4` and `varpi^3`; it is an
order control, not the selected K77 tensor coefficient.

## What remains of `O_SR1C`

| component | status |
|---|---|
| primitive-epsilon principal block | **constructed**, branch-independent rank 13 |
| metric `g^4` block | **exactly zero** |
| metric `varpi^3` block | **exactly zero** |
| metric `epsilon^3` selected tensor block | **type-missing** |
| lower mixed `j^1(E_B-E_T)` coefficients on the nonzero-`T` branch | **type-missing** |
| moving Shiab/Hodge/frame/density/lowerer returns | **type-missing** |
| common 196-row branch serialization and held-out root evaluation | **incomplete** |

Both algebraic roots remain `NOT-YET-FALSIFIED`. A nonzero top symbol proves
that the primitive equation genuinely needs prolongation; it does not prove
that either branch fails after the admitted higher jets are solved.

## Next gate and claim ceiling

Next compute the selected metric `epsilon^3` block and the remaining
branch-dependent lower mixed coefficients of `O_SR1C` on the reduced
`(3,2,3)` metric envelope. Serialize them in the common basis, include the
moving Shiab/Hodge/frame/density/lowerer returns, and held-out validate both
algebraic roots before solving compatible jets.

No stationary background, total `K/L`, physical cohomology, positive pairing,
closed domain, superposition law or Born rule is constructed. `SR-1` remains
`BACKGROUND-MISSING`; `SR-2` remains blocked. No ledger, canon, residue,
quotient, datum or public-posture change occurs.
