---
title: "K1286--K1290 algebraic radial orientation selector"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1286--K1290 algebraic radial orientation selector

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact classifies
> a repository-built algebraic selector on the regular positive-`I2` split-`D7`
> invariant horn. It does not derive a released source action, physical
> orientation, boundary condition or functional state space. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` for composition with the SC-ACT-06
owner question and `INTERNAL_STRUCTURAL_ONLY` for the finite invariant theory.

```gu-typed-objects
result: algebraic weight-21 radial coefficient, exact scale-uniform orientation threshold, branch regularity boundary, proper rank-seven horn selector and integrated admission
carrier: regular positive-I2 split-D7 invariant quotient horn with r=sqrt(I2)>0 LAYER=source-print CHIRALITY=N/A
pairing: weighted scalar potential on radial/shape coordinates ON=regular_positive_I2_invariant_horn
real_structure: real invariant coordinates with outer deck reflection p to minus p
grading: r has weight 1, p has weight 7 and lambda r^21 p has weight 28
action_owner: repository-construction -- no released source coefficient, shape law or physical orientation is supplied
target: K1273 scale-covariant odd response and K1285 source/functional admission MAP-TYPE=evaluation
```

## K1286: the algebraic positive-radius branch is the sharp escape

K1251 already supplies the canonical positive radial coordinate

```text
r = sqrt(I2) > 0
```

on the regular `I2>0` horn. Therefore

```text
epsilon_lambda = lambda r^21 = lambda I2^(21/2)
```

has invariant weight 21 and is even under `p -> -p`. The selector term
`lambda r^21 p` has weight 28 and is odd under the outer reflection. This is
exactly the parity behavior K1273 needs.

There is no contradiction with K1281--K1283. The coefficient is not a
polynomial in the invariant generators, not a convergent analytic germ at
`I2=0`, and not rational in those generators. It is real analytic only on the
open positive horn. Choosing positive radius does not choose a `p` sheet: both
orientation signs remain present at every `r>0`.

More generally, every weight-21 homogeneous coefficient on this chart has the
form

```text
epsilon = r^21 h(y4,y6,y7,y8,y10,y12).
```

It is outer-even exactly when `h` is even in `y7`; then `epsilon p` is
weight 28 and outer-odd. The constant choice `h=lambda` is only the minimal
example. The algebraic escape is therefore an infinite family until an
action, boundary or Green law fixes the shape function; it is not canonical.

## K1287: the threshold becomes scale independent

For the K1273 fiber scale `a=|c7|r^7`, the algebraic response gives

```text
eta = epsilon/a^3 = lambda/|c7|^3.
```

The normalized strength is independent of `r`. Thus the opposite metastable
basin disappears for

```text
|lambda| >= 4 |c7|^3/(3 sqrt(3)),
```

while exactly one nondegenerate critical point requires a strict inequality.
At equality the second stationary point is an inflection. The unique global
sign is opposite the sign of `lambda`. This solves the conditional finite
scale-uniformity problem, but neither `lambda` nor `c7` is source-derived.

## K1288: the price is finite boundary regularity

As a function of the quotient coordinate `I2`, `I2^(21/2)` extends to
`I2=0` as `C10` but not `C11`; its eleventh derivative is proportional to
`I2^(-1/2)`. The actual Cartan lift has extra vanishing from the degree-seven
polynomial `p7(x)`:

```text
||x||^21 p7(x).
```

It is homogeneous of ordinary degree 28 and extends `C27` at the Cartan
origin, but a generic ray with `p7(v) != 0` restricts it to a nonzero multiple
of `s^7 |s|^21`, which is not `C28`. Quotient-coordinate and Cartan-lift
regularity therefore cannot be silently identified. A finite Hessian is
available, but an analytic global action germ is not.

## K1289: a proper rank-seven selector exists on the open horn

Let `s=r/r0`, let the five even shapes be `y_d=I_d/r^d`, and define

```text
f(y)=1/2(y^2-c^2)^2+lambda y,
B(s)=1/2(s-s^(-1))^2.
```

Under the strict K1287 threshold, `f` has one critical point `y_star`, it is a
nondegenerate global minimum, and `f''(y_star)>0`. Then

```text
U = B(s)
    + 1/2 sum_{d=4,6,8,10,12} (y_d-c_d)^2
    + r^28 (f(y7)-f(y_star))
```

is nonnegative and proper on `(0,infinity) x R^6`. It has one global minimum
at `r=r0`, the five stated even shapes and `y7=y_star`. The Hessian is positive
rank seven with determinant

```text
4 r0^26 f''(y_star) > 0.
```

The orientation sector expands to

```text
1/2(p^2-c^2 r^14)^2 + lambda r^21 p - f(y_star) r^28.
```

The radial barrier repairs K1254's open-horn properness escape, but does so by
using inverse radius and therefore does not extend through `I2=0`. The
construction imports one scale, five even shapes, the orientation magnitude
and `lambda`; it does not reduce the source-data debt or classify the realized
orbit image globally.

## K1290: admission boundary

The integrated certificate contains fifteen satisfied, six excluded, five
conditional and six missing rows. The algebraic branch reopens the finite
orientation-selector class and proves K1283 sharp. It does not reopen the
polynomial, analytic-germ or regular-rational classes.

K1145 and K1150 remain `0/7`. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`, and no source,
ledger, canon, paper, public posture, prediction, confirmation or protected
verdict moves.

## Verification and next exact input

The five producers pass `63/63` declared controls and the five probes reject
`42/42` hostile mutations. The next exact input is a released source action,
boundary or Green law that owns the algebraic radial term, `lambda`, the scale
and all six shapes on the realized orbit image, together with the common
K1145/K1150 domain, range/gap, causal generator and positive-cohomology packet.
