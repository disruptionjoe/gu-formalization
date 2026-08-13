---
artifact_type: build_result_and_scope_split
created: 2026-08-08
status: ACTION_NORMAL_EULER_MIXED_HESSIAN_EXACT__FULL_K77_COEFFICIENT_SPECIALIZATION_OPEN
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 source-native normal Euler jet

## Result in plain English

The selected action does determine what its missing normal Euler jet **is**:
it is the mixed second derivative of the action, once in a normal
metric-section direction and once in a dynamical field direction.

That sounds modest, but it closes an important ambiguity. The missing object
is not a second observation field, not an arbitrary ambient extension, and not
an external datum. It is a polynomial in the already-owned ambient field jets
and moving geometric coefficients.

For the selected first action, write schematically

```text
I_s(B,T) = rho_s <T_s, S_s(barF(B_s,T_s))>_{G_s}
           + (kappa_1/2) <T_s,*_s T_s>.
```

If `n` is one of the ten normal metric-fibre directions, then

```text
N_B(n)       = D_n E_B       = D_n D_B I,
N_T(n)       = D_n E_T       = D_n D_T I,
N_epsilon(n) = D_n E_epsilon.
```

An exact noncyclic rational fixture differentiates all connection and epsilon
directions and verifies these identities as mixed action Hessians. Seven
normal-owner classes are independently live and their sum exactly exhausts
the normal Euler pair:

1. the normal jet of `B`;
2. the normal jet of `T=A-B`;
3. density motion;
4. target/Krein-pairing motion;
5. the left Shiab leg;
6. the right Shiab leg; and
7. Hodge/mass-pairing motion.

Freezing any one changes the answer. The action-owned epsilon companion also
has a live normal jet and is not either sign of a naive covariant derivative
of the `T` Euler jet.

The remaining boundary is now smaller and honest. The repository has built
the derivative owners for these classes in separate exact artifacts, but it
has not assembled their **coefficientwise full K77 specialization in one
selected action operator**. Therefore this wave constructs the universal
normal-Euler functor and a complete firing fixture; it does not yet claim the
final `14`-dimensional coefficient bank or antisymmetrized presymplectic class.

## 1. Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| printed normal residual jet | `D_n Upsilon_print` | `D_n E_action`, because the printed endpoint is not the selected noncyclic action derivative |
| normal Euler jet | mixed Hessian `D_n D_field I` | a freely chosen normal correction |
| dependent ambient jet | first jet of an already-owned field on `Y` | a new action field or external datum |
| numerical value | evaluation on a chosen background field germ | the differential operator determined by the action |
| complete-germ insertion | lossless local transport of the normal packet | coefficientwise global K77 descent |
| Green potential | field-space one-form from first variation | antisymmetrized presymplectic current or BFV class |

The distinction between an operator and its value matters. An action can
determine the formula for `D_n E` without selecting a particular ambient
solution jet. Supplying initial/boundary data for a solution is not the same
as adding an unexplained coupling or a new external datum to the theory.

## 2. Source return

The 2021 draft prints the residual/prolongation pair

```text
Upsilon_print,
Xi_print = D_omega Upsilon_print.
```

The source does not print the mixed Hessian of the action-selected
Fréchet-adjoint Euler operator. Repository archaeology is decisive here:
K77-B3 and the eddy/action variation wave already show that the printed
endpoint is not the selected noncyclic action derivative. The present exact
fixture confirms that even their normal jets differ.

```text
SOURCE-CONFIRMS:
  the printed residual and its covariant prolongation.

REPO-DERIVES:
  the action normal Euler jet is the mixed action Hessian, including all
  moving field, density, pairing, Shiab and Hodge owners.

SOURCE-SILENT:
  the coefficientwise full-K77 specialization of that mixed Hessian and its
  antisymmetrized observation Green current.
```

## 3. Exact construction

On a moving noncyclic matrix fixture, define

```text
barF(C,T) = C^2 + 1/2(CT+TC) + 1/3 T^2,
S_s(X)    = L_s X R_s.
```

The action contains moving density `rho_s`, target pairing `G_s`, and
Hodge/mass pairing `H_s`. Entrywise differentiation produces `E_C(s)` and
`E_T(s)`. Direct differentiation in the normal parameter gives

