---
artifact_type: source_return
created: 2026-08-13
source_claims: [SC-ACT-01, WGS-04]
return_code: SOURCE_CONFIRMS_ARBITRARY_ALPHA_TILTED_SOURCE_TANGENT_AND_XI_EQUALS_D_OMEGA_UPSILON_REDUNDANCY__SOURCE_SILENT_PRIMAL_TANGENT_CONSTRAINT_AND_FULL_BV_MASTER_ACTION__REPOSITORY_DERIVES_EXACT_LOCAL_BVKT_SEQUENCE
---

# Source return: I2B source/BV--Koszul--Tate exact sequence

## `SOURCE-CONFIRMS`

- Weinstein varies the first bosonic action through arbitrary connection
  translations `varpi+s alpha`; `alpha` is therefore a primal Euler test
  direction, not automatically a gauge parameter.
- The tilted source-coordinate grammar yields
  `delta T = alpha-D_A zeta`.
- The source displays `dI=(Upsilon,Xi)` with
  `Xi=D_omega Upsilon`, and calls the second equation redundant once
  `Upsilon=0`.

## `SOURCE-CORRECTS`

The source pack explicitly warns that the displayed `Xi=D Upsilon`
redundancy is not automatically an off-shell Noether identity.  It therefore
cannot be used by itself to declare the independent `varpi/T` Euler equation
gauge or to restrict `alpha`.

## `SOURCE-SILENT`

The checked source does not print:

- a primal tangent constraint on arbitrary `alpha`;
- a BV master action or its complete ghost/antifield tower;
- the selected 196-cell real-K77 reduction;
- an action-owned moving fundamental symmetry;
- the global BFV boundary complex or common analytic domain; or
- the relation between this selected connection and the complete
  `U(64,64)` / two-`C^(32,32)`-half action parent.

## `REPO-DERIVES`

The finite selected source chart, residual gauge generator and first
reducibility form an exact local sequence.  Both live Euler covectors satisfy
the Ward/KT nilpotence identities and remain nonzero after descent.  This is a
source-directed repository theorem, not a quotation.

```text
SOURCE-CONFIRMS: arbitrary alpha, tilted tangent grammar, on-shell Xi redundancy.
SOURCE-CORRECTS: redundancy is not automatically an off-shell Noether identity.
SOURCE-SILENT: primal constraint, full BV master action, moving reduction, global BFV/domain.
REPO-DERIVES: exact local BV/KT sequence closes while both Euler classes survive.
```
