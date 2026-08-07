---
artifact_type: conditional_build_result
created: 2026-08-07
status: FIXED_B_TRANSLATION_CURVATURE_PARTIAL_OWNER_EXACT__TRANSVERSE_MOVING_SOLDERING_OWNER_OPEN
source_return: SOURCE-CONFIRMS__T_CONNECTION_DIFFERENCE_AND_DB_T_TRANSLATION_CURVATURE__SOURCE-SILENT__RICHER_MOVING_SOLDERING_COEFFICIENTS
ledger: lab/process/conditional-physics-ledger-v0.51.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer translation-curvature principal owner

## Result in plain English

The written GU augmented-torsion geometry owns a genuine part of the exact
odd packet found in v0.48, but not all of it.

At a fixed reference connection `B`, the first-order symbol of the source term
`D_B T` is

```text
delta T  |->  q wedge delta T.
```

For non-null `q=e^0`, that map has rank `182` on the full
`Lambda1 tensor Cl1` carrier. In the selected HN/NN bank it retains `140`
coordinates. Coefficientwise comparison gives:

```text
exact q-containing packet:  7 + 7 + 7 + 7 = 28  — source-owned by D_B T
transverse packet:          51 + 22 + 22 + 22 = 117 — outside im(q wedge)

owned four-column rank:       4
transverse four-column rank:  4
```

Thus fixed-`B` translation curvature is a **partial owner**. It supplies every
coefficient in the canonical connection part and no coefficient in the
transverse part. The next construction is no longer “find any odd owner.” It
is specifically: calculate how the moving gauge-rotated Levi-Civita reference,
moving `epsilon`, or soldering field contributes to the 117 transverse
coefficients.

## Layer 0

| phrase | object tested | kept distinct |
| --- | --- | --- |
| augmented torsion `T` | an adjoint-valued one-form and difference of two connections | its curvature `D_B T + T wedge T` |
| translation-curvature principal symbol | `q wedge delta T` at fixed `B` | lower-order commutators and moving-`B(g)` derivatives |
| owned packet | the 28 q-containing Cl1-valued two-form coefficients | the 117 transverse coefficients |
| algebraic term | variation of `T wedge T`, differential order zero for independent `T` | an odd first-order principal-symbol extension |
| non-null result | the `q=e^0` selected carrier | the null characteristic screen |
| source ownership | carrier and symbol supplied by the written action | Euler, Helmholtz, Ward, BV, BFV or physical-state closure |

The source confirms the first two connection-curvature ingredients. It does
not print or derive the richer moving-reference coefficients needed for the
transverse family.

## Exact theorem

Let `V` be fourteen-dimensional and fix nonzero `q`. The principal symbol of
the linearization of `D_B T` in `T` is

```text
sigma_q(delta T) = q wedge delta T.
```

For `q=e^0`, the fourteen components of `delta T` whose one-form slot is
parallel to `q` form the kernel. Hence the full image rank is

```text
14 * 14 - 14 = 182.
```

The selected inverse-Shiab bank excludes direct HH exterior pairs. Exactly ten
of its exterior pairs contain `0`, so its retained fixed-`B` image has
`10 * 14 = 140` coordinates. Every one of the 28 canonical connection
coefficients is among those coordinates. Every one of the 117 transverse
coefficients has an exterior pair not containing `0`, so its intersection with
the image support is empty.

This support theorem is stronger than a dimension count. It checks each of the
four exact inverse columns and reproduces ranks four and four on the owned and
unowned families.

## Why `T wedge T` does not fill the gap

When `T` is an independent connection-difference field, `T wedge T` is
algebraic in `T`. Its variation contributes no first derivative of `delta T`
and therefore cannot enlarge the first-order principal image. Moreover the
Clifford product of two odd `Cl1` values is even. The missing packet is odd.

This does not discard the algebraic term from the nonlinear action. It only
excludes it as the missing odd first-order owner.

## What is not killed

A moving reference connection `B(g)`, moving `epsilon`, or moving soldering
field can produce derivatives of additional variables. Those terms are not in
the frozen-`B` principal symbol and are not excluded. Weinstein's
gauge-rotated Levi-Civita prescription therefore remains the leading source
route for the transverse response.

The null branch is also untouched: the non-null Koszul split used to expose
the 28/117 decomposition has no canonical metric-normalized continuation to
`q^2=0` without a screen or gauge quotient.

## Specialist and hostile review

- **Source geometry:** the connection difference and `D_B T` term are
  source-confirmed; the exact moving-soldering coefficients are source-silent.
- **Differential geometry:** `q wedge delta T` is the fixed-reference
  translation-curvature symbol; varying the reference connection is a
  separate tangent contribution.
- **Representation theory:** support and rank are checked on all four exact
  columns; no multiplicity-to-count inference is used.
- **Variational PDE/hyperbolic equations:** the result is a principal-symbol
  owner theorem, not a nonlinear Bianchi or characteristic-domain theorem.
- **Symplectic geometry:** no Euler covector, presymplectic current, reduced
  phase space or BFV structure follows from partial symbol ownership.
- **Krein/operator theory:** positivity, self-adjointness and a common closed
  domain remain open.
- **Repo archaeology:** the older GCR and v0.48 files are used only through
  their typed exact carriers; no `(9,5)` object is ported into K77 by name.

Both standing hostile charges pass after fencing the claim as partial. The
summary does not turn 28 coefficients into 145, and the lane does not continue
hardening the superseded direct-GCR owner.

## Progress and fences

```text
Ledger v0.51 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - fixed-B D_B T principal image constructed exactly
  - all 28 q-wedge coefficients assigned to that source-native owner
  - T wedge T excluded as an odd first-order principal enlargement
frontier_conditions_opened: 0
remaining_named_conditions: 5
  - moving-reference/epsilon/soldering owner for the 117 transverse coefficients
  - null characteristic screen and continuation
  - total nonlinear Bianchi and raw-Upsilon naturality
  - scalar and massless physical constraint quotient
  - coupled fermion Hessian and common domain
```

No verdict, residue, quotient, datum, canon or public posture moves.
P1/P2/P3 remain unused. Curt remains formally separate and no third lane is
promoted.

## Next gate

Compute the principal response of the moving gauge-rotated Levi-Civita
reference and the moving `epsilon`/soldering variables on the same exact
selected carrier. Compare it coefficientwise with the 117 transverse
coefficients. If that closes, combine it with the 28 fixed-`B` coefficients,
then construct the null screen and test total covariant Bianchi and raw
`Upsilon` naturality.

The executable probe passes `45/45`, including the immutable 61-check
predecessor replay and planted failures against full-owner, algebraic-owner,
Euler/BFV, null-screen and datum inflation.
