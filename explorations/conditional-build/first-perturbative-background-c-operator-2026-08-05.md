---
artifact_type: construction_result
created: 2026-08-05
status: SUPERSEDED_BY_K116_FRAME_MISMATCH__RETAINED_AS_HISTORICAL_PROVENANCE
source_return: SOURCE-SILENT
ledger_rows: [LT-GR2b, LT-GR3, LT-GR5, LT-SM8]
scripts:
  - tests/channel-swings/first_perturbative_background_c_operator_probe.py
  - tests/channel-swings/first_perturbative_background_c_operator_independent.sage
registry: lab/process/first-perturbative-background-c-operator.json
---

# First perturbative background C-operator on the selected TT action

> **K116 FRAME-CONSISTENCY CORRECTION (2026-08-15):** the concrete pencil
> below is superseded. It combines the raw `(h,v)` matrices `K,M0` with the
> eigenmode `(q0,qm)` interaction Hessian `u vv^T`. Use
> `selected-k116-rsap-tt-frame-consistency-correction-and-transport-gate-2026-08-15.md`:
> in one consistent frame `Delta=b(alpha^2 b+4u)`, there is one gap wall, and
> the moving connection is nonzero at `alpha=1`. Retain this file only as the
> provenance record of the historical calculation and its scope ceilings.

## Result first

The previous wave proved that the free TT grading cannot survive the first
action-owned cubic interaction by assigning the scalar field either an even
or odd sign. That was a route kill for multiplicative parity, not a kill of
an interacting metric.

The smallest selected-action gravitational TT field-mixing lift now exists.
At a fixed constant scalar background, the cubic changes the actual
selected-action TT Hessian. On the open distinct-real-spectrum component
connected to the free theory, and for the fixed native Krein form, that
Hessian has a unique positive spectral fundamental symmetry

\[
 C(u)={2L(u)-\operatorname{tr}L(u)\,I\over\sqrt{\Delta(u)}},
 \qquad u=2c\bar\theta,
\]

which exactly:

- squares to one;
- commutes with the background dynamics;
- is self-adjoint in the native Krein form;
- makes `K C(u)` positive definite; and
- reduces to the predecessor's free `P` at `u=0`.

Its first perturbative coefficient is uniquely fixed after the action
coefficients and scalar background are supplied: four matrix entries face a
rank-four linear constraint system, leaving zero C-correction freedom. Thus
the metric correction is not a fitted sign repair; this count does not derive
`alpha`, `b`, `c`, or `bar theta`.

The same calculation exposes the exact limits. Two algebraic walls bound the
free-connected component. A generic wall is a Jordan exceptional point, the
region between the walls has complex-conjugate spectrum, and a second real
component requires the opposite positive orientation. At the special
coincident wall `alpha=1, u=-b`, the dynamics becomes scalar and admits a
continuum of positive fundamental symmetries, so dynamics selects none.

This closes the **first perturbative background-Hessian** horn. The fixed
background is not proved stationary for the complete action, so this is also
not yet a physical-vacuum theorem. It does not construct a nonlinear symmetry
of the complete action, a quantum Fock-space `C`, a common interacting domain,
or loop/UV positivity.

## Layer 0: three different objects

| shared phrase | object | disposition |
| --- | --- | --- |
| background `C` | linear fundamental symmetry of the second variation at fixed `bar theta` | built exactly here |
| nonlinear interacting symmetry | field-dependent transformation preserving the complete classical action | open |
| quantum interacting `C` | linear metric operator on the physical state/Fock space, including domain and amplitudes | open |

The first is a useful local precursor to the latter two, not a proved
necessary-and-sufficient gate or an identification with them. The result uses
the GU-native keep-and-grade Krein
form. Mannheim's pseudo-Hermitian machinery supplies a checked method
precedent, not the ontology. Weinstein's released GU sources are
`SOURCE-SILENT` on this construction.

## Action ownership

On one already-surviving TT polarization the predecessor action gives

