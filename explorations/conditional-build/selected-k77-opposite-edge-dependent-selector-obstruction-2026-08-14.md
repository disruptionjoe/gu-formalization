---
artifact_type: exact_opposite_edge_dependent_selector_obstruction
created: 2026-08-14
status: NO_FULL_G_EQUIVARIANT_CHARGE_ONLY_SECTION__SOURCE_EPSILON_IS_SAME_SIGN_PARENT_NOT_OPPOSITE_COPY__CHARGED_BOUNDARY_SYMMETRY_RETAINS_ZERO_IMPORT_PRIMACY
source_return: SOURCE_CONFIRMS_ONE_EPSILON_FIELD_AND_ITS_ENDPOINT_MOMENTUM__SOURCE_SILENT_SECOND_FRAME_CHARGE_ADAPTED_CONSTRAINT_AND_OPPOSITE_ACTION
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-opposite-edge-dependent-selector-obstruction.json
canon_verdict_change: none
---

# Selected K77 opposite-edge dependent-selector obstruction

## Result first

The 98-dimensional opposite Cartan-slice compensator cannot be selected as a
full-`Spin_0(7,7)`-equivariant function of the endpoint charge alone.

Over the selected regular chamber the moment map

```text
J : M_-C = G x (-C) -> U,
J(g,lambda)=Ad_g^* lambda
```

is a principal `H` bundle.  Its fibre has dimension seven, where `H` is the
regular Cartan stabilizer.  The left `G` action on `G x (-C)` is free.

Suppose an equivariant section `s:U->M_-C` existed.  At the selected charge
`-mu`, every `h in H` fixes the base point.  Equivariance would give

```text
s(-mu)=s(h.-mu)=h.s(-mu).
```

Freeness of the left action forces `h=e`, contradicting the exact nontrivial
seven-dimensional stabilizer.  Therefore no such equivariant section exists.
This is a wholesale theorem inside the stated full-`G`-equivariant,
charge-only class, not a failed search; it is not a no-go for local sections
or sections using new source-owned data.

Local non-equivariant sections do exist because `dJ` has rank 91.  They choose
one point in the seven-dimensional `H` fibre and are gauge/frame choices, not
canonical dependent fields.

## Source epsilon does not evade the theorem automatically

The source owns one epsilon field and its actual boundary momentum has the
same sign as the endpoint charge.  At the selected fixture it realizes the
positive parent point `(e,+mu)`.  Treating that same field as an additional
edge system gives the planted same-sign expression

```text
mu + mu = 2 mu != 0.
```

The opposite cancellation requires a simultaneous second point with moment
`-mu`.  Reversing the existing momentum would replace the original endpoint
pair; it would not add an independent compensator.

Existing epsilon data could help only if the source/action imposed a new
charge-adapted frame condition that maps it into the principal `H` torsor and
supplied the opposite symplectic sign.  No inspected formula does so.

## The canonical connection is not a selector

The trace pairing gives the reductive split

```text
g = h direct_sum m,
A_H = pr_h(g^-1 dg).
```

This is a left-`G`-invariant principal `H` connection.  Exact selected-fixture
checks give `dim h=7`, `dim m=84`, an abelian `h`, and nonzero curvature whose
Cartan projection spans all seven `h` directions.  It transports the fibre
ambiguity covariantly but does not select a point or produce a flat global
trivialization.

Thus the best covariant charge-only object is a principal bundle with
connection, not an edge field section.

## Three surviving horns

1. **Charged boundary symmetry.** Retain the action-owned source-epsilon
   cotangent parent and its nonzero boundary charges.  This adds no field.
2. **Local gauge-fixed dependent representative.** Choose a local section of
   the `H` fibre.  It breaks full equivariance and is not a physical selection.
3. **Independent opposite edge completion.** Add a second group-valued
   boundary system with opposite moment map and a boundary action.  This is
   mathematically compatible but source/action unowned.

The first horn therefore retains zero-import primacy.  The result does not
prove that every extended GU action must choose it; it proves the current
source/action cannot obtain the opposite copy from the charge alone.

## Scientific effect

The edge-carrier dimension and cancellation searches are complete at the
current grade.  The remaining question is no longer “find the right
98-dimensional carrier.”  It is whether GU supplies an independently owned
second boundary frame/action.  Without one, the correct action-owned reading
is charged boundary symmetry, not gauge completion.

No ledger verdict, residue, quotient, datum, canon claim, physical BFV,
W/mirror selection, chirality or generation count follows.

## Reproduction

```sh
sage -python tests/channel-swings/selected_k77_opposite_edge_dependent_selector_obstruction_probe.py
```
