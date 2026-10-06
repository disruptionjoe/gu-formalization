---
title: "K1271--K1275 odd-response uniform selection boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1271--K1275 odd-response uniform selection boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact uses the
> source-owned connected `Spin(7,7)` datum and K1266--K1270's split-`D7`
> orbit theorem to classify a repository-constructed odd response. The
> coefficient is not derived from a source action, boundary law or Green
> operator. The disconnected `O(7,7)` parity remains an unowned mathematical
> comparison. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the connected-versus-outer symmetry
boundary and `INTERNAL_STRUCTURAL_ONLY` for the quartic bifurcation, Morse and
scaling theorems.

Scope: the one-dimensional degree-seven invariant fiber at fixed even
split-`D7` invariants, followed by its exact invariant-weight scaling. This is
not a derivation of a source response, a physical parity-breaking mechanism,
or a common-domain BV-BFV theorem.

```gu-typed-objects
result: exact odd-tilt bifurcation, global versus metastable sign selection, weight-21 uniform-response law and connected/outer symmetry fork
carrier: degree-seven invariant fiber p over fixed six-even-invariant regular split-D7 quotient data LAYER=source-print CHIRALITY=N/A
pairing: ordinary real polynomial potential and Hessian ON=p_fiber
real_structure: real p, a>0 and real response epsilon
grading: p has weight 7; (p^2-a^2)^2 has weight 28; epsilon must have weight 21 in a weighted law
action_owner: repository-construction -- source action, epsilon, outer gauging and one-component restriction remain unowned
target: K1270 odd-response requirement and sign-selection stability MAP-TYPE=evaluation
```

## K1271: exact odd-tilt bifurcation

At fixed even invariants, write the sign-paired K1263 fiber as

```text
F(p)=1/2 (p^2-a^2)^2+epsilon p,    a>0.
```

Its critical equation and monic discriminant are

```text
F'(p)=2p^3-2a^2p+epsilon=0,
Delta=4a^6-27epsilon^2/4.
```

Therefore the exact critical response is

```text
epsilon_c = 4a^3/(3sqrt(3)).
```

For `0<|epsilon|<epsilon_c` there are three distinct critical points; at
equality there are two distinct points with one double root of the critical
equation; above it there is one critical point. The identity

```text
F(-p)-F(p)=-2epsilon p
```

shows more than critical-point counting: every nonzero tilt gives a unique
global minimum whose sign is opposite the sign of `epsilon`.

## K1272: global selection is weaker than single-basin stability

The fiber Hessian is `F''(p)=6p^2-2a^2`. In the subcritical regime the two
outer critical points are strict local minima and the middle point is a strict
maximum. The opposite-`epsilon` minimum is global, while the same-`epsilon`
minimum remains metastable. Thus an arbitrarily small odd response selects a
global sign but does not remove the competing basin.

At `|epsilon|=epsilon_c`, the same-`epsilon` point
`p=sign(epsilon)a/sqrt(3)` has `F''=0` and `F'''!=0`, so it is a stationary
inflection, not a minimum. The other point
`p=-2sign(epsilon)a/sqrt(3)` is the unique global minimum with Hessian
`6a^2`. Strictly above threshold the landscape has exactly one critical
point, a strict global minimum. Hence three requirements differ:

1. unique global sign: `epsilon!=0`;
2. no metastable opposite-sign minimum: `|epsilon|>=epsilon_c`;
3. exactly one critical point with no threshold degeneracy:
   `|epsilon|>epsilon_c`.

## K1273: uniform selection requires a weight-21 response

Set `p=aq` and `eta=epsilon/a^3`. Then

```text
F(aq)/a^4 = 1/2(q^2-1)^2 + eta q,
eta_c = 4/(3sqrt(3)).
```

A fixed nonzero `epsilon` is not uniformly single-basin over unbounded fiber
scale: `eta=epsilon/a^3` tends to zero and eventually returns to the
two-minimum regime. The scale-covariant family

```text
epsilon(a)=lambda a^3
```

has one normalized landscape at every scale, and exactly one critical point
when `|lambda|>4/(3sqrt(3))`.

This scaling is also forced by the invariant weights of the conditional
polynomial. The sign fiber has `p` of weight seven and the squared even
residual has weight twenty-eight, so the coefficient of `epsilon p` must have
weight twenty-one. With `a=|c7|r0^7`, the threshold scales as

```text
epsilon_c = 4|c7|^3 r0^21/(3sqrt(3)).
```

This is a requirement on a possible owner, not evidence that the source
supplies such a response.

## K1274: connected and outer symmetry give opposite admissibility rules

The connected `D7` Weyl group preserves `p`, so a scalar term `epsilon p` is
mathematically invariant under the source-owned connected group. Connected
symmetry therefore does not forbid the odd response, but it also does not
derive its coefficient.

The disconnected outer involution sends `p` to `-p`. If that parity is gauged
and `epsilon` is an invariant scalar, the odd term is forbidden. A spurion
assignment `epsilon -> -epsilon` restores covariance, but choosing a nonzero
spurion adds exactly the orientation-breaking datum that needs ownership. A
one-component physical restriction could select a sign without a potential,
but K1266--K1270 found no source-owned restriction.

## K1275: admission boundary

The finite response question is now exact. Nonzero odd dependence is enough
to choose one global sign in the canonical quartic fiber, but an infinitesimal
term is not enough to erase the competing local basin. A uniform,
nondegenerate, one-critical-point law across scales requires a coefficient of
weight twenty-one whose normalized magnitude is strictly above
`4/(3sqrt(3))`. Such a term is allowed by connected `D7` and forbidden by a
gauged outer parity unless an additional transforming datum is supplied.

None of those alternatives is source-owned. The six continuous shape
responses also remain repository constructions, and K1145/K1150 remain
`0/7`. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`;
LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`.

The exact effect is

`ANY_NONZERO_ODD_TILT_SELECTS_ONE_GLOBAL_SIGN_BUT_UNIFORM_NONDEGENERATE_SINGLE_CRITICAL_POINT_SELECTION_REQUIRES_A_SCALE_COVARIANT_WEIGHT_21_RESPONSE_ABOVE_THE_EXACT_THRESHOLD__SOURCE_AND_FUNCTIONAL_OWNERSHIP_UNCHANGED`.

The next real input is a source action, boundary law or Green response that
supplies the six shape channels and an odd-in-`p` coefficient with its scale
and stability regime, or an explicitly owned outer quotient or one-component
restriction. It must still compose with one common closed BV-BFV domain,
closed range, positive quotient gap, causal Green/maximal-generator data and
positive nonzero cohomology.
