---
title: "K298 Order-Seven Coherent Terminal-Corner Obstruction"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-22"
claim_ceiling: "Exact ordered-coherent cofactor theorem and nonzero terminal fourth-derivative obstruction; no divergence of the integrand value or complete exterior bound."
manifest: lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json
producer: tests/channel-swings/k298_order_seven_coherent_terminal_corner_obstruction.py
probe: tests/channel-swings/k298_order_seven_coherent_terminal_corner_obstruction_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: ORDERED_COHERENT_SUM_DOES_NOT_CANCEL_TERMINAL_FOURTH_DERIVATIVE__METHOD_SWITCH_REQUIRED
canon_verdict_change: none
---

# K298 Order-Seven Coherent Terminal-Corner Obstruction

## GU-COMPARATOR-ROUTING

This is an `INTERNAL_STRUCTURAL_ONLY` result about the repository-supplied
conditional Fock construction. It does not identify a source-selected action
or move a physics-ledger row.

```gu-typed-objects
result: exact cofactor reconstruction of the ordered old-position coherent sum and proof that its terminal fourth-derivative leading coefficient is nonzero
carrier: four K288 coherent groups on even cumulative positions 2,4,6,8 LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing before upper-triangle integral compression PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection and real Bessel K1 kernel
grading: conserved incidence charges, impurity seed, bath species, order seven, old position and terminal face support
action_owner: repository-construction from K139, K156 and K179; no source-selected GU action or physical state is supplied
target: decide whether ordered coherent cancellation repairs the K297 terminal fourth derivative MAP-TYPE=intertwiner
```

## Ordered sum and cofactor identity

Every relevant coherent group has old positions `(2,4,6)` and coefficient
vector `c=(1,-1,1)`. Its six stored K288 entries are the upper triangle after
integral symmetry. Restoring all nine ordered entries gives

```text
sum_(a,b=1)^3 c_a c_b L_a R_b det M[delete a, delete b],
M_ab = 2 K1(T_(2a)+U_(2b)),  a,b=1,...,4.
```

Because `c_a c_b=(-1)^(a+b)`, this is a truncated adjugate bilinear form.
The coefficient of the singular left old-position-six kernel is the
determinant obtained by replacing row six of `M` with
`[R_2,R_4,R_6,0]`.

At `T_6=T_8=0`, the full row
`[K(U_2),K(U_4),K(U_6),K(U_8)]` equals row eight. Its determinant is zero.
The actual contraction omits position eight, so subtracting that final
component leaves

```text
K(U_8) det M[rows (2,4,8), columns (2,4,6)].
```

Both factors are strictly positive: `K1` is positive, and K280's Andreief
theorem makes the canonical size-three Bessel minor strictly positive. An
independent exact rational Cauchy control evaluates the same identity as
`1/6237=(2/U_8)*(1/12474)`.

## Consequence

The ordered coherent sum does not cancel K297's terminal coefficient. Each of
the four groups retains the degree-`-2` fourth derivative in a two-variable
corner, so the complete four-group fourth shape derivative is not locally
absolutely integrable. The integrand itself remains locally integrable. This
is a derivative-method obstruction, not divergence of the action-column
integrand or its integral.

The global fourth-order Jacobi route is therefore closed. The next route must
either use a positive cubature remainder requiring at most third shape
derivatives or subtract and integrate the explicit terminal singular model
before bounding a smooth remainder. Only after that angular repair may the
K294 radial gamma strata be composed.
