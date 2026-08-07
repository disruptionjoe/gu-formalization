---
artifact_type: conditional_build_result
created: 2026-08-07
status: SOURCE_NATIVE_POINTWISE_VARPI_LIFT_EXACT__SOURCE_SELECTION_AND_GLOBAL_SPENCER_EULER_OPEN
source_return: SOURCE-CONFIRMS__FIXED_EPSILON_VARPI_TRANSLATION_AND_ENDPOINT_FA__SOURCE-CORRECTS__VARPI_TANGENT_IS_DELTA_T_DELTA_A_NOT_DELTA_B__SOURCE-SILENT__COVARIANT_GRAPH_LIFT_GLOBAL_INTEGRABILITY_AND_EULER_DESCENT
ledger: lab/process/conditional-physics-ledger-v0.56.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected source-varpi / Cartan composition

## Result in plain English

The source-native local tangent exists, and it carries all four missing
pointwise directions exactly. The important correction is **which connection
moves**.

Weinstein's displayed translation variation holds `epsilon` fixed and varies
`varpi`. In two-connection coordinates this is

```text
delta B = 0,
delta T = alpha,
delta A = alpha.
```

It is not the `delta B` label used in v0.55. But the endpoint curvature obeys

```text
F_A = F_B + D_B T + T wedge T,
```

so its derivative contains `[T_*,alpha]`. At the selected nonzero background

```text
T_* = -(kappa_1/312) Phi1,
```

this is a signed and scaled copy of the same invertible Cartan/Spencer map.
Composing the source tangent with the four v0.55 Koszul inverses gives exact
local lifts with supports `57,34,34,34`, rank four, and coefficientwise
reconstruction of all `117` transverse coefficients. At fixed background and
fixed selected operator, the lift has zero coefficient freedom.

This closes **pointwise source-coordinate realizability**. It does not prove
that the source selects this lift, that it varies covariantly with the four
observation/graph columns, that its jets integrate globally, or that the
first-action Euler and presymplectic classes survive. Those are now the
sharper next gate.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| fixed-epsilon translation | `delta B=0`, `delta T=alpha`, `delta A=alpha` | a variation of the gauge-rotated Levi-Civita reference |
| tilted epsilon graph | `delta B=D_B zeta`, `delta T=-D_B zeta`, `delta A=0` | the independent translation direction |
| Cartan owner | `[T_*,alpha]` inside `delta F_A` | `[delta B,T_*]` as a source-coordinate statement |
| source tangent space | full adjoint-valued one-forms, including the real `so(7,7)` bivector subspace | a source-selected four-column graph law |
| pointwise lift | four exact values of `alpha` at a background point | a covariant first-jet morphism over the observation atlas |
| zero freedom | uniqueness after the four target columns and `T_*` are fixed | derivation of those target columns from the full action |
| raw endpoint residual | derivative of the `F_A` term in `Upsilon` | first-action Hessian, Euler covector and preboundary class |

This corrects the owner label without retracting the v0.55 algebra: its
Cartan/Spencer isomorphism remains exact. The correction is that the source
uses the same algebra through endpoint motion `delta A=alpha`, not through
reference motion `delta B=alpha`.

## Exact construction

Let

\[
K(\alpha)=[\alpha,\Phi_1]
\]

denote the normalized Cartan map certified in v0.55. With

\[
T_*=t\Phi_1,\qquad t=-\kappa_1/312\ne0,
\]

the algebraic part of the fixed-epsilon endpoint response is

\[
[T_*,\alpha]=-tK(\alpha).
\]

For each transverse target `R_j`, let `omega_j=K^{-1}(R_j)` be the exact
v0.55 Koszul preimage. Then

\[
\alpha_j=-t^{-1}\omega_j
\]

satisfies

\[
[T_*,\alpha_j]=R_j
\]

coefficientwise. The executable uses `kappa_1=1`, hence `t=-1/312`, and
checks all four columns exactly over the rationals. Scaling does not change
their supports or rank. Invertibility of `K` proves uniqueness at this grade.

The negative control is the tilted tangent. When

\[
(\delta B,\delta T)=(D_B\zeta,-D_B\zeta),
\]

the endpoint tangent is zero. It cannot be silently substituted for the four
nonzero independent-`varpi` lifts.

