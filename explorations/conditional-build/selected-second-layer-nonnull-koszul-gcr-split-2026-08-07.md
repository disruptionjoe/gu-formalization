---
artifact_type: conditional_build_result
created: 2026-08-07
status: NONNULL_CANONICAL_SPLIT__LAWFUL_CONNECTION_JET_PLUS_NONZERO_TRANSVERSE_COMPLETION_BURDEN
source_return: SOURCE-CONFIRMS__CONNECTION_MINUS_GAUGE_ROTATED_LEVI_CIVITA_AND_FULL_TWO_CONNECTION_ARENA__SOURCE-SILENT__NONNULL_KOSZUL_SPLIT_AND_GCR_REMAINDER_COEFFICIENTS
ledger: lab/process/conditional-physics-ledger-v0.48.json
canon_verdict_change: none
---

# Selected second-layer non-null Koszul/GCR split

## Result in plain English

The previous result said none of the four full corrections could be a
connection-curvature derivative by itself. This wave recovers the largest
canonical connection piece at the timelike rest momentum already used by the
physics calculation.

Each correction splits uniquely into:

1. a lawful `q`-exact, principal-Bianchi-closed connection-curvature jet; and
2. a nonzero transverse remainder that the full moving Gauss-Codazzi-Ricci or
   background geometry must still own.

Across all four graph directions, the connection pieces contain `28` of the
`145` nonzero source coefficients. The transverse completion burden contains
the other `117`. Both families have exact rank four, both have nonzero
selected-Shiab images, and their images sum coefficientwise to the four
required corrections.

This is real construction, but it is not the full source action yet. The
remainder has been typed and counted; it has not been identified with
Weinstein's source-native Gauss, Codazzi or Ricci blocks. The massless/null
branch also remains open because the canonical normalization fails at
`q^2=0`.

```text
connection supports: 7, 7, 7, 7       total 28
transverse supports: 51, 22, 22, 22    total 117
connection family rank: 4
transverse family rank: 4
selected-Shiab reconstruction: exact
null branch: auxiliary-screen dependent
```

## Layer 0

| phrase | object tested | object kept distinct |
| --- | --- | --- |
| `q` | the fixed principal-symbol rest covector already in use | an external datum, field or vacuum choice |
| Koszul split | the canonical algebraic homotopy at non-null `q` | a source-derived moving GCR formula |
| connection part | `q wedge i_v F`, hence `q`-closed | the whole nonlinear connection curvature |
| transverse remainder | `i_v(q wedge F)` | Codazzi/Ricci ownership or a counterterm |
| Bianchi | principal `q wedge F=0` | nonlinear covariant Bianchi with background commutators |
| non-null result | `q^2 != 0` | the null characteristic screen/gauge quotient |

## Exact construction

For non-null `q`, set `v=q-sharp/q-squared`, so `q(v)=1`. The standard Koszul
identity gives

\[
 F=q\wedge\iota_vF+\iota_v(q\wedge F).
\]

At `q=e^0`, the first projector retains exactly the two-form coefficients
whose form pair contains `0`; the second retains the complementary pairs.
The first term is visibly `q`-wedge exact and therefore closed. The second is
`i_v`-transverse. Exact sparse rank and selected-Shiab reconstruction checks
show neither family collapses.

Carrier accounting is also exact. Every connection part has seven mixed
horizontal-normal entries. The time remainder has `15 HN + 36 NN`; each
spatial remainder has `13 HN + 9 NN`. These labels type where the burden
lives. They do **not** identify the entries as Codazzi or Ricci tensors; that
requires the moving embedding and connection formulas.

The null control is decisive. For `q=e^0+e^1`, `q^2=0`, so the metric cannot
supply `v=q-sharp/q-squared`. Two algebraic complements satisfying `q(v)=1`
give different projectors already on `F=e^0 wedge e^2`. A null screen or gauge
quotient must therefore be constructed rather than inferred from this result.

## Source return

Weinstein explicitly uses a full adjoint-valued difference of two connections
and places the gauge-rotated Levi-Civita connection in the contorsion slot.
That confirms the connection/GCR arena and corrects an ordinary-contorsion
reading. The source does not publish this non-null Koszul decomposition, the
`28/117` coefficient split, or the moving GCR/background coefficients.

```text
SOURCE-CONFIRMS:
  full two-connection carrier on Y; gauge-rotated Levi-Civita comparison;
  improved tilted-gauge equivariance as the intended arena.

SOURCE-SILENT:
  non-null Koszul coefficients; GCR ownership of the transverse remainder;
  null screen and completed nonlinear Bianchi identity.
```

## Specialist and hostile review

- **Differential geometry:** the Koszul identity constructs the largest
  canonical non-null connection-exact part, but the transverse carrier must
  not be renamed GCR without the moving embedding formulas.
- **Representation theory:** both four-column families have rank four;
  support counts are not multiplicities or particle counts.
- **Variational PDE / hyperbolic equations:** the timelike rest branch is
  valid, while the null characteristic branch requires a screen/gauge choice.
- **Symplectic geometry:** principal Bianchi closure is an integrability gate,
  not a presymplectic reduction, BV quotient or BFV boundary phase space.
- **Krein/operator theory:** no positivity, self-adjointness or common closed
  domain follows from this finite exact split.
- **Source criticism:** the source confirms the two-connection and
  gauge-rotated-Levi-Civita arena, not the repo-derived coefficients.
- **Repo archaeology:** v0.47's unique preimages and exact selected-Shiab map
  were reused; this wave added a new decomposition rather than recomputing
  the predecessor as substitute work.

## Progress and fences

```text
Ledger v0.48 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - canonical non-null connection projection constructed
  - connection and transverse ranks/supports measured exactly
  - selected-Shiab image recombination proved coefficientwise
frontier_conditions_opened: 2
  - source-native GCR/background ownership of the transverse remainder
  - null screen or gauge quotient
remaining_named_conditions: 5
  - source-native transverse GCR/background owner map
  - null characteristic screen and continuation
  - total nonlinear Bianchi and raw-Upsilon naturality
  - scalar and massless physical constraint quotient
  - coupled fermion Hessian and common domain
```

No scalar pole, cosmological magnitude, physical equation, fifth quotient,
external datum, canon verdict or public posture changes. P1/P2/P3 remain
unused. Curt remains formally separate and no third lane is promoted.

## Next gate

Identify the `117` transverse coefficients with the actual moving
Gauss-Codazzi-Ricci/background blocks supplied by the two-connection geometry,
construct the null screen, and then test the completed packet against total
covariant Bianchi and raw-`Upsilon` naturality. Do not call carrier labels
source ownership and do not continue the non-null normalization through
`q^2=0`.

The executable probe passes `61/61`, including exact null-screen dependence
and planted failures against GCR attribution, datum substitution, split-to-
total promotion, particle-count inference and BV/BFV inflation.
