---
title: "Selected-K77 SR-1C compatible parallel two-jet primitive epsilon"
status: active_research
doc_type: construction_result
created: "2026-08-14"
registry: lab/process/selected-k77-sr1c-compatible-parallel-two-jet-epsilon.json
probe: tests/channel-swings/selected_k77_sr1c_compatible_parallel_two_jet_epsilon_probe.py
grade: "EXACT LOCAL FORMAL TWO-JET; PRIMITIVE EPSILON ZERO; TOTAL METRIC GRAPH OPEN"
canon_verdict_change: none
---

# Selected-K77 SR-1C compatible parallel two-jet primitive epsilon

## Result first

The qualified parallel candidate now constructs as an actual local formal
two-jet. On the canonical-`B_Z`, nonzero-`T` branch, set the covariant
derivative of the complete raw first-jet tensor to zero:

```text
D_m Q_(r,k)^ij = 0,
Q_(r,k)^ij = (D_r T_k)^ij.
```

This assigns all `14 x 9,555 = 133,770` symmetric second-jet slots. It is not
an assignment of zero to the downstream momentum derivative. The jet passes
the missing checks:

- the zero second derivative is Spencer-symmetric;
- the canonical curvature commutator with `Phi1` is exact zero, so the Ricci
  identity permits the parallel choice;
- all `2,744` differentiated translation-action rows vanish;
- all `71,344` differentiated inherited Bianchi rows vanish; and
- direct differentiation of the unreduced local `E_T` and independent-`B`
  `E_B` formulas gives `j1E_T=j1E_B=0`.

Consequently the complete `14 x 196` common-basis first jet of
`p=E_B-E_T` is zero. Its signed formal-adjoint contraction has 91 zero
primitive-Spin components. Composed with the predecessor's independently
computed moving-Shiab zero,

```text
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S = 0
```

on both exact algebraic roots.

This closes primitive epsilon only on the declared parallel formal extension.
The moving fixed-`varpi` Hodge, frame, density, lowerer and observation metric
returns remain open. Neither root is promoted to a stationary background.

## Why this is stronger than the shortcut

The preceding qualification rejected the inference

```text
dt=0 and d(serialized p)=0  =>  j1p=0.
```

That rejection remains valid. The field has a live first jet even when the
scalar amplitude is constant, so differentiating the quadratic `T` terms can
produce forced contributions. The present gate instead differentiates the
unreduced formulas.

For fixed spatial direction let `X=D_mT`. With `D_m(DT)=0` and parallel
curvature, the derivative-bearing companion is zero but the other `E_T`
pieces are

```text
S((1/3)(X T+T X)) + D_X[algebraic adjoint] + *X.
```

The direct-plus-star packet and algebraic-adjoint packet vanish separately,
as does the independent-`B` algebraic derivative. These termwise zeros are
evaluated on every one of the 196 rows in all 14 directions.

## Exact polynomial certificate

The branch family has `T` affine in `t` and its admitted first jet quadratic
in `t`. Each directional Euler coefficient therefore has degree at most three.
The probe evaluates the unreduced formulas exactly over `QQ` at four distinct
amplitudes `t=0,1,2,3`. Every `E_T` and `E_B` derivative is zero at all four,
which certifies the entire polynomial rather than selecting or approximating a
root. Both real roots of

```text
28392 t^2+91 t-351
```

are included automatically.

## Controls

- A planted nonzero symmetric second-jet cell produces a live response through
  the exact rank-195 action map.
- A branch-transverse amplitude derivative produces a live `E_T` response;
  simple-root rigidity correctly excludes that direction from the extension.
- The prior moving-Shiab return is not vacuous: its two input image banks each
  have rank 91 before pairing.

## Layer 0 and claim ceiling

The owner is the selected noncyclic first action, not the printed residual.
The object is a covariant local formal two-jet, not a globally parallel field,
open solution germ, total `Y14` stationary background, analytic domain,
physical cohomology, positive state space or superposition rule.

No ledger, canon, residue, quotient datum or public posture changes.

The exact Sage probe passes `34/34`.

## Next exact gate

On this same two-jet, compute the fixed-`varpi` moving Hodge, frame, density,
lowerer and observation returns and add them to the live direct metric partial.
A nonzero total row kills this formal extension as a stationary background; an
exact zero advances to the next formal-integrability prolongation without yet
proving an analytic solution.
