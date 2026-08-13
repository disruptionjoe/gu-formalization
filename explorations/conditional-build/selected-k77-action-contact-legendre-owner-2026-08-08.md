---
artifact_type: construction_scope_correction
created: 2026-08-08
status: GENERIC_CONTACT_THEOREM_ONLY__ACTION_K77_LEGENDRE_GREEN_BANK_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS__NONQUADRATIC_FIRST_ORDER_ACTION_AND_AUGMENTED_TORSION__SOURCE-SILENT__BFV_LEGENDRE_IDENTIFICATION__REPO-CORRECTS__KT_IS_GENERIC_CONTACT_FIXTURE_ONLY
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_action_contact_legendre_owner_probe.py
  - tests/channel-swings/selected_k77_action_contact_legendre_owner_independent.sage
registry: lab/process/selected-k77-action-contact-legendre-owner.json
---

# Selected K77 action/contact Legendre owner

## Result first

The endpoint geometry survives, but the proposed action coefficient does not.

The v0.69 contact calculation introduced

```text
p = K T,                 K = diag(-1,2,3),
```

inside a finite quadratic control.  That control correctly proves a universal
contact theorem: the two-connection Ward complex closes, compact-support gauge
is characteristic, unrestricted endpoint gauge carries a moment map, and the
endpoint cotangent two-form is nondegenerate after the stated quotient.

But `K` was chosen, not derived from the selected GU action.  A second
inequivalent indefinite form `diag(-2,5,7)` passes the same Ward, rank, Green
and symplectic tests while assigning a different `p=KT`.  The selected source
action cannot remove this ambiguity by secretly being quadratic: on the exact
noncyclic action fixture its scaling polynomial is

\[
 I(C,zT)=-\frac43z^3+\frac{300}{7}z^2-5z.
\]

Its action-derived coefficient `E_B-E_T` is nonzero already at `T=0`, whereas
every fixed linear `KT` vanishes there.  Therefore no fixed `K` can make

```text
E_B-E_T = K T
```

an identity on the selected configuration family.

The fired ending is:

```text
GENERIC_CONTACT_THEOREM_ONLY__ACTION_K77_LEGENDRE_GREEN_BANK_OPEN
```

This is a scope correction, not a loss of the local `40/40` endpoint quotient.
The independent endpoint cotangent variables and their dressing remain exact.
The missing object is now correctly named: the actual ten-direction selected-
action boundary bank obtained from `E_B-E_T`, with its normal restriction and
complete observation receiver.

## Layer 0

| shared phrase | exact object | distinct object |
| --- | --- | --- |
| action Green coefficient | boundary restriction/normal trace of the selected action's degree-thirteen `E_B-E_T` | a generic contact momentum |
| cotangent momentum `p` | independent coordinate on the endpoint cotangent model | a constitutive graph `p=KT` |
| `K` | coefficient form chosen in the quadratic finite control | a map derived from the nonquadratic GU action |
| ten K77 contact directions | rank-ten Levi-Civita/observation geometry and ten nonzero generic cotangent shifts | the selected action's ten coefficient values |
| coefficient fit | a map arranged to match one background | an identity forced over the action's configuration family |
| local endpoint quotient | exact direct-sum collar phase geometry | global `tau_A0` BFV phase space and common domain |

The load-bearing correction is variational depth and ownership.  A canonical
cotangent coordinate need not be expressed as `KT`.  A Legendre graph becomes
part of this action only when the action derives it.

## Primary-source return

The 2021 draft explicitly supplies

\[
 I^B_1=\left\langle T_\omega,*\left[\odot_\omega
 \left(F_{B_\omega}+\frac12d_{B_\omega}T_\omega
 +\frac13[T_\omega,T_\omega]\right)
 +\frac{\kappa_1}{2}T_\omega\right]\right\rangle
\]

and `T_omega=varpi-epsilon^-1 d_0 epsilon`.  The cubic eddy term is therefore
source-explicit.  The checked source packet does not publish a BFV phase-space
construction or identify its endpoint momentum with the v0.69 quadratic
fixture.

```text
SOURCE-CONFIRMS:
  the nonquadratic first-order action, augmented torsion and epsilon chain.

SOURCE-SILENT:
  BFV/Legendre identification and the physical endpoint coefficient bank.

REPO-CORRECTS:
  p=KT is a generic quadratic contact realization, not the selected-action
  coefficient owner.
```

## Exact tests

### Two valid `K` controls

For the three-edge/four-node difference matrix `D`, both

```text
K1 = diag(-1,2,3)
K2 = diag(-2,5,7)
```

are nondegenerate and indefinite.  For

