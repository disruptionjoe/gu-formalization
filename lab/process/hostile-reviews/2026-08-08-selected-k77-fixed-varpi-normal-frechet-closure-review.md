# Hostile review — selected K77 fixed-varpi normal Frechet closure

Date: 2026-08-08

Verdict:
`SURVIVES_WITH_SCOPE_NARROWING__LOCAL_FIXED_VARPI_RAW_RESIDUAL_BLOCK_ONLY`

## Preregistered attacks

1. The calculation may differentiate the stationary identity
   `F_A*=T* wedge T*` as if it defined the off-branch curvature.
2. “Fixed varpi” may freeze the wrong object if `A`, `T`, the observed
   pullback and ambient `varpi` are conflated.
3. A principal symbol may be relabelled as the complete lower-order
   Levi-Civita response.
4. The moving-observation term may be deleted by freezing the receiver rather
   than by the raw-residual-zero chain rule.
5. A local partial derivative may be inflated into the common-field Euler,
   Green, symplectic or physical equation.

## Charge 1 — where the summary outruns the artifact

The strongest invalid summary is “the full field equation is complete.”  The
certificate closes only the **local partial raw-residual derivative with
respect to `g` at fixed independent `varpi,epsilon`**.  It does not construct
the common-field formal adjoint, Green operator, analytic domain or reduced
equation.

The pre-wave expectation that the full Levi-Civita first jet has rank `24`
was false.  Exact calculation gives rank `20`.  The report now states that the
metric-derived torsion-free image is a proper subspace of the unrestricted
Lorentz-connection carrier.  The fixed-symbol transverse rank-six theorem
survives this correction.

The narrowed summary is supported.

## Charge 2 — where rigor could defend a mistyped object

The main mistyping is differentiating `F_A*=T* wedge T*`.  That is a selected
stationary equality obtained after choosing a flat reference branch.  The
off-branch source definition is

```text
F_A = F_B + d_B T + T wedge T,  A=B+T=varpi.
```

At fixed `varpi`, the three displayed constituent derivatives are separately
nonzero and cancel.  The planted `T* wedge T*`-only derivative is nonzero and
therefore catches the wrong-object route rather than silently agreeing with
it.

The second mistyping would transfer the raw-residual observation cancellation
to the action Euler covector.  At `Upsilon*=0`, `(delta O)Upsilon*=0`; the
action Euler owner in the Green construction is generally nonzero and keeps
all moving-receiver terms.  Both objects remain separately typed.

## Charge 3 — what else changes if this stands

| Surface | Disposition |
| --- | --- |
| v0.85 principal transverse augmented-torsion rank six | `survives_and_is_locally_completed` |
| v0.90 common-field Cartan/Ward composition | `survives` |
| v0.92 local indefinite residual pairing | `survives` |
| v0.94 comoving coefficient packet | `survives_and_composes` |
| component-normal curvature derivative at fixed varpi | `dissolved_as_independent_owner` |
| unrestricted rank-24 Lorentz connection tangent | `survives_as_varpi_field_space_not_LC_image` |
| v0.65 moving action-Euler observation terms | `survives` |
| common-field formal adjoint and Green concomitant | `needs-recheck` |
| common analytic/Krein/symplectic domain | `needs-recheck` |
| BV/BFV and physical quotient | `needs-recheck` |
| signature, canon and public posture | `survives_unchanged` |

No other artifact dissolves.

## Mandatory lenses

- **Layer 0 semantics:** ambient `varpi`, observed pullback, reference
  connection, augmented torsion, total connection, raw residual and action
  Euler are distinct.
- **Prior art:** v0.33 already fixed the source variables; v0.28 owned the
  local soldering/observation chain; v0.65 owned the moving action receiver;
  v0.94 closed coefficient transport.  This wave composes them with the
  previously missing expanded curvature derivative rather than rebuilding
  them.
- **Differential geometry:** the covariant variation formula closes the local
  first jet and exposes the rank-20 torsion-free image.
- **Symplectic geometry:** no presymplectic current is claimed; the
  common-field Green concomitant remains the next gate.
- **Variational PDE:** local covariant completeness is not a global closed
  operator, hyperbolicity estimate or common domain.
- **Real Clifford/Krein:** the v0.92 pairing is indefinite and conditional;
  no positivity inference appears.
- **Complex/path-integral:** the calculation makes no contour, measure,
  determinant, saddle or Wick-rotation claim.
- **Source fidelity:** source confirms the field coordinates and is silent on
  the exact cancellation/rank theorem.
- **Constraint accounting:** no field, coefficient, function, quotient,
  residue or P1/P2/P3 consumption is introduced.

## Controls

- all three expanded curvature constituent derivatives are nonzero;
- their sum and direct `delta F_A` are zero;
- freezing `T` while moving `B` produces nonzero `delta F_A`;
- differentiating `T* wedge T*` alone produces a false live term;
- full covariant Levi-Civita rank is `20`, while each fixed-symbol rank is `9`;
- all three causal transverse restrictions have rank `6`;
- the moving observation term becomes live away from `Upsilon*=0`;
- independent Sage reproduces every new rank and cancellation.

## Verdict and next gate

The local fixed-varpi raw-residual metric block survives.  The next gate is to
assemble it with the already-owned `D_varpi` and gauge/epsilon blocks and the
v0.92 conditional residual pairing, then derive the common-field
action-density formal adjoint and Green concomitant.  Only that result may
open symplectic, BFV and common-domain work.

No trap file was changed.  The on-shell-identity/off-shell-definition error is
recorded directly in the result, controls, ledger migration and operating
contract successor so future agents encounter it at the active work surface.