\[
 K=\begin{pmatrix}\alpha&1\\1&0\end{pmatrix},\qquad
 M_0=\begin{pmatrix}0&0\\0&b\end{pmatrix},\qquad
 L_0=K^{-1}M_0,
\]

with `alpha>0`, `b>0`, massless vector `(1,0)` and massive vector
`(1,-alpha)`. Its free fundamental symmetry is

\[
 P=I+{2L_0\over\alpha b}
  =\begin{pmatrix}1&2/\alpha\\0&-1\end{pmatrix}.
\]

The first owned cubic is

\[
 V_3=c\theta(q_0+q_m)^2.
\]

At constant `bar theta`, whether or not that off-shell background is later
selected as a stationary solution, its exact TT Hessian is

\[
 D_q^2V_3=u\,vv^T,\qquad
 u=2c\bar\theta,\quad v=(1,1)^T.
\]

Therefore the actual background matrices—not a new toy—are

\[
 M(u)=M_0+uvv^T
 =\begin{pmatrix}u&u\\u&b+u\end{pmatrix},
 \qquad L(u)=K^{-1}M(u).
\]

Since `M(u)` is symmetric, `L(u)` is automatically K-self-adjoint:
`K L=L^T K`.

## Exact spectral construction

The characteristic discriminant factors completely:

\[
 \Delta(u)
 =\operatorname{tr}(L)^2-4\det L
 =(b+u)\left[\alpha^2b+(\alpha-2)^2u\right]. \tag{1}
\]

Away from `Delta=0`, define the numerator

\[
 N(u)=2L(u)-\operatorname{tr}(L(u))I.
\]

Cayley-Hamilton gives `N(u)^2=Delta(u) I`, hence on a chosen real branch
`C=N/sqrt(Delta)`. Direct exact computation gives

\[
 C(u)={1\over\sqrt\Delta}
 \begin{pmatrix}
 \alpha(b+u)&2(b+u)\\
 -2u(\alpha-1)&-\alpha(b+u)
 \end{pmatrix}. \tag{2}
\]

It satisfies

\[
 C^2=I,\qquad [C,L]=0,\qquad C^TK=KC. \tag{3}
\]

The positive-metric numerator is

\[
 \sqrt\Delta\,KC=
 \begin{pmatrix}
 \alpha^2(b+u)-2u(\alpha-1)&\alpha(b+u)\\
 \alpha(b+u)&2(b+u)
 \end{pmatrix}, \tag{4}
\]

with determinant `Delta`. On the component containing `u=0`, both factors in
(1) are positive, so (4) is positive definite and `det(KC)=1`. Positivity
also fixes the overall sign of `C`. There is no extra binary choice once the
Krein anchor and connected component are fixed.

For `alpha,b>0`, the component is

\[
 b+u>0,\qquad \alpha^2b+(\alpha-2)^2u>0. \tag{5}
\]

Every positive `u` lies in it. Negative interaction backgrounds can hit the
walls.

## Unique first perturbative lift

Expanding `C(u)=P+uC_1+O(u^2)` gives

\[
 C_1=
 \begin{pmatrix}
 {2(\alpha-1)\over\alpha^2b}&
 {4(\alpha-1)\over\alpha^3b}\\
 -{2(\alpha-1)\over\alpha b}&
 -{2(\alpha-1)\over\alpha^2b}
 \end{pmatrix}. \tag{6}
\]

It solves the three linearized obligations

\[
 PC_1+C_1P=0,
\]
\[
 [C_1,L_0]+[P,L_1]=0,
\]
\[
 C_1^TK=KC_1.
\]

Writing a general two-by-two `C_1` introduces four coefficients. The combined
linear system has rank four and a unique solution, exactly (6):

```text
free coefficients: 4
independent constraint rank: 4
remaining freedom: 0
```

This is the relevant constraint-surplus result. The correction is selected by
the action Hessian; it was not adjusted after seeing positivity.

## Exceptional-locus classification

Equation (1) gives two walls:

