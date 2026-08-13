---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: COMMON_GRADED_TRACE_AND_RELATIVE_POLARIZATION_EXACT__ACTUAL_BULK_GREEN_KREIN_DOMAIN_UNOWNED
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 common graded trace and boundary-triple skeleton

## Plain English result

The two boundary sectors can live in one mathematically coherent phase space,
even though they require different smoothness. The physical distortion and
its momentum occupy `H^7 x H^-7`; the gauge/ghost sector occupies
`H^8 x H^-8`. Their direct sum has one exact, nondegenerate canonical form,
and the relative `A0` edge-bitorsor changes frames by a cotangent lift that
preserves both the form and its vertical polarization.

That closes the feared regularity mismatch. It does **not** yet give the bulk
Green/Krein domain requested by v0.115. A boundary phase space is the set of
possible boundary values. A bulk domain is a closed class of fields on which
the complete gauge-fixed Euler operator acts and whose boundary values satisfy
the Green identity. The repository owns the former skeleton, but not the
complete operator, its maximal/minimal graph domains, a surjective trace map,
a Green inverse, or a positive physical realization.

## 1. Layer 0

| phrase | object in this result | not the same as |
| --- | --- | --- |
| common trace space | graded direct sum of two Sobolev cotangent pairs | one scalar Sobolev exponent imposed on every field |
| boundary Green form | canonical skew pairing of trace data | a Green operator or inverse |
| maximal boundary data | unrestricted trace quotient candidate | a chosen boundary condition |
| vertical polarization | Lagrangian subspace used to organize boundary variables | an action-selected physical extension |
| boundary condition | a later Lagrangian/closed relation in trace space | the whole BFV phase space |
| bulk Green domain | closed graph realization of a complete bulk operator | finite-mode nondegeneracy of the boundary form |
| positive Sobolev majorant | auxiliary Hilbert topology | the physical Krein form or positivity theorem |
| boundary | thirteen-dimensional boundary of an upstairs region | three-dimensional boundary of observed spacetime |

This distinction matters operationally: imposing a Lagrangian boundary
condition before building BFV would erase the boundary degrees of freedom the
BFV construction is meant to encode.

## 2. Exact graded trace theorem

On a compact smooth thirteen-dimensional boundary `B`, define

\[
\mathcal T_B=
\bigl(H^7(B,E)\oplus H^{-7}(B,E^*)\bigr)_{\rm physical}
\oplus
\bigl(H^8(B,\mathfrak h[1])\oplus H^{-8}(B,\mathfrak h^*[-1])\bigr)_{\rm ghost}.
\]

Give each pair its canonical cotangent form and take their graded direct sum.
At a Fourier weight `w`, the Hilbert majorant is

\[
N_w=\operatorname{diag}(w^{14},w^{-14},w^{16},w^{-16})
\]

with identity factors on the finite fibre. For the block canonical matrix
`Omega`, the probe verifies exactly

\[
\Omega^T N_w^{-1}\Omega=N_w
\]

at every tested mode. Thus the musical map is a strong isometry on the graded
product. By contrast, identifying `H^7` with `H^8` has mode norm growing like
`w`, and the same-positive-regularity `H^7 x H^7` form has an unbounded inverse.
The direct sum is the construction; equality of exponents is neither needed
nor true.

The ordinary trace theorem explains the half-order bulk regularities:
`H^(15/2)` fields trace to physical `H^7`, while `H^(17/2)` gauge/ghost fields
trace to `H^8`. The negative-order entries are continuous cotangent/conormal
duals, not ordinary positive-field traces.

## 3. Relative bitorsor and polarization

For a relative frame transition represented locally by `A`, field coordinates
transform by `A` and their cotangent variables by `A^-T`. The exact block map

\[
S=\operatorname{diag}(A,A^{-T},A,A^{-T})
\]

satisfies `S^T Omega S=Omega`. The vertical momentum/antighost-momentum space
is half-dimensional, equal to its symplectic orthogonal, and is preserved by
`S`. Therefore the v0.115 relative topology and the new graded analytic trace
structure compose without adding a bundle class, coefficient, selector or
physical datum.

This result constructs a polarization but does not select it as a physical
boundary condition. The charged boundary-symmetry rival remains live.

## 4. Boundary-triple readiness and the real obstruction

For a closed bulk operator `D_max`, a boundary-triple route would require a
continuous surjective trace

\[
\gamma:\operatorname{Dom}(D_{\max})\longrightarrow\mathcal T_B,
\]

a Green identity with the form above, and
`Dom(D_min)=ker(gamma)`. Only then could one identify
`Dom(D_max)/Dom(D_min)` with the trace space and classify closed extensions by
appropriate boundary relations.

The repository now owns `T_B`, its form, relative patch descent and a
Lagrangian polarization. It does not own:

- the complete action-owned gauge-fixed bulk linearized operator;
- closed maximal and minimal graph realizations;
- surjectivity of the full graded trace from the bulk domain;
- a common Green inverse or causal/ultrahyperbolic replacement;
- a Krein-positive physical subdomain;
- the coupled bulk BV differential and boundary BFV charge.

The obstruction is not cosmetic. The ordinary ambient Lorentzian Cauchy route
was already killed for signature `(7,7)`, because there is no spacelike
codimension-one hypersurface. The separately constructed observed `X4` defect
domain is not an ambient `Y14` domain. A constrained ultrahyperbolic spectral
projector could be a future route, but it would be a new owned construction and
cannot be inserted by declaration.

## 5. Source return and accounting

```text
SOURCE-CONFIRMS:
  Weinstein explicitly treats the upstairs multiple-time boundary problem as
  unresolved technical debt.

SOURCE-SILENT:
  Sobolev scales, trace triple, graph realizations, Green/Krein domain,
  ultrahyperbolic projector, BV-BFV coupling, contour and measure.
```

```text
new physical fields: 0
new continuous coefficients: 0
new discrete selectors: 0
new bundle classes: 0
new booked quotients: 0
P1/P2/P3 consumed: 0
```

Primary certificate: `40 exact + 11 planted = 51 PASS`.
Independent Sage/FLINT: `14 exact + 5 planted = 19 PASS`.
Predecessor v0.103 mathematics replays `59/59`; v0.115 mathematics replays
`44/44` plus independent `19/19`. Its governance audit correctly rejects the
new v0.116 pointers and is not counted as a regression.

## 6. Progress and next gate

```text
Ledger v0.116 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed: compatibility of the two Sobolev trace scales, and preservation of the
strong graded form/polarization under relative bitorsor patching. Opened as an
explicit owner burden: the `D_max/D_min` graded trace exact sequence for the
complete action-owned bulk operator. Coupled BV--BFV remains the second named
condition.

Next:

`ASSEMBLE_COMPLETE_ACTION_OWNED_GAUGE_FIXED_BULK_LINEARIZED_OPERATOR_ON_A_STATIONARY_BRANCH__PROVE_CLOSED_DMAX_DMIN_GRADED_TRACE_EXACT_SEQUENCE_ON_THE_RELATIVE_EDGE_BITORSOR_OR_KILL__THEN_COUPLE_BULK_BV_TO_BOUNDARY_BFV__KEEP_PHYSICAL_HORN_OPEN`.
