---
title: "K1251--K1255 two-weight source-epsilon selector boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1251--K1255 two-weight source-epsilon selector boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact uses the
> action-owned finite source-epsilon cotangent parent and constructs a
> repository-owned potential on one regular quotient horn. It does not derive
> a source boundary law, functional deformation complex or physical boundary
> condition. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the quotient carrier and
`INTERNAL_STRUCTURAL_ONLY` for the two-weight selector.

Scope: exact finite selection on the regular `I2>0` split-`D7` quotient horn.
No result is claimed for the `I2<=0` horns, a global split-real orbit space,
an extension through `I2=0`, or the functional BV-BFV theory.

```gu-typed-objects
result: exact radial/shape chart, two-weight full-rank selector, seven-datum inventory and finite-versus-functional properness boundary
carrier: regular source-epsilon coadjoint quotient horn I2>0 with one radial and six shape coordinates LAYER=source-print CHIRALITY=N/A
pairing: ordinary finite Hessian on quotient coordinates ON=finite_regular_quotient
real_structure: real split-D7 invariant base restricted to I2>0
grading: weighted degrees 2,4,6,7,8,10,12; selector components of degrees four and two
action_owner: repository-construction owns the selector potential, scale and shape values; source-action owns the cotangent parent
target: K949 regular seven-lock plus K1145/K1150 functional admission MAP-TYPE=evaluation
```

## Exact construction

K1251 uses the positive quadratic invariant as radial coordinate,

```text
r=sqrt(I2)>0,              y_d=I_d/r^d,
I2=r^2,                    I_d=r^d y_d.
```

The Jacobian determinant is `2 r^48`, so this is a genuine seven-dimensional
chart on the stated horn. Charge dilation changes `r` and leaves the six
`y_d` invariant. The chart itself selects no value.

Let `r0>0`, let `c=(c4,c6,c7,c8,c10,c12)`, put `s=r/r0`, and define

```text
Q(y)=1/2 sum_d (y_d-c_d)^2,
V4=s^4(2+Q),
V2=s^2(-4+Q),
V=V4+V2.
```

`V4` and `V2` have distinct weighted degrees four and two. At `s=1,y=c`,
the gradient vanishes and the Hessian in `(r,y)` coordinates is

```text
diag(16/r0^2,2,2,2,2,2,2).
```

Its rank is seven, inertia is `(7,0,0)`, and determinant is `1024/r0^2`.
Because the chart Jacobian is invertible and the gradient vanishes at the
selected point, Hessians in the chart and original invariant coordinates are
related by congruence there; rank and inertia therefore carry back to the
`I_d` coordinates.
Thus two weighted components are already sufficient to evade K1247's
single-weight radial-null theorem. The obstruction is sharp; it is not a
no-go for multi-weight laws.

The stronger exact identity

```text
V+2=2(s^2-1)^2+(s^4+s^2)Q
```

shows that the selected point is the unique minimum inside the finite open
horn chart. This still does not make `V` a source law. The coefficients carry
exactly the target orbit data:

```text
I2*=r0^2,                  I_d*=r0^d c_d.
```

Conversely, every target in this horn returns `r0=sqrt(I2*)` and
`c_d=I_d*/r0^d`. The construction therefore relocates one scale and six shape
values into the potential; it does not derive or eliminate them. Even a
favorable grant that the displayed scalar `kappa_1` fixes the scale would
leave all six shape ratios without a source-owned coupling.

## Properness and admission boundary

The finite result is stronger than local Hessian rank but weaker than the
needed global and functional result. At fixed positive radius the potential
is coercive in shape, and at fixed shape it is coercive as `s` tends to
infinity. On the open horn, however, `s_n=1/n,y=c` gives
`V_n=2/n^4-4/n^2 -> 0`; the sublevel `V<=1` is not compact in the chart.
No extension through `I2=0` has been constructed.

More importantly, no finite quotient potential defines the field-space
complex, common graph domain, closed range, positive quotient gap, causal
Green operators or maximal generator, trace preservation, or positive
nonzero cohomology required by K1145/K1150. K1255 therefore records three
finite rows satisfied, one single-weight row excluded, and six ownership or
functional rows missing. Both K1145 and K1150 remain `0/7`.

## Boundary and next condition

The exact effect is
`TWO_WEIGHT_FINITE_SELECTOR_EXISTS_BUT_IMPORTS_SEVEN_UNOWNED_ORBIT_DATA_WITHOUT_FUNCTIONAL_ADMISSION`.
SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`. Charged boundary symmetry remains the
honest default until an action-derived boundary or Green law fixes the scale
and all six shapes and then passes the common functional-domain packet.
