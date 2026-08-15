---
title: "Selected-K77 SR-1C branch momentum zero-jet"
status: active_research
doc_type: construction_result
created: "2026-08-14"
lane_id: SRC-RES-COH-01
registry: lab/process/selected-k77-sr1c-branch-momentum-zero-jet.json
probe: tests/channel-swings/selected_k77_sr1c_branch_momentum_zero_jet_probe.py
grade: "EXACT 196-ROW BRANCH MOMENTUM ZERO-JET AND MOVING-SHIAB RETURN; SPATIAL J1P STILL MISSING"
canon_verdict_change: none
---

# Selected-K77 SR-1C branch momentum zero-jet

## Result first

The first lower component of `O_SR1C` now serializes. On the exact
canonical-`B_Z`, nonzero-`T` witness, the already-owned translation Euler row
vanishes on both roots, while the independent-`B` Euler covector is nonzero.
Therefore the connection momentum

```text
p = E_B-E_T
```

equals the newly computed `E_B` zero-jet on this branch.

In the common 196-row grade-one action-covector basis, `p` has exactly fourteen
nonzero diagonal invariant cells. Every coefficient is affine in the root
amplitude `t` and is one of

```text
+/-(7/2-t),   +/-(9/2-t).
```

Because `28392t^2+91t-351` is irreducible over the rationals, none of these
nonzero affine coefficients can vanish on either real root. The momentum is
therefore live on both branches.

The algebraic moving-Shiab primitive-epsilon return was also evaluated on all
91 Spin generators. Its `F_BZ` and invariant-curvature image banks each have
rank 91, but pairing them with `T=t Phi1` gives an exact zero row. Thus the
primitive epsilon equation now reduces locally to the still-missing spatial
divergence `D_B^!p`; the zero moving-Shiab return does not make that equation
vanish because `p` itself is live.

## Action-owned reconstruction

For an independent `B` variation `U`, the derivative-bearing path average has

```text
delta_B Fbar[U] = D_B U + (1/2)(U T+T U).
```

The first term has twice the formal-adjoint coefficient of the corresponding
`E_T` companion, since `E_T` contains `(1/2)D_B(delta T)`. The probe therefore
assembles

```text
E_B,derivative
  = 2 [companion(-F_BZ/2)
       + companion((-t/312-t^2)C/2)
       + companion(Q_symmetric)].
```

It then computes the independent algebraic term

```text
<T,S_selected((U T+T U)/2)>
```

directly against every dual basis row. The thirteen-cell symmetric correction
is the exact rational correction already proven to solve all 196 `E_T` rows
and all 5,096 inherited Bianchi rows. Deleting either that correction or the
nonzero-`T` algebraic term changes the resulting momentum and fires a planted
control.

Every coefficient is accumulated as `c0+c1 t+c2 t^2` and only then reduced in

```text
Q[t]/(28392t^2+91t-351).
```

No floating root is selected.

## Exact support

Let `A7=7/2-t` and `A9=9/2-t`. In input-axis order the diagonal support is:

| input axis | common row | coefficient |
|---:|---:|---:|
| 0 | 182 | `+A9` |
| 1 | 169 | `+A9` |
| 2 | 156 | `-A9` |
| 3 | 143 | `+A9` |
| 4 | 130 | `+A7` |
| 5 | 117 | `-A7` |
| 6 | 104 | `+A7` |
| 7 | 91 | `-A7` |
| 8 | 78 | `+A7` |
| 9 | 65 | `-A7` |
| 10 | 52 | `-A9` |
| 11 | 39 | `+A7` |
| 12 | 26 | `-A7` |
| 13 | 13 | `+A7` |

All other 182 common rows vanish at zero-jet grade.

## Moving-Shiab return

The path-average curvature at the witness is

```text
Fbar = (1/2)F_BZ + (-t/624-t^2/6) C.
```

For each of the 91 primitive Spin generators `eta`, the probe evaluates

```text
<t Phi1,(D_eta S_selected)(Fbar)>.
```

Both constituent moving-Shiab image families have exact rank 91, yet all 91
paired coefficients vanish after exact quadratic reduction. This is a live-
image pairing zero, not frozen coefficient motion.

## What is and is not closed

| `O_SR1C` component | status |
|---|---|
| all nominal top-order slots | disposed |
| `p=E_B-E_T` zero-jet | **serialized; support 14; live on both roots** |
| moving-Shiab primitive zero-jet return | **exact zero with rank-91 live-image controls** |
| spatial `j^1p` | type-missing |
| primitive `D_B^!p` | blocked by spatial `j^1p` |
| moving Hodge/frame/density/lowerer metric returns | type-missing |
| total fixed-`varpi` metric row | incomplete |

The next swing must differentiate this exact fourteen-cell momentum on the
admitted formal first jet, preserving the branch quotient and common basis.
Only then can it compose `D_B^!p` and decide primitive epsilon stationarity.

## Claim ceiling

The live momentum value is not an epsilon obstruction: a divergence cannot be
inferred from a point value. The moving-Shiab zero is not the total primitive
epsilon row. No compatible stationary jet, open background, total complex,
physical cohomology, positive pairing, superposition law or Born rule follows.
Both roots remain `NOT-YET-FALSIFIED`; `SR-1` remains `BACKGROUND-MISSING` and
`SR-2` remains blocked.

## Evidence

- `tests/channel-swings/selected_k77_sr1c_branch_momentum_zero_jet_probe.py`
  — `29/29 PASS`.
- `lab/process/selected-k77-sr1c-branch-momentum-zero-jet.json`.
- `lab/process/hostile-reviews/2026-08-14-selected-k77-sr1c-branch-momentum-zero-jet-review.md`.
