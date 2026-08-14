---
title: "Selected-K77 SR-1C metric epsilon3 top block"
status: active_research
doc_type: construction_result
created: "2026-08-14"
lane_id: SRC-RES-COH-01
registry: lab/process/selected-k77-sr1c-metric-epsilon3-top-block.json
probe: tests/channel-swings/selected_k77_sr1c_metric_epsilon3_top_block_probe.py
grade: "EXACT SELECTED METRIC-EPSILON3 ZERO CERTIFICATE; LOWER O_SR1C BANK STILL MISSING"
canon_verdict_change: none
---

# Selected-K77 SR-1C metric `epsilon^3` top block

## Result first

The last unresolved top-order slot of the fixed-`varpi` metric row is exactly
zero on the selected K77 tensor bank. The mixed density symbol is

```text
-1/2 [ <delta B_epsilon, S_selected(k wedge delta B_g)>
     + <delta B_g,       S_selected(k wedge delta B_epsilon)> ].
```

After inserting the exact ten-column Levi-Civita symbol and the exact
91-column primitive `Spin(7,7)` symbol, the resulting `10 x 91` matrix has
rank zero and no nonzero entries for timelike, spacelike and null covectors.
The zero is termwise rather than a cancellation between the two halves:

- `k wedge delta B_epsilon=0` by exterior-symbol nilpotence because
  `delta B_epsilon=k eta` at principal grade;
- the other half vanishes coefficientwise under the selected K77 same-grade
  action pairing, even though the metric curvature and its selected-Shiab
  image both have rank six.

The safe metric envelope therefore reduces again:

```text
(g,varpi,epsilon) <= (3,2,3)
                 -> (3,2,2).
```

This completes the top-order reduction of `O_SR1C`. It does not complete the
branch-dependent lower mixed coefficient bank.

## Action-owned derivation

At fixed independent `varpi`, every source variation of the reference
connection satisfies

```text
delta T = -delta B.
```

Only the derivative-bearing first-action cell can carry two metric
derivatives and one epsilon derivative:

```text
<T, S_selected(F_B + (1/2)D_B T)>.
```

At top grade its first variation in a fixed-`varpi` splitting direction `u`
is

```text
delta(F_B + (1/2)D_B T)
  = d u - (1/2)d u
  = (1/2)d u.
```

Polarizing in a metric direction `u=delta B_g` and a primitive epsilon
direction `w=delta B_epsilon` gives precisely

```text
-(1/2)[<w,S(d u)> + <u,S(d w)>].
```

The Levi-Civita lift contributes one `k`, its curvature contributes the
second, and the primitive epsilon lift contributes the third. Moving Shiab,
Hodge, frame, density and lowerer coefficients depend on undifferentiated
primitive epsilon at this top count and therefore belong to the surviving
order-two-or-lower bank, not to `epsilon^3`.

## Exact coefficient result

| covector | `rank(delta B_g)` | `rank(delta B_epsilon)` | metric curvature | selected image | epsilon curvature | mixed rank |
|---|---:|---:|---:|---:|---:|---:|
| timelike | 9 | 91 | 6 | 6 | 0 | **0** |
| spacelike | 9 | 91 | 6 | 6 | 0 | **0** |
| null | 9 | 91 | 6 | 6 | 0 | **0** |

Thus the zero cannot be attributed to frozen or absent inputs. The metric
source bank, primitive epsilon source bank, curvature bank and selected-Shiab
metric image are all live. Both polarized summands nevertheless vanish
coefficientwise on the action pairing.

The coefficient contains no background amplitude `t`, so the certificate is
common to both roots of `28392 t^2+91 t-351`.

## What remains of `O_SR1C`

| component | status |
|---|---|
| primitive-epsilon action-owned top block | constructed; rank 13 |
| metric `g^4` block | exact zero |
| metric `varpi^3` block | exact zero |
| metric `epsilon^3` block | **exact zero** |
| reduced metric envelope | **`(3,2,2)`** |
| branch-dependent lower `j^1(E_B-E_T)` coefficients | type-missing |
| moving Shiab/Hodge/frame/density/lowerer returns | type-missing |
| common 196-row branch serialization and held-out roots | incomplete |

The next useful swing is no longer another order estimate. It is the exact
lower-bank serialization on the two algebraic roots, followed by held-out
evaluation and a compatible-jet solve only at the surviving orders.

## Claim ceiling

This is a local selected-symbol zero certificate, not a full metric Euler
operator, stationary background, total deformation complex, physical
cohomology, positive pairing, superposition law or Born rule. It does not
select between the two exact roots. Both remain `NOT-YET-FALSIFIED`; `SR-1`
remains `BACKGROUND-MISSING` and `SR-2` remains blocked.

## Evidence

- `tests/channel-swings/selected_k77_sr1c_metric_epsilon3_top_block_probe.py`
  — `29/29 PASS`.
- `lab/process/selected-action-offgraph-dbt-principal-symbol.json` —
  independent predecessor theorem that the complete selected same-grade `Cl2`
  raw action pairing has rank zero on all three causal representatives.
- `lab/process/selected-k77-sr1c-metric-epsilon3-top-block.json`.
- `lab/process/hostile-reviews/2026-08-14-selected-k77-sr1c-metric-epsilon3-top-block-review.md`.