## Constraint-surplus accounting

No new field, parameter, sign or external datum is charged here. `varpi` is
already a source field, and `alpha` is a test direction in its tangent space.
Once the selected background and four target columns are held fixed, the
invertible Cartan map leaves zero coefficient freedom.

That is not yet a positive global surplus claim. The missing covariant graph
morphism may impose transition, Spencer, observation and action constraints
that the four pointwise columns do not satisfy. The next swing must count
those independent conditions before calling the lift constructed globally.

## Source return

The 2021 action explicitly varies `varpi+s alpha` at fixed `epsilon`, and its
displayed residual uses the endpoint curvature `F_A`. The source-native
distortion tangent `delta T=alpha-D_A zeta` was already reconstructed and
tested in B2C15P. The K77 source-normalization work already places the 91
bivector generators inside the real adjoint carrier.

```text
SOURCE-CONFIRMS:
  fixed-epsilon varpi translation, full adjoint one-form carrier, endpoint
  F_A residual, and the tilted connection-difference grammar.

SOURCE-CORRECTS:
  an independent varpi tangent is delta T=delta A=alpha with delta B=0;
  it is not a reference-connection delta B tangent.

SOURCE-SILENT:
  the selected four-column covariant graph lift, its constraint surplus,
  Spencer/atlas integrability, global admissible domain and Euler descent.
```

The standard two-connection endpoint identity and its linearization are
repository-derived connection calculus compatible with the source, not a
quotation of a missing formula.

## Specialist and hostile review

- **Differential geometry:** the fixed-reference and endpoint connections are
  now correctly separated; the endpoint derivative supplies the same Cartan
  map with the opposite bracket order.
- **Representation theory:** the `so(7,7)` bivector subspace is a real
  91-dimensional adjoint subspace of the source's full matrix-adjoint carrier;
  this does not make every full-adjoint component geometric torsion.
- **Variational PDE / hyperbolic equations:** the pointwise lower-order owner
  does not change the q-exact principal symbol, characteristic variety, or
  hyperbolic domain.
- **Symplectic geometry:** no Euler one-form, Green identity, presymplectic
  current, characteristic quotient or BFV class follows from a pointwise
  tangent match. Those must be recomputed after the graph lift is globalized.
- **Krein/operator theory:** no positivity, self-adjoint extension or common
  closed domain is inferred.
- **Source criticism:** fixed-epsilon translation and endpoint `F_A` are
  source-explicit; the four-column lift is a conditional repo construction.
- **Repo archaeology:** B2C15P had already built `delta T=alpha-D_A zeta`,
  B2C6 had already built the endpoint transgression identity, and v0.55 had
  already built the inverse. This swing composes them instead of repeating
  any one calculation.

Both two-sided hostile charges fire. The summary-overreach charge rejects
"the actual global varpi normal jet is finished." The superseded-object charge
rejects further attempts to source the transverse response from Levi-Civita
`delta B` or another generic carrier search.

## Progress and fences

```text
Ledger v0.56 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - source fixed-epsilon tangent typed as delta B=0, delta T=delta A=alpha
  - all four pointwise source-varpi lifts reconstructed exactly
  - local lift uniqueness and zero coefficient freedom proved at fixed T_*
frontier_conditions_opened: 0
remaining_named_conditions: 3
  - covariant four-column graph morphism plus constraint-surplus count
  - Spencer/atlas integrability and total raw-Upsilon Bianchi/naturality
  - survivor-only Euler/preboundary, null quotient and common domain
```

No verdict, residue, quotient, external datum, canon or public posture moves.
`P1/P2/P3` remain unused. Curt remains formally separate and no third lane is
promoted.

## Next gate

Construct one covariant linear graph morphism from the four physical
soldering/observation columns to the source `varpi` tangent, with the pointwise
values fixed by the four exact lifts. Count independent constraints versus
remaining freedom, then test Spencer compatibility and three-patch descent.
Only surviving columns proceed to total raw-`Upsilon` Bianchi/naturality and
first-action Euler/preboundary/symplectic descent.

The executable probe passes `35/35`, including the immutable v0.55 replay and
planted failures against wrong bracket sign, zero background, tilted-graph
equivocation, Levi-Civita relabeling, parameter inflation and global promotion.
