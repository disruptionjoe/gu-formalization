---
title: "K1266--K1270 split-D7 orbit sign boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1266--K1270 split-D7 orbit sign boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact uses the
> source-owned connected `Spin(7,7)` gauge datum and standard split-`D7`
> Cartan/Weyl theory to classify the sign pair left by K1264. The full
> disconnected `O(7,7)` parity is a mathematical comparison, not a
> source-owned physical gauge identification. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the connected-group ownership
boundary and `INTERNAL_STRUCTURAL_ONLY` for the Cartan, Weyl and invariant-ring
theorems.

Scope: regular semisimple elements in one maximally split Cartan of
`so(7,7)`, their connected inner conjugacy classes, and the larger
all-signed normalizer available after adjoining a disconnected orthogonal
reflection. This is not a classification of singular or non-semisimple
orbits, a proof that a source action depends on the degree-seven invariant, or
a functional BV-BFV construction.

```gu-typed-objects
result: explicit realized opposite-sign regular pair, connected D7 orbit separation, disconnected parity exchange and exact D7/B7 invariant-ring boundary
carrier: maximally split Cartan h in so(7,7) with coordinates x1 through x7 LAYER=source-print CHIRALITY=N/A
pairing: split orthogonal form J on R7,7 and polynomial invariant pairing ON=Cartan_coordinate_ring
real_structure: real split Cartan with H(x)=diag(x1,...,x7,-x1,...,-x7)
grading: primitive D7 degrees 2,4,6,7,8,10,12; outer-quotient replacement degree 14 equals degree-seven-square
action_owner: source-print owns connected Spin(7,7); repository theorem owns the orbit calculation; disconnected O(7,7) parity and every selector remain unowned
target: K1264 realized-orbit sign identification alternative plus K1145/K1150 admission MAP-TYPE=quotient
```

## K1266: both signs are realized regularly

In an isotropic basis, write a split Cartan element as

```text
H(x)=diag(x1,...,x7,-x1,...,-x7).
```

The `D7` roots are `plus_or_minus e_i plus_or_minus e_j`; hence `H(x)` is
regular exactly when `x_i plus_or_minus x_j` is nonzero for every `i != j`.
Take

```text
x+=(1,2,3,4,5,6,7),   x-=(-1,2,3,4,5,6,7).
```

Both are regular. Their six even primitive invariants, represented by the
elementary symmetric functions `e_k(x_1^2,...,x_7^2)` for `k=1,...,6`, agree.
The degree-seven Pfaffian coordinate `p=x1*...*x7` equals `+5040` and `-5040`.
Thus K1264's opposite-sign pair is not merely an ambient formal-base artifact:
both signs occur on the realized regular split Cartan.

## K1267: connected Spin does not identify the pair

The connected split `D7` Weyl group is

```text
W(D7)=S7 semidirect {sign vectors with an even number of minus signs}.
```

Permutations leave the coordinate product unchanged and every admitted sign
vector has product `+1`. Therefore `p` is constant on every `W(D7)` orbit.
Since `p(x+)=-p(x-)`, the pair is not Weyl-conjugate. Regular semisimple
conjugacy in the connected split group reduces to Weyl conjugacy on the split
Cartan, so the two elements are not identified by connected inner
`Spin(7,7)` gauge symmetry.

This conclusion is strictly narrower than saying the two configurations are
physically distinct states. A physical quotient could still gauge an outer
symmetry, impose a boundary identification, or exclude one component, but
none of those effects follows from connected `Spin(7,7)` alone.

## K1268: one disconnected reflection exchanges them

Let the split form in an isotropic basis be

```text
J = [[0,I7],[I7,0]].
```

The permutation matrix `S1` swapping the first isotropic basis pair preserves
`J`, has determinant `-1`, and conjugates

```text
H(x1,x2,...,x7) -> H(-x1,x2,...,x7).
```

It therefore exchanges `x+` and `x-`, but it lies in a disconnected component
of `O(7,7)` rather than in the identity component covered by `Spin(7,7)`.
This exactly matches the older split-shiab warning: importing `O(7,7)` parity
can relate the two chiral channels, but that parity is not part of the
source-owned connected datum. Mathematical exchange is not physical gauging.

## K1269: the quotient change is exactly p to p squared

Chevalley restriction gives

```text
R[h]^{W(D7)} = R[e1(x^2),...,e6(x^2),p],
degrees             = 2,4,6,8,10,12,7.
```

After adjoining an odd sign flip, the normalizer becomes the all-signed
hyperoctahedral group `W(B7)`. Its invariant ring is

```text
R[h]^{W(B7)} = R[e1(x^2),...,e6(x^2),e7(x^2)]
             = R[e1,...,e6,p^2],
degrees        2,4,6,8,10,12,14.
```

So K1264's even subring is not arbitrary: it is precisely the quotient ring
obtained after forgetting the connected-orbit orientation through the outer
sign involution. On the connected source group, `p` is a genuine invariant;
on the disconnected extension, only `p^2` remains.

## K1270: admission boundary

The realized-orbit ambiguity is now resolved in the adverse direction for
automatic identification. Both signs occur regularly, and connected
`Spin(7,7)` does not identify them. The larger `O(7,7)` comparison does, but
only by adjoining a disconnected parity not owned by the source action or
physical quotient.

The exact effect is

`OPPOSITE_I7_SIGNS_ARE_REALIZED_DISTINCT_CONNECTED_SPLIT_D7_ORBITS__ONLY_DISCONNECTED_OUTER_PARITY_IDENTIFIES_THEM__SOURCE_AND_FUNCTIONAL_OWNERSHIP_UNCHANGED`.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`. K1145 and K1150 remain `0/7`.
The next finite action-side input is therefore sharper: either the source
action/boundary law must contain an odd-in-`p` response, or the physical
theory must explicitly gauge the disconnected parity or exclude one regular
component. Independently, a source-derived six-shape response and the complete
common-domain, closed-range, positive-gap, causal-generator and positive
nonzero-cohomology packet remain missing.
