---
artifact_type: exact_construction_and_scope_result
created: 2026-08-10
status: COMPLETE_POINTWISE_CONNECTION_HESSIAN_FULL_RANK__NONZERO_BRANCH_OWNS_BOTH_DECOMPOSITIONS__NO_ACTION_DERIVED_PARENT_REDUCTION
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, RA-D2, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
canon_verdict_change: none
---

# Selected K77 nonzero-branch parent Hessian

## Result in plain English

The known nonzero connection branch does **not** dynamically throw away the
extra connection directions. Its exact pointwise Hessian is full rank on all
`229,376 = 14*16,384` real K77 connection-coefficient directions.

This remains true under both decompositions that had been competing to define
the parent:

| candidate piece | dimension | exact inertia | radical |
|---|---:|---:|---:|
| moving-Spin / `B`-skew | `113,792` | `(56,874,56,918)` | `0` |
| `B`-self complement | `115,584` | `(57,785,57,799)` | `0` |
| two-half block directions | `114,688` | `(57,344,57,344)` | `0` |
| half-exchanging odd coset | `114,688` | `(57,315,57,373)` | `0` |
| complete coefficient tangent | `229,376` | `(114,659,114,717)` | `0` |

Thus the preregistered second horn fires:

```text
NONZERO_HESSIAN_OWNS_BOTH
```

The action has a genuine quadratic response in every connection direction. A
hard moving-Spin restriction, a two-Weyl-half connection, or a quotient would
need an additional owner: a declared field domain, source reduction, gauge/BV
differential, boundary/domain condition, or a coupled mechanism not present in
this pointwise Hessian.

## Efficient complete calculation

A dense `229,376`-square matrix would be both wasteful and unauditable. The
exact Hessian preserves Clifford grade and, on a basis vector
`e^i tensor gamma_J`, the label

```text
J xor {i}.
```

Each label therefore gives a block of size at most fourteen. Signed
permutations of the seven positive and seven negative K77 axes reduce the
complete carrier to one rational block for each label signature. The probe
computes every such orbit, multiplies by the exact binomial multiplicity, and
recovers all `14*2^14` directions. Each of the fifteen grade banks is full
rank. The independent radial checksum is the previously known
`-14*kappa_1`.

For `kappa_1 != 0`, the complete Hessian scales with `kappa_1`; a negative
value swaps positive and negative inertia but cannot create a radical. The
`kappa_1=0` zero branch is a different stratum and is not covered by this
statement.

## The two `C^(32,32)` halves are retained correctly

Curt's two split Weyl spaces and the later full `U(64,64)` principal group are
not competing transcriptions of one object. They define a moving block
reduction inside the full source parent. The even Clifford bank preserves the
halves; the odd bank exchanges them.

The background `T*=-(kappa_1/312)Phi1` is odd, so it does not lie in the
two-half block-reduced connection. Conditional on choosing this particular
nonzero branch, the full `U(64,64)` comparator can host it and its complete
normal Hessian; a separately posited moving-Spin field domain can also host
the odd `Phi1` line. The action calculation does not choose between those two
field-domain claims.

This is narrower than saying that GU has selected full `U(64,64)`. Other
stationary branches can exist on the two-half reduction, and the source still
does not say which residual/action parent is physically operative.

## Layer 0 and source return

The object computed is the **pointwise first-transgression connection
Hessian** at fixed geometry and moving frame. It is not the raw residual
Jacobian, residual-square Gram Hessian, metric/epsilon Hessian, BV quotient,
closed operator, or fermion spectrum.

The already-audited source material supplies:

- the full `U(64,64)` `P_H`;
- two `C^(32,32)` Weyl halves;
- the first-transgression `1,1/2,1/3` action grammar.

It does not supply this Hessian or select the operative reduction:

```text
SOURCE_CONFIRMS_FULL_U6464_P_H_TWO_C32_32_WEYL_HALVES_AND_FIRST_TRANSGRESSION_ACTION_GRAMMAR
SOURCE_SILENT_OPERATIVE_PARENT_REDUCTION_AND_COMPLETE_HESSIAN
```

## Specialist pre-assessment applied

1. **Layer-0 semantics — ACTUAL MATH, very high.** Keep the two parent
   decompositions and three action notions separate; only the first-action
   Hessian is admissible here.
2. **Clifford/representation theory — ACTUAL MATH, very high.** Use real K77
   grade and signed-permutation orbits; a complexified calculation cannot
   decide the real parent question.
3. **Variational PDE — ACTUAL MATH, high.** Compute the true second variation,
   including both Frechet-adjoint placements, rather than differentiating the
   printed residual endpoint.
4. **Symplectic geometry — ACTUAL MATH, high.** Do not call a Hessian kernel a
   quotient without a characteristic distribution; conversely, nonzero
   Hessian rank does not establish a positive physical phase space.
5. **Krein/operator theory — ACTUAL MATH, high.** Record inertia but do not
   infer stability, a fundamental symmetry, or a closed domain from a finite
   indefinite matrix.
6. **Source archaeology — ACTUAL MATH, high.** Retain both the two-half and
   full-group source statements; neither is allowed to disappear into the
   other's notation.

## Controls and hostile boundary

- exact radial replay: `-14*kappa_1`;
- every signed-permutation orbit counted to the full denominator;
- `210` cross-grade representatives vanish exactly;
- three noncanonical orbit representatives reproduce rank and inertia;
- a planted `B`-skew-only quadratic form misses a nonzero grade-zero
  complement entry;
- no complexification is used to infer a real-form property.

The probe passes `38/38` after the durable registry is present. The separate
hostile review keeps the conclusion pointwise and branch-specific.

## Accounting and next gate

No ledger verdict, residue, quotient, coefficient, external datum, P1/P2/P3,
canon verdict or public posture changes.

The bosonic pointwise parent-selection gate is now closed negatively. The next
highest-information Build is the induced K77 Dirac/Rarita--Schwinger operator
on the source-full common carrier, with the moving-Spin restriction and the
two-half reduction retained as explicit ablations. It must compare the proposed
`W`, its mirror, planted `192`s, the `640`, and the `832`, and may only select a
physical carrier through a source/action kernel, cohomology, or spectral
projector. Coupled metric/epsilon/derivative Hessians, gauge/BV, Green/Krein
domain and physical spectrum remain serial downstream gates.
