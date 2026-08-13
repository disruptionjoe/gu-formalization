---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
status: MOVING_SPLIT_COVARIANT_DERIVATIVES_EXACT__COMPATIBLE_LOCUS_CONSTRUCTED__CURRENT_ACTION_DOES_NOT_SELECT_IT
target_claim: NONE-NOT-A-KILL
ledger: lab/process/conditional-physics-ledger-v0.192.json
canon_verdict_change: none
---

# Selected K77 moving split structure and action-selection gate

## Result in plain English

The admitted `4+10` split now has an exact moving-connection calculus.  Its two
Clifford structures are not bookkeeping labels:

- `omega` distinguishes the two ambient Weyl halves;
- `J4` is the split-native real complex structure inside them.

Their covariant derivatives recover, without fitting, every connection piece
that fails to preserve the corresponding structure.  The canonical
projector-reduced K77 connection preserves both.  A larger block connection
can preserve `omega` while breaking `J4`, and a still larger connection can
exchange the two `omega` halves.

The selected action does **not** presently force those extra pieces to vanish.
The already-certified nonzero-branch Hessian is nondegenerate on both the
block-preserving and half-exchanging direction banks.  Thus the reduction is a
valid conditional connection locus, but it is not dynamically selected by
the current pointwise action.  The extra pieces remain live tensor fields.
The source says `varpi` hosts Higgs-like and Yukawa functions, making this
decomposition a promising construction arena; it does not identify either
tensor with a Higgs or Yukawa channel.

## Pre-wave and Layer 0

- **Inherited fork:** `REAL-CLIFFORD-FORM=Cl(7,7)`.  No settlement of the
  separate `SIGNATURE-AMBIENT` or action-parent forks is made.
- **Decidable search:** the complete pointwise stabilizer decomposition and
  moving-frame covariance are decided wholesale.  A full-unitary Hermitian
  connection, global action domain and physical quotient are not.
- **New unowned objects:** none.  `omega` and `J4` are transported Clifford
  volume elements of the already admitted split.
- **Kill conditions:** failure of the affine moving-frame term, incomplete
  reconstruction, basis dependence, or failure of the canonical compatible
  connection.  None fired.

The following remain distinct:

| object | type | result |
|---|---|---|
| `A^P` | K77 vector connection preserving the observation projector | previously exact |
| spin lift of `A^P` | `spin(1,3)+spin(6,4)` connection | preserves `omega,J4` |
| `omega` | real square-`+1` ambient chirality | two-half reduction |
| `J4` | real square-`-1` split-native endomorphism | finer reduction |
| scalar `i` | external complex scalar | not identified with `J4` |
| Hermitian `(32,32)` forms | source-asserted same-half unitary structure | not derived here |
| full `varpi` | complex `U(64,64)`-arena connection | no K77 projection built |
| breaking tensors | covariant derivatives of moving structures | exact, physical identity open |

## Exact decomposition

Suppressing conjugation by the moving spin frame, write its logarithmic
derivative as `x` and the adapted connection as

```text
Ahat = A + x.
```

For `omega^2=1`, `J^2=-1` and `[omega,J]=0`, define

```text
B_omega = (Ahat + omega Ahat omega)/2,
K_omega = (Ahat - omega Ahat omega)/2,
H       = (B_omega - J B_omega J)/2,
K_J     = (B_omega + J B_omega J)/2.
```

Then exactly

```text
Ahat = H + K_J + K_omega.
```

`H` preserves both structures.  `K_J` preserves `omega` but breaks `J`.
`K_omega` exchanges the two `omega` halves.  More importantly, these pieces
are reconstructed directly from the moving covariant derivatives:

```text
K_omega = (D_A omega) omega / 2,
K_J     = - ((D_A J)_omega-even) J / 2.
```

Thus no desired rank, preferred basis or auxiliary projector is inserted.
The covariant derivatives are the intrinsic-torsion coordinates of the two
nested reductions.

The exact probe transports the structures by a nontrivial Spin element,
includes the `-x` affine compensation, and repeats the calculation after a
nontrivial residual subgroup change of adapted frame.  Global fields and both
covariant derivatives are unchanged.  Freezing the moving structure or
dropping the affine term produces a nonzero false defect, so both controls
fire.

