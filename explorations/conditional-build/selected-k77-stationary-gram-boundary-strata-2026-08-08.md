---
title: "Selected K77 stationary Gram and boundary strata"
status: conditional_build
doc_type: exploration
created: "2026-08-08"
lane: "1"
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 stationary Gram and boundary strata

## Result

The existing common principal derivative is a rectangular map from ten metric
and twenty-four connection variables into the residual carrier. It therefore
is not itself a self-adjoint operator. On the stationary zero-residual branch,
however, the norm-square action has the well-typed 34-by-34 equation-dual
symbol

\[
H_2(q)=A(q)^T K_{\mathrm{loc}}A(q).
\]

The exact raw map has rank 22 in timelike, spacelike and null directions. Its
Gram ranks are respectively 22, 22 and 14, with inertias

| stratum | rank A(q) | rank H2(q) | inertia (+,-,0) | doubled Green quotient |
|---|---:|---:|---:|---:|
| timelike | 22 | 22 | (12,10,12) | 44 |
| spacelike | 22 | 22 | (13,9,12) | 44 |
| null | 22 | 14 | (8,6,20) | 28 |

Thus the boundary symbol is genuinely stratified: at null covectors eight
additional directions in the residual image are isotropic for the induced
pairing. A fixed-rank trace quotient cannot be inferred across the
characteristic boundary.

This closes a partial second-action symbol calculation. It does **not** build
the full common GU domain. The independent epsilon columns, the first action
on the same stationary background, the edge-distortion trace soldering map,
the tangential/collar operator, a maximal closed domain and the odd BFV charge
remain unbuilt.

## Layer 0

| object | type | disposition |
|---|---|---|
| raw `D Upsilon` | rectangular residual response, 34 fields to 1,470 owned response coordinates | not self-adjoint |
| `A^T K_loc A` | symmetric covector-valued second-action principal symbol on the 34-field tangent | computed here |
| field-valued Hessian | requires a field-space Riesz map | open; unnecessary for the covector equation itself |
| full selected action | first action plus residual norm-square, on one stationary background and complete field tangent | open |
| Green trace quotient | quotient of the doubled partial symbol by its radical | dimensions 44/44/28, diagnostic only |
| edge phase space | distortion/momentum carrier with `H7 x H-7` completion | carrier identification open |

The calculation never identifies the trace quotient with the edge carrier.
Doing so would repeat the familiar error of treating matching dimensions or
regularities as an object-level map.

## Exact construction

The metric bank is replayed from the actual K77 common residual-coordinate
probe. The connection bank is independently constructed from the 24
horizontal bivector-valued one-form columns. Their directional ranks are
`9+13=22` in all four coordinate directions. For the canonical timelike,
spacelike and null covectors, exact congruence elimination gives the inertias
above. Exact characteristic polynomials and an independent Sage/FLINT route
guard against numerical rank thresholds.

The doubled Green form is

\[
\Omega_q=\begin{pmatrix}0&H_2(q)\\-H_2(q)&0\end{pmatrix}.
\]

Its reduced ranks are twice the Gram ranks, giving 44 on both non-null strata
and 28 on the null stratum. The null rank drop is not a gauge quotient: no
source-derived tangent/BV differential has yet identified the extra null
radical.

## Analytic and symplectic return

The compact-boundary `H7 x H-7` completion has the correct strong cotangent
regularity for this finite-fibre Green pairing; `H7 x H7` remains weak. This
is an analytic compatibility statement, not a proof that the partial Gram
trace variables are the previously constructed edge distortion and momentum.

The symplectic lens therefore refuses promotion of a sixth booked quotient.
A physical preboundary form requires the explicit trace soldering/Legendre
map from complete selected-action fields to edge variables. The analytic lens
also requires a tangential operator, collar model and maximal domain; a
principal normal matrix alone does not supply any of these.

## Specialist pre-assessment and hostile return

- **Variational/PDE:** form the action Hessian, not a fictitious adjoint of a
  rectangular residual map. Keep the first and second action parents separate
  until evaluated on one background.
- **Krein/operator:** the exact inertia is indispensable, but a finite matrix
  quotient is not a closed infinite-dimensional domain.
- **Microlocal:** the null rank drop forces a stratified characteristic
  analysis; do not impose one constant quotient rank.
- **Symplectic geometry:** identify the boundary variables by a Legendre or
  soldering map before calling the reduced Gram form the BFV phase space.
- **Real Clifford:** the calculation is on the selected Spin-native K77
  carrier. It neither promotes full `U(64,64)` nor collapses the two
  `U(32,32)` Weyl-half comparator.
- **Complex/path-integral:** no complexification is used to decide a
  signature-sensitive fact; measure and reflection-positivity questions are
  downstream of a complete real domain.
- **Source:** Weinstein's norm-square/adjoint arena supports forming this
  second variation. The source is silent on the field Riesz, maximal domain,
  trace soldering and odd BFV completion.
- **Accounting:** the new trace quotients are unbooked diagnostics; verdicts,
  residue, five scoped quotients and P1/P2/P3 do not move.

## Seven axes and Layer 0

Layer 0 passes only for the partial metric-plus-varpi second-action symbol.
L1 source locus is `SOURCE-CONFIRMS` for the norm-square/adjoint arena and
`SOURCE-SILENT` for the missing analytic objects. L2 typing passes with the
rectangular/square split. L3 exact construction passes. L4 independent
Sage/FLINT reconstruction passes. L5 negative controls reject fixed rank and
full-domain promotion. L6 compatibility passes only at Sobolev regularity.
L7 downstream physical/BFV interpretation remains open.

## Progress and next gate

Ledger v0.104 remains `82/82`, with verdict counts `32/19/26/5`, residue
`84..86`, nine forks and five booked scoped quotients. Four named conditions
close and one opens: the common normal bank, exact stationary Gram, causal
rank/inertia and Sobolev regularity type close; null-stratum carrier descent
opens explicitly.

Next construct the independent epsilon residual columns and recompute the
first and second action on one stationary background. Then build the edge
trace soldering map and tangential/collar maximal domain. Only after those
steps should the odd BFV/BRST charge and CME be attempted. The charged horn,
edge-torsor topology and all three action parents remain live.

## Receipts

- Primary: `tests/channel-swings/selected_k77_stationary_gram_boundary_strata_probe.py`
  — 60/60.
- Independent: `tests/channel-swings/selected_k77_stationary_gram_boundary_strata_independent.sage`
  — 34/34.
- Hostile review:
  `lab/process/hostile-reviews/2026-08-08-selected-k77-stationary-gram-boundary-strata-review.md`.
