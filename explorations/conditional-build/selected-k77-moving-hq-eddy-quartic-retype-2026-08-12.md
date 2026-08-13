---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
grade: EXACT_SCOPED_MOVING_HQ_UNITARY_PHASE_AND_MINIMAL_J_EDDY_QUARTIC_CARRIER
canon_verdict_change: none
---

# Selected K77 moving-Hq eddy-quartic retyping gate

## Result first

The four-real weak-doublet carrier survives, and the 90-dimensional arbitrary
kernel fit is no longer the nearest constructive route.

Two corrections make the difference.

First, relative to the exact Hermitian form

\[
H_q=iB\gamma(q),
\]

the four fixed-unitary Clifford coefficients do not all carry the same real
phase.  The unique phase pattern tested here is

\[
C_q(v)=v_{\parallel}\gamma(q)+i\gamma(v_{\perp}).
\]

Thus the radial cell is `gamma(q)`, while the three angular cells are
`i gamma(H_perp)`.  Each lies exactly in `u(H_q)`.  The opposite phase choices
fail with full-rank defect.  This corrects the loose “all-real full-unitary
bank” wording in v0.198 without changing its common-leg curvature-zero result.

Second, the already-present orthogonal complex structure `J` fixes the
smallest invisible second leg.  In the one-parameter family

\[
L_c(H)=H\theta_q+c\,JH\theta_{Jq},
\]

the observed soldering output is `H` for every `c`, but `[L_c(H),J]=0` for all
four weak basis directions if and only if `c=1`.  No coefficient is fitted.
The resulting two-leg connection candidate has quadratic eddy

\[
(\theta_q\wedge\theta_{Jq})
[C_q(H),C_q(JH)]
\]

and the complete exact coefficient polynomial is

\[
\left\|[C_q(H),C_q(JH)]\right\|_F^2
=512\,(h_1^2+h_2^2+h_3^2+h_4^2)^2.
\]

This is a nonzero, positive, weak-doublet-invariant algebraic **quartic carrier**
conditional on the existing `J` reduction.  It is not yet the
physical Higgs potential.

## Plain English

The previous wave found the right four-component field but lifted all four
components along one geometric direction.  That necessarily made the
self-interaction zero.  The geometry already contained a second natural
direction, `Jq`.  Requiring the lift to respect the same complex structure
fixes that second direction with coefficient one.  Once it is included, the
quadratic eddy is nonzero and its square has exactly the rotationally symmetric
quartic shape needed for a Higgs-like potential.

The important restraint is that we have built the bowl-shaped quartic part,
not the Mexican hat.  The selected action still has to provide the physical
contraction and normalization, a negative/background-induced quadratic term,
a nonzero stationary amplitude, one surviving radial mass, three eaten orbit
directions, the photon kernel and Yukawa placement.

## Layer 0

| object | type | status |
| --- | --- | --- |
| `C_q(H)` | fixed-`H_q` odd unitary Clifford coefficient | exact |
| spin compensator `-gamma(H)gamma(q)/2` | even tangent connection moving `q` and `H_q` | exact, distinct from `C_q(H)` |
| `L_1(H)` | `J`-linear two-leg soldering lift | exact in the minimal family |
| quadratic eddy | algebraic `T wedge T` coefficient | exact for the candidate lift |
| coefficient Frobenius norm | finite positive quartic polynomial | exact |
| selected GU Higgs potential | Shiab/Hodge/Krein contracted action term | open |
| physical vacuum and spectrum | stationary Euler/Hessian result | open |

The three angular field directions coincide with the compact `q` orbit, but
they are not the even spin compensators that move the frame.  The former are
odd candidate Higgs coefficients; the latter are grade-two connection terms.

## Exact phase gate

For the three weak directions perpendicular to `q`, real `gamma(H)` has a
full-rank fixed-`H_q` unitary defect, while `i gamma(H)` has zero defect.  The
radial behavior reverses: real `gamma(q)` has zero defect and `i gamma(q)` has
full-rank defect.  Hence the complex phase is forced cell-by-cell by the same
Hermitian geometry; it is not an arbitrary convention.

This also explains why a purely real Clifford calculation could locate the
carrier yet mistype its unitary admission.  The relevant action parent is the
source-sized complex unitary bundle, with the full `U(64,64)` form and its two
`U(32,32)` half restrictions kept distinct.

## Moving-reduction check

For each of the three angular orbit directions `H`, the even spin generator

\[
S_H=-\frac12\gamma(H)\gamma(q)
\]

satisfies

\[
[S_H,\gamma(q)]=\gamma(H)
\]

and the full first variation of the moving `H_q` family vanishes.  Freezing
`H_q` makes the same generator fail the fixed-unitary test.  This is the exact
principal-bundle distinction between a connection adapted to a moving
reduction and an odd coefficient inside the resulting unitary parent.

## Constraint surplus and selection cost

Within the minimal two-leg family there was one unknown coefficient `c` and
the `J`-linearity equations force `c=1`; the resulting quartic polynomial then
satisfies all fifteen nontrivial degree-four coefficient conditions of a
single `U(2)`-radial invariant.  The fit therefore has positive surplus in
this restricted family.

```text
new fields: 0
new coefficients: 0 after J-linearity
new external datum: 0
P1/P2/P3 consumed: 0
remaining selection: one J from the existing 20-dimensional family
```

This does not prove uniqueness among every possible 90-dimensional kernel
lift.  It proves that the smallest `J`-compatible completion is unique and
works without selecting arbitrary kernel coordinates.

## Source and prior-art boundary

The general augmented-torsion eddy and its action Euler were already present
in the repo.  What is added here is the exact moving-`H_q` phase map and its
restriction to the previously constructed four-real weak doublet, followed by
the coefficientwise `J`-completed quartic certificate.  The source confirms
the eddy/quartic route and remains silent on this identification.

## Symplectic and analytic boundary

The Frobenius norm is a finite coefficient diagnostic.  It is not the
presymplectic form, the physical Hamiltonian, a Krein-positive energy, or the
selected Shiab/Hodge contraction.  No BV generator, boundary charge, quotient,
Green identity, closed domain, index or spectrum is obtained.

The physical sign and stability cannot be inferred from `512>0`.  A nonzero
vacuum requires a competing quadratic term and the full action Euler.  The
source's curvature-driven VEV suggestion is therefore the next action-level
test rather than a conclusion of this wave.

## Ledger effect and next gate

Three rows move in distance/evidence only: `RA-E1`, `RA-E3`, and `LT-SM6`.
Coverage, verdict counts, residue, five scoped quotients, P1/P2/P3, canon and
public posture do not move.

The next gate is now narrower:

1. insert this `J`-completed augmented-torsion candidate into the actual
   selected first-order action, including moving Shiab/Hodge and the
   Frechet-adjoint Euler term;
2. derive the physical quartic coefficient and the curvature/background
   quadratic term rather than importing a Mexican hat;
3. solve the four-real stationary equation and Hessian, requiring three gauge
   orbit directions, one radial scalar, a photon kernel, and no fitted kernel
   coordinates; and
4. only then port the lower-order Yukawa and fermion blocks.

The exact probe passes `61/61` after the predecessor chain.