\[
 u=-b,
 \qquad
 u=-{\alpha^2b\over(\alpha-2)^2}\quad(\alpha\ne2). \tag{7}
\]

They have three distinct meanings.

1. **Generic wall: Jordan failure.** A repeated eigenvalue of a nonscalar
   two-by-two matrix has a rank-one square-zero Jordan remainder. No positive
   metric can make such a matrix self-adjoint, because positive-metric
   self-adjoint operators are real diagonalizable.
2. **Between the walls: complex pair.** `Delta<0`; the positive-C construction
   is absent. This is a scoped PT-broken region, not a theory-wide kill.
3. **Beyond both walls: disconnected real branch.** `Delta>0` again, but the
   continuation of (2) makes `KC` negative. The opposite sign supplies the
   positive orientation on that disconnected component. It cannot be reached
   continuously from the free component without crossing a wall.

There is one special collision. When `alpha=1`, both walls coincide at
`u=-b` and `L=-bI`. This is not Jordan: every operator commutes with `L`, and
an explicit hyperbolic family supplies distinct positive fundamental
symmetries. The failure is non-uniqueness rather than nonexistence, matching
the distinction already learned in the D1 toy audit.

## What was learned relative to the previous kill

The scalar-sign test failed because it demanded that the old `P` continue to
act diagonally on `(q0,qm,theta)`. The Hessian calculation instead lets the
eigenvectors and grading move with the action. At a generic interacting point,

\[
 [P,L(u)]\ne0,
\]

but `[C(u),L(u)]=0`. The apparent conflict is therefore resolved without
weakening either result:

- old result: the fixed multiplicative parity route is dead;
- new result: a zero-parameter field-mixing spectral route survives locally.

That is exactly the kind of constructive response a scoped kill should
generate.

## Seven-axis audit

| layer | disposition |
| --- | --- |
| Layer 0 | background Hessian C, nonlinear classical symmetry and quantum state-space C separated |
| L1 source | `SOURCE-SILENT` for Weinstein; Mannheim method precedent already primary-checked |
| L2 algebra | exact Hessian, discriminant, C, C1, constraint rank and exceptional strata |
| L3 geometry | selected observed TT carrier at constant scalar background; full ambient field bundle open |
| L4 variation | interaction enters through the exact second variation of the written cubic |
| L5 covariance/BV | two TT even-BV classes imported; complete interacting BV quotient open |
| L6 analytic | finite background matrix only; common nonlinear/Fock domain and uniform boundedness open |
| L7 physics | positive tree/background majorant on one component; loop/UV/unitarity claim absent |

## Constraint and datum accounting

- New fitted coefficients: zero; existing `alpha`, `b`, `c` and the chosen
  background value are supplied to this calculation.
- First-order C coefficients: four.
- Independent linear constraint rank: four.
- Residual first-order freedom: zero.
- P1/P2/P3 used: none.
- Global continuous, function-valued and discrete residue: unchanged.

## Hostile boundary and next gate

This result must not be summarized as “the interacting C-operator is built.”
The honest statement is:

> The first action-owned cubic admits a unique positive spectral C for its
> fixed-background TT Hessian on the component connected to the free theory.

Still open:

1. include scalar fluctuations and the complete cubic vertex bank, then test
   whether a nonlinear field-space or quantum state-space C closes;
2. place that operator on the common interacting BV/Green/Fock domain and run
   the W132/H59 amplitude and loop criteria;
3. separately globalize the mixed super-IG bracket; and
4. separately derive or supply the normalized covariant observer functional
   required by the global dark-energy horn.

P1/P2/P3 remain unused. Curt remains formally separate. No canon, Lane-count,
claim-status or public-posture change is made.

The July D1 toy's separate 192-dimensional record-sector lift also remains
open; this two-dimensional gravitational TT construction does not discharge
it.

## Reproduction

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/first_perturbative_background_c_operator_probe.py
DOT_SAGE=/private/tmp/gu-first-background-c-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/first_perturbative_background_c_operator_independent.sage
```
