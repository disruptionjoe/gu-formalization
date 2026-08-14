---
title: "VRS-3 second-action ownership discriminator"
status: active_research
doc_type: reverse_superposition_type_theorem
created: "2026-08-14"
lane_id: SRC-RES-COH-01
claim_grade: "EXACT CONDITIONAL HESSIAN TYPE THEOREM; NO BACKGROUND, PHYSICAL COHOMOLOGY, POSITIVITY OR SUPERPOSITION RESULT"
registry: lab/process/superposition-vrs3-second-action-ownership-discriminator.json
probe: tests/channel-swings/superposition_vrs3_second_action_ownership_probe.py
canon_verdict_change: none
---

# VRS-3 second-action ownership discriminator

## Result first

At a conditional residual-zero point, the bulk second variation of

```text
I2(phi) = (1/2) <Upsilon(phi), Q(phi) Upsilon(phi)>
```

reduces to the real symmetric pullback form

```text
H2_bulk(u,v) = <D Upsilon u, Q D Upsilon v>.
```

Away from residual zero, the full Hessian also contains the second derivative
of `Upsilon`, derivatives of `Q`, and their symmetric cross terms. With a
boundary, it additionally contains the second variation of the action-owned
boundary functional and the Green contribution on its admitted domain. Those
terms cannot be discarded by calling the bulk expression a square.

The ownership result is therefore:

```text
real quadratic control / derived differential input: OWNED CONDITIONALLY
complex structure J:                               NOT PRODUCED
symplectic form:                                   NOT PRODUCED
Hermitian pairing:                                 NOT PRODUCED
positive physical inner product:                   NOT PRODUCED
boundary domain and Green closure:                 TYPE-MISSING
```

The exact disposition is

```text
CONDITIONAL_REAL_SYMMETRIC_PULLBACK_OWNED
__COMPLEX_SYMPLECTIC_HERMITIAN_AND_POSITIVE_DATA_REQUIRE_SEPARATE_INPUT
__BOUNDARY_HESSIAN_AND_DOMAIN_REMAIN_REQUIRED.
```

## Layer-0 typing

Let `E` be the real field tangent carrier, `R` the real residual carrier,
`A=D Upsilon:E->R`, and `Q:R->R*` the action-owned symmetric receiver. Then
`A^! Q A:E->E*` is a symmetric covector-valued operator. It is not an
endomorphism `E->E`, and hence cannot even be asked to square to `-1` without
an additional identification. Raising an index with a separately chosen metric
still produces a self-adjoint operator, not a selected complex structure.

A separately owned endomorphism `J:E->E` may be tested against the Hessian:

```text
J^2 = -1,
H2(Ju,Jv) = H2(u,v).
```

Only after those independent conditions hold can one define the conditional
alternating form `omega(u,v)=H2(Ju,v)`. Neither `J` nor its invariance follows
from symmetry of `H2`. Nondegeneracy and positivity are further independent;
the current action receiver is not a positive physical metric.

## Honest boundary completion

For an action `I2_total=I2_bulk+I_boundary`, the conditional Hessian is

```text
H2_total = A^! Q A + Hess(I_boundary) + Green_domain_terms.
```

The last two summands require an action-owned endpoint functional, an admitted
boundary condition, and a common closed domain. VRS-2 proves that these are
indispensable on the live nonzero charged branch. The finite W/mirror
base-conormal relations do not supply them: active mixed gauge directions break
both halves, and normal conormals are not isotropic.

## Exact controls

The executable probe checks a finite exact residual-square model, including:

- symmetry and factorization at residual zero;
- a firing residual-dependent off-shell second-variation term;
- an independent symmetric boundary Hessian;
- a square-minus-one `J` compatible with one Hessian and incompatible with a
  planted comparator;
- the alternating form obtained only after `J` is supplied; and
- an indefinite receiver proving that quadratic ownership does not imply
  positivity.

## Hostile ceiling

This theorem does not establish an action-owned stationary background, total
`K/L`, a closed Green domain, physical cohomology, a positive pairing, a Born
rule, unitary evolution or superposition. It types the only role the current
second-action Hessian can honestly play: real quadratic and derived
differential input to a later, separately complex-equipped reduction.

VRS-4 is therefore licensed as a conditional descent theorem. VRS-5 remains
the forward construction needed to supply the missing background/operator
premise before VRS-6 can instantiate a total complex.
