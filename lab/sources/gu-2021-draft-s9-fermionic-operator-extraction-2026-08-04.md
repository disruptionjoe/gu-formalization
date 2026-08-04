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

The candidate status is explicit. Section 9.3 says the fields can **"begin
with operators like"** equation 9.16. Section 8 is titled **"The Family of
Shiab Operators"**; section 8.2 says the author cannot locate the historical
calculation selecting the operator of choice. The later deformation diagram,
equation 10.10, is labeled as inherited from an older version and possibly
inconsistent. Thus the draft supplies a construction-bearing matrix grammar,
not a unique stabilized fermion operator.

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

This is an identity-grade ledger of all sixteen displayed cells. It does not
define the plus/minus grading or prove that those labels are ambient spin
chirality.

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

## Successor source collision: equation 9.16 versus section 11.2 signs

Rendered PDF page 51 supplies a second identity-grade locator that must travel
with equation 9.16.  In the rolled fermionic diagram it places

```text
zeta_minus in Omega1(S_minus)
zeta_plus  in Omega1(S_plus)
nu_plus    in Omega0(S_plus)
nu_minus   in Omega0(S_minus).
```

The `plus/minus` field glyphs are therefore ambient half-spinor labels in
section 11.2.  They cannot silently be redefined as the product of form parity
with ambient chirality.

This exposes a precise construction fork.  The real-K77 rolled symbol already
built in the repository has three principal classes:

```text
Phi d on Omega1: flips ambient J;
d from Omega0 to Omega1: preserves ambient J;
-d-times from Omega1 to Omega0: preserves ambient J.
```

Yet the equation-9.16 derivative cells apply the first two classes to inputs
with the same displayed sign and place them in rows with the same displayed
sign.  Under either natural uniform convention for barred rows--a dual of the
same half or a vector representative paired with the opposite half--those two
classes must have the same ambient-J parity.  The selected gamma-contraction
and exterior derivative do not.

The product grading

```text
G = (-1)^form J
```

does make all three principal classes odd and reproduces the six derivative
cell locations after reversing the one-form labels.  It is a coherent
**conditional rival**, but that reversal conflicts with the identity-grade
section-11.2 field labels.  The present disposition is therefore:

- section-11.2 field signs: `SOURCE-STATES-AMBIENT-HALF-SPINOR`;
- six equation-9.16 derivative-cell locations: `SOURCE-DISPLAYS`;
- auxiliary total grading: `CONSTRUCTION-WORKS-AFTER-ONE-FORM-RELABEL`;
- identification of that relabeling with the source glyphs:
  `LAYER0-COLLISION / NOT-ESTABLISHED`;
- source-faithful parity or duality convention reconciling the selected
  `Phi d`, `d`, and `-d-times`: `OPEN`.

This is narrower than saying equation 9.16 is inconsistent.  A different
Shiab contraction, a degree-dependent duality/reality map, or a corrected
source sign convention may repair it.  Each is a different construction and
must be written explicitly.

## Earlier provisional total-grading reading (superseded)

The rendered matrix puts `d0` or `d0-star` in exactly six cells:

```text
(row,column), zero-indexed:
(0,1), (0,3), (1,0), (1,2), (2,1), (3,0).
```

That placement is source data.  The earlier provisional interpretation was
that, on the real K77 rolled carrier, the product grading

```text
G = (-1)^form J
```

makes `Phi d_A`, `d_A`, and `-d_A-times` all odd. Ambient spin chirality `J`
alone makes only `Phi d_A` odd and gives the wrong support for the other four
derivative cells.  Page 51 shows that the source **does** contradict using
`G` as the meaning of its field subscripts unless the one-form labels are
explicitly corrected or reinterpreted.  The repaired disposition is:

- six derivative-cell locations: `SOURCE-DISPLAYS`;
- `G=(-1)^form J`: `CONSTRUCTION-SELECTED-RIVAL`;
- identifying source plus/minus with ambient `J`: `SOURCE-STATES`, while its
  compatibility with the selected gamma-contraction remains open;
- identifying equation 9.16 uniquely with the 2025 unreleased cyclic
  operator: `FORBIDDEN`.

The same distinction applies to `rho(epsilon)`. The source displays active
conjugation. A moving Clifford, chirality, pairing, and contraction orbit is a
construction that can realize that conjugation; it is not a quotation that
the draft already proved global descent.

## Honest boundary

This extraction closes the source identity of equation 9.16. It does not
prove that its stars are the K77 Krein formal adjoints, that its matrix
descends globally, that a physical boundary condition exists, or that any
of its representation pieces is an observed chiral family.

## Successor collision: the released 2025 spoken explanation

The repository transcript of Weinstein's 2025 conversation with Curt
Jaimungal narrows the middle-arrow grammar without correcting the sign
collision above.

- At `02:38:12--02:39:51`, Weinstein starts from a de Rham complex tensored
  with a connection and describes rolling `d_A+d_A^*` after curvature spoils
  `d_A^2=0`.
- At `02:40:30--02:42:55`, he says the truncated sequence is
  `0 -> 1 -> 13 -> 14`: a two-form is **contracted back to a one-form and
  then starred**.  He explicitly associates the southeast zero of the rolled
  two-by-two operator with a possible seesaw mechanism.
- At `02:44:06--02:45:13`, he describes a different cyclic `D^2` construction,
  says that it has never been released, and recalls its entries and signs
  tentatively.

This is `SOURCE-CONFIRMS` for the contraction-plus-star grammar and the
importance of the southeast-zero branch.  It is `SOURCE-SILENT` on an
ambient-half-spinor relabel or a correction to equation 9.16.  The unreleased
cyclic construction cannot repair the released matrix by implication.

```text
SOURCE-CORRECTS-SIGNS: NONE FOUND
```

The draft's own section 8 also makes the parity issue structural for the
simple native contraction.  Its `Phi_r` are invariant differential-form /
Clifford tensors, and the `2 -> 1` map uses the invariant one-form `Phi_1`.
Conjugating `Phi_1` and ambient chirality by the same `epsilon` preserves their
relative odd parity.  An ambient-even replacement therefore requires either
a different non-native tensor grammar or an additional moving odd tensor; it
does not follow merely from writing `rho(epsilon)`.
