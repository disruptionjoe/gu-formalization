---
title: "K299 Order-Seven Positive Peano Simplex Rule"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-22"
claim_ceiling: "Exact positive one-node angular cubature and second-derivative Peano remainder; face legality and numerical global derivative norms remain separate."
manifest: lab/process/k299-order-seven-positive-peano-simplex-rule.json
producer: tests/channel-swings/k299_order_seven_positive_peano_simplex_rule.py
probe: tests/channel-swings/k299_order_seven_positive_peano_simplex_rule_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: POSITIVE_SECOND_DERIVATIVE_ANGULAR_RULE_CONSTRUCTED__GLOBAL_NORM_OPEN
canon_verdict_change: none
---

# K299 Order-Seven Positive Peano Simplex Rule

## GU-COMPARATOR-ROUTING

This is an `INTERNAL_STRUCTURAL_ONLY` result about the repository-supplied
conditional Fock construction. It does not identify a source-selected action
or move a physics-ledger row.

```gu-typed-objects
result: exact positive one-node Duffy cubature and tensor Peano remainder on the K294 projective simplex times endpoint interval
carrier: complete K288 order-seven coherent Gram occurrence family with its native projective weight retained LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing before coherent signed group composition PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection and real Bessel K1 kernel
grading: order seven, primitive gap order r0,r1,r2,c0,c1,c2 and endpoint coordinate y
action_owner: repository construction from K139/K156/K179; no source-selected GU action or physical state is supplied
target: replace K298's illegal fourth-derivative global remainder by a positive rule using only second directional derivatives MAP-TYPE=intertwiner
```

## Exact rule

Use the ordered Duffy chart

```text
p_j = t_j product_(i<j)(1-t_i),  j=0,...,4,
p_5 = product_(i<5)(1-t_i).
```

Its Jacobian is `product_(j=0)^4 (1-t_j)^(4-j)`. The five
one-dimensional weights are `(1-t)^(n-1)` for `n=5,4,3,2,1`; their
means are `1/(n+1)`. The tensor mean maps exactly to `p_i=1/6` for all
six gaps. The independent uniform `y` factor has mean `1/2`. Hence

```text
integral_(Delta_5 x [0,1]) F(p,y) dp dy
  approximately (1/120) F((1/6,...,1/6),1/2).
```

For `I_n[h]=integral_0^1 (1-t)^(n-1)h(t)dt`, the error has the exact
Peano form

```text
I_n[h]-I_n[1]h(1/(n+1)) = integral_0^1 K_n(s) h''(s) ds.
```

`K_n` is nonnegative, has mass `1/(2(n+1)^2(n+2))`, and vanishes to
order two at `s=0` and order `n+1` at `s=1`. Tensor telescoping produces
six terms and no mixed or higher derivative requirement. The complete native
factor `product(p_i)y(1-y)` remains inside `F`; the rule never divides away
K296's face zeros.

## Decision boundary

K299 supplies the missing legal positive rule, but it does not yet prove that
its six complete coherent directional-derivative norms are finite or
numerically small. K300 transfers the rule through the K296/K297 face atlas.
No radial gamma join, exterior value, action-column value, residual or native
K152 interval follows from the cubature identity alone.