## The three connection loci

The predecessor asked whether the geometry selects the full parent, the two
halves, the finer split, or none.  At K77 spin-connection grade the answer is:

| locus | `D omega` | `D J4` | construction status |
|---|---:|---:|---|
| finer compatible `H` | `0` | `0` | exact conditional path |
| two-half block `H+K_J` | `0` | nonzero | exact conditional path |
| full `H+K_J+K_omega` | nonzero | generally nonzero | exact endomorphism decomposition |

This table is a classification, not action selection.  It also stops the two
source statements from being treated as rivals: two Weyl halves can be a
moving reduction inside a full connection, whose off-diagonal components are
tensorial fields.

## Action-selection composition

The August 10 nonzero-branch calculation already decided the relevant
pointwise variational question.  Its exact Hessian has zero radical on:

- `114,688` two-half block directions;
- `114,688` half-exchanging directions; and
- all `229,376` connection-coefficient directions together.

It therefore gives a genuine quadratic response to both `K_J` and
`K_omega`; it does not quotient either away or force the action onto `H`.
Both larger field domains remain stationary competitors.  This is consistent
with the moving-projector theorem: restricting the field space makes a
consistent truncation, not an Euler equation that creates the truncation.

The conclusion is pointwise and branch-specific.  A source constraint,
coupled moving-reduction Euler equation, BV differential, global boundary
condition or different stationary branch could still select one locus.

## Specialist preassessment

- **Layer-0 semantics — actual math, very high.** The vector, spin and unitary
  connections and the real/complex structures remain separately typed.
- **Prior art/source — actual math, high.** Existing exact Hessian work is
  composed rather than needlessly recomputed; source assignments are not
  promoted to derivations.
- **Principal-bundle geometry — actual math, very high.** The affine frame
  derivative is included and residual-frame naturality is exact.
- **Clifford/commutant theory — actual math, very high.** The three pieces are
  the complete nested stabilizer decomposition.
- **Variational bicomplex — actual math, high.** Selection is priced only from
  an existing action Hessian, not from compatibility.
- **Symplectic/BV — actual math, high.** No configuration reduction is called
  a characteristic quotient.
- **Analytic/PDE — actual math, high.** Positivity, Green domains and index are
  fenced out.
- **Construction versus selection — actual math, very high.** The compatible
  path exists while its dynamical ownership remains absent.
- **Contrary path — actual math, high.** Non-preserving components are retained
  as possible physical fields rather than automatically killed.

## Source return

The checked source confirms:

- two complex `C^(32,32)` Weyl halves;
- a distinct full `U(64,64)` principal-group arena; and
- the assignment of gauge, Higgs-like, CKM and Yukawa functions to components
  of the connection one-form `varpi`.

It does not print the `D omega/D J` decomposition, derive the same-half
Hermitian form, map the full unitary connection to the K77 spin connection, or
identify `K_J`/`K_omega` with a physical Higgs, Yukawa or mirror channel.

## Accounting and next gate

The probe passes `40/40`.  Six ledger rows move in distance/evidence only.
Headline verdicts, residue `84`, at least `19` function-valued slots, nine
forks, five quotients, P1/P2/P3, canon and public posture do not move.

The next high-information truth-status research gate is not another demand that all breaking
pieces vanish.  It is:

```text
BUILD_THE_FULL_UNITARY_TO_K77_SPLIT_INTRINSIC_TORSION_COMPATIBILITY_MAP;
DERIVE_OR_KILL_THE_HERMITIAN_FORM_AND_EXTERNAL_I_PLACEMENT;
PORT_K_J_AND_K_OMEGA_INTO_THE_SOURCE_VARPI_BLOCKS;
THEN_TEST_WHETHER_ANY_BLOCK_IS_THE_SOURCE_HIGGS_LIKE_CHANNEL_WITHOUT_FITTING IT.
```

Only after that typing succeeds should the surviving block enter the
lower-order Riccati and BV/KT system.

Postflight found no GU scientific mailbox item newer than the already absorbed
2026-08-10 packets. The 2026-08-12 PROG-004 note is a process-evidence pointer
for a separate steerability session and does not reorder this successor.
