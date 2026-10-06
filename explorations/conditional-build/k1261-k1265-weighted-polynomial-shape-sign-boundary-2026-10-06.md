---
title: "K1261--K1265 weighted-polynomial shape/sign boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1261--K1265 weighted-polynomial shape/sign boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact keeps the
> source torsion field, its displayed quadratic `kappa_1` term, the finite
> source-epsilon charge, and the regular invariant quotient distinct. It
> constructs polynomial response laws on the ambient formal invariant base;
> the source does not supply those laws. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the action-owner obligation and
`INTERNAL_STRUCTURAL_ONLY` for the polynomial construction and parity theorem.

Scope: finite real controls and polynomial laws on the ambient formal
seven-coordinate base. The result does not classify the realized split-real
orbit image or construct a functional BV-BFV domain.

```gu-typed-objects
result: parameter/field/quotient rank separation, six weighted-polynomial shape responses, proper rank-seven paired-minimum completion and odd-invariant parity obstruction
carrier: source-print torsion-field control plus ambient formal split-D7 invariant base R7 LAYER=source-print CHIRALITY=N/A
pairing: nondegenerate finite field pairing and Euclidean residual-square Hessian ON=formal_invariant_residuals
real_structure: real invariant coordinates on the positive-I2 regular horn
grading: primitive degrees 2,4,6,7,8,10,12 with the odd magnitude residual at weight 14
action_owner: source-print owns the displayed kappa_1 torsion term; repository-construction owns every quotient residual and selector built here
target: K949 regular continuous lock plus odd-I7 sign selection and K1145/K1150 admission MAP-TYPE=evaluation
```

## One scalar coefficient is not one field-Hessian rank

For a nondegenerate finite pairing `G`, the field law

```text
V_kappa(T) = kappa/2 <T,T>_G
```

has Hessian `kappa G`, hence full field rank whenever `kappa` is nonzero. Its
only critical point is `T=0`. By contrast, the favorable affine quotient
surrogate `v_kappa(I)=kappa I2/2` has constant nonzero quotient gradient and
zero quotient Hessian, hence no critical point on the regular nonzero horn.

There is no contradiction. Parameter dimension, field-Hessian rank and the
rank of a quotient response map are different quantities. K1256 constrains
the last quantity at a critical quotient law; it never says that one scalar
coefficient forces a rank-one field Hessian. Conversely, full field rank at
`T=0` does not select a nonzero quotient shape. Any nonzero regular stationary
point must obtain its shape response from companion action or boundary terms.

## Six continuous polynomial shape responses

Write `x=I2`. For the five even primitive degrees set

```text
R_d = I_d - c_d x^(d/2),  d in {4,6,8,10,12},
```

and polynomialize the odd degree-seven magnitude as

```text
R_7 = I7^2 - c7^2 x^7.
```

At a regular target `x=r0^2>0`, `I_d=c_d r0^d`, with `c7` nonzero, the six
residuals have Jacobian rank six. Their squared law has Hessian rank six and
one-dimensional kernel spanned by the weighted radial tangent

```text
(2 I2,4 I4,6 I6,7 I7,8 I8,10 I10,12 I12).
```

Thus the missing continuous shape rank is mathematically constructible by
weighted polynomial channels. The coefficients `c_d` and the laws themselves
remain imported repository data, not source responses.

## Proper rank seven still leaves a discrete sign

Add the scale residual `R_2=I2-r0^2` and define

```text
U = 1/2 (R_2^2+R_4^2+R_6^2+R_7^2+R_8^2+R_10^2+R_12^2).
```

This polynomial is globally proper on the ambient formal `R7`: a sublevel
first bounds `I2`, then every even `I_d`, then `I7^2`. It has exactly two
global minima,

```text
I2=r0^2,  I_d=c_d r0^d (d even),  I7=plus_or_minus c7 r0^7.
```

At either minimum the residual Jacobian determinant is
`plus_or_minus 2 c7 r0^7`. The Hessian is positive definite with rank seven,
inertia `(7,0,0)`, and determinant `4 c7^2 r0^14`.

The remaining pair is structural for the stated law class. Every polynomial
in

```text
R[I2,I4,I6,I8,I10,I12,I7^2]
```

is invariant under `I7 -> -I7`. Its nonzero critical points occur in equal
value pairs, and their Hessians are congruent, so a unique nonzero sign cannot
be selected inside that even subring. Selection requires an odd-in-`I7`
response or an independently owned physical identification of the pair. This
is a precise algebraic boundary, not a claim that the source action is even in
`I7` or that both formal points are realized physical orbits.

## Admission boundary

K1265 records four satisfied finite rows, two excluded routes, one conditional
scale row and seven missing source, orbit-image or functional rows. K1145 and
K1150 remain `0/7`. The exact effect is

`SIX_CONTINUOUS_SHAPE_RESPONSES_AND_PROPER_RANK_SEVEN_LOCK_CONSTRUCTIBLE_BUT_EVEN_ODD_INVARIANT_LAW_LEAVES_Z2_SIGN__SOURCE_AND_FUNCTIONAL_OWNERSHIP_UNCHANGED`.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`. Charged boundary symmetry remains the
honest default. The next useful input is an action-derived six-shape response
law plus an odd-in-`I7` response or a proved identification of the sign pair
on the realized orbit space, followed by the common closed functional domain,
closed range, positive gap, causal Green/maximal-generator data and positive
nonzero cohomology.