```text
E_C_normal =
[[36,      457/5, 50],
 [21/2,     -1/2, 263/5],
 [351/10,  406/5, 447/10]]

E_T_normal =
[[109/15, 5849/105,   788/35],
 [94/7,   8467/210, 15361/210],
 [2159/35,8833/105,  6679/105]].
```

For every one of the nine matrix-unit field directions `H`, independently,

```text
tr(H E_C_normal) = D_n (D_C I[H]),
tr(H E_T_normal) = D_n (D_T I[H]).
```

Two dense held-outs pass as well. Decomposing the normal motion into the seven
owner classes gives seven nonzero contributions whose matrix sum is exactly
the total pair. This is the required nonvacuity and surplus control: the
formula is not being satisfied by zero terms or by a permissive carrier.

The primitive epsilon variation is differentiated separately on all nine
epsilon directions. Its normal companion is live and differs from both signs
of the naive commutator derivative of `E_T_normal`.

Finally, the resulting `27` connection/epsilon coefficients insert into a
nontrivial unipotent complete observation germ with determinant one and are
recovered exactly by the inverse. This specializes the v0.65 universal
receiver with an explicit normal Euler packet rather than a placeholder.

Independent Sage over `QQ` reproduces both displayed matrices, their ranks,
the seven-owner sum, dense mixed-Hessian checks, and rejection of the printed
residual transfer.

## 4. What is and is not now built

Built at exact formal-variational grade:

- the definition and computation of the normal Euler jet as `D_n D_field I`;
- the complete seven-owner decomposition;
- exact connection and epsilon mixed-Hessian identities;
- proof that no new field, coefficient, selector or external datum is needed
  to type the object; and
- lossless insertion of an explicit normal packet into the complete-germ
  receiver.

Still open:

- assemble the seven owner classes coefficientwise on the complete real K77
  selected Shiab/action carrier;
- include the actual ten normal directions and their section/field
  prolongations in one bank;
- differentiate the full K77 preboundary potential on the same bank;
- antisymmetrize, then test basicness, polarization and common-domain descent;
- construct any reduced BFV phase space or physical charge.

This is a real construction step, not a claim that the coefficient expansion
has already been performed. It converts “missing normal jet” into a finite
assembly specification with seven typed input families.

## 5. Symplectic and specialist review

- **Symplectic geometry:** a mixed Hessian is exactly the correct precursor
  to the antisymmetrized Green current. The order is action Hessian, complete
  Green potential, antisymmetrization, basicness, then reduction.
- **Differential geometry:** normal field jets live in the first jet bundle of
  existing ambient fields; they are not a second copy of the metric section.
- **Variational PDE:** equality with the mixed scalar-action derivative on all
  basis directions is stronger than a rank or support match.
- **Krein/operator theory:** the target pairing is allowed to move and remains
  indefinite; no positivity or closed-domain inference is made.
- **Representation theory:** the exact result is a universal coefficient
  module plus a noncyclic realization, not the full K77 representation bank.
- **Source criticism:** the printed residual jet is retained as a rival and
  explicitly rejected as a substitute for the action jet.
- **Exact computation:** SymPy and Sage/QQ agree; seven deletion plants fire.

Both standing hostile charges fire:

1. **Summary outruns artifact:** “the K77 normal jet is complete” is rejected.
   The universal action-owned functor is complete; the full K77 coefficient
   specialization is not.
2. **Artifact defends a superseded object:** `D_n Upsilon_print` is rejected as
   the target because its zero-order endpoint was already superseded as the
   selected action derivative.

## 6. Progress and next gate

```text
Ledger v0.66 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - action-normal jet is typed as the mixed action Hessian
  - seven normal-owner classes are complete and independently live
  - dependent normal field jets require no new action field or external datum
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - coefficientwise full-K77 seven-owner specialization
  - antisymmetrized Green/basic/common-domain/BFV descent
```

P1/P2/P3, verdicts, residue, quotients, canon and public posture remain
unchanged.

Next:

`FULL_K77_SEVEN_OWNER_NORMAL_EULER_BANK__THEN_ANTISYMMETRIZE_COMPLETE_GREEN_POTENTIAL`.

Main probe: `49/49 PASS`. Independent Sage/QQ: `PASS`.
