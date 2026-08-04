---
artifact_type: source-extraction
status: source
doc_type: primary-source-extraction
created: 2026-08-04
title: "Rendered primary-source extraction: GU 2021 draft section 9.3, equations 9.16--9.20"
grade: "VERBATIM EQUATION TRANSCRIPTION WITH SOURCE/CONSTRUCTION FENCES; no global adjoint, domain, physics, or generation theorem is certified by extraction"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# GU draft section 9.3: the four-field fermion operator

## Provenance and method

The source is the official April 1, 2021 Author's Working Draft v1.0:

`https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf`

- SHA-256:
  `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.
- Size/page count: 2,087,649 bytes; 69 pages.
- The hash exactly matches the prior repository receipt.
- Equations 9.16--9.20 were read visually from rendered PDF page 46 at 200
  dpi and checked against Poppler's layout-preserving text extraction. The
  rendered page, not the fragmented text layer, controls signs, row order,
  stars, bars, and the southeast quadrant.

This closes the earlier identity-grade source-extraction gap. It does not
turn the displayed candidate into a unique or globally defined operator.

## Fields and order

The draft says that at classical level the barred and unbarred fields are
**four distinct fields**. It places

```text
nu, bar-nu     in Omega^0(Y,S)
zeta, bar-zeta in Omega^1(Y,S).
```

The displayed bilinear has row order

```text
(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus) rho(epsilon)
```

and column order

```text
(zeta-plus, zeta-minus, nu-plus, nu-minus)^T rho(epsilon^-1).
```

The reversal is load-bearing. It is consistent with an opposite-half
pairing but is not itself a proof of the global Krein adjoint.

## Equation 9.16

Using `odot` for the draft's Shiab/contraction glyph and `varpi` for its
connection one-form, the displayed matrix is

\[
\mathscr D_\omega=
\begin{pmatrix}
*\odot\varpi_{++} & *\odot(d_0+\varpi_{+-})
  & \varpi_{++} & d_0+\varpi_{+-}\\
*\odot(d_0+\varpi_{-+}) & *\odot\varpi_{--}
  & d_0+\varpi_{-+} & \varpi_{--}\\
-\bar\varpi_{++}^{*} & -d_0^{*}-\bar\varpi_{+-}^{*}
  & 0 & 0\\
-d_0^{*}-\bar\varpi_{-+}^{*} & -\bar\varpi_{--}^{*}
  & 0 & 0
\end{pmatrix}.
\]

Machine-readable cell ledger, in row-major order:

```text
star-odot-varpi-pp
star-odot-d0-varpi-pm
varpi-pp
d0-varpi-pm
star-odot-d0-varpi-mp
star-odot-varpi-mm
d0-varpi-mp
varpi-mm
minus-bar-varpi-pp-star
minus-d0-star-bar-varpi-pm-star
southeast-zero
southeast-zero
minus-d0-star-bar-varpi-mp-star
minus-bar-varpi-mm-star
southeast-zero
southeast-zero
```

The `rho(epsilon)` factors wrap the matrix on the barred and unbarred sides.
They are a displayed covariance ansatz. The draft does not prove overlap
descent or identify these factors with the active real-K77 transition group.

## The southeast fork is explicit

Immediately after equation 9.16 the draft says other versions exist with a
**"non-trivial map in the lower right quadrant"**. Therefore:

- `SE=0` is the displayed 2021 candidate;
- the 2025 TOE conversation at `02:38:12--02:43:30` again treats the
  southeast zero as the expected seesaw shape, but prospectively;
- `SE!=0` is explicitly source-admitted;
- neither source supplies a uniqueness theorem or selects the nonzero map.

The source-preferred construction branch keeps zero. A parameterized nonzero
branch remains a rival and must satisfy the same pairing, descent, action, and
domain tests.

## Equations 9.17--9.20

Equation 9.17 abbreviates the four-field display as a Dirac-like fermion
equation on `chi=(zeta,nu)`, with the right `rho(epsilon^-1)` action. Nearby
prose assigns to `chi` observed-fermion, looking-glass, dark-spinorial, and
Rarita--Schwinger content, while the components of `varpi` are said to host
gauge, Higgs-like, CKM, and Yukawa functions. These are source assignments,
not derivations of the corresponding observed equations.

Equation 9.18 places an **outer Hodge star around the entire column** and
assembles a fermionic Euler residual from three displayed classes:

```text
Upsilon_F = star (
  d_A nu + star-odot d_A zeta
  direct-sum d_A^* zeta
  direct-sum bar-nu zeta + bar-zeta nu + odot(bar-zeta,zeta)
)
```

Equation 9.19 places those classes schematically in

```text
Omega^(d-1)(Y,S) + Omega^d(Y,S) + Omega^(d-1)(Y,ad).
```

Equation 9.20 then places the bosonic and fermionic residuals in one total
Euler system. This supports an action-first, no-separate-current-bridge
architecture. It does not supply the missing density, global adjoint,
boundary condition, or closed domain.

## Source-collision disposition for the present gate

| gate object | collision status | implication |
|---|---|---|
| four independent barred/unbarred fields | `SOURCE-STATES` | do not replace the bars by an adjoint before constructing a reality condition |
| signed four-by-four block matrix | `SOURCE-DISPLAYS-CANDIDATE` | use the exact displayed order and signs as the primary candidate |
| southeast zero | `SOURCE-DISPLAYS-2021 / REITERATES-PROSPECTIVELY-2025` | primary branch, not uniqueness |
| nonzero southeast rival | `SOURCE-ADMITS-UNSPECIFIED-RIVAL` | keep separately parameterized |
| Hodge, Shiab, split pairing, formal-star ingredients | `SOURCE-DISPLAYS-INGREDIENTS` | ingredients exist |
| global Hodge/Krein/reality adjoint | `SOURCE-SILENT` | construction required |
| Green preboundary current | `SOURCE-SILENT` | construction required |
| common variational domain | `SOURCE-SILENT` | construction choice required |
| closed physical evolution domain | `SOURCE-SILENT` | downstream Wave-5 problem |
| three kinematic family-shaped pieces | `SOURCE-ASSERTS-WITH-HEDGES` | representation/provenance claim only |
| three observed chiral families | `SOURCE-ASSERTS-WITH-HEDGES / DOES-NOT-DERIVE` | observation, quotient, vacuum, and index still required |

## Layer-0 result

1. The **draft bilinear** is a local Lagrangian/integrand candidate involving
   independent barred and unbarred variables. The source does not supply its
   density lift.
2. A proposed **density-dual operator** is a construction that types the
   bilinear as `E -> E!` after adding Hodge/Krein/density data.
3. A **formal Krein adjoint** is an integration-by-parts construction after
   density, bundle pairing, Hodge, reality, and connection are frozen.
4. A **common variational domain** is a product field space on which the
   action can be differentiated and its boundary current stated.
5. A **closed physical evolution domain** is an analytic realization with
   boundary/constraint/evolution properties. It is not item 3.
6. A **three-family index** is an observed equivariant spectral/cohomological
   statement. It is not the three-piece `Omega0 / chosen gamma-trace
   complement / ker Gamma` decomposition.

These six objects are related but not interchangeable.

## Honest boundary

This extraction closes the source identity of equation 9.16. It does not
prove that its stars are the K77 Krein formal adjoints, that its matrix
descends globally, that a physical boundary condition exists, or that any
of its representation pieces is an observed chiral family.
