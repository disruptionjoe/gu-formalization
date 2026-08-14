---
artifact_type: exact_conditional_homogeneous_space_result
created: 2026-08-14
status: ONE_DOUBLET_NORM_PRESERVING_INVOLUTION_QUOTIENT_TRIVIAL__JOINT_W_MIRROR_BOSONIC_ACTION_UNTYPED__FULL_STATIONARITY_OPEN
source_return: SOURCE_CONFIRMS_HIGGS_LIKE_VARPI_ASSIGNMENT_AND_EMERGENT_CHIRAL_TARGET__SOURCE_SILENT_JOINT_W_MIRROR_BOSONIC_INVOLUTION_VACUUM_AND_SELECTION
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 moving-`H_q` vacuum conjugation quotient

## Result first

The cheapest candidate escape from the fixed-background W/mirror theorem does
not work by itself.  The already-built moving-`H_q` Higgs candidate is one
complex weak doublet.  Its pre-Higgs gauge group contains the fundamental
`SU(2)` action, and `SU(2)` acts transitively on every nonzero norm sphere in
`C^2`.  Therefore

```text
C^2 / SU(2)  ~=  R_{>=0},
H             |->  ||H||.
```

Any involution that stays inside this one doublet and preserves its norm acts
as the identity on the quotient.  Ordinary complex conjugation is an exact
witness: for generic `H=(a,b)` the certificate constructs a special-unitary
matrix taking `H` to `bar(H)`.  Thus a complex-looking coordinate
representative does not supply two physically distinct conjugate vacua.

This is directly relevant to both radial potentials already in the repository.
At fixed nonzero radius their stationary set is one `S^3` gauge orbit, so the
stationary quotient is one point:

```text
SC-ACT-04 trace-Hq comparator:       ||H||^2 = -3 rho,
conditional observer-Q_B rival:     ||H||^2 = -3 rho - 9 kappa^2/160.
```

The conclusion is conditional in one important direction and negative in
another.  The repository has not constructed a joint involution on the
bosonic vacuum fields whose fermion part is the exact W/mirror conjugation.
If such an involution stays within this single norm-preserving doublet, the
theorem decides it wholesale: it is quotient-trivial.  If it exchanges a
different carrier copy or changes an additional phase-sensitive invariant,
that is a new construction and remains open.

Neither existing radial branch is promoted to a vacuum.  The trace-`H_q`
branch has fourteen nonzero derivatives in the complete fixed-`H_q`
196-real connection tangent.  The observer-`Q_B` branch is repository-
conditional and its complete moving connection/metric/section variation is
still open.

## Plain English

A Higgs doublet has four real coordinates, so it looks as though choosing a
complex direction might break the symmetry that exchanges matter with its
mirror.  But the weak gauge group can rotate any nonzero vector of a fixed
length into any other.  After removing that gauge redundancy, this candidate
has only one physical coordinate: its length.  Conjugation does not change the
length, so it does not produce a second physical vacuum.

That does not prove GU cannot break the matter/mirror symmetry.  It says the
breaking cannot come merely from the orientation of this one radial Higgs
doublet.  It needs an additional action-owned invariant: for example a
relative phase between two genuinely distinct fields, a coupling between
different carrier blocks, or an asymmetric BV/boundary/domain reduction.

## Exact theorem

For `H=(a,b)` put

```text
A(H) = [[bar(a), bar(b)], [-b, a]].
```

Then `A(H)H=||H||^2 e_1`, `det A(H)=||H||^2`, and for nonzero `H`

```text
g_H = A(bar(H))^{-1} A(H) in SU(2),
g_H H = bar(H).
```

The probe checks these identities over the rational function field
`Q(i)(a_R,a_I,b_R,b_I)` and on three held-out Gaussian-rational vectors.  The
argument is stronger than the displayed conjugation witness: transitivity says
every norm-preserving self-map of the single doublet is trivial on the orbit
quotient.

The nontrivial control uses two doublets.  Their common gauge action preserves
`H_1^dagger H_2`; its imaginary part changes sign under conjugation.  Exact
vectors with values `+i` and `-i` are therefore gauge-inequivalent.  This
control proves that quotienting has not erased conjugation by definition.  It
also does **not** license adding a second Higgs doublet to GU: the action/source
must own any second carrier or cross-block invariant.

## Layer 0

| object | decided here | not decided |
| --- | --- | --- |
| one moving weak doublet | `C^2` with an `SU(2)` fundamental action | every possible `varpi` Higgs-like cell |
| orientation sphere | one nonzero `SU(2)` orbit | physical BV orbit after constraints and boundaries |
| radial quotient | `R_{>=0}` | a selected nonzero radius or physical Higgs spectrum |
| norm-preserving doublet involution | identity on the orbit quotient | action-owned joint W/mirror action on bosons and fermions |
| coordinate conjugates | exactly gauge-equivalent within one doublet | distinct carrier copies exchanged by conjugation |
| two-doublet control | admits a conjugation-odd invariant | a source-owned second GU doublet |
| two ambient `C^(32,32)` halves | source carrier halves | two Higgs doublets or two independent connections |
| radial critical point | restricted one-variable Euler zero | full 196-tangent stationarity |

The last two distinctions prevent the most tempting overreads.  The two
source carrier halves are not two Higgs doublets, and broken gauge
transformations remain gauge redundancies unless a boundary/BFV construction
turns them into physical charges.

## Adaptive specialist close

- **Invariant/homogeneous-space geometry — ACTUAL MATH, very high:** the full
  one-doublet orbit class is decided by transitivity, without sampling a large
  matrix family.
- **Category/Layer 0 — ACTUAL MATH, very high:** a representative, orbit,
  stationary locus and quotient are different objects; W/mirror conjugation
  has no constructed bosonic leg yet.
- **Bifurcation theory — ACTUAL MATH, high:** both current potentials are
  radial, so their nonzero stationary strata reduce to a single orbit class.
- **Variational bicomplex — ACTUAL MATH, very high:** restricted radial
  criticality does not repair the fourteen-cell ambient Euler failure.
- **Real/complex descent — ACTUAL MATH, high:** every norm-preserving
  within-doublet involution descends trivially; a cross-carrier involution is
  a distinct route.
- **Symplectic/BV — ACTUAL MATH, high:** the finite configuration quotient is
  not a reduced phase space, and boundary gauge transformations may require a
  separate BFV treatment.
- **Analytic/PDE — ACTUAL MATH, high:** no domain, Green operator, spectrum or
  stability theorem follows.
- **Source criticism — ACTUAL MATH, high:** the source assigns Higgs-like
  functions to `varpi` and claims emergent chirality, but does not publish this
  doublet, the joint involution, a full stationary vacuum or its selection.

## Progress and next gate

```text
Ledger v0.242 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: the entire norm-preserving one-doublet non-fixed-vacuum class
Frontier remaining: joint W/mirror bosonic action plus phase-sensitive invariant, or asymmetric BV/domain
```

Before another W/mirror Hessian, construct the joint action involution on the
actual bosonic and fermionic field complex.  Compute its invariant ring on the
source-owned stationary carrier.  Continue the vacuum route only if a
conjugation-odd gauge invariant survives the physical quotient and the
complete Euler equations admit a nonzero stationary point.  Otherwise move
directly to an explicitly asymmetric BV/BFV or closed-domain construction.

No field, coupling, datum, residue coordinate, quotient count, P1/P2/P3 use,
canon verdict or public posture changes.  The exact probe passes `43/43` after
the joint-involution typing checks are included.
