---
title: "K1246--K1250 source-epsilon scale-selection boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1246--K1250 source-epsilon scale-selection boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact works on
> the action-owned finite source-epsilon cotangent parent and its regular
> coadjoint quotient. It does not construct the source's full functional
> deformation complex or a physical boundary condition. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` for the cotangent parent and
`INTERNAL_STRUCTURAL_ONLY` for the candidate selector laws.

Scope: the theorem binds finite regular invariant selection on the
`so(7,7)*` quotient. It does not classify inhomogeneous, nonlocal or
noncommutative boundary laws, singular zero charge, or the functional
BV-BFV problem.

```gu-typed-objects
result: exact regular-quotient weight census, homogeneous-selector obstruction and gauge-slice no-selection theorem
carrier: regular source-epsilon coadjoint charge locus in so(7,7)* with 84-dimensional orbits and seven-dimensional quotient LAYER=source-print CHIRALITY=N/A
pairing: canonical cotangent symplectic parent; ordinary Hessian only on the seven invariant coordinates ON=finite_regular_quotient
real_structure: split real D7, with primitive invariant degrees inherited from the complex Chevalley algebra
grading: quotient weights 2,4,6,7,8,10,12
action_owner: source-action owns the cotangent parent; the tested boundary potentials, slices and invariant values are not source-owned
target: K949 regular seven-lock plus K1145/K1150 functional admission MAP-TYPE=evaluation
```

## Exact result

K1246 resolves the regular quotient's scale weights. Split `D7` has dimension
`91`, rank `7`, exponents `1,3,5,6,7,9,11` and primitive invariant degrees
`2,4,6,7,8,10,12`. A regular orbit therefore has dimension `84`, while its
quotient retains seven coordinates. Under charge dilation,
`I_d(t mu)=t^d I_d(mu)`.

K1247 applies weighted Euler differentiation to any invariant boundary
potential `V` of one weighted degree `D`:

```text
sum_i w_i I_i partial_i V = D V,
[Hess(V)(W I)]_j = (D-w_j) partial_j V.
```

At a critical point whose invariant tuple is nonzero, the weighted radial
vector `W I` is nonzero and lies in the Hessian kernel. The Hessian rank is
therefore at most six, below K949's rank-seven regular lock. A scale-free
single-weight invariant potential cannot have a nondegenerate regular selected
point with nonzero invariant tuple. This does not exclude the all-zero
invariant tuple, an inhomogeneous or scale-breaking potential, a singular law,
or a nonlocal boundary condition.

K1248 closes a distinct apparent escape. Any local gauge or Kostant-type
representative slice `s` obeys `pi o s=id` on the seven-dimensional quotient.
Its quotient Jacobian has rank seven: it chooses one representative of every
orbit while leaving all seven orbit values free. Canonical gauge fixing is not
physical charge selection.

K1249 composes those results with K949 and K951--K955. The finite regular
escape now has an exact form: a source-owned scale-breaking or multi-weight
boundary law whose quotient derivative has rank seven. A genuinely nonlocal
or noncommutative boundary/Green law remains outside this finite theorem. The
source displays neither class. In particular, this result does not prove that
the displayed `kappa_1` is insufficient; no source-owned coupling from it to
the seven invariant coordinates has been derived either way.

K1250 records one satisfied structural row, three excluded selector routes and
five missing owner/functional rows. K1145 and K1150 remain `0/7`. The honest
effect is
`SCALE_FREE_REGULAR_SELECTOR_AND_GAUGE_SLICE_EXCLUDED_WITHOUT_FUNCTIONAL_ADMISSION`.

## Boundary and next condition

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`. Charged boundary symmetry remains the
honest default at nonzero regular charge. Reopen with a source-owned
scale-breaking or multi-weight boundary law with rank-seven quotient
derivative, or a genuinely nonlocal/noncommutative boundary-Green owner, and
then construct the common closed functional BV-BFV domain, range/gap,
generator/Green packet and positive nonzero cohomology.
