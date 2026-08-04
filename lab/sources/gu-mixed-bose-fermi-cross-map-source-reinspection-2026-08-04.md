# GU mixed Bose--Fermi cross-map source reinspection

Date: 2026-08-04
Lane: Eric-guided real-`Cl(7,7)` K77 construction
Purpose: mandatory primary-source collision and visual equation audit before
stabilizing the mixed cross maps requested by the preceding Wave-2 gate.

## Layer 0: what equation 10.10 actually diagrams

The visual source does **not** display an endomorphism of one carrier
`B plus F`. It displays a three-term deformation/Euler complex:

\[
 C^0\xrightarrow{\delta_1}C^1\xrightarrow{\delta_2}C^2,
\]

with the visible node types

\[
\begin{aligned}
C^0&=\Omega^0(\operatorname{ad}),\\
C^1&=\Omega^1(\not S\oplus\operatorname{ad})
      \oplus\Omega^0(\not S\oplus\operatorname{ad}),\\
C^2&=\Omega^{d-1}(\not S\oplus\operatorname{ad})
      \oplus\Omega^d(\not S).
\end{aligned}
\]

Thus the second arrow lands in density-dual/Euler slots, not back in the field
carrier. Its mixed linearizations have the raw types

\[
 U_{\rm raw}:B\longrightarrow F^!,\qquad
 V_{\rm raw}:F\longrightarrow B^!.
\]

They become composable field maps only after constructing pseudo-musical maps
`R_F:F! -> F` and `R_B:B! -> B` from the moving Hodge, Krein pairing and
density. An identity between coordinates is not such a construction.

## Visual receipt

The author PDF used in this swing is `/tmp/gu-working-draft-2021.pdf`, with
SHA-256

```text
3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4
```

Printed pages 47--49 were extracted with layout preservation; printed page 49
was rendered and inspected at high resolution. The visual audit confirms:

- equation `10.5` states `delta_2^omega circle delta_1^omega = Upsilon_omega`;
- equation `10.10` has the five node types listed above;
- visible mixed cells contain `zeta`, `nu`, barred `zeta/nu`, `d_A^omega`,
  `Ad_epsilon`, Hodge/adjoint labels and `kappa_2`;
- the page calls the diagram inherited, potentially inconsistent until
  stabilized, and adds “Caveat Emptor.”

## Source collision ledger

| source | locator | statement relevant to this gate | disposition |
|---|---|---|---|
| 2021 draft | printed p. 47, eqs. `10.1--10.3` | deformation complex is symmetry tangent to field tangent to equation tangent | `SOURCE-CONFIRMS-RECTANGULAR-TOPOLOGY` |
| 2021 draft | printed p. 48, eqs. `10.4--10.5` | mixed spinors enter the full Euler residual and `delta_2 delta_1` is identified with that residual | `SOURCE-CONFIRMS-MIXED-EULER-ARCHITECTURE` |
| 2021 draft | printed p. 49, eq. `10.10` | mixed `/S plus ad` field and Euler nodes with background-spinor cross labels | `SOURCE-DISPLAYS-RAW-MIXED-CELLS` |
| 2021 draft | immediately after `10.10` | diagram may be inconsistent until stabilized | `SOURCE-BLOCKS-STABILIZED-GLOBAL-PROMOTION` |
| Portal/Oxford 2020 | `01:47:01--02:03:07` | Bose and Fermi complexes should meet through up/back and crossed paths; signs and cancellations remained unfinished | `SOURCE-CONFIRMS-ARCHITECTURE__SOURCE-SILENT-ON-PRIMALIZERS` |
| TOE 2025 | `02:44:06--02:45:13` | a tentative unreleased two-connection cyclic square is recalled | `SOURCE-BOUNDS-RIVAL-TARGET` |

## Common-action consequence

For a common scalar action

\[
S_F(b,\zeta,\bar\zeta)
=\langle\bar\zeta,F(b)\zeta\rangle,
\]

the mixed Hessian supplies both raw directions:

\[
\delta_bE_{\bar\zeta}= (\delta_bF)\zeta,
\qquad
\delta_{(\zeta,\bar\zeta)}E_b
=\langle\delta\bar\zeta,(\partial_bF)\zeta\rangle
 +\langle\bar\zeta,(\partial_bF)\delta\zeta\rangle.
\]

Their reciprocity is a Helmholtz/mixed-Hessian identity. It constructs the
raw cross blocks without a separate bridge equation. It does **not** select a
trace-`q` coefficient, construct the global primalizers, identify an observed
Yukawa map, or make the later two-connection grading identical to the
Bose--Fermi grading.

## Existing-repo collision

`explorations/hourly-cycles/hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md`
already typed all five nodes and seven visible arrow families. Its scoped
question was whether any cell supplied a pure Rarita--Schwinger minus-one
source rule; the answer was no. The present result does not reverse that
finding. It reuses the same mixed-cell inventory for a different, action-
Hessian question.

## Source boundary and next object

The sources support the mixed deformation/Euler topology and motivate a common
action. They do not supply global maps

\[
R_F:F^!\to F,\qquad R_B:B^!\to B
\]

or a comparison functor from the two-connection complex to the common
Bose--Fermi Euler complex. Those are constructions, not external data.
