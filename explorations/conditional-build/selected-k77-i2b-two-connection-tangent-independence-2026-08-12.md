---
artifact_type: construction_correction
created: 2026-08-12
status: SC_ACT_04_OWNER_RETYPED__B_ONLY_BACKGROUND_CANCELLATION_KILLED__ENDPOINT_AND_ACTION_EULER_RIVALS_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
source_claims: [SC-ACT-01, SC-ACT-04]
source_return: SOURCE_CORRECTS_SC_ACT_04_OWNER_TYPING__LITERAL_I2B_SQUARES_PRINTED_ENDPOINT_UPSILON__ACTION_CONSISTENCY_LEAVES_CORRECTED_E_ACT_SQUARE_AS_SEPARATE_RIVAL
target_claim: NONE-NOT-A-GU-KILL
free_object_delta: "zero fields, parameters, data, selectors, quotients or boundary conditions"
scripts:
  - tests/channel-swings/selected_k77_i2b_two_connection_tangent_independence_probe.py
---

# Selected K77 `I2B` residual-owner and two-connection tangent gate

## Result

The last 24 ledger versions were building a real and useful object, but the
source ownership attached to that object was wrong.

Three expressions had been compressed into one name:

```text
Fbar       = F_B + 1/2 D_B T + 1/3 T wedge T       (inside I1B)
Upsilon_p  = Shiab(F_A) + * kappa T                 (printed endpoint)
E_act      = Shiab(Fbar) + L_T^! Shiab^! T + *kT   (actual I1B derivative)
```

The draft's literal second action squares `Upsilon_p`.  The repo's corrected
variational reading would instead square `E_act`.  The v0.201--v0.224 chain
squared the path-average bracket itself.  Its exact calculations survive as a
conditional construction, but the claim that `SC-ACT-04` literally owns that
particular residual is withdrawn.

This is not cosmetic.  On the same exact moving-`Q_u` bank, changing the
quadratic coefficient from the path-average `1/3` to the printed endpoint's
unit coefficient changes the restricted equation from

```text
rho = -r^2/3 - 3 kappa^2/160
```

to

```text
rho = -r^2 - kappa^2/160.
```

The old branch fails the printed-endpoint equation exactly.  On the new branch
the complete connection Euler still has twelve diagonal cells:

```text
(0,0):   kappa^2 (kappa - 44 r) / 40
(i,i):  -kappa^2 (kappa + 36 r) / 40,  i=1,...,11.
```

Their two cancellation equations again have determinant `80`, so this literal
endpoint rival also has no nonzero stationary point on the unrestricted fixed-
reference translation bank.  The action-consistent `||E_act||^2` rival has not
yet been assembled on this moving family.

## The two-connection theorem

Write `A=B+T`.  The exact tangent coordinate map is

```text
(delta B, delta T) -> (delta A, delta B)
                      = (delta B+delta T, delta B).
```

If a differential in `(A,B)` coordinates is `(E_A,E_B)`, then in `(B,T)`
coordinates it is

```text
E_B-coordinate = E_A + E_B,
E_T-coordinate = E_A.
```

The displayed source variation is the independent translation injection
`delta B=0`, `delta T=alpha`.  Consequently a term depending only on the
reference connection `B`—or on metric/section data without `A/T` dependence—
annihilates this direction and cannot cancel the live translation equation.
Even choosing its covector to cancel the common diagonal `(delta A,delta B)`
motion leaves `E_T=E_A` unchanged.

This kills the v0.224 successor *as typed*: “derive a background-only Frechet
response and cancel the two shapes” is not available.  It does not kill:

- an independently source-owned term with genuine `A/T` dependence;
- the action-consistent `||E_act||^2` completion;
- an action-derived coupled tangent graph `delta B=L delta T`;
- a justified gauge/BV quotient that removes the transverse directions; or
- a different second-action parent.

## Plain English

We had been asking the geometry in the fixed background to push back against
the Higgs connection variation.  But Eric's two-connection coordinates make
those independent knobs: varying the difference connection while holding the
reference connection fixed does not vary a reference-only background.  It
cannot provide the missing force.

More importantly, the action we called Eric's second action used the wrong one
of three nearby residuals.  The construction did not become useless—it exposed
exactly why the source action now has to be typed before we keep hardening its
vacuum.  The next calculation compares the literal endpoint square with the
variationally consistent Euler square, rather than trying to repair the
path-average surrogate.

## Layer 0

| object | status here | not identified with |
| --- | --- | --- |
| `Fbar` | path-average curvature inside `I1B` | endpoint `F_A` |
| `Upsilon_print` | literal printed first residual and literal `I2B` input | actual derivative of selected `I1B` |
| `E_act` | repo-corrected first-action Euler covector | either raw curvature expression |
| `B` | gauge-rotated reference connection | translation difference `T` |
| `T=A-B` | independently varied source field | a diagonal gauge/Ward motion |
| carrier halves | two `C^(32,32)` Weyl carriers | two independent connection fields |

## Adaptive specialist assessment

- **Variational bicomplex:** the differential of the first action, the printed
  residual, and a bracket inside the integrand are different variational
  objects; only the first is action-owned without an extra choice.
- **Principal-bundle geometry:** `A=B+T` is an invertible change of coordinates,
  not a constraint tying `delta B` to `delta T`.
- **Symplectic geometry:** common gauge/Ward directions test `E_A+E_B`; their
  nullity does not erase the independent `E_T` equation or establish a BV
  quotient.
- **Source criticism:** the draft genuinely displays both the path average and
  endpoint formulas, but their collision must not be repaired by transferring
  the one-third coefficient into `I2B` silently.
- **Analytic/operator:** this is a finite local tangent theorem.  It says
  nothing about a closed domain, spectrum, positivity, or propagator.
- **Contrary path:** a source-owned `A/T` response or derived reduction remains
  a valid conditional escape and should now be tested directly.

## Progress meter

```text
Ledger v0.225 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: background-B-only translation cancellation is unavailable
Frontier reopened: SC-ACT-04 owner is endpoint Upsilon or corrected E_act, not the path-average bracket
```

## Next gate

Assemble the corrected `E_act` residual on the exact moving-`Q_u` bank and
compare `||E_act||^2` with the already-computed literal endpoint square.  Then
ask whether either owner derives a physical tangent reduction.  Do not append
an arbitrary cancellation term or infer that a diagonal Ward identity deletes
the independent translation equation.
