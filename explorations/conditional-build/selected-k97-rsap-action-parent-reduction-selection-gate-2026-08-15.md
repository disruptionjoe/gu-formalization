---
title: "Selected-K97 RSAP action-parent reduction and selection gate"
status: active_research
doc_type: exact_formal_attachment_and_current_action_nonselection_result
created: "2026-08-15"
registry: lab/process/selected-k97-rsap-action-parent-reduction-selection-gate.json
probe: tests/channel-swings/selected_k97_rsap_action_parent_reduction_selection_gate_probe.py
grade: "GLOBAL FORMAL ATTACHMENT TO ACTION-OWNED PREBOUNDARY PARENT CONSTRUCTED; CURRENT BARE ACTION DOES NOT SELECT THE REDUCTION"
canon_verdict_change: none
---

# Selected-K97 RSAP action-parent reduction and selection gate

## Result first

K96's `98D` RSAP is not an unrelated mathematical phase space. It has a
canonical global attachment to the formal preboundary carrier already owned
by the selected action:

```text
T*(Spin_0(7,7)/H_bal)
  = J_R,H_bal^(-1)(0) / H_bal
  inside the action-owned formal parent T*Spin_0(7,7).
```

The attachment is the standard cotangent reduction, and here it is exact.
In left trivialization write the source-epsilon preboundary parent as

```text
T*G = G x g*,
Theta_epsilon = <lambda,g^(-1) delta g>.
```

The right `H_bal` moment map is restriction of `lambda` to `h_bal` (up to an
irrelevant overall sign convention). Its zero set is

```text
lambda in h_bal^perp = p_0.
```

Quotienting by the cotangent-lifted right action gives

```text
(G x p_0)/H_bal = G x_(H_bal) p_0 = T*(G/H_bal),
dim = 182 - 2*42 = 98,
J_left([g,X]) = Ad_g X.
```

This is exactly the balanced carrier and moment map proved globally
surjective in K96. Thus the previously open *formal global attachment* is
closed.

The source/action **selection** question does not close positively. The
current bare boundary action has only these already certified dispositions:

1. free epsilon variation forces the full endpoint covector `lambda=0`, not
   the complete `49D` condition `lambda in p_0`;
2. fixed epsilon data leaves `lambda` unrestricted and makes transformations
   that move the boundary datum physical boundary symmetries, not right-
   `H_bal` gauge directions; and
3. a generated/mixed boundary graph or BFV constraint could impose the
   required coisotropic law, but no such boundary functional, constraint
   owner or gauge generator is present in the inspected source/action record.

Therefore the honest result is:

```text
global formal attachment to action-owned T*G parent: CONSTRUCTED
selection of J_R,H_bal=0 by the current bare action: OBSTRUCTED
right-H_bal gauge quotient owned by the current action: NOT CONSTRUCTED
physical GU phase-space attachment: OPEN
```

## Why this is stronger than source silence

`H_bal` was reverse-constructed from two mathematical requirements: a
`42D` stabilizer is forced by the sharp `98D` target, and the balanced
`(3,4)|(4,3)` involution makes the resulting moment map globally surjective.
Those requirements explain why the subgroup works. They do not make it an
Euler--Lagrange consequence.

K97 does not stop at finding no printed `H_bal`. It composes four owned facts:

- the selected epsilon variation gives the canonical potential on formal
  `T*G`;
- the balanced Lie algebra has `h_bal^perp=p_0`;
- cotangent reduction at the right-`H_bal` zero level produces the exact K96
  carrier globally; and
- the complete current bare-boundary classification contains no horn that
  imposes that level while also quotienting its right action.

So the missing item is no longer vaguely “an attachment.” It is one typed
dynamical law: an action-owned right-`H_bal` coisotropic constraint and gauge
identification.

## Exact reduction certificate

At the zero covector, the tangent to the right-moment zero set is

```text
g plus p_0.
```

The `42D` characteristic subspace is the right `h_bal` orbit. After quotient,
the tangent is

```text
(g/h_bal) plus p_0 = p_0 plus p_0.
```

The reduced two-form is the canonical off-diagonal trace-pairing matrix. The
trace form is nondegenerate on `p_0`, so this matrix has exact rank `98`.
Globally the right action sends

```text
(g,X) -> (g h, Ad_(h^-1) X),
```

and the left moment map descends because

```text
Ad_(g h)(Ad_(h^-1) X) = Ad_g X.
```

There is no local-section or orbit-type seam in this attachment. The open seam
is entirely variational and gauge-theoretic.

## Source and ownership typing

The source owns the epsilon field and the two-connection variation grammar.
The repository derives the formal `T*G` identification from the exact
preboundary potential, and derives the balanced reduction and global RSAP.
The inspected record does not own the right-`H_bal` constraint, a boundary
functional generating it, a right-`H_bal` BFV charge, or the declaration that
these boundary transformations are gauge.

This is repository- and current-action-scoped. A future completed action,
boundary term, edge system or BV/BFV construction can reopen selection. It
must construct the missing law rather than infer it from the success of the
reverse-built geometry.

## Claim ceiling and next gate

K97 does not promote the `98D` RSAP to a physical GU phase space. No analytic
domain, BFV master equation, positivity, polarization, quantization, state
space, particle spectrum, datum, ledger verdict, canon claim or public posture
follows.

The next gate is now narrow:

```text
DERIVE_OR_OBSTRUCT_AN_ACTION_OWNED_BOUNDARY_OR_BFV_LAW_WHOSE_CONSTRAINT_IS
J_R,H_bal=0_AND_WHOSE_CHARACTERISTIC_ORBITS_ARE_EXACTLY_RIGHT_H_bal;
CHECK_COMPATIBILITY_WITH_THE_SELECTED_EPSILON_VARIATION_AND_ALL_BOUNDARY_HORNS;
DO_NOT_REINFER_SELECTION_FROM_DIMENSION_OR_GLOBAL_SURJECTIVITY.
```

Reproduce with:

```bash
python3 tests/channel-swings/selected_k97_rsap_action_parent_reduction_selection_gate_probe.py
```
