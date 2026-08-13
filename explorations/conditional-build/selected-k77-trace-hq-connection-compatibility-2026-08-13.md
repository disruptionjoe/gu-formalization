---
artifact_type: exact_construction_and_scope_result
created: 2026-08-13
run_id: RUN-20260813-225039-gu-trace-hq-connection-compatibility
status: TRACE_HQ_COMPATIBILITY_EXACT_AND_NONEMPTY__FULL_AND_TWO_HALF_BLOCK_PARENTS_BOTH_ADMITTED__NO_PARENT_OR_HALF_SELECTION
target_claim: NONE-NOT-A-KILL
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 trace-Hq full-connection compatibility

## Result in plain English

The geometry-owned Hermitian form

\[
H_q=iB\gamma(q_g)
\]

is compatible with the complete source-sized connection arena.  It does not,
however, choose between the full `U(64,64)` parent and the block-preserving
description associated with the two complex `C^(32,32)` Weyl halves.

The exact reason is now visible.  The real `Cl(7,7)` monomials form a basis of
all endomorphisms of the real 128-spinor.  For each of the `16,384` monomials
`X`, exactly one of `X` and `iX` is infinitesimally unitary for `H_q`.  The
phase-completed basis therefore spans all of `u(64,64)`:

```text
real-phase Clifford directions       8,256
i-phase Clifford directions          8,128
total                               16,384 = dim u(64,64)
```

The `8,192` even directions preserve the ambient Weyl halves and exactly
saturate

```text
u(32,32) + u(32,32),
```

while the `8,192` odd directions exchange the halves and provide the
complement that enlarges the block algebra to full `u(64,64)`.

Covariant constancy for the moving `H_q` family is also nonempty.  It is an
affine torsor: one exact normal-boost compensator solves `D_varpi H_q=0`, and
every other solution differs by an arbitrary `H_q`-unitary connection.  The
same moving equation has both block-preserving solutions and half-exchanging
full-parent solutions.  Thus `D_varpi H_q=0` constructs a valid compatibility
condition but cannot be the missing action-parent, luminous-half, mirror, or
physical-carrier selector.

## What is new relative to prior art

The 2026-08-12 predecessor correctly computed the fixed-trace split-spin
stabilizer

```text
spin(1,3) + spin(6,3), dimension 42,
```

and the later moving-Hq/Higgs work constructed particular compatible odd and
even directions.  Neither predecessor classified the complete source-sized
`16,384`-dimensional connection algebra or proved that the moving equation
admits both full and block parents.  This wave closes exactly that gap.  It
does not repeat or replace the dimension-42 internal-chain result.

## Exact phase fingerprint

Writing `H_q=iC` with `C=B gamma(q)` real antisymmetric, a real monomial `X`
is admitted when `X^T C=-CX`; otherwise `iX` is admitted when `X^T C=+CX`.
The complete grade counts are:

| grade | real phase | `i` phase | total |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 1 | 1 | 13 | 14 |
| 2 | 78 | 13 | 91 |
| 3 | 286 | 78 | 364 |
| 4 | 286 | 715 | 1001 |
| 5 | 715 | 1287 | 2002 |
| 6 | 1716 | 1287 | 3003 |
| 7 | 1716 | 1716 | 3432 |
| 8 | 1716 | 1287 | 3003 |
| 9 | 1287 | 715 | 2002 |
| 10 | 286 | 715 | 1001 |
| 11 | 78 | 286 | 364 |
| 12 | 78 | 13 | 91 |
| 13 | 13 | 1 | 14 |
| 14 | 0 | 1 | 1 |

This is why a purely real coefficient bank is not the full unitary parent:
it misses `8,128` required phase choices.  It also explains the already-found
Higgs-cell phase rule—real `gamma(q)` is the unique radial real grade-one
direction, whereas the 13 transverse grade-one directions require `i`.

## Moving-family theorem

For a congruence-transported Hermitian family with tangent `dot H`, the
compatibility equation is

\[
\dot H+A^\dagger H+HA=0.
\]

One algebraic representative is

\[
A_0=-\frac12 H^{-1}\dot H,
\]

which at the normalized base point is `-H dot(H)/2`.  The exact probe checks
that the geometric normal boost and `A_0` both solve the equation and differ
by an `H_q`-unitary element.  Therefore the solution set per one-form leg is
an affine space modeled on `u(64,64)`, real dimension `16,384`.  Its
block-preserving affine subspace is modeled on
`u(32,32)+u(32,32)`, dimension `8,192`.

## Layer 0

- `C^(32,32) + C^(32,32)` describes two carrier halves.  It does not by
  itself declare two independent connection fields.
- `U(32,32) x U(32,32)` is the half-preserving subgroup; `U(64,64)` is the
  larger parent that also admits half exchange.
- `D_varpi H_q=0` is compatibility with a Hermitian family, not an Euler
  equation selecting an action parent.
- A block-compatible connection still does not choose one half as luminous or
  remove its mirror.
- Finite Hermitian compatibility is not Krein-positive physical cohomology,
  a closed Dirac domain, a BV quotient, an index, or a generation count.

## Source return and accounting

`SC-GRP-01` and `SC-GRP-02` authorially supply the full `U(64,64)` arena.
Curt's exposition separately supplies two complex `C^(32,32)` Weyl halves.
The checked sources do not identify the repository-constructed trace `H_q` as
the defining source Hermitian form and do not select the block parent, one
half, or a physical cohomology.

No new field, coefficient, datum, quotient, verdict, canon statement, or
public posture is introduced.  `P1/P2/P3` remain unused.  The exact probe
passes `51/51`, including three firing plants.

## Consequence and next gate

Retire `D_varpi H_q=0` as a possible selector by itself.  Keep it as a valid
compatibility requirement.  The next physical-carrier gate must come from the
selected action or physical BV/domain complex: derive a half-asymmetric
cohomology or physical projector on the full fermion carrier and test it
against `W`, mirror, planted random `192`s, `H640`, and `832`.  A fitted
projector, a freely selected member of the affine compatibility fibre, or a
mere choice of block parent is not admissible.
