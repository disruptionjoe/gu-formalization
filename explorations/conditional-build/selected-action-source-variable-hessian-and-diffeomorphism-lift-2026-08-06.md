---
artifact_type: source_variable_hessian_and_principal_diffeomorphism_lift
created: 2026-08-06
status: ZERO_JET_SOURCE_VARIABLE_HESSIAN_EXACT__FULL_I1B_DERIVATIVE_CURVATURE_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CORRECTS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_source_variable_hessian_probe.py
registry: lab/process/selected-action-source-variable-hessian-and-diffeomorphism-lift.json
---

# Selected-action source-variable Hessian and diffeomorphism lift

## Result first

The selected zero-jet augmented-torsion summand now has its exact
source-variable Hessian on the actual variables `(g,varpi)`. It closes both
principal Ward block equations on timelike, spacelike and null covectors with
no new field, fitted coefficient or external datum.

The correction is structural. The selected background is
`T*=t Phi1`, where `Phi1` is the tautological identity. Moving only its
covector slot produces the rank-four symbol used in v0.32, but moving its
internal slot at the same time cancels that response exactly. The field that
moves independently is instead the connection `varpi`, while

\[
 T=\varpi-B_{LC}(g).
\]

If `L` is the principal symmetric-frame spin Levi-Civita map and `K` is the
exact selected torsion Hessian on the 24-dimensional horizontal Lorentz
connection carrier, the source tangent and Hessian are

\[
 J=(-L,I_{24}),\qquad
 H_0=J^T KJ=
 \begin{pmatrix}
 L^TKL&-L^TK\\
 -KL&K
 \end{pmatrix}.
\]

The principal diffeomorphism lift is `(D,LD)`. Hence `J(D,LD)=0` and both
block Ward equations close identically. The coupled 34-dimensional Hessian
has rank 24 and nullity ten. Four null directions are the diffeomorphism
image. The other six are genuine zero-jet blindness: the torsion difference
is constant along the full graph `(h,Lh)`.

This is not the full first-order action `I1B`. Its curvature,
`d_B T/2`, density, moving pairing and observation terms must lift those six
nongauge null directions while retaining the four gauge directions. That
six-versus-four test is now the next decisive gate.

## Plain English

The previous wave proved that including a connection-like field could repair
the metric-only gauge mismatch, but it used a simplified model of how that
field moved. The source action tells us the actual variables: the metric and
an independent connection, whose difference from the metric-built
Levi-Civita connection is the augmented torsion.

When we differentiate that exact difference, the cross terms are no longer
arbitrary. They are fixed by the same torsion term, and they cancel the four
gauge directions exactly. The remaining six flat directions are useful: they
tell the next wave precisely what the derivative and curvature terms must do.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| selected background | `T*=t Phi1` with both tautological slots co-moving | a covector whose internal slot is frozen |
| source variables | metric `g` and independent connection `varpi` | metric plus an independently supplied torsion tensor |
| augmented torsion tangent | `delta T=delta varpi-L delta g` | the connection Lie derivative by itself |
| zero-jet Hessian | Hessian of the selected algebraic torsion summand | the Hessian of full first-order `I1B` |
| ten-dimensional radical | constant-`T` graph `(h,Lh)` | ten gauge directions or a BV quotient |
| six extra nulls | nongauge part of zero-jet blindness | six parameters or six physical modes |

This also scopes v0.32. Its `10+16`, rank-98/affine-198 system remains a valid
diagnostic completion problem on its deliberately reduced carrier. It is not
the source-variable Hessian and should not remain the construction target.

## Source collision

The primary-source pack writes the augmented torsion as an independent
connection minus a gauge-rotated reference connection and places both
`F_B` and `d_B T/2` in the first-order action. Therefore:

```text
SOURCE-CORRECTS: use (g,varpi), T=varpi-B_LC(g), and the complete source lift
SOURCE-SILENT:   the full nonlinear/global Hessian, reduced phase space,
                 Green domain, BFV class and observed physics
```

The source fixes the object and the action architecture. It does not prove
the finite ranks or the full action result.

## Exact construction

On each causal representative, the metric symbol `D` has rank four, the spin
Levi-Civita map `L` has rank nine and the induced independent-connection lift
`LD` has rank three. Nevertheless the stacked generator `(D,LD)` has rank
four. The selected torsion Hessian `K` is symmetric, nondegenerate and has
inertia `(12,12,0)`.

The source-variable blocks are action-derived:

\[
 H_{gg}=L^TKL,\quad H_{g\varpi}=-L^TK,\quad
 H_{\varpi g}=-KL,\quad H_{\varpi\varpi}=K.
\]

Exact rational computation gives, on timelike, spacelike and null covectors:

- `rank H_0=24`, `nullity H_0=10`, inertia `(12,12,10)`;
- `rank(D,LD)=4`;
- `H_0(D,LD)=0=(D,LD)^T H_0`;
- both metric and connection Ward block equations vanish coefficientwise;
- `ker H_0` is exactly the rank-ten graph `(h,Lh)`; and
- its quotient by the gauge image has dimension six at this symbol grade.

The metric restriction `L^TKL` reproduces the v0.30 stationary metric block
exactly, including its rank-three isolated Ward residual. Thus the old result
was correct while holding `varpi` fixed; the full source tangent explains why
that restriction is not gauge closed.

## Symplectic interpretation

Gauge vectors must lie in the radical of the on-shell presymplectic form.
This zero-jet Hessian passes the necessary principal precursor: its complete
four-dimensional diffeomorphism image is radical. But the ten-dimensional
Hessian kernel is not yet a characteristic distribution of the full action.
The six extra directions could be lifted, constrained or retained only after
the derivative Green current, equations and boundary quotient are assembled.
No reduced covariant phase space or Hamiltonian observable is claimed.

## Corrected queue

1. Differentiate the complete first-order `I1B` on `(g,varpi)` including
   curvature, `d_B T/2`, moving density/pairings and observation.
2. Test whether the completed principal Hessian retains exactly the four
   gauge null directions while lifting the six zero-jet nongauge directions.
3. Derive the corresponding Euler/Green identity and only then build the odd
   BV and unrestricted BFV quotient on a common analytic domain.
4. Keep `I2B <-> ||II||^2` as the separate `LT-GR3` owner-map gate.

## Ledger v0.33

```text
Ledger v0.33 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances move. Verdicts, reason kinds, revival triggers, residue,
quotient count and P1/P2/P3 do not.

## Seven-axis disposition

- **Layer 0:** tautological `T*`, independent `varpi`, augmented torsion and
  full `I1B` are separated.
- **L1 syntactic:** the source tangent, four Hessian blocks and full lift are
  explicit.
- **L2 type:** `L` maps metric perturbations to the same 24-dimensional
  horizontal Lorentz connection carrier as `delta varpi`.
- **L3 algebraic:** ranks, inertias, kernels and both Ward equations are exact
  on all three causal representatives.
- **L4 geometric:** the local symmetric-frame principal lift is exact; global
  bundle descent remains open.
- **L5 variational/symplectic:** the zero-jet action-derived Hessian closes,
  but the full Euler/Green/BV/BFV class remains open.
- **L6 analytic:** no closed Krein/Green or hyperbolic domain is claimed.
- **L7 physical:** no Einstein recovery, cosmology, particle, Q1 or unitarity
  claim is made.

## Constraint fence

```text
new fields: 0
new coefficients: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.