\[
 H(K)=\begin{pmatrix}D^TKD&-D^TK\\-KD&K\end{pmatrix},
 \qquad R=\binom{I}{D},
\]

exact arithmetic gives

```text
H(K1)R = H(K2)R = 0
R^T H(K1) = R^T H(K2) = 0
rank H(K1) = rank H(K2) = 3.
```

Both have the same oriented Green decomposition and the same canonical
endpoint two-form.  Yet for the same background `T=(2,-3,5)`, `K1 T != K2 T`.
Thus none of Ward closure, nondegeneracy, indefinite signature, endpoint
orientation or symplectic rank selects the original `K`.

### Selected-action obstruction

The source-shaped noncyclic action fixture has live linear, quadratic and
cubic scaling coefficients.  Entrywise Fréchet differentiation gives a live
`E_B-E_T` at both `T=0` and `T=T*`, with different values.  Since every fixed
linear `KT` vanishes at `T=0`, the proposed global identity is impossible on
that selected action class.

### Constraint-surplus control

At one nonzero nine-component background, a symmetric `9 x 9` matrix has 45
free entries.  The map

```text
Sym^2(Q^9) -> Q^9,       K |-> K T*
```

has rank nine, so fitting `K T*=E_B-E_T` leaves 36 free directions.  It can
fit every target and therefore supplies no confirmation.  A field-dependent
`K` would be an additional function-valued construction and must be charged as
one; it cannot be hidden inside the letter `K`.

Main exact probe: `48/48 PASS`.  Independent Sage/QQ replay: `PASS`.

## What is preserved and what is corrected

Preserved:

- the source-native two-connection contact map;
- exact local Ward closure and small-gauge basicness;
- the live unrestricted boundary moment map;
- the independent two-endpoint cotangent model;
- the direct-sum local K77 `40/40` quotient; and
- the single-holonomy `40 -> 20` compression no-go.

Corrected:

- v0.69's `p=KT` is not an action-derived GU coefficient;
- the arbitrary nonzero `connection_current` proves generic rank-ten contact
  sensitivity, not the selected action's ten coefficients;
- matching the signs of `eta_3 e_2-eta_0 e_0` and
  `eta_3 p_2-eta_0 p_0` does not supply coefficient ownership; and
- one-background `K` fitting is underconstrained rather than explanatory.

Still open:

- assemble `E_B-E_T` coefficientwise on all ten actual K77 normal directions;
- apply the correct normal restriction/boundary trace and complete observation
  equation dual;
- insert that action-owned bank into the already-built independent endpoint
  dressing;
- extend through full `tau_A0`, moment-map/BFV reduction and a common domain.

## Specialist and hostile disposition

- **Symplectic geometry:** preserve the cotangent phase geometry; a Legendre
  submanifold is extra constitutive data and is not needed to define the
  canonical two-form.
- **Variational bicomplex:** `E_B-E_T` is action-owned; its boundary trace must
  be computed before it is identified with endpoint `p`.
- **Differential geometry:** rank-ten contact directions do not fix their
  action coefficients.
- **Representation theory:** a universal coefficient-module tensor product is
  not a full K77 specialization.
- **Krein/operator theory:** indefinite nondegeneracy is retained, but cannot
  select one `K` from another.
- **PDE/domain theory:** no global boundary domain, hyperbolicity or common
  closed operator follows.
- **Source criticism:** the action is source-explicit; the BFV and Legendre
  identification are not.

Both standing hostile charges fire.  The v0.69 summary outran its arbitrary
current and quadratic fixture, while a full retraction would defend the wrong
object by discarding a valid universal contact theorem.  The repair narrows
ownership and preserves the theorem.

## Progress and accounting

```text
Ledger v0.75 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: none
frontier_conditions_closed: 2
  - p=KT is disposed as a generic quadratic realization, not action ownership
  - the independent endpoint/contact theorem survives the correction
frontier_conditions_opened: 1
  - actual ten-direction selected-action E_B-E_T boundary bank
remaining_named_conditions: 2
```

No new field, coefficient, selector, quotient or external datum is introduced.
P1/P2/P3 remain unused.  Curt remains formally separate inside the Eric lane;
no third lane, verdict, canon or public-posture movement occurs.

## Next gate

Assemble the actual selected-action `E_B-E_T` boundary coefficient on all ten
K77 normal directions, including the normal restriction/orientation and
complete observation receiver.  Only then insert it as the endpoint cotangent
bank in the already-exact direct-sum dressing.  A successful action bank opens
full `tau_A0`/BFV/common-domain descent; a rank or type failure retains the
universal contact theorem but blocks action ownership.
