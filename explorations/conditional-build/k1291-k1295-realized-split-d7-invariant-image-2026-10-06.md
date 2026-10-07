---
title: "K1291--K1295 realized split-D7 invariant image"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1291--K1295 realized split-D7 invariant image

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact classifies
> the finite split-Cartan invariant image used by the repository's conditional
> selector constructions. It does not identify that quotient with a physical
> phase space, derive a released source action or choose a physical
> orientation. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the SC-ACT-06 ownership question and
`INTERNAL_STRUCTURAL_ONLY` for the real invariant, Jacobian and selector-transfer
theorems.

Scope: the real maximally split Cartan of `so(7,7)`, its connected `D7` Weyl
quotient, the normalized `I2>0` shape image and repository-constructed finite
selectors. This is not a classification of non-semisimple Lie-algebra orbits,
a functional field space, a BV-BFV complex or a physical state space.

```gu-typed-objects
result: complete realized invariant image, compact normalized shape image, regular quotient Jacobian, feasible-target selector transfer and integrated admission
carrier: maximally split Cartan h=R7 with coordinates x1 through x7 LAYER=source-print CHIRALITY=N/A
pairing: ordinary real polynomial coordinate pairing and positive target-residual square ON=finite_Cartan
real_structure: real x_i with z_i=x_i^2 nonnegative and signed p=product_i x_i
grading: primitive D7 degrees 2,4,6,7,8,10,12
action_owner: repository-construction -- invariant theorem and selector only; no released source law selects the target data
target: K1259/K1289 realized-orbit transfer and K1290 admission MAP-TYPE=quotient
```

## K1291: the complete real invariant image is a root region

Put `z_i=x_i^2` and use the primitive connected-`D7` invariants

```text
F(x)=(e1(z),e2(z),e3(z),e4(z),e5(z),e6(z),p),
p=x1*...*x7.
```

The missing seventh elementary symmetric function is not free:

```text
e7(z)=z1*...*z7=p^2.
```

Consequently an invariant tuple
`(I2,I4,I6,I8,I10,I12,I7)` is realized by a real split-Cartan
point exactly when

```text
P(t)=t^7-I2*t^6+I4*t^5-I6*t^4+I8*t^3-I10*t^2+I12*t-I7^2
```

has seven nonnegative real roots, counted with multiplicity. Necessity is
Vieta's formula. For sufficiency, take the nonnegative roots `z_i`, choose
`x_i=sqrt(z_i)`, and, when `I7` is nonzero, flip one sign if necessary to make
the coordinate product equal `I7`.

The tuple also separates connected `W(D7)` orbits. Equal even invariants give
the same unordered squared coordinates. For nonzero product, equal `p` means
the relative sign vector has even parity. When a coordinate is zero, any
otherwise odd relative sign change can be completed by flipping the zero
coordinate, which changes no point but restores even parity. Thus the root
criterion is both a complete image theorem and a complete Cartan Weyl-orbit
criterion. The ambient formal invariant base used by K1259 is strictly larger.

## K1292: the realized shape image is compact and the sign is not a component

On `I2>0`, normalize

```text
q_i=x_i^2/I2,  q_i>=0,  sum_i q_i=1.
```

Then the six shapes are

```text
y4=e2(q), y6=e3(q), y8=e4(q), y10=e5(q), y12=e6(q),
y7=p/I2^(7/2), with y7^2=e7(q)=product_i q_i.
```

Hence the realized shape image is the permutation quotient of a compact
six-simplex, with the allowed signed square root attached. It is not all of
`R6`. Maclaurin's inequalities give the sharp bounds

```text
0 <= e_k(q) <= binomial(7,k)/7^k,  k=2,...,6,
|y7| <= 7^(-7/2).
```

All upper equalities occur at `q_i=1/7`, a collision point outside the regular
locus.

There is also a topology correction to a tempting reading of K1266--K1270.
The opposite signs at fixed six even invariants are distinct connected-inner
orbits, but the sign of `p` is not a connected-component label of the whole
regular quotient. The path

```text
x(t)=(t,2,3,4,5,6,7),  -1<=t<=1,
```

has pairwise distinct squared coordinates throughout, so it remains
`D7`-regular while `p` crosses zero. This is a path in the mathematical
regular quotient, not a physical history or a gauge identification of its
endpoints.

## K1293: the connected quotient is smooth through p=0

For the connected invariant map `F`, direct differentiation gives

```text
|det dF_x| = 2^6 product_{i<j}|x_i^2-x_j^2|,
(det dF_x)^2 = 2^12 product_{i<j}(x_i^2-x_j^2)^2.
```

This is nonzero exactly when the squared coordinates are pairwise distinct,
which is exactly split-`D7` regular semisimplicity. Therefore `F` is a local
diffeomorphism on every regular chamber and provides ordinary quotient
coordinates there.

One zero coordinate can be regular. At such a point `p=0`, the connected
`D7` Jacobian remains nonzero. The apparent branching belongs instead to the
outer all-signed quotient:

```text
det d(e1,...,e6,p^2) = 2p det d(e1,...,e6,p).
```

Thus the `B7` quotient branches at `p=0`; the connected `D7` quotient does
not. Local finite quotient regularity supplies no Fredholm, Green, causal or
closed-domain result.

## K1294: feasible targets transfer the polynomial selector to Cartan

Let `a=(a_d)` pass K1291's nonnegative-root criterion and K1293's nonzero
discriminant test, and let `r0^2=a2`. Restrict K1259's target-centered law to
the actual Cartan:

```text
V(x)=1/2 sum_d ((I_d(x)-a_d)/r0^d)^2,
d in {2,4,6,7,8,10,12}.
```

The `I2` residual makes `V` proper as `|x|` tends to infinity. Its zero set is
exactly one `W(D7)` orbit. At any point of that orbit the Hessian is

```text
(dF_x)^T diag(r0^(-2d)) dF_x,
```

so it is positive definite of rank seven, with

```text
det Hess V = 2^12 r0^(-98)
             product_{i<j}(x_i^2-x_j^2)^2 > 0.
```

If the formal target fails the root criterion, the restricted law has no zero
there and the formal-base minimum does not transfer. K1289's horn selector has
the same exact qualification: its six target shapes must lie in K1292's
regular image. The realized-orbit gap is therefore closed for explicitly
feasible finite targets, not for arbitrary formal coordinates.

This transfer imports the complete target orbit—one scale and six shapes—and
uses a repository residual square. It does not derive any of those data from
the source. In particular, polynomiality and global finite Cartan properness
do not supply functional BV-BFV properness.

## K1295: admission boundary

The integrated certificate now has nineteen satisfied, six excluded, four
conditional and six missing rows. Realized-image classification is no longer
the finite ambiguity: a proposed target can be tested exactly by the root and
discriminant criteria, and every feasible regular target admits the stated
proper polynomial selector on Cartan.

The remaining question is ownership, not finite realizability. A released
action, boundary or Green law must derive a feasible target, `lambda` and all
six shapes, then supply the common closed domain, closed range, positive
quotient gap, causal Green or maximal generator and positive nonzero
cohomology. K1145 and K1150 remain `0/7`.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`;
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source, physics-ledger, canon,
paper, public-posture, prediction, confirmation or protected verdict moves.

## Verification and exact next input

The five producers pass `74/74` declared controls and the five independent
probes reject `43/43` hostile mutations. The next exact input is a released
source action, boundary or Green law that selects data passing K1291's root
criterion and K1293's discriminant test, derives `lambda` and the six shape
responses, and realizes the complete K1145/K1150 functional packet.
