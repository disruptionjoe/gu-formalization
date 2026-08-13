---
artifact_type: conditional_construction_result
created: 2026-08-12
status: CORRECTED_ACTION_EULER_SQUARE_EXACT_ON_FIXED_BACKGROUND__NO_NEW_ESCAPE_AT_THIS_GRADE
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
source_claims: [SC-ACT-01, SC-ACT-04]
source_return: SOURCE_CONFIRMS_FIRST_ACTION_AND_PRINTED_ENDPOINT_FORMULAS__SOURCE_SILENT_CORRECTED_E_ACT_SQUARE__REPO_CONSTRUCTS_EXACT_LOCAL_RIVAL
target_claim: NONE-NOT-A-GU-KILL
free_object_delta: "zero fields, parameters, data, selectors, quotients or boundary conditions"
scripts:
  - tests/channel-swings/selected_k77_i2b_action_euler_square_probe.py
  - tests/channel-swings/selected_k77_i2b_action_euler_square_independent.sage
---

# Selected K77 corrected action-Euler square

## Result

The corrected first-action Euler covector has now been squared on the exact
moving-`Q_u`, fixed-background, `196`-real connection tangent left open by
ledger v0.225.

The action wedge-Hodge pairing gives an exact diagonal Riesz matrix with
inertia `(98,98)`.  It therefore turns the Fréchet-adjoint contribution in

```text
E_act = S(Fbar) + L_T^! S^! T + *kappa T
```

into a unique degree-thirteen representative on this bank.  On the constant
trace-`H_q` locus that companion is exactly `2 S_q`.  The observer-`Q_u` Gram
of `(S_q, companion, H_q)` is

```text
[[160, 320, 0],
 [320, 640, 0],
 [  0,   0, 2]].
```

Consequently the repo-composed corrected square is

```text
1/2 ||E_act||^2_Q_u = 80 (rho+r^2)^2 + kappa^2 r^2,
```

with radial branch

```text
rho = -r^2-kappa^2/160.
```

This is exactly the same restricted polynomial and branch as the literal
printed-endpoint square.  More strongly, the two squared-action Euler
covectors agree after exact simplification on all `196` fixed-background
connection cells.

That agreement is not a global residual identity.  The two Fréchet maps are
different: the companion derivative is six times the direct derivative in
only `4/196` cells.  Their equality occurs only after evaluating the common
constant-locus residual and pairing through `Q_u`.  The full-domain cyclic-
kernel obstruction and the distinction between literal `SC-ACT-04` and the
repo-composed corrected rival therefore survive.

## The stationary obstruction survives

On the common radial branch, both rivals retain the same twelve diagonal
Euler cells:

```text
(0,0):   kappa^2 (kappa - 44 r) / 40
(i,i):  -kappa^2 (kappa + 36 r) / 40,  i=1,...,11.
```

The two cancellation shapes have determinant `80`.  For nonzero `kappa`, no
single nonzero `r` cancels both.  Thus the corrected square supplies no new
unrestricted fixed-background stationary point relative to the printed
endpoint rival.

This does not prove that the conditional Higgs/source-action route fails.  It
identifies the precise remaining construction burden: the allowed physical
tangent must be derived from the source action, constraints, or BV complex,
or the presently held metric/reference/section/Shiab data must contribute
through their actual moving variation.  Restricting the tangent merely to fit
the branch would not meet that burden.

## Layer 0

| object | established here | not identified with |
| --- | --- | --- |
| first-action Euler covector | exact derivative representative on the declared bank | printed endpoint residual globally |
| action Riesz representative | unique because the action Gram is nondegenerate | observer `Q_u` primalizer |
| equality of restricted residual values | exact on the constant trace-`H_q` locus | equality of Fréchet maps |
| equality of squared Euler covectors | exact on the fixed-background 196-cell bank | equality on moving metric/section/reference data |
| radial stationarity | one restricted contraction vanishes | unrestricted connection stationarity |
| two `C^(32,32)` halves | inherited matter carriers | two connection fields or full `U(64,64)` parent |

## Structure fingerprint and altitude

- **Carrier:** the inherited `196`-real fixed-`H_q` connection tangent.
- **Pairings:** action wedge-Hodge pairing for the Riesz map; observer `Q_u`
  pairing for the composed square.
- **Real structure/grading:** selected real K77, grade-one connection cells to
  degree-thirteen Euler representatives.
- **Embedding:** trace-`H_q` owner inside the selected K77 construction; the two
  `C^(32,32)` halves, their block subgroup, and full `U(64,64)` remain distinct.
- **Variational altitude:** exact local fixed-background first variation of a
  repo-composed action rival.
- **Globalization grade:** pointwise finite bank only; no global section,
  domain, quotient, state, or spectrum.

The commuting diagram

```text
action covector --Riesz(action pairing)--> E_act representative
       |                                      |
       | differentiate                        | square with Q_u
       v                                      v
196-cell covector <-------------------- fixed-background Euler
```

is proved on the declared bank.  Transport to moving background variables,
the source's unprinted `Q_B`, or a physical BV quotient remains open.

## Adaptive specialist assessment

- **Variational bicomplex:** equality of values after restriction does not
  identify the underlying Fréchet derivatives; the certificate keeps both.
- **Symplectic geometry:** twelve transverse equations cannot be discarded
  until the action supplies a coisotropic constraint surface and quotient.
- **Principal-bundle geometry:** the held reference connection is still
  independent of the translation field; its moving response must be derived.
- **Krein/operator theory:** the exact balanced Riesz inertia gives existence
  and uniqueness on this finite bank, not positivity or a closed domain.
- **Exact computation:** a singularized Riesz control and a derivative-
  equality plant both fire; an independent Sage checksum verifies the reduced
  polynomial and determinant.
- **Source criticism:** the released source prints the first action and
  endpoint square but does not print this corrected Euler-norm action.
- **Contrary path:** a source/action-owned tangent/BV reduction remains live;
  this result tells it exactly which twelve cells it must remove or balance.

## Progress meter

```text
Ledger v0.226 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: corrected E_act square assembled and compared exactly
Frontier open: derive the physical tangent/BV reduction or full moving-background contribution
```

## Next gate

Construct the smallest source/action-owned tangent or BV differential on this
same bank and test whether its image/kernel legitimately excludes the twelve
transverse cells.  In parallel, type the moving reference/metric/section/Shiab
derivatives that are absent from the held-background calculation.  Do not fit
a restriction to the desired branch, infer a quotient from Ward nullity, or
identify the corrected square with literal `SC-ACT-04` globally.
